import sys
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

queryTerm = "trail"
ix = open_dir("indexdir")
with ix.searcher(weighting=scoring.Frequency) as searcher:
    queryParser = QueryParser("description", ix.schema)
    query = queryParser.parse(queryTerm)
    results = searcher.search(query, limit=10)
    print(results)
    for i in results:
        print(i['title'])
