import pygal
from die import Die

#Criando os dados oito lados
dado_1 = Die(8)
dado_2 = Die(8)

#Resultado  de lançar os dados 1000 vez
resultado =[(dado_1.roll() + dado_2.roll()) for num_jogadas in range(1000)]

#Analisa os resultados
valor_maximo = dado_1.num_sides + dado_2.num_sides
frequencia =[resultado.count(valor) for valor in range(2, valor_maximo+1)]

#visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '16']
hist.x_title = "Resultado"
hist.y_title = "Frequencia do Resultado"

hist.add('D8 + D8', frequencia)
hist.render_to_file('visualizao_dado.svg')
