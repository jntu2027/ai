class water:
    def __init__(self):
        self.j1_capacity = int(input("Enter the water capacity of Jug 1:\t"))
        self.j2_capacity = int(input("Enter the water capacity of Jug 2:\t"))
        self.target = int(input("Enter the required water:\t"))
        self.max_depth = (self.j1_capacity*self.j2_capacity) - self.j1_capacity - self.j2_capacity
        self.cur_depth = 0
        self.solution = list()
        self.visited = set()
        self.start(0,0)
        
    def check(self,j1,j2):
        if (j1 == self.target or j2 == self.target):
            print("Found Solution")
            for i in self.solution:
                print(f"jug A: {i[0]}L    jug B: {i[1]}L")
            exit()
    
    def start(self,j1,j2):
        if (j1,j2) in self.visited:
            return
        
        self.visited.add((j1,j2))
        self.solution.append((j1,j2))
        
        if (self.cur_depth >=  self.max_depth ):
            self.solution.pop()
            return
        
        self.check(j1,j2)
        self.cur_depth += 1


        self.start( 0 , j2)
        self.start( j1 , 0)
        self.start(self.j1_capacity , j2)
        self.start(j1 , self.j2_capacity)
        self.start(j1 - min(j1,self.j2_capacity - j2), j2 + min(j1,self.j2_capacity - j2))
        self.start(j1 + min(j2,self.j1_capacity - j1), j2 - min(j2,self.j1_capacity - j1))
        
        
        self.cur_depth -= 1
        self.solution.pop()

water()