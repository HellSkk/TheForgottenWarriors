import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q7 = {'매우 그렇다': {'해적': 1.0, '마법사': 0.8, '궁수': 0.6, '전사': 0.4, '도적': 0.2}, '그렇다': {'마법사': 1.0, '궁수': 0.8, '해적': 0.6, '도적': 0.4, '전사': 0.2}, '보통이다': {'궁수': 1.0, '전사': 0.8, '마법사': 0.6, '도적': 0.4, '해적': 0.2}, '그렇지 않다': {'전사': 1.0, '도적': 0.8, '해적': 0.6, '마법사': 0.4, '궁수': 0.2}, '전혀 그렇지 않다': {'도적': 1.0, '전사': 0.8, '마법사': 0.6, '해적': 0.4, '궁수': 0.2}}

def show():
    st.subheader("7. 남들이 하지 않는 특별한 경험을 하고 싶다")
    st.write("다른 사람들과는 다른 특별한 경험을 하는 걸 좋아한다")
    st.write("희귀하거나 독특한 경험에 끌리는 편이다")
    selected = st.radio("선택하세요:", answer_options, key="q7")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q7.get(selected))
        st.session_state.question_number = 8
        st.rerun()
