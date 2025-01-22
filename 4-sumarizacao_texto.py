import os
from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

# 1 - Coletando o Artigo
g = Goose()
url = "https://olhardigital.com.br/2023/08/09/ciencia-e-espaco/por-que-e-importante-criar-uma-rotina-de-sono/"
noticia = g.extract(url)
# print(noticia.cleaned_text)

# 2 - Trabalhando com a Sumarização
parser = PlaintextParser.from_string(noticia.cleaned_text, Tokenizer("portuguese"))
# print(parser.document)
sumarizador = LuhnSummarizer()
resumo = sumarizador(parser.document, 3)


with open(os.path.join("data", "sumarizacao.txt"), "a", encoding="utf-8") as file:
    for sentenca in resumo:
        print(sentenca)
        file.write(str(sentenca) + "\n")
