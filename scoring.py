import streamlit as st

def ensure_init():
    if "scores" not in st.session_state:
        st.session_state.scores = {"전사":1.0,"도적":1.0,"해적":1.0,"마법사":1.0,"궁수":1.0}
    if "question_number" not in st.session_state:
        st.session_state.question_number = 1

def update_scores(user_points: float, weights: dict | None):
    if not weights or user_points == 0:
        return
    # 감쇠: 점수가 클수록 증가폭 줄이기
    for job, w in weights.items():
        cur = st.session_state.scores[job]
        damp = 1 / (cur ** 0.5)   # √감쇠
        st.session_state.scores[job] = cur + user_points * w * damp
    # 정규화
    total = sum(st.session_state.scores.values())
    k = len(st.session_state.scores)
    if total > 0:
        for job in st.session_state.scores:
            st.session_state.scores[job] = st.session_state.scores[job] / total * k