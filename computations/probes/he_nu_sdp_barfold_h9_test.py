#!/usr/bin/env python3
"""DECISIVE TEST — bar-fold SDP support at H₉ REFUTES the self-conjugate ν_SDP candidate.

EXPLORATORY — derive-or-refute, no fit. The decisive test flagged by
`he_nu_sdp_selfconjugate_candidate.py` (#2556): does the bar-involution-folded
operator-selection SDP support equal the self-conjugate blocks at H₉ (T, ³He),
as it does for the deuteron at H₆?

If yes → ν_SDP = #{self-conjugate λ⊢3A} gains a real mechanism (and ⁴He=3 becomes a
serious challenge to ρ_F=2). If no → the count match (D=1, T=2, ³He=2) is coincidence.

Pipeline (all reused canonical machinery, validated on the deuteron first):
  • y_λ        ← y_lambda_wenzl_bridge.y_lambda_wenzl_bridge_numeric  (Markov weight)
  • χ^λ(β)     ← hoefsmit_numpy.chi_numpy(λ, atom_canonical_crossings(Z,N), q₀)
  • cost t_λ = y_λ·χ^λ ;  Gram diag = y_λ·dim = tr_M(P_λ) ;  n_target = tr_M(β) = Σt_λ
  • bar-fold:  min t·x  s.t.  Σx=n_target,  x_λ=x_λ' (conjugate fold),  diag(tr_M)·x ≥ 0
    (= encoding 1 of deuteron_real_sdp.py — the §7b symmetry regulariser, NO fit)

RESULT
------
  D  (n=6):  support = {(3,2,1)} (value tr_M(β_D))  → 1 self-conj block  ✓ pipeline OK
  ³He(n=9):  NON-RAIL support = {(5,1,1,1,1)} only (1 of 2 self-conj); the other
             4 support entries are ±10⁶ RAILS (degenerate). |bounded support| = 1.
  T  (n=9):  ALL support entries are ±10⁶ rails — NO bounded support at all.

So |bar-fold support| = (D:1, ³He:1, T:0) ≠ canonical ν_SDP = (1, 2, 2).

VERDICT: REFUTED. The bar-fold regularises ONLY the deuteron; at A≥3 the indefinite-
Gram unboundedness returns (rail-pinned conjugate pairs), so the support does NOT
equal the self-conjugate blocks. The #self-conjugate count match (1,2,2) was
COINCIDENCE — there is no bar-fold-support mechanism producing ν_SDP. A weaker fact
survives: the bounded (non-rail) support is ⊆ self-conjugate blocks (D:{(3,2,1)},
³He:{(5,1⁴)}, T:∅), but it is not all of them. ν_SDP derivation remains OPEN; this
closes the self-conjugate avenue.

Output: he-nu-sdp-barfold-h9-test.witness.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from hoefsmit_numpy import chi_numpy  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

Q0 = 1.1099785955573347
RAIL = 1e5  # |x| above this is a degenerate bound-rail, not a genuine support


def _parts(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for f in range(min(n, mx), 0, -1):
        for r in _parts(n - f, f):
            yield (f,) + r


def _conj(p):
    return tuple(sum(1 for r in p if r > j) for j in range(p[0])) if p else ()


def _hook_dim(lam):
    lp = _conj(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - (j + 1)) + (lp[j] - (i + 1)) + 1
    return math.factorial(sum(lam)) // prod


def barfold(Z, N):
    n = 3 * (Z + N)
    cr = atom_canonical_crossings(Z, N)
    P = list(_parts(n))
    idx = {p: i for i, p in enumerate(P)}
    y = {p: float(y_lambda_wenzl_bridge_numeric(list(p), Q0)) for p in P}
    chi = {p: float(chi_numpy(p, cr, Q0)) for p in P}
    t = np.array([y[p] * chi[p] for p in P])
    frob = np.array([y[p] * _hook_dim(p) for p in P])
    nt = float(t.sum())
    rows, seen = [], set()
    for p in P:
        cp = _conj(p)
        if cp != p and cp in idx and (p, cp) not in seen and (cp, p) not in seen:
            seen.add((p, cp))
            r = np.zeros(len(P)); r[idx[p]] = 1.0; r[idx[cp]] = -1.0
            rows.append(r)
    A_eq = np.array([np.ones(len(P))] + rows)
    b_eq = np.array([nt] + [0.0] * len(rows))
    res = linprog(c=t, A_ub=-np.diag(frob), b_ub=np.zeros(len(P)),
                  A_eq=A_eq, b_eq=b_eq, bounds=[(-1e6, 1e6)] * len(P), method="highs")
    sc = [p for p in P if _conj(p) == p]
    if not res.success:
        return {"n": n, "self_conj": sc, "feasible": False,
                "support": [], "bounded_support": []}
    supp = [(p, float(res.x[i])) for i, p in enumerate(P) if abs(res.x[i]) > 1e-6]
    bounded = [(p, v) for p, v in supp if abs(v) < RAIL]
    return {"n": n, "self_conj": sc, "feasible": True,
            "support": supp, "bounded_support": bounded}


def main() -> int:
    print("=" * 84)
    print("  DECISIVE TEST — bar-fold SDP support at H₉ vs self-conjugate blocks")
    print("  candidate: ν_SDP = #self-conjugate(3A); mechanism: support = self-conj blocks")
    print("=" * 84)
    rows = []
    nu_conf = {"D": 1, "T": 2, "3He": 2}
    for nm, Z, N in [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]:
        r = barfold(Z, N)
        b = r["bounded_support"]
        sc = set(r["self_conj"])
        bset = {p for p, _ in b}
        print(f"\n  {nm} (n={r['n']}):  self-conj = {r['self_conj']}  (ν_canon={nu_conf[nm]})")
        print(f"    full support ({len(r['support'])}): "
              f"{[(p, round(v,3)) for p,v in r['support']]}")
        print(f"    BOUNDED (non-rail) support ({len(b)}): {[(p, round(v,4)) for p,v in b]}")
        print(f"    |bounded| = {len(b)}  vs  ν_canon = {nu_conf[nm]}  "
              f"{'✓' if len(b)==nu_conf[nm] else '✗'}   bounded ⊆ self-conj? {bset<=sc}")
        rows.append({"atom": nm, "Z": Z, "N": N, "n": r["n"],
                     "self_conj": [list(p) for p in r["self_conj"]],
                     "nu_canonical": nu_conf[nm],
                     "bounded_support": [[list(p), v] for p, v in b],
                     "bounded_support_size": len(b),
                     "bounded_subset_self_conj": bool(bset <= sc),
                     "feasible": r["feasible"]})

    sizes = {r["atom"]: r["bounded_support_size"] for r in rows}
    refuted = not all(r["bounded_support_size"] == r["nu_canonical"] for r in rows)
    print("\n" + "=" * 84)
    print(f"  VERDICT: {'REFUTED' if refuted else 'consistent'} — "
          f"|bar-fold bounded support| = {sizes} vs ν = {{'D':1,'T':2,'3He':2}}.")
    if refuted:
        print("  The bar-fold regularises ONLY the deuteron; at A≥3 the indefinite-Gram")
        print("  unboundedness returns (rail-pinned). Support ≠ self-conj blocks, so the")
        print("  #self-conj count match (1,2,2) was COINCIDENCE. Weaker fact survives:")
        print("  bounded support ⊆ self-conjugate. ν_SDP derivation remains OPEN.")
    print("=" * 84)

    witness = {
        "computation": "he-nu-sdp-barfold-h9-test",
        "kind": "exploratory-probe",
        "description": (
            "Decisive test of the self-conjugate ν_SDP candidate: does the bar-fold SDP "
            "support equal the self-conjugate blocks at H₉? REFUTED — |bounded support| "
            "= D:1, ³He:1, T:0 ≠ ν=1,2,2; the bar-fold regularises only the deuteron, "
            "rails at A≥3. The #self-conj match was coincidence. y_λ via Wenzl bridge, "
            "χ^λ via hoefsmit_numpy, no fit."
        ),
        "engine": "numpy+scipy", "q0": Q0,
        "atoms": rows,
        "bounded_support_sizes": sizes,
        "verdict": "REFUTED",
        "weaker_fact": "bounded (non-rail) bar-fold support ⊆ self-conjugate blocks (D,T,³He)",
        "conclusion": ("No bar-fold-support mechanism yields ν_SDP; the self-conjugate "
                       "count avenue is closed. ν_SDP derivation remains open (cf. #2552)."),
        "refs": ["PR #2556 (self-conjugate candidate)",
                 "PR #2552 (ν_SDP not computable)",
                 "computations/deuteron_real_sdp.py (bar-fold = encoding 1)",
                 "computations/y_lambda_wenzl_bridge.py, computations/hoefsmit_numpy.py"],
        "discipline": "EXPLORATORY — derive-or-refute, no fit, no forced ⁴He number.",
    }
    out = HERE.parent / "he-nu-sdp-barfold-h9-test.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
