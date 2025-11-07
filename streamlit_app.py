import random
import streamlit as st

st.title("🧮 덧셈/뺄셈 연습 (3문제)")

def new_problem():
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    op = random.choice(["+", "-"])
    if op == "-" and a < b:
        a, b = b, a
    st.session_state['current'] = {"a": a, "b": b, "op": op, "answer": a + b if op == "+" else a - b}

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.current = None
    st.session_state.show_feedback = False
    st.session_state.feedback_msg = ""
    new_problem()

if st.session_state.q_index < 3:
    prob = st.session_state.current
    st.write(f"문제 {st.session_state.q_index + 1} / 3")
    st.markdown(f"### {prob['a']} {prob['op']} {prob['b']} = ?")

    with st.form("answer_form"):
        user_ans = st.number_input("정답을 입력하세요", value=0, step=1, format="%d", key=f"ans_{st.session_state.q_index}")
        submit = st.form_submit_button("제출")

    if submit and not st.session_state.show_feedback:
        try:
            user_int = int(user_ans)
        except Exception:
            user_int = user_ans
        correct = user_int == prob['answer']
        if correct:
            st.session_state.score += 1
            st.session_state.feedback_msg = "정답입니다! 🎉"
        else:
            st.session_state.feedback_msg = f"틀렸습니다. 정답은 {prob['answer']} 입니다."
        st.session_state.show_feedback = True

    if st.session_state.show_feedback:
        st.info(st.session_state.feedback_msg)
        if st.button("다음 문제"):
            st.session_state.show_feedback = False
            st.session_state.q_index += 1
            if st.session_state.q_index < 3:
                new_problem()
            st.experimental_rerun()

else:
    st.success(f"연습 완료! 3문제 중 {st.session_state.score}개 맞췄습니다.")
    if st.button("다시 시작"):
        for k in ['q_index', 'score', 'current', 'show_feedback', 'feedback_msg']:
            if k in st.session_state:
                del st.session_state[k]
        st.experimental_rerun()
