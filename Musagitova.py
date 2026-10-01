import platform
import os
import json

par = []
par.append(f"ОС: {platform.system()}")
par.append(f"Версия ОС: {platform.version()}")
par.append(f"Релиз ОС: {platform.release()}")
par.append(f" Сетевое имя ПК: {platform.node()}")
par.append(f"Модель процессора: {platform.processor()}")
par.append(f" Количество ядер процессора: {os.cpu_count()}")
par.append(f" разрядность: {platform.architecture()[0]}")
par.append(f"Модель процессора: {platform.machine()}")

with open('information.json', 'w', encoding='utf-8') as file:
    json.dump( par , file, ensure_ascii=False, indent=2)

# with open('information.json', 'r', encoding='utf-8') as file:
#     print(json.load(file))
