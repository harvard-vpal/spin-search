# SPIN API client

Python API client to the infoEd SPIN funding opportunities search engine

## About
SPIN (https://spin.infoedglobal.com) is a web-based search tool that allows researchers, faculty, and administrators to search for research funding opportunties.

This Python library provides a Python interface to the SPIN search interface for programmatic access in applications.

## Usage
Institutional credentials provided by infoEd are required to use the API client:
* Public key
* Signature
* Institution code

Contact infoEd (https://infoedglobal) to obtain credentials for your institution.

Using the Python client:
```python
import spinsearch

public_key = ...
signature = ...
institution_code = ...

spin = spinsearch.client(public_key, signature, institution_code)
# basic example
spin.search(['oceanography'])
# multiple keywords
spin.search(['oceanography', 'genetics'])
# search options, e.g. AND vs OR (default) search logic for multiple keywords
spin.search(['oceanography', 'genetics'], 
    how='and', max_results=5, columns=['id','objective','prog_title'])
# fetch resources by list of internal SOLR ids if known
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

See the SPIN widget documentation for more info on columns and column options: https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm


## Tests
Use pytest to run tests (see `tests/`). Tests assume credentials are available as environment variables `SPIN_PUBLIC_KEY`, `SPIN_SIGNATURE`, and `SPIN_INSTITUTION_CODE`.

Usage:
```
SPIN_PUBLIC_KEY=xxx-xxx-xx SPIN_SIGNATURE=xxxxxxx SPIN_INSTITUTION_CODE=xxx pytest
```

## References
* SPIN search page: https://spin.infoedglobal.com
* SPIN widget documentation: https://vpal-public.s3.amazonaws.com/spin/spin-documentation.min.htm
