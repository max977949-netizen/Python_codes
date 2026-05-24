using System;
    Console.WriteLine("Pon una contraseña");
    string y = Console.ReadLine();
    string result = (y.Length > 8 && char.IsDigit(y[y.Length - 1])) ? "Aceptada":"Rechazada";
    Console.WriteLine(result);
