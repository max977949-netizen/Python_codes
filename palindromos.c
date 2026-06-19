#include <stdio.h>

int main() {
    int numero, original, invertido = 0, ultimo_digito;

    printf("Ingresa un numero entero: ");
    scanf("%d", &numero);

    // 1. Guarda el valor original antes de destruir "numero"
    original = numero;

    // 2. AQUÍ VA TU LÓGICA (Puedes usar while o do-while)
    // Desarma "numero" paso a paso y construye "invertido"
    do{
        ultimo_digito = numero % 10;
        invertido = (invertido*10) + ultimo_digito;
        numero /= 10;
    }while(numero > 0);
    

    // 3. COMPARACIÓN FINAL
    // Si el invertido es igual al original, es palíndromo...
    if (original == invertido){
        printf("\n%d es palindromo", original);
    }
    else{
        printf("\n%d no es palindromo", original);
    }

    return 0;
}
