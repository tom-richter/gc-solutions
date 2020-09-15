# Solution for GC8ZV5N - Herbstzeit - Pilzzeit #5

from itertools import combinations

pots = [
    ['dot', '1', 'lid', 'dotted'],
    ['square', '2', 'lid', 'dotted'],
    ['square', '2', 'handle', 'dotted'],
    ['square', '1', 'none', 'striped'],
    ['dot', '1', 'none', 'dark'],
    ['triangle', '2', 'none', 'dotted'],
    ['square', '1', 'lid', 'dark'],
    ['triangle', '1', 'lid', 'dotted'],
    ['dot', '3', 'lid', 'dotted'],
    ['dot', '3', 'lid', 'dark'],
    ['triangle', '1', 'none', 'dark'],
    ['triangle', '2', 'lid', 'dotted'],
]


def compare_attributes(attr1, attr2, attr3):
    return (attr1 == attr2 and attr2 == attr3) or (attr1 != attr2 and attr2 != attr3 and attr1 != attr3)


def compare_pots(pot1, pot2, pot3):
    return (compare_attributes(pot1[0], pot2[0], pot3[0]) and compare_attributes(pot1[1], pot2[1], pot3[1])
            and compare_attributes(pot1[2], pot2[2], pot3[2]) and compare_attributes(pot1[3], pot2[3], pot3[3]))


for selected_pots in combinations(range(0, 12), 3):
    if compare_pots(pots[selected_pots[0]], pots[selected_pots[1]], pots[selected_pots[2]]):
        print("Selected Pots:", selected_pots[0]+1, selected_pots[1]+1, selected_pots[2]+1,)
