import matcensor

'''
    Тест модуля #1.
    Основные функции    
'''

'''
    Доступные базы:
    - ignorelist - слова для игнора модулем (исключения)
    - badlist - сами плохие слова
'''

# Объявляем главный класс модуля
mats = matcensor.MatProtect()

# Строка с "плохими словами"
string = 'Я еб*л твою мамашу!'

# Узнаем, есть ли в строке "плохие слова"
print(mats.checkCensor(obj=string))

# Обновляем базу ignorelist с добавлением слова "бляхи", как исключение из слов
print(mats.updateDB(db='ignorelist',word='бляхи'))
