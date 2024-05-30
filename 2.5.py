class Animal:
    """
    A base class to represent an animal.
    Attributes:
    zoo_name - str : The name of the zoo where the animals are housed (class attribute).
    _name - str : The name of the animal.
    _hunger - int : The hunger level of the animal. Default is 0.
    """
    zoo_name = "Hayaton"
    def __init__(self, _name, _hunger=0):
        self._name = _name
        self._hunger = _hunger

    def get_name(self):
        """
        Returns the name of the animal.
        """
        return self._name

    def is_hungry(self):
        """
        Returns True if the animal is hungry (hunger > 0), otherwise False.
        """
        return self._hunger > 0

    def feed(self):
        """
        Decreases the animal's hunger by 1 if it is greater than 0.
        """
        if self._hunger > 0:
            self._hunger -= 1

    def talk(self):
        """
        A placeholder method to be overridden in subclasses for animal-specific sounds.
        """
        pass

class Dog(Animal):
    """
    A class to represent a dog, inheriting from Animal.
    """
    def talk(self):
        """
        Prints the sound a dog makes.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        Prints a message indicating the dog fetched a stick.
        """
        print("There you go, sir!")


class Cat(Animal):
    """
    A class to represent a cat, inheriting from Animal.
    """
    def talk(self):
        """
        Prints the sound a cat makes.
        """
        print("meow")

    def chase_laser(self):
        """
        Prints a message indicating the cat is chasing a laser.
        """
        print("Meeeeow")


class Skunk(Animal):
    """
    A class to represent a skunk, inheriting from Animal.
    Attributes:
    _stink_count - int : The number of times the skunk can spray. Default is 6.
    """
    def __init__(self, _name, _hunger=0, _stink_count=6):
        super().__init__(_name, _hunger)
        self._stink_count = _stink_count

    def talk(self):
        """
        Prints the sound a skunk makes.
        """
        print("tsssss")

    def stink(self):
        """
        Prints a message indicating the skunk is spraying.
        """
        print("Dear lord!")


class Unicorn(Animal):
    """
    A class to represent a unicorn, inheriting from Animal.
    """
    def talk(self):
        """
        Prints the sound a unicorn makes.
        """
        print("Good day, darling")

    def sing(self):
        """
        Prints a message indicating the unicorn is singing.
        """
        print("I’m not your toy...")


class Dragon(Animal):
    """
    A class to represent a dragon, inheriting from Animal.
    Attributes:
    _color - str : The color of the dragon. Default is "Green".
    """
    def __init__(self, _name, _hunger=0, _color="Green"):
        super().__init__(_name, _hunger)
        self.color = _color

    def talk(self):
        """
        Prints the sound a dragon makes.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        Prints a message indicating the dragon is breathing fire.
        """
        print("$@#$#@$")


def main():
    # Create instances of each animal with the given attributes
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcfly = Dragon("McFly", 80)

    # Store all instances in a list called zoo_lst
    zoo_lst = [brownie, zelda, stinky, keith, lizzy, doggo, kitty, stinky_jr, clair, mcfly]

    # Loop through the animals in zoo_lst
    for animal in zoo_lst:
        # If the animal is hungry, print its type and name, then feed it until it's no longer hungry
        if animal.is_hungry():
            print(f"{animal.__class__.__name__} {animal.get_name()}")
            while animal.is_hungry():
                animal.feed()
        # Call the talk method for each animal
        animal.talk()

        # Call the special method for each animal based on its type
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # Print the zoo_name class attribute
    print(f"Zoo name: {Animal.zoo_name}")

if __name__ == '__main__':
 main()