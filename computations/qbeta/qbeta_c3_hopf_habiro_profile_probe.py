#!/usr/bin/env python3
# ANCHOR NOTE (2026-06-22): q0 = 1.10997858275… occurrences below are the
# RETIRED pre-2026-05-28 proton anchor (old re-pin #1422), kept as this
# probe's historical / cross-anchor / pinned comparison value. The CURRENT
# canonical proton q0 is q_at() ≈ 1.1099785955573347…; the muon anchor is
# q_muon_at() ≈ 1.10997859555418…. This probe is preserved as-is by design.
"""qbeta_c3_hopf_habiro_profile_probe.py — Step 4 (corrected) probe:
the Q_β c_3 residue A on the **Hopf-link substructure**, via the Step 3
`trace_formal` roots-of-unity machinery (PR #1811).

EXPLORATORY / NEGATIVE — NOT a wire decision and NOT a derivation.

## Why the Hopf link (corrected knot assignment, 2026-06-04)

The fibre-composite-4 implementation spec
(`docs/scope/2026-06-04-fibre-composite4-implementation-spec.md`, Step 4)
verified that the c_3 rung is **NOT** the cinquefoil T(2,5) — that is the
*muon* particle-knot (`lepton_t2n_torus_tower.py`). The structural source
of c_3 is the **Hopf link**: `c_3 = J_Hopf(q=1) = -2`, proven
categorically in
`content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md`
(2-strand sub-braid windings; Facts 1-4). The shared `/25` is a
coincident *fibre constant* `[5]_q²|_{q=1}`, not a shared knot.

So this probe replaces the retired cinquefoil attack with the Hopf one,
and stays at the **fibre / root-of-unity** level (the real-q route is
closed by the 2026-06-04 rigidity falsification — a smooth real-q `f(q)`
cannot track `dc_3/dq ≈ 4.6×10⁶`).

## What it does (uses all three Step-3 primitives)

1. Builds the Hopf-link Jones in ℚ(s) (s = q^½) in the two framings the
   corpus uses, and confirms `classical_limit → -2` for BOTH via the
   Step-3 `classical_limit` — i.e. the new machinery recovers the proven
   `c_3 = J_Hopf(1) = -2` (framing-independent at q=1).
2. Exhibits the clean identity `J_bal = -[2]_q = -quantum_int(4)/quantum_int(2)`
   symbolically (Step-3 `quantum_int`).
3. Maps `habiro_profile(J_bal, N_max)` (Step-3) over the roots of unity:
   the family is REAL and pole-free, and **only N=1 (= q=1) returns -2**
   — the #1811 lesson, now on the Hopf object.
4. Cross-anchor NEGATIVE: shows the bare real-q Hopf framing `J_Hopf(q₀)`
   is RIGID — it reproduces the residue at one anchor scale but cannot
   produce the proton-vs-muon residue spread (q₀ differ by ~1e-8, the
   residues by ~7×). Re-confirms
   `docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`
   via the Hopf object.

## Conclusion / Δ_λ-gate

NEGATIVE, bounding. The proven `c_3 = -2` stays the production structural
value (112× residual tightening at N=3, per the Hopf doc). The *residue A*
(the sub-ppm correction beyond -2) is NOT recovered by any single real-q
Hopf framing nor any finite root of unity. The genuine open object is a
**non-trivial cyclotomic (colored-Jones) Habiro element** on the Hopf
substructure whose τ-evaluation gives the residue across anchors — still
open. Nothing is wired; c_3 = -2 unchanged.

## Requires

`pyhecke` (+ `sympy`) for the Step-3 `trace_formal` machinery, and
`mpmath` for the anchor arithmetic. (Unlike the self-contained sibling
`qbeta_composite4_fibre_root_of_unity_probe.py`, this one demonstrates
the pyhecke machinery, so it is not pyhecke-free.)
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf

from pyhecke.trace_formal import (
    s,
    quantum_int,
    classical_limit,
    habiro_profile,
)

mp.dps = 50

# ── Pinned anchor data (verified against the corpus) ──────────────────
# Cross-anchor q₀ + empirical c_3, from
# docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md
Q0_PROTON = "1.10997858275"     # proton (production) anchor
Q0_MUON = "1.10997859555"       # muon anchor
C3_PROTON = "-2.0693"           # empirical c_3 at proton anchor
C3_MUON = "-2.0097"             # empirical c_3 at muon anchor
C3_STRUCTURAL = -2              # proven J_Hopf(q=1) = -2 (production)


def _close(a, b, tol=1e-9) -> bool:
    return abs(complex(a) - complex(b)) < tol


def main() -> int:
    # ── 1. Hopf Jones in ℚ(s), two corpus framings ───────────────────
    # balanced: J_bal = -(q + q⁻¹) = -(s² + s⁻²)   [c3_hopf_habiro_analysis.py]
    # writhe  : J_wr  = -q²(1 + q²) = -s⁴(1 + s⁴)   [hopf doc Fact 4]
    J_bal = -(s ** 2 + s ** (-2))
    J_wr = -s ** 4 * (1 + s ** 4)

    cl_bal = complex(classical_limit(J_bal))
    cl_wr = complex(classical_limit(J_wr))
    assert _close(cl_bal, C3_STRUCTURAL), cl_bal
    assert _close(cl_wr, C3_STRUCTURAL), cl_wr

    # ── 2. quantum_int identity: J_bal = -[2]_q = -[4]/[2] ────────────
    # [4]_q/[2]_q = (s⁴-s⁻⁴)/(s²-s⁻²) = s²+s⁻², so J_bal = -that.
    qint_identity = sp.simplify(
        J_bal - (-quantum_int(4) / quantum_int(2))
    )
    assert qint_identity == 0, qint_identity

    # ── 3. habiro_profile of the Hopf object over roots of unity ──────
    # J_bal is a Laurent polynomial in s → pole-free → every N kept.
    # At ζ_N = exp(2πi/N): J_bal = -2cos(2π/N), REAL. Only N=1 (=q=1)
    # gives -2.
    prof = habiro_profile(J_bal, 12)
    prof_serialized = []
    n1_value = None
    only_n1_hits_structural = True
    for N, val in prof:
        re_im = (float(val.real), float(val.imag))
        prof_serialized.append({"N": N, "re": re_im[0], "im": re_im[1]})
        if N == 1:
            n1_value = re_im[0]
        elif _close(val, C3_STRUCTURAL):
            only_n1_hits_structural = False
    assert n1_value is not None and _close(n1_value, C3_STRUCTURAL)
    assert only_n1_hits_structural, "a finite root N>1 unexpectedly hit -2"
    # family is real (sin/cos ratios), no imaginary residue
    max_im = max(abs(p["im"]) for p in prof_serialized)
    assert max_im < 1e-12, max_im

    # ── 4. Cross-anchor rigidity NEGATIVE (real-q Hopf framing) ───────
    def j_bal_num(q0_str):
        q0 = mpf(q0_str)
        return -(q0 + 1 / q0)

    jp = j_bal_num(Q0_PROTON)         # J_Hopf(q₀_proton), real-q
    jm = j_bal_num(Q0_MUON)
    res_p = mpf(C3_PROTON) - C3_STRUCTURAL   # empirical residue, proton
    res_m = mpf(C3_MUON) - C3_STRUCTURAL     # empirical residue, muon
    model_res_p = jp - C3_STRUCTURAL          # Hopf real-q residue model
    model_res_m = jm - C3_STRUCTURAL
    empirical_swing = res_p - res_m           # ~ -0.0596 (7× spread)
    model_swing = model_res_p - model_res_m   # ~ 1e-8 (rigid)
    swing_ratio = float(model_swing / empirical_swing)

    # The model residue (~ -0.011) sits near the muon residue but is rigid:
    # it cannot reach the proton residue (~ -0.069). That is the NEGATIVE.
    rigidity_factor = float(abs(empirical_swing / model_swing))

    # ── witness (self-contained schema, mirrors the sibling probe) ────
    here = Path(__file__).resolve().parent
    assertions = [
        {
            "name": "hopf_classical_limit_is_minus_2_both_framings",
            "computed": [cl_bal.real, cl_wr.real],
            "expected": [C3_STRUCTURAL, C3_STRUCTURAL],
            "passed": _close(cl_bal, C3_STRUCTURAL) and _close(cl_wr, C3_STRUCTURAL),
            "source": "Step-3 classical_limit of both corpus framings of "
                      "J_Hopf (balanced -(q+q⁻¹), writhe -q²(1+q²)) returns -2 "
                      "= the proven c_3 = J_Hopf(q=1) (framing-independent at q=1).",
        },
        {
            "name": "j_bal_equals_minus_quantum_int_4_over_2",
            "computed": int(qint_identity == 0),
            "expected": 1,
            "passed": bool(qint_identity == 0),
            "source": "Symbolic identity J_bal = -[2]_q = "
                      "-quantum_int(4)/quantum_int(2) (Step-3 quantum_int); "
                      "residual simplifies to 0 in ℚ(s).",
        },
        {
            "name": "habiro_profile_real_only_N1_hits_structural",
            "computed": {"n1": n1_value, "only_N1": only_n1_hits_structural,
                         "max_im": max_im},
            "expected": "only N=1 (=q=1) → -2; family real",
            "passed": bool(only_n1_hits_structural and max_im < 1e-12
                           and _close(n1_value, C3_STRUCTURAL)),
            "source": "Step-3 habiro_profile(J_bal, 12): the root-of-unity "
                      "family is REAL (max|Im|<1e-12) and pole-free; only N=1 "
                      "(which is q=1) returns -2 — the #1811 lesson on the Hopf "
                      "object. No finite root N>1 reproduces the structural -2.",
        },
        {
            "name": "real_q_hopf_framing_rigid_across_anchors",
            "computed": rigidity_factor,
            "expected": ">1e6 (rigid)",
            "passed": bool(rigidity_factor > 1e6),
            "source": "Bare real-q Hopf framing J_Hopf(q₀) swings "
                      f"{1.0/rigidity_factor:.2e} of the empirical proton-vs-muon "
                      "residue spread → residue A is fibre-level, not real-q. "
                      "Re-confirms docs/audits/"
                      "2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md.",
        },
    ]
    witness = {
        "engine": "pyhecke.trace_formal",
        "engineVersion": f"sympy-{sp.__version__}+mpmath",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-c3-hopf-habiro-profile",
        "scriptFile": "qbeta_c3_hopf_habiro_profile_probe.py",
        "tier": "NEGATIVE/exploratory",
        "precisionMetadata": {"compute_dps": 50},
        "assertions": assertions,
        "data": {
            "classical_limit": {
                "J_bal_minus_q_plus_qinv": cl_bal.real,
                "J_wr_minus_q2_1_plus_q2": cl_wr.real,
                "proven_value": C3_STRUCTURAL,
            },
            "quantum_int_identity": "J_bal = -[2]_q = -quantum_int(4)/quantum_int(2)",
            "habiro_profile_J_bal": {
                "N_max": 12,
                "n1_equals_q1_value": n1_value,
                "only_N1_hits_structural_minus2": only_n1_hits_structural,
                "max_imaginary_part": max_im,
                "samples": prof_serialized,
            },
            "cross_anchor_rigidity": {
                "q0_proton": Q0_PROTON,
                "q0_muon": Q0_MUON,
                "empirical_residue_proton": str(res_p),
                "empirical_residue_muon": str(res_m),
                "model_residue_proton": str(model_res_p),
                "model_residue_muon": str(model_res_m),
                "empirical_swing": str(empirical_swing),
                "model_swing": str(model_swing),
                "swing_ratio_model_over_empirical": swing_ratio,
                "rigidity_factor": rigidity_factor,
            },
        },
        "deltaLambdaGate": {
            "fittedForms": False,
            "wiredToProduction": False,
            "productionC3": "c_3 = -2 (proven J_Hopf(1), 112× tightening)",
        },
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    out = here / "qbeta-c3-hopf-habiro-profile.witness.json"
    out.write_text(json.dumps(witness, indent=2))

    print("✓ qbeta-c3-hopf-habiro-profile.witness.json")
    print(f"  classical_limit(J_bal) = {cl_bal.real:+.6f}  (proven c_3 = -2)")
    print(f"  classical_limit(J_wr)  = {cl_wr.real:+.6f}  (framing-independent)")
    print(f"  J_bal = -[2]_q = -[4]/[2]  (symbolic identity): OK")
    print(f"  habiro_profile: only N=1 (=q=1) returns -2; max|Im| = {max_im:.1e}")
    print(f"  cross-anchor rigidity factor = {rigidity_factor:.3e}× "
          f"(model swings {1/rigidity_factor:.2e} of empirical) → residue A fibre-level")
    return 0


if __name__ == "__main__":
    sys.exit(main())
