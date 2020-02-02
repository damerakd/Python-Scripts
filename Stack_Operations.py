class MinStack:

    def __init__(self):
        self.list = []
         
    def push(self, x: int) -> None:
        self.list.append(x)
        
    def pop(self) -> None:
        self.list.pop()

    def top(self) -> int:
        return self.list[len(self.list) - 1]

    def getMin(self) -> int:
        if len(self.list) == 0:
            return 0
        return min(self.list)