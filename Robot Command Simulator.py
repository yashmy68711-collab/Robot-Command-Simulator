class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.directions = ["North", "East", "South", "West"]
        self.direction_index = 0

    def forward(self):
        direction = self.directions[self.direction_index]

        if direction == "North":
            self.y += 1
        elif direction == "South":
            self.y -= 1
        elif direction == "East":
            self.x += 1
        elif direction == "West":
            self.x -= 1

        print("Robot moved forward")

    def back(self):
        direction = self.directions[self.direction_index]

        if direction == "North":
            self.y -= 1
        elif direction == "South":
            self.y += 1
        elif direction == "East":
            self.x -= 1
        elif direction == "West":
            self.x += 1

        print("Robot moved backward")

    def left(self):
        self.direction_index = (self.direction_index - 1) % 4
        print("Robot turned left")

    def right(self):
        self.direction_index = (self.direction_index + 1) % 4
        print("Robot turned right")

    def status(self):
        print(f"Position: ({self.x}, {self.y})")
        print(f"Facing: {self.directions[self.direction_index]}")


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