using System;

class Programes
{
    // 1. Tus funciones personalizadas se quedan exactamente igual fuera del Main
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
        int chaty = Convert.ToInt32(chat);
        if (chaty == 1)
        {
            Console.WriteLine("Abriendo chat de minecraft");
        }
        else if (chaty == 2)
        {
            Console.WriteLine("Abriendo chat de c++");
        }
        else if (chaty == 3)
        {
            Console.WriteLine("Abriendo chat de python");
        }
        else
        {
            Console.WriteLine("accion no valida");
        }
    }

    // 2. Tu motor principal
    static void Main()
    {
        Console.WriteLine("Pon tu apodo");
        string usuario = Console.ReadLine();
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

        // --- AQUÍ METEMOS TU VARIABLE Y TU BUCLE ---
        // Al poner la variable aquí adentro, arreglamos el error del 'static'
        bool programa = true;

        while (programa)
        {
            Console.WriteLine("Que chat quieres abrir? 1 minecraft. 2 c++. 3 python. 4 salir");
            string respuesta = Console.ReadLine(); // Metimos esto aquí adentro para que no se cicle al infinito

            int respueNume;
            bool respue = int.TryParse(respuesta, out respueNume);

            if (respue)
            {
                if (respueNume == 4)
                {
                    programa = false; // Tu idea original de cambiar la variable a false
                    Console.WriteLine("Saliendo...");
                }
                else
                {
                    chats(respueNume); // Llama a tu función original
                }
            }
            else
            {
                Console.WriteLine("Accion no valida");
            }
        }

        Console.WriteLine("\n--- Fin del inicio de sesión ---");
    }
}
