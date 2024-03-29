## Порівняння результатів Методу Монте-Карло та Аналітичних Розрахунків

Я недавно почала вивчати алгоритми та програмування, і одним із завдань, яке я вирішила, було моделювання кидання двох кубиків і обчислення ймовірностей для кожної можливої суми.

### Метод Монте-Карло

Для цього завдання я скористалася Методом Монте-Карло. Я випадковим чином кинула 1 мільйон пар кубиків і записала суму очок. Потім я обчислила ймовірність для кожної можливої суми.

Отримані результати для ймовірностей сум:

- Сума 10: 8.29% (3/36)
- Сума 6: 13.93% (5/36)
- Сума 7: 16.64% (6/36)
- Сума 9: 11.11% (4/36)
- Сума 5: 11.17% (4/36)
- Сума 12: 2.79% (1/36)
- Сума 2: 2.78% (1/36)
- Сума 3: 5.55% (2/36)
- Сума 4: 8.35% (3/36)
- Сума 8: 13.83% (5/36)
- Сума 11: 5.56% (2/36)

### Аналітичні Розрахунки

У завданні були наведені аналітичні розрахунки для цієї задачі:

- Сума 10: 8.33% (3/36)
- Сума 6: 13.89% (5/36)
- Сума 7: 16.67% (6/36)
- Сума 9: 11.11% (4/36)
- Сума 5: 11.11% (4/36)
- Сума 12: 2.78% (1/36)
- Сума 2: 2.78% (1/36)
- Сума 3: 5.56% (2/36)
- Сума 4: 8.33% (3/36)
- Сума 8: 13.89% (5/36)
- Сума 11: 5.56% (2/36)

### Порівняння результатів

Я порівняла результати, і вони виявилися досить близкими один до одного. Це означає, що Метод Монте-Карло надає достатньо точні результати для даної задачі, особливо з великою кількістю спроб (у моєму випадку 1 мільйон).

| Сума | Метод Монте-Карло | Аналітичні Розрахунки |
| ---- | ----------------- | --------------------- |
| 2    | 2.78% (1/36)      | 2.78% (1/36)          |
| 3    | 5.55% (2/36)      | 5.56% (2/36)          |
| 4    | 8.35% (3/36)      | 8.33% (3/36)          |
| 5    | 11.17% (4/36)     | 11.11% (4/36)         |
| 6    | 13.93% (5/36)     | 13.89% (5/36)         |
| 7    | 16.64% (6/36)     | 16.67% (6/36)         |
| 8    | 13.83% (5/36)     | 13.89% (5/36)         |
| 9    | 11.11% (4/36)     | 11.11% (4/36)         |
| 10   | 8.29% (3/36)      | 8.33% (3/36)          |
| 11   | 5.56% (2/36)      | 5.56% (2/36)          |
| 12   | 2.79% (1/36)      | 2.78% (1/36)          |

### Висновок

Навчання та використання Методу Монте-Карло було цікавим досвідом для мене. Це потужний інструмент для моделювання ймовірностей та інших складних систем.
