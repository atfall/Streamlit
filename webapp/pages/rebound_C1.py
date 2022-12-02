import rebound
import streamlit as st
import pandas as pd
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.tools as tls


d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)


@st.cache(allow_output_mutation=True)
def init_sim():
	sim = rebound.Simulation()
	sim.add("Sun", date = d)
	sim.add("Mercury", hash = "Mercury", date = d)
	sim.add("Venus", hash = "Venus", date = d)
	sim.add("Earth", hash = "Earth", date = d)
	sim.add("Mars", hash = "Mars", date = d)
	sim.add("Jupiter", hash = "Jupiter", date = d)
	sim.add("Saturn", hash = "Saturn", date = d)
	sim.add("Uranus", hash = "Uranus", date = d)
	sim.add("Neptune", hash = "Neptune", date = d)
	sim.add("Ceres", hash = "Ceres", date = d)
	sim.add("Orcus", hash = "Orcus", date = d)
	sim.add("Pluto", hash = "Pluto", date = d)
	sim.add("Haumea", hash = "Haumea", date = d)
	sim.add("Quaoar", hash = "Quaoar", date = d)
	sim.add("Makemake", hash = "Makemake", date = d)
	sim.add("Gonggong", hash = "Gonggong", date = d)
	sim.add("Eris", hash = "Eris", date = d)
	sim.add("Sedna", hash = "Sedna", date = d)
	sim.move_to_com()
	return sim


sim = init_sim()

in_body_type = []
in_colour = []
out_colour = []
out_body_type = []
inner_bodies = []
outer_bodies = []

#checkboxes
st.header("Planets")
mercury = st.checkbox('Mercury', value = True)
venus = st.checkbox('Venus')
earth = st.checkbox('Earth', value = True)
mars = st.checkbox('Mars')
jupiter = st.checkbox('Jupiter', value = True)
saturn = st.checkbox('Saturn')
uranus = st.checkbox('Uranus')
neptune = st.checkbox('Neptune')

st.header("Dwarf Planets")
col1, col2, col3 = st.columns(3)

with col1:
    ceres = st.checkbox('Ceres', value = True)
    orcus = st.checkbox('Orcus', value = True)
    pluto = st.checkbox('Pluto', value = True)
                    
with col2:
    haumea = st.checkbox('Haumea', value = True)
    quaoar = st.checkbox('Quaoar', value = True)
    makemake = st.checkbox('Makemake', value = True)

with col3:
    gonggong = st.checkbox('Gonggong', value = True)
    eris = st.checkbox('Eris', value = True)
    sedna = st.checkbox('Sedna')

#add checked bodies to plot
if mercury:
    inner_bodies.append("Mercury")
    in_body_type.append("Planet")
    in_colour.append("Red")
if venus:
    inner_bodies.append("Venus")
    in_body_type.append("Planet")
    in_colour.append("Black")
if earth:
    inner_bodies.append("Earth")
    in_body_type.append("Planet")
    in_colour.append("Black")
if mars:
    inner_bodies.append("Mars")
    in_body_type.append("Planet")
    in_colour.append("Black")
    
if jupiter:
    outer_bodies.append("Jupiter")
    out_body_type.append("Planet")
    out_colour.append("Black")
if saturn:
    outer_bodies.append("Saturn")
    out_body_type.append("Planet")
    out_colour.append("Black")
if uranus:
    outer_bodies.append("Uranus")
    out_body_type.append("Planet")
    out_colour.append("Black")
if neptune:
    outer_bodies.append("Neptune")
    out_body_type.append("Planet")
    out_colour.append("Black")

if ceres:
    inner_bodies.append("Ceres")
    in_body_type.append("Dwarf")
    in_colour.append("Gray")    

if orcus:
    outer_bodies.append("Orcus")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if pluto:
    outer_bodies.append("Pluto")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if haumea:
    outer_bodies.append("Haumea")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if quaoar:
    outer_bodies.append("Quaoar")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if makemake:
    outer_bodies.append("Makemake")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if gonggong:
    outer_bodies.append("Gonggong")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if eris:
    outer_bodies.append("Eris")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if sedna:
    outer_bodies.append("Sedna")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
    
#create orbit plots
op1 = rebound.OrbitPlot(sim, particles = inner_bodies) 
op2 = rebound.OrbitPlot(sim,  particles = outer_bodies)

#integrate/stepping
def step1():
    sim.steps(5)
    op1.update()
    op2.update()

def step2():
    sim.steps(100)
    op1.update()
    op2.update()

def step3():
    sim.steps(500)
    op1.update()
    op2.update()

#stepping buttons
st.header('Time Step')
col_1, col_2, col_3 = st.columns(3)

with col_1:
    step_btn_1 = st.button('step1')

with col_2:	
    step_btn_2 = st.button('step2')

with col_3:	
    step_btn_3 = st.button('step3')	

if step_btn_1:
	step1()

if step_btn_2:
	step2()

if step_btn_3:
	step3()

#plotting
op1.particles.set_color(in_colour)
for i in range(len(in_body_type)):
    if in_body_type[i] == "Dwarf":
        op1.orbits[i].set_linestyle("--")

op2.particles.set_color(out_colour)
for i in range(len(out_body_type)):
    if out_body_type[i] == "Dwarf":
      op2.orbits[i].set_linestyle("--")
	
#Display plots
col_in, col_out = st.columns(2)

with col_in:
    st.header("Inner Solar System")
    st.pyplot(op1.fig)

with col_out:
    st.header("Outer Solar System")
    st.pyplot(op2.fig)

#Experimental animate
animate = st.checkbox('Animate: !Experimental!')

if animate:
    step1()

if animate:
    st.experimental_rerun()
