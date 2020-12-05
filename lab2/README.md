# LAB2 for IAD course
### Requirements:
- Написати скрипт – парсер для завантаження даних про динаміку поширення COVID-19 із [https://nszu.gov.ua/covid/dashboard](https://nszu.gov.ua/covid/dashboard)
- Вибрати дані по одній з областей України
- Згрупувати дані по ознаці “однакова дата” за операцією SUM
- За допомогою розробленої функції візуалізації даних побудувати динаміку активних, підозрілих, підтверджених, летальних, госпіталізованих хворих
- Провести порівняльний аналіз захворівших по різним областям
- Вивести статистичні дані по Україні на географічну карту
- Результати аналізу імпортувати в Excel
- Оформити модуль на репозиторії GitHub з відповідним описом установки та використання


### Notes:
- File ```main.py``` is main in the project. It contains preprocessing functions, parser from Github and scripts for teading Shapefiles.
- File ```plotter.py``` is module for building plots from the previous lab. Also there is a map visualization and a plot for comparing areas.
- ```UKR_adm.zip``` contains Shapefiles of Ukraine without transcription of areas, but with Kyiv.
- ```ukr_admbnda_adm1_q2_sspe_20171221.zip``` contains Shapefiles of Ukraine with transcription of areas, but without Kyiv.

### How to run:
- Clone repository ```git clone https://github.com/nosoccus/Data-Mining-IAD.git```
- Run ```main.py``` in ```lab2``` and follow instructions in console.
