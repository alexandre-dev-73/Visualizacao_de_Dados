import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Continua criando novos passeios enquanto o programa estiver ativo
while True:
    #cria u passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Define o tamanho da janela de plotagem
    plt.figure(dpi=128, figsize=(10, 6))
    #Plotando os pontos e mostra o grafico
    point_numbers = list(range(rw.num_points))
    #Remove os eixos
    plt.axes().get_yaxis().set_visible(False)
    #plt.axes().get_xaxis().set_visible(True)

   # plt.plot(rw.x_values, rw.y_values, 'go--', linewidth=2, markersize=0)

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Enfatiza o primerio eo último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
