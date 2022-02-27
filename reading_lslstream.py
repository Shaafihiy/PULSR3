 #"""Example program to show how to read a multi-channel time series from LSL."""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import model_selection 
from pylsl import StreamInlet, resolve_stream
import sklearn.metrics as metrics
from ggplot import *


# first resolve an EEG stream on the lab network
print("looking for an EEG stream and Marker stream...")
streams = resolve_stream('name', 'probStream')
streams_marker = resolve_stream('name', 'probStream-markers')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
inlet_marker = StreamInlet(streams_marker[0])
global sample_marker
sample_marker=list(['start'])
classificationResult=np.array([['rest','active-movement','sound','eye-blink','label']])
while sample_marker[0]!='calib-end':
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    
    sample, timestamp = inlet.pull_sample()
    sample_marker, timestamp = inlet_marker.pull_sample()
    print(sample,sample_marker)
    classificationResult=np.vstack((classificationResult,np.array([[float(sample[0]),float(sample[1]),float(sample[2]),float(sample[3]),sample_marker[0]]])))
    # print(classificationResult)
   # array = np.concatenate((list(sample), np.concatenate(list(sample_marker))[:,None]),axis=1)
    #print(array)
df=pd.DataFrame(classificationResult[1:,:],columns=classificationResult[0,:])
print(df)
predict=list()
for i in range(0,len(df)):
    val=np.array([df.iloc[i][0:4]], dtype=float)
    if np.argmax(val[0])==0:
        predict.append('rest')
    elif np.argmax(val[0])==1:
        predict.append('active-movement')
    elif np.argmax(val[0])==2:
        predict.append('sound')
    elif np.argmax(val[0])==3:
        predict.append('eye-blink')
    # print(index_max)
    # print(val,max(val[0]))
# df['Predict'] = max_val
df['predict']=predict
print(df)

con_matrix_table = pd.crosstab(df['predict'], df['label'])
print(con_matrix_table) 

#plt.clf()
#ax = fig.add_subplot(111)
#ax.set_aspect(1)

res = sns.heatmap(con_matrix_table.T, annot=True, fmt='.2f', cmap="YlGnBu", cbar=False)
#plt.savefig("crosstab_pandas.png", bbox_inches='tight', dpi=100)

plt.show()

# calculate the fpr and tpr for all thresholds of the classification
probs = model_selection.predict_proba(df['label'])
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(df['predict'], preds)
roc_auc = metrics.auc(fpr, tpr)



df = pd.DataFrame(dict(fpr = fpr, tpr = tpr))
ggplot(df, aes(x = 'fpr', y = 'tpr')) + geom_line() + geom_abline(linetype = 'dashed')