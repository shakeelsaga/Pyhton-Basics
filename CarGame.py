def car_game():
    is_started = False
    while True:
        cmd = input(">").lower()
        if cmd == "help":
            print("\nAvailable commands:\nstart - To start the Car\nstop - To stop the car\nquit - To exit the game\n")
        elif cmd == "start":
            if is_started:
                print("Car is already started.\n")
            else:
                is_started = True
                is_stopped = False
                print("Car started... Ready to go!\n")
        elif cmd == "stop":
            if not is_started:
                print("Car is already stopped.")
                print("You need to start the car first.\n")
            else:
                is_started = False
                is_stopped = True
                print("Car stopped.\n")
        elif cmd == "quit":
            print("Exiting the game. Goodbye!\n")
            break
        else:
            print("I don't understand that command. Type 'help' for a list of commands.\n")
            
if __name__ == "__main__":
    print("Welcome to the Car Game!\n")
    print("Type 'help' for a list of commands.\n")
    car_game()
    print("Thank you for playing!")