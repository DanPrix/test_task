'''Функция расчёта стоимости доставки'''
def get_cost(path_len:float, size:str, delicate:bool, workload = 1.0):
  '''Проверка типов переменных'''
  if not(type(path_len) == int) and not(type(path_len) == float):
    return "Некорректный тип расстояния"
  if not(type(size) == str):
    return "Некорректный тип габаритов"
  if not(type(delicate) == bool):
    return "Некорректный тип хрупкости"
  if not(type(workload) == int) and not(type(workload) == float):
    return "Некорректный тип загрузки"
  wl_list = [1,1.2,1.4,1.6]
  size_list = ['s','b']
  cost = 0
  '''Проверка расстояния'''
  if 0 < path_len <= 2:
    cost += 50
  elif 0 < path_len <= 10:
    cost += 100
  elif 0 < path_len <= 30:
    cost += 200
  elif path_len > 30:
    cost += 300
  else:
    return "Некорректное значение расстояние"
  '''Проверка габаритов'''
  if size in size_list:
    if size == 's':
      cost += 100
    else:
      cost += 200
  else:
    return "Некорректные габариты"
  '''Проверка хрупкости'''
  if delicate and path_len > 30:
    return "Хрупкие грузы нельзя возить на расстояние более 30 км"
  elif delicate and not path_len > 30:
    cost += 300
  '''Проверка загруженности'''
  if workload in wl_list:
    cost *= workload
  '''Проверка на минимальную стоимость'''
  if cost < 400:
    return 400
  else:
    return cost