import json
from networkx import DiGraph, pagerank

import numpy
from crawling import crawl

if __name__ == '__main__':
    pages = crawl(list(map(
        lambda l: l.replace('\n', ''),
        open('resources/start.txt')
    )))

    json.dump(pages, open('dump.json', mode='w'))

    page_ids = {}
    id_pages = {}
    for page in pages:
        new_id = len(page_ids)
        page_ids[page['id']] = new_id
        id_pages[new_id] = page['id']

    graph = DiGraph()
    for i in range(len(pages)):
        graph.add_node(i)
    for page in pages:
        reference_ids = [
            page_ids[reference_id] for reference_id in page['references'] if reference_id in page_ids
        ]
        for reference_id in reference_ids:
            graph.add_edge(page_ids[page['id']], reference_id)

    pr = pagerank(graph, alpha=float(input("Enter alpha: ")))

    top_documents = sorted([(rank, id_pages[node]) for node, rank in pr.items()], reverse=True)[:10]

    print(*top_documents, sep='\n')
