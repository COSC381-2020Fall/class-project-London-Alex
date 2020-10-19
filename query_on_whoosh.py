import sys
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

def performQuery(queryTerm, pageNum, itemsPerPage):
    ix = open_dir("indexdir")
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        queryParser = QueryParser("description", ix.schema)
        query = queryParser.parse(queryTerm)
        results = searcher.search_page(query, pageNum, pagelen=itemsPerPage)
        print(results)
        for i in results:
            print(i['title'])

if __name__ == '__main__':
    queryTerm = sys.argv[1]
    pageNum = int(sys.argv[2])
    itemsPerPage = int(sys.argv[3])
    performQuery(queryTerm, pageNum, itemsPerPage)
