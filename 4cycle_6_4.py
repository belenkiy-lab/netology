def solve(cook_book: list, person: int):
    result = []
    for dish in cook_book:
        ingredients = ", ".join([f"{ingredient[0]} {ingredient[1] * person} {ingredient[2]}" for ingredient in dish[1]])
        dish_recipe = f"{dish[0]}: {ingredients}"
        result.append(dish_recipe)
    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    cook_book = [
      ['Салат',
          [
            ['картофель', 100, 'гр.'],
            ['морковь', 50, 'гр.'],
            ['огурцы', 50, 'гр.'],
            ['горошек', 30, 'гр.'],
            ['майонез', 70, 'мл.'],
          ]
      ],
      ['Пицца',
          [
            ['сыр', 50, 'гр.'],
            ['томаты', 50, 'гр.'],
            ['тесто', 100, 'гр.'],
            ['бекон', 30, 'гр.'],
            ['колбаса', 30, 'гр.'],
            ['грибы', 20, 'гр.'],
          ],
      ],
      ['Фруктовый десерт',
          [
            ['хурма', 60, 'гр.'],
            ['киви', 60, 'гр.'],
            ['творог', 60, 'гр.'],
            ['сахар', 10, 'гр.'],
            ['мед', 50, 'мл.'],
          ]
      ]
    ]

    result = solve(cook_book, 5)
    assert result == ['Салат: картофель 500 гр., морковь 250 гр., огурцы 250 гр., горошек 150 гр., майонез 350 мл.',
                      'Пицца: сыр 250 гр., томаты 250 гр., тесто 500 гр., бекон 150 гр., колбаса 150 гр., грибы 100 гр.',
                      'Фруктовый десерт: хурма 300 гр., киви 300 гр., творог 300 гр., сахар 50 гр., мед 250 мл.'],\
            f"Неверный результат: {result}"
    print(f"Список покупок на 5 персон: {result}")