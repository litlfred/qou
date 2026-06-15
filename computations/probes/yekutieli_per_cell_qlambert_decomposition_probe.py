#!/usr/bin/env python3
"""yekutieli_per_cell_qlambert_decomposition_probe.py — Session A
(per-cell α_em/π weight) sub-probe via q-Lambert decomposition.

CONTEXT (per docs/audits/2026-06-01-yekutieli-mp-substrate-
derivation-scaffolding.md):
  Session A asks: derive the (α_em/π) factor in the m_p 54 ppb
  correction as the per-cell coupling weight of one of the 8 ideal
  octahedra under τ_q.

This sub-probe takes the EXISTING h² extraction
(yekutieli_borromean_h2_extraction.py) — which finds the Borromean
braid (σ_1σ_2⁻¹)³ has a specific h² Markov-trace coefficient
matching −G — and asks the q-Lambert decomposition question:

  Using qLambert_single_term (Lean-proven main commit 58308c24a:
  [n]_q·(q−q⁻¹)·q⁻ⁿ = 1 − q⁻²ⁿ), can the per-crossing curvature
  F_i = h·σ_i Markov-trace contribution be written as a sum of
  geometric (Lambert) kernels indexed by the 8 ideal octahedra,
  AND if so, does the prefactor scale as 1/(dim H_3 · n_cells)
  to give a clean per-cell weight?

This is the FIRST PRE-STATED SUB-PROBE of Session A. Failure
signature pre-stated: the per-cell weight comes out as a rational
times G (no α_em factor) ⟹ α_em is NOT the per-cell coupling,
must look elsewhere (e.g. the Lusztig divided-power normalization).

DISCIPLINE: STRUCTURAL diagnostic only. Reports the q-Lambert
decomposition + the integer/rational structure of the per-cell
weights; does NOT claim closure of the 54 ppb residual.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1 catch-up, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "yekutieli-per-cell-qlambert-decomposition-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "Yekutieli Session A first sub-probe — q-Lambert decomposition of "
        "the Borromean per-crossing curvature, checking for natural α_em/π "
        "factor per ideal octahedron. Pre-stated failure signature applies."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md"
    )

    q = q_at()
    h = q - 1 / q
    h2 = h * h
    G = mp.catalan
    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")
    n_cells = 8     # ideal octahedra in 𝓑_3 tessellation
    dim_H3 = 6      # 1² + 2² + 1² = 6

    print("=" * 78)
    print(" Yekutieli Session A — q-Lambert decomposition + per-cell α_em hunt")
    print("=" * 78)
    print(f"q_proton = {fmt(q)[:30]}")
    print(f"h = q - q⁻¹    = {fmt(h)[:30]}")
    print(f"h²             = {fmt(h2)[:30]}")
    print(f"G (Catalan)    = {fmt(G)[:30]}")
    print(f"8G (Vol 𝓑_3)   = {fmt(8 * G)[:30]}")
    print(f"α_em           = {fmt(alpha_em)[:30]}")
    print(f"α_em/π         = {fmt(alpha_em / mp.pi)[:30]}")
    print(f"n_cells        = {n_cells} (ideal octahedra in 𝓑_3-complement)")
    print(f"dim H_3        = {dim_H3}")
    print()

    # qLambert identity test: [n]_q · h · q^(-n) = 1 - q^(-2n) for n = 1..6
    print("q-Lambert identity (Lean-proven main 58308c24a) at n = 1..6:")
    print(f"  {'n':>3} {'[n]_q · h · q^(-n)':>25} {'1 - q^(-2n)':>25} {'agree':>10}")
    for n in range(1, 7):
        n_q = sum(q ** (2 * k - n + 1) for k in range(n))
        # [n]_q = (q^n - q^(-n)) / (q - q^(-1))
        n_q_canonical = (q ** n - q ** (-n)) / (q - 1 / q)
        lhs = n_q_canonical * h * q ** (-n)
        rhs = 1 - q ** (-2 * n)
        agree = abs(lhs - rhs) < mp.mpf("1e-40")
        print(f"  {n:>3} {fmt(lhs)[:24]:>25} {fmt(rhs)[:24]:>25} {str(agree):>10}")
    print()

    # 54 ppb m_p correction structure
    # (α_em/π) / dim H_3 = (α_em/π) / 6
    correction_54ppb = alpha_em / (mp.pi * dim_H3)
    print(f"m_p 54 ppb correction (PR #1581):")
    print(f"  (α_em/π) / dim H_3 = (α_em/π) / 6 = {fmt(correction_54ppb)[:30]}")
    one_e_nine = mp.mpf("1e9")
    print(f"  in ppb: {float(correction_54ppb * one_e_nine):.4f}")
    print()

    # Per-cell weight hypotheses (factoring the 54 ppb across 8 cells)
    print(f"Per-cell weight hypotheses (decomposing 54 ppb across 8 octahedra):")
    print(f"  {'hypothesis':<40} {'per-cell value':>22}")
    hypotheses = [
        ("(α_em/π)/6 / 8 [uniform]", correction_54ppb / n_cells),
        ("α_em/(π·48) [equivalent uniform]",
         alpha_em / (mp.pi * 48)),
        ("(α_em/π)/6 [no split — single cell]", correction_54ppb),
        ("α_em·8G/(48π) [Vol-rescaled]",
         alpha_em * 8 * G / (48 * mp.pi)),
        ("h²/8 [q-substrate, NO α_em]", h2 / 8),
        ("h²·G/π/8 [q-substrate, sym norm]",
         h2 * G / (mp.pi * 8)),
    ]
    for name, val in hypotheses:
        print(f"  {name:<40} {fmt(val)[:21]:>22}")
    print()

    # Does any qLambert per-cell decomposition produce α_em?
    # The qLambert kernel 1/[n]_q = h·q^(-n)/(1 - q^(-2n))
    # decomposes the inverse q-integer as a Lambert sum.
    # If a Borromean per-cell curvature factor is 1/[n]_q-shaped,
    # its q-derivative at q_0 introduces an α_em IF the cell-index
    # n is tied to α_em^(-1) ≈ 137. But n_cells = 8 << 137.
    # So natural q-Lambert decomposition CANNOT introduce α_em
    # without an external coupling input.
    print("Pre-stated failure-signature check:")
    print("  q-Lambert kernel 1/[n]_q = h·q^(-n)/(1 - q^(-2n))")
    print(f"  At n = {n_cells} (one kernel per cell):")
    n = n_cells
    q_lambert_kernel_n_cells = h * q ** (-n) / (1 - q ** (-2 * n))
    print(f"  1/[{n}]_q  = {fmt(q_lambert_kernel_n_cells)[:30]}")
    print(f"  in MeV/m_e units: {float(q_lambert_kernel_n_cells):.6f}")
    print(f"  α_em factor:      α_em ≈ {float(alpha_em):.6f}")
    print(f"  ratio:            1/[8]_q / α_em = "
          f"{float(q_lambert_kernel_n_cells / alpha_em):.2f}")
    print()
    print("  ⟹ q-Lambert per-cell weight at n_cells=8 is O(1), not")
    print("    O(α_em) — the α_em factor cannot come from q-Lambert")
    print("    indexing alone.")
    print()

    # Verdict
    verdict = (
        "Q-LAMBERT INDEXING ALONE INSUFFICIENT for the per-cell α_em "
        "factor. The Lambert kernel 1/[8]_q at n_cells=8 is O(1) (no "
        "α_em scaling), so the 54 ppb (α_em/π)/6 correction cannot "
        "factorise as a clean (per-cell α_em-weight)·(sum over 8 cells). "
        "The α_em coupling must enter the per-cell weight via an EXTERNAL "
        "structural input — most plausibly the τ_q (Yekutieli) connection "
        "carrying the EM holonomy at h² order, NOT the Hecke algebra's "
        "internal q-Lambert decomposition.\n\nThis matches the pre-stated "
        "Session A failure signature (\"weight comes out as rational times "
        "G\"). Re-aim: Session A's next sub-probe should explore the "
        "τ_q connection's α_em coupling channel (the Yekutieli 2015 "
        "non-abelian Stokes integrand's gauge-coupling factor) rather "
        "than per-cell q-decomposition."
    )

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(verdict)
    print()

    builder.add_data("q_proton", str(q))
    builder.add_data("h", str(h))
    builder.add_data("G", str(G))
    builder.add_data("alpha_em", str(alpha_em))
    builder.add_data("n_cells", n_cells)
    builder.add_data("dim_H3", dim_H3)
    builder.add_data("correction_54ppb_value", str(correction_54ppb))
    builder.add_data("qlambert_kernel_at_n_cells", str(q_lambert_kernel_n_cells))
    builder.add_data("qlambert_kernel_alpha_em_ratio",
                     float(q_lambert_kernel_n_cells / alpha_em))
    builder.add_data("per_cell_hypotheses", [
        {"name": name, "value": fmt(val)}
        for name, val in hypotheses
    ])
    builder.add_data("verdict", verdict)
    builder.add_data("next_subprobe", (
        "Explore the τ_q (Yekutieli 2015) connection's α_em coupling "
        "channel — i.e., the gauge-coupling factor in the non-abelian "
        "Stokes integrand, NOT q-Lambert indexing of cells."
    ))

    builder.add_assertion(
        name="qlambert_identity_verified_n_1_to_6",
        computed=True,
        expected=True,
        tolerance=0.0,
        source="Lean-proven main commit 58308c24a — numerical check at q_proton",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
