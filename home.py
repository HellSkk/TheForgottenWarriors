from scoring import ensure_init
ensure_init()
import streamlit as st

# 세션 상태 초기화
if "question_number" not in st.session_state:
    st.session_state.question_number = 1
if "scores" not in st.session_state:
    st.session_state.scores = {
        "전사": 0, "도적": 0, "해적": 0, "마법사": 0, "궁수": 0
    }

# 각 질문 파일 임포트
import question_raid
import question_fishing
import question_pvp
import question_pve
import question_quest
import question_inhabitants
import question_unique
import question_payment
import question_job_preference
import results

st.set_page_config(page_title="게임 직업 추천", page_icon="🎮")
st.title("🧙‍♂️ 당신의 게임 직업은 무엇일까요?")
st.write("간단한 질문에 답하고 당신에게 가장 어울리는 직업을 찾아보세요!")
st.write("---")

if st.session_state.question_number == 1:
    question_raid.show()
elif st.session_state.question_number == 2:
    question_fishing.show()
elif st.session_state.question_number == 3:
    question_pvp.show()
elif st.session_state.question_number == 4:
    question_pve.show()
elif st.session_state.question_number == 5:
    question_quest.show()
elif st.session_state.question_number == 6:
    question_inhabitants.show()
elif st.session_state.question_number == 7:
    question_unique.show()
elif st.session_state.question_number == 8:
    question_payment.show()
elif st.session_state.question_number == 9:
    question_job_preference.show()
elif st.session_state.question_number == 10:
    results.show()