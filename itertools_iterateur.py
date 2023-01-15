from itertools import count, cycle, repeat
import operator

compteur = count(34, 2)
cycleur = cycle([23, 'Japon', 45.6])
repetiteur = repeat([34, 3])
print(compteur, type(compteur))
print(cycleur, type(cycleur))
print(repetiteur, type(repetiteur))


def print_elements(tool):
  n = 0
  N = 20
  for element in tool:
    print(element, sep=",")
    if n > N:
      break
    n += 1


print("\nCompteur")
print_elements(compteur)
print("\nCycleur")
print_elements(cycleur)
print("\nRepetiteur")
print_elements(repetiteur)

# Appliquer une fonction aux éléments d'un flux de données
lst_carre = map(lambda x: x * x, count(2, 10))
lst_carre = map(operator.pow, count(2, 10), repeat(2))

print("\nlst_carre")
print_elements(lst_carre)

# Difference entre cycle et repeat
#for i in repeat("abcd"): print(i)
# réponse: "abcd", "abcd", "abcd", ...

#for i in cycle("abcd"): print(i)
# réponse: a, b, c, d, a, b, c, d, a, b, c, d, ...
