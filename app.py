import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
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
        options=["홈", "블로그", "베뉴 리뷰", "이벤트", "랭킹", "경쟁 대시보드", "소개"],
        icons=["house", "journal-text", "star", "calendar", "trophy", "graph-up-arrow", "info-circle"],
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

# 경쟁 대시보드용 확장 데이터
@st.cache_data
def load_competitive_data():
    # 확장된 업소 데이터 (경쟁사 포함)
    extended_venues = pd.DataFrame({
        'name': ['클럽 오로라', '바 레드문', '노래방 골드', '펍 블루나이트', '라운지 실버',
                '클럽 네온', '바 문라이트', '노래방 플래티넘', '펍 스타더스트', '라운지 골든'],
        'category': ['클럽', '바', '노래방', '펍', '라운지', '클럽', '바', '노래방', '펍', '라운지'],
        'rating': [4.5, 4.2, 4.8, 4.0, 4.3, 4.1, 3.9, 4.6, 3.8, 4.4],
        'location': ['안양역 근처', '평촌역 근처', '안양시청 근처', '범계역 근처', '인덕원역 근처',
                    '안양역 근처', '평촌역 근처', '안양시청 근처', '범계역 근처', '인덕원역 근처'],
        'price_range': ['$$$$', '$$$', '$$', '$$$', '$$$$', '$$$', '$$', '$$$', '$$', '$$$$'],
        'monthly_visitors': [1200, 800, 1500, 600, 900, 1000, 700, 1300, 550, 850],
        'avg_spending': [50000, 35000, 25000, 30000, 45000, 45000, 32000, 28000, 28000, 48000],
        'competitor': ['우리', '우리', '우리', '우리', '우리', '경쟁사', '경쟁사', '경쟁사', '경쟁사', '경쟁사']
    })

    # 시계열 데이터 (지난 30일)
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    time_series = pd.DataFrame({
        'date': dates,
        'visitors': np.random.poisson(1000, 30) + np.arange(30) * 10,
        'revenue': np.random.normal(5000000, 500000, 30) + np.arange(30) * 50000,
        'satisfaction': np.clip(np.random.normal(4.5, 0.3, 30), 3.0, 5.0),
        'competitor_visitors': np.random.poisson(800, 30) + np.arange(30) * 5
    })

    # 카테고리별 성과 데이터
    category_performance = pd.DataFrame({
        'category': ['클럽', '바', '노래방', '펍', '라운지'],
        'market_share': [25, 20, 30, 15, 10],
        'growth_rate': [15.5, 8.2, 22.3, 5.1, 12.8],
        'avg_rating': [4.3, 4.05, 4.7, 3.9, 4.35],
        'customer_retention': [75, 68, 82, 60, 72]
    })

    # 지역별 데이터
    location_data = pd.DataFrame({
        'location': ['안양역 근처', '평촌역 근처', '안양시청 근처', '범계역 근처', '인덕원역 근처'],
        'venue_count': [15, 22, 18, 20, 12],
        'avg_rating': [4.3, 4.1, 4.5, 4.0, 4.2],
        'total_visitors': [3500, 4200, 3800, 3600, 2900],
        'revenue': [18000000, 22000000, 19500000, 18500000, 15000000]
    })

    return extended_venues, time_series, category_performance, location_data

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

# 경쟁 대시보드 페이지
elif selected == "경쟁 대시보드":
    st.markdown("""
    <div class="main-header">
        <h1>📊 경쟁 분석 대시보드</h1>
        <h3>실시간 데이터 기반 전략적 인사이트</h3>
        <p>최정호도 울고 갈 최첨단 분석 대시보드</p>
    </div>
    """, unsafe_allow_html=True)

    # 데이터 로드
    extended_venues, time_series, category_performance, location_data = load_competitive_data()

    # 핵심 KPI 대시보드
    st.header("🎯 핵심 성과 지표 (KPI)")

    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

    our_venues = extended_venues[extended_venues['competitor'] == '우리']
    competitor_venues = extended_venues[extended_venues['competitor'] == '경쟁사']

    with kpi_col1:
        our_avg_rating = our_venues['rating'].mean()
        comp_avg_rating = competitor_venues['rating'].mean()
        delta = our_avg_rating - comp_avg_rating
        st.metric(
            label="평균 평점",
            value=f"{our_avg_rating:.2f}⭐",
            delta=f"{delta:+.2f} vs 경쟁사"
        )

    with kpi_col2:
        our_visitors = our_venues['monthly_visitors'].sum()
        comp_visitors = competitor_venues['monthly_visitors'].sum()
        delta_pct = ((our_visitors - comp_visitors) / comp_visitors * 100)
        st.metric(
            label="월 방문자 수",
            value=f"{our_visitors:,}명",
            delta=f"{delta_pct:+.1f}%"
        )

    with kpi_col3:
        our_revenue = (our_venues['monthly_visitors'] * our_venues['avg_spending']).sum()
        comp_revenue = (competitor_venues['monthly_visitors'] * competitor_venues['avg_spending']).sum()
        delta_pct = ((our_revenue - comp_revenue) / comp_revenue * 100)
        st.metric(
            label="월 예상 매출",
            value=f"{our_revenue/1000000:.1f}백만원",
            delta=f"{delta_pct:+.1f}%"
        )

    with kpi_col4:
        market_share = (our_visitors / (our_visitors + comp_visitors) * 100)
        st.metric(
            label="시장 점유율",
            value=f"{market_share:.1f}%",
            delta="선도적" if market_share > 50 else "성장 중"
        )

    st.markdown("---")

    # 트렌드 분석
    st.header("📈 트렌드 분석 (30일)")

    col1, col2 = st.columns(2)

    with col1:
        # 방문자 추세
        fig_visitors = go.Figure()
        fig_visitors.add_trace(go.Scatter(
            x=time_series['date'],
            y=time_series['visitors'],
            mode='lines+markers',
            name='우리 업소',
            line=dict(color='#667eea', width=3),
            fill='tozeroy'
        ))
        fig_visitors.add_trace(go.Scatter(
            x=time_series['date'],
            y=time_series['competitor_visitors'],
            mode='lines+markers',
            name='경쟁사',
            line=dict(color='#f56565', width=3, dash='dash')
        ))
        fig_visitors.update_layout(
            title='일일 방문자 추이',
            xaxis_title='날짜',
            yaxis_title='방문자 수',
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig_visitors, use_container_width=True)

    with col2:
        # 매출 및 만족도
        fig_revenue = make_subplots(specs=[[{"secondary_y": True}]])
        fig_revenue.add_trace(
            go.Bar(x=time_series['date'], y=time_series['revenue']/1000000,
                   name='매출', marker_color='#667eea'),
            secondary_y=False
        )
        fig_revenue.add_trace(
            go.Scatter(x=time_series['date'], y=time_series['satisfaction'],
                      name='고객 만족도', mode='lines+markers',
                      line=dict(color='#48bb78', width=3)),
            secondary_y=True
        )
        fig_revenue.update_xaxes(title_text="날짜")
        fig_revenue.update_yaxes(title_text="매출 (백만원)", secondary_y=False)
        fig_revenue.update_yaxes(title_text="만족도 (⭐)", secondary_y=True)
        fig_revenue.update_layout(
            title='매출 & 고객 만족도',
            hovermode='x unified',
            template='plotly_white'
        )
        st.plotly_chart(fig_revenue, use_container_width=True)

    st.markdown("---")

    # 경쟁사 비교 분석
    st.header("⚔️ 경쟁사 직접 대결")

    col1, col2 = st.columns(2)

    with col1:
        # 카테고리별 평점 비교
        comparison_df = extended_venues.groupby(['category', 'competitor'])['rating'].mean().reset_index()
        fig_rating_comp = px.bar(
            comparison_df,
            x='category',
            y='rating',
            color='competitor',
            barmode='group',
            title='카테고리별 평점 비교',
            color_discrete_map={'우리': '#667eea', '경쟁사': '#f56565'}
        )
        fig_rating_comp.update_layout(template='plotly_white')
        st.plotly_chart(fig_rating_comp, use_container_width=True)

    with col2:
        # 방문자 수 비교
        visitor_comp = extended_venues.groupby(['category', 'competitor'])['monthly_visitors'].sum().reset_index()
        fig_visitor_comp = px.bar(
            visitor_comp,
            x='category',
            y='monthly_visitors',
            color='competitor',
            barmode='group',
            title='카테고리별 방문자 수 비교',
            color_discrete_map={'우리': '#667eea', '경쟁사': '#f56565'}
        )
        fig_visitor_comp.update_layout(template='plotly_white')
        st.plotly_chart(fig_visitor_comp, use_container_width=True)

    st.markdown("---")

    # 카테고리별 성과 분석
    st.header("🎯 카테고리별 성과 분석")

    col1, col2 = st.columns(2)

    with col1:
        # 시장 점유율 파이 차트
        fig_market = px.pie(
            category_performance,
            values='market_share',
            names='category',
            title='카테고리별 시장 점유율',
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig_market, use_container_width=True)

    with col2:
        # 성장률 vs 고객 유지율
        fig_growth = px.scatter(
            category_performance,
            x='growth_rate',
            y='customer_retention',
            size='market_share',
            color='category',
            title='성장률 vs 고객 유지율',
            labels={'growth_rate': '성장률 (%)', 'customer_retention': '고객 유지율 (%)'},
            text='category'
        )
        fig_growth.update_traces(textposition='top center')
        fig_growth.update_layout(template='plotly_white')
        st.plotly_chart(fig_growth, use_container_width=True)

    # 성과 테이블
    st.subheader("📋 상세 성과 지표")
    styled_performance = category_performance.copy()
    styled_performance.columns = ['카테고리', '시장점유율(%)', '성장률(%)', '평균평점', '고객유지율(%)']
    st.dataframe(
        styled_performance.style.background_gradient(cmap='RdYlGn', subset=['성장률(%)', '평균평점', '고객유지율(%)']),
        use_container_width=True
    )

    st.markdown("---")

    # 지역별 분석
    st.header("🗺️ 지역별 성과 분석")

    col1, col2 = st.columns(2)

    with col1:
        # 지역별 매출
        fig_location_revenue = px.bar(
            location_data,
            x='location',
            y='revenue',
            title='지역별 월 매출',
            color='revenue',
            color_continuous_scale='Viridis'
        )
        fig_location_revenue.update_layout(
            xaxis_title='지역',
            yaxis_title='매출 (원)',
            template='plotly_white'
        )
        st.plotly_chart(fig_location_revenue, use_container_width=True)

    with col2:
        # 지역별 평점 vs 방문자
        fig_location_perf = px.scatter(
            location_data,
            x='avg_rating',
            y='total_visitors',
            size='revenue',
            color='location',
            title='지역별 평점 vs 방문자 수',
            labels={'avg_rating': '평균 평점', 'total_visitors': '총 방문자'},
            text='location'
        )
        fig_location_perf.update_traces(textposition='top center')
        fig_location_perf.update_layout(template='plotly_white')
        st.plotly_chart(fig_location_perf, use_container_width=True)

    st.markdown("---")

    # 가격 대비 가치 분석
    st.header("💰 가격 대비 가치 분석")

    price_map = {'$': 1, '$$': 2, '$$$': 3, '$$$$': 4}
    extended_venues['price_numeric'] = extended_venues['price_range'].map(price_map)

    fig_value = px.scatter(
        extended_venues,
        x='price_numeric',
        y='rating',
        size='monthly_visitors',
        color='competitor',
        hover_data=['name', 'category'],
        title='가격대별 평점 분석 (버블 크기 = 방문자 수)',
        labels={'price_numeric': '가격대', 'rating': '평점'},
        color_discrete_map={'우리': '#667eea', '경쟁사': '#f56565'}
    )
    fig_value.update_layout(template='plotly_white')
    st.plotly_chart(fig_value, use_container_width=True)

    st.markdown("---")

    # 예측 분석
    st.header("🔮 예측 분석 (향후 7일)")

    # 간단한 선형 예측
    from sklearn.linear_model import LinearRegression

    X = np.arange(len(time_series)).reshape(-1, 1)
    y_visitors = time_series['visitors'].values
    y_revenue = time_series['revenue'].values

    model_visitors = LinearRegression().fit(X, y_visitors)
    model_revenue = LinearRegression().fit(X, y_revenue)

    future_X = np.arange(len(time_series), len(time_series) + 7).reshape(-1, 1)
    future_dates = pd.date_range(start=time_series['date'].max() + timedelta(days=1), periods=7, freq='D')

    pred_visitors = model_visitors.predict(future_X)
    pred_revenue = model_revenue.predict(future_X)

    col1, col2 = st.columns(2)

    with col1:
        fig_pred_visitors = go.Figure()
        fig_pred_visitors.add_trace(go.Scatter(
            x=time_series['date'],
            y=time_series['visitors'],
            mode='lines+markers',
            name='실제 데이터',
            line=dict(color='#667eea', width=2)
        ))
        fig_pred_visitors.add_trace(go.Scatter(
            x=future_dates,
            y=pred_visitors,
            mode='lines+markers',
            name='예측',
            line=dict(color='#48bb78', width=2, dash='dash')
        ))
        fig_pred_visitors.update_layout(
            title='방문자 수 예측',
            xaxis_title='날짜',
            yaxis_title='방문자 수',
            template='plotly_white'
        )
        st.plotly_chart(fig_pred_visitors, use_container_width=True)

    with col2:
        fig_pred_revenue = go.Figure()
        fig_pred_revenue.add_trace(go.Scatter(
            x=time_series['date'],
            y=time_series['revenue']/1000000,
            mode='lines+markers',
            name='실제 데이터',
            line=dict(color='#667eea', width=2)
        ))
        fig_pred_revenue.add_trace(go.Scatter(
            x=future_dates,
            y=pred_revenue/1000000,
            mode='lines+markers',
            name='예측',
            line=dict(color='#48bb78', width=2, dash='dash')
        ))
        fig_pred_revenue.update_layout(
            title='매출 예측',
            xaxis_title='날짜',
            yaxis_title='매출 (백만원)',
            template='plotly_white'
        )
        st.plotly_chart(fig_pred_revenue, use_container_width=True)

    # 예측 요약
    st.info(f"""
    📊 **7일 예측 요약**
    - 예상 총 방문자: {pred_visitors.sum():,.0f}명
    - 예상 총 매출: {pred_revenue.sum()/1000000:.1f}백만원
    - 일평균 방문자 증가율: {((pred_visitors[-1] - y_visitors[-1]) / y_visitors[-1] * 100):.1f}%
    """)

    st.markdown("---")

    # 전략적 인사이트
    st.header("💡 전략적 인사이트")

    insight_col1, insight_col2, insight_col3 = st.columns(3)

    with insight_col1:
        st.markdown("""
        <div class="venue-card">
            <h4>🎯 강점</h4>
            <ul>
                <li>평균 평점 경쟁사 대비 우위</li>
                <li>노래방 카테고리 압도적 성장</li>
                <li>안양시청 지역 높은 만족도</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with insight_col2:
        st.markdown("""
        <div class="venue-card">
            <h4>⚠️ 개선 필요</h4>
            <ul>
                <li>펍 카테고리 성장률 저조</li>
                <li>인덕원 지역 방문자 증대 필요</li>
                <li>고가 업소 가성비 개선</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with insight_col3:
        st.markdown("""
        <div class="venue-card">
            <h4>🚀 기회</h4>
            <ul>
                <li>평촌 지역 시장 확대 가능</li>
                <li>라운지 고객 유지율 활용</li>
                <li>방문자 증가 추세 지속</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

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