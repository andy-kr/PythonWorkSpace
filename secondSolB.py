data =[]
def inputData():
    while True:
        name = input('이름:')
        kor = int( input('국어:') )
        eng = int( input('영어:') )
        math = int( input('수학:') )
        data.append( (name, kor, eng,math) )
        yn= input('계속 입력하시겠습니까(y/n)?')
        if yn=='n':
            break
# print(data)
def outputData():
    print("="*30)
    print('이름','국어','영어','수학',sep='\t')
    print("="*30)
    for n,k,e,m in data:
        print(  n,k,e,m,sep='\t\t' )

inputData()
outputData()

