#include <stdio.h>
#include <math.h> // ¡La necesitas para sqrt()!

int main() {
    int x, y;
    double distancia;

    printf("--- SISTEMA DE RADAR DE PROXIMIDAD ---\n");
    
    // 1. Pide al usuario las coordenadas X y Y (No olvides el & en el scanf)
    printf("pon cordenada X: \n");
    scanf("%d", &x);
    printf("pon cordenada Y: \n");
    scanf("%d", &y);


    // 2. AQUÍ VA TU MATEMÁTICA
    // Calcula la distancia usando sqrt() y los cuadrados de X e Y
    distancia = sqrt((x*x)+(y*y));


    // 3. LOGICA DE CONTROL (if, else if, else)
    // Despliega las alertas según la distancia calculada
    if (distancia <= 5){
        printf("Peligro, peligro corran");
    }
    else if(distancia > 5 && distancia <= 10){
        printf("Alerta amarilla, con precaución");
        
    }
    else{
        printf("Seguro");
    }


    return 0;
}
