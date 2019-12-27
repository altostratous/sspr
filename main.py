from crawling import crawl


if __name__ == '__main__':
    print(
        len(
            crawl(list(
                map(
                    lambda l: l.replace('\n', ''),
                    open('resources/start.txt')
                )
            ))
        )
    )
