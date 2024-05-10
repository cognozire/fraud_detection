import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
st.title("Financial Fraud Detection App")
model = load_model("fraud.h5")
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
arr1 = []
type_of_payment = st.selectbox("Type of Payment", ['CASH_OUT', 'PAYMENT', 'CASH_IN', 'TRANSFER', 'DEBIT'])
if type_of_payment=="CASH_IN":
    type_of_payment=0
elif type_of_payment=="CASH_OUT":
    type_of_payment=1
elif type_of_payment=="DEBIT":
    type_of_payment=2
elif type_of_payment=="PAYMENT":
    type_of_payment=3
elif type_of_payment=="TRANSFER":
    type_of_payment=4
arr1.append(type_of_payment)
transaction_amount = st.number_input("Transaction Amount", min_value=0)
arr1.append(transaction_amount)
sender_old_balance = st.number_input("Sender Old Account Balance", min_value=0)
arr1.append(sender_old_balance)
sender_new_balance = st.number_input("Sender New Account Balance", min_value=0)
arr1.append(sender_new_balance)
receiver_old_balance = st.number_input("Receiver Old Account Balance", min_value=0)
arr1.append(receiver_old_balance)
receiver_new_balance = st.number_input("Receiver New Account Balance", min_value=0)
arr1.append(receiver_new_balance)
suspicious = st.radio("Is the transaction suspicious?", ('Yes', 'No'))
if suspicious=="Yes":
    suspicious = 1
else:
    suspicious =0
arr1.append(suspicious)
# if type_of_payment and transaction_amount and sender_new_balance and sender_old_balance and receiver_old_balance and receiver_new_balance:
#         if st.button("Predict"):
#             y = np.array([arr1])
#             pred = model.predict(y)
#             results = pred[0]
#             if results[0]>results[1]:
#                 st.write(f"This transaction seems to be fair with a probability of {results[0]}")
#             elif results[1]>results[0]:
#                 st.write(f"This transaction seems to be fraud with a probability of {results[1]}")

# else:
#     pass

if st.button("Predict"):
    if str(type_of_payment) != '' and str(transaction_amount) != '' and str(sender_old_balance) != '' and str(sender_new_balance) != '' and str(receiver_old_balance) != '' and str(receiver_new_balance) != '' and str(suspicious) != '':
        y = scaler.transform([arr1])
        pred = model.predict(y)
        results = pred[0]
        if results[0]>results[1]:
            st.write(f"This transaction seems to be fair with a probability of {results[0]}")
        elif results[1]>results[0]:
            st.write(f"This transaction seems to be fraud with a probability of {results[1]}")
    else:
        st.warning('Kindly enter all values.')
            
            

        
   
