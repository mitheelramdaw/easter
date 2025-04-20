import streamlit as st
import pandas as pd
import altair as alt

# --- Easter-themed header and introduction ---
st.title("He is Risen! 🌅 Happy Easter 🐰🥚")
st.markdown("As we celebrate Easter, let's remember the resurrection and the joy of new life! 🌸")

# --- Built-in Streamlit Celebration (Real Balloons flying!) ---
st.balloons()

# --- Cross Data ---
st.subheader("✝️ Resurrection Cross Chart ✝️")

# Make a proper CROSS shape
cross_data = pd.DataFrame({
    'x': [0, 0, 0, -1, 0, 1],  # 3 points vertically, 2 horizontal arms
    'y': [-1, 0, 1, 0, 0, 0],  # vertical up and down + horizontal left-right
    'part': ['Bottom', 'Center', 'Top', 'Left Arm', 'Center', 'Right Arm']
})

cross_chart = alt.Chart(cross_data).mark_point(
    size=200, 
    shape='cross', 
    color='purple'
).encode(
    x=alt.X('x', axis=None),
    y=alt.Y('y', axis=None),
    tooltip=['part']
).properties(
    width=400,
    height=400,
    title="The Cross: Symbol of Resurrection ✝️"
)

st.altair_chart(cross_chart, use_container_width=True)

# --- Fun Easter Closing Message ---
st.success("Thanks for visiting! May your Easter be filled with resurrection joy, blessings, and lots of chocolate! 🍫🐰🥚")
