"""
This is a simple CLI tool to manage virtual machines locally using VirtualBox library.
"""
import virtualbox
from time import sleep

# Instance of virtualbox
vbox = virtualbox.VirtualBox()

# Dict to store available VMs and ids.
machines ={}

#Dict to store active sessions
sessions = {}

# Flag to stop execution loop
stop_program = False

def get_machines():
    """Retrieves all available machines and stores them in machines{}"""
    sleep(1) #Avoid quick showing
    id_count = 1 #counter for id
    for m in vbox.machines:
        machines[id_count] = m
        id_count += 1
        
def list_machines():
    """Lists all available machines in console"""
    get_machines()
    print("Available machines\n")
    print("ID \t \t NAME \t \t \t STATE")
    print("-----------------------------------------------------------------")
    for vm_id in machines:
        print(str(vm_id) + "  " + machines[vm_id].name + " " + str(machines[vm_id].state))
        print("")

def start_machine():
    """Starts a machine from the available ones"""
    list_machines() #Show available machines
    vm_id = int(input("Please write the ID of the machine you want to start: "))
    #Launching the machine
    session = virtualbox.Session()
    machine = vbox.find_machine(machines[vm_id].name)
    if machine.state == 5:
        print("Machine is already running!")
    else:
        progress = machine.launch_vm_process(session, "gui", [])
        progress.wait_for_completion()
        # Saving session
        sessions[vm_id] = session

        print("Machine succesfully started!")


def stop_machine():
    """Stops a machine from the available ones"""
    list_machines() #Show available machines
    vm_id = int(input("Please write the ID of the machine you want to shut down: "))
    # Getting Session object
    session = sessions[vm_id]
    # Shutting down the vm
    progress = session.console.power_down()
    progress.wait_for_completion()

    print("Machine succesfully shut down!")


def create_machine():
    """Creates a new machine in the root folder"""

def delete_machine():
    """Deletes a machine from the ones available"""
    list_machines()


# Execution loop
while not stop_program:
    sleep(1)
    print("=====================================")
    print("VM Manager\n")
    print("Options available:\n")
    print("1: Show available machines")
    print("2: Start a machine")
    print("3: Shut down a machine")
    print("4: Create a machine")
    print("5: Delete a machine")
    print("0: Exit\n")

    # User option
    u_opt = input("Please choose an option: ")

    if u_opt == "1":
        list_machines()
    if u_opt == "2":
        start_machine()
    if u_opt == "3":
        stop_machine()
    if u_opt == "4":
        create_machine()
    if u_opt == "5":
        delete_machine()
    if u_opt == "0":
        stop_program = True 