class salesman:
    def __init__(self,g,s):
        self.graph = g
        self.root = s
        self.distance = 0
        self.n = len(g)
        self.visited = [False for i in range(self.n)]
        self.path = []
        self.min_path = list()
        self.minimun = 100000
        self.start(self.root)
        self.prints()
        
    def prints(self):
        print("0",end="")
        for i in self.min_path:
            print(f" -> {i}",end="")
        print()
        print(f"Minimum Cost : {self.minimun}\t")
        
    def start(self , n):
        if (len(self.path) == self.n) and (self.path[-1] == self.root):
            self.minimun = self.distance
            self.min_path = self.path.copy()
        
        if (self.distance > self.minimun):
            return
        
        for i in range(self.n):
            if (not self.visited[i]) and (i != n):
                self.visited[i] = True
                self.path.append(i)
                self.distance += self.graph[n][i]
                self.start(i)
                self.distance -= self.graph[n][i]
                self.visited[i] = False
                self.path.pop()
                


distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]



salesman(distances,0)
