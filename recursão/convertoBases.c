#include <stdio.h>
//#include <math.h>
#include <stdlib.h>
#include <string.h>

void opcoes();
void binario(int valor);
void octal(int valor);
void hexadecimal(int valor);

int main(){

    int op, valor, resu;

    do{
    
        opcoes();
        scanf("%d", &op);

        if(op > 0 && op <= 3){
            puts("Digite o valor natural: ");
            scanf("%d", &valor);
        }

        switch(op){
            case 0: 
                break;
            case 1:
                printf("O Valor = %d -> Binario = ", valor);
                binario(valor);
                break;
            case 2: 
                printf("O Valor = %d -> Octal = ", valor);
                octal(valor);
                break;
            case 3:
                printf("O Valor = %d -> Hexadecimal = ", valor);
                hexadecimal(valor);
                break;
            default:
                printf ("Opcao invalida!");
                break;
        }

        printf("\n");

    }while (op != 0);

    return 0;
}

void opcoes(){
    printf("0 - Sair\n");
    printf("1 - Valor natural -> Binario\n");
    printf("2 - Valor natural -> Octal\n");
    printf("3 - Valor natural -> Hexadecimal\n");
    puts("Digite a opcao: ");
}

void binario(int valor){
    int res = valor;

    if (res / 2 != 0) {
        res = res /2;
        binario(res);
    }

    printf("%d", valor % 2);
}

void octal(int valor){
    int res = valor;

    if(res >= 8){
        res = res/8;
        octal(res);
    }
    
    printf("%d", valor % 8);
}
void hexadecimal(int valor){
    int res = valor;

    if(res >= 16){
        res = res/16;

        hexadecimal(res);
    }   
    printf("%X", valor%16);
}