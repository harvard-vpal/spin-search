# SPIN API client

Python API client to the infoEd SPIN funding opportunities search engine

## About
[SPIN](https://spin.infoedglobal.com) is a web-based search tool that allows researchers, faculty, and administrators to search for research funding opportunties.

This Python library provides a Python interface to the SPIN search interface for programmatic access in applications.

## Getting started

### Requirements
Institutional credentials provided by infoEd are required to use the API client:
* Public key
* Signature
* Institution code

Contact [infoEd](https://infoedglobal.com) to obtain credentials for your institution.

### Installation
Pip install directly from Github repo: https://pip.pypa.io/en/stable/reference/pip_install/#git


### Usage
Using the Python client:
```python
import spinsearch

public_key = ...
signature = ...
institution_code = ...

spin = spinsearch.client(public_key, signature, institution_code)

results = spin.search(['oceanography'])
# results is a list of dictionaries
```

Example output:
```python
# >> results
[
    {
        'id': '070334',
        'prog_title': 'Medwin Prize in Acoustical Oceanography',
        'cfda': None,
        'synopsis': '<p>The Medwin Prize in Acoustical Oceanography was established in 2000 to recognize a person for the effective use of sound in the discovery and understanding of physical and biological parameters and processes in the sea. </p>',
        'objective': '<p>The Medwin Prize in Acoustical Oceanography recognizes a person for the effective use of sound in the discovery and understanding of physical and biological parameters and processes in the sea.&nbsp; The recipient will be expected to attend the award ceremony and to deliver an &ldquo;Acoustical Oceanography Prize Lecture&rdquo; at the spring ASA meeting in Chicago, Illinois (13 May 2020). </p>',
        'sponwebsite': 'https://acousticalsociety.org/',
        'spon_prog': None,
        'spon_name': 'Acoustical Society of America',
        'applicant_type': ['Researcher or Investigator'],
        'geographic': ['United States'],
        'target': None,
        'keyword': ['Oceanography', 'Acoustics'],
        'deadline_date': ['23-Sep-2019'],
        'contact': 'Elaine Moran, Office Manager',
        'contact_tel': '516-576-2360',
        'contact_email': 'asa@acousticalsociety.org',
        'programurl': 'https://acousticalsociety.org/prizes/',
        'sponsor_type': 'Professional/Academic Assoc &amp; Soc.'
    },
    ...
]
```

### Advanced usage:

```python
# specify maximum number of results to return
spin.search(['oceanography'], max_results=5)

# multiple keywords
spin.search(['oceanography', 'genetics'])

# search options, e.g. AND vs OR (default) search logic for multiple keywords
# default behavior is how='or'
spin.search(['oceanography', 'genetics'], how='and')

# directly fetch resource metadata with list of known SOLR ids
spin.fetch_by_ids(['123456', '234567'])
```

Columns to return can be passed in through the `columns` keyword argument in a search query.

Avaiable columns include:
```
[
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
```

See the [SPIN widget documentation](https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm
) for more info on columns and column options.

## Tests
Use pytest to run tests (see `tests/`). Tests assume credentials are available as environment variables `SPIN_PUBLIC_KEY`, `SPIN_SIGNATURE`, and `SPIN_INSTITUTION_CODE`.

To run tests (ensure variable values are provided):
```
SPIN_PUBLIC_KEY=xxx-xxx-xx SPIN_SIGNATURE=xxxxxxx SPIN_INSTITUTION_CODE=xxx pytest
```

## References
* SPIN search page: https://spin.infoedglobal.com
* SPIN widget documentation: https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm
