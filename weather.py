# Для работы используется плагин pyowm
#Задание №1 3а.

from pyowm import OWM

owm = OWM('API KE')
place = input('Введи название вашего города')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

#Показатели
#Температура
t = w.temperature('celsius')
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

#статус данных
sts = w.status
#Время
time = w.reference_time('iso')
#Вывод данных print

print(f'В городе {place}, время {time} текущая температура{t1} градусов цельсия, ощущается как{t2} градусов цельсия, температура ночью{t4} градусов цельсия')
