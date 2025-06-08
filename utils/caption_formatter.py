from deep_translator import GoogleTranslator

def instagram_format(caption: str) -> str:
    """Add line breaks and emojis for Instagram-like format."""
    return f"📸 {caption}\n\n#CapturedMoments #AIgenerated #ImageCaption"

def generate_hashtags(caption: str) -> str:
    keywords = [word for word in caption.split() if len(word) > 4]
    hashtags = " ".join([f"#{word.lower()}" for word in keywords[:5]])
    return hashtags

def translate_caption(caption: str, lang: str = "hi") -> str:
    return GoogleTranslator(source='auto', target=lang).translate(caption)
