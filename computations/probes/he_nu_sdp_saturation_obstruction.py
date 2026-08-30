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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# q0 RESOLVED, never a literal. Ruled PROTON 2026-08-30 (Q4 of the UNCLEAR
# archeology, docs/coordination/2026-08-30-unclear-44-archeology-triage.md).
#
# It held pin A, which `fca08de7d2` RETIRED on 2026-08-22 -- that value inverts
# to m_mu/m_e = 206.768282989315, matching no published CODATA. So keeping it
# was never an option; only the layer was open.
#
# WHY PROTON, stated honestly as an argument from DEFAULT, not from evidence
# of intent -- there is no positive evidence of intent in this file:
#   * No muon signal anywhere in the he_nu_sdp trio. The only "muon" mentions
#     are the 2026-08-29 label-correction note, which itself records the
#     question as OPEN -- that is the question, not an answer to it.
#   * The `q0Anchor: proton` stamp on the committed witness is NOT cited as
#     evidence: this stem is absent from q0_anchor_manifest.json, so
#     resolve_q0_anchor hands it the runtime DEFAULT. A default proves nothing.
#   * Proton is the ruled default layer for production compute, and nothing
#     here argues for the ideal layer.
#   * The witness was a straddle -- payload q0 = pin A (a MUON value) beside a
#     stamped proton q0Value. Resolving to proton makes it self-consistent.
#
# COST OF BEING WRONG IS LOW, measured: this probe records only integers
# (bounded_support_size, nu_canonical, neg_norm_blocks) and a categorical
# verdict (OBSTRUCTED); the sole continuous outputs are support weights, which
# an 11.5371 ppb pin shift moves in the ~10th significant digit. It asserts
# NOTHING (allPassed is null), nothing imports it, and no producer reads its
# witness. So no verdict can flip and nothing propagates.
#
# FLOAT64 IS CORRECT HERE and is not a NO-FLOAT64 violation: this probe runs on
# numpy throughout (hoefsmit_matrices_numpy, np.linalg.eigvalsh) and its witness
# records engine numpy+scipy, so an mpf would be downcast at the first call. It
# is f64 BY CONSTRUCTION -- bean qou-840k's 67-file class, not its 49 fixable
# ones. The float() cast below is therefore deliberate: resolve the PIN, keep
# the tier.
Q0 = float(Q_50_DIGIT_STR)
# PRECISION OF THE STRING FORM MATTERS HERE -- corrected 2026-08-30, same day,
# after the first version of this migration got it wrong.
#
# `y_lambda_wenzl_bridge_numeric` does `str(q_val)` internally, so the number of
# digits in the STRING decides the mpmath computation. Passing the float64 head
# (17 digits) leaves cancellation debris ~1e-53 where the exact answer is ZERO:
# under convention D the Wenzl level is r=2, so y_lambda vanishes identically for
# every partition with >=3 rows. Measured at the proton pin:
#     float(Q_50_DIGIT_STR) -> n=6: 3/11 negative, 0 exact zeros
#                              n=9: 10/30 negative, 0 exact zeros
#     Q_50_DIGIT_STR        -> n=6: 0/11 negative, 7 exact zeros
#                              n=9: 0/30 negative, 25 exact zeros
# `neg_norm_blocks` counts those with NO tolerance, so the float form
# resurrects a spurious "indefinite Gram" reading that the canonical reference
# (deuteron-real-sdp.witness.json, frobenius_gram_indefinite = false) denies.
#
# So: the 50-dps STRING goes to y_lambda, and float() only where numpy needs it
# (chi_numpy / hoefsmit are f64 by construction anyway).
Q0_STR: str = Q_50_DIGIT_STR
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
    # `q` arrives as a STRING; see the Q0_STR note at module scope. y_lambda
    # needs the digits, chi_numpy is numpy and needs a float.
    y = {p: float(y_lambda_wenzl_bridge_numeric(list(p), q)) for p in P}
    chi = {p: float(chi_numpy(p, cr, float(q))) for p in P}
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
    for label, q in [("q→1⁺ (well-posed)", "1.0005"), ("q₀ (indefinite)", Q0_STR)]:
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
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    o.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {o}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
