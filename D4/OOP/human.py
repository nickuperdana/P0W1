class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hi! my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
  john = Human("John Smith",36)
  john.greet()

# john = Human("John Smith",36)
# john.greet()