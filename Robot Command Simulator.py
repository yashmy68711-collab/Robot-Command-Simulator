class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.directions = ["North", "East", "South", "West"]
        self.direction_index = 0
         self.history = []
        self.battery = 100

    def forward(self):
        if self.battery < 5:
            print("Not enough battery!")
            return
        direction = self.directions[self.direction_index]

        if direction == "North":
            self.y += 1
        elif direction == "South":
            self.y -= 1
        elif direction == "East":
            self.x += 1
        elif direction == "West":
            self.x -= 1

        self.battery -= 5
        self.history.append("Forward")
        print("Robot moved forward")

    def back(self):
        if self.battery < 5:
            print("Not enough battery!")
            return
        direction = self.directions[self.direction_index]

        if direction == "North":
            self.y -= 1
        elif direction == "South":
            self.y += 1
        elif direction == "East":
            self.x -= 1
        elif direction == "West":
            self.x += 1

        self.battery -= 5
        self.history.append("Forward")
        print("Robot moved backward")

    def left(self):
        if self.battery < 2:
            print("Not enough battery!")
            return

        self.direction_index = (self.direction_index - 1) % 4
        self.battery -= 2
        self.history.append("Left Turn")
        print("Robot turned left")

    def right(self):
       if self.battery < 2:
            print("Not enough battery!")
            return

        self.direction_index = (self.direction_index + 1) % 4
        self.battery -= 2
        self.history.append("Right Turn")
        print("Robot turned right")

    def status(self):
        print(f"Position: ({self.x}, {self.y})")
        print(f"Facing: {self.directions[self.direction_index]}")
        print(f"Battery: {self.battery}%")

        if self.battery < 20:
            print("Warning: Low Battery!")

    def show_history(self):
        if len(self.history) == 0:
            print("No movement history")
        else:
            print("\nMovement History:")
            for move in self.history:
                print("-", move)


robot = Robot()

while True:
    print("\n--- Robot Command Simulator ---")
    print("Commands: forward, back, left, right, status, exit")

    command = input("Enter command: ").lower().strip()

    if command == "forward":
        robot.forward()

    elif command == "back":
        robot.back()

    elif command == "left":
        robot.left()

    elif command == "right":
        robot.right()

    elif command == "status":
        robot.status()

    elif command == "exit":
        print("Simulation ended")
        break

    else:
        print("Invalid command")
