# zixi-51M

A Chinese-exclusive TTS voice model by Zixi Li. VITS2 lineage (forked from MeloTTS), 51.43M parameters, **Chinese-only, no BERT**.

Three selling points:

- **Small** — 51M params is light enough for local inference, CPU included. No cloud, no API key, no GPU bill
- **Chinese-exclusive** — the whole stack serves one language: 77 symbols, 6 tones, zero language-routing overhead, nothing multi-lingual left in the way
- **One real person's voice** — not a synthetic stock voice, not a multi-speaker average. This is a single real human's voice, so the output keeps one person's timbre, rhythm and breath — that's what makes it hyper-realistic

Differences from upstream MeloTTS:

- **BERT fully removed** — the text encoder carries only phone + tone embeddings, no dangling compatibility shims
- **Chinese-only** — no language embedding, no language selection; symbol table 77 (63 Chinese phones + punctuation + pad), tone table 6
- **Embedding transplant warm start** — phone/tone/speaker embeddings inherited row-by-row from the MeloTTS-Chinese base by symbol name, no random init
- Single speaker `zixi`; G has 51.43M params; D/DUR trained from scratch

## Sample

[assets/final_showcase.wav](assets/final_showcase.wav) — one take, default inference parameters (`sdp_ratio=0.2, noise_scale=0.6, noise_scale_w=0.8`), text from Zixi Li's own fiction.

<audio controls src="assets/final_showcase.wav"></audio>

## Install

```bash
uv venv .venv --python 3.11
uv pip install -e .
```

(The monotonic_align MAS op JIT-compiles via numba — needs a numba-supported Python ≥3.10; 3.14 not yet.)

## Weights

Released on Hugging Face as [`NoesisLab/zixi-51m`](https://huggingface.co/NoesisLab/zixi-51m), **weights only; training data is not part of this release**:

```
zixi-51m/
├── config.json          # model hyperparams
└── pytorch_model.bin    # final generator weights (51.43M params, 206MB)
```

## Quick inference

```python
# pip install this package (uv pip install -e . or git+https), then:
from huggingface_hub import snapshot_download
from zixi.api import TTS

ckpt_dir = snapshot_download("NoesisLab/zixi-51m")   # downloads the two files above
model = TTS(language='ZH',
            config_path=f'{ckpt_dir}/config.json',
            ckpt_path=f'{ckpt_dir}/pytorch_model.bin')
model.tts_to_file('你好，世界。', model.hps.data.spk2id['zixi'], 'hello.wav')
# → hello.wav, 44.1kHz Int16 mono
```

## Fine-tuning

`zixi/train.py` and `zixi/preprocess_text.py` are the full training stack; the expected data layout is shown in [`zixi/data/example/metadata.list`](zixi/data/example/metadata.list) (`wav_path|speaker|ZH|text`, 44.1kHz mono wav). Point the config at your own speaker folder to fine-tune your own voice.

## Acknowledgements

Based on [MeloTTS](https://github.com/myshell-ai/MeloTTS) (MIT, MyShell.ai), by Wenliang Zhao, Xumin Yu and Zengyi Qin. Base weights from `myshell-ai/MeloTTS-Chinese`. Upstream in turn builds on coqui-ai TTS, VITS, VITS2 and Bert-VITS2.
