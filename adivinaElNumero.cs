using System;
    Random numero = new Random();
    int num = numero.Next(1, 11);
    bool juan = true;
    while(juan)
    {
        bool y = int.TryParse(Console.ReadLine(), out int x);
        if(y)
        {
            if(x==num)
            {
                Console.WriteLine("Ganaste");
                juan = false;
            }
            else if(x>num)
            {
                Console.WriteLine("El numero es menor");
            }
            else if(x<num)
            {
                Console.WriteLine("El numero es mayor");
            }
            
        }
        else
        {
            Console.WriteLine("Accion no valida");
        }
    }
