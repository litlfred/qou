#!/usr/bin/env python3
"""Two-sector split of the deuteron pn-pair binding: trace-decoherence vs
genuine Frobenius-norm loss.

EXPLORATORY (audit-only, no production rewire, no fit, no selection).
Tranche 5 of the reeb-flow pn-magnitude program. The real deuteron binding
b₂ = 2.2246 MeV sits BETWEEN the exchange-sector marginal value
(−E₀·ln(1−g²) ≈ 0.93) and the trace-sector suppression
(α·ln(tr_free/tr_atom) ≈ 3.9). This probe asks WHICH sector it lives in by
splitting the trace suppression into its two physically-distinct parts,
using the Frobenius/Markov Gram machinery of gram_norm_binding_probe.py.

For each isotope the atom word W_atom (with inter-block pn crossing) and the
free word W_free (without) are evaluated per Wedderburn block λ ⊢ 3(Z+N):

  T(W)  = Σ_λ y_λ tr(ρ_λ(W))          — the SCALAR (identity-channel) trace
  G(W)  = Σ_λ y_λ tr(ρ_λ(W)ρ_λ(W^♯))  — the total ♯-Gram length (all channels)

The two-sector split of the binding (α = E₀):

  B_scalar = α · ln(T_free / T_atom)        — total scalar-channel collapse
                                              (this is what Term 1 counts)
  B_norm   = (α/2) · ln(G_free / G_atom)     — GENUINE loss of total ♯-length
  B_redist = B_scalar − B_norm               — DECOHERENCE: scalar amplitude
                                              that moved off-diagonal without
                                              leaving the total norm

Hypothesis (preregistered, not assumed): if binding is genuine size
reduction, B_norm ≈ b_AME; if the trace suppression is mostly decoherence,
B_norm ≈ 0 and B_redist carries the bulk. The exchange-sector marginal
value B_exch = −E₀·ln(1−g²) with g = 1/√(1+[2]_v²) is printed alongside as
the third reference sector.

VERDICT is reported, not chosen: the three sector values vs AME per isotope.
Scope-(a): constrains the (word, functional) decomposition at q₀ only.

PRECISION: float64 (the seminormal ρ path is scipy float64) — adequate for
the %-level sector comparison; the linear trace is cross-checked against the
50-dps tr_m_atom_zn transfer value (float64 floor ~1e-8 rel).

-- Ref: gram_norm_binding_probe.py (G/T machinery, ♯ pairing, free/atom words);
QOU/MassTheory/ReebPnMagnitude.lean (exchange criticality);
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md;
docs/audits/2026-07-03-qbar-norm-repitch-assessment.md §3 (norm near-conservation).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import math  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
# Reuse the exact aggregation used by the landed Gram probe.
from probes.gram_norm_binding_probe import _gram_and_trace  # noqa: E402

HERE = Path(__file__).resolve().parent
ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1)]


def main() -> int:
    t0 = time.monotonic()
    from mass_binding_dashboard import _ame_table, _constants
    ame = _ame_table()
    _, _, alpha = _constants()
    alpha = float(alpha)

    # exchange-sector reference magnitude g (structural form)
    q0 = mp.mpf(str(Q0))
    v = mp.sqrt(q0)
    z = mp.mpf(1) / (v + 1 / v)
    g = z / mp.sqrt(1 + z * z)
    E0 = alpha  # α = E₀ in this convention
    B_exch = float(-mp.mpf(str(E0)) * mp.log(1 - g * g))

    rows = []
    for name, Z, N in ISOTOPES:
        n = 3 * (Z + N)
        y = y_lambda_at(n, q_val=float(Q0))
        w_atom = atom_braid_word_3A(Z, N, include_inter=True)
        w_free = atom_braid_word_3A(Z, N, include_inter=False)
        Ga, Ta, _, _ = _gram_and_trace(w_atom, n, y)
        Gf, Tf, _, _ = _gram_and_trace(w_free, n, y)

        # scalar-channel collapse (Term-1-like). Guard against sign/zero.
        B_scalar = alpha * math.log(Tf / Ta) if (Ta > 0 and Tf > 0) else None
        # genuine total-norm loss (quadratic ⇒ /2). G indefinite at q₀ ⇒ guard.
        B_norm = (alpha / 2) * math.log(Gf / Ga) if (Ga > 0 and Gf > 0) else None
        B_redist = (B_scalar - B_norm) if (B_scalar is not None
                                           and B_norm is not None) else None
        # AME table is keyed (Z, A) → (B, B_err, M, M_err).
        b_ame = float(ame[(Z, Z + N)][0])

        def err(x):
            return None if (x is None or not b_ame) else round(100 * (x - b_ame) / b_ame, 3)

        rows.append({
            "iso": name, "n": n,
            "T_free": f"{Tf:.6g}", "T_atom": f"{Ta:.6g}",
            "G_free": f"{Gf:.6g}", "G_atom": f"{Ga:.6g}",
            "B_scalar_MeV": None if B_scalar is None else round(B_scalar, 5),
            "B_norm_MeV": None if B_norm is None else round(B_norm, 5),
            "B_redist_MeV": None if B_redist is None else round(B_redist, 5),
            "B_exch_MeV": round(B_exch, 5),
            "B_AME_MeV": round(b_ame, 5),
            "err_scalar_pct": err(B_scalar),
            "err_norm_pct": err(B_norm),
            "err_exch_pct": err(B_exch),
        })

    # verdict text keyed on the deuteron
    d = rows[0]
    verdict = (
        f"Deuteron two-sector split: genuine norm-loss B_norm = "
        f"{d['B_norm_MeV']} MeV vs AME {d['B_AME_MeV']}; scalar collapse "
        f"B_scalar = {d['B_scalar_MeV']} (of which decoherence/redistribution "
        f"B_redist = {d['B_redist_MeV']}). Reported per sector, no selection; "
        f"scope-(a)."
    )

    result = {
        "constants": {"q0": mp.nstr(q0, 12), "z": mp.nstr(z, 10),
                      "g_exch": mp.nstr(g, 10), "alpha_E0_MeV": f"{alpha:.6g}"},
        "sectors": {
            "B_scalar": "α·ln(T_free/T_atom) — scalar-channel collapse (Term-1-like)",
            "B_norm": "(α/2)·ln(G_free/G_atom) — genuine total ♯-norm loss",
            "B_redist": "B_scalar − B_norm — decoherence (norm-conserving redistribution)",
            "B_exch": "−E₀·ln(1−g²) — exchange-sector marginal (reeb-flow)",
        },
        "rows": rows,
        "verdict": verdict,
    }
    payload = {
        "computation": "pn-pair-two-sector-split",
        "description": ("Two-sector split of deuteron pn-pair binding: genuine "
                        "Frobenius-norm loss vs trace-scalar decoherence, vs the "
                        "exchange-sector marginal value. Audit-only; no fit; no "
                        "selection."),
        "tier": "exploratory (sector decomposition, float64 ρ path)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "pn-pair-two-sector-split", payload,
        script_path=__file__, engine="python+mpmath+scipy",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=str(HERE), start_time=t0,
    )
    # sanity: all three sector values are finite for the deuteron
    wb.add_assertion("deuteron_sectors_finite",
                     computed=str(all(d[k] is not None for k in
                                      ("B_scalar_MeV", "B_norm_MeV", "B_exch_MeV"))),
                     expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== deuteron pn-pair two-sector split ===")
    print(f"  q0={float(q0):.6f}  g_exch={float(g):.6f}  E0=α={alpha:.4f} MeV")
    print(f"  {'iso':>4} {'B_scalar':>9} {'B_norm':>8} {'B_redist':>9} "
          f"{'B_exch':>7} {'AME':>7}")
    for r in rows:
        print(f"  {r['iso']:>4} {str(r['B_scalar_MeV']):>9} {str(r['B_norm_MeV']):>8} "
              f"{str(r['B_redist_MeV']):>9} {str(r['B_exch_MeV']):>7} "
              f"{str(r['B_AME_MeV']):>7}")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
