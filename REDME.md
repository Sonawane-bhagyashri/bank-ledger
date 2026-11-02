# 💰 Enterprise Banking Ledger Dashboard

[![Python Version](https://shields.io)](https://python.org)
[![Framework](https://shields.io)](https://streamlit.io)
[![Data Structure](https://shields.io)]()
[![License](https://shields.io)]()

An enterprise-ready banking ledger simulation and real-time transaction auditing engine. This project bypasses high-overhead external database frameworks to implement a high-performance **custom Doubly Linked List (DLL)** architecture directly in memory.

---

## 🚀 Key Features

* **Custom Memory Architecture:** Employs independent heap-allocated pointer chains (`TransactionNode`) ensuring appends scale efficiently.
* **Persistent Session State:** Binds data lifecycles securely inside a continuous Streamlit `session_state` runtime environment to prevent data loss across dynamic frontend UI reloads.
* **Instantaneous Reversals:** Features an algorithmic backtracking engine leveraging `.prev` pointer manipulation to safely drop nodes and restore previous account balance values.
* **Financial Risk Safeguards:** Proactively intercepts illegal amounts, zero-value configurations, and critical overdraft occurrences prior to historical record mutation.

---

## 📊 Algorithmic Complexity Profile

| Operation | Time Complexity | Space Complexity | Underlying Mechanism |
| :--- | :---: | :---: | :--- |
| **Deposit / Process Tx** | O(1) | O(1) | Direct mutation via tracking `tail` pointer. |
| **Undo Last Transaction** | O(1) | O(1) | Node severance by reassigning the `tail` to `tail.prev`. |
| **Render Audit History** | O(N) | O(N) | Backward structural traversal starting from latest entry. |

---

## 🛠️ Local Installation & Run

### 1. Clone the repository
```bash
git clone https://github.com
cd bank-ledger-dsa
```

### 2. Configure Virtual Environment & Dependencies
```bash
# Create and activate environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required core modules
pip install -r requirements.txt
```

### 3. Start Web Dashboard Application
```bash
streamlit run ledger.py
```

---

## 📂 Repository Architecture
```text
bank-ledger-dsa/
├── venv/                 # Isolated local runtime environment (Omitted from Git)
├── .gitignore            # Rules specifying file tracking exemptions
├── app.py                # Main project file containing DLL & Streamlit app logic
├── README.md             # Developer documentation and system profile
└── requirements.txt      # Production package dependency registry
```
