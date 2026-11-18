import pandas as pd
data=pd.read_csv("C:\ML\DataSet\students.csv")
print(data)
'''to count null values in each column'''
print(data.head())
print(data.isnull().sum())

'''for insert values to na values'''
data=data.dropna(subset=["result"])
numerical_columns=["study_hours","attendance","previous_marks"]
for column in numerical_columns:
    data[column]=data[column].fillna(data[column].median())
print(data)
print(data.isnull().sum())

'''to check for dupicate values'''
print(data.duplicated().sum())
'''to remove dupicate values'''
data=data.drop_duplicates()
'''save the cleaned data to a new CSV file'''
data.to_csv("C:\ML\DataSet\students_cleaned.csv", index=False)
print("data saved ")

'''to convert result values to binary values'''
data["result"]=data["result"].map({"Pass":1,"Fail":0})
print(data)

'''as x and y values'''
x=data[['study_hours','attendance','previous_marks']]
y=data['result']

print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, stratify=y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(x_train, y_train)

print("Model trained")
#predict results
y_pred = model.predict(x_test)
print(y_test.values)
print(y_pred)

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

accuracy = accuracy_score(y_test, y_pred)

print(accuracy*100,"%")
print(classification_report(y_test, y_pred,zero_division=0))

#saving trained mode1

import joblib
joblib.dump(model,r"C:\\ML\\Models\\student_model_2.pkl")
            
print("success")

#to predict

import joblib
import pandas as pd
model=joblib.load(r"C:\\ML\\Models\\student_model_2.pkl")
new_student=pd.DataFrame({"study_hours":[7],"attendance":[85],"previous_marks":[70]})
prediction=model.predict(new_student)
if prediction[0]==1:
    print("student result: Pass")
else:
    print("student result: Fail")