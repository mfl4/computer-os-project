class ClassExploration(object):
    name = str(input("Enter your name: "))

    def show_title(self):
        message = f"Welcome to Class Exploration, {name}"
        return message


ce = ClassExploration()
print(ce.show_title())
