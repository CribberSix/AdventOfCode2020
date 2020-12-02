
using System; 
using System.Collections.Generic;


Example.Main();

public class Example {
    public static void Main(){
        
        // read input
        string[] lines = File.ReadAllLines("input.txt"); 

        // parse input
        List<Item> entries = new List<Item>();
        foreach (string item in lines)
            {  
            //Console.WriteLine(item);  
            string[] subs = item.Split(' ');

            string[] ranges = subs[0].Split('-');
            int s1 = Int16.Parse(ranges[0]);
            int s2 = Int16.Parse(ranges[1]);
            char c_char = char.Parse(subs[1].Substring(0,1)); 
            string password = subs[2];

            /*  I could also check for validity & count all valid lines here,
            but I want to try how Lists and Classes work in C# */
            Item temp =  new Item(s1, s2, password, c_char);
            entries.Add(temp);

            }
        // check each item for validity
        int valid_items = 0;
        foreach (Item i in entries)
        {
            /*
            if (i.is_valid_part1()){
                valid_items ++;
            }
            */
            if (i.is_valid_part2()){
                valid_items ++;
            }
        }
        Console.WriteLine("Number of valid passwords: " + Convert.ToString(valid_items));
    }
}




public class Item
    {
            public int s1;
            public int s2;
            public string password;
            public char c_char;

            public Item(int x, int y, string pw, char c){
                this.s1 = x - 1; // for part 1, remove "-1" -> part2: 'no concept of index-zero'
                this.s2 = y - 1; // for part 1, remove "-1" -> part2: 'no concept of index-zero'
                this.password = pw;
                this.c_char = c;
            }

            public bool is_valid_part1(){
                int occ = this.count_occurences(this.c_char, this.password);
                if (this.s1 <= occ && occ <= this.s2){
                    return true;
                } else {                    
                    return false;
                }
            }

            public bool is_valid_part2(){
                if ((this.password[this.s1] == this.c_char && this.password[this.s2] != this.c_char) || (this.password[this.s1] != this.c_char && this.password[this.s2] == this.c_char)){
                    return true;    
                } else {
                    return false;
                }
            }

            public int count_occurences(char c, string to_look_in){
                int counter = 0; 
                foreach (char s in to_look_in)
                {
                    if (s == c){
                        counter ++;
                    }                    
                }
                return counter; 
            }
    }
