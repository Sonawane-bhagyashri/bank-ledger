Enterprise Banking Ledger Engine is a real-time transactional stream simulation and financial auditing dashboard built using Python and Streamlit.
To demonstrate robust, low-level backend engineering principles required for enterprise FinTech platforms, this project completely bypasses standard database frameworks to implement a high-performance custom Doubly Linked List (DLL) architecture directly inside system memory.

🚀 Key Technical Highlights

• Constant Time Complexity (O(1)): Leverages direct heap-allocated pointer chains (TransactionNode) ensuring that account modifications and structural push logs happen at an absolute performance scale of O(1).
• Algorithmic Rollback Tracking: Features a low-latency data rollback engine utilizing backward-traversal manipulation (.prev) to execute instant transaction undos and restore previous account balance layers at O(1) complexity.
• State Persistence Control: Binds custom data structures securely within a continuous Streamlit session_state scope to prevent data drops across dynamic web re-renders and form submissions.
• Proactive Security Guards: Implements embedded validation logic that intercepts invalid entry sizes or overdraft attempts before record mutations are allowed to commit to history.

⚙️ Core Stack & Concepts Demonstrated

• Languages & Frameworks: Python 3.x, Streamlit (Interactive Frontend Dashboard Architecture)
• Data Structures & Algorithms: Custom Doubly Linked List (DLL), Linear Traversal Loops, Pointer Manipulation, State Management Control.
![Project Screenshot](image_ledger%20(2).jpg)
