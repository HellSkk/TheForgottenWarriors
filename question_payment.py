import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q8 = {'매우 그렇다': {'해적': 1.0, '전사': 0.8, '마법사': 0.6, '도적': 0.4, '궁수': 0.2}, '그렇다': {'전사': 1.0, '마법사': 0.8, '해적': 0.6, '궁수': 0.4, '도적': 0.2}, '보통이다': {'마법사': 1.0, '도적': 0.8, '전사': 0.6, '해적': 0.4, '궁수': 0.2}, '그렇지 않다': {'도적': 1.0, '궁수': 0.8, '마법사': 0.6, '전사': 0.4, '해적': 0.2}, '전혀 그렇지 않다': {'궁수': 1.0, '도적': 0.8, '마법사': 0.6, '전사': 0.4, '해적': 0.2}}

def show():
    st.subheader("8. 나는 내가 좋아하는 일에 돈을 아끼지 않는다")
    st.write("마음에 드는 것이라면 가격이 비싸도 사는 편이다")
    st.write("마음에 꼭 드는 건 나중에 후회할까 봐 바로 구매한다")
    selected = st.radio("선택하세요:", answer_options, key="q8")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q8.get(selected))
        st.session_state.question_number = 9
        st.rerun()
