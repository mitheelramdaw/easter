import streamlit as st
import altair as alt
import pandas as pd

# --- Title and Balloons ---
st.title("He is Risen! 🌅 Happy Easter 🐰🥚")
st.markdown("As we celebrate Easter, let's remember the resurrection and the joy of new life! 🌸")
st.balloons()

# --- Resurrection Cross ---
st.subheader("✝️ Resurrection Cross Chart ✝️")

# Create vertical bar
vertical_bar = pd.DataFrame({
    'x': [-0.08],
    'y': [-1],
    'x2': [0.08],
    'y2': [1]
})

# Create horizontal bar
horizontal_bar = pd.DataFrame({
    'x': [-0.7],
    'y': [-0.2],
    'x2': [0.7],
    'y2': [0.1]
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

# Combine
cross = (vbar + hbar).properties(
    width=400,
    height=600,
    title="The Cross: Symbol of Resurrection ✝️"
)

# Show the cross
st.altair_chart(cross, use_container_width=True)

# --- Closing Easter Message ---
st.success("Thanks for visiting! May your Easter be filled with resurrection joy, blessings, and lots of chocolate! 🍫🐰🥚")
