from transformers import pipeline
import gradio as gr


# Load Hugging Face sentiment analysis model
sentiment_pipeline = pipeline(
    "sentiment-analysis"
)


# Sentiment analysis function
def analyze_sentiment(text):

    if not text or not text.strip():
        return "Please enter some text."

    result = sentiment_pipeline(text)[0]

    label = result["label"]
    score = result["score"]

    return (
        f"Sentiment: {label}\n"
        f"Confidence: {score:.2%}"
    )


# Create Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,

    inputs=gr.Textbox(
        lines=5,
        label="Enter Text",
        placeholder="Write your text here..."
    ),

    outputs=gr.Textbox(
        label="AI Prediction"
    ),

    title="SentimentAI — Hugging Face NLP Analyzer",

    description=(
        "An interactive sentiment analysis application "
        "using a pre-trained Hugging Face model."
    ),

    examples=[
        ["I love learning artificial intelligence!"],
        ["This product is fantastic."],
        ["The service was disappointing."],
        ["The movie was average."]
    ]
)


# Launch application
if __name__ == "__main__":
    demo.launch()