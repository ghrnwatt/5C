#!/bin/bash

# 안양 유흥왕 5C 블로그 시작 스크립트

echo "🌟 안양 유흥왕 5C 블로그를 시작합니다..."

# 가상환경 활성화
source venv/bin/activate

# Streamlit 애플리케이션 실행
echo "📱 Streamlit 서버를 시작합니다..."
echo "🌐 브라우저에서 http://localhost:8501 로 접속하세요"

streamlit run app.py --server.address 0.0.0.0 --server.port 8501