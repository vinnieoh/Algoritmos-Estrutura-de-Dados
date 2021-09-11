/*Vinicius de Oliveira*/
#include <stdio.h>
#include <stdlib.h>

void armazena(int *v, int num);
void prints(int *v, int num);
int funRecursiva(int *v, int num);

int main(){

    int num, veri;
    int *v;
    
    puts("Digite o tamanho do vetor: ");
    scanf("%d", &num);
    v = (int *) malloc(num * sizeof(int)); 

    if(v == NULL){
        printf("Erro: Memoria Insuficiente! \n");
        system("pause");
        exit(1);
    }	

    armazena(v, num);
    veri = funRecursiva(v, num);
    prints(v, num);
    printf("Maior numero: %d", veri);

    free(v);

    return 0;
}

void armazena(int *v, int num){
    for(int i=0;i<num;i++){
        puts("Digite os numeros do vetor: ");
        scanf("%d", &v[i]);
    }
}

void prints(int *v, int num){
    for(int i=0;i<num;i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}

int funRecursiva(int *v, int num){
    int cont;
    if(num == 1){
        return cont = v[0];
    }else{
        cont = funRecursiva(v, num-1);
        if(cont>v[num-1]){
            return (cont);
        }else{
            return (v[num-1]);
        }        
    }
    
}
