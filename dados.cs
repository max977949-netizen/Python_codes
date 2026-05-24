using System;
    Random dado = new Random();
    int[] result = new int[7];
    for (int i = 0; i<100;i++)
    {
        
        int num = dado.Next(1,7);
        result[num]++;
    }
    for(int cara = 1; cara<=6;cara++)
    {
        Console.WriteLine($"la cara {cara} cayo {result[cara]} veces");
    }
