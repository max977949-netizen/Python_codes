using System;

namespace HelloWorld;

public class sat
{
    static void Main()
    {
        int pres = 15;


        Console.WriteLine("Cuanto dinero tienes?");
        bool f = int.TryParse(Console.ReadLine(), out int p);
        if (f)
        {
            Console.WriteLine("la pocion cuesta 15 pesos, cuantas quieres?");
            bool yes = int.TryParse(Console.ReadLine(), out int yexs);
            if (yes)
            {
                yexs *= pres;
                p -= yexs;
                if (p < 0)
                {
                    Console.WriteLine($"Ahora le debes al SAT {p} pesos");
                }
                else
                {

                    Console.WriteLine($"pagaste {yexs} pesos y te quedan {p} pesos");

                }

            }
            else
            {
                Console.WriteLine("accion no valida");

            }


        }
        else
        {
            Console.WriteLine("accion no valida");
        }

    }
}

