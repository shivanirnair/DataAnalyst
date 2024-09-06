Below are the set of question  we will answer with the dashboard: 
1 - Indicate at least three key performance indicators. 
2-  What channel receives the most inquiries?
3-  Which state has the most records of inquiries?
4-  What particular month has the most number of records?
5-  What question does a customer typically want to be answered?
6-  Which service level of agreement has received the most inquiries?

Note: (SLA means Service Level Agreement, this is an agreement between a vendor and customer to deliver a certain level of service to that customer)

Data cleaning:
Checked - No duplicates
Checked - No null values
Only the call_timestamp columns was text type so used Pandas to change it to date type.
Below is the code:
import pandas as pd;
df = pd.read_csv("D:\\Data Analyst\\DataSet\\OMNI channel Call Center.csv")
print(df.head())
df['call_timestamp'] = pd.to_datetime(df['call_timestamp'])

print(df.dtypes)
df.to_csv("D:\\Data Analyst\\DataSet\\OMNI channel Call Center.csv", index=False)
