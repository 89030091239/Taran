class Cat:
    """Создадим еще отдельный файл под названием testCat.py, для того,
        чтобы реализовать наследование.
        Причем обязательно в той папке, где находится cat_21_7_1.py"""

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age
