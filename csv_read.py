import csv
def open_csv(path):
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter = ',') 
    header = next(reader) 
    data = []
    for row in reader:
      iter_tuple = zip(header, row) 
      dictionary = { key: value for (key, value) in iter_tuple}
      data.append(dictionary)
      
    return data

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

def population_country(lista, country):
  for dicty in lista:
    if dicty['Country/Territory'] == country:
      population_dict = {
        '2022': int(dicty['2022 Population']),
        '2020': int(dicty['2020 Population']),
        '2015': int(dicty['2015 Population']),
        '2010': int(dicty['2010 Population']),
        '2000': int(dicty['2000 Population']),
        '1990': int(dicty['1990 Population']),
        '1980': int(dicty['1980 Population']),
        '1970': int(dicty['1970 Population']),
      }
  return population_dict.keys(), population_dict.values()

def population_mundial(lista):
  population = {}
  for element in lista:
    population[element['Country/Territory']] = element['World Population Percentage']
  labels = population.keys()
  values = population.values()
  return labels, values

if __name__ == '__main__':
  data = open_csv('./Data/population.csv')
  option = int(input('Para ver la poblacion de un pais digite 1 \nPara ver la poblacion mundial digite 2 \n==> '))
  if option == 1:
    country = input('Digite el pais del cual desea ver su crecimiento poblacional => ')
    labels, values = population_country(data, country)
    print(generate_bar_chart(labels, values))
  elif option == 2:
    labels, values = population_mundial(data)
    print(generate_pie_chart(labels, values))
  else: 
    print('Seleccion incorrecta')

  