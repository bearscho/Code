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
    print(data_g.head())
    print(data_g['elapsed'].describe()) 
    
    
# 초당 처리건수 통계 출력
def showThroughput(df__):
    # divmod()  나누기  [0] 몫,  [1] 나머지
    df__['YMDHMS'] = df__['timeStamp']
    rowCnt = df__['timeStamp'].count()
    print (rowCnt)
    
    for a in range(rowCnt):        
        ct = divmod(df__['timeStamp'].iloc[a],1000)[0]        
        #print (datetime.fromtimestamp(ct))        
        df__['YMDHMS'].iloc[a] = datetime.fromtimestamp(ct)
    
    data_tg = df__.groupby('YMDHMS')
    #print(data_tg['YMDHMS'].describe())
    
    
    print(data_tg.describe())


def divmodTimeStamp(ts_):
    # 13자리,   10자리는 Unix Time, 3자리는 ms
    ts = divmod(ts_,1000)

    return ts    
    

def loadData(fname):
    # 1. 지정된 CSV 형식의 파일을 Load   
    data = pd.read_csv(fname)    
    return data



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
    
    start_ts = df_['timeStamp'].min()
    end_ts = df_['timeStamp'].max()
    
    start_dt = divmodTimeStamp(start_ts)
    end_dt = divmodTimeStamp(end_ts)
      
    print ('최근 ', cnt, '개,  테스트 시간 :', datetime.fromtimestamp(start_dt[0]),'~', datetime.fromtimestamp(end_dt[0]))
    
    # lable 기준 통계
    showLabelElapsedStatics(df_)
    


# ------------------
data = loadData('C:\\MyProject\\Code\\Python\\analJTL\\test1.jtl')

print ('------------------ Jmeter Statistics ------------------')
analysisJmeter(data,300)

# 주기별로 재처리
while True:
    print ('------------------ Jmeter Statistics ------------------')
    analysisJmeter(data,300)
    time.sleep(retryX) 


''' 
    # DataFrame 정보 출력
    # print(data.info())

    # Jmeter 결과 저장 형식은 아래의 형식으로 저장됨
    
    timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect
    1641362300849,270,Home Page,200,,Scenario 1 1-1,text,true,,345,314,1,1,https://49.247.147.78:8783/,270,0,239 
    
    # DataFrame 정보 출력
    # print(data.info())

    # print('elapsed Max:',data['elapsed'].max())
    # print('elapsed Min:',data['elapsed'].min())
    # print('elapsed Mean:',data['elapsed'].mean())

    # 2. 응답시간 (elapsed) 의 정보 출력 
    #print('---- 전체 데이터 elapsed 의 describe() -------------------')
    # print('elapsed Describe:',data['elapsed'].describe())

    # 3. Label (Sampler or Transaction 이름) 으로 그룹핑
    # print('-------- label group ---------------------')
    # label_grp = data.groupby('label')

    # print(label_grp.size())      

    # print(label_grp['elapsed'].mean())
    # print(label_grp['elapsed'].max())
    # print('############')
    # print(label_grp['elapsed'].describe())


    """ 
    print('----------- 시간 ---------')
    current_time = datetime.datetime.now()
    print(current_time)

    unixtime = time.time()
    print(unixtime) 
    """
    
    current_time = datetime.now()
    print(current_time)

    # 전체 기간에 대한 Label 별 Elapsed 통계
    print('----------- 전체 기간 Label,Elapsed 통계 ---------')
    #showLabelElapsedStatics(data)

    print('----------- 최근 X건 Label,Elapsed 통계 ---------')
    data1 = data.tail(tailX)
    #showLabelElapsedStatics(data1)
    
    showThroughput(data)
    
    
   '''