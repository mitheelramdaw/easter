import streamlit as st
import altair as alt
import pandas as pd

# --- Title and Balloons ---
st.title("He has Risen! ✝️ 🌅 Happy Easter 🐰🥚")
st.markdown("As we celebrate Easter, let's remember the resurrection and the joy of new life! 🌸")
st.balloons()

# --- Resurrection Cross ---
st.subheader("✝️ Resurrection Cross ✝️")

# Thickness of the bars
thickness = 0.16

# Vertical bar (centered)
vertical_bar = pd.DataFrame({
    'x': [-thickness/2],
    'y': [-1],
    'x2': [thickness/2],
    'y2': [1]
})

# Horizontal bar (centered around 0.6)
horizontal_center = 0.4

horizontal_bar = pd.DataFrame({
    'x': [-0.7],
    'y': [horizontal_center - (thickness/2)],
    'x2': [0.7],
    'y2': [horizontal_center + (thickness/1.2)]
})

# Draw the vertical bar
vbar = alt.Chart(vertical_bar).mark_rect(
    color='purple'
).encode(
    x='x:Q',
    x2='x2:Q',
    y='y:Q',
    y2='y2:Q'
)

# Draw the horizontal bar
hbar = alt.Chart(horizontal_bar).mark_rect(
    color='purple'
).encode(
    x='x:Q',
    x2='x2:Q',
    y='y:Q',
    y2='y2:Q'
)

# Combine into a cross
cross = (vbar + hbar).properties(
    width=400,
    height=600,
    title="The Cross: Symbol of Resurrection ✝️"
)

# Show the cross
st.altair_chart(cross, use_container_width=True)

# --- Closing Easter Message ---
st.success("Thanks for visiting! May your Easter be filled with resurrection joy, blessings, and lots of chocolate! 🍫🐰🥚")
