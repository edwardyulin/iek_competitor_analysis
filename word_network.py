""""""
import spacy
from spacy.lang.zh.examples import sentences

nlp = spacy.load("zh_core_web_sm")
doc = nlp("2021年前3季全球IC設計產業綜整研析")
print(doc.text)
for token in doc:
        print(token.text, token.pos_, token.dep_)
