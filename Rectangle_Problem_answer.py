class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Define a generator to yield the length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(10, 20)

for dimension in rect:
    print(dimension)
