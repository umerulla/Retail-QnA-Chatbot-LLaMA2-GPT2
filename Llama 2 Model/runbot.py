import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "./llama2-final"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to("cuda" if torch.cuda.is_available() else "cpu")

def ask_bot(question, max_new_tokens=100):
    prompt = f"[INST] {question.strip()} [/INST]"
    inputs = tokenizer(prompt, return_tensors="pt", return_token_type_ids=False).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.05
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded.replace(prompt, "").strip()

if __name__ == "__main__":
    for _ in range(10):
        question = input("🧑 You: ")
        if question.lower() in ["exit", "quit"]:
            print("👋 Exiting.")
            break
        print("🤖 Bot:", ask_bot(question), "\n")
