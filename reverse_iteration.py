class reverse_iter:
    def __init__(self,n):
        self.n=n
        self.i=len(self.n)-1
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.i>=0:
            i=self.i
            self.i-=1
            return self.n[i]
        if self.i<0:
            raise StopIteration()

z=reverse_iter([1, 2, 3, 4])
print(list(z))




