class Computer:
    
    #Attributes:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # The constructor (makes a computer with all its elements)
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int,
    memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price =  price


def main():
    pass

if __name__ == "__main__":
    main()

