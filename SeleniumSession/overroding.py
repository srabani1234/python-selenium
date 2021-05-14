class A:
    def property(self):
        print('cash')
    def marry(self):
        print('shu')
class C(A):
    def marry(self,a):
        super().property()
        print('kat',a)
c1 = C()
c1.marry(10)
A1 = A()
A1.marry()
