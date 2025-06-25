#[1, 3, 5] => 30
#[6] => 36
#[] => 0

lists = [
    [1, 3, 5],
    [6],
    []
]

for lst in lists:
    if len(lst) == 0:
        print(0)
    else:
        zero = 0
        for x in range(0, len(lst), 2):
            zero += lst[x]
        finish = zero * lst[-1]
        print(finish)