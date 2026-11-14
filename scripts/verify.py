"""Verify KPFS solutions.

usage: python verify.py SOLUTIONS.csv [--root DIR]

SOLUTIONS.csv has the columns file, k, value and items (the selected items, 0-based, separated by
spaces); file is the instance path relative to DIR. Each solution must respect the capacity (W <= b) and
the global bound on the violations (V <= k), and its value, the profit minus the forfeit costs, must
equal the value column. The instance format is that of the benchmark: a line "n l b", a line of profits,
a line of weights, and for each forfeit set a line "h d size" followed by a line with its items.
"""
import argparse
import csv
from pathlib import Path


def read(path):
    lines = Path(path).read_text().split("\n")
    n, l, b = map(int, lines[0].split())
    p = list(map(int, lines[1].split()))
    w = list(map(int, lines[2].split()))
    assert len(p) == n and len(w) == n, path
    sets = []
    for s in range(l):
        h, d, size = map(int, lines[3 + 2 * s].split())
        items = list(map(int, lines[4 + 2 * s].split()))
        assert len(items) == size, (path, s)
        sets.append((h, d, items))
    return n, b, p, w, sets


def evaluate(inst, sel):
    """(value, weight, violations) of a selection; repeated or unknown items are an error."""
    n, b, p, w, sets = inst
    S = set(sel)
    assert len(S) == len(sel) and all(0 <= j < n for j in S), "repeated or unknown item"
    V = cost = 0
    for h, d, items in sets:
        v = sum(j in S for j in items) - h
        if v > 0:
            V += v
            cost += v * d
    return sum(p[j] for j in S) - cost, sum(w[j] for j in S), V


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("solutions")
    ap.add_argument("--root", default=".", help="folder the file column is relative to")
    a = ap.parse_args()
    ok = total = 0
    for row in csv.DictReader(open(a.solutions, newline="")):
        total += 1
        inst = read(Path(a.root) / row["file"])
        f, W, V = evaluate(inst, [int(x) for x in row["items"].split()])
        errors = [msg for bad, msg in ((W > inst[1], f"weight {W} > capacity {inst[1]}"),
                                       (V > int(row["k"]), f"violations {V} > k = {row['k']}"),
                                       (f != int(row["value"]), f"value {f} != {row['value']}")) if bad]
        if errors:
            print(row.get("uid", row["file"]), "; ".join(errors))
        else:
            ok += 1
    print(f"{ok} of {total} solutions verified")


if __name__ == "__main__":
    main()
