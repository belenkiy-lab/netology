set_a = {1, 2, 3, (1, 2)}
set_b = {3, 4, 5}
set_c = {4, 6, 7, "a"}

# print(set_a)

a = 1
# print(a)
# print(id(a))
# a = a + 2
# print(a)
# print(id(a))

# [1, 2, 3] [[3, 1, 5], [5, 3, 3], [1, 3, 5]]
# (1, 2, 3)
# {1, 2, 3}

# print(set_a & set_a)
# print({1, 2, 3, (1, 2)} & {1, (1, 2), 2, 3})
# set_a = {1, 2, 3, (1, 2)}
# print((2, 1) in set_a)
# {1, 2, 3, {1, 2)}}

# пересечение множеств - поиск одинаковых
# print(set_c & set_b & set_a)
# print(type(set_c & set_b & set_a))

# print(set_c.intersection(set_b))
# print(set_b.intersection(set_c, set_a))
# print(type(set())) #{}
# print(type(None)) #None

set_a = {1, 2, 3, (1, 2)}
# print(set_a)
# print(type(set_a))
set_b = {3, 4, 5}
set_c = {4, 6, 7, "a"}

# объединение множеств
# print(set_c | set_a | set_b)
# print(set_c.union(set_a, set_b))
# print("исходные множества:", set_a, set_b, set_c)

# set_d = set_c | set_a | set_b
# # vs
# set_c.update(set_a, set_b)

# # # объединение множеств №2
# print(set_c.update(set_a, set_b))
# print(set_c)
# print("исходные множества:", set_a, set_b, set_c)

set_a = {1, 2, 3, (1, 2)}
set_b = {3, 4, 5}
set_c = {4, 6, 7, "a"}

# разность множеств
# print(set_a - set_b - set_c)
# print(set_a.difference(set_b, set_c))
# print(set_a - (set_b - set_c))
# print(set_b - set_a - set_c)
# print(set_b - (set_a - set_c))

# {1, 2, 3, (1, 2)} - {4, 6, 7, "a"} -> {1, 2, 3, (1, 2)}
# {3, 4, 5} - {1, 2, 3, (1, 2)} -> {4, 5}

# симметрическая разность
set_a = {1, 2, 3, (1, 2)}
set_b = {3, 4, 5}
set_c = {4, 6, 7, "a"}

# print(set_a ^ set_b)
# print(set_b ^ set_a)

# print((set_a - set_b) | (set_b - set_a))

# print(set_a.symmetric_difference(set_b))
# print(set_b.symmetric_difference(set_a))

# print(set_a.symmetric_difference(set_b).symmetric_difference(set_c))

# set_c = {4, 6, 7, "a", (1, 2, (3, 4))}
# set_d = set_c
# set_e = set_c.copy()
# set_c.add("привет")
# print(set_c)
# print(set_e)
# print(id(set_c), id(set_e))

# print(len(set_c))
# set_c.add("привет")
# set_c.add((1, 2))
# print(set_c)

# if (1, 2) in set_c:
# 	set_c.remove((1, 2))
# print(set_c)
# if (1, 2) in set_c:
# 	set_c.remove((1, 2))
# set_c.discard((1, 2))
# print(set_c)

# любые числа, строки, bool, None, tuple

# print(set_c.discard((3, 2)))

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]
mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

set_py = set(mentors[0])
set_jv = set(mentors[1])
set_fs = set(mentors[2])
set_fe = set(mentors[3])

print(set_py & set_jv & set_fs & set_fe)
print(set_py & set_fs)
print(set_fs & set_fe)

print((set_py & set_fs) & (set_fs & set_fe))
print(len(set_py & set_fs))
print(len(set_fs & set_fe))

all_mentors_list = []
for m in mentors:
	all_mentors_list += m

print(all_mentors_list)
print(len(all_mentors_list))


all_mentors_set = set_py | set_jv | set_fs | set_fe
print(all_mentors_set)
print(len(all_mentors_set))

all_mentors_set = set(all_mentors_list)
print(all_mentors_set)
print(len(all_mentors_set))


# ДОПОЛНЕНИЕ К ЛЕКЦИИ.
# раскомментируйте код ниже, чтобы попробовать

# если тип данных неизменяемый, то у него есть метод __hash__()
# два подчеркивания в начале и конце имени - нужные!
# a = 1
# a.__hash__()

# а у изменяемого объекта нет хэша. потому что хэш - это постоянное значение.
# а объект-то изменяется, за ним не уследишь, тогда все хэши будут разные!
# test_set = set()
# test_set.__hash__() # здесь будет ошибка и код упадет, потому что у множества нет хэша