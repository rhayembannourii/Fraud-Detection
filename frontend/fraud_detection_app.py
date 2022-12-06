import json
import requests
import streamlit as st
from pathlib import Path


# App title
st.title("Credit Card Transaction Fraud Detection App")
BASE_DIR = Path(__file__).resolve(strict=True).parent
# some image
st.image(f"{BASE_DIR}/img/credit_card_fraud.jpg")

# Description
st.write(
    """
    ## About
    
    With the growth of e-commerce websites, people and financial companies rely on online services
    to carry out their transactions that have led to an exponential increase in the credit card frauds.
    Fraudulent credit card transactions lead to a loss of huge amount of money. The design of an
    effective fraud detection system is necessary in order to reduce the losses incurred by the
    customers and financial companies. 

    **This Streamlit App  utilizes a Machine Learning model(XGBoost) API to detect potential fraud in credit card transactions.**

    The notebook, model, documentation(FastApi script, Streamlit script) are available on [Github](https://github.com/rhayembannourii/Fraud-Detection/blob/master/NoteBook/Fraud_detection.ipynb)

    **Made by Rhayem Bannouri**

    """
)

###################### Funtions to transform categorical variable #############################################
def type_transaction(content):
    if content == "PAYMENT":
        content = 0
    elif content == "TRANSFER":
        content = 1
    elif content == "CASH_OUT":
        content = 2
    elif content == "DEBIT":
        content = 3
    elif content == "CASH_IN":
        content = 4
    return content

######################################### Input elements #############################################################
st.sidebar.header("Input user and transaction information")

# User data
sender_name = st.sidebar.text_input(" Sender Name ID")
receiver_name = st.sidebar.text_input(" Receiver Name ID")

## Transaction information
type_lebels = ("PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN")
type = st.sidebar.selectbox(" Type of transaction", type_lebels)

step = st.sidebar.slider("Number of Hours it took the Transaction to complete:", min_value=0, max_value=744)

amount = st.sidebar.number_input("Amount in $", min_value=0, max_value=110000)
oldbalanceorg = st.sidebar.number_input("""Sender Balance Before Transaction was made""", min_value=0,
                                        max_value=110000)
newbalanceorg = st.sidebar.number_input("""Sender Balance After Transaction was made""", min_value=0,
                                        max_value=110000)
oldbalancedest = st.sidebar.number_input("""Recipient Balance Before Transaction was made""", min_value=0,
                                         max_value=110000)
newbalancedest = st.sidebar.number_input("""Recipient Balance After Transaction was made""", min_value=0,
                                         max_value=110000)
## flag
isflaggedfraud = "Non fraudulent"
if amount >= 200000:
    isflaggedfraud = "Fraudulent transaction"
else:
    isflaggedfraud = "Non fraudulent"

result_button = st.button("Detect Result")

if result_button:

    ## Features
    data = {
        "step": step,
        "type": type_transaction(type),
        "amount": amount,
        "oldbalanceOrg": oldbalanceorg,
        "newbalanceOrig": newbalanceorg,
        "oldbalanceDest": oldbalancedest,
        "newbalanceDest": newbalancedest
    }

    ## Transaction detail
    st.write(
        f""" 
        ## **Transaction Details**

        #### **User informantion**:

        Sender Name(ID): {sender_name}\n
        Receiver Name(ID): {receiver_name}

        #### **Transaction information**:

        Number of Hours it took to complete: {step}\n
        Type of Transaction: {type}\n
        Amount Sent: {amount}$\n
        Sender Balance Before Transaction: {oldbalanceorg}$\n
        Sender Balance After Transaction: {newbalanceorg}$\n
        Recepient Balance Before Transaction: {oldbalancedest}$\n
        Recepient Balance After Transaction: {newbalancedest}$\n
        System Flag Fraud Status(Transaction amount greater than $200000): {isflaggedfraud}

        """
    )

    st.write("""## **Prediction**""")

    # inference from ml api
    # res = requests.post("https://heroku-host.com/prediction", json= data) ## for heroku
    res = requests.post("http://0.0.0.0:8000/prediction", json=data)  ## local
    json_str = json.dumps(res.json())
    respon = json.loads(json_str)

    if sender_name == '' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        st.write(
            f"""### The **'{type}'** transaction that took place between {sender_name} and {receiver_name} {respon[0]}.""")


