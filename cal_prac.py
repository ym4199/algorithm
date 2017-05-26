class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def aplus(self):
        return self.a+self.b

    def amin(self):
        return self.a-self.b

class calss(cal):

    def amulti(self):
        return self.a * self.b

    def adiv(self):
        return self.a / self.b

cals=cal(3,4)
cals1=calss(3,4)

print(cals.aplus())
print(cals.amin())
print(cals1.amulti())
print(int(cals1.adiv()))

a = int(input('put your number :'))
b = int(input('put your number :'))

p=cal(a,b)
pp=calss(a,b)


input_num_op = input('choice option \n 1. add\n 2. min\n 3. mul\n 4. div\n :')


if input_num_op == '1':
    print(p.aplus())
elif input_num_op == '2':
    print(p.amin())
elif input_num_op == '3':
    print(pp.amulti())
elif input_num_op == '4':
    print(pp.adiv())
else:
    print('plea again')

