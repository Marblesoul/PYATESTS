def solve(phrases: list):
    result = []
    for phrase in phrases:
        cut_phrase = phrase.replace(" ", "")
        print(cut_phrase)
        if cut_phrase == cut_phrase[::-1]:
           result.append(phrase)
    return result

if __name__ == '__main__':
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = solve(phrases)
    assert result == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"], f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")
