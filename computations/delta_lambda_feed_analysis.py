#!/usr/bin/env python3
"""Δ_λ feed analysis — per-Wedderburn-block contributions vs AME binding.

EXPLORATORY (production-vs-exploratory discipline: no production wiring;
this CHARACTERIZES the Δ_λ gate, it does not propose a closure).

Reads the v2 Wedderburn-spectral witness
(`all-nuclides-wedderburn-spectral-v2.witness.json`) and quantifies the
relationship between the per-block contributions y_λ·χ_λ(a) and the AME
binding energy B(A,Z), to FEED the Δ_λ gate

    B(K) = m_e · Σ_λ y_λ χ^λ(β_K) Δ_λ(K).

KEY FINDING (a refutation + structural characterization — NOT a seventh
fit ansatz, which AGENTS.md's Δ_λ-gate note forbids):

  log10|tr_M(a)| grows QUADRATICALLY in A (R² ≈ 0.9999) because the atom
  crossing count is T = 11A + A(A−1)/2 + Z ≈ A²/2, so every Wedderburn
  character χ_λ(a) ~ q^T blows up super-exponentially (|tr_M| reaches
  ~10^1025 at the heavy end), while binding B is ~LINEAR in A
  (B/A ∈ 0.02–8.8 MeV, log10 B ≤ 3.3).

  Consequence: NO per-partition CONSTANT Δ_λ can satisfy the formula —
  the required Δ_λ(K) = B / (m_e · y_λ · χ_λ(a)) must itself DECAY like
  10^(−c·A²).  This is exactly why the six tabulated constant/structural
  Δ_λ ansätze fail on heavy nuclei, and it pins what Δ_λ must structurally
  BE: a per-nucleus exponential normalization in the crossing count —
  i.e. an inverse-hyperbolic-volume / packing-density factor, consistent
  with the rho_F · V_hyp binding law (`rem:frobenius-packing-density`),
  NOT a Wedderburn-block constant.

Output: delta-lambda-feed-analysis.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "substrate"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV as _M_E_MEV  # noqa: E402  canonical registry (P31)

M_E_MEV = float(_M_E_MEV)  # registry value is mpf; this analysis is float/numpy
HERE = Path(__file__).parent
V2 = HERE / "all-nuclides-wedderburn-spectral-v2.witness.json"


def r2(y, pred):
    y = np.asarray(y, float)
    return float(1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2))


def main() -> int:
    t0 = time.monotonic()
    src = json.loads(V2.read_text())
    rows_in = src["data"]["rows"]
    yw = src["data"]["markov_weights_y_lambda"]
    import mpmath as mp
    mp.mp.dps = 30
    # only the alt-channel weight enters the dominant-channel Δ scale.
    log_y_alt = float(mp.log10(abs(mp.mpf(yw["(1,1,1)"]))))

    r = [x for x in rows_in if x["A"] >= 2 and x["B_AME_MeV"] > 0]
    A = np.array([x["A"] for x in r], float)
    T = np.array([x["T_crossings"] for x in r], float)
    B = np.array([x["B_AME_MeV"] for x in r], float)
    trL = np.array([x["trM_log10"] for x in r], float)   # log10|tr_M(a)|
    altL = np.array([x["alt_log10"] for x in r], float)   # log10|χ_alt(a)|

    # ── (1) quadratic crossing-count law for log10|tr_M| ──────────────
    Xq = np.vstack([A * A, A, np.ones_like(A)]).T
    cq, *_ = np.linalg.lstsq(Xq, trL, rcond=None)
    r2_quad = r2(trL, Xq @ cq)
    Xl = np.vstack([A, np.ones_like(A)]).T
    cl, *_ = np.linalg.lstsq(Xl, trL, rcond=None)
    r2_lin = r2(trL, Xl @ cl)
    # tr_M tracks the crossing count T directly:
    r2_T = float(np.corrcoef(trL, T)[0, 1] ** 2)

    # ── (2) binding is linear in A (the famous curve) ─────────────────
    cB, *_ = np.linalg.lstsq(Xl, B, rcond=None)
    r2_B_lin = r2(B, Xl @ cB)
    BperA = B / A
    corr_BperA_trL = float(np.corrcoef(BperA, trL)[0, 1])

    # ── (3) required Δ_λ(K): log10|Δ_λ| = log10(B/m_e) − log10|y_λ χ_λ| ─
    # alt block dominates |tr_M|, so use it as the representative channel.
    logB_over_me = np.log10(B / M_E_MEV)
    logDelta_alt = logB_over_me - (log_y_alt + altL)
    # If Δ_alt were a CONSTANT it would have ~zero spread; measure spread
    # and its A-dependence.
    cD, *_ = np.linalg.lstsq(Xq, logDelta_alt, rcond=None)
    r2_Delta_quad = r2(logDelta_alt, Xq @ cD)

    # ── (4) per-block FEED table (the Δ_λ-derivation input) ───────────
    # signed log10 contributions log10|y_λ χ_λ| with sign, per nucleus.
    feed_sample = []
    for x in [y for y in r if (y["Z"], y["N"]) in
              {(2, 2), (6, 6), (8, 8), (20, 20), (26, 30), (82, 126)}]:
        feed_sample.append({
            "ZN": [x["Z"], x["N"]], "A": x["A"], "B_MeV": x["B_AME_MeV"],
            "log10_chi_sym": x["sym_log10"], "log10_chi_alt": x["alt_log10"],
            "log10_absTrM": x["trM_log10"],
            "log10_required_Delta_alt": round(
                float(np.log10(x["B_AME_MeV"] / M_E_MEV)
                      - (log_y_alt + x["alt_log10"])), 3),
        })

    w = WitnessBuilder("delta-lambda-feed-analysis", engine="python",
                       start_time=t0)
    w.set_description(
        "Δ_λ feed analysis (EXPLORATORY): characterizes why a per-partition "
        "constant Δ_λ cannot close B = m_e Σ_λ y_λ χ_λ Δ_λ. log10|tr_M(a)| "
        "is quadratic in A (crossings T≈A²/2) → χ_λ blow up while B is "
        "linear, so the required Δ_λ(K) must decay ~10^(−cA²). Refutation + "
        "structural characterization, not a closure ansatz."
    )
    w.add_data("n_nuclei", len(r))
    w.add_data("trM_log10_vs_A", {
        "quadratic_fit_aA2_bA_c": [float(v) for v in cq],
        "R2_quadratic": round(r2_quad, 6),
        "R2_linear_only": round(r2_lin, 6),
        "R2_vs_crossing_count_T": round(r2_T, 6),
        "trM_log10_max": float(trL.max()),
    })
    w.add_data("binding_vs_A", {
        "linear_fit_mA_c": [float(v) for v in cB],
        "R2_linear": round(r2_B_lin, 6),
        "B_per_A_range_MeV": [float(BperA.min()), float(BperA.max())],
        "corr_BperA_vs_log10TrM": round(corr_BperA_trL, 4),
        "log10_B_max": float(np.log10(B).max()),
    })
    w.add_data("required_Delta_alt", {
        "is_constant": False,
        "log10_range": [float(logDelta_alt.min()), float(logDelta_alt.max())],
        "orders_of_magnitude_spread": round(
            float(logDelta_alt.max() - logDelta_alt.min()), 1),
        "quadratic_in_A_fit_aA2_bA_c": [float(v) for v in cD],
        "R2_quadratic": round(r2_Delta_quad, 6),
        "interpretation": (
            "required Δ_alt(K) spans ~%d orders of magnitude and is "
            "quadratic in A (R²=%.4f) — a constant Δ_λ is refuted; Δ_λ must "
            "be a per-nucleus ~10^(−cA²) normalization (inverse crossing-"
            "count / hyperbolic-volume scale)."
            % (round(logDelta_alt.max() - logDelta_alt.min()), r2_Delta_quad)
        ),
    })
    w.add_data("feed_sample", feed_sample)
    w.add_data("findings", [
        "log10|tr_M(a)| = %.4f A² %+.3f A %+.2f, R²=%.5f — quadratic in A "
        "because the atom crossing count is T = 11A + A(A−1)/2 + Z. The "
        "linear-only fit is markedly worse (R²=%.5f)."
        % (cq[0], cq[1], cq[2], r2_quad, r2_lin),
        "Binding is linear in A (R²=%.4f, B/A ∈ %.2f–%.2f MeV); log10 B ≤ "
        "%.2f while log10|tr_M| reaches %.0f. The χ_λ(a)/B scale mismatch "
        "is ~10^1000."
        % (r2_B_lin, BperA.min(), BperA.max(), np.log10(B).max(),
           trL.max()),
        "The Δ_λ gate is therefore a SCALE gate: the required Δ_alt(K) is "
        "NOT constant (spans ~%d orders of magnitude, itself quadratic in "
        "A) — it must absorb the exponential crossing growth. This explains "
        "the six failed constant/structural ansätze and points to Δ_λ as a "
        "per-nucleus inverse-volume/packing factor (rho_F · V_hyp "
        "direction), not a Wedderburn-block constant."
        % round(logDelta_alt.max() - logDelta_alt.min()),
    ])
    w.add_assertion(
        name="trM_log10_quadratic_fit_excellent",
        computed=round(r2_quad, 6), expected=1.0, tolerance=0.001,
        source="log10|tr_M| ~ aA²+bA+c lstsq R² (crossing-count law)",
    )
    w.add_assertion(
        name="binding_linear_in_A",
        computed=round(r2_B_lin, 6), expected=1.0, tolerance=0.02,
        source="B ~ mA+c lstsq R² (linear binding curve)",
    )

    out = w.save()
    print(f"N = {len(r)} nuclei")
    print(f"log10|tr_M| = {cq[0]:.4f}A² {cq[1]:+.3f}A {cq[2]:+.2f}  "
          f"R²_quad={r2_quad:.5f}  R²_lin={r2_lin:.5f}  R²_vs_T={r2_T:.5f}")
    print(f"binding linear in A: R²={r2_B_lin:.4f}  B/A {BperA.min():.2f}"
          f"–{BperA.max():.2f} MeV")
    print(f"required Δ_alt(K): NOT constant — spans "
          f"{logDelta_alt.max()-logDelta_alt.min():.0f} orders of "
          f"magnitude, quadratic in A (R²={r2_Delta_quad:.4f})")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
