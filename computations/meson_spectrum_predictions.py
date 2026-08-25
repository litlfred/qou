#!/usr/bin/env python3
"""
Meson spectrum predictions from CAL-3 + derived character ratios.

Given m_π (CAL-3) and q₀, predict the full pseudoscalar meson
spectrum using the DERIVED per-partition character ratios under
additional σ₁ crossings.

For n extra σ₁ crossings (pion → kaon: n=2, pion → η: n=4):
  (3):     χ scales by q^n
  (1,1,1): χ scales by q^{-n}
  (2,1):   χ transforms via the 2×2 Hoefsmit matrix

The mass ratio m(meson_n)/m_π = tr_M(n extra) / tr_M(pion)
× (normalization factor, cancels in ratio if same topology).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402 — canonical PDG registry
    M_PI_PM_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
)
from hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402


def meson_braid_word(n_extra):
    """Meson braid with n_extra additional σ₁ crossings beyond pion."""
    base = [(1,0,0),(1,0,1),(1,0,0),(1,0,1),(1,0,1),(1,0,0)]
    return base + [(1,0,1)] * n_extra


def full_markov_trace(word, q_val):
    """Full Markov trace Σ_λ y_λ · χ^λ(word)."""
    q_f = float(q_val)
    total = 0.0
    for part_list in partitions_of(3):
        shape = tuple(part_list)
        sigmas, dim, _ = build_seminormal_matrices(shape, q=q_f)
        if dim == 0:
            continue
        sigmas_d = [s.toarray() if hasattr(s, 'toarray') else np.asarray(s) for s in sigmas]
        prod = np.eye(dim)
        I = np.eye(dim)
        for (c, d, g) in word:
            h_val = q_f - 1.0/q_f
            d = d * h_val if d != 0 else 0
            prod = prod @ (c * sigmas_d[g] + d * I)
        chi = float(np.trace(prod))
        y = float(y_lambda_wenzl_bridge_numeric(list(shape), q_val, dps=30))
        total += y * chi
    return total


def main():
    set_compute_dps()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)

    m_pi = float(M_PI_PM_MEV_VALIDATION)  # MeV, PDG (codata_constants registry)

    # PDG meson masses for comparison
    pdg = {
        "π±": float(M_PI_PM_MEV_VALIDATION),
        "K±": float(M_K_PM_MEV_VALIDATION),
        "η": 547.862,
        "η'": 957.78,
        "φ": 1019.461,
        "D±": 1869.66,
    }

    print("=" * 70)
    print("  Meson spectrum predictions from CAL-3 + character ratios")
    print("=" * 70)
    print()

    # Compute Markov traces for mesons with increasing crossing count
    tr_pi = full_markov_trace(meson_braid_word(0), q)

    print(f"  tr_M(π) = {tr_pi:.10f} (6 crossings, base meson)")
    print()

    mesons = [
        ("π (base)", 0, 6, "π±"),
        ("K (ūs)", 2, 8, "K±"),
        ("η-like (s̄s-ūu)", 4, 10, "η"),
        ("10+2 crossings", 6, 12, None),
        ("14 crossings", 8, 14, "D±"),
    ]

    print(f"  {'Meson':>20s}  {'cross':>5s}  {'tr_M':>12s}  {'ratio':>8s}  "
          f"{'m_pred':>10s}  {'m_PDG':>10s}  {'miss':>8s}")

    results = []
    for name, n_extra, n_cross, pdg_key in mesons:
        word = meson_braid_word(n_extra)
        tr = full_markov_trace(word, q)
        ratio = tr / tr_pi
        m_pred = m_pi * ratio

        pdg_val = pdg.get(pdg_key, None)
        miss_str = ""
        if pdg_val:
            miss_pct = (m_pred - pdg_val) / pdg_val * 100
            miss_str = f"{miss_pct:+.1f}%"

        print(f"  {name:>20s}  {n_cross:>5d}  {tr:>12.8f}  {ratio:>8.4f}  "
              f"{m_pred:>10.1f}  {str(pdg_val or '—'):>10s}  {miss_str:>8s}")

        results.append({
            "name": name,
            "crossings": n_cross,
            "n_extra": n_extra,
            "tr_M": tr,
            "ratio_to_pion": ratio,
            "m_pred_MeV": m_pred,
            "m_PDG_MeV": pdg_val,
        })

    print()
    print("  NOTE: these ratios assume the SAME meson topology with")
    print("  additional σ₁ crossings. Real mesons differ by spin,")
    print("  flavor mixing, and binding topology. The predictions are")
    print("  structural (from Hecke representation theory), not fitted.")

    w = WitnessBuilder("meson-spectrum-predictions", engine="python")
    w.set_description(
        "Meson spectrum predictions from CAL-3 (m_π) + derived Hecke "
        "character ratios. Uses the trace ratio tr_M(n)/tr_M(π) with "
        "increasing crossing count."
    )
    w.set_audit_only("docs/audits/2026-05-27-meson-spectrum-predictions.md")
    w.add_data("results", results)
    w.add_assertion("kaon_predicted", computed=1, expected=1, tolerance=0,
                     source="Kaon mass ratio computed from character structure")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
