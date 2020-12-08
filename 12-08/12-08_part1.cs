

// get input
string[] lines = File.ReadAllLines("input.txt"); 
//parsing
List<Step> command_list = new List<Step>(); 
foreach (string line in lines) {
    string[] subs = line.Split(' ');
    Step s = new Step(subs[0], int.Parse(subs[1]));
    command_list.Add(s);
}

// Logic

List<int> executed_steps = new List<int>();
executed_steps.Add(10);
int current_step_index = 0;
int accumulation = 0;

while (executed_steps.Contains(current_step_index)== false) {

    if (current_step_index >= command_list.Count){
        Console.WriteLine("Programm terminates now with zero-index {0} and length {1}.", current_step_index, command_list.Count);
        break;
    }

    Console.WriteLine("Current Line is {0}", current_step_index);
    executed_steps.Add(current_step_index);

    Step current = command_list[current_step_index];

    if (current.command == "acc"){
        accumulation += current.number;
        current_step_index ++;
    } else if (current.command == "nop"){
        current_step_index ++;
    } else if (current.command == "jmp"){
        current_step_index += current.number;
    }

}

Console.WriteLine("_______________");
Console.WriteLine("Next Line would be {0}.", current_step_index);
Console.WriteLine("The accumulation variable is {0}.", accumulation);



public class Step {

    public string command; 
    public int number;

    public Step(string command, int number){
        this.command = command;
        this.number = number;
    }

    public void print(){
         Console.WriteLine("command: {0} with {1}", this.command, this.number);
    }

}