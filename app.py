import streamlit as st
import pandas as pd

# Initialize an empty DataFrame to store expenses
expenses = pd.DataFrame(columns=["Description", "Amount", "Category"])

# Function to add an expense entry
def add_expense(description, amount, category):
    global expenses
    new_expense = pd.DataFrame([[description, amount, category]], columns=["Description", "Amount", "Category"])
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

# Function to get total expenses and summary by category
def get_summary():
    if expenses.empty:
        st.write("No expenses logged yet.")
        return

    st.subheader("Expense Summary")
    total_expense = expenses["Amount"].sum()
    st.write(f"**Total Expense: ${total_expense:.2f}**")
    
    # Show summary by category
    category_summary = expenses.groupby("Category")["Amount"].sum().reset_index()
    st.write("**Expenses by Category:**")
    st.dataframe(category_summary)

# Streamlit UI

st.title("Expense Tracker")

# Expense form
st.subheader("Add New Expense")
with st.form(key='expense_form'):
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
    submit_button = st.form_submit_button(label="Add Expense")

    if submit_button:
        add_expense(description, amount, category)
        st.success("Expense added successfully!")

# Display expenses
st.subheader("All Expenses")
if not expenses.empty:
    st.dataframe(expenses)
else:
    st.write("No expenses to show yet.")

# Show the summary
get_summary()
