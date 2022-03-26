import operator

##변수 선언##
trainTupleList=[('토마스',5),('헨리',8),('에드워드',9),('에밀리',5),  #기차와 수송량이 기록된 튜플의 리스트 준비
                ('토마스',4),('헨리',7),('토마스',3),('에밀리',8),
                ('퍼시',5),('고든',13)]

trainDic,trainList={},[]  #trainDic: 수송량의 합계를 기록할 딕셔너리, trainList: 딕셔너리를 다시 정렬할 튜플 리스트
tmpTup=None
totalRank,currentRank=1,1 #totalRank: 전체 순위 매기기, currentRank: 현재 동일한 순위 매기기

'''
2021041025
강희주
'''

##메인 코드 ##
if __name__=="__main__":
    for tmpTup in trainTupleList:
        tName=tmpTup[0]
        tWeight=tmpTup[1]
        if tName in trainDic:        #딕셔너리에 해당 기차 있으면 
            trainDic[tName]+=tWeight #값을 누적
        else:                        
            trainDic[tName]=tWeight  #없으면 새로운 값을 등록


    print("기차 수송량 목록 ==>",trainTupleList)
    print("--------------------")
    trainList=sorted(trainDic.items(),key=operator.itemgetter(1),reverse=True)

    print("기차\t총 수송량\t순위")
    print("--------------------")
    print(trainList[0][0],"\t",trainList[0][1],"\t",currentRank)
    for i in range(1,len(trainList)):
        totalRank+=1
        if trainList[i][1]==trainList[i-1][1]:  #앞 기차와 수송량이 같다면 41행으로 건너뛰기 
            pass
        else:                      
            currentRank=totalRank   #그렇지 않으면 현재 등수를 전체 등수로 변경
        print(trainList[i][0],"\t",trainList[i][1],"\t",currentRank) #앞 기차와 동일한 등수 출력
        
