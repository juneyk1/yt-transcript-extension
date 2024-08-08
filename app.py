from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter
from transformers import pipeline

app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '') # request the url of current video
    video_id = url.split('=')[1] # find the video id
    summary = summarize(return_transcript(video_id)) # call the functions to get transcript and summarize
    return summary, 200

def return_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id) # retrieve the transcript
    transcript = ' '.join([d['text'] for d in transcript_list]) # join the separate texts of listed transcript to one string
    return transcript
    
def summarize(transcript):
    summarizer = pipeline('summarization') # initialize summarization model
    summary = ''
    for i in range(0, (len(transcript)//1000)+1): # break transcript into multiple parts (1k char limit)
        summary_text = summarizer(transcript[i*1000:(i+1)*1000])[0]['summary_text'] # summarize part of transcript (by 1000th chars)
        summary = summary + summary_text + ' ' # add to final summary
    return summary


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
