import random

def both_random_fallow():
    rdm_places_m1 = random.sample(list(range(1,10000)),250)
    rdm_places_m2 = random.sample(list(range(1,10000)),250)

    m1_points = 0
    m2_points = 0

    m1 = random.choice([0,1])
    m2 = 0

    for i in range(1,1000):
        if i in rdm_places_m1: m1 = int(not m2)
        m2 = m1
        m2_points += m2
        if i in rdm_places_m2: m2 = int(not m1)
        m1 = m2
        m1_points += m1

    if m1_points == m2_points: return 0
    elif m1_points > m2_points: return 1
    else: return 2

if __name__ == "__main__":
    draw = 0
    m1_win = 0
    m2_win = 0
    for _ in range(0,100000):
        result = both_random_fallow()
        if not result: draw += 1
        elif result == 1: m1_win += 1
        else: m2_win += 1
    print(f"draw : {draw}")
    print(f"m1 : {m1_win}")
    print(f"m2 : {m2_win}")
