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
import math  # float64-ok: integer factorial in _hd only
import sys
from pathlib import Path

import numpy as np  # float64-ok: scipy.optimize.linprog array input
from scipy.optimize import linprog  # float64-ok: LP support size probe

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from hoefsmit_numpy import chi_numpy  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

# READ the pin; do not transcribe it. This was
#     Q0 = 1.1099785955573347
# -- a bare float64 literal of the RETIRED muon pin A (superseded by CODATA 2022
# in fca08de7d29, 2026-08-28). The witness recorded it as `q0` while
# `stamp_staleness_metadata(..., q0_anchor=None)` below resolved to the default
# PROTON anchor and wrote `q0Value` = 1.10997858275138..., so the witness
# declared an anchor it had not computed at, with its own two fields ~11.5 ppb
# apart -- the mu-p substrate tension itself. `q0_anchor_consistency_audit`
# compares q0Anchor against q0Value, and those agreed, so the straddle passed
# every gate (bean `qou-tekx`).
#
# Proton is the correct target here, not a choice: AGENTS.md's 2026-08-07 owner
# directive makes the experimental (proton) pin the default for all touched
# compute, and this stem is absent from `q0_anchor_manifest.json` entirely, so
# the stamper already resolves it to proton. Reading `q_parameter.Q` makes the
# computation agree with the stamp instead of contradicting it.
#
# float64 is forced at this boundary, not chosen: scipy/numpy below
# (`linprog`, `np.linalg`) cannot accept mpf. `q_parameter.Q` is already the
# float64 view of the proton pin, so nothing is downgraded here that was not
# float64 for the whole probe. The verdict is combinatorial (support sizes /
# PSD counts), not a precision measurement.
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
RAIL = 1e5  # float64-ok: scipy.optimize.linprog rail bound


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
    y = {p: float(y_lambda_wenzl_bridge_numeric(list(p), q)) for p in P}  # float64-ok: scipy.optimize.linprog LP input
    chi = {p: float(chi_numpy(p, cr, q)) for p in P}  # float64-ok: scipy.optimize.linprog LP input
    t = np.array([y[p] * chi[p] for p in P])
    frob = np.array([y[p] * _hd(p) for p in P])
    # `frob = y_lambda * hook-dim` and the hook-length dimension is a positive
    # integer, so this count is entirely `sign(y_lambda)`. Eight of the eleven
    # n=6 y_lambda are MATHEMATICALLY ZERO, and a bare `< 0` was reading the
    # sign of their arithmetic RESIDUE:
    #
    #   partition        y at the old A pin      y at the proton pin
    #   (4,1,1)          0.00000000e+00           3.22927672e-52
    #   (3,1,1,1)        0.00000000e+00          -6.18583095e-53   <- counted
    #   (2,2,1,1)        0.00000000e+00          -2.74307468e-53   <- counted
    #   (1,1,1,1,1,1)    0.00000000e+00          -2.83696452e-54   <- counted
    #
    # The nonzero blocks are O(1e-2 .. 1e-1), so the two populations are ~50
    # orders of magnitude apart and no real value is anywhere near the cut.
    # The committed `neg_norm_blocks: 0` was never "no negative-norm blocks" --
    # it was "at that pin the residues came out as exact 0.0". Changing q0 by
    # 11.5 ppb (the mu-p tension) moved them off exact zero and the count jumped
    # 0 -> 3 for D and 0 -> 10 for 3He and T, with nothing about the Gram having
    # changed. Verified by a control run: the OLD pin under CURRENT code
    # reproduces the committed 0/0/0 byte-identically, so this is the pin and
    # not code drift (bean `qou-tekx`).
    #
    # AGENTS.md: a float64/residue-level agreement is the floor of the
    # arithmetic, not evidence about the mathematics. Threshold it, and record
    # BOTH numbers so a reader can see the separation rather than trust a cut.
    # Carried as TEXT and parsed for the comparison, not the other way round.
    # The threshold is a chosen literal, not a computed quantity, so serializing
    # `float(1e-30)` into the witness put a raw float64 in six places for a
    # number that has an exact decimal spelling. Comparing against float64
    # residues is the one thing it legitimately has to be a float for.
    _ZERO_TOL_STR = "1e-30"      # ~28 orders below the smallest real |y|,
    _ZERO_TOL = float(_ZERO_TOL_STR)  # float64-ok: threshold against f64 frob array
    n_neg = int((frob < -_ZERO_TOL).sum())
    n_zero = int((np.abs(frob) <= _ZERO_TOL).sum())
    nt = float(t.sum())  # float64-ok: scipy.optimize.linprog b_eq rhs
    res = linprog(c=t, A_ub=-np.diag(frob), b_ub=np.zeros(len(P)),
                  A_eq=[np.ones(len(P))], b_eq=[nt],
                  bounds=[(-1e6, 1e6)] * len(P), method="highs")
    if not res.success:
        return {"n": n, "neg_norm_blocks": n_neg, "blocks_indistinguishable_from_zero": n_zero,
                "zero_tolerance": _ZERO_TOL_STR, "feasible": False, "bounded_support": []}
    # Serialize scipy.optimize.linprog f64 support weights as strings so raw
    # float64 values do not enter the witness (bean qou-4pmk).
    bs = [(list(P[i]), f"{float(res.x[i]):.12g}") for i in range(len(P))  # float64-ok: scipy linprog f64 output serialized at true precision
          if 1e-6 < abs(res.x[i]) < RAIL]
    return {"n": n, "neg_norm_blocks": n_neg, "blocks_indistinguishable_from_zero": n_zero,
            "zero_tolerance": _ZERO_TOL_STR, "feasible": True, "bounded_support": bs}


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
                              "blocks_indistinguishable_from_zero":
                                  r["blocks_indistinguishable_from_zero"],
                              "zero_tolerance": r["zero_tolerance"],
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
        "engine": "numpy+scipy", "q0": Q_50_DIGIT_STR,
        "regimes": out,
        "q1_saturation_sizes": q1,
        "verdict": "OBSTRUCTED",
        "conclusion": ("No principled Markov-trace SDP saturation yields ν_SDP=1,2,2. "
                       "The kashaev 'MacMahon SDP-multiplicity' categorical home is "
                       "aspirational; ρ_F=2 (⁴He) is an underived acknowledged input, "
                       "not a derived structural quantity."),
        "refs": ["PR #2552, #2556 (ν_SDP arc)",
                 "folio/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md",
                 "computations/deuteron_real_sdp.py"],
        "discipline": "EXPLORATORY — derive-or-refute, no fit, no forced ⁴He number.",
    }
    o = HERE.parent / "he-nu-sdp-saturation-obstruction.witness.json"
    from qou_substrate.witness import WitnessBuilder as _WB
    q0_reg = {k: v["bounded_support_size"] for k, v in out["q₀ (indefinite)"].items()}
    _q1_max_support = max(q1.values())
    _neither_matches = 1 if (q1 != nu_conf and q0_reg != nu_conf) else 0
    saved_path = (
        _WB.wrap_legacy(
            "he-nu-sdp-saturation-obstruction",
            witness,
            script_path=__file__,
            engine="numpy+scipy",
            output_dir=HERE.parent,
        )
        .add_assertion(
            "he_nu_sdp_q1_saturates_at_most_single_block",
            computed=str(_q1_max_support),
            expected="1",
            tolerance="0",
            source="at q->1+ bounded support size across D, T, 3He is at most 1 (never 2)",
        )
        .add_assertion(
            "he_nu_sdp_neither_regime_yields_1_2_2",
            computed=str(_neither_matches),
            expected="1",
            tolerance="0",
            source="neither q->1+ nor q0 reproduces the hand-assigned nu_SDP = (1,2,2)",
        )
        .save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    )
    print(f"  witness: {saved_path}")
    return 0


def _selftest() -> int:
    assert _hd((3,)) == 1 and _hd((2, 1)) == 2 and _hd((1, 1, 1)) == 1
    print("self-test: ok (_hd hook dimensions verified)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:] or "--selftest" in sys.argv[1:]:
        raise SystemExit(_selftest())
    raise SystemExit(main())
