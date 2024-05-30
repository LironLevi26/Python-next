def check_id_valid(id_number):
    """
    Checks if an Israeli ID number is valid.

    :param id_number: int, the ID number to check
    :return: bool, True if the ID number is valid, False otherwise
    """
    id_str = str(id_number).zfill(9)  # Ensure the ID is 9 digits, padding with zeros if necessary
    total = 0
    for i, digit in enumerate(id_str):
        num = int(digit)
        if i % 2 == 0:
            total += num
        else:
            double_num = num * 2
            if double_num > 9:
                double_num = double_num // 10 + double_num % 10
            total += double_num
    return total % 10 == 0



class IDIterator:
    """
    Iterator class for generating valid Israeli ID numbers starting from a given ID.
    """

    def __init__(self, id_):
        """
        Initializes the iterator with a starting ID.

        :param id_: int, the starting ID number
        """
        self.id_ = id_

    def __iter__(self):
        """
        Returns the iterator object itself.

        :return: IDIterator, the iterator instance
        """
        return self

    def __next__(self):
        """
        Returns the next valid ID number in the sequence.

        :return: int, the next valid ID number
        :raises StopIteration: when the ID exceeds 999999999
        """
        self.id_ += 1
        while self.id_ <= 999999999:
            if check_id_valid(self.id_):
                return self.id_
            self.id_ += 1
        raise StopIteration



def id_generator(id_):
    """
    Generator function for producing valid Israeli ID numbers starting from a given ID.

    :param id_: int, the starting ID number
    :yield: int, the next valid ID number
    """
    id_ += 1
    while id_ <= 999999999:
        if check_id_valid(id_):
            yield id_
        id_ += 1



def main():
    """
    Main function to run the ID generation program.
    It asks the user for an ID number and whether to use an iterator or generator
    to produce the next 10 valid ID numbers.
    """
    id_number = int(input("Enter ID: "))
    method = input("Generator or Iterator? (gen/it)? ").strip().lower()

    if method == "it":
        id_iter = IDIterator(id_number)
        for _ in range(10):
            print(next(id_iter))
    elif method == "gen":
        id_gen = id_generator(id_number)
        for _ in range(10):
            print(next(id_gen))
    else:
        print("Invalid input. Please enter 'gen' or 'it'.")


if __name__ == '__main__':
    main()
