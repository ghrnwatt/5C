import streamlit as st
import pandas as pd
from datetime import datetime, date
import plotly.express as px
from streamlit_option_menu import option_menu

# 페이지 설정
st.set_page_config(
    page_title="안양 유흥왕 5C - 안양 최고의 유흥 정보",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .venue-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .blog-post {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .event-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
    .metric-card {
        background: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 사이드바 메뉴
with st.sidebar:
    st.image("https://via.placeholder.com/200x100/667eea/ffffff?text=안양+유흥왕+5C", width=200)
    
    selected = option_menu(
        menu_title="메뉴",
        options=["홈", "블로그", "베뉴 리뷰", "이벤트", "랭킹", "소개"],
        icons=["house", "journal-text", "star", "calendar", "trophy", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )

# 샘플 데이터
@st.cache_data
def load_sample_data():
    venues = pd.DataFrame({
        'name': ['클럽 오로라', '바 레드문', '노래방 골드', '펍 블루나이트', '라운지 실버'],
        'category': ['클럽', '바', '노래방', '펍', '라운지'],
        'rating': [4.5, 4.2, 4.8, 4.0, 4.3],
        'location': ['안양역 근처', '평촌역 근처', '안양시청 근처', '범계역 근처', '인덕원역 근처'],
        'price_range': ['$$$$', '$$$', '$$', '$$$', '$$$$']
    })
    
    blog_posts = [
        {
            'title': '안양 최고의 클럽 탐방기',
            'date': '2024-01-15',
            'category': '클럽 리뷰',
            'content': '안양에서 가장 핫한 클럽들을 직접 방문해서 리뷰했습니다. 음악, 분위기, 서비스 모든 면에서...',
            'author': '유흥왕 5C'
        },
        {
            'title': '평촌 바 거리 완전 정복',
            'date': '2024-01-10',
            'category': '바 리뷰',
            'content': '평촌역 근처의 숨겨진 바들을 찾아서 떠난 여행. 각각의 특색있는 분위기와 시그니처 칵테일...',
            'author': '유흥왕 5C'
        },
        {
            'title': '2024년 안양 유흥업소 트렌드',
            'date': '2024-01-05',
            'category': '트렌드',
            'content': '새해를 맞아 안양 유흥업소들의 최신 트렌드를 분석해봤습니다. 올해는 어떤 변화가...',
            'author': '유흥왕 5C'
        }
    ]
    
    events = [
        {
            'title': '신년 특별 파티',
            'date': '2024-02-01',
            'venue': '클럽 오로라',
            'description': '새해를 맞아 진행되는 특별 파티 이벤트'
        },
        {
            'title': '발렌타인 커플 이벤트',
            'date': '2024-02-14',
            'venue': '라운지 실버',
            'description': '연인들을 위한 특별한 이벤트와 할인'
        }
    ]
    
    return venues, blog_posts, events

venues_df, blog_posts, events = load_sample_data()

# 메인 페이지
if selected == "홈":
    # 헤더
    st.markdown("""
    <div class="main-header">
        <h1>🌟 안양 유흥왕 5C</h1>
        <h3>안양 최고의 유흥 정보를 제공합니다</h3>
        <p>신뢰할 수 있는 리뷰와 최신 정보로 여러분의 밤을 완벽하게!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 메트릭 카드
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>150+</h2>
            <p>리뷰된 업소</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>50+</h2>
            <p>블로그 포스트</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>1000+</h2>
            <p>만족한 고객</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>4.8⭐</h2>
            <p>평균 평점</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 최신 블로그 포스트
    st.header("📝 최신 블로그 포스트")
    
    for post in blog_posts[:2]:
        st.markdown(f"""
        <div class="blog-post">
            <h3>{post['title']}</h3>
            <p><strong>카테고리:</strong> {post['category']} | <strong>날짜:</strong> {post['date']} | <strong>작성자:</strong> {post['author']}</p>
            <p>{post['content']}</p>
            <p><a href="#" style="color: #667eea;">더 읽기 →</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 인기 베뉴
    st.header("⭐ 이주의 인기 베뉴")
    
    col1, col2 = st.columns(2)
    
    with col1:
        top_venues = venues_df.nlargest(3, 'rating')
        for _, venue in top_venues.iterrows():
            st.markdown(f"""
            <div class="venue-card">
                <h4>{venue['name']}</h4>
                <p><strong>카테고리:</strong> {venue['category']}</p>
                <p><strong>평점:</strong> {venue['rating']}⭐</p>
                <p><strong>위치:</strong> {venue['location']}</p>
                <p><strong>가격대:</strong> {venue['price_range']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # 카테고리별 평점 차트
        fig = px.bar(venues_df, x='category', y='rating', 
                     title='카테고리별 평균 평점',
                     color='rating',
                     color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)

# 블로그 페이지
elif selected == "블로그":
    st.header("📖 블로그 포스트")
    
    # 카테고리 필터
    categories = ['전체'] + list(set([post['category'] for post in blog_posts]))
    selected_category = st.selectbox("카테고리 선택", categories)
    
    # 블로그 포스트 표시
    filtered_posts = blog_posts if selected_category == '전체' else [post for post in blog_posts if post['category'] == selected_category]
    
    for post in filtered_posts:
        st.markdown(f"""
        <div class="blog-post">
            <h3>{post['title']}</h3>
            <p><strong>카테고리:</strong> {post['category']} | <strong>날짜:</strong> {post['date']} | <strong>작성자:</strong> {post['author']}</p>
            <p>{post['content']}</p>
            <button style="background-color: #667eea; color: white; border: none; padding: 10px 20px; border-radius: 5px;">더 읽기</button>
        </div>
        """, unsafe_allow_html=True)

# 베뉴 리뷰 페이지
elif selected == "베뉴 리뷰":
    st.header("⭐ 베뉴 리뷰")
    
    # 필터링 옵션
    col1, col2 = st.columns(2)
    with col1:
        category_filter = st.selectbox("카테고리", ['전체'] + list(venues_df['category'].unique()))
    with col2:
        location_filter = st.selectbox("위치", ['전체'] + list(venues_df['location'].unique()))
    
    # 데이터 필터링
    filtered_venues = venues_df.copy()
    if category_filter != '전체':
        filtered_venues = filtered_venues[filtered_venues['category'] == category_filter]
    if location_filter != '전체':
        filtered_venues = filtered_venues[filtered_venues['location'] == location_filter]
    
    # 베뉴 카드 표시
    for _, venue in filtered_venues.iterrows():
        st.markdown(f"""
        <div class="venue-card">
            <h3>{venue['name']}</h3>
            <p><strong>카테고리:</strong> {venue['category']}</p>
            <p><strong>평점:</strong> {venue['rating']}⭐</p>
            <p><strong>위치:</strong> {venue['location']}</p>
            <p><strong>가격대:</strong> {venue['price_range']}</p>
            <p>상세한 리뷰와 방문 후기를 확인하실 수 있습니다.</p>
        </div>
        """, unsafe_allow_html=True)

# 이벤트 페이지
elif selected == "이벤트":
    st.header("🎉 이벤트 정보")
    
    for event in events:
        st.markdown(f"""
        <div class="event-card">
            <h3>{event['title']}</h3>
            <p><strong>날짜:</strong> {event['date']}</p>
            <p><strong>장소:</strong> {event['venue']}</p>
            <p>{event['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 새 이벤트 추가 폼
    st.markdown("---")
    st.subheader("📅 이벤트 제보하기")
    
    with st.form("event_form"):
        event_title = st.text_input("이벤트 제목")
        event_date = st.date_input("이벤트 날짜")
        event_venue = st.text_input("장소")
        event_description = st.text_area("설명")
        
        submitted = st.form_submit_button("제보하기")
        if submitted:
            st.success("이벤트 제보가 완료되었습니다!")

# 랭킹 페이지
elif selected == "랭킹":
    st.header("🏆 안양 유흥업소 랭킹")
    
    # 전체 랭킹
    st.subheader("전체 랭킹")
    ranked_venues = venues_df.sort_values('rating', ascending=False).reset_index(drop=True)
    ranked_venues.index += 1
    
    for idx, venue in ranked_venues.iterrows():
        medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"{idx}위"
        st.markdown(f"""
        <div class="venue-card">
            <h4>{medal} {venue['name']}</h4>
            <p><strong>카테고리:</strong> {venue['category']} | <strong>평점:</strong> {venue['rating']}⭐</p>
            <p><strong>위치:</strong> {venue['location']} | <strong>가격대:</strong> {venue['price_range']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 카테고리별 랭킹 차트
    st.subheader("카테고리별 평점 분석")
    fig = px.box(venues_df, x='category', y='rating', 
                 title='카테고리별 평점 분포',
                 color='category')
    st.plotly_chart(fig, use_container_width=True)

# 소개 페이지
elif selected == "소개":
    st.header("ℹ️ 안양 유흥왕 5C 소개")
    
    st.markdown("""
    <div class="blog-post">
        <h3>🌟 안양 유흥왕 5C란?</h3>
        <p>
        안양 유흥왕 5C는 안양 지역 최고의 유흥 정보를 제공하는 전문 블로그입니다. 
        우리는 직접 방문하고 경험한 솔직한 리뷰를 통해 여러분의 선택을 도와드립니다.
        </p>
        
        <h3>📋 우리의 미션</h3>
        <ul>
            <li>정확하고 신뢰할 수 있는 업소 정보 제공</li>
            <li>공정하고 객관적인 리뷰</li>
            <li>최신 이벤트 및 프로모션 정보</li>
            <li>고객 중심의 서비스</li>
        </ul>
        
        <h3>⭐ 우리의 특징</h3>
        <ul>
            <li><strong>전문성:</strong> 5년 이상의 업계 경험</li>
            <li><strong>신뢰성:</strong> 실제 방문 후 작성되는 리뷰</li>
            <li><strong>최신성:</strong> 매주 업데이트되는 정보</li>
            <li><strong>다양성:</strong> 클럽, 바, 노래방, 펍 등 다양한 업소</li>
        </ul>
        
        <h3>📞 연락처</h3>
        <p>
        📧 이메일: contact@anyang5c.com<br>
        📱 카카오톡: 안양유흥왕5C<br>
        📍 위치: 안양시 만안구
        </p>
    </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>© 2024 안양 유흥왕 5C. All rights reserved.</p>
    <p>책임감 있는 음주문화를 지향합니다.</p>
</div>
""", unsafe_allow_html=True)