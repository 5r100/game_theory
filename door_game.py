import random

def game(first_choice):
        door = random.choice([1,2,3])
        all_doors = [1,2,3]

        choice_set = [1,2,3]
        choice_set.remove(door)

        choice = random.choice(choice_set)
        if choice == first_choice:
            choice_set.remove(choice)
            choice = choice_set[0]
        
        all_doors.remove(choice)
        all_doors.remove(first_choice)
        second_choice = all_doors[0]
        
        if door == second_choice: return 1
        return 0

if __name__ == "__main__":
    won = 0
    lose = 0
    for _ in range(0,10000000):
        if game(random.choice([1,2,3])): won += 1
        else: lose += 1
    print(f"won : {won}")
    print(f"lost : {lose}")
