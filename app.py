import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(filepath_or_buffer="./tips.csv")
st.title("Hello Streamlit :D")
st.dataframe(data=df)
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
st.pyplot(fig=fig)
a = st.sidebar.number_input(label="a")
b = st.sidebar.number_input(label="b")
if (a==0 and b==0):
    string = "Infinitely many solutions!"
elif (a==0 and b!=0):
    string = "No solution!"
else:
    x = - b/a
    string = f"The solution to ax+b=0 is x={x}"
st.write(string)