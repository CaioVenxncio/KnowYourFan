# Know Your Fan 🧠 - FURIA Edition

**Aplicativo Stand-alone em Streamlit para cadastro e validação de fãs de e-sports**

---

## 📝 Descrição
Este projeto é um aplicativo web stand-alone construído com **Streamlit** e **SQLite** para:

- Coletar informações de fãs de e-sports (nome, CPF, endereço, interesses, atividades, compras, links sociais e perfis de e-sports).
- Validar documentos (RG/CNH) por OCR usando **pytesseract**.
- Listar os fãs cadastrados em um painel acessível somente com senha de administrador.

A aplicação não requer um backend separado (FastAPI); toda a lógica de persistência e validação está embutida no script **`main.py`**.

---

## ⚙️ Funcionalidades Principais

1. **Formulário de Cadastro**  
   - Validação de campos obrigatórios (nome e CPF).  
   - Validação de formato de CPF (algoritmo de dígitos).  
   - Armazenamento em banco de dados SQLite local (`fans.db`).

2. **Validação de Documento**  
   - Upload de imagem de RG/CNH (JPG, PNG, JPEG).  
   - Pré-processamento de imagem (grayscale + inversão).  
   - Extração de texto via OCR com `pytesseract`.  
   - Verificação de presença do nome cadastrado no documento.

3. **Painel de Fãs Cadastrados**  
   - Acesso restrito por senha de administrador.  
   - Exibição de todos os registros com detalhes em accordions.

---

## 🛠️ Requisitos

- Python 3.7 ou superior  
- Bibliotecas Python (ver **`requirements.txt`**):
  ```bash
  streamlit
  pytesseract
  pillow
  sqlite3 (incluso na biblioteca padrão)
  ```
- **Tesseract OCR** instalado no sistema operacional:
  - **Windows**: Instalar via instalador oficial e configurar PATH.  
  - **macOS**: `brew install tesseract`  
  - **Linux (Ubuntu/Debian)**: `sudo apt install tesseract-ocr`

---

## 🚀 Instalação e Execução Local

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/know-your-fan.git
   cd know-your-fan
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\Activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```bash
   streamlit run main.py
   ```

5. Abra no navegador: [http://localhost:8501](http://localhost:8501)

---

## 🔐 Acesso de Administrador

Para visualizar a aba **"Fãs Cadastrados"**, digite a senha de administrador no campo lateral:

```
🔒 Acesso Admin: minhasenhafuria
```

Substitua `minhasenhafuria` por uma senha mais segura em produção.

---

## ☁️ Deploy no Streamlit Community Cloud

1. Faça push do projeto para um repositório no GitHub.  
2. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte seu repositório.  
3. Aponte para o arquivo `main.py` e clique em **Deploy**.  
4. Compartilhe o link gerado (`https://share.streamlit.io/...`) com seus usuários.

---

## 📄 Licença
Concedido sob a [MIT License](LICENSE).

