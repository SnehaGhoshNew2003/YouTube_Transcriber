import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from googletrans import Translator
prompt = """You are a Youtube video summarizer. You will be taking the transcript text and summarizing the video and providing the important summary in points within 250 words.The transcript text will be appending here and please provide the summary of the text given here:"""
def extract_transcript_details(youtube_video_url,max_length=1500):
    try:
        video_id = youtube_video_url.split('=')[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " "+i["text"]
        if len(transcript) > max_length:
            transcript = transcript[:max_length] + "..."
        return transcript
    except NoTranscriptFound:
        return "No transcript available for this video."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except Exception as e:
        return str(e) 
def translate_text(text,dest_lang="en"):
    translator = Translator()
    translation = translator.translate(text,dest = dest_lang)
    return translation.text
def generate_gemini_content(transcript_text,prompt):
    llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
    model = ChatHuggingFace(llm=llm)
    result = model.invoke(prompt+transcript_text)
    return result.content
st.title("Youtube Transcript to detailed Notes Converter")
youtube_link = st.text_input("Enter your Video link:")
selected_language = st.selectbox("Select transcript language:", ["en", "hi", "es", "fr", "de", "auto"], index=0)
if youtube_link:
    video_id = youtube_link.split('=')[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)
    if "No transcript" not in transcript_text and "Transcripts are disabled" not in transcript_text:
        if selected_language!="en":
            transcript_text = translate_text(transcript_text,dest_lang ="en")

        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
    else:
        st.error(transcript_text)

