import random
import webbrowser
class Sorteio:
    # constructor
    def __init__ (self, qtd_dezenas, tot_jogos, resultado, jogos):
        # atributos privados
        self.__qtd_dezenas = qtd_dezenas
        self.__resultado = resultado
        self.__tot_jogos = tot_jogos
        self.__jogos = jogos

    def qtdDezenas(self, qtd_dezenas):
        self.__qtd_dezenas = qtd_dezenas

    def totJogos(self, tot_jogos):
        self.__tot_jogos = tot_jogos

    def resultado(self, __qtd_dezenas, __tot_jogos):
        return self.__qtd_dezenas, self.__tot_jogos

    def jogos(self, qtd_dezenas):
        lista = []
        lista.append(sorted(random.sample(range(1, 60), qtd_dezenas)))
        self.__jogos = sorted(lista)
        return sorted(self.__jogos)

    def resultados(self, qtd_dezenas, jogos):
        sorts = []
        for i in range(jogos):
            sorts.append(sorted(self.jogos(qtd_dezenas)))
        self.__qtd_dezenas = qtd_dezenas
        self.__resultado = sorts
        return self.__resultado

sorte = Sorteio(0, 0, 0,0)

with open("resultados.html", "w", encoding="utf-8") as htmlfile:
    htmlfile.write("<!DOCTYPE html>")
    htmlfile.write("<html>")
    htmlfile.write("<head>")
    htmlfile.write("<style>")
    htmlfile.write("table, th, td{")
    htmlfile.write("border: 1px solid black")
    htmlfile.write("}")
    htmlfile.write("</style>")
    htmlfile.write("</head>")
    htmlfile.write("<body>")
    htmlfile.write("<h2>Resultados</h2>")
    htmlfile.write("<table>")
    htmlfile.write("<tr>")
    htmlfile.write("<th>Numeros</th>")
    htmlfile.write("</tr>")
    for resultado in sorte.resultados(6, 10):
        htmlfile.write("<tr>")
        htmlfile.write("<td>"+str(*resultado).strip('[]')+"</td>")
        htmlfile.write("</tr>")
    htmlfile.write("</tr>")
    htmlfile.write("</table>")
    htmlfile.write("</body>")
    htmlfile.write("</html>")


webbrowser.open("resultados.html")