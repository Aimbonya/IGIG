from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0

    def calculate_area(self):
        self.area = self.height*self.width
        return self.area

    def main_params(self):
        return "Width: "+self.width+ "Length: "+ self.height+ "Area: "+ self.area


class Color:
    def __init__(self):
        self._color = None

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    color = property(get_color, set_color)


if __name__ == "__main__":
    print("Вывести на экран треугольник вписанный в окружность радиуса R")
    while True:
        try:
            z = int(input("Введите R"))
            break
        except ValueError:  # Exception for the wrong input
            print("Ошибка: число введено некорректно!")

