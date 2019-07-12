#!/usr/bin/env python
# coding: utf-8

# In[1]:


def data_type(df):
    sol1=df.dtypes
    return sol1


def data_info_shape(df):
    sol2=df.info()
    sol3=df.shape
    return sol2, sol3


def null_values(df):
    null1 = df.isna().sum()
    return null1


def data_desc(df):
    sol3=df.describe(include='all')
    return sol3


def data_rename(df):
    sol4=df.rename(columns = {"COMPNOS" : "ReportNumber", "INCIDENT_TYPE_DESCRIPTION" : "IncidentClassification", "MAIN_CRIMECODE" : "CrimeCode", "REPORTINGAREA" : "AreaCode", "FROMDATE" : "Date", "DAY_WEEK" : "Day"}, inplace=True)
    return sol4


def incidentclass_lowercase(df):
    sol5=df["IncidentClassification"] = df.IncidentClassification.str.lower()
    return sol5





