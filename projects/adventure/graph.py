import random
from linked_list import LinkedList

# create stack class
class Stack:
    def __init__(self):
        self.stack = []  # points to empty stack

    # add value to end of stack
    def push(self, value):
        self.stack.append(value)

    # remove value from front of stack
    def pop(self):
        # check if stack is empty
        if self.size() > 0:
            # if not, pop last value out of stack
            return self.stack.pop()
        else:
            # if empty, return None
            return None

    # get size of the stack
    def size(self):
        return len(self.stack)


# create queue class
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size  # return size of the queue

    def enqueue(self, value):
        # insert tail to the queue
        self.storage.add_to_tail(value)
        self.size += 1  # increment size of queue by 1

    def dequeue(self):
        if self.size > 0:  # Check that there are items in the queue
            val = self.storage.remove_head()  # remove head of queue (first node) and store the value of the node removed
            self.size -= 1  # decrement size by 1
            return val  # return value of the removed node
        return None  # if there is nothing in the queue, return None

# create graph class
class Graph:
    def __init__(self, player):
        self.player = player
        self.visited = set()
        self.directory = {}
        self.path = []
    
    # get player's current room id
    def get_room_id(self):
        return self.player.current_room.id

    # get player's current room exits
    def get_exits(self):
        
        exits = []
        
        for exit in self.player.current_room.get_exits():
            exits.append(exit)

        return exits

    # create function for depth first traversal
    def dft(self, s=Stack()):

        # check if current room is in visited set
        current_room = self.get_room_id()

        print(f"You currently reside in room: {current_room}")
        if current_room not in self.visited:
            print(f"Current room {current_room} not in visited set")
            self.directory[current_room] = {}
            self.visited.add(current_room)
            print(f"Current room has been added to visited set: {self.visited}")
            for ex in self.get_exits():
                print(f"Getting exit: {ex}")
                s.push(ex)
                print(f"Added exit {ex} to stack")
                self.directory[current_room].update({ex : '?'})
                print(f"Updated directory of current room: {self.directory[current_room]}")
        elif '?' in self.directory[current_room].values():
            print(f"Current room found in visited set, but there still contains '?' exits: {self.directory[current_room]}")
            for ex in self.directory[current_room]:
                if self.directory[current_room][ex] == '?':
                    s.push(ex)

        else:
            print(f"Current room already in visited set: commencing bfs.")
            print(f"Current room exits include: {self.directory[current_room]}")
            s = Stack()
            print(f"Created new empty stack: {s.stack}")
            path = self.bfs()
            print(f"Created path to unvisited room: {path}")
            if path is None:
                return
            for room in path:
                print(f"Room {room} in path")
                if current_room == room:
                    print(f"This is the room you reside in: {room}")
                else:
                    print(f"You do not reside in this room {room}")
                    for direction in self.directory[current_room]:
                        print(f"Checking direction: {direction}")
                        if self.directory[current_room][direction] == room:
                            print(f"Path to room has been found")
                            self.player.travel(direction)
                            self.path.append(direction)
                            print(f"Player has moved to room {self.get_room_id()}")
                            print(f"Checking directory: {self.directory[self.get_room_id()]}")
                            print(f"Checking stack: {s.stack}")
                current_room = self.get_room_id()


        
        # while stack is not empty
        while s.size() > 0:
            current_room = self.get_room_id()
            print(f"Player's current room: {current_room}")
            print(f"Size of stack is greater than 0: {s.size()}")
            print(f"Stack currently holds: {s.stack}")
            # pop last value from stack and store it in variable
            direction = s.pop()
            print(f"Popped direction {direction} from end of stack. stack now holds: {s.stack}")
            if direction in self.directory[current_room].keys():
                if self.directory[current_room][direction] == '?':
                    print(f"Value of current room at position direction == ?: {self.directory[current_room][direction]}")
                    # move in the popped direction
                    self.player.travel(direction)
                    self.path.append(direction)
                    print(f"Player traveled to room: {self.get_room_id()}")
                    self.directory[current_room][direction] = self.get_room_id()
                    print(f"Updated direction to point to new room: {self.directory[current_room]}")
                    self.dft(s)


    def bfs(self, destination_room='?'):
        visited = set()
        path = Queue()
        current_room = self.get_room_id()
        path.enqueue([current_room])

        while path.size > 0:
            room_path = path.dequeue()
            # print(f"Room path: {room_path}")
            if room_path[-1] not in visited:
                visited.add(room_path[-1])
                # print(f"Visited: {visited}")
                # print(f"room_path: {room_path}")
                # print(f"Directory: {self.directory}")
                for ex in self.directory[room_path[-1]]:
                    # print(f"Exit: {ex}")
                    # print(f"Points to: {self.directory[room_path[-1]][ex]}")
                    if self.directory[room_path[-1]][ex] == '?':
                        return room_path
                    else:
                        path.enqueue(room_path + [self.directory[room_path[-1]][ex]])
            


    
