import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
st.title("Financial Fraud Detection App")
model = load_model("fraud.h5")
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
# arr1.append(type_of_payment)
transaction_amount = st.number_input("Transaction Amount", min_value=0)
# arr1.append(transaction_amount)
sender_old_balance = st.number_input("Sender Old Account Balance", min_value=0)
# arr1.append(sender_old_balance)
sender_new_balance = st.number_input("Sender New Account Balance", min_value=0)
# arr1.append(sender_new_balance)
receiver_old_balance = st.number_input("Receiver Old Account Balance", min_value=0)
# arr1.append(receiver_old_balance)
receiver_new_balance = st.number_input("Receiver New Account Balance", min_value=0)
# arr1.append(receiver_new_balance)
suspicious = st.radio("Is the transaction suspicious?", ('Yes', 'No'))
if suspicious=="Yes":
    suspicious = 1
else:
    suspicious =0
    arr1 = []
# arr1.append(suspicious)
if st.button("Predict"):
    arr1[0] = type_of_payment
    arr1[1] = transaction_amount
    arr1[2] = sender_old_balance
    arr[3] = sender_new_balance
    arr1[4] = receiver_old_balance
    arr1[5] = receiver_new_balance
    arr1[6] = suspicious
    y = np.array([arr1])
    pred = model.predict(y)
    results = pred[0]
    if results[0]>results[1]:
        st.write(f"This transaction seems to be fair with a probability of {results[0]}")
    elif results[1]>results[0]:
        st.write(f"This transaction seems to be fraud with a probability of {results[1]}")
