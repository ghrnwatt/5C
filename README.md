# 🌟 안양 유흥왕 5C - 유흥 블로그

안양 지역 최고의 유흥 정보를 제공하는 Streamlit 기반 웹 애플리케이션입니다.

## 📋 주요 기능

- **홈페이지**: 최신 블로그 포스트, 인기 베뉴, 통계 정보
- **블로그**: 카테고리별 블로그 포스트 관리
- **베뉴 리뷰**: 업소별 상세 리뷰 및 평점 시스템
- **이벤트**: 최신 이벤트 정보 및 제보 기능
- **랭킹**: 업소별 랭킹 및 데이터 분석
- **소개**: 블로그 소개 및 연락처 정보

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **Data Visualization**: Plotly
- **Data Processing**: Pandas
- **UI Components**: streamlit-option-menu

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone <repository-url>
cd anyang-nightlife-blog
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행
```bash
streamlit run app.py
```

### 4. 브라우저에서 확인
애플리케이션이 실행되면 자동으로 브라우저가 열리거나, 다음 URL로 접속하세요:
```
http://localhost:8501
```

## 📁 프로젝트 구조

```
anyang-nightlife-blog/
├── app.py              # 메인 Streamlit 애플리케이션
├── requirements.txt    # Python 의존성
├── README.md          # 프로젝트 문서
└── .git/              # Git 저장소
```

## 🎨 주요 페이지

### 홈페이지
- 블로그 통계 및 주요 메트릭
- 최신 블로그 포스트 미리보기
- 인기 베뉴 순위
- 카테고리별 평점 차트

### 블로그
- 카테고리별 포스트 필터링
- 블로그 포스트 목록 및 내용
- 작성자 및 날짜 정보

### 베뉴 리뷰
- 카테고리 및 위치별 필터링
- 업소별 상세 정보 및 평점
- 가격대 정보

### 이벤트
- 최신 이벤트 정보
- 이벤트 제보 기능
- 날짜별 이벤트 관리

### 랭킹
- 평점 기반 업소 랭킹
- 카테고리별 평점 분석
- 데이터 시각화

## 🔧 사용자 정의

### 데이터 수정
`app.py` 파일의 `load_sample_data()` 함수에서 샘플 데이터를 수정할 수 있습니다:

```python
def load_sample_data():
    venues = pd.DataFrame({
        'name': ['업소명1', '업소명2', ...],
        'category': ['카테고리1', '카테고리2', ...],
        # ... 더 많은 데이터
    })
```

### 스타일 변경
CSS 스타일은 `app.py` 파일 상단의 `st.markdown()` 섹션에서 수정할 수 있습니다.

### 새로운 페이지 추가
사이드바 메뉴의 `options` 리스트에 새 항목을 추가하고, 해당하는 조건문을 작성하면 됩니다.

## 🚧 개발 중인 기능

- [ ] 데이터베이스 연동
- [ ] 사용자 인증 시스템
- [ ] 댓글 기능
- [ ] 이미지 업로드
- [ ] 모바일 최적화

## 📞 연락처

- 📧 이메일: contact@anyang5c.com
- 📱 카카오톡: 안양유흥왕5C
- 📍 위치: 안양시 만안구

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## ⚠️ 주의사항

- 이 애플리케이션은 책임감 있는 음주문화를 지향합니다.
- 모든 정보는 참고용이며, 실제 정보와 다를 수 있습니다.
- 미성년자의 이용을 금지합니다.