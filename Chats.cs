using System;

class Chats
{
    // 1. Aquí creamos nuestra función personalizada fuera del Main
    static void DarBienvenida(string nombreUsuario)
    {
        Console.WriteLine("¡Hola, " + nombreUsuario + "! Bienvenido al Refugio del Programador.");
        Console.WriteLine("Conectando al servidor seguro...");
    }
    static void contrasenaUser(string contraseñaUsuario)
    {
        Console.WriteLine("Tu contraseña es, " + contraseñaUsuario);
    }
    static void chats(int chat)
    {
        if (chat == 1)
        {
            Console.WriteLine("Abriendo chat de minecraft");
        }
        else if (chat == 2)
        {
            Console.WriteLine("Abriendo chat de c++");
        }
        else if (chat == 3)
        {
            Console.WriteLine("Abriendo chat de python");
        }
        else
        {
            Console.WriteLine("accion no valida");
        }

    }


    // 2. Este es el motor principal que ya conoces
    static void Main()
    {
        Console.WriteLine("Pon tu apodo");
        string usuario = Console.ReadLine();        // En lugar de escribir todo el texto aquí, solo "llamamos" a la función
        DarBienvenida(usuario);
        Console.WriteLine("Crea tu contraseña");
        string contra = Console.ReadLine();
        contrasenaUser(contra);
        Console.WriteLine("Pon tu contraseña");
        string confir = Console.ReadLine();
        if (confir == contra)
        {
            Console.WriteLine("Confirmado, usuario correcto");
        }
        Console.WriteLine("Que chat quieres abrir? 1 minecraft. 2 c++. 3 python ");
        string respuesta = Console.ReadLine();
        int respue = Convert.ToInt32(respuesta);
        chats(respue);


        Console.WriteLine("\n--- Fin del inicio de sesión ---");
    }
}
