#!/usr/bin/env python3
"""delta_lambda_rK_closure_test.py — the Δ_λ closure check, pre-wired for R(q,x).

The three-piece test (`delta-lambda-three-piece-multiplicative.md`, PR #3040)
established the combination law: `B(K) = B_bulk(K) · R_eff(K)` with `B_bulk =
A·2·m_e·8G` (extensive, derived) and `R_eff(K)` the MULTIPLICATIVE per-nucleus
modulation a fibre kernel must supply, whose target profile is

    r(K) = B_AME(K) / B_bulk(K) :  D 0.15 · ⁴He 0.95 · ⁶Li 0.71 · ¹²C 1.03
                                 · ¹⁶O 1.07 · ⁴⁰Ca 1.14 · ⁵⁶Fe 1.17.

STATE OF R(q,x) (the z2bn Lever-1 fibre q-difference kernel): **not yet landed.**
It is the OPEN KEYSTONE — `z2bn_prolongation_qdifference_constraint.py` proves
(b)-exclusion that the λ_SW prolongation must be q-difference (not classical jet);
the single-element / contiguity form is refuted (#3009, #2985); the core `R_m(q)`
is characterized (Stage 8) — but the explicit operator that produces per-isotope
binding via `a_D^(n) = ∮ λ_SW^(n)` is flagged the open keystone
(`mba-step09b-per-isotope-binding.md`), with the anchors `a_D^(2)=1`,
`a_D^(3)=(q+1)²/(3q)`, `a_D^(4)=Family-A` still WIRED (a_D^(4) a CODATA near-match).

This harness is the **closure check, ready to consume R(q,x) the moment it lands**:
pass any candidate per-isotope modulation `R_eff(Z, N) -> float` to `check()`; it
reports the max/RMS deviation from r(K). The baseline below (`R_eff ≡ 1`, i.e.
extensive bulk alone) shows the gap the kernel must close. No fit: r(K) is a
measured target, R_eff is the object under test.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))

import mpmath as mp  # noqa: E402
from codata_constants import M_E_MEV as M_E  # noqa: E402

AME = [("D", 1, 1, 2.224573), ("4He", 2, 2, 28.295673), ("6Li", 3, 3, 31.994564),
       ("12C", 6, 6, 92.161728), ("16O", 8, 8, 127.619), ("40Ca", 20, 20, 342.052),
       ("56Fe", 26, 30, 492.254)]


def r_target():
    """The measured multiplicative target r(K) = B_AME / (A·2·m_e·8G)."""
    me = float(M_E); per_nuc = 2 * me * 8 * float(mp.catalan)
    return {nm: B / ((Z + N) * per_nuc) for nm, Z, N, B in AME}, per_nuc


def check(R_eff, label="candidate"):
    """Compare a candidate per-nucleus modulation R_eff(Z, N) -> float against
    the r(K) target. Returns (max_abs_dev, rms_dev, rows). Closure ⇒ max_dev ≈ 0."""
    rK, _ = r_target()
    rows, devs = [], []
    for nm, Z, N, _ in AME:
        re = float(R_eff(Z, N)); tgt = rK[nm]; d = re - tgt
        rows.append((nm, Z + N, tgt, re, d)); devs.append(d)
    mx = max(abs(d) for d in devs)
    rms = (sum(d * d for d in devs) / len(devs)) ** 0.5
    print(f"\n  [{label}]  R_eff vs r(K) target")
    print(f"  {'iso':5s}{'A':>3s}{'r(K) target':>13s}{'R_eff':>9s}{'Δ':>9s}")
    for nm, A, tgt, re, d in rows:
        print(f"  {nm:5s}{A:3d}{tgt:13.3f}{re:9.3f}{d:+9.3f}")
    print(f"  → max|Δ| = {mx:.3f}, RMS = {rms:.3f}  (closure ⇒ ≈ 0)")
    return mx, rms, rows


if __name__ == "__main__":
    rK, per_nuc = r_target()
    print(f"Δ_λ closure check (pre-wired for R(q,x), the open z2bn keystone).")
    print(f"target r(K) = B_AME/(A·2·m_e·8G),  2·m_e·8G = {per_nuc:.4f} MeV/nucleon")
    # BASELINE: extensive bulk alone (R_eff ≡ 1) — the gap the kernel must close.
    check(lambda Z, N: 1.0, label="baseline R_eff≡1 (extensive bulk alone)")
    print("\n  Awaiting R(q,x): when the z2bn q-difference prolongation lands and")
    print("  yields a per-isotope R_eff(K), pass it to check() for the closure test.")
    print("  Bridge spec: R(q,x) → a_D^(n)=∮λ_SW^(n) jet anchors → per-isotope")
    print("  binding (mba-step09b) → R_eff(K); must reproduce r(K) above.")
