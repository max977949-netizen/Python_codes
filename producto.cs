using System;
    Console.WriteLine("Cuanto vale tu producto");
    bool y = double.TryParse(Console.ReadLine(), out double x);
    if(y)
    {
        double g = (x > 100)? x *= 0.90:x;
        Console.WriteLine($"Tu precio es de ${g}");
    }
    else
    {
        Console.WriteLine("Accion no valida");
    }
