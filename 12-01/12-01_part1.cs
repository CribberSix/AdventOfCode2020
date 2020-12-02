using System;


string[] lines = System.IO.File.ReadAllLines(@"input_part.txt");
int x = 0;
bool break_early = false;
foreach (string outer in lines)
{
    foreach (string inner in lines)
    {
        if (Int16.Parse(outer) + Int16.Parse(inner)  == 2020) {
            Console.WriteLine("Found them: " + outer + " and " + inner);
            int a = Int16.Parse(outer);
            int b = Int16.Parse(inner);
            int result = a * b;
            Console.WriteLine("Result is: " + Convert.ToString(result));
            break_early = true;
            break;

        }
        
    }
    if (break_early) {
        break;
    }
}
 
Console.WriteLine("Finished.")