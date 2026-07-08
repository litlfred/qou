import json
import sys
import mpmath as mp
mp.mp.dps = 50

CHI = {
    "tritium": "computations/chi-tritium-h9-at-q0-50dps.witness.json",
    "helium-3": "computations/chi-helium-3-h9-at-q0-50dps.witness.json",
}

def load(fname):
    with open(fname, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    return {tuple(r["partition"]): {"y": mp.mpf(r["y_lambda"]), "chi": mp.mpf(r["chi_lambda"])} for r in d["by_partition"]}

T = load(CHI["tritium"])
H = load(CHI["helium-3"])
parts = sorted(T.keys(), reverse=True)

rows = []
for p in parts:
    y = T[p]["y"]
    dchi = T[p]["chi"] - H[p]["chi"]
    v = y * dchi
    if v > 0:
        rows.append((p, v))

rows.sort(key=lambda x: x[1], reverse=True)
for p, v in rows:
    print(f"{str(list(p)):<22} v={mp.nstr(v, 6)}")

