import csv
labtoid = {"entailment":1,"contradiction":0,"neutral":2}
with open(name, "r") as f:
    with open(name2, "r") as g:
        reader = csv.reader(f, delimiter="\t")
        labels = [labtoid[row[-1]] for row in reader]
        reader = csv.reader(g, delimiter="\t")
        preds = [[float(x) for x in row].index(max([float(x) for x in row])) for row in reader]
        trulines = zip(labels,preds)
total = 0
right = 0
for pair in trulines:
    if pair[0] == pair[1]:
        right += 1
    total += 1
print(total, right, total/right)
