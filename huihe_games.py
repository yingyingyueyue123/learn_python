def fight():
    my_hp = 1000
    my_power = 300
    enemy_power = 200
    enemy_hp = 1200
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp <= 0:
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break


if __name__ == '__main__':
    fight()
