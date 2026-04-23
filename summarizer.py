from transformers import pipeline

# load model only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    max_chunk = 800   # safe size

    # split text into chunks
    chunks = []
    for i in range(0, len(text), max_chunk):
        chunks.append(text[i:i+max_chunk])

    summaries = []

    # summarize each chunk
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=120,
            min_length=40,
            do_sample=False
        )[0]['summary_text']
        summaries.append(summary)

    # combine all summaries
    final_summary = " ".join(summaries)

    return final_summary