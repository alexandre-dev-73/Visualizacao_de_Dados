from die import Die
import pygal

#Cria um D6
die = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista
results =[die.roll() for roll_num in range(100)]

#Analisa os resultados
frequencies = [(results.count(values)) for values in range(1, die.num_sides+1)]

#Visualiza os resultados
lista = [str(item) for item in range(1, 7)]

hist = pygal.Bar()

hist.title = "Results of rolling on D6 1000 times."
hist.x_labels = lista
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
