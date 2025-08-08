import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q4 = {'매우 그렇다': {'궁수': 1.0, '전사': 0.8, '마법사': 0.6, '도적': 0.4, '해적': 0.2}, '그렇다': {'전사': 1.0, '마법사': 0.8, '궁수': 0.6, '도적': 0.4, '해적': 0.2}, '보통이다': {'마법사': 1.0, '궁수': 0.8, '전사': 0.6, '해적': 0.4, '도적': 0.2}, '그렇지 않다': {'도적': 1.0, '해적': 0.8, '궁수': 0.6, '전사': 0.4, '마법사': 0.2}, '전혀 그렇지 않다': {'해적': 1.0, '도적': 0.8, '전사': 0.6, '마법사': 0.4, '궁수': 0.2}}

def show():
    st.subheader("4. PVE: 지역마다 다른 몬스터와 전투하는 것이 흥미롭다")
    st.write("몬스터를 사냥하며 장비나 재료를 얻는 것이 즐겁다")
    st.write("탐험하는 것을 좋아하고 수집욕이 강하다")
    selected = st.radio("선택하세요:", answer_options, key="q4")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q4.get(selected))
        st.session_state.question_number = 5
        st.rerun()
