using System;
    Console.WriteLine("pon un grado sin el º");
    bool y = double.TryParse(Console.ReadLine(), out double x);
    if(y)
    {
        x = x*1.8+32;
        Console.WriteLine($"En grados fahrenheit son {x}º");
    }
    else
    {
        Console.WriteLine("Accion no valida");
    }
