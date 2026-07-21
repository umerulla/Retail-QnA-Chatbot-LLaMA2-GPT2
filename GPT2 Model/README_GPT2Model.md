# GPT-2 Chatbot (Baseline Model)

This folder contains a domain-specific QnA chatbot built using the GPT-2-Large model (774M) for a chocolate retail business.
It was fine-tuned using LoRA (r=8 on c_attn/c_proj) with 4-bit quantization on Google Colab.

📉 **Note on the reported score:**
This pipeline recorded a 96.00% exact-match score on its validation set. That number is **not comparable** to the LLaMA2 model's 37.14%, because the two evaluations differ on four axes (documented in the research paper, Section V.4):

- This pipeline did **not de-duplicate** its data — it trained on all 800 raw blocks and was scored on a validation set containing duplicates it had memorised.
- It was scored on the **validation** set; LLaMA2 was scored on the **test** set.
- Its matching rule compares **only the first line** of the generated answer (lenient); LLaMA2's compares the full string (strict).
- It decodes with **default sampling**; LLaMA2 decodes greedily under a repetition penalty and n-gram block.

Each of these differences inflates the GPT-2 score or depresses the LLaMA2 score, so **no conclusion about relative model quality can be drawn** from these numbers.

🚫 **Not Recommended for Production**
Use the GPT-2 model only for learning, testing, or comparison purposes.

✅ **For the primary system:**
Please refer to the LLaMA2-7B version in this same repository — the deployed system with the full safety layer (input screening, constrained decoding, fallback validation).
