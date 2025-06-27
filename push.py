from datasets import load_dataset
dataset = load_dataset("audio/scp-frogs")
dataset.push_to_hub("bioamla/scp-frogs")