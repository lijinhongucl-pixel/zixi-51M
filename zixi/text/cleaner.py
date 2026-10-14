from . import chinese
from . import cleaned_text_to_sequence


def clean_text(text, language='ZH'):
    """文本 → (norm_text, phones, tones, word2ph)。仅中文。"""
    assert language == 'ZH', f"zixi-51M 仅支持中文, 收到: {language}"
    norm_text = chinese.text_normalize(text)
    phones, tones, word2ph = chinese.g2p(norm_text)
    return norm_text, phones, tones, word2ph


def clean_text_bert(text, language='ZH', device=None):
    raise NotImplementedError("zixi-51M 无 BERT")


def text_to_sequence(text, language='ZH'):
    norm_text, phones, tones, _ = clean_text(text, language)
    return cleaned_text_to_sequence(phones, tones, language)


if __name__ == "__main__":
    pass
