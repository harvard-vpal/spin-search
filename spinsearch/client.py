import json
import requests


class SpinClient:
    def __init__(self, public_key, signature, institution_code, default_columns=None):
        """
        Client to interact with SPIN API
        https://spin.infoedglobal.com
        https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm

        Usage:
        client = SpinClient(public_key, signature, institution_code)
        client.search(['oceanography'])
        client.search(['oceanography', 'genetics'], how='and', max_results=5)
        client.fetch_by_ids(['123456', '234567'])

        :param public_key: e.g. ABC01DE2-12F3-4567-A8B9-123456789ABC
        :param signature: e.g. 123456789abcdef
        :param institution_code: ABCDEF
        :param default_columns: list of columns to return by default (optional)
        :type default_columns: list of strings
        """
        
        self.url = 'https://spin.infoedglobal.com/Service/ProgramSearch'
        self.public_key = public_key
        self.signature = signature
        self.institution_code = institution_code

        # additional columns that get returned without explicitly specifying in request: contact, contact_email, contact_tel, deadline_date
        # see https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm for column documentation
        self.default_columns = default_columns or [
            'applicant_type',
            'cfda',
            'geographic',
            'id',
            'keyword',
            'objective',
            'prog_title',
            'programurl',
            'project_location'
            'project_type',
            'spon_name',
            'spon_prog',
            'sponsor_type',
            'sponwebsite',
            'synopsis',
            'target'
        ]
        
    def _fetch_page(self, **params):
        """
        Fetch a single page using params
        :param params: keyword arguments corresponding to param arguments to pass to SPIN http request
        """
        r = requests.get(self.url, params=params)
        if not r.ok:
            raise Exception(r.text)
        return json.loads(r.text.strip('()'))

    def search(self, keywords, columns=None, max_results=None, how='or'):
        """
        :param keywords: list of keywords
        :param columns: list of columns to include; if not provided, uses the default columns set in client instance
        :param max_results: optional, maximum number of results to return
        :param how: optional, specify whether for multiple keywords to use OR or AND logic
        """
        # search logic determines query delimiter between multiple keywords
        if how == 'and':
            query = '+'.join(keywords)
        else:
            query = ' or '.join(keywords)
        
        params = dict(
            # credentials
            PublicKey=self.public_key,
            signature=self.signature,
            InstCode=self.institution_code,
            # query
            keywords=query,
            # settings
            pageSize=50,
            responseFormat='JSON',
            isCrossDomain='true',
            callback='',
            columns=','.join(columns or self.default_columns),
        )
        
        # iterate through pages and construct result set
        page_number = 1
        page = self._fetch_page(**params, pageNumber=page_number)
        results = page['Programs']
        while page['PageNumber']<page['NumberOfPages']:
            # return results if at or over the maximum number of results allowed
            if max_results is not None:
                if len(results) >= max_results:
                    return results[:max_results]
            # fetch next page of results
            page_number += 1
            page = self._fetch_page(**params, pageNumber=page_number)
            results.extend(page['Programs'])
            
        return results

    def fetch_by_ids(self, ids, columns=None):
        """
        Retrieve results directly using list of SOLR ids
        
        :param ids: list of ids, e.g. ['025254', '039997']
        :type ids: list of strings
        """
        query = [f'[SOLR]id:{id}' for id in ids]
        return self.search(query, columns=columns, how='or')
