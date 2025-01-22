import os
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# nltk.download("punkt_tab")

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


# 4 - WordCloud / WordCloud Customizado
def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


wordcloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="salmon",
    colormap="Pastel1",
    collocations=False,
    stopwords=STOPWORDS,
).generate(texto)

plot_cloud(wordcloud)

try:
    file_path = "data/upvote.png"
    if os.path.exists(file_path):

        # Abrindo o arquivo de imagem
        mascara = np.array(Image.open(file_path))

    else:
        print("Arquivo não encontrado:", file_path)

    wordcloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="salmon",
        colormap="Pastel1",
        collocations=False,
        stopwords=STOPWORDS,
        mask=mascara,
    ).generate(texto)

    plot_cloud(wordcloud)
except Exception as e:
    print("Erro ao abrir a imagem:", e)


with open(os.path.join("data", "result.txt"), "w", encoding="utf-8") as file:
    file.write(str(dic))
