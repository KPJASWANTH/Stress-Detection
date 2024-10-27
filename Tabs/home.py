"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("MULTIMODAL STRESS DETECTION")

    # Add image to the home page
    st.image(".\images\image.jpg ")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
          Work-related stress is a significant concern for many people and can have negative effects on
            both physical and mental health.  Detecting stress continuously and unobtrusive stress
              detection may help prevent and reduce stress sby providing personalised feedback and 
              allowing for the development of just-in time adaptive health interventions(JITAI)for 
              stress management.Previous studies on stress detection have some drawbacks like limited 
              interpretability ,small and biased datasets ,single modality focus, lack of real-world
                validation. To address this limitation, An experiment involving 90 participants was 
                conducted in a simulated group office environment. Multimodal stress detection is
                  nothing but detecting stress from multiple sources like mouse movements, keyboard 
                  usage, and heart rate variability to capture different aspects of participants 
                  behaviour and physiology. Using machine learning techniques such as support vector
                    machines, random forests, and gradient boosting models, the data were analyzed to 
                    detect three levels of perceived stress, as well as measures of valence and arousal.
                   The proposed uses Shapley Additive explanations (SHAP) technique to get required
                     features for predicting stress levels.
 
    """, unsafe_allow_html=True)