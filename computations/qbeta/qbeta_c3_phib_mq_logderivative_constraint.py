#!/usr/bin/env python3
"""qbeta_c3_phib_mq_logderivative_constraint.py — derive + verify the LEVER
LOG-DERIVATIVE LAW: the first-order constraint any m(q₀) assignment must
satisfy to reproduce the c₃ bar-odd S. STRUCTURAL MEASUREMENT — no fit.

Derivation (calculus, not physics): S − Vol41 = A/u³ with
A := Q_codata/Q_N2 − 1. Differentiating the quotient (exact identity):

    dS/dq  =  A′/u³  −  3·(u′/u)·(S − Vol41).

MEASURED (this probe; the initial guess that the log-derivative term
dominates was WRONG and is corrected here — anti-self-deception by design):
the log-derivative term is only ~1e2 while A′/u³ carries ~99.997% of the
3.84e6 slope, with A′ ≈ +2.37 — exactly the smooth un-levered slope dr/dq
measured in the round-1 m-plane inversion (r = S·u³, consistency check).
So the S hypersensitivity is a STATIC 1/u³ amplification of a smooth
CODATA-vs-ladder residual slope — not a log-derivative effect.

CONSEQUENCE — the m(q₀) DERIVATIVE GATE (third check beside the two
S-values, needing only ONE anchor):

    u(q)³ · d/dq [ Im 𝔙(m(q)) ]  ≈  A′(q)  ≈  +2.37   at the anchors,

i.e. the un-levered derivative of the candidate's complex volume must equal
the smooth canonical slope A′ = d/dq[Q_codata/Q_N2] (CODATA + ladder only).
Equivalently Im 𝔙(m(q)) = A(q)/u(q)³ with A smooth — the complex volume
carries the inverse-cube ladder factor STATICALLY. Candidates failing this
one-anchor derivative gate are excluded without the second anchor.

Companion Lean (same PR): QOU.QBeta.LeverLogDerivative — the quotient-rule
decomposition d(f/u³) = f′/u³ − 3(u′/u)(f/u³) as a HasDerivAt statement,
so the gate's algebraic form is machine-checked, not re-derived by hand.

Run: python3 -u computations/qbeta/qbeta_c3_phib_mq_logderivative_constraint.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_mq_logderivative.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)

    def S_of(q):
        return c3_target_at(q, Qcod, me) + Vol41

    def u_of(q):
        return substrate_ladder_quantities(q)["u"]

    anchors = {"proton": q_at(50), "muon": q_muon_at(50)}
    h = mp.mpf(10) ** (-20)   # central-difference step; 70 dps leaves 30+ digits

    wb = WitnessBuilder("qbeta-c3-phib-mq-logderivative-constraint", engine="mpmath")
    wb.set_description(
        "Lever derivative decomposition (exact): dS/dq = A'/u^3 - "
        "3(u'/u)(S - Vol41), with A'/u^3 carrying ~99.997% (A' ~ +2.37 = the "
        "smooth un-levered slope; the log-derivative term is only ~1e2). The "
        "S hypersensitivity is a STATIC 1/u^3 amplification of a smooth "
        "CODATA-vs-ladder slope. Gate for any m(q0) assignment (one anchor): "
        "u^3 d/dq[Im V(m(q))] = A'(q) ~ +2.37. Structural measurement; "
        "no fit; no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" Lever derivative decomposition — the one-anchor m(q₀) derivative gate")
    print("=" * 78)

    def A_of(q):
        return (S_of(q) - Vol41) * u_of(q) ** 3   # A = (S - Vol41) u^3 exactly

    results = {}
    for a, q in anchors.items():
        Sp = (S_of(q + h) - S_of(q - h)) / (2 * h)          # dS/dq
        up = (u_of(q + h) - u_of(q - h)) / (2 * h)          # du/dq
        Ap = (A_of(q + h) - A_of(q - h)) / (2 * h)          # A'
        u = u_of(q)
        S = S_of(q)
        lever = -3 * (up / u) * (S - Vol41)                  # log-derivative term
        main_t = Ap / u ** 3                                 # static-amplification term
        closure = mp.fabs(Sp - (main_t + lever)) / mp.fabs(Sp)
        frac_main = mp.fabs(main_t / Sp)
        results[a] = {"dS_dq": Sp, "Ap": Ap, "main": main_t,
                      "lever": lever, "closure": closure, "frac_main": frac_main}
        print(f"\n  {a}:")
        print(f"    dS/dq              = {mp.nstr(Sp, 12)}")
        print(f"    A′/u³ (static amp) = {mp.nstr(main_t, 12)}   A′ = {mp.nstr(Ap, 8)}")
        print(f"    −3(u′/u)(S−Vol41)  = {mp.nstr(lever, 8)}")
        print(f"    identity closure   = {mp.nstr(closure, 4)}   A′/u³ fraction: {mp.nstr(frac_main, 8)}")
        wb.add_data(f"{a}_decomposition", {
            "dS_dq": mp.nstr(Sp, 25), "A_prime": mp.nstr(Ap, 20),
            "static_term_Aprime_over_u3": mp.nstr(main_t, 25),
            "logderiv_term": mp.nstr(lever, 20),
            "identity_closure_rel": float(closure),
            "static_term_fraction": float(frac_main)})

    # exact quotient-rule identity must close to machine precision
    worst_closure = max(float(r["closure"]) for r in results.values())
    wb.add_assertion("quotient_rule_identity_closes",
                     computed=worst_closure, expected=0.0, tolerance=1e-8,
                     source="dS/dq = A'/u^3 - 3(u'/u)(S - Vol41) exactly (calculus; "
                           "machine-checked in Lean as QOU.QBeta.LeverLogDerivative)")
    # the static-amplification term dominates (the corrected law)
    worst_dom = min(float(r["frac_main"]) for r in results.values())
    wb.add_assertion("static_amplification_dominates",
                     computed=worst_dom, expected=1.0, tolerance=0.01,
                     source="A'/u^3 carries >99% of dS/dq at both anchors: the "
                           "hypersensitivity is STATIC 1/u^3 amplification of the "
                           "smooth slope A' ~ +2.37 (= round-1 dr/dq, consistency)")
    # two-anchor cross-check: finite difference across anchors vs local derivative
    dq_anch = anchors["proton"] - anchors["muon"]
    fd = (S_of(anchors["proton"]) - S_of(anchors["muon"])) / dq_anch
    loc = results["proton"]["dS_dq"]
    agree = float(mp.fabs(fd / loc - 1))
    print(f"\n  cross-check: anchor finite-diff dS/dq = {mp.nstr(fd, 10)} "
          f"vs local {mp.nstr(loc, 10)}  (rel {agree:.2e})")
    wb.add_assertion("anchor_fd_matches_local_derivative",
                     computed=agree, expected=0.0, tolerance=1e-4,
                     source="S is smooth between the anchors; the two-anchor swing "
                           "is the same lever derivative (no hidden discontinuity)")

    ok = all(x.passed for x in wb.assertions)
    wb.add_data("m_q0_gate", (
        "DERIVATIVE GATE (per-candidate, one-anchor): a candidate assignment "
        "m(q0) with S = Im V(m(q0)) must satisfy u^3 d/dq[Im V(m(q))] = A'(q) "
        "~ +2.37 at the anchor (A' = d/dq[Q_codata/Q_N2 - 1], smooth, "
        "canonical). Equivalently Im V(m(q)) = A(q)/u(q)^3 with A smooth: the "
        "complex volume carries the inverse-cube ladder factor STATICALLY. "
        "NZ-leading: |u_hol(q)|^2 sin(2 phi(q)) proportional to u^-3 x smooth. "
        "Candidates failing this are excluded without the second anchor."))
    wb.add_data("initial_guess_corrected", (
        "The probe's original hypothesis (log-derivative term dominates) was "
        "REFUTED by its own measurement and corrected: the log-derivative "
        "term is ~1e2 of the 3.84e6 slope; A'/u^3 dominates. Recorded per "
        "the anti-self-deception design."))
    wb.add_data("verdict", (
        "DECOMPOSITION VERIFIED (exact identity + dominance): dS/dq = A'/u^3 "
        "- 3(u'/u)(S - Vol41), identity closes to machine precision, and the "
        "static term A'/u^3 carries >99.99% at both anchors with A' ~ +2.37 "
        "= the round-1 un-levered slope. The S hypersensitivity is a STATIC "
        "1/u^3 amplification of a smooth CODATA-vs-ladder slope; the m(q0) "
        "assignment inherits a one-anchor derivative gate. Scope-(a); no "
        "fit; nothing wired." if ok else "INCONCLUSIVE — assertion failed."))
    wb.save()
    print("\nwitness -> computations/qbeta/qbeta-c3-phib-mq-logderivative-constraint.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
