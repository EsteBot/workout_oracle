import streamlit as st

excersize_dict = {'BICEP': ['Inside curl', 'Middle curl', 'Outside curl', 'Overhand grip Middle curl'],
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

# Centering the headers
st.markdown("<h3 class='center'>An EsteStyle Streamlit Page Where Python Wiz Meets Workout Biz!</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='center'></h1>", unsafe_allow_html=True)

st.markdown("<img src='https://1drv.ms/i/s!ArWyPNkF5S-foZspwsary83MhqEWiA?embed=1&width=307&height=307' width='300' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)

st.markdown("<h3 class='center'> </h3>", unsafe_allow_html=True)

st.markdown("<h4 class='center'>A Workout Combination Suggestion App</h4>", unsafe_allow_html=True)


st.markdown("<h3 class='center'> </h3>", unsafe_allow_html=True)

# Initialize session state for index tracking
if 'cycle_index' not in st.session_state:
    st.session_state.cycle_index = 0

# Function to cycle through values of each key
def cycle_values():
    cycle_index = st.session_state.cycle_index
    st.write(f'Cycle: {[cycle_index + 1]} of 4')
    for key in excersize_dict:
        # Display the current item based on cycle_index
        st.write(f"{key}:   {excersize_dict[key][cycle_index]}")
    
    # Update the index, cycling back to 0 if at the end of the lists
    st.session_state.cycle_index = (cycle_index + 1) % len(next(iter(excersize_dict.values())))

if st.button("Get Today's Epic Workouts", icon="🦾", use_container_width=True):
    
        cycle_values()

