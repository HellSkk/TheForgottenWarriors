import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q5 = {'매우 그렇다': {'도적': 1.0, '마법사': 0.8, '해적': 0.6, '전사': 0.4, '궁수': 0.2}, '그렇다': {'마법사': 1.0, '궁수': 0.8, '도적': 0.6, '해적': 0.4, '전사': 0.2}, '보통이다': {'궁수': 1.0, '전사': 0.8, '마법사': 0.6, '도적': 0.4, '해적': 0.2}, '그렇지 않다': {'전사': 1.0, '해적': 0.8, '궁수': 0.6, '마법사': 0.4, '도적': 0.2}, '전혀 그렇지 않다': {'해적': 1.0, '전사': 0.8, '도적': 0.6, '마법사': 0.4, '궁수': 0.2}}

def show():
    st.subheader("5. QUEST: 호기심이 많고 탐구하는 걸 좋아한다")
    st.write("게임의 스토리 전개가 기대된다")
    st.write("새로운 장소에 가면 ‘왜 이게 여기 있을까?’라는 생각이 먼저 난다")
    selected = st.radio("선택하세요:", answer_options, key="q5")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q5.get(selected))
        st.session_state.question_number = 6
        st.rerun()
