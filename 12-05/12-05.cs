using System;
using System.Collections.Generic; 

 // read input
string[] lines = File.ReadAllLines("input.txt"); 

List<Seat> seats  = new List<Seat>();


int max_id = -1;
foreach (string _s in lines)
{   
    Seat temp = new Seat(_s);
    seats.Add(temp);
    range.Remove(temp.id);
    if (temp.id > max_id){
        max_id = temp.id;
    } 
}

Console.WriteLine("MAX ID: {0}", max_id);

List<int> range = Enumerable.Range(0, max_id).ToList<int>();
foreach (int i in range) {
    Console.WriteLine("Range: {0}", i);
}

public class Seat {

    public int row; 
    public int column;
    public int id; 

    public Seat(string s){
        string s_row = s.Substring(0,7);
        string s_seat = s.Substring(7,3);
        this.row = this.calculate_row(s_row);
        this.column = this.calculate_col(s_seat);
        this.calculate_id();
        
        Console.WriteLine("Row-Col-ID: {0}-{1}-{2}", this.row, this.column, this.id);
        //Console.WriteLine("  ");
    }

    public void calculate_id(){
        this.id = (this.row * 8) + this.column;
    }
    public int calculate_row(string s){
        int low = 0;
        int up = 127;
        int half = 0;
        //Console.WriteLine("___ROW____");
        foreach (char _char in s)
        {
            half = (up - low) / 2;
            //Console.WriteLine("Half: {0}. ", half);

            if (_char == 'F'){               
                up -= half + 1;
            }
            if (_char == 'B'){
                low += half +1;
            }
            //Console.WriteLine("{0} -> From {1} to {2}. ", _char, low, up);
            
        }
       return low;
    }

    public int calculate_col(string s){
        int low = 0;
        int up = 7;
        int half = 0;
         //Console.WriteLine("___COLUMN____");
        foreach (char _char in s)
        {
            half = (up - low) / 2;
            //Console.WriteLine("Half: {0}. ", half);
            if (_char == 'L'){               
                up -= half + 1;
            }
            if (_char == 'R'){
                low += half + 1;
            }
            //Console.WriteLine("{0} -> From {1} to {2}. ", _char, low, up);
            
        }
        return up; 
    }
   
}