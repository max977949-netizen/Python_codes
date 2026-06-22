#include <stdio.h>

// 1. ESCRIBE AQUÍ TU FUNCIÓN evaluar_bateria
// Recibe un int, devuelve un char* usando un ternario
char* bateria(int baterias) {

	return baterias < 15? "Lo siento bateria baja ":"Bateria estable";
}


// 2. ESCRIBE AQUÍ TU FUNCIÓN calcular_velocidad
// Recibe un int (distancia), calcula el PWM (0-255) y lo devuelve
int velocidad(int dise) {
	int dis = dise > 10? dise*5: 0;
	return dis > 255? 255: dis;
}


int main() {
	int bateria_ingresada, distancia_ingresada;

	printf("--- SISTEMA CENTRAL DEL ROBOT ---\n");
	printf("Ingrese porcentaje de bateria: ");
	scanf("%d", &bateria_ingresada);
	printf("Ingrese distancia al obstaculo (cm): ");
	scanf("%d", &distancia_ingresada);

	printf("\n--- REPORTE DE SISTEMA ---\n");

	// 3. INVOCA AQUÍ TUS FUNCIONES DENTRO DE LOS PRINTF
	// Ejemplo: printf("Estado: %s\n", evaluar_bateria(bateria_ingresada));
	printf("Estado Energia: %s\n", bateria(bateria_ingresada));
	char* res = bateria_ingresada < 15? "Bateria baja , motores inutiles":"Velocidad Motores (PWM): %d\n";
	printf(res, velocidad(distancia_ingresada));

	return 0;
}
