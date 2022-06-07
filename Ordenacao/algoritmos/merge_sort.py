import datetime


def merge_sort(vetor):
  comp, trocas = 0, 0

  if len(vetor) > 1:
    divisao = len(vetor) // 2
    esquerda = vetor[:divisao].copy()
    direita = vetor[divisao:].copy()

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    # Ordena esquerda e direita
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        comp += 1
        vetor[k] = esquerda[i]
        i += 1
      else:
        comp += 1
        vetor[k] = direita[j]
        j += 1
      k += 1
      trocas += 1

    # Ordenação final
    while i < len(esquerda):
      comp += 1
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    while j < len(direita):
      comp += 1
      vetor[k] = direita[j]
      j += 1
      k += 1
      trocas += 1

  return comp, trocas

def arquivos():
    lista = []
    temp = ''
    
    with open('./lista_numeros/cincoMilhoes.txt', 'r') as arq:
        data = arq.readline().replace(" ", ",")
        for i in data:
            if i != ',':
                temp +=i
            else:
                lista.append(temp)
                temp = ''

        arq.close()


    
    return lista



def main():

  arq = arquivos()
  list = []

  for i in arq:
      if i != "," :
        i = int(i)
        list.append(i)
            
  inicio = datetime.datetime.now()

  comparacao, trocas = merge_sort(arq)


  tempo = datetime.datetime.now() - inicio
  print(f'Tempo: {tempo.total_seconds():.5f} segundos. | Comparacao: {comparacao} | Trocas: {trocas}| Tamanho: {len(list)} ')
  print()

if __name__ == '__main__':
    main()
