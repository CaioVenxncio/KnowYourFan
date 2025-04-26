import streamlit as st
import sqlite3
import pytesseract
from PIL import Image, ImageOps
import io
import re

# ==== ATENÇÃO: Isso precisa vir AQUI! ====
st.set_page_config(page_title="Know Your Fan - FURIA", layout="wide")

# ==== BANCO DE DADOS SQLite ====
conn = sqlite3.connect("fans.db")
c = conn.cursor()

# Criação da tabela se não existir
c.execute("""
    CREATE TABLE IF NOT EXISTS fans (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cpf TEXT,
        endereco TEXT,
        interesses TEXT,
        atividades TEXT,
        compras TEXT,
        social_links TEXT,
        esports_profiles TEXT
    )
""")
conn.commit()

# Função de validação de CPF
def valida_cpf(cpf: str) -> bool:
    cpf_num = re.sub(r"\D", "", cpf)
    if len(cpf_num) != 11 or cpf_num == cpf_num[0] * 11:
        return False
    def calc_dig(nums):
        s = sum(int(d) * w for d, w in zip(nums, range(len(nums)+1, 1, -1)))
        r = (s * 10) % 11
        return r if r < 10 else 0
    d1 = calc_dig(cpf_num[:9])
    d2 = calc_dig(cpf_num[:10])
    return d1 == int(cpf_num[9]) and d2 == int(cpf_num[10])

# Função de validação de documento com OCR
def valida_documento(file, nome):
    image = Image.open(io.BytesIO(file))
    image = ImageOps.grayscale(image)
    image = ImageOps.invert(image)
    text = pytesseract.image_to_string(image, lang='por')
    valid = re.search(re.escape(nome.split()[0]), text, re.IGNORECASE) is not None
    return valid, text

# ==== FRONTEND - Streamlit ====
st.title("Know Your Fan 🧠 - FURIA Edition")

# Layout do sidebar
senha_acesso = st.sidebar.text_input("🔒 Acesso Admin", type="password")

# Mostra as opções conforme o acesso
if senha_acesso == "minhasenhafuria":
    page = st.sidebar.radio("Ir para", ["Cadastro", "Validação", "Fãs Cadastrados"])
else:
    page = st.sidebar.radio("Ir para", ["Cadastro", "Validação"])

if page == "Cadastro":
    st.header("📋 Formulário de Cadastro")
    with st.form(key="form_cadastro"):
        nome = st.text_input("Nome completo *", placeholder="Ex: João Silva")
        cpf = st.text_input("CPF *", placeholder="___.___.___-__")
        endereco = st.text_input("Endereço", placeholder="Rua Exemplo, 123")
        interesses = st.text_area("Interesses em e-sports", placeholder="Times, jogos...")
        atividades = st.text_area("Atividades do último ano", placeholder="Campeonatos, streams...")
        compras = st.text_area("Compras no último ano", placeholder="Ingressos, periféricos...")
        social_links = st.text_area("Links das redes sociais", help="Um link por linha")
        esports_profiles = st.text_area("Perfis em sites e-sports", help="Faceit, HLTV etc.")
        submitted = st.form_submit_button("Enviar Dados")

    if submitted:
        if not nome or not cpf:
            st.error("Campos marcados com * são obrigatórios.")
        else:
            with st.spinner("Enviando dados..."):
                if not valida_cpf(cpf):
                    st.error("CPF inválido.")
                else:
                    # Salvar os dados no banco de dados SQLite
                    c.execute("""
                        INSERT INTO fans (nome, cpf, endereco, interesses, atividades, compras, social_links, esports_profiles)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, (nome, cpf, endereco, interesses, atividades, compras, social_links, esports_profiles))
                    conn.commit()
                    st.success("Dados enviados com sucesso!")

elif page == "Validação":
    st.header("📄 Validação de Documento")
    nome_val = st.text_input("Nome para validação *", placeholder="Mesmo nome do cadastro")
    doc = st.file_uploader("Envie imagem do RG ou CNH", type=["jpg", "png", "jpeg"])

    if st.button("Validar Documento"):
        if not nome_val or not doc:
            st.error("Preencha o nome e carregue uma imagem.")
        else:
            with st.spinner("Validando OCR..."):
                file = doc.getvalue()
                valid, ocr_text = valida_documento(file, nome_val)
                if valid:
                    st.success("✅ Documento válido!")
                else:
                    st.warning("❌ Nome não encontrado no documento.")
                st.text_area("Texto extraído (OCR)", ocr_text)

elif page == "Fãs Cadastrados":
    st.header("📋 Lista de Fãs Cadastrados")
    with st.spinner("Carregando dados..."):
        c.execute("SELECT * FROM fans")
        fans = c.fetchall()
        for fan in fans:
            with st.expander(f"{fan[1]} - ID {fan[0]}"):
                st.markdown(f"**CPF:** {fan[2]}")
                st.markdown(f"**Endereço:** {fan[3]}")
                st.markdown(f"**Interesses:** {fan[4]}")
                st.markdown(f"**Atividades:** {fan[5]}")
                st.markdown(f"**Compras:** {fan[6]}")
                st.markdown("**Links sociais:**")
                for link in fan[7].split("|"):
                    st.markdown(f"- {link}")
                st.markdown("**Perfis e-sports:**")
                for profile in fan[8].split("|"):
                    st.markdown(f"- {profile}")


