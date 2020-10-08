mkdir -p ~/.streamlit/
echo "[general]
email = \"aidancurley1012@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
