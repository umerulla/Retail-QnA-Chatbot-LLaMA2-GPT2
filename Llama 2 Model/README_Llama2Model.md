# Retail Chatbot for a Chocolate Retail Business (LLaMA2-7B, QLoRA)

Fine-tuned model link: https://drive.google.com/drive/folders/171I3cCbr3BONz7w71wA8_349xP-ACFOJ?usp=sharing

This project features a chatbot built using Meta's LLaMA2-7B model, fine-tuned via QLoRA on a custom QnA corpus tailored for a premium chocolate retail business.

The chatbot can answer questions related to:
- Gifting, packaging, and shipping
- Sugar levels, dietary needs, daily consumption
- Bulk orders, international queries, and more

---
## Technologies & Tools Used

| Category      | Tool / Library                            |
|---------------|-------------------------------------------|
| Base Model    | `meta-llama/Llama-2-7b-hf` (Hugging Face) |
| Fine-Tuning   | `QLoRA` (LoRA r=16 on q_proj/v_proj + 4-bit NF4 quantization) |
| Libraries     | `transformers`, `peft`, `trl`, `bitsandbytes` |
| Platform      | Google Colab (A100 GPU)                   |
| Format        | Prompt-tuned using `[INST]...[/INST]` style |
| Inference     | Gradio ChatInterface + Python CLI (`runbot.py`) |

---

## Dataset Overview

- Stored QnA blocks: 1,000 — **222 unique pairs after de-duplication** (214 train / 78 validation / 70 test)
- Topics: Product info, gifting, packaging, health queries, pricing, bulk orders, and varied tones (funny, clever, confused, formal, casual)

> ⚠️ **Known defect, reported in the accompanying research paper:** 66 of the 70 unique test questions (94.3%) also appear in the training file. The evaluation splits are not held out, so the scores below measure recall of memorised items, not generalisation.

---

## Model Training & Evaluation — LLaMA2-7B

| Metric            | Value                  |
|-------------------|------------------------|
| Mean training loss| 1.0006                 |
| Validation loss   | 0.2108                 |
| Validation perplexity | 1.23               |
| Mean token accuracy | 93.45%               |
| Exact Match       | 37.14% (test set)      |
| Epochs            | 3 (81 optimizer steps, 87.8 s) |
| Splits (unique)   | 214 train / 78 val / 70 test |

The headline story of the project: token-level metrics (perplexity 1.23, token accuracy 93.45%) suggest a near-perfect model, while exact match reaches only 37.14% — *even though most test items were seen in training*. The reconciliation of these two numbers is the subject of the research paper (*"Fluency Is Not Fidelity"*): teacher forcing vs free generation, the brittleness of strict exact match on ornate text, and anti-hallucination decoding constraints that fight verbatim recall. Most exact-match failures are surface-form mismatches, not wrong answers.

Training was done using **QLoRA** with `SFTTrainer` from `trl`. LoRA adapters were merged post-training using `.merge_and_unload()` to make the model self-contained.

---

## 📁 Folder Structure
```plaintext
Llama 2 Model/
├── data-files/
    ├── train.txt                        # Training set   (formatted QnAs)
    ├── test.txt                         # Test set       (formatted QnAs)
    └── validation.txt                   # Validation set (formatted QnAs)
├── Llama_model_for_Retail_Business.py   # Colab notebook for QLoRA fine-tuning
├── README.md                            # Project documentation
├── requirements.txt                     # Full environment for Colab fine-tuning
├── requirements_minimal.txt             # Minimal dependencies for running the bot
├── runbot.py                            # Command-line chatbot for local inference
```

---

## 🛠️ Setup Instructions

#### 1. Install dependencies

pip install -r requirements.txt

#### 2. 📥 Download the Fine-Tuned Model

1. The fine-tuned model is too large for GitHub, so please download it manually from Google Drive: https://drive.google.com/file/d/1jKaaXJ31wHnbciCGqBXg-HZeI-10uZdZ/view?usp=sharing
2. Unzip the file
3. Copy the merged model folder into the root directory and set `model_path` in `runbot.py` to match

#### 3. Run the chatbot
python runbot.py

> Note: `runbot.py` samples (temperature 0.7) while the notebook client decodes greedily with a gibberish screen and fallback validation. The two will not produce identical answers; the paper reports the notebook client's behaviour. Aligning the two is listed as future work.

---

### ✨ Features
- Layered hallucination controls: input screening, constrained decoding, post-generation fallback validation (notebook client)
- Works offline after fine-tuning (no API needed)
- Format-ready for future RAG integration
- Can be served via Gradio, Streamlit, or web chat UI

---

### ⚠️ Limitations & Disclaimer

- The corpus is **synthetic** (AI-generated from a handcrafted seed set, then curated) and only **222 pairs are unique** — small enough that memorisation dominates.
- The evaluation splits **overlap training (94.3% test leakage)**; no reported score is a generalisation estimate. See the paper for the standardised evaluation harness that fixes this.
- The model may inherit **biases or hallucinations** present in the base LLaMA-2 model.
- This chatbot is designed for **informational and demonstration purposes** only. It should not be used for medical, legal, or financial advice.
- International pricing, shipping timelines, and allergen-specific answers may not always be accurate — users should contact the business directly for final confirmation.
- The creators are not responsible for any misinterpretation or misuse of the chatbot's responses in real-world applications.

---

### 📬 Contact
Maintained by Umerulla Belavadi (umerullab@gmail.com)
