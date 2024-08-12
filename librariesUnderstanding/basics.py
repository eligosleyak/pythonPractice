'''
Libraries/Packages
    -Collection of codes and resources that has alot of function and operations already written for us
    -Example of packages/libraries are TensorFlow, Pytorch, Keras, Pandas, sklearn etc.
    -Not all packages are directly installed with python
    -Those libraries which comes with python are called preinstalled libraries. Others are installed by us.
    -Installing packages:
        pip install package_name
'''
import pandas as pd
"""
Pandas Library:
    -Pandas is equivalent to SQL for python, SQL already exists for python but pandas is more suited for AI work
    -Work on table, read table, modify table, save table and everything related table.
"""

dicta = {
    'student': ['Ram', 'Shyam', 'Sita', 'Gita'],
    'marks': [10, 20, 30, 40],
}

#Pandas operation 1:
dataFrameVariable = pd.DataFrame(dicta)
# print(dataFrameVariable)

# #Adding new column
# dataFrameVariable['Social Skills'] = [10,20,30,40]
# print('--'*25)
# print(dataFrameVariable)

# #Removing column
# dataFrameVariable = dataFrameVariable.drop(columns = ('Social Skills'))
# print('--'*25)
# print(dataFrameVariable)

'''
Task 1:
    Take n from user (N = number of questions)
    get n number of questions and N number of answers for quiz
    collect all questions in qtn list and asn in ans list
    convert to dictionary
    convet to dataframe
    display the final table
'''

# n = int(input('Enter number of questions: '))
# qtn = []
# ans = []
# for i in range(0, n):
#     qtn.append(input('Enter a question: '))
#     ans.append(input('Enter the answer: '))

# # Create a DataFrame with questions and answers as columns
# dic = {'Question': qtn, 'Answer': ans}
# dataFrame = pd.DataFrame(dic)
# print(dataFrame)

#Look up certain row loc, iloc
# print(dataFrameVariable.loc[dataFrameVariable['marks']<=32])

"""
Task 2:
    In the previous table include this question compulsory:
        What is the capital city of Nepal: KTM
    Look up only the row with this question: 'What is the capital city of Nepal'
"""

# print(dataFrame.loc[dataFrame['Question'] == 'What is the capital city of Nepal'])

#SAving to CSV
dataFrameVariable.to_csv('data.csv', index=False)

#Loading from CSV
newDataFrame = pd.read_csv('data.csv')
print(newDataFrame)
print('--'*25)
print(newDataFrame.iloc[1])