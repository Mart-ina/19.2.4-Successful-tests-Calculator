import pytest
from app.calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator()

   def test_adding_success(self):
       assert self.calc.adding(12, 4) == 16         #сложение

   def test_subtraction_success(self):
       assert self.calc.subtraction(12, 4) == 8     #вычитание

   def test_division_success(self):                       #деление
        assert self.calc.division(12, 4) == 3.0

   def test_multiply_success(self):                       #умножение
        assert self.calc.multiply(12, 4) == 48

   def teardown(self):
       print ('Задание выполнено.')



