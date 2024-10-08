import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.write("""
# Body Mass Index Calculator
"""
)

st.header("Please enter your height and weight below")

height = st.number_input("Height:", min_value=1.00, max_value=110.00, format="%.2f")
weight = st.number_input("Weight:", min_value=1.0, max_value=650.0, format="%.1f")

rb = st.radio(
    "Units",
    ('Imperial (feet/pounds)', 'Metric (meters/kilograms)'))


if (rb == 'Imperial (feet/pounds)'):
    BMI = (weight / np.power(height * 12, 2))*703
    st.write(f"You're BMI (Imperial Units) is **{BMI}**")
else:
    BMI = weight / np.power(height, 2)
    st.write(f"You're BMI (Metric Units) is **{BMI}**")


data = pd.DataFrame({'BMI': ["< 16", "16 - 17", " 17 - 18.5", "18.5 - 25", "25 - 30", "30 -35", "35 - 40", ">40"],
                     'Status' : ["Severe Thinness", "Moderate Thinness", "Mild Thinness", "Normal",  "Overweight",  "Obese Class I", "Obese Class II", "Obese Class III"]
                     })

def get_bmi_category(bmi_value):
    if bmi_value < 16:
        return 0
    elif 16 <= bmi_value < 17:
        return 1
    elif 17 <= bmi_value < 18.5:
        return 2
    elif 18.5 <= bmi_value < 25:
        return 3
    elif 25 <= bmi_value < 30:
        return 4
    elif 30 <= bmi_value < 35:
        return 5
    elif 35 <= bmi_value < 40:
        return 6
    elif bmi_value > 40:
        return 7
    else:
        return -1

# Find the row index that matches the BMI
highlight_idx = get_bmi_category(BMI)

# Highlight the matching row
def highlight_row(row):
    color = 'background-color: green' if row.name == highlight_idx else ''
    return [color] * len(row)

# Display the dataframe with highlighted row
if(highlight_idx != -1):    
    st.dataframe(data.style.apply(highlight_row, axis=1), use_container_width=True, hide_index=True)
else:
    st.dataframe(data, use_container_width=True, hide_index=True)
