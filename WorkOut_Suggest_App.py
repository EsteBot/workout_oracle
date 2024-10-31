import streamlit as st

exercise_dict = {'BICEP': ['Inside curl', 'Middle curl', 'Outside curl', 'Overhand grip Middle curl'],
                  'TRICEP': ['Standing Overhead extentions', 'Laying down front extentions', 'Body weight dips with bench', 'Cable pulldowns'],
                  'CHEST': ['Chest press', 'Cable fly', 'Knee push-up', 'Cable press'],
                  'BACK': ['Standing row', 'Sitting row', 'Reverse fly', 'Stright leg stand talls'],
                  'SHOULDER': ['Shoulder press', 'Front lateral raise', 'Side lateral raise', 'Shruggs' ],
                  'LAT': ['Assisted pull-ups', 'Cable pull-downs', 'Standing cable pull-downs', 'Laying lat extensions'],
                  'OBLIQUE': ['Cable wood chops', 'Sitting twists', 'Side bends', 'Side planks'],
                  'LEGS': ['Squats', 'Lunges', 'Laying hamstring tuck-ins with ball', 'Calf raises']}

# CSS to center the elements
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom CSS to change button color
button_style = """
    <style>
    .stButton button {
        background-color: #006766;
        color: white;
        border-radius: 10px;
        border: 5px solid: lightblue;
    }
    .stButton button:hover {
        background-color: white;
        color: #006766;
    }
    </style>
    """

# Inject the CSS into the Streamlit app
st.markdown(button_style, unsafe_allow_html=True)

# Centering the headers
st.markdown("<h3 class='center'>An EsteStyle Streamlit Page Where Python Wiz Meets Workout Biz!</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='center'></h1>", unsafe_allow_html=True)

st.markdown("<img src='https://1drv.ms/i/s!ArWyPNkF5S-foZspwsary83MhqEWiA?embed=1&width=307&height=307' width='300' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)

st.markdown("<h3 class='center'> </h3>", unsafe_allow_html=True)

st.markdown("<h4 class='center'>A Workout Combination Suggestion App</h4>", unsafe_allow_html=True)


st.markdown("<h3 class='center'> </h3>", unsafe_allow_html=True)

import streamlit as st

# Initialize session state for index tracking, button press, and checkbox states
if 'cycle_index' not in st.session_state:
    st.session_state.cycle_index = 0
if 'button_pressed' not in st.session_state:
    st.session_state.button_pressed = False
if 'checkbox_states' not in st.session_state:
    st.session_state.checkbox_states = {}


# Function to display exercises with checkboxes
def display_exercises():
    cycle_index = st.session_state.cycle_index
    st.write(f'Cycle: {cycle_index + 1} of 4')

    for key in exercise_dict:
        # Checkbox to track completion
        checkbox_key = f"{key}_{cycle_index}"
        if checkbox_key not in st.session_state.checkbox_states:
            st.session_state.checkbox_states[checkbox_key] = False
        checked = st.checkbox(f"{key}: {exercise_dict[key][cycle_index]}", key=checkbox_key)
        st.write(' ')
        
        # Update session state with checkbox value
        st.session_state.checkbox_states[checkbox_key] = checked

# Button press logic to display exercises
if st.button("Get Today's Epic Workouts", icon="🦾", use_container_width=True):
    st.session_state.button_pressed = True
    st.session_state.cycle_index = (st.session_state.cycle_index + 1) % len(next(iter(exercise_dict.values())))
    #display_exercises()

# Persist the button output
if st.session_state.button_pressed:
   display_exercises()

