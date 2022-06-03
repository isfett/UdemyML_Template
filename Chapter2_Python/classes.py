# C++, Java, PHP, C#: this

class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def jump(self):
        print("Jump!")


def main():
    dog = Animal(10, 0.8)
    print(dog, dog.weight, dog.height)
    dog.jump()

    cat = Animal(3, 0.3)
    print(cat, cat.weight, cat.height)
    cat.jump()


if __name__ == "__main__":
    main()
