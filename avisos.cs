using System;
class avisos {
	static void Main() {
		int temp = 0;
		int mini = 300;
		int sum = 0;
		int alertas = 0;
		int[] temperaturas = {85, 92, 110, 115, 120, 95, 88, 130, 145, 102};
		foreach(int x in temperaturas)
		{
			if(x>temp)
			{
				temp = x;
			}
			if(x<mini)
			{
				mini = x;
			}
			if(x>110)
			{
				alertas++;
			}
			sum += x;
		}
		if(alertas>3)
		{
			Console.WriteLine($"La temperatura subio {alertas} veces, peligro detectado");
		}
		Console.WriteLine($"Temperatura mas alta fue {temp}");
		Console.WriteLine($"Temperatura más baja fue {mini}");
		Console.WriteLine($"La media de temperatura fue {sum/10}");
		Console.WriteLine($"Números de alertas {alertas}");
	}
}
