x = 10
class Looker:
    x = 15
    print(x)
    def func_1(self):
        x=20
        print(x)
        def func_2():
            x=30
            print(x)
        func_2()

some_object = Looker()
some_object.func_1()

