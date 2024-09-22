class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will use the setter for validation
        self.condition = "Used"  # Default condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise ValueError("size must be an integer")
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
