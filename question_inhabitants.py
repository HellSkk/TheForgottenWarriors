import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q6 = {'매우 그렇다': {'도적': 1.0, '전사': 0.8, '궁수': 0.6, '마법사': 0.4, '해적': 0.2}, 
              '그렇다': {'궁수': 1.0, '전사': 0.8, '마법사': 0.6, '해적': 0.4, '도적': 0.2}, 
              '보통이다': {'마법사': 1.0, '궁수': 0.8, '전사': 0.6, '도적': 0.4, '해적': 0.2}, 
              '그렇지 그렇다': {'전사': 1.0, '궁수': 0.8, '마법사': 0.6, '도적': 0.4, '해적': 0.2}, 
              '전혀 그렇지 않다': {'해적': 1.0, '도적': 0.8, '전사': 0.6, '마법사': 0.4, '궁수': 0.2}}

def show():
    st.subheader("6. 나는 사람이 많은 곳에 가도 아무렇지 않다")
    st.write("새로운 걸 선택할 때 주변 사람들이 많이 하는 걸 참고한다")
    st.write("많은 사람이 몰리는 곳은 그만한 이유가 있다고 생각한다")
    selected = st.radio("선택하세요:", answer_options, key="q6")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q6.get(selected))
        st.session_state.question_number = 7
        st.rerun()
