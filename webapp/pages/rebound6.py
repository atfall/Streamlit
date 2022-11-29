import rebound
import streamlit as st
import pandas as pd
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

sim_in = rebound.Simulation()
sim_out = rebound.Simulation()

mercury = st.checkbox('Mercury')
venus = st.checkbox('Venus')
earth = st.checkbox('Earth', value = True)
mars = st.checkbox('Mars')
jupiter = st.checkbox('Jupiter')
saturn = st.checkbox('Saturn')
uranus = st.checkbox('Uranus')
neptune = st.checkbox('Neptune')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)
sim.add("Sun")

if mercury:
    sim_in.add("Mercury", date = d)
if venus:
    sim_in.add("Venus", date = d)
if earth:
    sim_in.add("Earth", date = d)
if mars:
    sim_in.add("Mars", date = d)
if jupiter:
    sim_out.add("Jupiter", date = d)
if saturn:
    sim_out.add("Saturn", date = d)
if uranus:
    sim_out.add("Uranus", date = d)
if neptune:
    sim_out.add("Neptune", date = d)
 
op1 = rebound.OrbitPlot(sim_in)
op2 = rebound.OrbitPlot(sim_out)
st.pyplot(op1.fig)
st.pyplot(op2.fig)
