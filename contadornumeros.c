#include <stdio.h>

int main() {
    int numero;
    int contador = 0;

    printf("Ingresa un numero entero positivo: ");
    scanf("%d", &numero);

    // --- AQUÍ VA TU BUCLE WHILE ---
    // MIENTRAS el numero sea mayor que 0, haz los pasos...
    /*while (numero > 0){
        numero = numero / 10;
        contador++;
    }*/
    do
    {
        numero = numero / 10;
        contador++;
    }while(numero > 0);
    
    

    // --- SALIDA ---
    printf("\n El numero tiene %d digitos.\n", contador);

    return 0;
}
