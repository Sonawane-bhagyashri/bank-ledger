import streamlit as st
import datetime

# --- CORE DATA STRUCTURES LAYER ---
class TransactionNode:
    def __init__(self, tx_id: int, tx_type: str, amount: float):
        self.tx_id = tx_id
        self.tx_type = tx_type.upper()  # "DEPOSIT" or "WITHDRAW"
        self.amount = amount
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None
        self.prev = None

class AccountLedger:
    def __init__(self):
        self.head = None
        self.tail = None
        self.balance = 0.0
        self.tx_counter = 100

    def add_transaction(self, tx_type: str, amount: float):
        if amount <= 0:
            return False, "Amount must be greater than zero."
            
        if tx_type.upper() == "WITHDRAW" and self.balance - amount < 0:
            return False, f"Insufficient balance. Current balance is ₹{self.balance:,.2f}."

        self.tx_counter += 1
        new_node = TransactionNode(self.tx_counter, tx_type, amount)

        if tx_type.upper() == "DEPOSIT":
            self.balance += amount
        elif tx_type.upper() == "WITHDRAW":
            self.balance -= amount

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        return True, f"Logged {tx_type.upper()} of ₹{amount:,.2f} (Tx ID: {self.tx_counter})."

    def undo_last_transaction(self):
        """Removes the latest node (tail) and reverses its balance impact. Complexity: O(1)"""
        if not self.tail:
            return False, "No transactions available to undo."

        target_node = self.tail
        
        if target_node.tx_type == "DEPOSIT":
            self.balance -= target_node.amount
        elif target_node.tx_type == "WITHDRAW":
            self.balance += target_node.amount

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = target_node.prev
            self.tail.next = None  

        return True, f"Successfully undone Transaction ID: {target_node.tx_id}."

    def get_history(self):
        transactions = []
        current = self.tail  # Latest first
        while current:
            transactions.append({
                "Timestamp": current.timestamp,
                "Tx ID": current.tx_id,
                "Type": current.tx_type,
                "Amount": f"₹{current.amount:,.2f}"
            })
            current = current.prev
        return transactions

# --- STREAMLIT WEB UI LAYER ---
st.set_page_config(page_title="FinTech Ledger Engine", page_icon="💰", layout="centered")

st.title("💰 Enterprise Banking Ledger Dashboard")
st.markdown("A real-time financial auditing engine powered by a custom **Doubly Linked List** architecture.")
st.write("---")

# Maintain state across updates
if 'ledger' not in st.session_state:
    st.session_state.ledger = AccountLedger()

ledger = st.session_state.ledger

# Key Metrics Display Panel
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Account Balance", value=f"₹{ledger.balance:,.2f}")
with col2:
    total_txs = len(ledger.get_history())
    st.metric(label="Total Audited Transactions", value=total_txs)

# Control Action Row
c1, c2 = st.columns([2, 1])
with c1:
    st.write("### 🔄 Process New Transaction")
with c2:
    st.write("### ")
    if st.button("↩️ Undo Last", use_container_width=True):
        success, msg = ledger.undo_last_transaction()
        if success:
            st.success(msg)
            st.rerun()
        else:
            st.warning(msg)

# Input Form
with st.form(key="transaction_form", clear_on_submit=True):
    tx_type = st.selectbox("Transaction Type", ["DEPOSIT", "WITHDRAW"])
    amount = st.number_input("Amount (₹)", min_value=0.0, step=500.0, format="%.2f")
    submit_button = st.form_submit_button(label="Execute Transaction")

    if submit_button:
        success, message = ledger.add_transaction(tx_type, amount)
        if success:
            st.success(message)
            st.rerun()
        else:
            st.error(message)

# Audit Trail Section
st.write("### 📜 Real-Time Audit Trail (Latest First)")
history_data = ledger.get_history()

if history_data:
    st.table(history_data)
else:
    st.info("No transaction records found in the current memory lifecycle.")
