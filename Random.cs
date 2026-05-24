using System;
class Random {
	static void Main() {
		Random dado = new Random();
		Random dados = new Random();
		int resultado = dado.Next(1,7);
		int result = dados.Next(1, 7);
		if(resultado<result)
		{
		    Console.WriteLine($"perdiste, la pc saco {result} y tu {resultado}");
		}
		else if(result == resultado)
		{
		    Console.WriteLine($"empate ambos sacaron {result}");
		}
		else
		{
		    Console.WriteLine($"Ganaste, tu sacaste {resultado} y la pc {result}");
		}
		
	}
}
