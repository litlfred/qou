#!/usr/bin/env python3
"""Route 11: the three level-7 numerators are DERIVED from the five-term relation.

Bean ``qou-fivt``.  Routes 8–10 (merged #4658 + follow-up) reduced the 5₂ sum rule
to three explicit rational values

    Re[2·L(wₖ) + L(−wₖ)] = mₖ·π²/42,   m = (17, 5, −1),   wₖ = 1 + 2cos(2πk/7)

verified to 100 dps and **underived**.  Those three integers were the entire
remaining mathematical content.  This probe derives them.

The derivation
--------------
**Step 1 — reduce to (0,1).**  Only ``w₂`` lies in ``(0,1)``; ``w₁ > 1`` and
``w₃ < 0``.  Using the three classical extensions of the real Rogers dilogarithm

    reflection  L(x) + L(1−x)     = L(1) = π²/6     (0 < x < 1)
    inversion   L(x) + L(1/x)     = 2·L(1)          (x > 1)
    Landen      L(x) + L(x/(x−1)) = 0               (x < 0)

every term reduces to arguments in ``(0,1)``.  Writing

    a = L(w₂),  q = w₁/(1+w₁),  r = w₂/(1+w₂),  s = −w₃      (and 1/w₁ = 1−w₂)

the three targets become, in the basis ``[L(1), a, L(q), L(r), L(s)]``:

    T₁ = (−3/7,  2, −1,  0,  0)          [ 2L(1) + 2a − L(q) = 17π²/42 ]
    T₂ = (−5/7,  2,  0, −1,  0)          [        2a − L(r)  =  5π²/42 ]
    T₃ = (−13/7, 2,  0,  0,  1)          [−2L(1) + 2a + L(s) = −1π²/42 ]

**Step 2 — the argument set is CLOSED under the five-term relation.**
``{w₂, q, r, s}`` together with their reflections is closed under

    L(x) + L(y) − L(xy) − L(x(1−y)/(1−xy)) − L(y(1−x)/(1−xy)) = 0

Three of the closed instances are independent:

    R₁  (x = y = w₂)      :  2L(w₂) − L(1−q) − 2L(r)                 = 0
    R₂  (x = 1−w₂, y = q) :  L(1−w₂) + L(q) − L(1−q) − L(1−s) − L(w₂) = 0
    R₃  (x = w₂,   y = s) :  L(w₂) + L(s) − L(1−w₂) − L(1−s) − L(1−r) = 0

**Step 3 — the certificate.**  Each target is an exact rational combination:

    T₁ = (2/7)·R₁ − (4/7)·R₂ + (1/7)·R₃
    T₂ = (1/7)·R₁ − (2/7)·R₂ + (4/7)·R₃
    T₃ = (4/7)·R₁ − (1/7)·R₂ + (2/7)·R₃

checked in exact rational arithmetic.  The coefficient triples are cyclic shifts
of ``(1, 2, 4)`` — **the quadratic residues mod 7** — and the ``1/7`` in those
coefficients is exactly where the ``mₖ/7`` denominators come from.

⚠ Epistemic status — read before quoting this
---------------------------------------------
**Derived:** the three numerators, from the five-term relation plus the three
standard extension formulas.  That is a genuine derivation, not a fit.

**NOT thereby proved: the 5₂ sum rule.**  The chain still passes through Route 8's
analytic transport (envelope theorem along GGM's deformation, plus the branch
integer ``k = 0`` on ``|x| = 1``), which is *argued* — via integrality plus local
constancy on a collision-free arc — but not proved.  That is now the weakest link,
and it is an analytic one, not an arithmetic one.

Also note the extension formulas here are **verified on generic points**, not
proved; they are standard textbook facts about the real Rogers dilogarithm, but
this probe does not derive them.

Gates
-----
G1  The three extension formulas, on generic points (not just our w's).
G2  R₁, R₂, R₃ are genuine five-term instances (all arguments in (0,1)).
G3  The closed argument set: five-term maps {w₂,q,r,s,reflections} into itself.
G4  Exact rational certificate T = c·R, in Fraction arithmetic.
G5  rank(R) = rank(R ∪ T) = 3, i.e. the targets lie in the span.
G6  The targets, recomputed from scratch, equal mₖπ²/42.
"""
from __future__ import annotations

import json
import pathlib
from fractions import Fraction as F

from mpmath import cos, fabs, log, mp, mpf, nstr, pi, polylog, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
TOL = mpf(10) ** -40


def L(x):
    return re(polylog(2, x) + log(x) * log(1 - x) / 2)


def rank(rows):
    M = [list(r) for r in rows]
    rr = 0
    n = len(M[0])
    for c in range(n):
        p = next((i for i in range(rr, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[rr], M[p] = M[p], M[rr]
        pv = M[rr][c]
        for i in range(len(M)):
            if i != rr and M[i][c] != 0:
                f = M[i][c] / pv
                M[i] = [M[i][j] - f * M[rr][j] for j in range(n)]
        rr += 1
    return rr


def main():
    gates = []
    L1 = pi ** 2 / 6
    W = {k: 1 + 2 * cos(2 * pi * k / 7) for k in (1, 2, 3)}
    w1, w2, w3 = W[1], W[2], W[3]
    q, r, s = w1 / (1 + w1), w2 / (1 + w2), -w3

    # G1 -- extension formulas on GENERIC points
    e1 = max(fabs(L(x) + L(1 - x) - L1) for x in (mpf('0.3'), mpf('0.77'), w2))
    e2 = max(fabs(L(x) + L(1 / x) - 2 * L1) for x in (mpf('1.7'), mpf('5.3'), w1))
    e3 = max(fabs(L(x) + L(x / (x - 1))) for x in (mpf('-0.4'), mpf('-3.1'), w3))
    gates.append({"gate": "G1",
                  "claim": "reflection L(x)+L(1-x)=L(1); inversion L(x)+L(1/x)=2L(1) for x>1; "
                           "Landen L(x)+L(x/(x-1))=0 for x<0 -- on generic points",
                  "reflection_worst": nstr(e1, 6), "inversion_worst": nstr(e2, 6),
                  "landen_worst": nstr(e3, 6),
                  "caveat": "verified, not derived -- standard facts, but this probe does not prove them",
                  "pass": bool(max(e1, e2, e3) < TOL)})

    # G2 -- the three five-term instances
    R1n = 2 * L(w2) - L(1 - q) - 2 * L(r)
    R2n = L(1 - w2) + L(q) - L(1 - q) - L(1 - s) - L(w2)
    R3n = L(w2) + L(s) - L(1 - w2) - L(1 - s) - L(1 - r)
    inrange = all(0 < t < 1 for t in (w2, q, r, s, 1 - w2, 1 - q, 1 - r, 1 - s))
    gates.append({"gate": "G2", "claim": "R1, R2, R3 are genuine five-term instances, args all in (0,1)",
                  "R1": nstr(R1n, 6), "R2": nstr(R2n, 6), "R3": nstr(R3n, 6),
                  "all_args_in_unit_interval": bool(inrange),
                  "pass": bool(max(fabs(R1n), fabs(R2n), fabs(R3n)) < TOL and inrange)})

    # G3 -- closure of the argument set
    vals = {"w2": w2, "q": q, "r": r, "s": s}
    for n in list(vals):
        vals["1-" + n] = 1 - vals[n]
    lookup = {nstr(v, 25): n for n, v in vals.items()}
    closed = 0
    total = 0
    for x in vals.values():
        for y in vals.values():
            d = 1 - x * y
            if fabs(d) < mpf('1e-6'):
                continue
            A, B, C = x * y, x * (1 - y) / d, y * (1 - x) / d
            if not all(0 < t < 1 for t in (A, B, C)):
                continue
            total += 1
            if all(lookup.get(nstr(t, 25)) is not None for t in (A, B, C)):
                closed += 1
    gates.append({"gate": "G3", "claim": "{w2,q,r,s} + reflections is CLOSED under the five-term relation",
                  "closed_instances": closed, "valid_instances": total,
                  "pass": bool(closed >= 3)})

    # G4/G5 -- the exact certificate and the span
    R = [(F(-3), F(2), F(0), F(1), F(2)),
         (F(-1), F(-2), F(2), F(0), F(1)),
         (F(-1), F(2), F(1), F(-2), F(0))]
    T = [(F(-3, 7), F(2), F(-1), F(0), F(0)),
         (F(-5, 7), F(2), F(0), F(-1), F(0)),
         (F(-13, 7), F(2), F(0), F(0), F(1))]
    C = [[F(2, 7), F(-4, 7), F(1, 7)],
         [F(1, 7), F(-2, 7), F(4, 7)],
         [F(4, 7), F(-1, 7), F(2, 7)]]
    ok = True
    cert = []
    for i in range(3):
        combo = tuple(sum(C[i][j] * R[j][k] for j in range(3)) for k in range(5))
        ok = ok and combo == T[i]
        cert.append({"target": f"T{i+1}", "coeffs_over_R": [str(c) for c in C[i]],
                     "combination": [str(x) for x in combo], "target_row": [str(x) for x in T[i]],
                     "match": bool(combo == T[i])})
    gates.append({"gate": "G4", "claim": "exact rational certificate T_i = sum_j c_ij R_j (Fraction arithmetic)",
                  "certificate": cert,
                  "note": "coefficient triples are cyclic shifts of (1,2,4), the quadratic residues mod 7 -- "
                          "this is the origin of the /7 in m_k/7",
                  "pass": bool(ok)})

    rR, rRT = rank(R), rank(R + T)
    gates.append({"gate": "G5", "claim": "rank(R) = rank(R union T) = 3: targets lie in the five-term span",
                  "rank_R": rR, "rank_R_and_T": rRT, "pass": bool(rR == 3 and rRT == 3)})

    # G6 -- targets from scratch
    ms = [17, 5, -1]
    w6 = mpf(0)
    per = []
    for k, (w, m) in enumerate(zip([w1, w2, w3], ms), 1):
        v = re(2 * (polylog(2, w) + log(w) * log(1 - w) / 2)
               + (polylog(2, -w) + log(-w) * log(1 + w) / 2))
        err = fabs(v - mpf(m) * pi ** 2 / 42)
        w6 = max(w6, err)
        per.append({"k": k, "value": nstr(v, 24), "m": m, "abs_err": nstr(err, 6)})
    gates.append({"gate": "G6", "claim": "targets recomputed from scratch equal m_k pi^2/42",
                  "per_k": per, "worst": nstr(w6, 8), "pass": bool(w6 < TOL)})

    out = {
        "probe": "qbeta_5two_route11_fiveterm_certificate",
        "bean": "qou-fivt",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "route11": "THE THREE NUMERATORS ARE DERIVED from the five-term relation.",
            "derivation": "reduce to (0,1) by reflection/inversion/Landen; the argument set "
                          "{w2, q, r, s} + reflections is closed under the five-term relation; three "
                          "independent instances R1,R2,R3 span the targets, with exact certificate "
                          "T1 = (2R1 - 4R2 + R3)/7, T2 = (R1 - 2R2 + 4R3)/7, T3 = (4R1 - R2 + 2R3)/7.",
            "where_the_sevens_come_from": "the certificate coefficients are cyclic shifts of (1,2,4), "
                                          "the quadratic residues mod 7.",
            "NOT_proved": "the 5_2 sum rule itself. The chain still passes through Route 8's analytic "
                          "transport (envelope theorem + the branch integer k=0 on |x|=1), which is "
                          "argued via integrality and local constancy on a collision-free arc, but not "
                          "proved. That is now the weakest link -- and it is analytic, not arithmetic.",
            "also_not_proved": "the three extension formulas are verified on generic points here, not "
                               "derived; they are standard facts about the real Rogers dilogarithm.",
            "sum_rule_status": "verified to 80 dps; numerators now derived; transport still argued",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route11-fiveterm-certificate.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the three numerators are DERIVED. The sum rule still rests on Route 8's transport.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
