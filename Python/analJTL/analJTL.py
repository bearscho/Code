import pandas as pd
import datetime 
import time 

fname = 'C:\\MyProject\\Code\\Python\\analJTL\\test1.jtl'
data = pd.read_csv(fname)


''' 
timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect
1641362300849,270,Home Page,200,,Scenario 1 1-1,text,true,,345,314,1,1,https://49.247.147.78:8783/,270,0,239 
'''
print(data.info())

print('elapsed Max:',data['elapsed'].max())
print('elapsed Min:',data['elapsed'].min())
print('elapsed Mean:',data['elapsed'].mean())

print('----------------------------------------')
print('elapsed Describe:',data['elapsed'].describe())

print('-------- label group ---------------------')
label_grp = data.groupby('label')

print(label_grp.size())      

print(label_grp['elapsed'].mean())
print(label_grp['elapsed'].max())


print('----------- 시간 ---------')
current_time = datetime.datetime.now()
print(current_time)


unixtime = time.time()
print(unixtime)


data1 = data[data['timeStamp']>unixtime]
print(data1)