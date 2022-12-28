import spacy
nlp = spacy.load("en_core_web_md")


# Pare of words - cat and monkey - has a significant similarity, they are both animals.
# Pare of words - banana and monkey - has high similarity, because monkey eats banana
# Pare of words - banana and cat - doesn't has any significant similarity
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.text, word2.text, word1.similarity(word2))
print(word3.text, word2.text, word3.similarity(word2))
print(word3.text, word1.text, word3.similarity(word1))
print("=========")


# In this example I take three words: rice, flower and butterfly.
# Pare of words - rice and butterfly - has a low similarity.
# Pare of words - rice and flower - has higher similarity, because thay are both plants
# Pare of words - butterfly and flower - has a significant similarity

word4 = nlp("rice")
word5 = nlp("butterfly")
word6 = nlp("flower")
print(word4.text, word5.text, word4.similarity(word5))
print(word4.text, word6.text, word4.similarity(word6))
print(word5.text, word6.text, word5.similarity(word6))


"""
tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
"""

"""
sentence_to_compare = "Why is my cat on tha car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
"""
