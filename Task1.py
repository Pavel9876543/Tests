def solve(cook_book: list, person: int):
    result = []
    res=""
    # самостоятельно напишите код решения:
    for cb in cook_book:
        res+=f"{cb[0]}: "
        for c in cb[1]:
            res+=f"{c[0]} {c[1]*person} {c[2]}, "
        result.append(res[:-2])
        res=""
    return result

