#!/usr/bin/env python
# coding: utf-8

# In[2]:


mo_df = pd.read_csv("/Users/yeonsu/Desktop/패캠/프로젝트/데이터셋/유동인구.csv", encoding='euc-kr')


# In[4]:


mo_df.info()


# In[5]:


sales_df = pd.read_csv("/Users/yeonsu/Desktop/패캠/프로젝트/데이터셋/매출.csv", encoding='euc-kr')


# In[36]:


sales_df.info()


# In[19]:


sales_name = list(sales_df.columns)
sales_name_change1 = list(map(lambda x : x.replace(' "',""), sales_name))
sales_name_change2 = list(map(lambda x : x.replace('"',""), sales_name_change1))
sales_df.columns = sales_name_change2


# In[23]:


sales_df.to_csv("~/Desktop/매출.csv", encoding="euc-kr", index=False)


# In[47]:


area_code = list(sales_df["상권_코드"])


# In[48]:


area_list = []
def dist(data):
    for data in data:
        if data not in area_list:
            area_list.append(data)
    return area_list


# In[49]:


len(dist(area_code))  # 1491개의 상권 # 너무 많은디..


# In[54]:


list(sales_df["상권_코드_명"])[0:10]


# In[52]:


dist(area_name)[0:20]


# In[ ]:





# In[ ]:





# In[21]:


sales_df.info()


# In[33]:


mo_df_names = list(mo_df.columns)
mo_df_names_change1 = list(map(lambda x : x.replace(" ",""), mo_df_names))
mo_df.columns = mo_df_names_change1


# In[35]:


mo_df.columns


# In[ ]:




