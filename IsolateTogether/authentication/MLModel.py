import pandas as pd
pd.set_option('display.max_colwidth',500)
import numpy as np
import _pickle as pickle
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler
import os
import random


def addProfile(interest,a):
    print("Inside MLModel")
    #print(i)
    print(a)
    print(type(a))
    ls = list(interest.items())
    fs = []
    topic_name = []
    #print(ls)
    for ki in ls:
        #print(ki)
        for ki_val in ki[1].items():
            fs.append(ki_val[1])
            topic_name.append(ki_val[0])
        topic_name.pop()
        topic_name.append(ki[0])
        
    print("-------------")
    #print(fs)
    #print(topic_name)
    #print(len(topic_name))

    modulePath = os.path.dirname(__file__)  # get current directory
    filePath_clus = os.path.join(modulePath, 'profiles_clustered.pkl')

    with open(filePath_clus,'rb') as fp:
        df = pickle.load(fp)

    filePath_map = os.path.join(modulePath, "profilesMapIndex.pkl")
    with open(filePath_map,'rb') as fp:
        profileMap = pickle.load(fp)

    df = df.drop('Cluster #', axis=1)
    new_profile = pd.DataFrame(columns=df.columns)

    data_to_append = {}
    
    for i in range(len(new_profile.columns)):
        data_to_append[new_profile.columns[i]] = fs[i]
    
    new_profile = new_profile.append(data_to_append, ignore_index = True)
    new_profile.index = [df.index[-1] + 1]

    df=df.append(new_profile)

    new_profile_map = pd.DataFrame(columns=profileMap.columns)
    new_profile_map['uid'] = [a]
    new_profile_map.index=new_profile.index
    profileMap = profileMap.append(new_profile_map)
    
    scaler = MinMaxScaler()
    df = pd.DataFrame(scaler.fit_transform(df),columns=df.columns[0:],index=df.index)

    cluster_cnt = [i for i in range(2, 3, 1)]


    s_scores = []

    db_scores = []

    print(df)
    for i in cluster_cnt:
        
        hac = AgglomerativeClustering(n_clusters=i)
        
        hac.fit(df)
        
        cluster_assignments = hac.labels_
        
        s_scores.append(silhouette_score(df, cluster_assignments))
        
        db_scores.append(davies_bouldin_score(df, cluster_assignments))

    def cluster_eval(y, x, z):
        df = pd.DataFrame(columns=['Cluster Score'], index=[i for i in range(2, len(y)+2)])
        df['Cluster Score'] = y
        
        #print('Max Value:\nCluster #', df[df['Cluster Score']==df['Cluster Score'].max()])
        #print('\nMin Value:\nCluster #', df[df['Cluster Score']==df['Cluster Score'].min()])
        
        if z==1:
            return df[df['Cluster Score']==df['Cluster Score'].max()]
        else:
            return df[df['Cluster Score']==df['Cluster Score'].min()]
        
            
    effi_cluster = (int)((cluster_eval(s_scores, cluster_cnt,1).index[0] + cluster_eval(db_scores, cluster_cnt,2).index[0])/2)

    hac = AgglomerativeClustering(n_clusters=effi_cluster)
    hac.fit(df)
    cluster_assignments = hac.labels_
    df = (pd.DataFrame(scaler.inverse_transform(df), columns=df.columns[0:], index=df.index))
    df['Cluster #'] = cluster_assignments

    with open(filePath_clus,"wb") as fp:
        pickle.dump(df,fp)
    
    with open(filePath_map,"wb") as fp:
        pickle.dump(profileMap,fp)

    seeData()

    print("Leaving MLModel")


def seeData():
    
    print("----------------Inside seeData-------------------")
    modulePath = os.path.dirname(__file__)  # get current directory
    filePath_clus = os.path.join(modulePath, 'profiles_clustered.pkl')

    with open(filePath_clus,'rb') as fp:
        df = pickle.load(fp)

    filePath_map = os.path.join(modulePath, "profilesMapIndex.pkl")
    with open(filePath_map,'rb') as fp:
        profileMap = pickle.load(fp)
    

    print(df)
    print(profileMap)

    

def findSimilarProfile(a):
    seeData()
    modulePath = os.path.dirname(__file__)  # get current directory
    filePath = os.path.join(modulePath, 'profiles_clustered.pkl')

    with open(filePath,'rb') as fp:
        df = pickle.load(fp)

    filePath = os.path.join(modulePath, "profilesMapIndex.pkl")
    with open(filePath,'rb') as fp:
        profileMap = pickle.load(fp)

    random_user = profileMap[profileMap['uid'] == a].index[0]

    group = df[df['Cluster #']==df['Cluster #'][random_user]].drop('Cluster #', axis=1)
    corr_group = group.T.corr()

    print("Top 10 most similar users to User #", random_user, '\n')
    top_10_sim = corr_group[[random_user]].sort_values(by=[random_user],axis=0, ascending=False)[1:11]
    print(top_10_sim)
    print("\nThe most similar user to User #", random_user, "is User #", top_10_sim.index[0])

    ar = []
    for i in top_10_sim.index:
        #print(profileMap[profileMap.index==profileMap.index[i]])
        #print("-----")
        ar.append(profileMap['uid'][i])
        #print("------------------------------")

    print(ar)
    return ar


seeData()