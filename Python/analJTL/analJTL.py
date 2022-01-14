from contextlib import suppress
from numpy import True_
import pandas as pd
from datetime import datetime
import time 


# 반복 주기 (초)
retryX = 10
# 최근 건수
tailX = 50

# Lable 그룹핑 된 통계 정보 출력
def showLabelElapsedStatics(df_):    
    data_g = df_.groupby('label')
    #print(data_g.head())
    
    
    #print(data_g['elapsed'].describe())        #Percentiles 기본 
    print(data_g['elapsed'].describe(percentiles=[.50,.75,.90,.99])) 
    
    
# 초당 처리건수 통계 출력
def showThroughput(df__):
   
    
    print(' ')
        
    #print(data_tg.describe())


def divmodTimeStamp(ts_):
    # 13자리,   10자리는 Unix Time, 3자리는 ms
    ts = divmod(ts_,1000)

    return ts    
    

def loadData(fname):
    # 1. 지정된 CSV 형식의 파일을 Load   
    data = pd.read_csv(fname)    
    return data

# DafaFrame 데이터 정제
def refineDF(df__,ynTR,ynUT):
    # 1. NaN 제거
    # Nan 은 공백으로 치환
    df__ = df__.fillna('')    
    
    # 2. Transaction Controller 처리
    # Transaction Controller 사용한 경우 Transaction Controller만 Filter
    # 'Response message' 에 "Number of samples in transaction" 가 포함된 경우는 Transaction Controller 임    
    if ynTR == "Y":   
        df__ = df__[df__['responseMessage'].str.contains('Number of samples in transaction')] 
    
    # 3. timeStamp 가 UnixTime 이면 DateTime Fotmat 형식으로 변환
    df__['TStamp'] = df__['timeStamp']
    
    if ynUT == 'Y' :                
        #print(df__)
        for a in range(df__['TStamp'].count()) :            
            ct = divmodTimeStamp(df__['timeStamp'].iloc[a])[0]
            dt = datetime.fromtimestamp(ct)
            df__['TStamp'].iloc[a] = dt
            #print (a,df__['TStamp'].iloc[a])           
        
    return df__


def analysisJmeter(df__,cnt):
    # DataFrame 정보 출력
    #print(data.info())
    #print(data['elapsed'].describe())    

    t_cnt = len(df__.index)
    a_idx = t_cnt-cnt
    #print(t_cnt , a_idx)
   
    df_ = df__.iloc[a_idx:,:]
    #print(df_)
    rows_cnt = len(df_.index)
    #print(rows_cnt)
    
    start_ts = df_['TStamp'].min()
    end_ts = df_['TStamp'].max()
          
    print ('최근 ', cnt, '개,  테스트 시간 :', start_ts,'~', end_ts)
    # Label 별 응답시간 통계
    showLabelElapsedStatics (df_)

    # 처리량 통계
    showThroughput(df_)
    
    
# 데이터 값 실수. 소수점 두째자리까지 표시
pd.options.display.float_format = '{:.2f}'.format

print ('------------------ Jmeter Statistics ------------------')
# 주기별로 재처리
 #test2.jtl   UnixTime         #test3.jtl DateFormat
while True:
    data = loadData('C:\\MyProject\\Code\\Python\\analJTL\\test2.jtl')        
    data = refineDF(data,'Y','Y')   
    analysisJmeter(data,300)
    time.sleep(retryX) 


''' 
# Jmeter 결과 저장 형식은 아래의 형식으로 저장됨
timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect
1641362300849,270,Home Page,200,,Scenario 1 1-1,text,true,,345,314,1,1,https://49.247.147.78:8783/,270,0,239 
    
'''