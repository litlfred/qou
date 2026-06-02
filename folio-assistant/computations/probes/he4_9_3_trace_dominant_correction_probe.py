#!/usr/bin/env python3
"""he4_9_3_trace_dominant_correction_probe.py — does the (9,3)
trace-dominant channel carry the ⁴He +5.87% binding gap?

CONTEXT.
PR #1673 Probe 2 empirically refuted the "(4,4,4) PSD-dominant"
framing for tr_M(β_⁴He): (4,4,4)'s contribution is ≤ 4.28e-51.

`conj:psd-trace-orthogonality` (content/quantum-observable-universe/
mass-theory/conj-psd-trace-orthogonality.md) explicitly states the
SAME finding from the structural side:
  - (4,4,4) is PSD-dominant (LP-cone-obstruction-carrier)
  - (4,4,4) is NOT trace-dominant
  - The binding-energy gap lives in the trace-dominant family
    (2-row long-string partitions)
  - At A=4: top trace-dominant partitions are (10,2), (9,3), (11,1),
    (8,4), (7,5), (6,6), (12).

So the ⁴He +5.87% gap research direction must target the
trace-dominant channels, NOT the (4,4,4) PSD block.

This probe asks: what local correction at the (9,3) channel
(top single contributor at 29.09% of tr_M) would close the +5.87%
binding gap (ρ_F: 2 → 1.8892)?

PARAMETRIZATION. The magic-A formula is

    B(⁴He) = ρ_F · m_e · A · 8G                    [postulated ρ_F=2]

Suppose ρ_F is in fact decomposable over Wedderburn channels:

    ρ_F = Σ_λ w_λ · ρ_F^λ          with Σ w_λ = 1

with w_λ proportional to the (9,3)-dominant trace-weight pattern
y_λ · |χ^λ|. If only (9,3) carries a non-trivial ρ_F^λ correction
relative to 2, the required local correction is

    Δρ_F^(9,3) = (ρ_F_req - 2) / w_(9,3)

This probe computes Δρ_F^(9,3) at q_proton and asks:
  - Is Δρ_F^(9,3) a recognizable substrate quantity?
  - Cross-anchor: same Δρ_F^(9,3) at q_muon?

DISCIPLINE. PURE diagnostic — does NOT propose a new substrate
constant. The verdict is binary: either Δρ_F^(9,3) has a clean
structural form (then naming the categorical operator is the next
step) or it doesn't (and the gap distributes across multiple
channels, requiring a multi-channel ρ_F^λ analysis).
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

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

try:
    from qou_substrate.constants import q_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "he4-9-3-trace-dominant-correction-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "⁴He +5.87% binding gap localized to the (9,3) trace-dominant "
        "channel (per conj:psd-trace-orthogonality + PR #1673 Probe 2 "
        "reframing). Computes Δρ_F^(9,3) and reports structural pattern."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-xq-habiro-he4-9-3-yekutieli-a-workplan.md"
    )

    # Load H_12 chi cache
    cache_path = _pb.witness_path("chi-helium-4-h12-at-q0-50dps.witness.json", HERE)
    with open(cache_path) as f:
        cache = json.load(f)
    tr_M = mp.mpf(cache["tr_M_at_q0"])

    # Build trace-dominant ordered list with weights
    entries = []
    for p in cache["by_partition"]:
        part = tuple(p["partition"])
        y = mp.mpf(p["y_lambda"])
        chi = mp.mpf(p["chi_lambda"])
        contrib = y * chi
        entries.append({
            "partition": part,
            "dim": p["dim"],
            "y": y,
            "chi": chi,
            "contribution": contrib,
            "fraction": contrib / tr_M,
        })

    # Top trace-dominant by |contribution|
    entries_sorted = sorted(entries, key=lambda e: -abs(e["contribution"]))
    top = entries_sorted[:8]

    q = q_at()
    m_e = mp.mpf(str(M_E_MEV))
    A = 4
    G = mp.catalan
    rho_F_postulated = mp.mpf(2)
    B_AME = mp.mpf("28.295674")
    B_pred_postulated = rho_F_postulated * m_e * A * 8 * G
    rho_F_required = B_AME / (m_e * A * 8 * G)
    gap_rho_F = rho_F_postulated - rho_F_required
    gap_pct = gap_rho_F / rho_F_postulated * 100

    print("=" * 78)
    print(" ⁴He +5.87% gap — (9,3) trace-dominant channel correction probe")
    print("=" * 78)
    print(f"q_proton = {fmt(q)[:30]}")
    print(f"m_e = {m_e} MeV; A = {A}; 8G = {fmt(8 * G)[:18]}...")
    print(f"B_pred (ρ_F=2)      = {float(B_pred_postulated):.6f} MeV")
    print(f"B_AME              = {float(B_AME):.6f} MeV")
    print(f"required ρ_F       = {fmt(rho_F_required)[:25]}")
    print(f"gap (ρ_F)          = {fmt(gap_rho_F)[:18]} = {float(gap_pct):.4f}%")
    print()

    print(f"Top 8 trace-dominant partitions (from H_12 cache):")
    print(f"{'partition':<22}{'dim':>6}{'y_λ':>22}{'χ_λ(β_⁴He)':>22}{'frac of tr_M':>14}")
    print("-" * 100)
    for e in top:
        print(f"  {str(e['partition']):<20} {e['dim']:>5} "
              f"{float(e['y']):>22.6e} {float(e['chi']):>22.6e} "
              f"{float(e['fraction']) * 100:>13.4f}%")
    print()

    # Scenarios:
    #   (a) gap concentrated entirely in (9,3): Δρ_F^(9,3) = gap / frac_(9,3)
    #   (b) gap spread proportional to |contribution|: Δρ_F^λ = gap / 1
    #   (c) gap localized to top-3 trace-dominant: split equally
    print("=" * 78)
    print(" Δρ_F^λ scenarios — what correction localizes the +5.87% gap?")
    print("=" * 78)
    print()

    nine_three = next(e for e in entries if e["partition"] == (9, 3))
    nine_three_frac = nine_three["fraction"]

    print(f"(a) ALL gap concentrated in (9,3):")
    delta_rho_93 = gap_rho_F / nine_three_frac
    print(f"    Δρ_F^(9,3) = {fmt(gap_rho_F)[:14]} / {float(nine_three_frac):.6f}")
    print(f"               = {fmt(delta_rho_93)[:18]}")
    print()
    print(f"    Interpretation: at (9,3) the local ρ_F^(9,3) needs to be")
    print(f"    {fmt(rho_F_postulated - delta_rho_93)[:18]} instead of 2.")
    print()

    # (b) Σ |contrib| weighted (i.e. distribute Δ proportionally)
    sum_abs = sum(abs(e["contribution"]) for e in entries)
    print(f"(b) Spread proportional to |contribution| (sum|c|={float(sum_abs):.6e}):")
    print(f"    Each Δρ_F^λ ∝ |c_λ|/Σ|c| · gap_total = gap/A=4 ≈ {float(gap_rho_F/A):.6e}")
    print(f"    (trivial — this is just splitting gap uniformly across A=4)")
    print()

    # (c) only top-3: equal split
    top3_frac = sum(e["fraction"] for e in top[:3])
    print(f"(c) Localized to top 3 trace-dominant ({float(top3_frac)*100:.1f}% of tr_M):")
    delta_top3 = gap_rho_F / 3
    print(f"    Δρ_F^each = gap/3 = {float(delta_top3):.6e}")
    print()

    # Now ask: is delta_rho_93 a recognizable substrate quantity?
    print("=" * 78)
    print(" Δρ_F^(9,3) — substrate identification check")
    print("=" * 78)
    print()
    print(f"Δρ_F^(9,3) = {fmt(delta_rho_93)[:30]}")
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    G_val = mp.catalan
    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")

    candidates_str = [
        ("h²", h2),
        ("h", h),
        ("ℏ_q", hbar_q),
        ("ℏ_q²", hbar_q ** 2),
        ("α_em", alpha_em),
        ("α_em·G", alpha_em * G_val),
        ("h² · [2]_q", h2 * (q + 1 / q)),
        ("(q - q⁻¹)/3", h / 3),
        ("(q - 1)/(q + 1)", (q - 1) / (q + 1)),
        ("q⁻³", 1 / q ** 3),
        ("h² · q²", h2 * q ** 2),
        ("1 / [3]_q", 1 / (q ** 2 + 1 + 1 / q ** 2)),
    ]

    print(f"  {'candidate':<28} {'ratio Δρ/candidate':>22}")
    print("-" * 60)
    for name, val in candidates_str:
        ratio = delta_rho_93 / val
        print(f"  {name:<28} {float(ratio):>22.6f}")

    # PSLQ on delta_rho_93 in some natural basis
    print()
    print("PSLQ on Δρ_F^(9,3) in basis [1, h², ℏ_q², α_em, G·h², G·α_em]:")
    basis = [mp.mpf(1), h2, hbar_q ** 2, alpha_em, G_val * h2, G_val * alpha_em]
    rel = mp.pslq([delta_rho_93] + basis, tol=mp.mpf("1e-30"), maxcoeff=1000)
    if rel and rel[0] != 0:
        rhs_terms = []
        names = ["1", "h²", "ℏ_q²", "α_em", "G·h²", "G·α_em"]
        for i in range(1, len(rel)):
            if rel[i] != 0:
                rhs_terms.append(f"({-rel[i]}/{rel[0]})·{names[i-1]}")
        rhs = " + ".join(rhs_terms)
        check = sum(mp.mpf(rel[i]) * ([delta_rho_93] + basis)[i] for i in range(len(rel)))
        if abs(check) < mp.mpf("1e-28"):
            print(f"  ⭐ Δρ_F^(9,3) = {rhs}  (resid {float(abs(check)):.3e})")
        else:
            print(f"  pslq output: {rel} (residual {float(abs(check)):.3e}) — likely junk")
    else:
        print("  no PSLQ relation found at tol 1e-30, maxcoeff 1000")

    # Verdict
    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    verdict = (
        f"Localizing the +5.87% gap to the (9,3) trace-dominant channel "
        f"requires Δρ_F^(9,3) = {fmt(delta_rho_93)[:14]} (relative correction "
        f"{float(delta_rho_93 / 2 * 100):.2f}% of ρ_F=2). This is a "
        f"NUMERICAL LOCAL CORRECTION; the PSLQ search above tries to "
        f"identify it as a substrate combination. If no clean PSLQ hit: "
        f"the gap likely distributes across multiple channels (scenario b/c), "
        f"and the structural correction is NOT a single-block (9,3) feature. "
        f"The right next probe would then be the joint top-3 trace-dominant "
        f"channels ((10,2) + (9,3) + (11,1)) Δρ_F splitting analysis."
    )
    print(verdict)
    print()

    builder.add_data("q_proton", str(q))
    builder.add_data("m_e_MeV", str(m_e))
    builder.add_data("A", A)
    builder.add_data("B_AME_MeV", str(B_AME))
    builder.add_data("rho_F_postulated", float(rho_F_postulated))
    builder.add_data("rho_F_required", fmt(rho_F_required))
    builder.add_data("gap_rho_F", fmt(gap_rho_F))
    builder.add_data("gap_pct", float(gap_pct))
    builder.add_data("top_trace_dominant", [
        {
            "partition": list(e["partition"]),
            "dim": e["dim"],
            "y": float(e["y"]),
            "chi": float(e["chi"]),
            "fraction_of_tr_M": float(e["fraction"]),
        }
        for e in top
    ])
    builder.add_data("nine_three_fraction", float(nine_three_frac))
    builder.add_data("delta_rho_F_9_3_if_all_localized", fmt(delta_rho_93))
    builder.add_data("verdict", verdict)
    builder.add_data("framing_correction", (
        "PR #1673 Probe 2 + conj:psd-trace-orthogonality together say the "
        "binding-energy gap lives in the trace-dominant family, NOT the "
        "PSD-dominant (4,4,4) block. Research direction is re-aimed to "
        "the (9,3)/(8,4)/(10,2) channels."
    ))

    builder.add_assertion(
        name="trace_dominant_top_8_extracted",
        computed=len(top),
        expected=8,
        tolerance=0.0,
        source="Top 8 trace-dominant partitions from H_12 cache",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
