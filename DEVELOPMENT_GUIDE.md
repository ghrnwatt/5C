# 🔧 안양 유흥왕 5C 블로그 개발 가이드

이 문서는 안양 유흥왕 5C 블로그 애플리케이션을 커스터마이징하고 확장하는 방법을 설명합니다.

## 📁 프로젝트 구조

```
안양-유흥왕-5C-블로그/
├── app.py                  # 메인 Streamlit 애플리케이션
├── requirements.txt        # Python 의존성
├── start.sh               # 시작 스크립트
├── README.md              # 프로젝트 문서
├── DEVELOPMENT_GUIDE.md   # 개발 가이드 (이 파일)
├── venv/                  # Python 가상환경
└── .git/                  # Git 저장소
```

## 🎨 UI 커스터마이징

### 1. CSS 스타일 수정

`app.py` 파일의 CSS 섹션에서 스타일을 변경할 수 있습니다:

```python
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        # 여기서 배경색을 변경
    }
    .venue-card {
        background: #f8f9fa;
        # 카드 배경색 변경
    }
</style>
""", unsafe_allow_html=True)
```

### 2. 색상 테마 변경

주요 색상들:
- 메인 컬러: `#667eea`, `#764ba2` (그라데이션)
- 카드 배경: `#f8f9fa`
- 텍스트 링크: `#667eea`

### 3. 로고 및 이미지 변경

사이드바의 플레이스홀더 이미지를 실제 로고로 교체:

```python
st.image("path/to/your/logo.png", width=200)
```

## 📊 데이터 관리

### 1. 샘플 데이터 수정

`load_sample_data()` 함수에서 데이터를 수정:

```python
def load_sample_data():
    venues = pd.DataFrame({
        'name': ['새로운 업소명', '다른 업소명', ...],
        'category': ['클럽', '바', '노래방', ...],
        'rating': [4.5, 4.2, 4.8, ...],
        'location': ['안양역 근처', '평촌역 근처', ...],
        'price_range': ['$$$$', '$$$', '$$', ...]
    })
    return venues, blog_posts, events
```

### 2. 데이터베이스 연동

향후 데이터베이스 연동을 위한 구조:

```python
import sqlite3
# 또는
import mysql.connector
# 또는
from sqlalchemy import create_engine
```

### 3. 실시간 데이터 로딩

```python
@st.cache_data(ttl=3600)  # 1시간 캐시
def load_live_data():
    # API 호출 또는 데이터베이스 쿼리
    pass
```

## 🎯 새로운 기능 추가

### 1. 새 페이지 추가

1. 사이드바 메뉴에 옵션 추가:
```python
selected = option_menu(
    menu_title="메뉴",
    options=["홈", "블로그", "베뉴 리뷰", "이벤트", "랭킹", "소개", "새 페이지"],
    # ...
)
```

2. 조건문 추가:
```python
elif selected == "새 페이지":
    st.header("새 페이지")
    # 페이지 내용 추가
```

### 2. 새로운 위젯 추가

#### 검색 기능
```python
search_term = st.text_input("🔍 검색", placeholder="업소명이나 키워드를 입력하세요")
if search_term:
    # 검색 로직 구현
    filtered_data = data[data['name'].str.contains(search_term, case=False)]
```

#### 필터링 기능
```python
col1, col2, col3 = st.columns(3)
with col1:
    category_filter = st.selectbox("카테고리", options)
with col2:
    rating_filter = st.slider("최소 평점", 1.0, 5.0, 1.0)
with col3:
    price_filter = st.multiselect("가격대", price_options)
```

### 3. 차트 및 시각화 추가

#### 새로운 차트 타입
```python
import plotly.graph_objects as go

# 도넛 차트
fig = go.Figure(data=[go.Pie(labels=categories, values=counts, hole=.3)])
st.plotly_chart(fig)

# 산점도
fig = px.scatter(df, x='price', y='rating', color='category')
st.plotly_chart(fig)
```

## 🔧 고급 기능

### 1. 사용자 인증

```python
import streamlit_authenticator as stauth

# 인증 설정
authenticator = stauth.Authenticate(
    credentials,
    cookie_name,
    cookie_key,
    cookie_expiry_days
)

name, authentication_status, username = authenticator.login('Login', 'main')
```

### 2. 파일 업로드

```python
uploaded_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드된 이미지')
```

### 3. 폼 제출 처리

```python
with st.form("venue_form"):
    name = st.text_input("업소명")
    category = st.selectbox("카테고리", categories)
    rating = st.slider("평점", 1.0, 5.0, 3.0)
    
    submitted = st.form_submit_button("제출")
    if submitted:
        # 데이터 저장 로직
        save_venue_data(name, category, rating)
        st.success("저장되었습니다!")
```

## 📱 반응형 디자인

### 모바일 최적화

```python
# 화면 크기에 따른 컬럼 조정
if st.session_state.get('mobile_view', False):
    col1, col2 = st.columns([1, 1])
else:
    col1, col2, col3, col4 = st.columns(4)
```

### 컨테이너 활용

```python
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        # 메인 콘텐츠
        pass
    with col2:
        # 사이드 콘텐츠
        pass
```

## 🎨 테마 및 스타일링

### 다크 모드 지원

```python
# .streamlit/config.toml 파일 생성
[theme]
primaryColor = "#667eea"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#262730"
textColor = "#fafafa"
```

### 커스텀 CSS 클래스

```python
st.markdown("""
<style>
    .custom-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .highlight-text {
        color: #667eea;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 사용법
st.markdown('<div class="custom-card">커스텀 카드</div>', unsafe_allow_html=True)
```

## 🚀 성능 최적화

### 1. 캐싱 활용

```python
@st.cache_data
def expensive_computation(data):
    # 무거운 연산
    return result

@st.cache_resource
def init_model():
    # 모델 초기화
    return model
```

### 2. 세션 상태 관리

```python
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# 세션 상태 사용
st.session_state.key = new_value
```

### 3. 페이지네이션

```python
def paginate_dataframe(df, page_size=10):
    page_number = st.number_input('페이지', min_value=1, max_value=len(df)//page_size+1)
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    return df.iloc[start_idx:end_idx]
```

## 🔍 디버깅 및 로깅

### 개발 모드 활성화

```python
DEBUG = True

if DEBUG:
    st.sidebar.markdown("### 🔧 디버그 정보")
    st.sidebar.json(st.session_state)
```

### 로깅 설정

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("애플리케이션 시작")
```

## 📦 배포 준비

### 1. requirements.txt 업데이트

```bash
pip freeze > requirements.txt
```

### 2. Streamlit 설정 파일

`.streamlit/config.toml` 생성:

```toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
```

### 3. Docker 설정 (선택사항)

`Dockerfile` 생성:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

## 🤝 기여 가이드라인

1. 새로운 기능 추가 시 함수를 모듈화하세요
2. 코드에 주석을 충분히 추가하세요
3. 큰 변경사항은 별도 브랜치에서 작업하세요
4. 테스트를 거친 후 메인 브랜치에 병합하세요

## ❓ 문제 해결

### 자주 발생하는 문제들

1. **포트 충돌**: 다른 포트 사용 `--server.port 8502`
2. **패키지 충돌**: 가상환경 재생성
3. **캐시 문제**: `st.cache_data.clear()` 또는 브라우저 캐시 삭제

### 성능 이슈

1. 큰 데이터셋은 `@st.cache_data` 활용
2. 이미지는 적절한 크기로 리사이즈
3. 무거운 연산은 백그라운드에서 처리

## 📞 지원

- 개발 관련 문의: contact@anyang5c.com
- GitHub Issues: 프로젝트 리포지토리에서 이슈 등록
- 문서 개선 제안: Pull Request 환영

---

이 가이드를 통해 안양 유흥왕 5C 블로그를 자유롭게 커스터마이징하고 확장해보세요! 🚀