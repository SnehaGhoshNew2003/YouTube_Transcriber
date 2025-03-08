# YouTube Video Summarizer

This project extracts YouTube video transcripts and generates AI-powered summaries using Google Gemini AI. It provides key insights from videos in a concise format.

## Features
- **Transcript Extraction:** Fetches YouTube subtitles using `youtube_transcript_api`.
- **AI Summarization:** Generates structured summaries with key points (max 250 words).
- **Video Thumbnail Display:** Automatically shows the video's thumbnail.
- **Streamlit Web App:** User-friendly interface for easy access.

## Technologies Used
- **Streamlit** (Web UI Framework)
- **Google Gemini AI** (AI-driven summarization)
- **YouTube Transcript API** (Extracts subtitles)
- **dotenv & os** (Manages API keys)

## Installation
Install the required dependencies:
```bash
pip install streamlit google-generativeai youtube-transcript-api python-dotenv
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Youtube-Summarizer.git
cd Youtube-Summarizer
```
2. Set up your **Google API Key** in a `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```
3. Run the Streamlit application:
```bash
streamlit run app.py
```
4. Enter a YouTube video URL and click **Get Detailed Notes**.
5. View the AI-generated summary of the video.

## Example Output
- **Input:** YouTube Video Link
- **Output:** AI-generated summary with key points

## Contributing
Feel free to submit issues or pull requests to improve this project.


