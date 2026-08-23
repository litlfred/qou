#!/usr/bin/env python3
"""
T6 gap (c) probes — identify structural source of the 3/2 factor.

Per docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md:
the canonical Li_2^q per-braid mass tower applied to muon T(2,5) via the
H_3 3-channel V̂ gives m_μ/m_e ratio = 1.36, vs CODATA 206.77.

  Required factor = 206.77 / 1.36 = 152.04
  1/ℏ_q²          = 101.86  (SUPERSEDED ρ_q at q_0)
  Ratio           = 152.04 / 101.86 ≈ 1.493 ≈ 3/2

This script tests ~20 candidate closed-form expressions for the
required factor at 50-dps precision to identify the structural
source (if any).

Probes:
  (1) Pure 3/2 (rational)
  (2) Wedderburn weight ratios W_STD / (W_SYM + W_ALT), etc.
  (3) q-integer / q-bracket ratios
  (4) Trigonometric / hyperbolic candidates
  (5) Branching coefficients A^λ_{μν} candidates per
      prop:hecke-branching-trace-decomposition
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def main() -> int:
    set_compute_dps()

    # Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 53 digits, correct to 19 (qou-ckbv)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    cal2_target = M_MU_OVER_M_E
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    qi = 1 / q0
    h = q0 - qi
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    two_q = q0 + qi
    three_q = q0**2 + 1 + qi**2
    qfac_3 = two_q * three_q
    W_SYM = mp.mpf(1) / qfac_3
    W_STD = two_q * two_q / qfac_3
    W_ALT = mp.mpf(1) / qfac_3

    # Recompute V̂_μ_T(2,5) exactly via H_3 3-channel formula
    # σ_1^5: hecke_ab recursion
    a, b = mp.mpf(0), mp.mpf(1)
    for _ in range(5):
        a, b = a * h + b, a
    # σ_1^5 = a σ_1 + b
    chi_sym_5 = q0**5
    chi_alt_5 = (-qi)**5
    std_markov_5 = z * a + b
    V_mu = W_SYM * chi_sym_5 + W_STD * std_markov_5 + W_ALT * chi_alt_5

    # Electron σ_1^3
    a3, b3 = mp.mpf(0), mp.mpf(1)
    for _ in range(3):
        a3, b3 = a3 * h + b3, a3
    chi_sym_3 = q0**3
    chi_alt_3 = (-qi)**3
    std_markov_3 = z * a3 + b3
    V_e = W_SYM * chi_sym_3 + W_STD * std_markov_3 + W_ALT * chi_alt_3

    # Li_2^q for single-gen (descended-dropped Li_2^q canonical convention)
    def li2q(z_arg, max_terms=500):
        s = mp.mpf(0)
        for n in range(1, max_terms + 1):
            qint = (q0**n - q0**(-n)) / h
            t = z_arg**n / (n * qint)
            s += t
            if mp.fabs(t) < mp.mpf(10)**(-50):
                break
        return s

    m_e = -li2q(-mp.fabs(V_e))
    m_mu = -li2q(-mp.fabs(V_mu))
    ratio_computed = m_mu / m_e

    required_factor = cal2_target / ratio_computed
    bare_dim = mp.mpf(1) / hbar_q_sq

    print(f"=== Substrate ===")
    print(f"  q_0 = {float(q0):.16f}")
    print(f"  V̂_e = {float(V_e):.10f}")
    print(f"  V̂_μ_T(2,5) = {float(V_mu):.10f}")
    print(f"  m_e_dim (Li_2^q) = {float(m_e):.10f}")
    print(f"  m_μ_dim (Li_2^q) = {float(m_mu):.10f}")
    print(f"  ratio computed = {float(ratio_computed):.10f}")
    print(f"  CODATA m_μ/m_e = {float(cal2_target):.10f}")
    print(f"  required_factor = CODATA / ratio = {float(required_factor):.10f}")
    print(f"  1/ℏ_q² = {float(bare_dim):.10f}")
    print(f"  RATIO factor/bare_dim = {float(required_factor / bare_dim):.10f}")
    print()
    print("=== Candidate matches for ratio (factor/bare_dim ≈ 1.493) ===")

    target = required_factor / bare_dim
    candidates = [
        ("3/2 (pure rational)", mp.mpf(3) / 2),
        ("(3+h²)/(2+h²)", (3 + h**2) / (2 + h**2)),
        ("(3+h²)/2", (3 + h**2) / 2),
        ("[3]_q/[2]_q", three_q / two_q),
        ("[3]_q/(2[2]_q)", three_q / (2 * two_q)),
        ("(2z²+1)", 2 * z**2 + 1),
        ("(z+1)", z + 1),
        ("1 + cosh(η) - sinh(η)", 1 + mp.cosh(mp.log(q0)) - mp.sinh(mp.log(q0))),
        ("(q+q⁻¹+1)/2", (q0 + qi + 1) / 2),
        ("W_STD/(W_SYM+W_ALT)", W_STD / (W_SYM + W_ALT)),
        ("1+W_STD", 1 + W_STD),
        ("(1+W_STD)/2 + 1", (1 + W_STD) / 2 + 1),
        ("[2]_q · z² + 1", two_q * z**2 + 1),
        ("cosh(η)", mp.cosh(mp.log(q0))),
        ("cosh(η) · [2]_q / z", mp.cosh(mp.log(q0)) * two_q / z),
        ("q+1 / (q⁻¹+1)", (q0 + 1) / (qi + 1)),
        ("(q²+1)/q", (q0**2 + 1) / q0),
        ("1 + h", 1 + h),
        ("1 + h/2 · [3]_q/[2]_q", 1 + h/2 * three_q/two_q),
        ("(2[3]_q - [2]_q²)/[2]_q", (2*three_q - two_q**2)/two_q),
        ("[3]_q · z", three_q * z),
        ("(3 + h)/2", (3 + h) / 2),
        ("(3 - h)/2", (3 - h) / 2),
        ("(q^3+q^{-3})/(q+q^{-1})", (q0**3 + qi**3)/(q0 + qi)),
        ("(q^3-q^{-3})/(q-q^{-1})", (q0**3 - qi**3)/(q0 - qi)),
        # ↑ this is [3]_q itself
        ("Σ W (3 channels)", W_SYM + W_STD + W_ALT),
        ("3 · max(W) = 3 · W_STD", 3 * W_STD),
    ]

    print(f"{'candidate':50s}  {'value':>14s}  {'diff %':>10s}  {'match?':>7s}")
    print("-" * 88)
    matches_1pct = []
    matches_0p1pct = []
    matches_0p01pct = []
    for name, val in candidates:
        diff = (val - target) / target * 100
        tag = ""
        if mp.fabs(diff) < mp.mpf("0.01"):
            tag = "✓✓✓ 0.01%"
            matches_0p01pct.append((name, val))
        elif mp.fabs(diff) < mp.mpf("0.1"):
            tag = "✓✓ 0.1%"
            matches_0p1pct.append((name, val))
        elif mp.fabs(diff) < mp.mpf("1"):
            tag = "✓ 1%"
            matches_1pct.append((name, val))
        else:
            tag = "—"
        print(f"  {name:48s}  {float(val):14.8f}  {float(diff):+9.4f}%  {tag:>7s}")
    print()
    print(f"  Target value: {float(target):.10f}")
    print()

    # Probe (3) — Hecke branching coefficient A^λ_{μν}(I)
    # For H_3, the Littlewood-Richardson coefficients c^{λ}_{μν}
    # for partitions of 3 = 2+1 = 1+1+1 = 3 (and 2 + 1 splits):
    # The branching from H_3 to H_2 × H_1 reduces (3) → (2)·(1) + (1,1)·(1)
    # and the standard 2D irrep (2,1) → (2)·(1) + (1,1)·(1)
    # A^λ_{μν}(I) involves these branching multiplicities
    # weighted by Hoefsmit basis intertwiner factors.
    #
    # For lepton mass formula, the relevant A^λ_{μν} coefficient
    # would couple H_3 (electron's 3-channel basis at the
    # convention level) to H_2 (electron's natural braid).
    # The H_3 → H_2 × H_1 branching for standard rep (2,1):
    # std(H_3) → sym(H_2) ⊕ alt(H_2) in some normalization.

    print("=== Probe (3): branching coefficient candidates A^λ_{μν} ===")
    # H_3 → H_2 × H_1 branching multiplicities
    # (3) → (2): 1
    # (2,1) → (2): 1, (2,1) → (1,1): 1
    # (1,1,1) → (1,1): 1
    branching_candidates = [
        ("(2,1) → sym + alt branching", mp.mpf(2)),  # 2 sub-irreps
        ("std rank / sum 1D ranks = 2/(1+1)", mp.mpf(2) / 2),
        ("(3 channels) / 2 chiralities", mp.mpf(3) / 2),
        ("3 sheets / 2 (s_3 → s_2 fold)", mp.mpf(3) / 2),
        ("|S_3|/|S_2| × (1/2)", mp.mpf(6) / 2 / 2),
        ("3!/(2·2!) = 3/2", mp.mpf(6) / (2 * 2)),
        ("dim H_3 / dim H_2 / 2 = 6/2/2", mp.mpf(6) / 2 / 2),
        ("3·z·[2]_q / [3]_q", 3 * z * two_q / three_q),
        ("LR coeff c^{(2,1)}_{(2),(1)}", mp.mpf(1)),  # standard LR coefficient
        ("LR coeff c^{(3)}_{(2),(1)} + c^{(3)}_{(1,1),(1)}", mp.mpf(2)),  # speculative
    ]
    print(f"{'branching candidate':50s}  {'value':>14s}  {'diff %':>10s}  {'match?':>7s}")
    print("-" * 88)
    for name, val in branching_candidates:
        diff = (val - target) / target * 100
        tag = ""
        if mp.fabs(diff) < mp.mpf("0.5"):
            tag = "✓ <0.5%"
        else:
            tag = "—"
        print(f"  {name:48s}  {float(val):14.8f}  {float(diff):+9.4f}%  {tag:>7s}")
    print()

    # Witness
    witness = {
        "description": "T6 gap (c) — try all candidates for the 3/2 factor structural source",
        "computation": "t6_three_halves_factor_probes",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "source_audit": "docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z": str(z),
            "Vol_4_1": str(Vol_4_1),
            "hbar_q_sq": str(hbar_q_sq),
            "V_e_h3_3channel": str(V_e),
            "V_mu_T25_h3_3channel": str(V_mu),
            "m_e_li2q": str(m_e),
            "m_mu_li2q": str(m_mu),
            "ratio_computed": str(ratio_computed),
            "codata_m_mu_over_m_e": str(cal2_target),
            "required_factor_total": str(required_factor),
            "inv_hbar_q_sq": str(bare_dim),
            "ratio_factor_over_bare_dim": str(target),
        },
        "candidate_matches": {
            "within_0.01_percent": [(n, str(v)) for n, v in matches_0p01pct],
            "within_0.1_percent": [(n, str(v)) for n, v in matches_0p1pct],
            "within_1_percent": [(n, str(v)) for n, v in matches_1pct],
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    here = Path(__file__).resolve().parent
    out = here / "t6-three-halves-factor-probes.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
