'''
4. 종료
'''
from statistics import mean, median, stdev

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def show(self):
        print('%5s\t%4d\t%4d\t%4d'%(self.name, self.kor, self.eng, self.math))

############################################################################################################
def mainMenu():
    sel = int(input(
        '메인 메뉴)\n'
        '     1.입력\n'
        '     2.출력\n'
        '     3.검색\n'
        '     4.종료\n'
        '     번호를 입력하세요: '))
    return sel
############################################################################################################
def inputMenu(dt):
    name = input('1. 입력)\n이름: ')
    kor = int(input('국어: '))
    eng = int(input('영어: '))
    math = int(input('수학: '))

    dt.append(Student(name, kor, eng, math))

    inputAgain = input('계속 입력하시겠습니까(y/n)?')

    if(inputAgain == 'y' or inputAgain == 'Y'):
        inputMenu(dt)
############################################################################################################
def printMenu(dt):
    print('''
2.출력
-----------------------------------------------------------------
    이름\t국어\t영어\t수학\t총점\t평균
----------------------------------------------------------------''')
    listKor = []
    listEng = []
    listMath = []

    for std in dt:
        listKor.append(std.kor)
        listEng.append(std.eng)
        listMath.append(std.math)
        print('%5s\t%4d\t%4d\t%4d\t%4d\t%4.2f'%(std.name, std.kor, std.eng, std.math, sum([std.kor, std.eng, std.math]), mean([std.kor, std.eng, std.math])))
    print('''-----------------------------------------------------------------
총점: 국어 %d  영어 %d 수학 %d
평균: 국어 %d  영어 %d 수학 %d
최고점수: 국어 %d  영어 %d 수학 %d
    '''%(sum(listKor), sum(listEng), sum(listMath), mean(listKor), mean(listEng), mean(listMath), max(listKor), max(listEng), max(listMath)))


############################################################################################################
def searchMenu(dt):
    searchName = input('''
3.검색
검색할 이름을 입력하세요: ''')

    print('''----------------------------------------
    이름\t국어\t영어\t수학
----------------------------------------''')

    for i in dt:
        if(i.name == searchName):
            i.show()
            break

#filter use



############################################################################################################
data = []
data.append(Student('홍길동',20, 20, 20))
data.append(Student('이순신',30, 40, 50))
data.append(Student('abc',100, 100, 100))
fn = {1:inputMenu, 2:printMenu, 3:searchMenu, 4:exit}

while(True):
    sel = mainMenu()
    if(0 < sel < 5):
        fn[sel](data)


# data = []
# data.append( (name, kor, eng, math) )
