import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q2 = {'매우 그렇다': {'도적': 1.0, '해적': 0.8, '궁수': 0.6, '마법사': 0.4, '전사': 0.2}, '그렇다': {'궁수': 1.0, '도적': 0.8, '마법사': 0.6, '전사': 0.4, '해적': 0.2}, '보통이다': {'마법사': 1.0, '궁수': 0.8, '전사': 0.6, '해적': 0.4, '도적': 0.2}, '그렇지 않다': {'전사': 1.0, '해적': 0.8, '도적': 0.6, '궁수': 0.4, '마법사': 0.2}, '전혀 그렇지 않다': {'해적': 1.0, '전사': 0.8, '마법사': 0.6, '도적': 0.4, '궁수': 0.2}}

def show():
    st.subheader("2. 느긋하게 혼자 집에 있고 싶을 때가 많다")
    st.write("긴장감 있는 콘텐츠보다는 편안하고 반복 가능한 활동을 좋아한다")
    st.write("반복되는 루틴이 오히려 안정감을 준다")
    selected = st.radio("선택하세요:", answer_options, key="q2")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q2.get(selected))
        st.session_state.question_number = 3
        st.rerun()
