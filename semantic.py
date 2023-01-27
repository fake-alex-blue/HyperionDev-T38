import spacy
nlp = spacy.load('en_core_web_md')


# Similarity with spaCy

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))      # "cat" similar to "monkey"
print(word3.similarity(word2))      # "banana" similar to "monkey"
print(word3.similarity(word1))      # "banana" similar to "cat"

print()
print("-" * 50)
print()

'''
There's nothing surprising about the results of the above, 'cat' and 'monkey' share some semantic connotations,
fewer than 'monkey' and 'banana', but more than the (largely) semantically unrelated 'cat' and 'banana'. 
'''

# An example of my own
word4 = nlp("tiger")
word5 = nlp("dog")

print(word1.similarity(word4))      # "cat" similar to "tiger"
print(word1.similarity(word5))      # "cat" similar to "dog"
print(word4.similarity(word5))      # "tiger" similar to "dog"

print()
print("-" * 50)
print()



# Working with Vectors
tokens = nlp('cat apple monkey banana dog')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
print("-" * 50)
print()


# Trying it out myself
tokens = nlp('mountains madness hills trees valleys swamps')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
print("-" * 50)
print()


# Working with Sentences
sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "My cat is on a car, why?",
    "Is a cat on my car?",
    "Where does my cat go?",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
    ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
Runing the provided example.py using the 'en_core_web_sm' language instead of 'en_core_web_md',
I notice a greater variance between similarity values, and generally speaking all the values
are lower - approximately 20% lower on average.

I also get a user warning that there are no word vectors provided with that language model.

The course material has not explained word vectors, so I will not comment on them.
'''