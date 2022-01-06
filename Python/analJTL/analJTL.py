from contextlib import suppress
import pandas as pd
import datetime 
import time 


# Lable 그룹핑 된 통계 정보 출력
def showLabelElapsedStatics(df_):
    
    data_g = df_.groupby('label')
    print(data_g['elapsed'].describe()) 

# 1. 지정된 CSV 형식의 파일을 Load
fname = 'C:\\MyProject\\Code\\Python\\analJTL\\test1.jtl'
data = pd.read_csv(fname)

# Jmeter 결과 저장 형식은 아래의 형식으로 저장됨
''' 
timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect
1641362300849,270,Home Page,200,,Scenario 1 1-1,text,true,,345,314,1,1,https://49.247.147.78:8783/,270,0,239 
'''
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

# 전체 기간에 대한 Label 별 Elapsed 통계
print('----------- 전체 기간 Label,Elapsed 통계 ---------')
showLabelElapsedStatics(data)

print('----------- 최근 X건 Label,Elapsed 통계 ---------')
data1 = data.tail(5)
showLabelElapsedStatics(data1)