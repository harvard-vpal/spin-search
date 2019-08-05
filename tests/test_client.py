"""
Usage:
SPIN_PUBLIC_KEY=xxx-xxx-xx SPIN_SIGNATURE=xxxxxxx SPIN_INSTITUTION_CODE=xxx pytest
"""

import os
import spinsearch

public_key = os.environ['SPIN_PUBLIC_KEY']
signature = os.environ['SPIN_SIGNATURE']
institution_code = os.environ['SPIN_INSTITUTION_CODE']


def test_client():
    spin = spinsearch.client(public_key, signature, institution_code)
    results = spin.search(['science'], max_results=1)
    assert results


def test_pagination():
    spin = spinsearch.client(public_key, signature, institution_code)
    results = spin.search(['science'], max_results=150)
    assert results


def test_multiple_terms():
    spin = spinsearch.client(public_key, signature, institution_code)
    results = spin.search(['science', 'arts'], max_results=10)
    assert results


def test_multiple_terms_and():
    spin = spinsearch.client(public_key, signature, institution_code)
    results = spin.search(['science', 'arts'], max_results=10, how='and')
    assert results


def test_max_results():
    spin = spinsearch.client(public_key, signature, institution_code)
    results = spin.search(['science'], max_results=5)
    assert len(results) == 5
