from datasets import load_dataset

dataset = load_dataset("mhenrichsen/alpaca_2k_test")

print(dataset)
dataset['train'][10]