


// Read & Parse
string[] lines = File.ReadAllLines("input.txt"); 
List<int> integer_lines = new List<int>();
foreach (string line in lines)
{
    integer_lines.Add(int.Parse(line));
}

integer_lines.Sort();


int one = 0;
int two = 0;
int three = 0;
int previous = 0;

foreach (int item in integer_lines){
    if (item - previous == 1){
        one++;
    } else if (item - previous == 2){
        two++;
    } else if (item - previous ==  3){
        three++;
    }
    previous = item;
}
    
three ++;  // built-in adapter is 3 higher than my highest adapter. 


Console.WriteLine(one);
Console.WriteLine(two);
Console.WriteLine(three);   
Console.WriteLine(one * three);   
