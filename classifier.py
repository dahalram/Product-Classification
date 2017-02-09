import nltk
#nltk.download()
from nltk.corpus import wordnet as wn
import nltk.corpus.reader.sentiwordnet
from itertools import chain

word = 'shoes'
synonyms = wn.synsets(word)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))

print lemmas

words = list(lemmas)

print "\n****\n" 
print words

print "\n****\n" 

dog = wn.synset('shoe.n.01')
dog_words = set(chain.from_iterable([word.lemma_names() for word in dog.hyponyms()]))
print list(dog_words)

# def get_hyponyms(synset):
#     hyponyms = set()
#     for hyponym in synset.hyponyms():
#         hyponyms |= set(get_hyponyms(hyponym))
#     return hyponyms | set(synset.hyponyms())


# vehicle = wn.synsets('vehicles.n.01')
# # print get_hyponyms(vehicle)

# typesOfVehicles = list(set([w for s in vehicle.closure(lambda s:s.hyponyms()) for w in s.lemma_names]))
# print typesOfVehicles

# # print "\n****\n" 

# # test = wn.morphy('abaci')
# # print test

print wn.morphy('abaci', wn.NOUN)

print wn.morphy('dogs')
print wn.morphy('dogs', wn.ADV)

print wn.morphy('using')
print wn.morphy('using', wn.VERB)

# # for i,j in enumerate(wn.synsets(word)):
# #   print "Meaning",i, "NLTK ID:", j.name
# #   print "Definition:",j.definition