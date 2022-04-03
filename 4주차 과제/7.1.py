import random

##변수 선언##
data=[]      #16진수를 저장할 data 리스트
i,k=0,0      #for문에서 사용할 i,k

'''
2021041025
강희주
'''

##메인 코드##
if __name__=="__main__":
    for i in range(0,10):                   #임의의 16진수 10개 생성
        tmp=hex(random.randrange(0,100000)) #0~99999에서 추출
        data.append(tmp)

    print("정렬 전 데이터 :",end=" ")          #추출된 정렬 전 데이터 출력
    [print(num,end=" ") for num in data]

    #중첩 for문을 이용해 리스트를 선택 정렬로 내림차순 정렬
    for i in range(0,len(data)-1):          #0번째부터 마지막 값 바로 전까지
        for k in range(i+1,len(data)):      #비교하는 앞의 값 바로 다음부터 마지막 값까지 
            if int(data[i],16)> int(data[k],16):
                tmp=data[i]
                data[i]=data[k]
                data[k]=tmp

    print("\n정렬 후 데이터:",end=" ")         #정렬 후 데이터 출력
    [print(num,end=" ") for num in data]
