"""Charge-class pseudo-Anosov ladder in B3 (structure only; no measured value, no fitting).

Thread "Derive the tau lepton's word", part 2 (2026-11-27). Lean:
QOU/Observations/LeptonChargeClassTrace.lean (parity -> even trace; traces of the ladder words).

Enumerates cyclically reduced signed words in sigma_1, sigma_2 up to length MAXLEN, groups them by
(length parity, |trace| of the SL(2,Z) image), and for each group lists the distinct volumes of
closure-union-axis (the mapping torus of the braid on the 3-punctured disk), computed with SnapPy
in high precision (ManifoldHP, ~63 significant digits; printed to 20). Exact traces are integers.

Checks: odd words have even |trace|; the odd class at |tr| = 4 and 6 has a single volume; the
odd class at |tr| = 8 has more than one (so a fourth rung would need a further rule).
"""
import itertools
import sys
import warnings

warnings.filterwarnings("ignore")
import snappy  # noqa: E402

MAXLEN = 9
M = {1: ((1, 1), (0, 1)), -1: ((1, -1), (0, 1)), 2: ((1, 0), (-1, 1)), -2: ((1, 0), (1, 1))}


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def trace(w):
    X = ((1, 0), (0, 1))
    for s in w:
        X = mul(X, M[s])
    return abs(X[0][0] + X[1][1])


def axis_volume(w):
    L = snappy.Link(braid_closure=list(w) + [3, 2, 1, 1, 2, 3])
    return L.exterior().high_precision().volume()


checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


groups = {}
for n in range(1, MAXLEN + 1):
    for w in itertools.product([1, -1, 2, -2], repeat=n):
        if any(w[i] == -w[i + 1] for i in range(n - 1)) or (n > 1 and w[0] == -w[-1]):
            continue
        groups.setdefault((n % 2, trace(w)), []).append(w)

check("odd words have even |trace|", all(t % 2 == 0 for (p, t) in groups if p == 1))

summary = {}
for (p, t), ws in sorted(groups.items()):
    if t < 3 or t > 8:
        continue
    vols = {}
    for w in ws[:400]:
        try:
            v = axis_volume(w)
        except Exception:
            continue
        key = str(v)[:12]
        vols.setdefault(key, (w, v))
    summary[(p, t)] = vols
    cls = "odd (charge)" if p else "even (neutral)"
    for key, (w, v) in vols.items():
        print(f"{cls:15s} |tr|={t}  vol={str(v)[:22]}  e.g. {w}")

check("odd |tr|=4: one volume", len(summary[(1, 4)]) == 1)
check("odd |tr|=6: one volume", len(summary[(1, 6)]) == 1)
check("odd |tr|=8: more than one volume", len(summary[(1, 8)]) > 1)
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
