# Chocolate Retail QnA Chatbot – LLaMA2-7B & GPT-2

This repository contains two domain-specific chatbots for a premium chocolate retail business — built using **Meta's LLaMA2-7B (via QLoRA)** and **GPT-2-Large (via LoRA)**.

The bots are trained on a custom chocolate-retail QnA corpus to handle queries related to:

- Gifting, packaging, freshness, pricing
- Dietary needs, daily consumption
- Bulk orders, international questions
- Casual, funny, emotional tones and more

> **⚠️ Read this before quoting any metric from this repo.**
> An audit of the training artefacts (reported in full in the accompanying research paper, *"Fluency Is Not Fidelity"*) found that:
> - The stored corpus of 1,000 QnA blocks contains only **222 unique pairs** (~4.5× duplication).
> - **94.3% of test questions also appear in the training file** — the evaluation splits are not held out, so no score below is a generalisation estimate.
> - The GPT-2 and LLaMA2 pipelines were evaluated with **different splits, different de-duplication, and different exact-match rules** — their headline scores are **not comparable**.
>
> All numbers are reported exactly as the notebooks printed them, defects and all.

---

## 📁 Repository Structure

```
Retail-QnA-Chatbot-LLaMA2-GPT2/
├── GPT2 Model/              ← GPT-2-Large LoRA baseline
├── Llama 2 Model/           ← LLaMA2-7B QLoRA chatbot (primary model)
├── INSTRUCTIONS.md          ← Instructions to run the chatbot locally
├── README.md                ← You're here!
```

---

## ⚖️ Measured Results (as printed by the notebooks)

| Metric | LLaMA2-7B (QLoRA) | GPT-2-Large (LoRA) |
| --- | --- | --- |
| Unique training samples | 214 (de-duplicated) | 800 (not de-duplicated) |
| Training runtime | 87.8 s (81 steps, 3 epochs) | 485 s (300 steps) |
| Validation loss | 0.2108 | 0.1686 |
| Validation perplexity | 1.23 | 1.18 |
| Mean token accuracy | 93.45% | not recorded |
| Exact match | **37.14%** (test set) | 96.00% (validation set) |

> 🔍 The two exact-match figures were computed on **different splits with different matching rules and different decoding** — the apparent GPT-2 advantage is an artifact of the protocol, not a property of the models. See the paper (Section V.4) for the full analysis, and the standardised evaluation harness that makes them comparable.
>
> 👉 The **`Llama 2 Model`** folder contains the primary, deployed system. In interactive use it answers domain questions accurately and routes out-of-scope input to a safe fallback.

---

## 🧠 Tech Stack

- Transformers, TRL, PEFT, bitsandbytes
- QLoRA (4-bit NF4 + LoRA r=16 on q_proj/v_proj) for LLaMA2-7B
- LoRA (r=8 on c_attn/c_proj) for GPT-2-Large
- Python + Google Colab (A100)
- Dataset: curated synthetic QnA pairs — 222 unique after de-duplication

---

## 📥 Fine-Tuned Model Access

The LLaMA2 model is too large for GitHub.

🔗 [Download LLaMA2 fine-tuned model here](https://drive.google.com/drive/folders/171I3cCbr3BONz7w71wA8_349xP-ACFOJ?usp=drive_link)

Setup instructions are included in `Llama 2 Model/README.md`.

---

## 🙋‍♂️ Maintainer

Umerulla Belavadi – [umerullab@gmail.com]
