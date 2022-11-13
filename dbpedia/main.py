import quepy


dbpedia = quepy.install("dbpedia")


"""
target, query, metadata = dbpedia.get_query("Who is the king of Scotland?")
print(query)
target, query, metadata = dbpedia.get_query("Who is president of France?")
print(query)
target, query, metadata = dbpedia.get_query("Who is queen of England?")
print(query)
target, query, metadata = dbpedia.get_query("Who is the CEO of Sony?")
print(query)
target, query, metadata = dbpedia.get_query("In which state is Frankfurt?")
print(query)
"""
target, query, metadata = dbpedia.get_query("What is the time zone of Salt Lake City?")
print(query)