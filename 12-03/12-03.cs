using System;


// get input
string[] lines = File.ReadAllLines("input.txt"); 


long x1 = check_slope(1, 1, lines);
long x2 = check_slope(3, 1, lines);
long x3 = check_slope(5, 1, lines);
long x4 = check_slope(7, 1, lines);
long x5 = check_slope(1, 2, lines);

long result = x1 * x2 * x3 * x4 * x5;
Console.WriteLine("Multiplied trees: {0}", Convert.ToString(result));

public long check_slope(int right, int down, string[] lines){

    int index_x = 0;
    int index_y = 0;
    long tree_counter = 0;
    char tree = '#';

    for (int i = 0; i < lines.Length; i++){
        if (index_y > i){
            continue;
        }

        if (lines[i][index_x] == tree){
            tree_counter ++;
        }

        // prep for the next step and reset index_x if necessary.
        index_x += right;
        index_y += down;
        if (index_x >= lines[0].Length){
            index_x -= lines[0].Length;
        }
    }
    Console.WriteLine("On the slope with {0} right and {1} down, there were {2} trees.", right, down, tree_counter);
    return tree_counter;

}
