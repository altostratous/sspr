from time import sleep
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from caching import dict_pickle_cached


@dict_pickle_cached()
def fetch_url(url: str):
    print(url)
    response = requests.get(url)
    assert response.ok
    sleep(0.1)
    return response.content.decode(errors='replace')


def fetch_document(document_id: str):
    bs = BeautifulSoup(fetch_url(document_id))
    references_element = bs.find(name='div', attrs={'id': 'references'})
    data = {
        'id': document_id,
        'title': bs.find(name='meta', attrs={'name': 'citation_title'}).get('content'),
        'abstract': bs.find(
            name='meta', attrs={'name': 'description'}
        ).get('content')[len('Abstract '):].replace('\xa0', ' '),
        'date': bs.find(name='meta', attrs={'name': 'citation_publication_date'}).get('content'),
        'authors': list(
            map(
                lambda e: e.get('content'),
                bs.find_all(name='meta', attrs={'name': 'citation_author'})
            )
        ),
        'references': list(
            map(
                lambda e: urljoin(document_id, e.get('href')),
                references_element.find_all(
                    name='a', attrs={'data-selenium-selector': 'title-link'}
                ) if references_element else []
            )
        )
    }
    return data


def crawl(queue: list, crawled_set: set=set(), limit=5000):
    if len(queue) == 0:
        return []
    first, rest = queue[0], queue[1:]
    fetched_document = fetch_document(first)
    crawled_set.add(fetched_document['id'])
    print('crawled:', len(crawled_set))
    references_to_crawl = fetched_document['references'][:5]
    fresh_references_to_crawl = set(references_to_crawl) - crawled_set
    rest.extend(fresh_references_to_crawl)
    result = crawl(rest, crawled_set, limit)
    result.insert(0, fetched_document)
    return result
