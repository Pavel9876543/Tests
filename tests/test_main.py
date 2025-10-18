import pytest

from Task1 import solve
from Task2 import solution
from Task3 import vote

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
count_person = 5
expected = ['Салат: картофель 500 гр., морковь 250 гр., огурцы 250 гр., горошек 150 гр., майонез 350 мл.',
                      'Пицца: сыр 250 гр., томаты 250 гр., тесто 500 гр., бекон 150 гр., колбаса 150 гр., грибы 100 гр.',
                      'Фруктовый десерт: хурма 300 гр., киви 300 гр., творог 300 гр., сахар 50 гр., мед 250 мл.']

params_solve = ((cook_book, count_person, expected),)

@pytest.mark.parametrize(
    'cook_book,count_person,expected',
    params_solve
)
def test_solve_params(cook_book, count_person, expected):
    assert solve(cook_book, count_person) == expected


params_solution = ((1, 8, 15, (-3.0, -5.0)), (1, -13, 12, (12.0, 1.0)), (-4, 28, -49, 3.5), (1, 1, 1, "корней нет"))
@pytest.mark.parametrize(
    'x,y,z,expected',
    params_solution
)
def test_solution_params(x, y, z, expected):
    assert solution(x, y, z) == expected

params_vote = (([1,1,1,2,3], 1), ([1,2,3,2,2], 2))
@pytest.mark.parametrize(
    'list_votes, expected',
    params_vote
)
def test_vote_params(list_votes, expected):
    assert vote(list_votes) == expected