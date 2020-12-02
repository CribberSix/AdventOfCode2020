using System;


string[] lines = System.IO.File.ReadAllLines(@"input_part.txt");
int x = 0;
bool break_early = false;
foreach (string outer in lines)
{
    foreach (string inner in lines)
    {
            
        foreach (string inner_2 in lines)
        {
            if (Int16.Parse(outer) + Int16.Parse(inner) + Int16.Parse(inner_2) == 2020) {
                Console.WriteLine("Found them: " + outer + " and " + inner +  " and" + inner_2 );
                int a = Int16.Parse(outer);
                int b = Int16.Parse(inner);
                int c = Int16.Parse(inner_2);
                int result = a * b * c;
                Console.WriteLine("Result is: " + Convert.ToString(result));
                break_early = true;
                break;

            }
        }
        if (break_early) {
            break;
        }
    }
    if (break_early) {
        break;
    }
}
 
Console.WriteLine("Finished.");
