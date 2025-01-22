import os
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist

nltk.download("punkt_tab")

dic = list()

# 1 - Importação do Texto
with open(os.path.join("data", "texto.txt"), "r", encoding="utf-8") as file:
    texto = file.read()
    print(texto)

# 2 - Tokenizando o Texto
sent_tokens = sent_tokenize(texto)
print(sent_tokens)
print(len(sent_tokens))

dic.append(sent_tokens)

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))

dic.append(word_tokens)

# 3 - Frequência de Distribuição
fdist = FreqDist(word_tokens)
# print(fdist)
print(fdist.most_common(10))
fdist.plot(10)

dic.append(fdist)

print(dic)

with open(os.path.join("data", "result.txt"), "w", encoding="utf-8") as file:
    file.write(str(dic))
