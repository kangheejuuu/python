##변수 선언##
inStr,outStr="",""  #inStr: 입력받을 문자열 저장, outStr: 대/소문자 변환
ch=""               #문자열에서 한 글자씩 뽑아 잠시 저장
count,i=0,0


'''
2021041025
강희주
'''

##메인 코드##
if __name__=="__main__":
    inStr=input("문자열을 입력하세요 : ")
    count=len(inStr)

    for i in range(0,count):
        ch=inStr[i]
        if(ord(ch)>=ord("A") and ord(ch)<=ord("Z")):    #ord함수는 문자를 숫자로 변환
            newCh=ch.lower()

        elif(ord(ch)>=ord("a") and ord(ch)<=ord("z")):
            newCh=ch.upper()

        else:
            newCh=ch

        outStr+=newCh

    print("대소문자 변환 결과 --> %s" % outStr)
