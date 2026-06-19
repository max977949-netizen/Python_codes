#include <stdio.h>

int main() {
	int tuercas = 21;
	int quita_humano;
	int quita_robot;

	printf("--- EL JUEGO DE LAS 21 TUERCAS ---\n");
	printf("El que se lleve la ultima tuerca, pierde.\n\n");

	// ¡Aquí empieza tu código!
	// Diseña el bucle del juego y la IA matemática del robot...
	do {
		printf("Cuantas tuercas quieres quitar?: \n");
		scanf("%d", &quita_humano);
		tuercas -= quita_humano;
		quita_robot = (tuercas - 1)%4;
		tuercas -= quita_robot;
		printf(" el robot a quitado %d tuercas \n", quita_robot);
		printf("quedan %d tuercas \n", tuercas);
	} while(tuercas > 1);

	return 0;
}
