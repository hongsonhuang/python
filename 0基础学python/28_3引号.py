#三引号制作doc文档
class Hello:
    '''hello class'''
    def printHello(self):
        '''print hello world'''
        print("hello world2222!")
print(Hello.__doc__)
print(Hello.printHello.__doc__)