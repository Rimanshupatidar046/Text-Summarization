import heapq
import re
from collections import Counter

def summarize_text(text, max_len=3):
    try:
        # -------- EMPTY CHECK --------
        if not text or not text.strip():
            return "No text provided."

        # -------- CLEAN TEXT --------
        text = re.sub(r'\s+', ' ', text)

        # -------- SPLIT SENTENCES --------
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        # -------- EDGE CASE: VERY SMALL TEXT --------
        if len(sentences) <= 1:
            return text

        # -------- WORD FREQUENCY --------
        words = re.findall(r'\w+', text.lower())
        freq = Counter(words)

        # -------- SENTENCE SCORING --------
        scores = {}
        for sentence in sentences:
            sentence_words = re.findall(r'\w+', sentence.lower())

            # skip too short sentences
            if len(sentence_words) < 3:
                continue

            for word in sentence_words:
                scores[sentence] = scores.get(sentence, 0) + freq[word]

        # अगर scoring fail हो जाए
        if not scores:
            return '. '.join(sentences[:max_len])

        # -------- SAFE max_len --------
        max_len = max(1, min(max_len, len(sentences) - 1))

        # -------- TOP SENTENCES --------
        best = heapq.nlargest(max_len, scores, key=scores.get)

        # -------- MAINTAIN ORIGINAL ORDER --------
        summary = '. '.join([s for s in sentences if s in best])

        return summary

    except Exception as e:
        return f"Error: {str(e)}"
