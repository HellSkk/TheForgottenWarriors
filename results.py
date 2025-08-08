import streamlit as st

def get_job_info(job):
    """직업에 대한 정보와 이미지를 반환하는 함수"""
    info = {
        "전사": {
            "설명": "강력한 체력과 방어력을 바탕으로 적진의 최전선에서 아군을 보호합니다. 동료와 함께 어려운 문제를 해결하며 성취감을 느끼는 당신에게 완벽한 직업입니다.",
            "이미지": "https://cdn.pixabay.com/photo/2024/07/26/16/40/norse-mythology-8923936_960_720.png" 
        },
        "도적": {
            "설명": "빠르고 은밀하게 움직이며 적의 약점을 파고드는 기습 공격에 능합니다. 혼자만의 시간을 소중히 여기고, 호기심이 많아 탐구하는 것을 좋아하는 당신에게 적합합니다.",
            "이미지": "https://velog.velcdn.com/images/shrudals8520/post/7cbc56bb-25b4-42f2-92de-9b79baa9631f/image.png" 
        },
        "해적": {
            "설명": "자유로운 영혼의 소유자로, 모험을 즐기며 보물을 찾아 나섭니다. 경쟁심이 강하고 독특한 것을 좋아하는 당신의 모험심을 채워줄 것입니다.",
            "이미지": "https://cdn.pixabay.com/photo/2024/08/08/07/31/penguin-8953847_960_720.jpg" 
        },
        "마법사": {
            "설명": "강력한 원소 마법으로 멀리서 적을 제압합니다. 지능적인 전략을 선호하며, 새로운 것을 탐구하는 호기심이 많은 당신에게 최고의 선택입니다.",
            "이미지": "https://cdn.pixabay.com/photo/2020/10/08/00/05/man-5636464_1280.png" 
        },
        "궁수": {
            "설명": "민첩하고 정확한 활 솜씨로 멀리서 적을 제압합니다. 친구들과 함께하는 활동을 즐기며, 목표를 향해 집중하는 당신의 능력을 극대화할 수 있습니다.",
            "이미지": "https://cdn.pixabay.com/photo/2019/07/22/03/45/female-4354077_1280.png" 
        }
    }
    return info.get(job)


def show():
    st.subheader("🎉 당신에게 어울리는 직업을 찾고 있습니다...")

    recommended_job = max(st.session_state.scores, key=st.session_state.scores.get)
    info = get_job_info(recommended_job)

    if info:
        st.header(f"당신에게 추천하는 직업은 **{recommended_job}**입니다!")
        st.write(info["설명"])
        st.image(info["이미지"], use_container_width=True)

    if st.button("다시 시작하기"):
        st.session_state.question_number = 1
        st.session_state.scores = {"전사":1.0,"도적":1.0,"해적":1.0,"마법사":1.0,"궁수":1.0}
        st.rerun()