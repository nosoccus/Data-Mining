# LAB1 for IAD course
### Requirements:
- ✔️ Завантажити дані з DATABASE.csv.
  - Дані зберегти в структуру DataFrame.
  - Для правильного завантаження та конвертації даних створити функцію-парсер.
  - В якості індексного поля вибрати day/month (додати 2019 рік)
  - Коректно перетворити дані полів до відповідних типів даних (наприклад: 54 F –> 54, 6:50 PM –> 18:50)
- ✔️ Побудувати графіки для всіх полів отриманого DataFrame. 
  - Створити функцію, що виводить графіки любих типів даних та помістити її в окремий модуль.
  - Передбачити вивід одночасно декількох графіків.
  - Передбачити вивід легенди та підписів по осях.
  - Передбачити вибір типу графіків залежно від типу даних полів
- ✔️ Оформити модуль на репозиторії GitHub з відповідним описом установки та використання


### Notes:
- There is strange namings because of plagiarism check.
- File ```KN311_Holoven_main.py``` is main in the project. It contains preprocessing functions to standardize data and read ```csv``` to ```DataFrame```.
- File ```KN311_Holoven_plotter.py``` is module for making different plots of 4+ types. Also, there is capability to ovarlay plots or show several plots.


### How to run:
- Clone repository ```git clone https://github.com/nosoccus/Data-Mining-IAD.git```
- Install ```requirements.txt```.
- Run ```KN311_Holoven_main.py``` and follow instructions in console.
