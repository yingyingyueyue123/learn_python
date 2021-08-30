# 实现被装饰函数有参数的情况

import time


def time_1(time_2):
    def func1(aaaaa):
        def func2(m_time):
            print("开始的时间为", time.strftime("%S"))
            aaaaa(m_time)
            print("结束的时间为", time.strftime("%S"))

        return func2

    return func1


@time_1(time_2=True)
def be_decorate(m_time):
    time.sleep(m_time)
    print("被装饰器装饰的函数")


be_decorate(3)
