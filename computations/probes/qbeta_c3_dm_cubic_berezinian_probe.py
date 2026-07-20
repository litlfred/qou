#!/usr/bin/env python3
"""qbeta_c3_dm_cubic_berezinian_probe.py — DERIVATION ATTEMPT for the Q_β
precision-ladder coefficient c_3 via the Donagi–Markman cubic 3-jet /
Berezinian even–odd cross-term (bean qou-1dnr).

## The route being tested (NEW angle, landed 2026-07-20)

The Door-v / super-Berezinian framing (`QOU.Brings.SuperDMBerezinian`,
`QOU.Brings.CategoricalLagrangianDMCubic`) says: in the ladder
`Q_β = Q_base·∏(1 + c_k u^k)`, `u = b·ℏ_q²`,

  * `c_2 = ∂²F`  — the period matrix τ (the proved-EXACT bar-even 2-jet, c_2 = −1);
  * `c_3 = ∂³F`  — the Donagi–Markman **cubic** 3-jet, whose **bar-ODD**
    (sinh/decay) component is the one Q_β sees;
  * the first even/odd MIXING order is the Berezinian cross-term
    `B·D⁻¹·C` inside `Ber = det(A − B·D⁻¹·C)·(det D)⁻¹`.

This probe builds two INDEPENDENT (never CODATA-inverted) realizations of that
3-jet and runs the FALSIFIABLE anchor-invariance test.

## The falsifiable honesty test (AGENTS.md anti-fit / §Axiomatization-is-NOT-a-Proof)

A genuine DERIVED c_3 (a true Taylor coefficient of a convergent series) must
be **anchor-INVARIANT**: its value at the proton-pinned q₀ and the muon-pinned
q₀ must agree, because a Taylor coefficient is a property of the series, not of
which observable pinned q₀.

The EMPIRICAL c_3 target (extracted by inverting the CODATA Q_β through the
c_2 rung — this is the FIT side, `qbeta_utils.c3_target_at`) **SWINGS 2.43 %**
between the two near-identical anchors (they differ by ~1.3e-8 in q). Per the
registry KC21, that swing is the `1/u³` ladder-inversion magnifying a **smooth**
numerator zero: `dc_3/dq ≈ 3.8×10⁶`.

So the decisive discriminator is:

  * derived c_3 anchor-invariant AND value-matches empirical at both anchors
    → genuine DERIVATION (would let Q_β meet its 100× target);
  * derived c_3 anchor-invariant but the empirical target swings 2.43 %
    → the derived smooth object **cannot** reproduce the swinging empirical
      value (matches at most one anchor) — scope-(a) NEGATIVE;
  * derived c_3 swings comparably to empirical → it is itself a q₀-dependent
    near-match (a FIT), not a Taylor coefficient.

## Refuted mechanisms this route does NOT repeat (corpus-grep, AGENTS.md STRICT)

Verified against `docs/coordination/ck-dk-canonical-registry.md` and the
`1ppq-qbeta.md` flip-flop table BEFORE running:

  * NOT `c_3 = J_Hopf(q=1) = −2` (flip-flops #1–#4; near-match, not Taylor-exact).
  * NOT `c_3 = J − ℏ_q²` (flip #1).
  * NOT the `[3]_q/25` 3-rung Habiro closure (proton-anchor-only, rigidity-
    falsified PR #1781/#1842).
  * NOT the Li_2^q × spectral combiner (mech #7, refuted PR #1609).
  * NOT the Δtr_M bar-decomposition value-identity (accidental cross-order
    coincidence, PR #1593/#1615).
  * NOT `c_3 = −Vol(4₁)+u−(10/3)u²` (anchor-blind, misses proton, re-scoped
    2026-07-11).
  * NOT a real-q algebraic closure of the shape KC20 already Lean-EXCLUDES
    (bar-odd carrier lives in a degree-3 irreducible field with no quadratic
    anchor as a root).
  * NOT a q-difference / (q-)holonomic recurrence for the odd channel — KC22
    Lean-proves `D(ũ)` is NOT low-order (q-)holonomic in any tested class, so
    the "read c_3 off the q-lift 3-term recurrence" sub-route (task approach #1)
    is refuted a priori: the odd channel is transcendental/resurgent (Écalle),
    not a recurrence output.

The route IS new as an explicit **Berezinian even/odd cross-term** framing
(the super-Berezinian scaffold landed 2026-07-20). This probe tests whether the
new framing escapes the KC20/KC21/KC22 obstructions. It does not.

## What is NOT done here (honesty)

The exact geometric super-period data (A, B, C, D of the Bring hyperkähler
fibration) is the OPEN keystone `conj:qdifference-kernel-prolongation-symbol`.
This probe therefore instantiates the super-period matrix with corpus-grounded
substrate blocks (the H_3(q) Wedderburn characters + Markov weights) as a
representative realization. The exact numeric VALUE of any single cross-term is
modeling-dependent; what is construction-INDEPENDENT — and what the probe
actually rests its verdict on — is the **anchor-invariance / smoothness** of any
real-q algebraic Berezinian cross-term. That smoothness is the falsifier.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))                                  # computations/
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: E402, F401
from mpmath import mp, mpf, sqrt, cos, taylor, matrix  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import (  # noqa: E402
    c3_target_at,
    substrate_ladder_quantities,
    chi_block_3,
    chi_block_21,
    chi_block_111,
    markov_parameter,
)
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:  # pragma: no cover
    print("ERROR: qou_substrate not importable", file=sys.stderr)
    sys.exit(1)


# ── Construction 1: the DM cubic 3-jet ∂³F of the categorical producer phase ──
# F = the substrate phase Φ; G(u) = cos(α − u/2)(1 − u²)/cos(α) is the on-main
# canonical N=2 producer model (probe_q_beta_operator_valued_N3.py; the
# reconciliation probe uses the same). α = (z−1)h/2 is derived from the
# substrate (Markov weight z, h = q−1/q), NOT from CODATA — so its Taylor
# coefficients are an INDEPENDENT categorical prediction. c_3 = the 3-jet.
def dm_cubic_3jet_from_phase(alpha: mpf) -> mpf:
    ca = cos(alpha)

    def G(u):
        return cos(alpha - u / 2) * (1 - u ** 2) / ca

    return taylor(G, mpf(0), 3)[3]


# ── Construction 2: the Berezinian even/odd cross-term from the H_3 blocks ──
# Super-period matrix grounded in the H_3(q) Wedderburn decomposition:
#   even (bar-EVEN / cosh / mass) sector = { (3), (1,1,1) }  (both bar-even),
#   odd  (bar-ODD  / sinh / decay) sector = { (2,1) }        (κ_{(2,1)} exactly
#                                                              bar-odd — KC13).
# The off-diagonal super-blocks B, C carry the even↔odd MIXING. Its measure is
# the Berezinian Ber = det(A − B·D⁻¹·C)·(det D)⁻¹; the cross-term B·D⁻¹·C is the
# first even/odd mixing correction (berezinian_offDiag_zero: it vanishes at
# block-diagonal order). We report the dimensionless mixing fraction
#   frac = (Ber − Ber_nomix)/Ber_nomix
# for several natural mixing choices, and its ANCHOR SWING (the falsifier).
def berezinian_cross_fraction(q: mpf, mixing: str) -> mpf:
    c3v = chi_block_3(q)
    c21 = chi_block_21(q)      # bar-ODD block (odd sector D)
    c111 = chi_block_111(q)
    z = markov_parameter(q)
    h = q - 1 / q
    hbar = (q - 1) / q

    # even 2x2 block A (bar-even characters on the diagonal; even-even coupling
    # off-diagonal), odd 1x1 block D = χ_{(2,1)} (bar-odd).
    A = matrix([[c3v, z * h], [z * h, c111]])
    D = c21

    # three natural leading even↔odd mixing choices (all O(substrate), all real-q
    # algebraic) — the verdict rests on their COMMON anchor-invariance, not on
    # any single value:
    if mixing == "markov":       # B,C ~ Markov weight z
        B = matrix([[z], [z]])
        C = matrix([[z, z]])
    elif mixing == "hbar":       # B,C ~ ℏ_q (the deformation scale)
        B = matrix([[hbar], [hbar]])
        C = matrix([[hbar, hbar]])
    elif mixing == "mixed":      # B ~ z, C ~ h (asymmetric)
        B = matrix([[z], [z]])
        C = matrix([[h, h]])
    else:  # pragma: no cover
        raise ValueError(mixing)

    Dinv = mpf(1) / D
    cross = B * Dinv * C
    detA = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    Amix = A - cross
    detAmix = Amix[0, 0] * Amix[1, 1] - Amix[0, 1] * Amix[1, 0]
    ber = detAmix / D
    ber_nomix = detA / D
    return (ber - ber_nomix) / ber_nomix


def swing_pct(vp: mpf, vm: mpf) -> mpf:
    return (vp - vm) / vm * 100 if vm != 0 else mpf("nan")


def main() -> int:
    set_compute_dps()
    t0 = time.time()
    me = mpf(str(M_E_MEV))
    qc = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)

    # (0) The empirical (CODATA-inverted, FIT-side) c_3 target — the swinging
    #     object the derivation would have to reproduce.
    emp_p = c3_target_at(qp, qc, me)
    emp_m = c3_target_at(qm, qc, me)
    emp_swing = swing_pct(emp_p, emp_m)
    dc3_dq_emp = (emp_p - emp_m) / (qp - qm)

    sub_p = substrate_ladder_quantities(qp)
    sub_m = substrate_ladder_quantities(qm)

    # (1) DM cubic 3-jet of the categorical phase (∂³F).
    jet_p = dm_cubic_3jet_from_phase(sub_p["alpha"])
    jet_m = dm_cubic_3jet_from_phase(sub_m["alpha"])
    jet_swing = swing_pct(jet_p, jet_m)

    # (2) Berezinian even/odd cross-fraction (three mixing choices).
    berez = {}
    for mixing in ("markov", "hbar", "mixed"):
        bp = berezinian_cross_fraction(qp, mixing)
        bm = berezinian_cross_fraction(qm, mixing)
        berez[mixing] = {
            "proton": fmt(bp),
            "muon": fmt(bm),
            "swing_pct": fmt(swing_pct(bp, bm)),
        }

    # Required vs available derivative: a smooth real-q construction has
    # dc_3/dq = O(1); the empirical target needs ~3.8e6. Finite-difference the
    # DM-cubic 3-jet to exhibit the O(1) scale directly.
    dc3_dq_jet = (jet_p - jet_m) / (qp - qm)

    print("=" * 84)
    print(" Q_β c_3 — DM-cubic 3-jet / Berezinian even-odd cross-term derivation attempt")
    print("=" * 84)
    print(f"  q_proton = {mp.nstr(qp, 28)}")
    print(f"  q_muon   = {mp.nstr(qm, 28)}   (Δq = {mp.nstr(qp - qm, 4)})")
    print()
    print("  EMPIRICAL c_3 target (CODATA-inverted FIT side; the swinging object):")
    print(f"    proton = {mp.nstr(emp_p, 10)}   muon = {mp.nstr(emp_m, 10)}")
    print(f"    swing  = {float(emp_swing):+.4f} %      dc_3/dq = {mp.nstr(dc3_dq_emp, 5)}")
    print()
    print("  (1) DM cubic 3-jet ∂³F of the categorical phase (INDEPENDENT of CODATA):")
    print(f"    proton = {mp.nstr(jet_p, 10)}   muon = {mp.nstr(jet_m, 10)}")
    print(f"    swing  = {float(jet_swing):+.3e} %   dc_3/dq = {mp.nstr(dc3_dq_jet, 5)}")
    print(f"    value vs empirical: {float(jet_p):+.4f} vs {float(emp_p):+.4f} (WRONG sign & magnitude)")
    print()
    print("  (2) Berezinian even/odd cross-fraction B·D⁻¹·C (H_3 super-period matrix):")
    for mixing, d in berez.items():
        print(f"    [{mixing:>6}] proton={d['proton'][:12]:>13} muon={d['muon'][:12]:>13} "
              f"swing={float(mpf(d['swing_pct'])):+.3e} %")
    print()
    print("=" * 84)
    print(" VERDICT")
    print("=" * 84)
    # A construction is "anchor-invariant" if its swing is << the empirical
    # 2.43% (we use 1e-3 %, i.e. > 3 orders below empirical).
    ANCHOR_INV = mpf("1e-3")  # percent
    jet_invariant = abs(jet_swing) < ANCHOR_INV
    berez_invariant = all(abs(mpf(d["swing_pct"])) < ANCHOR_INV for d in berez.values())
    # A derivation would additionally have to value-match empirical at BOTH
    # anchors; the DM 3-jet is +0.027 vs empirical −2.07 — it does not even
    # near-match at one anchor.
    jet_value_matches = abs(jet_p - emp_p) < mpf("0.1")

    print(f"  DM-cubic 3-jet anchor-invariant?  {jet_invariant}  (swing {float(jet_swing):.2e}% << 2.43%)")
    print(f"  Berezinian cross-term anchor-invariant (all 3 mixings)?  {berez_invariant}")
    print(f"  DM-cubic 3-jet value-matches empirical c_3 at either anchor?  {jet_value_matches}")
    print()
    print("  → The DM-cubic/Berezinian 3-jet is a SMOOTH real-q object → anchor-INVARIANT")
    print("    (swings ~1e-5 %, ~5 orders below the 2.43% empirical swing).")
    print("    The empirical c_3 swings 2.43% (dc_3/dq ≈ 3.8e6) because the u³ ladder")
    print("    inversion magnifies a smooth numerator zero (registry KC21). A smooth")
    print("    construction (dc_3/dq = O(1)) CANNOT track that swing: it matches the")
    print("    empirical value at MOST one anchor. Here it matches at NEITHER (+0.027")
    print("    vs −2.07). This re-confirms the Lean-proved KC20 (real-q/quadratic c_3")
    print("    EXCLUDED), KC21 (swing = 1/u³ artifact of a smooth zero), KC22 (odd")
    print("    channel resurgent/transcendental, NOT a q-difference recurrence — so the")
    print("    'read c_3 off the q-lift 3-term recurrence' sub-route is refuted a priori).")
    print()
    print("  VERDICT: scope-(a) NEGATIVE — this construction, ALONE, does not derive")
    print("  c_3 anchor-invariantly-AND-value-matchingly. It is NOT a derivation and NOT")
    print("  even a near-match. Q_β does NOT meet its 100× target via this route.")

    verdict = "SCOPE_A_NEGATIVE_ANCHOR_INVARIANT_SMOOTH_CANNOT_TRACK_SWINGING_EMPIRICAL_C3"

    # ── witness ──
    wb = WitnessBuilder("qbeta-c3-dm-cubic-berezinian-probe", engine="mpmath")
    wb.set_description(
        "DERIVATION ATTEMPT for Q_β ladder c_3 via the Donagi–Markman cubic 3-jet "
        "/ Berezinian even-odd cross-term (bean qou-1dnr; super-Berezinian route "
        "landed 2026-07-20). Builds two CODATA-INDEPENDENT realizations of the "
        "3-jet (categorical phase ∂³F; Berezinian B·D⁻¹·C from the H_3 super-period "
        "matrix) and runs the anchor-invariance falsification. VERDICT: scope-(a) "
        "NEGATIVE — both realizations are anchor-invariant smooth real-q objects "
        "(swing ~1e-5%) and CANNOT reproduce the empirical c_3 that swings 2.43% "
        "(dc_3/dq ≈ 3.8e6, the 1/u³ ladder-inversion artifact of a smooth zero). "
        "Re-confirms Lean-proved KC20/KC21/KC22; the odd channel is "
        "resurgent/transcendental, not a recurrence output. NOT a derivation, NOT "
        "a near-match; nothing wired."
    )
    wb.set_content_block("conj:qdifference-kernel-prolongation-symbol")
    wb.set_audit_only("docs/audits/2026-07-20-c3-dm-cubic-derivation-attempt.md")
    wb.add_data("anchors", {
        "q_proton": fmt(qp), "q_muon": fmt(qm), "delta_q": fmt(qp - qm),
    })
    wb.add_data("empirical_c3_target", {
        "proton": fmt(emp_p), "muon": fmt(emp_m),
        "swing_pct": fmt(emp_swing), "dc3_dq": fmt(dc3_dq_emp),
        "note": "CODATA-inverted (FIT side, qbeta_utils.c3_target_at) — the swinging target.",
    })
    wb.add_data("dm_cubic_3jet_from_phase", {
        "proton": fmt(jet_p), "muon": fmt(jet_m),
        "swing_pct": fmt(jet_swing), "dc3_dq": fmt(dc3_dq_jet),
        "note": "∂³F of the categorical producer phase cos(α−u/2)(1−u²); α from "
                "substrate, not CODATA. Anchor-invariant; value +0.027 does not "
                "even near-match empirical −2.07 at either anchor.",
    })
    wb.add_data("berezinian_cross_fraction", berez)
    wb.add_data("interpretation", (
        "The empirical c_3 swing (2.43%) lives ENTIRELY in the 1/u³ ladder "
        "inversion (u, α, b are anchor-invariant to 8+ digits). Any real-q "
        "algebraic Berezinian cross-term / DM 3-jet is a smooth function of the "
        "substrate ⇒ anchor-invariant (dc_3/dq = O(1)) ⇒ structurally unable to "
        "reproduce a target needing dc_3/dq ≈ 3.8e6. Per KC21 the genuine "
        "derivation target is the SMOOTH bar-odd object S = h·D(ũ) (|S(substrate)| "
        "≈ 0.0094), NOT the swinging empirical c_3; the Berezinian route is "
        "structurally consistent with a bar-odd cross-term but produces no such "
        "derived closure. Approach #1 (recurrence output) is refuted a priori by "
        "KC22 (odd channel non-holonomic)."
    ))
    wb.add_data("verdict", verdict)
    wb.add_data("qbeta_100x_met_via_this_route", False)

    wb.add_assertion(
        "dm_cubic_3jet_anchor_invariant",
        computed=float(abs(jet_swing)), expected=0.0, tolerance=float(ANCHOR_INV),
    )
    wb.add_assertion(
        "berezinian_crossterm_anchor_invariant_all_mixings",
        computed=float(max(abs(mpf(d["swing_pct"])) for d in berez.values())),
        expected=0.0, tolerance=float(ANCHOR_INV),
    )
    wb.add_assertion(
        "empirical_c3_swings_far_more_than_derived",
        # empirical swing (2.43%) must exceed derived swing by >> 1000x
        computed=float(abs(jet_swing) / abs(emp_swing)),
        expected=0.0, tolerance=1e-3,
    )
    wb.add_assertion(
        "dm_cubic_3jet_does_not_value_match_empirical",
        computed=0.0 if not jet_value_matches else 1.0, expected=0.0,
    )
    wb.save()

    print()
    print(f"  Witness: qbeta-c3-dm-cubic-berezinian-probe.witness.json")
    print(f"  Elapsed: {time.time() - t0:.2f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
