#!/usr/bin/env python3
"""magnus_sign_growth_analysis.py — growth rates, truncation error, support, and
the representation-stability structure of the Magnus Ω₂ sign sum.

Answers the owner's question (2026-08-30): for high A we cannot exhaust the
partitions — can we bound the number needed for a target precision, characterise
the support, find symmetries / closed forms?

Three reproducible analyses (all cheap; the heavy A=4 run is NOT needed):

  --levels   : |c_λ| = y_λ|tr(ρ_λ Ω₂_λ)| grouped by b(λ) = n − λ₁ (boxes below the
               first row), from the committed A=2/A=3 witnesses (+ A=4 checkpoint).
               MEASURED: the contribution concentrates on LOW b, decaying fast.
  --weightbound : the a-priori bound Σ_λ y_λ·dim_λ (worst case |tr|≈dim), by b-level,
               computed from hook-length formulas alone (no reps). MEASURED: this
               bound does NOT concentrate — its tail plateaus at ~0.5 for every K.
               => the concentration is a property of tr, NOT of the weight y_λ; the
               naive norm bound |tr| ≤ q^L·dim is uselessly loose.
  --reflection : the leading term tr(ρ_{(n-1,1)} Ω₂) across A (dim 3A-1, trivial),
               its sign and inter-A growth ratio.

KEY FINDINGS (see docs/audits/2026-08-30-magnus-sign-growth-and-truncation-bound.md):
  1. |c_λ| concentrates on b=1 (reflection rep), 86 %→92 % for A=3→4, GROWING with A.
  2. The y·dim bound has a flat 50 % tail — so a rigorous error bound CANNOT come
     from the weights; it needs a real bound on |tr(ρ_λ Ω₂_λ)| that decays with b.
  3. OPPOSITE TRENDS: b=1's share of Σy·dim DECREASES with A (4.1 %→0.42 %) while its
     share of Σ|c| INCREASES (86 %→92 %) ⇒ |tr|/dim decays MORE steeply with b as A
     grows — the signature of REPRESENTATION STABILITY (the S_n-rep sequence
     stabilising; cf. Church–Ellenberg–Farb FI-modules).
  4. #partitions at level b=k is p(k), INDEPENDENT of n (k ≤ n/2), so the support
     COUNT for a fixed precision is A-independent; the per-partition DIM at level k
     grows ~n^k, so the cost is poly(A) for fixed precision.
  5. The reflection-rep leading term is negative for all A=2..6 with a converging
     inter-A ratio (→ a closed form poly(A)·μ^A) — the dominant, trivially-computable
     part of the sign.

HONEST STATUS. This gives the SIGN and a few digits cheaply and A-boundedly. A
rigorous 60-dps bound is NOT yet in hand: it needs the tr-decay-with-b theorem
(finding 2), the open problem — tied to the cumulant/cluster expansion (the newly
ingested Procacci–Yuhjtman / Rebenko papers) and representation stability.
scope-(a); NO-FLOAT64 (mpf, dps 140 for the reflection compute, 50 for weights).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from math import factorial, prod

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mpmath as mp  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a hardcoded PROTON
# literal -- the right VALUE by the wrong MECHANISM: it cannot follow the
# anchor, and it is invisible to the retired-pin drain because it never
# matched. Spellings across this family ran 13 to 60 digits for one pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))


def parts(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r


def _hooks(sh):
    rows = list(sh)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    return [(ri - j - 1) + (cols[j] - i - 1) + 1 for i, ri in enumerate(rows) for j in range(ri)]


def dimf(sh):
    return factorial(sum(sh)) // prod(_hooks(sh))


def analyze_levels():
    mp.mp.dps = 60

    def load(path):
        p = os.path.join(_HERE, path)
        if not os.path.exists(p):
            return None
        if path.endswith("witness.json"):
            return json.load(open(p))["results"]["per_partition"]
        return [json.loads(l) for l in open(p) if l.strip()]

    for path, n, label in [
        ("deuteron-magnus-omega2-sign.witness.json", 6, "A=2"),
        ("triton-magnus-omega2-sign.witness.json", 9, "A=3"),
        ("he4-magnus-omega2-sign.checkpoint.jsonl", 12, "A=4(partial)"),
    ]:
        rows = load(path)
        if not rows:
            continue
        byb = defaultdict(lambda: mp.mpf(0))
        tot = mp.mpf(0)
        for r in rows:
            b = n - r["lambda"][0]
            c = abs(mp.mpf(r["y_lambda"]) * mp.mpf(r["tr_rho_Omega2"]))
            byb[b] += c
            tot += c
        print(f"\n{label} (n={n}) — |c_λ| by b=n-λ₁:")
        prev = None
        for b in sorted(byb):
            ratio = (byb[b] / prev) if prev and prev > 0 else float("nan")
            print(f"  b={b:>2}  Σ|c|={mp.nstr(byb[b],5):>13} {mp.nstr(byb[b]/tot*100,4):>7}%"
                  f"   ratio={mp.nstr(mp.mpf(ratio),4)}")
            prev = byb[b]


def analyze_weightbound():
    mp.mp.dps = 50
    Q0 = Q_MP
    def qint(k):
        return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)

    def ylam(sh):
        n = sum(sh)
        dq = prod(qint(h) for h in _hooks(sh))
        nf = prod(qint(k) for k in range(1, n + 1))
        return (dq * dq) / nf

    print("\nWEIGHT BOUND Σ_λ y_λ·dim_λ by b-level (worst case |tr|≈dim; hook formulas only):")
    print(f"  {'A':>2} {'b=1 %':>8} {'tail b>1':>9} {'tail b>2':>9} {'tail b>3':>9} {'tail b>5':>9}")
    for A in (3, 4, 5, 6, 7, 8):
        n = 3 * A
        byb = defaultdict(lambda: mp.mpf(0))
        tot = mp.mpf(0)
        for sh in parts(n):
            v = ylam(sh) * dimf(sh)
            byb[n - sh[0]] += v
            tot += v

        def tail(K):
            return sum(byb[b] for b in byb if b > K) / tot
        print(f"  {A:>2} {mp.nstr(byb[1]/tot*100,4):>7}% {mp.nstr(tail(1),4):>9} "
              f"{mp.nstr(tail(2),4):>9} {mp.nstr(tail(3),4):>9} {mp.nstr(tail(5),4):>9}")
    print("  => the bound tail PLATEAUS at ~0.5: concentration is a tr property, not a weight one.")


def analyze_reflection(Amax=13):
    import he4_magnus_omega2_sign_sparse_probe as base  # sets dps=140
    from mass_at_3A_proper import atom_braid_word_3A
    print(f"\nREFLECTION REP (n-1,1) leading term (dps={mp.mp.dps}):")
    print(f"  {'A':>2} {'dim':>4} {'L':>3} {'tr(ρΩ₂)':>20} {'ratio A/A-1':>12} {'tr/4^A':>14}")
    prev = None
    for A in range(2, Amax + 1):
        n = 3 * A
        Z, N = A // 2, A - A // 2
        gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
        _row, _dP, _dC, tr_rO, _h, dim, _nnz = base._partition_contribution((n - 1, 1), gens)
        ratio = (tr_rO / prev) if prev else mp.mpf("nan")
        print(f"  {A:>2} {dim:>4} {len(gens):>3} {mp.nstr(tr_rO,12):>20} {mp.nstr(ratio,6):>12} "
              f"{mp.nstr(tr_rO/mp.mpf(4)**A,8):>14}")
        prev = tr_rO
    print("  => NEGATIVE for all A (the sign's leading term). But the growth base is NOT")
    print("     numerically pinned: tr/4^A peaks near A=9-10 then falls, and the ratio drifts")
    print("     below 4 (3.85 at A=13). The 'base 4' reading was a transient (RETRACTED); a")
    print("     closed form needs DERIVATION, not fitting. See the closedform-stability audit.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", action="store_true")
    ap.add_argument("--weightbound", action="store_true")
    ap.add_argument("--reflection", action="store_true")
    args = ap.parse_args()
    did = False
    if args.levels:
        analyze_levels()
        did = True
    if args.weightbound:
        analyze_weightbound()
        did = True
    if args.reflection:
        analyze_reflection()
        did = True
    if not did:
        analyze_levels()
        analyze_weightbound()
        analyze_reflection()


if __name__ == "__main__":
    main()
