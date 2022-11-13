import quepy


dbpedia = quepy.install("dbpedia")



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

target, query, metadata = dbpedia.get_query("which artists were born on the same date as Rachel Stevens")
print(query)
