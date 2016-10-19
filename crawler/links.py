def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    print(result)
    page = result.text
    #print(page)
    doc = soup(page)
    print(doc)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Link in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()
