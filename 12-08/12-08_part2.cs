

// get input
string[] lines = File.ReadAllLines("input.txt"); 
int length = lines.Length;
for (int i = 0; i < length; i++)
{
    string[] lines = File.ReadAllLines("input.txt"); 
    string[] subs = lines[i].Split(' ');
    
    if (subs[0] == "nop"){
        lines[i] = "jmp " + subs[1];
    } else if (subs[0] == "jmp"){
        lines[i] = "nop " +  subs[1];
    }
    
    if (run_code(lines)) {
        break;    
    }    
}


static bool run_code(string[] changed_lines){
    //parsing & creating Step objects
    List<Step> command_list = new List<Step>(); 
    foreach (string line in changed_lines) {
        string[] subs = line.Split(' ');
        command_list.Add(new Step(subs[0], int.Parse(subs[1])));
    }

    // Logic
    List<int> executed_steps = new List<int>();
    executed_steps.Add(10);
    int current_step_index = 0;
    int accumulation = 0;

    while (executed_steps.Contains(current_step_index)== false) {

        if (current_step_index >= command_list.Count){
            Console.WriteLine("Programm terminates in an orderly fashion with zero-index {0} and length {1}.", current_step_index, command_list.Count);
            Console.WriteLine("The accumulation variable is {0}.", accumulation);
            return true;
        }

        executed_steps.Add(current_step_index);

        Step current = command_list[current_step_index];
        // handling the current command
        if (current.command == "acc"){
            accumulation += current.number;
            current_step_index ++;
        } else if (current.command == "nop"){
            current_step_index ++;
        } else if (current.command == "jmp"){
            current_step_index += current.number;
        }

    }
    
    Console.WriteLine("Infinity loop detected!");
    return false;
}


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