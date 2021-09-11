/*Aluno: Vinicius de Oliveira*/
#include <stdio.h>
#include <stdlib.h>

void armazena(int *v, int aux);
void selectionSortCresente(int *v, int aux);
void ordenaCrescente(int aux, int*v);
void insertionSortDecresente(int *v, int aux);
void ordenaDecrescente(int aux, int*v);

int main(){

    int *v;
    int aux, cont, cs;

    do{
        puts("Informe o tamanho do verto: ");
        scanf("%d", &aux);
        v = (int *) malloc(aux * sizeof(int)); 

        if(v == NULL){
            printf("Erro: Memoria Insuficiente! \n");
            system("pause");
            exit(1);
        }	
            
        armazena(v, aux);

        printf("\n");

        puts("Voce deseja o vetor: 1- Forma crescente | 2 - decrescente ");
        scanf("%d", &cs);

        switch(cs){
            case 1:
                selectionSortCresente(v, aux);
                puts("Vetor crescente: ");
                ordenaCrescente(aux, v);
                break;
            case 2:
                insertionSortDecresente(v, aux);
                puts("Vetor decrescente: ");
                ordenaDecrescente(aux, v);
                break;
            default:
                printf ("Valor invalido!\n");
        }
        
        free(v);
        printf("\n");

        puts("Digite: 0 Para Parar | 1 Para continuar ");
        scanf("%d", &cont);

    }while(cont != 0);

    return 0;
}

void armazena(int *v, int aux){
    int i;

    for(i=0; i<aux; i++){
        puts("Digite os valores para o vetor: ");
        scanf("%d", &v[i]);
    }
}

void selectionSortCresente(int *v, int aux){
    int i, j, min, aux1;

    for (i = 0; i < (aux-1); i++) {
        min = i;
        for (j = (i+1); j < aux; j++) {
            if(v[j] < v[min]){
                min = j;
            }
        }

        if (v[i] != v[min]) {
            aux1 = v[i];
            v[i] = v[min];
            v[min] = aux1;
        }
    }

}

void ordenaCrescente(int aux, int*v){
    for(int i=0;i<aux;i++){
        printf("%d ",v[i]);
    }
}

void insertionSortDecresente(int *v, int aux) {
    int i, j, tmp;
    for (i = 1; i < aux; i++) {
        j = i;
        while (j > 0 && v[j - 1] < v[j]) {
            tmp = v[j];
            v[j] = v[j - 1];
            v[j - 1] = tmp;
            j--;
        }
    }
}

void ordenaDecrescente(int aux, int*v){
    for(int i=0;i<aux;i++){
        printf("%d ",v[i]);
    }
}
