# БЛОК ИНТЕРАКТИВА
import time

n = 10_000
print(f"\n==========\nСкорость поиска в списке и множестве из {n} элементов\n==========")

# функция, сравнивающая два списка
def fn1(x, y):
	print(f"\nСравнение двух списков из {len(x)} элементов. Первые 10 элементов:")
	print(x[:10])
	print(y[:10])
	start = time.time()
	z = []
	for x1 in x:
		for y1 in y:
			if x1 == y1:
				z.append(y1)
	print(f"Длительность выполнения: {time.time() - start} cек")
	print(f"Совпало элементов: {len(z)}")

# функция, сравнивающая два множества
def fn2(x, y):
	print(f"\nСравнение двух множеств из {len(x)} элементов. Первые 10 элементов:")
	print(list(x)[:10])
	print(list(y)[:10])
	start = time.time()
	z = x & y
	print(f"Длительность выполнения: {time.time() - start} сек")
	print(f"Совпало элементов: {len(z)}")

# в каждом списке у нас по 10 тыс элементов
xl = list(range(1,n+1))
yl = list(range(1,n+1))

# выводим первые 10 элементов (для иллюстрации) и вызываем функцию сравнения списков
fn1(xl, yl)

# будет ли работать дольше, если развернуть второй список?
print("\nПусть первый список теперь идет в прямом направлении, а второй - в обратном")
yl.reverse()
fn1(xl, yl)

# выводим первые 10 элементов (для иллюстрации) и вызываем функцию сравнения множеств
xs = set(xl)
ys = set(yl)					
fn2(xs, ys)