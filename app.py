import streamlit as st  

# 🎯 Title and Introduction  
st.title("🚀 Growth Mindset Challenge")  
st.subheader("Unlock Your Potential with a Growth Mindset! 🌱")  

st.write(  
    """  
    A **growth mindset** means believing that your abilities and intelligence  
    **can grow** with effort, learning, and persistence. By embracing challenges  
    and learning from mistakes, you can **unlock your full potential!**  
    """  
)  

# 🌟 Why Develop a Growth Mindset?  
st.markdown("## 🌟 Why Develop a Growth Mindset?")  
st.write("✅ **Embrace Challenges** – See obstacles as opportunities to grow.")  
st.write("✅ **Learn from Mistakes** – Treat failures as valuable lessons.")  
st.write("✅ **Persist Through Struggles** – Keep going, even when it’s tough.")  
st.write("✅ **Celebrate Effort** – Success is built on continuous improvement.")  

# 🎯 Interactive Section  
st.markdown("---")  
name = st.text_input("🎯 What's your name?")  

if st.button("🚀 Commit to a Growth Mindset"):  
    if name:  
        st.success(f"👏 Awesome, {name}! Keep learning, growing, and believing in yourself! 💡")  
    else:  
        st.warning("⚠️ Please enter your name to make a commitment!")  

# 🎥 Learning Resource  
st.markdown("---")  
st.markdown("## 📺 Want to Learn More?")  
st.video("https://youtu.be/8W8NQFFbDcU?si=vmi-XJcga4caX_AM")  

st.markdown("🚀 *Start today. Stay curious. Keep growing!* 🌱💪")  
