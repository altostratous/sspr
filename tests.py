import json
from unittest import TestCase

from crawling import fetch_document


class TestFetch(TestCase):

    def test_fetch(self):
        self.maxDiff = None
        with open('resources/sample.json') as sample_document_json_file:
            sample_document = json.load(sample_document_json_file)
            fetched_document = fetch_document(sample_document['id'])
            self.assertDictEqual(sample_document, fetched_document)
