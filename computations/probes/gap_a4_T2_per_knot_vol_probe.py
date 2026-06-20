#!/usr/bin/env python3
"""GAP-A-4 T2 — per-knot Vol(K) convention probe.

Tests whether ANY of three plausible Vol(K) conventions collapses the
100× S(K)/m_e swing my T1 probe documented (PR #1886, merged).  Per
the cross-axis ledger ([`docs/coordination/gap-a-path-b-lambda.md`](../../docs/coordination/gap-a-path-b-lambda.md))
T1's negative pointed exactly at the Vol(K) convention question; this
probe attacks it directly.

For each light atom K ∈ {p, n, D, T, ³He, ⁴He}, computes:

  λ_emp(K) = m(K) · ℏ_q² / (m_e · Vol(K))

under THREE Vol conventions side-by-side:

  A — Phase-4 SnapPy JSJ values (current L1 convention):
        p/n = 8·G (Borromean); D/T = 12.776 (Z=1); ³He/⁴He = 12.554 (Z=2)
  B — Model B small-knot values
        (`build_six_term_substrate_model_b.py:MODEL_B_BRAID_REGISTRY`):
        p/n = 8·G (Borromean); D = 4.401 (Vol(6_2)); T = 8.286 (Vol(8_11));
        ³He = 8·G (Borromean); ⁴He = 4·8·G (magic-A L6a4_x4)
  C — Uniform Vol(𝓑₃) = 8·G for every atom (production
        `vol_density_borromean` convention)

The verdict for each convention is the **per-light-series swing**
of λ_emp(K).  A tight convention has small swing across atoms — the
empirical λ(K) becomes a near-constant when Vol(K) is "right".  A
wide swing means the convention picks up A-dependent structure that
doesn't factor into Vol.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T2-per-knot-vol-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
from codata_constants import M_D_MEV_VALIDATION, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_T_MEV_VALIDATION  # noqa: E402 (codata sweep)
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = "1.1099785955573347198997632204832250266562084087802"

# CODATA-2022 / AME-2020 masses (MeV) routed through the canonical
# registry (I9 — no hardcoded literals). See codata_constants.py.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as M_N_MEV,
    M_D_MEV_VALIDATION as M_D_MEV,
    M_T_MEV_VALIDATION as M_T_MEV,
    M_HE3_MEV_VALIDATION as M_HE3_MEV,
    M_HE4_MEV_VALIDATION as M_HE4_MEV,
)

# Small-knot volumes (50-dps from `substrate/knot_volumes.py`):
VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_6_2 = mp.mpf("4.40083251612304610144120386564092803398348541851650")
# VOL_8_11: literature anchor is only 13 digits (SnapPy HP, Adams 1985);
# the trailing zeros are PADDING to the 50-dps storage convention used by
# `substrate/knot_volumes.py`, not significant digits.  Sub-13-digit
# differences are below the source's precision floor.  Copilot review on
# PR #1891 caught the literal apparent over-precision.
VOL_8_11 = mp.mpf("8.28631681780659258810000000000000000000000000000000")

# Phase-4 SnapPy JSJ values (from `2026-05-19-delta-lambda-phase4-z4N-closure.md`):
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


# Vol(K) conventions per atom — three side-by-side mappings.
# Returns (label, vol_K_value_under_this_convention) tuples for each atom.

LIGHT_SERIES = [
    # (label, Z, N, m_K, conventions)
    ("p", 1, 0, M_P_MEV, {
        "A_phase4_jsj": VOL_BORROMEAN_8G,   # Phase-4 uses 8G for p/n too
        "B_model_b_small_knot": VOL_BORROMEAN_8G,  # Borromean
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
    ("n", 0, 1, M_N_MEV, {
        "A_phase4_jsj": VOL_BORROMEAN_8G,
        "B_model_b_small_knot": VOL_BORROMEAN_8G,
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
    ("D", 1, 1, M_D_MEV, {
        "A_phase4_jsj": VOL_PHASE4_Z1,
        "B_model_b_small_knot": VOL_6_2,
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
    ("T", 1, 2, M_T_MEV, {
        "A_phase4_jsj": VOL_PHASE4_Z1,
        "B_model_b_small_knot": VOL_8_11,
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
    ("3He", 2, 1, M_HE3_MEV, {
        "A_phase4_jsj": VOL_PHASE4_Z2,
        "B_model_b_small_knot": VOL_BORROMEAN_8G,  # Model B uses L6a4 for ³He
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
    ("4He", 2, 2, M_HE4_MEV, {
        "A_phase4_jsj": VOL_PHASE4_Z2,
        "B_model_b_small_knot": 4 * VOL_BORROMEAN_8G,  # magic-A L6a4_x4
        "C_uniform_borromean": VOL_BORROMEAN_8G,
    }),
]


def lambda_empirical(m_K: mp.mpf, vol_K: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    return m_K * hbar_q_sq(q_0) / (M_E_MEV * vol_K)


def per_series_swing(values: list[mp.mpf]) -> mp.mpf:
    """Max(values) / Min(values) − 1: the multiplicative spread of
    λ_emp across the light series.  A "good" convention has small swing."""
    pos_vals = [v for v in values if v > 0]
    if not pos_vals:
        return mp.mpf("inf")
    return max(pos_vals) / min(pos_vals) - 1


def main() -> int:
    w = WitnessBuilder("gap-a4-T2-per-knot-vol-probe", engine="mpmath")
    w.set_audit_only("docs/coordination/gap-a-path-b-lambda.md")
    w.set_description(
        "GAP-A-4 Task T2: per-knot Vol(K) convention probe.  Tests "
        "whether ANY of three Vol conventions (Phase-4 JSJ, Model B "
        "small-knot, uniform Borromean) collapses the 100× λ_emp(K) "
        "swing my T1 (PR #1886) documented.  No production touches; "
        "cross-axis with PR #1871's §4.B C2 task.  EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    # `linking_weight_family_a(q) = (3q²+4+3q⁻²)/4` is a trivial algebraic
    # expression — compute it directly in mpmath at the live working
    # precision rather than going through sympy substitution + string
    # round-trip (Copilot + Gemini reviews on PR #1891).
    lw_q0 = (3 * q_0 ** 2 + 4 + 3 * q_0 ** (-2)) / 4

    print("=" * 78)
    print("GAP-A-4 T2 — per-knot Vol(K) convention probe")
    print("=" * 78)
    print(f"  q₀                = {Q_0_50DPS[:18]}...")
    print(f"  λ_uniform (lw)    = {float(lw_q0):.6f}")
    print(f"  ℏ_q²              = {float(hbar_q_sq(q_0)):.10f}")

    conventions = ["A_phase4_jsj", "B_model_b_small_knot", "C_uniform_borromean"]

    # Per-atom λ_emp under each convention
    print()
    print(f"  {'atom':<4} {'Z':>2} {'N':>2} ", end="")
    for c in conventions:
        print(f"{'Vol_'+c[:1]:>14s} {'λ_emp_'+c[:1]:>14s} ", end="")
    print()
    print("-" * 100)

    rows = []
    lambdas_by_convention: dict[str, list[mp.mpf]] = {c: [] for c in conventions}
    for label, Z, N, m_K, conv_vols in LIGHT_SERIES:
        per_atom = {"label": label, "Z": Z, "N": N, "m_K_MeV": str(m_K)}
        print(f"  {label:<4} {Z:>2} {N:>2} ", end="")
        for c in conventions:
            vol = conv_vols[c]
            lam = lambda_empirical(m_K, vol, q_0)
            lambdas_by_convention[c].append(lam)
            per_atom[f"vol_{c}"] = str(vol)
            per_atom[f"lambda_emp_{c}"] = str(lam)
            print(f"{float(vol):>14.4f} {float(lam):>14.6f} ", end="")
        print()
        rows.append(per_atom)

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("lambda_uniform_at_q0", str(lw_q0))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("per_atom_per_convention", rows)

    # Per-convention swing (max/min − 1) — the verdict metric
    print()
    print("-" * 78)
    print(f"  {'convention':<26s} {'min(λ)':>10s} {'max(λ)':>10s} "
          f"{'max/min−1':>12s} {'verdict':>20s}")
    print("-" * 78)

    convention_verdicts = []
    for c in conventions:
        lams = lambdas_by_convention[c]
        min_lam = min(lams)
        max_lam = max(lams)
        swing = per_series_swing(lams)
        if abs(swing) < mp.mpf("5e-2"):
            verdict = "TIGHT (<5 % swing)"
        elif abs(swing) < mp.mpf("0.25"):
            verdict = "NEAR (<25 % swing)"
        else:
            verdict = "REFUTED (≥25 %)"
        convention_verdicts.append({
            "convention": c,
            "min_lambda": str(min_lam),
            "max_lambda": str(max_lam),
            "swing": str(swing),
            "verdict": verdict,
        })
        print(f"  {c:<26s} {float(min_lam):>10.4f} {float(max_lam):>10.4f} "
              f"{float(swing):>+12.2%} {verdict:>20s}")
    w.add_data("convention_verdicts", convention_verdicts)

    # Synthesis
    tight = [v for v in convention_verdicts if v["verdict"].startswith("TIGHT")]
    near = [v for v in convention_verdicts if v["verdict"].startswith("NEAR")]
    if tight:
        synthesis = (
            f"Convention(s) {[v['convention'] for v in tight]} give a "
            f"TIGHT λ_emp swing (<5 %) across the light series.  The "
            f"per-knot Vol(K) convention question is settled: λ_emp "
            f"approaches a near-constant when the right Vol(K) is "
            f"used.  Promote this convention to production after "
            f"reviewer sign-off; #1871's C2 task can extend "
            f"`knot_volumes.py` accordingly.  Per the 'fix as "
            f"numerology unless derivable' rule, also confirm the "
            f"convention is CATEGORICALLY derivable (not a fit) "
            f"before promotion."
        )
    elif near:
        synthesis = (
            f"Convention(s) {[v['convention'] for v in near]} give a "
            f"NEAR λ_emp swing (<25 %).  Better than the others but "
            f"still not a clean closure; suggests the per-knot Vol "
            f"alone doesn't capture all the per-(Z, N) structure.  "
            f"The remaining productive direction is T3 — derive "
            f"λ(K) from a Path-B-specific formulation, not a "
            f"Phase-4 transplant."
        )
    else:
        # Format the swing as a clean percentage rather than dumping the
        # 70-digit mp.mpf string (Gemini review on PR #1891).
        swing_summary = ", ".join(
            f"{v['convention']}: {float(mp.mpf(v['swing'])):.2%}"
            for v in convention_verdicts
        )
        synthesis = (
            f"All three Vol conventions give wide λ_emp swings "
            f"(>25 %): {swing_summary}. "
            f"T2 closes NEGATIVE — no plausible Vol(K) convention "
            f"alone collapses the 100× S(K) swing my T1 documented.  "
            f"The Path B λ(K) is not just a Vol-convention artifact; "
            f"the productive direction shifts firmly to T3 — derive "
            f"λ(K) from a Path-B-specific formulation."
        )
    w.add_data("synthesis_verdict", synthesis)
    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Sanity assertion: proton row reproduces λ_emp(p) ≈ 2.46 under
    # conventions A/B/C (all use Vol(𝓑₃) = 8G for the proton).
    proton = rows[0]
    assert proton["label"] == "p"
    lam_p_A = mp.mpf(proton["lambda_emp_A_phase4_jsj"])
    w.add_assertion(
        "proton_lambda_emp_matches_documented_value",
        computed=float(lam_p_A),
        expected=2.460,
        tolerance=2e-3,
        source=(
            "Proton's λ_emp ≈ 2.46 (the CODATA-implied near-match in "
            "_li_2_q_util.py::vol_density_borromean docstring).  Anchors "
            "the probe — proton row is the proton row regardless of "
            "convention since all three use Vol(𝓑₃) = 8G for p."
        ),
    )

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
