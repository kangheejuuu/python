##변수 선언##
i,k,heartNum=0,0,0           #heartNum: 하트 개수 세기위한 변수
numStr,ch,heartStr="","",""  #numStr: 숫자 입력받음 , heartStr: 하트 저장

'''
2021041025
강희주
'''

##메인 코드##
if __name__=="__main__":
    numStr=input("숫자를 여러 개 입력하세요 : ") #숫자로 구성된 문자열 입력받음
    print("")
    i=0
    ch=numStr[i]
    while True:
        heartNum=int(ch)

        heartStr=""                         #하트 저장할 문자열 초기화 
        for k in range(0,heartNum):
            heartStr+="\u2665"
            k+=1

        print(heartStr)

        i+=1
        if(i>len(numStr)-1):
            break

        ch=numStr[i]
