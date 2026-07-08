import json
import mpmath as mp
mp.mp.dps = 50

q = mp.mpf("1.1099793132717013149866657930777598687799017684617")

def qbracket(k):
    if k == 0: return mp.mpf(0)
    return (q**k - q**(-k)) / (q - 1/q)

def conjugate(part):
    if not part: return []
    m = part[0]
    return [sum(1 for p in part if p > j) for j in range(m)]

def dim_gl_q(part, N):
    conj = conjugate(part)
    num = mp.mpf(1)
    den = mp.mpf(1)
    for i, row in enumerate(part):
        for j in range(row):
            content = j - i
            arm = row - j - 1
            leg = conj[j] - i - 1
            hook = arm + leg + 1
            num *= qbracket(N + content)
            den *= qbracket(hook)
    return num / den

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

sum_su4_q = mp.mpf(0)
for p in parts:
    y = T[p]["y"]
    dchi = T[p]["chi"] - H[p]["chi"]
    v = y * dchi
    dq = dim_gl_q(list(p), 4)
    sum_su4_q += dq * v

print("Target:", 1.4947119)
print("q-deformed Wigner SU(4) sum:", sum_su4_q)
