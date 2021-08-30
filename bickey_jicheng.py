class Bicycle:
    def run(self, km):
        print(f"我用脚骑行了{km}公里，累死了")


class EBicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.valume += vol
        print(f"充了{vol}度电，现在电量为{self.valume}")

    def run(self, km):
        print(f"这段路总共里程为{km}公里")
        power_km = self.valume * 10
        if power_km > km:
            print(f"我使用电瓶车骑行了{km}公里")
        else:
            print(f"我使用电瓶车骑行了{power_km}公里")
            # 非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承调用
            super().run(km - power_km)


ebike = EBicycle(10)
ebike.run(200)
