class Game():
    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.my_power = 300
        self.enemy_power = 200
        self.enemy_hp = enemy_hp

    def fight(self):

        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(f"我的血量为{self.my_hp}")
            print(f"敌人的血量为{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


class HouYi(Game):
    """
    如果子类与父类重名，会覆盖掉父类的属性
    """

    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        # 继承父类的构造方法,如果父类的构造方法有形参，需要传递参数
        super().__init__(my_hp, enemy_hp)

        # def fight(self):
        #
        #     while True:
        #         self.my_hp = self.my_hp + self.defense - self.enemy_power
        #         self.enemy_hp = self.enemy_hp - self.my_power
        #         print(f"我的血量为{self.my_hp}")
        #         if self.my_hp <= 0:
        #             print("我输了")
        #             break
        #         elif self.enemy_hp <= 0:
        #             print("我赢了")
        #             break


houyi_game = HouYi(1000, 1200)
houyi_game.fight()
