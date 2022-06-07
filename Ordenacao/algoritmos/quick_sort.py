import datetime


def particao(vetor, inicio, final):
  comp, trocas = 0, 0
  pivo = vetor[final]
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      comp += 1
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
      trocas += 1
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  trocas += 1

  return i + 1, comp, trocas

def quick_sort(vetor, inicio, final):
  comp, trocas = 0, 0

  if inicio < final:
    posicao, comp, trocas = particao(vetor, inicio, final)
    # Esquerda
    quick_sort(vetor, inicio, posicao - 1)
    # Direito
    quick_sort(vetor, posicao + 1, final)
  return comp, trocas


def arquivos():
    lista = []
    temp = ''
    
    with open('./lista_numeros/cem.txt', 'r') as arq:
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

  comparacao, trocas = quick_sort(arq, 0, len(list) - 1)


  tempo = datetime.datetime.now() - inicio
  print(f'Tempo: {tempo.total_seconds():.5f} segundos. | Comparacao: {comparacao} | Trocas: {trocas}| Tamanho: {len(list)} ')
  print()

if __name__ == '__main__':
    main()
