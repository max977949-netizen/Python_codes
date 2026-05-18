using System;

class Program
{
    // 1. Aquí creamos nuestra función personalizada fuera del Main
    static void DarBienvenida(string nombreUsuario)
    {
        Console.WriteLine("¡Hola, " + nombreUsuario + "! Bienvenido al Refugio del Programador.");
        Console.WriteLine("Conectando al servidor seguro...");
    }
    static void contraseñaUser(string contraseñaUsuario)
    {
        Console.WriteLine("Tu contraseña es, " + contraseñaUsuario);
    }


    // 2. Este es el motor principal que ya conoces
    static void Main()
    {
        Console.WriteLine("Pon tu apodo");
        string usuario = Console.ReadLine();        // En lugar de escribir todo el texto aquí, solo "llamamos" a la función
        DarBienvenida(usuario);
        Console.WriteLine("Crea tu contraseña");
        string contra = Console.ReadLine();
        contraseñaUser(contra);
        Console.WriteLine("Pon tu contraseña");
        string confir = Console.ReadLine();
        if (confir == contra)
        {
            Console.WriteLine("Confirmado, usuario correcto");
        }


        Console.WriteLine("\n--- Fin del inicio de sesión ---");
    }
}
