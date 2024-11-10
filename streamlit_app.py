from asyncio import sleep
from backend.classes import Check
from frontend.components.allert_components import allert_components
import streamlit as st

st.write("hello")
status=Check()
value=status.kalimera()
if value:
    st.write("allaksa")

sleep(3)
value=status.kalinixta()
if not value:
    modal=allert_components()
    modal.hello_world()