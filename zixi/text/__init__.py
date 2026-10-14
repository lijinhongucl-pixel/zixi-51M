from .symbols import *


_symbol_to_id = {s: i for i, s in enumerate(symbols)}


def cleaned_text_to_sequence(cleaned_text, tones, language='ZH', symbol_to_id=None):
    """(phones, tones) id 序列。仅中文: 声调偏移恒 0, 不产出语言 id。"""
    assert language in language_tone_start_map, f"zixi-51M 仅支持中文, 收到: {language}"
    symbol_to_id_map = symbol_to_id if symbol_to_id else _symbol_to_id
    phones = [symbol_to_id_map[symbol] for symbol in cleaned_text]
    tone_start = language_tone_start_map[language]
    tones = [i + tone_start for i in tones]
    return phones, tones


def get_bert(norm_text, word2ph, language='ZH', device=None):
    raise NotImplementedError("zixi-51M 无 BERT")
