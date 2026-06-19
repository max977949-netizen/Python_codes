#include <stdio.h>
#include <string.h> // ¡La necesitas para strcpy!

int main() {
    // Matriz de 4 filas y 20 columnas para guardar los textos
    char inventario[4][20] = {"Espada", "Escudo", "Pocion", "Vacio"};
    int opcion;
    int ranura_a_tirar;
    int esp;

    do {
        printf("\n--- MENU DE INVENTARIO ---\n");
        printf("1. Ver Inventario\n");
        printf("2. Tirar Objeto\n");
        printf("3. Salir\n");
        printf("Elige una opcion: ");
        scanf("%d", &opcion);

        switch(opcion) {
            case 1:
                // 1. AQUÍ VA TU BUCLE FOR
                // Haz un ciclo del 0 al 3 para imprimir cada ranura
                printf("\n");
                esp = sizeof(inventario) / sizeof(inventario[0]);
                for (int i = 0; i < esp; i++){
                    printf("%d %s \n", i, inventario[i]);
                }
                break;

            case 2:
                // 2. AQUÍ VA LA LÓGICA PARA TIRAR
                // Pregunta la ranura (0-3), léela con scanf
                // Usa strcpy(inventario[ranura_a_tirar], "Vacio");
                printf("Ranura 0, 1, 2 o 3");
                scanf("%d", &ranura_a_tirar);
                strcpy(inventario[ranura_a_tirar], "Vacio");
                printf("[INFO]: Objeto descartado.\n");
                break;

            case 3:
                printf("Saliendo del juego...\n");
                break;

            default:
                printf("Opcion no valida.\n");
        }

    } while(opcion != 3);

    return 0;
}
