import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q9 = {'매우 그렇다': {'마법사': 1.0, '궁수': 1.0, '해적': 0.6, '도적': 0.4, '전사': 0.2}, '그렇다': {'궁수': 1.0, '마법사': 0.8, '해적': 0.6, '도적': 0.4, '전사': 0.2}, '보통이다': {'마법사': 0.8, '궁수': 0.8, '도적': 0.6, '전사': 0.4, '해적': 0.2}, '그렇지 않다': {'전사': 1.0, '도적': 0.8, '궁수': 0.6, '마법사': 0.4, '해적': 0.2}, '전혀 그렇지 않다': {'도적': 1.0, '전사': 0.8, '궁수': 0.6, '마법사': 0.4, '해적': 0.2}}

def show():
    st.subheader("9. 직업 선호도: 원거리 직업을 선호한다")
    st.write("직접 부딪히기보다 안전한 거리에서 행동하는 걸 선호한다")
    st.write("상황을 멀리서 보고 판단하는 게 편하다고 느낀다")
    st.write("움직일 수 있는 공간이 넓을수록 마음이 편안하다")
    selected = st.radio("선택하세요:", answer_options, key="q9")
    if st.button("결과 보기"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q9.get(selected))
        st.session_state.question_number = 10
        st.rerun()
