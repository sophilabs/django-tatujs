from bs4 import BeautifulSoup


def extract(document, sources):
    """ Extract the specified sources from the document.
    """
    contents = {}

    soup = BeautifulSoup(document)

    for source in sources:
        contents[source] = unicode(soup.select(source)[0])

    return contents
