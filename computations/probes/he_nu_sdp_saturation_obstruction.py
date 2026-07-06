#!/usr/bin/env python3
"""First-principles Markov-trace SDP saturation — OBSTRUCTED (never yields ν=1,2,2).

EXPLORATORY — derive-or-refute, no fit. Capstone of the ν_SDP line (#2552, #2556):
can the "dimension of the saturating projection of T_w's SDP solution" (the kashaev
ρ_F = ν_SDP definition) be derived from first principles, reproducing the confirmed
D/T/³He = 1, 2, 2 without hand-assignment?

This probe tests the operator-selection SDP saturation `min t·x s.t. Σx=tr_M(β),
diag(tr_M P_λ)·x ≥ 0` in its two principled regimes, with NO external (encoding)
constraint:

  • q → 1⁺  — the Frobenius Gram is "most positive" (well-posed limit). The program
    reduces to a min-cost LP; its vertex solution saturates a SINGLE block.
  • q₀      — the Gram is indefinite (negative-norm blocks present at BOTH q→1 and q₀,
    so the indefiniteness is structural, not a q₀ artifact); the program is unbounded
    / rail-degenerate.

RESULT (y_λ via Wenzl bridge, χ^λ via hoefsmit_numpy + atom_canonical_crossings):

  q → 1⁺:  bounded support = 1 block for D, T, ³He  (ν_pred = 1, 1, 1)
  q₀    :  bounded support = 0 (D, T) / 1 (³He)     (rail-degenerate)

NEITHER regime reproduces the confirmed ν = 1, 2, 2. The min-cost LP always picks one
block; the indefinite SDP has no encoding-independent saturation. Combined with the
prior refutations (per-block PSD → 1,2,1; SDP active-set → 7; bar-fold → 1,1,0;
self-conjugate count → mechanism refuted), there is **no** principled Markov-trace SDP
saturation yielding ν_SDP. The values 1, 2, 2 are recovered only by hand-assignment.

VERDICT: the first-principles SDP-saturation derivation of ν_SDP is OBSTRUCTED. The
kashaev "MacMahon-style SDP-multiplicity" categorical home is, at present, aspirational
— no computation realizes it. ρ_F = 2 for ⁴He is therefore an underived input (chosen
to match the +5.87% magic-A binding), not a derived quantity; it should be labelled an
acknowledged input pending a genuine derivation, not a closed structural result.

Output: he-nu-sdp-saturation-obstruction.witness.json
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
RAIL = 1e5


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


def _hd(lam):
    lp = _conj(lam)
    pr = 1
    for i, row in enumerate(lam):
        for j in range(row):
            pr *= (row - (j + 1)) + (lp[j] - (i + 1)) + 1
    return math.factorial(sum(lam)) // pr


def saturate(Z, N, q):
    """Bare operator-selection LP saturation (NO encoding constraint)."""
    n = 3 * (Z + N)
    cr = atom_canonical_crossings(Z, N)
    P = list(_parts(n))
    y = {p: float(y_lambda_wenzl_bridge_numeric(list(p), q)) for p in P}
    chi = {p: float(chi_numpy(p, cr, q)) for p in P}
    t = np.array([y[p] * chi[p] for p in P])
    frob = np.array([y[p] * _hd(p) for p in P])
    n_neg = int((frob < 0).sum())
    nt = float(t.sum())
    res = linprog(c=t, A_ub=-np.diag(frob), b_ub=np.zeros(len(P)),
                  A_eq=[np.ones(len(P))], b_eq=[nt],
                  bounds=[(-1e6, 1e6)] * len(P), method="highs")
    if not res.success:
        return {"n": n, "neg_norm_blocks": n_neg, "feasible": False, "bounded_support": []}
    bs = [(list(P[i]), float(res.x[i])) for i in range(len(P))
          if 1e-6 < abs(res.x[i]) < RAIL]
    return {"n": n, "neg_norm_blocks": n_neg, "feasible": True, "bounded_support": bs}


def main() -> int:
    print("=" * 84)
    print("  First-principles Markov-trace SDP saturation — two principled regimes")
    print("=" * 84)
    nu_conf = {"D": 1, "T": 2, "3He": 2}
    out = {}
    for label, q in [("q→1⁺ (well-posed)", 1.0005), ("q₀ (indefinite)", Q0)]:
        print(f"\n  {label}   q={q}")
        out[label] = {}
        for nm, Z, N in [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1)]:
            r = saturate(Z, N, q)
            sz = len(r["bounded_support"])
            print(f"    {nm}: neg-norm {r['neg_norm_blocks']}/{('11' if r['n']==6 else '30')}"
                  f"  bounded support = {sz}  vs ν={nu_conf[nm]}  "
                  f"{[tuple(p) for p,_ in r['bounded_support']][:3]}")
            out[label][nm] = {"bounded_support_size": sz, "nu_canonical": nu_conf[nm],
                              "neg_norm_blocks": r["neg_norm_blocks"],
                              "support": r["bounded_support"]}

    q1 = {k: v["bounded_support_size"] for k, v in out["q→1⁺ (well-posed)"].items()}
    print("\n" + "=" * 84)
    print(f"  VERDICT: OBSTRUCTED — saturation sizes  q→1: {q1}  (all =1, single min-cost")
    print("  block); q₀: rail-degenerate. NEITHER regime gives ν=1,2,2. No principled")
    print("  Markov-trace SDP saturation yields ν_SDP; the values are hand-assigned.")
    print("  ⇒ ρ_F=2 (⁴He) is an underived input, not a derived structural quantity.")
    print("=" * 84)

    witness = {
        "computation": "he-nu-sdp-saturation-obstruction",
        "kind": "exploratory-probe",
        "description": (
            "Capstone of the ν_SDP line: the operator-selection SDP saturation does not "
            "reproduce ν=1,2,2 in any principled regime — q→1 gives a single min-cost "
            "block (ν=1 always); q₀ is indefinite/rail-degenerate. With per-block-PSD, "
            "SDP-active-set, bar-fold, and self-conjugate all refuted, ν_SDP has no "
            "first-principles SDP-saturation derivation; 1,2,2 are hand-assigned. No fit."
        ),
        "engine": "numpy+scipy", "q0": Q0,
        "regimes": out,
        "q1_saturation_sizes": q1,
        "verdict": "OBSTRUCTED",
        "conclusion": ("No principled Markov-trace SDP saturation yields ν_SDP=1,2,2. "
                       "The kashaev 'MacMahon SDP-multiplicity' categorical home is "
                       "aspirational; ρ_F=2 (⁴He) is an underived acknowledged input, "
                       "not a derived structural quantity."),
        "refs": ["PR #2552, #2556 (ν_SDP arc)",
                 "content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md",
                 "computations/deuteron_real_sdp.py"],
        "discipline": "EXPLORATORY — derive-or-refute, no fit, no forced ⁴He number.",
    }
    o = HERE.parent / "he-nu-sdp-saturation-obstruction.witness.json"
    o.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {o}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
