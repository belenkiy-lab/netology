def reverse(string: str) -> str:
    return(string.lower()[::-1])


if __name__ == '__main__':
    assert reverse('!dlroW olleH') == 'hello world!'
    assert reverse('AvadaKedavraaaaA!') == '!aaaaarvadekadava'
    assert reverse('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я') == 'я наконец-то разобрался в этих ваших срезах'
    print("\nОтличная работа, отправляйте на проверку!")
ve