
import pandas as pd
import numpy as np

df = pd.read_excel('trainDATA.xlsx')
dfTEST = pd.read_excel('testDATA.xlsx')
df.head()

def calculate_entropy(df_label):
    classes,class_counts=np.unique(df_label,return_counts=True)
    entropy_value=np.sum([(-class_counts[i]/np.sum(class_counts))*np.log2(class_counts[i]/np.sum(class_counts))
                          for i in range(len(classes))])
    return entropy_value


def calculate_information_gain(dataset,feature,label):
    dataset_entropy=calculate_entropy(dataset[label])
    values,feat_counts=np.unique(dataset[feature],return_counts=True)

    weighted_feature_entropy=np.sum([(feat_counts[i]/np.sum(feat_counts))*calculate_entropy(dataset.where(dataset[feature]==values[i]).dropna()[label]) for i in range (len(values))])
    feature_info_gain=dataset_entropy - weighted_feature_entropy
    return feature_info_gain

def create_decision_tree(dataset,df,features,label,parent):
    datum=np.unique(df[label],return_counts=True)
    unique_data=np.unique(dataset[label])
    if len(unique_data)<=1:
        return unique_data[0]

    elif len(dataset)==0:
        return unique_data[np.argmax(datum[1])]

    elif len(features)==0:
        return parent

    else:
        parent=unique_data[np.argmax(datum[1])]

        item_values=[calculate_information_gain(dataset,feature,label) for feature in features]

        optimum_feature_index=np.argmax(item_values)
        
        optimum_feature=features[optimum_feature_index]
        decision_tree ={optimum_feature:{}}
        

        features = [i for i in features if i != optimum_feature]

        
        for value in np.unique(dataset[optimum_feature]):
            min_data=dataset.where(dataset[optimum_feature]==value).dropna()

            min_tree=create_decision_tree(min_data,df,features,label,parent)

            decision_tree[optimum_feature][value] = min_tree

        return(decision_tree)
def predict_Accessibility(testdata,tree):
    try:
        for nodes in tree.keys():
            value=testdata[nodes]
            tree=tree[nodes][value]
            prediction=0
        
            if type(tree) is dict:
                prediction=predict_Accessibility(testdata,tree)
            else:
                prediction=tree
                break
    except:
          print("An exception occurred")
    
    return prediction
        


trainedModule=create_decision_tree(df,df,df.columns[:-1],'Car Acceptibility',None)
sampledata={'Price':1,'MaintPrice':2,'NoofDoors':3,'Persons':4,'Lug_size':2,'Safety':2}
test_data=pd.Series(sampledata)
prediction=predict_Accessibility(test_data,trainedModule)




def testDicts(columns,df):
    sampleArray=[]          
    for j in df.values:
        counter=0
        sample={}
        for i in columns:
            xsample={i:j[counter]}
            sample.update(xsample)
            counter=counter+1
        sampleArray.append(sample)
    return sampleArray

def getAllPrediction(getDictArray,trainedModule):
    predictions=[]
    for i in getDictArray:
        test_data=pd.Series(i)
        prediction=predict_Accessibility(test_data,trainedModule)
        predictions.append(prediction) 
        
    return predictions
    

samplesArray=testDicts(dfTEST.columns,dfTEST)
dfTEST['Car Acceptibility']=getAllPrediction(samplesArray,trainedModule)

dfTEST.to_excel('Tested.xlsx')












