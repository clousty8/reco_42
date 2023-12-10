import streamlit as st
import speech_recognition as sr
import pyaudio
import webrtcvad

def main():
    st.title("Speech-to-Text with Voice Activity Detection")

    # TODO: Ajoute le code ici pour la reconnaissance vocale et la détection d'activité vocale

if __name__ == "__main__":
    main()

recognizer = sr.Recognizer()

# Utilise un microphone pour capturer l'audio
with sr.Microphone() as source:
    st.write("Parle maintenant...")
    audio_data = recognizer.listen(source)

text = recognizer.recognize_google(audio_data, language='fr-FR')
st.write(f"Texte reconnu : {text}")


vad = webrtcvad.Vad()
vad.set_mode(3)  # Configurer le mode VAD (valeurs : 0-3)

# Écoute l'audio en petits morceaux pour détecter l'activité vocale
frames = ...  # Remplace cette variable par les frames audio capturées
is_speech = vad.is_speech(frames, sample_rate=16000)  # Sample rate typique pour la parole

if is_speech:
    st.write("Activité vocale détectée !")
else:
    st.write("Aucune activité vocale détectée.")

