# documents = [
#     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
# ]
#
# directories = {
#     '1': ['2207 876234', '11-2', '5455 028765'],
#     '2': ['10006'],
#     '3': []
# }
#
#
# def check_document_existance(user_doc_number):
#     doc_founded = False
#     for current_document in documents:
#         doc_number = current_document['number']
#         if doc_number == user_doc_number:
#             doc_founded = True
#             break
#     return doc_founded
#
#
# def get_doc_owner_name(user_doc_number=''):
#     if not user_doc_number:
#         user_doc_number = input('Введите номер документа - ')
#     print()
#     doc_exist = check_document_existance(user_doc_number)
#     if doc_exist:
#         for current_document in documents:
#             doc_number = current_document['number']
#             if doc_number == user_doc_number:
#                 return current_document['name']
#
#
# def get_all_doc_owners_names():
#     users_list = []
#     for current_document in documents:
#         try:
#             doc_owner_name = current_document['name']
#             users_list.append(doc_owner_name)
#         except KeyError:
#             pass
#     return set(users_list)
#
#
# def remove_doc_from_shelf(doc_number):
#     for directory_number, directory_docs_list in directories.items():
#         if doc_number in directory_docs_list:
#             directory_docs_list.remove(doc_number)
#             break
#
#
# def add_new_shelf(shelf_number=''):
#     if not shelf_number:
#         shelf_number = input('Введите номер полки - ')
#     if shelf_number not in directories.keys():
#         directories[shelf_number] = []
#         return shelf_number, True
#     return shelf_number, False
#
#
# def append_doc_to_shelf(doc_number, shelf_number):
#     add_new_shelf(shelf_number)
#     directories[shelf_number].append(doc_number)
#
#
# def delete_doc():
#     user_doc_number = input('Введите номер документа - ')
#     doc_exist = check_document_existance(user_doc_number)
#     if doc_exist:
#         for current_document in documents:
#             doc_number = current_document['number']
#             if doc_number == user_doc_number:
#                 documents.remove(current_document)
#                 remove_doc_from_shelf(doc_number)
#                 return doc_number, True
#
#
# def get_doc_shelf():
#     user_doc_number = input('Введите номер документа - ')
#     doc_exist = check_document_existance(user_doc_number)
#     if doc_exist:
#         for directory_number, directory_docs_list in directories.items():
#             if user_doc_number in directory_docs_list:
#                 return directory_number
#
#
# def move_doc_to_shelf():
#     user_doc_number = input('Введите номер документа - ')
#     user_shelf_number = input('Введите номер полки для перемещения - ')
#     remove_doc_from_shelf(user_doc_number)
#     append_doc_to_shelf(user_doc_number, user_shelf_number)
#     print('Документ номер "{}" был перемещен на полку номер "{}"'.format(user_doc_number, user_shelf_number))
#
#
# def show_document_info(document):
#     doc_type = document['type']
#     doc_number = document['number']
#     doc_owner_name = document['name']
#     print('{} "{}" "{}"'.format(doc_type, doc_number, doc_owner_name))
#
#
# def show_all_docs_info():
#     print('Список всех документов:\n')
#     for current_document in documents:
#         show_document_info(current_document)
#
#
# def add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
#     # new_doc_number = input('Введите номер документа - ')
#     # new_doc_type = input('Введите тип документа - ')
#     # new_doc_owner_name = input('Введите имя владельца документа- ')
#     # new_doc_shelf_number = input('Введите номер полки для хранения - ')
#     new_doc = {
#         "type": new_doc_type,
#         "number": new_doc_number,
#         "name": new_doc_owner_name
#     }
#     documents.append(new_doc)
#     append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
#     return new_doc_shelf_number
#
#
# def secretary_program_start():
#     """
#     ap - (all people) - команда, которая выводит список всех владельцев документов
#     p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#     l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
#     s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
#     a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
#     имя владельца и номер полки, на котором он будет храниться.
#     d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
#     m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
#     as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
#     q - (quit) - команда, которая завершает выполнение программы
#     """
#     print(
#         'Вас приветствует программа помошник!\n',
#         '(Введите help, для просмотра списка поддерживаемых команд)\n'
#     )
#     while True:
#         user_command = input('Введите команду - ')
#         if user_command == 'p':
#             owner_name = get_doc_owner_name()
#             print('Владелец документа - {}'.format(owner_name))
#         elif user_command == 'ap':
#             uniq_users = get_all_doc_owners_names()
#             print('Список владельцев документов - {}'.format(uniq_users))
#         elif user_command == 'l':
#             show_all_docs_info()
#         elif user_command == 's':
#             directory_number = get_doc_shelf()
#             print('Документ находится на полке номер {}'.format(directory_number))
#         elif user_command == 'a':
#             print('Добавление нового документа:')
#             new_doc_shelf_number = add_new_doc()
#             print('\nНа полку "{}" добавлен новый документ:'.format(new_doc_shelf_number))
#         elif user_command == 'd':
#             doc_number, deleted = delete_doc()
#             if deleted:
#                 print('Документ с номером "{}" был успешно удален'.format(doc_number))
#         elif user_command == 'm':
#             move_doc_to_shelf()
#         elif user_command == 'as':
#             shelf_number, added = add_new_shelf()
#             if added:
#                 print('Добавлена полка "{}"'.format(shelf_number))
#         elif user_command == 'help':
#             print(secretary_program_start.__doc__)
#         elif user_command == 'q':
#             break
#
#
# if __name__ == '__main__':
#     secretary_program_start()

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

# В этот список будут добавляться словари-курсы
courses_list = []
# Допишите код, который генерирует словарь-курс с тремя ключами:
key = ["title", "mentors", "duration"]
def course_longer():
	global min, max
	for a, b, c in zip(courses, mentors, durations):
		course_dict = {key[0]:a, key[1]:b, key[2]:c}
		courses_list.append(course_dict)
	#print(courses_list)
	# Найдите самое маленькое и самое большое значение длительности курса
	# Подсказка: используйте функции min и max для списка durations
	min = min(durations)
	max = max(durations)
	# Как видите, в duration встречаются одинаковые длительности курса. Допишите код, который это учитывает
	# Подсказка 1: найдите индексы, по которым в списке durations встречается самое маленькое и самое большое значение
	# Подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate
	maxes = []
	minis = []
	for n, mm in enumerate(durations):
	 if mm == max:
	   maxes.append((courses_list[n])['title'])
	 elif mm == min:
		 minis.append((courses_list[n])['title'])
	# # Соберите все названия самых коротких и самых длинных курсов
	# # Так как курсов с одной длительностью может быть больше одного,
	# # создайте список названий самых коротких (courses_min) и самых длинных (courses_max) курсов
	#courses_min = []
	#courses_max = []
	#for id in minis:
	# 	courses_min.append(courses_list[...][...]) # Допишите код, который берёт по id нужный курс из courses_list и получает название курса из ключа "title"
	# for id in maxes:
	# 	courses_max.append(...) # По аналогии допишите такой же код для курсов максимальной длительности

	# # Допишите конструкцию вывода результата. Можете использовать string.join()
	print(f'Самый короткий курс(ы): {", ".join(minis)} - {min} месяца(ев)')
	print(f'Самый длинный курс(ы): {", ".join(maxes)} - {max} месяца(ев)')
	return (', '.join(minis), min), (', '.join(maxes), max)

# courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
#
# mentors = [
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]

def top_name():
# Добавьте сюда ваш код из Задачи 1
	all_list = []
	all_list=sum(mentors, [])
	all_names_list = []
	for mentor in all_list:
		name = mentor.split(' ')[0]
		all_names_list.append(name)
	# Уникальные имена будут в unique_names
	unique_names = all_names_list

	# Подсчитайте встречаемость каждого имени через list.count()
	popular = []
	temp = []
	for name in unique_names:
		if name not in temp:
			temp.append(name)
			popular.append([name, unique_names.count(name)]) # Добавьте подсчёт имён

	# Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
	# Используйте его, как есть, или напишите собственный :)
	popular.sort(key=lambda x:x[1], reverse=True)

	# Получите топ-3 часто встречающихся имён из списка popular
	# Подсказка: возьмите срез списка
	top_3 = []
	for name, count in popular[:3]:
		top_3.append(name + ': ' + str(count))
	print(f'{" раз(а), ".join(top_3)} раз(а)')
	return top_3

# Это вы мне? Подсчитываем тёзок на каждом курсе

# courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
# mentors = [
# 	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
# 	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
# 	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
# ]
# durations = [14, 20, 12, 20]
#
# courses_list = []
def same_names():
	gg = []
	for course, mentor, duration in zip(courses, mentors, durations):
		course_dict = {"title":course, "mentors":mentor, "duration":duration}
		courses_list.append(course_dict)
	for course in courses_list:
		f = []
		same_name_list = []

		for name in course['mentors']:
			f.append(name.split(' ')[0])
		for name in course['mentors']:
			k = name.split(' ')[0]
			if f.count(k) > 1:
				same_name_list.append(name)
		same_name_list.sort()
		cours = course['title']
		gg.extend([same_name_list])
		print(f'На курсе {cours} есть тёзки: {", ".join(same_name_list)}')
	return gg

if __name__ == '__main__':
	course_longer()
	top_name()
	same_names()