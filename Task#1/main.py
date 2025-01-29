def solve(boys: list, girls: list) -> str:
    result = ""
    pair = []
    if len(boys) == len(girls):
        for boy, girl in zip(sorted(boys), sorted(girls)):
            pair.append(f'{boy} и {girl}')
        result = ", ".join(pair)
    else:
        result = "Кто-то может остаться без пары!"
    return result


if __name__ == '__main__':
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    print(solve(boys, girls))