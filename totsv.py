import csv
import json
out = "rebreak.tsv"
name = "rebreak2.jsonl"
with open(out, "wt") as g:
    tsv = csv.writer(g, delimiter="\t")
    with open(name, "r") as f:
        index = 0
        labels = ['index', 'promptID', 'pairID', 'sentence1_binary_parse', 'sentence2_binary_parse', 'sentence1_parse', 'sentence2_parse', 'sentence1', 'sentence2', 'label1', 'label2', 'label3', 'label4', 'label5', 'gold_label']
        tsv.writerow(labels)
        for line in f.readlines():
            example = json.loads(line.strip())
            tsv.writerow([index, "a", "b", "d","e","f","g","h",example["sentence1"], example["sentence2"], "a", "b", "c", "d", "e", example["gold_label"]])
            index += 1
