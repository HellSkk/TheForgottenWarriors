import streamlit as st
from scoring import update_scores

answer_options = ["매우 그렇다","그렇다","보통이다","그렇지 않다","전혀 그렇지 않다"]
base_points = {"매우 그렇다":5,"그렇다":4,"보통이다":3,"그렇지 않다":2,"전혀 그렇지 않다":1}

WEIGHTS_Q3 = {'매우 그렇다': {'해적': 1.0, '전사': 0.8, '도적': 0.6, '궁수': 0.4, '마법사': 0.2}, '그렇다': {'전사': 1.0, '해적': 0.8, '궁수': 0.6, '도적': 0.4, '마법사': 0.2}, '보통이다': {'궁수': 1.0, '도적': 0.8, '전사': 0.6, '해적': 0.4, '마법사': 0.2}, '그렇지 않다': {'도적': 1.0, '궁수': 0.8, '마법사': 0.6, '전사': 0.4, '해적': 0.2}, '전혀 그렇지 않다': {'마법사': 1.0, '궁수': 0.8, '도적': 0.6, '전사': 0.4, '해적': 0.2}}

def show():
    st.subheader("3. 모르는 상대와 경쟁할 때 도파민이 터진다")
    st.write("경쟁 상황이 되면 평소보다 더 몰입하게 된다")
    st.write("경쟁이 시작되면 심장이 두근거리면서 에너지가 솟는다")
    selected = st.radio("선택하세요:", answer_options, key="q3")
    if st.button("다음"):
        user_points = base_points.get(selected, 0)
        update_scores(user_points, WEIGHTS_Q3.get(selected))
        st.session_state.question_number = 4
        st.rerun()
