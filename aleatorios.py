"""
AOA T4
Nel Penin Yele

"""



class Aleat :

    '''
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    '''
 
    def __init__(self, *, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0

    def __next__(self):
        self.x0 = (self.a * self.x0 + self.c) % self.m
        return self.x0
    
    def __call__(self, x0, /):
        self.x0 = x0

def aleat(*, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """

  
    x = x0
    while True:
        nx = (a * x + c) % m
        nsemilla = (yield new_x)
        if nsemilla is not None:
            x = nsemilla
        else:
            x = nx

if __name__ == "__main__":
    import doctest
    doctest.testmod()
     



