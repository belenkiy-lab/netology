def solve(boys: list, girls: list):
    if len(boys) == len(girls): 
        pairs = [f"{boy} и {girl}" for boy, girl in zip(sorted(boys), sorted(girls))]
        result = ", ".join(pairs)
    else:
        result = "Кто-то может остаться без пары!"
    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = solve(boys, girls)
    assert result == "Кто-то может остаться без пары!", f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")
