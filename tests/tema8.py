# class Dreptunghi:
#     lungime = ""
#     latime = ""
#     culoare = ""
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         return f"Dreptunghiul meu are {self.lungime} cm lungime , {self.latime} cm latime si e de culoare {self.culoare}"
#
#     def aria(self):
#         return self.latime * self.lungime
#
#     def perimetru(self):
#         return (self.latime + self.lungime) * 2
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#----------------------------------------------------------------------------------------------------------------

from local_scripts.dreptunghi import Dreptunghi


def test_descrie():
    dreptunghi = Dreptunghi(5,6,"verde")
    actual = dreptunghi.descrie()
    expected = f"Dreptunghiul meu are 5 cm lungime , 6 cm latime si e de culoare verde"
    assert actual == expected


def test_aria():
    dreptunghi = Dreptunghi(5,6,"verde")
    actual = dreptunghi.aria()
    expected = 30
    assert actual == expected


def test_perimetru():
    dreptunghi = Dreptunghi(5,6,"verde")
    actual = dreptunghi.perimetru()
    expected = 22
    assert actual == expected

def test_schimba_culoarea():
    dreptunghi = Dreptunghi(5,6,"verde")
    dreptunghi.schimba_culoarea("negru")
    actual = dreptunghi.descrie()
    expected = f"Dreptunghiul meu are 5 cm lungime , 6 cm latime si e de culoare negru"
    assert actual == expected



