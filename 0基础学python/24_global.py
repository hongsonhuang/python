_a = 1
_b = 2
def add():
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    _b = 4
    return "_a - _b =", _a - _b
print (add())
print (sub())
print("添加global全局变量结果不一样")
def add():
    global _a
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    global _b
    _b = 4
    return "_a - _b =", _a - _b
print (add())
print (sub())