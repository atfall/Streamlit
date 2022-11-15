import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'])

if 'Mercury' in options:
    sim.add("Mercury")
if 'Venus' in options:
    sim.add("Venus")
 
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
