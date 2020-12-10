using System;
using System.Linq;

// Read & Parse
string[] lines = File.ReadAllLines("input.txt"); 
List<int> integer_lines = new List<int>();
foreach (string line in lines)
{
    integer_lines.Add(int.Parse(line));
}



for (int i = 5; i < integer_lines.Count; i++){
    int lower = i - 5;
    List<int> sublist = new List<int>(); 
    var slice = integer_lines[0..5];

}


//public static bool is_valid()