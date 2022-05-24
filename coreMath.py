import pandas as pd
import numpy as np
id=[]
a=202001
while a<202011:
    id.append(a)
    a+=1

Chinese=[98,67,84,88,78,90,93,75,82,87]
Math=[92,80,73,76,88,78,90,82,77,69]
English=[88,79,90,73,79,83,81,91,71,78]
StudentScore1={"id":id,"Chinese":Chinese,"Math":Math,"English":English}
# df = pd.DataFrame(data)
# print(df)
SumScore=[]
MeanScore=[]
MaxScore=[]
MinScore=[]
PtpScore=[]
VarScore=[]
for i in range(10):
    sum=Chinese[i]+English[i]+Math[i]
    SumScore.append(sum)
    MeanScore.append(int(sum/3))
     # 最大值
    MAXS=np.max([Chinese[i], English[i], Math[i]])
    MINS=np.min([Chinese[i], English[i], Math[i]])
    # 极差
    PtpScore.append(np.ptp([MAXS,MINS]))

    MaxScore.append(MAXS)
    MinScore.append(MINS)
    VarScore.append(int(np.var([Chinese[i], English[i], Math[i]])))

# print(SumScore)
# print(MeanScore)
# print(MaxScore)
# print(VarScore)
data1={"SumScore":SumScore,'MeanScore':MeanScore,"MaxScore":MaxScore,"MinScore":MinScore
       ,"PtpScore":PtpScore,"VarScore":VarScore}
StudentScore1.update(data1)
# print(StudentScore)
StudentScore=pd.DataFrame(StudentScore1)
data = pd.concat([StudentScore.iloc[:,0],StudentScore.iloc[:,1],StudentScore.iloc[:,2],StudentScore.iloc[:,3],StudentScore.iloc[:,4],StudentScore.iloc[:,5],StudentScore.iloc[:,6],StudentScore.iloc[:,7],StudentScore.iloc[:,8],StudentScore.iloc[:,9]])
df = pd.DataFrame(data, columns=['answer'])
df['id'] = range(len(df))
df.to_csv('answer_1.csv', index=False, encoding='utf-8-sig')
# print(df)
