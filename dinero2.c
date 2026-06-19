#include <stdio.h>

int main() {
    int dinero;
    int m10, m5, m2, m1;
    int sobrante;

    printf("Ingresa la cantidad a retirar: $");
    scanf("%d", &dinero);

    // --- AQUÍ VA TU LÓGICA ---
    // Pista para empezar:
    if (dinero >= 501 || dinero <= 0){
        printf("\n operación invalida");
        return 1;
    }
    else{
        m10 = dinero / 10;
        sobrante = dinero % 10;
        // Ahora te toca a ti calcular m5, m2 y m1 usando el "sobrante"...
        m5 = sobrante / 5;
        sobrante = sobrante % 5;
        m2 = sobrante / 2;
        sobrante = sobrante % 2;
        m1 = sobrante;
        // --- SALIDA DE DATOS ---
        printf("\nDesglose de monedas:\n");
        printf("Monedas de $10: %d\n", m10);
        printf("Monedas de $5: %d\n", m5);
        printf("Monedas de $2: %d\n", m2);
        printf("Monedas de $1: %d\n", m1);
        return 0;
    }
}
