import gensim, logging
#code below to understand how gensim works and gain understanding
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.I)

sentences = [['first', 'sentence'], ['second', 'sentence']]
model = gensim.models.Word2Vec(sentences, min_count=1)

