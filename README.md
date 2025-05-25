# Know Your Fan 🧠 - FURIA Edition

**Stand-alone Streamlit application for e-sports fan registration and validation**

---

## 📝 Description
This project is a stand-alone web application built with **Streamlit** and **SQLite** to:

- Collect data from e-sports fans (name, CPF, address, interests, activities, purchases, social links, and e-sports profiles).
- Validate documents (RG/CNH) via OCR using **pytesseract**.
- List registered fans in a panel accessible only with an admin password.

The application does not require a separate backend (like FastAPI); all persistence and validation logic is embedded in the **`main.py`** script.

---

## ⚙️ Key Features

1. **Registration Form**  
   - Validation of required fields (name and CPF).  
   - CPF format validation (digit check algorithm).  
   - Local SQLite database storage (`fans.db`).

2. **Document Validation**  
   - Upload of RG/CNH image (JPG, PNG, JPEG).  
   - Image preprocessing (grayscale + inversion).  
   - Text extraction via OCR with `pytesseract`.  
   - Check if the registered name is present in the document.

3. **Registered Fans Panel**  
   - Access restricted by admin password.  
   - Display of all records with details using accordions.

---

## 🛠️ Requirements

- Python 3.7 or higher  
- Python libraries (see **`requirements.txt`**):
  ```bash
  streamlit
  pytesseract
  pillow
  sqlite3 (included in Python standard library)
  ```
- **Tesseract OCR** installed on the system:
  - **Windows**: Install via official installer and configure PATH  
  - **macOS**: `brew install tesseract`  
  - **Linux (Ubuntu/Debian)**: `sudo apt install tesseract-ocr`

---

## 🚀 Local Installation and Execution

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/know-your-fan.git
   cd know-your-fan
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\Activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run main.py
   ```

5. Open in your browser: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Admin Access

To view the **"Registered Fans"** tab, enter the admin password in the sidebar:

```
🔒 Admin Access: minhasenhafuria
```

Replace `minhasenhafuria` with a more secure password in production.

---

## ☁️ Deploying to Streamlit Community Cloud

1. Push the project to a GitHub repository.  
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo.  
3. Point to the `main.py` file and click **Deploy**.  
4. Share the generated link (`https://share.streamlit.io/...`) with your users.

---


## 📄 Licença
Concedido sob a [MIT License](LICENSE).

