def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    D = b ** 2 - 4 * a * c
    return D


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        return "корней нет"


if __name__ == '__main__':
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)