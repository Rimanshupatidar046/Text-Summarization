from transformers import pipeline

# ✅ model only load once
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text, max_len=100):
    
    # ✅ SAFETY: text limit (VERY IMPORTANT)
    if len(text) > 1000:
        text = text[:1000]

    try:
        result = summarizer(
            text,
            max_length=max_len,
            min_length=30,
            do_sample=False
        )
        return result[0]['summary_text']

    except Exception as e:
        return f"Error: {str(e)}"

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
