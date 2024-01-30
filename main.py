import streamlit as st
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with (col2):
    st.title("alvinah Singano")
    content = """
    (A highly energetic and hardworking graduate from University of Zimbabwe 
    (UZ) with (BSc)Honors Degree in Computer Science with knowledge in Information
    and Technology, Networking, Software and Web designing. Also, 
    I obtained a networking HUAWEI certificate in Datacom (HCIA)
    """

    st.info(content)

