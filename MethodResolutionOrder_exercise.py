class A:
    num = 10


class B(A):
    num = 2


class C(A):
    num = 1


class D(C, B):
    pass


print(D.num)


class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass


print(M.__mro__)
