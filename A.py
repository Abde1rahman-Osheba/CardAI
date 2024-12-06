import streamlit as st
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to play sound
def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        st.error(f"Error playing sound: {e}")

# Streamlit App
st.title("CardAI")
st.write("""Hi I’m the beginner tool CardAI I have been designed by Artificial Intelligence Science and Pharmacy Team
they made me to help you dear physician at the current time,
I’m working on the aortic sounds only, 
but I promise you that in the upcoming generations 
I will cover all the cardiac sounds. """)

# Layout for Two Vertical Sections
col1, col2 = st.columns(2)

with col1:
    # Section 1
    st.subheader("Mr. Ramses")
    if st.button("listen"):
        play_sound("C:\\Users\\bodya\\OneDrive\\Pictures\\Desktop\\Mr_Ramses.wav")
    st.text("""He is a 70-year-old man 
he suffers Shortness
of breath with exertion, 
chest pain, and fainting spells. 
Over the past few months,
the patient has noticed 
increasing shortness of breath,
especially during exertion.
He has also experienced chest pain,
described as a pressure
or squeezing sensation, 
and has fainted
on a couple of occasions. 
He also suffers from Hypertension
and hyperlipidemia since years. 
After knowing the case history 
and then passing to 
the physical examination at 
the step of cardiac auscultation 
we have listened to this record.
""")

with col2:
    # Section 2
    st.subheader("Mrs. Isis")
    if st.button("Listen"):
        play_sound("C:\\Users\\bodya\\OneDrive\\Pictures\\Desktop\\Mrs_Isis.wav")
    st.text("""She is a 52-year-old woman suffers from 
Progressive fatigue, shortness of breath, 
and palpitations. Over the past year,
she has noticed increasing fatigue,
even with minimal exertion.
She has also
experienced shortness of breath, 
especially when lying flat,
and occasional rapid heartbeats. 
She has been diagnosed with Hypertension 
and hyperthyroidism since years.
After knowing the case history
and then passing 
to the physical examination
at the step of cardiac auscultation 
we have listened to this record 
""")

# Reveal Texts Button at the Bottom
st.divider()
if st.button("CardAI Answer"):
    st.write("""Mr. Ramses:After analysis for this sound as you mentioned that this sound came from the aortic side so I recommend that this case suffers from aortic stenosis so if it left without management and life style modifications may lead to
1)	Heart Failure
2)	Angina
3)	Syncope (Fainting)
4)	Sudden Cardiac Death
""")
    st.write("""Mrs. Isis: After analysis for this sound as you mentioned that this sound came from the aortic side so I recommend that this case suffers from aortic regurgitation so if it left without management and life style modifications may lead to 
1)	Heart Failure
2)	Atrial Fibrillation
3)	Endocarditis
4)	Sudden Cardiac Death
""")

    st.write(""" That’s my opinion you are the only decision maker I’m only here to help you 
Was with you CardAI 😊
""")
