import streamlit as st
import asyncio
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import hashlib

# --------------------------------------------------
# KONFIGURASI STREAMLIT
# --------------------------------------------------

st.set_page_config(page_title="AI Programmer Consultant", page_icon="💻")
st.title("AI Programmer Consultant")

st.markdown(
    """
Selamat datang! Unggah file kode atau masukkan pertanyaan Anda di kolom chat untuk:
1. **Menganalisis kode** yang Anda unggah.
2. **Debugging** dan mencari error.
3. Memberikan rekomendasi **optimasi kode**.
4. Membuat kode baru berdasarkan kebutuhan Anda.
"""
)

# --------------------------------------------------
# PENGATURAN SIDEBAR
# --------------------------------------------------

openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="Masukkan API Key Anda",
)

model_list = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4", "gpt-o1", "gpt-o1-mini"]
chosen_model = st.sidebar.selectbox("Pilih model", model_list, index=0)

if not openai_api_key:
    st.warning("Masukkan OpenAI API Key untuk melanjutkan.")
    st.stop()

# --------------------------------------------------
# INISIALISASI LLM & CHAT HISTORY
# --------------------------------------------------

llm = ChatOpenAI(model_name=chosen_model, openai_api_key=openai_api_key, temperature=0.0)

# Inisialisasi riwayat pesan dan hash file sebelumnya
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "file_hash" not in st.session_state:
    st.session_state["file_hash"] = None

msgs = st.session_state["messages"]

if len(msgs) == 0:
    # Pesan awal dari AI
    initial_message = AIMessage(content="Halo! Saya siap membantu Anda. Silakan unggah file atau ketikkan pertanyaan Anda.")
    msgs.append(initial_message)

# --------------------------------------------------
# FILE UPLOADER
# --------------------------------------------------

uploaded_file = st.file_uploader("Unggah file kode yang ingin dianalisis", type=["py", "txt", "sql", "js"])
file_content = None

def calculate_file_hash(file_content):
    """Menghitung hash dari konten file untuk mendeteksi perubahan."""
    return hashlib.md5(file_content.encode()).hexdigest()

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    file_hash = calculate_file_hash(file_content)

    # Reset riwayat jika file baru berbeda
    if file_hash != st.session_state["file_hash"]:
        st.session_state["messages"] = []  # Reset riwayat
        st.session_state["file_hash"] = file_hash  # Simpan hash file baru
        initial_message = AIMessage(content="File baru telah diunggah. Silakan ajukan pertanyaan terkait file ini.")
        st.session_state["messages"].append(initial_message)
    else:
        st.info("File yang diunggah sama dengan sebelumnya. Riwayat percakapan tidak dihapus.")

    # Tampilkan isi file
    st.text_area("Isi file yang diunggah:", file_content, height=300)

# --------------------------------------------------
# MENAMPILKAN RIWAYAT CHAT
# --------------------------------------------------

def display_chat_history():
    """Menampilkan riwayat percakapan secara berurutan."""
    for message in st.session_state["messages"]:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("ai"):
                st.write(message.content)

# Render riwayat percakapan
display_chat_history()

# --------------------------------------------------
# INPUT CHAT
# --------------------------------------------------

user_input = st.chat_input("Tulis pertanyaan Anda di sini...")

async def process_user_input(user_input, file_content=None):
    """Memproses input user dan menambahkan konteks file jika ada."""
    system_message = SystemMessage(
        content=(
            "Kamu adalah asisten AI yang membantu analisis kode, debugging, optimasi, dan pembuatan kode baru."
        )
    )

    # Siapkan riwayat pesan
    chat_history = [system_message] + st.session_state["messages"]  # Tambahkan riwayat percakapan sebelumnya

    # Tambahkan input user dan file (jika ada)
    if file_content:
        user_input += f"\n\nKonteks file yang diunggah:\n{file_content}"
    chat_history.append(HumanMessage(content=user_input))

    # Kirim ke LLM
    return llm(chat_history).content

if user_input:
    # Tambahkan input user ke riwayat
    st.session_state["messages"].append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("AI sedang memproses..."):
        try:
            response_text = asyncio.run(process_user_input(user_input, file_content))
            
            # Tambahkan respons AI ke riwayat
            ai_response = AIMessage(content=response_text)
            st.session_state["messages"].append(ai_response)

            # Tampilkan respons AI
            with st.chat_message("ai"):
                st.write(response_text)
        except Exception as e:
            error_message = f"Terjadi error: {e}"
            st.session_state["messages"].append(AIMessage(content=error_message))
            st.error(error_message)
