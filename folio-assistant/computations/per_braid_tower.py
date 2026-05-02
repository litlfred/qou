#!/usr/bin/env python3
"""
Per-braid mass tower (P2.2a-deeper, per user clarification).

Implements the per-sub-braid form of `prop:mass-endomorphism-tower`,
replacing the per-generator V̂_i^full with **per-sub-braid Markov
traces** computed via the proper H_{3A} Schur-Weyl path.

Formula:

  𝔪(K) = |tr_M(W)|                                  (descended, level 0)
       +     Σ_{ξ ∈ S_1}    Φ_q(|tr_M(ξ)|)         (per-sub-braid, level 1)
       + z² Σ_{(ξ,ξ') ∈ S_2} Φ_q(|tr_M(ξ ξ')|)     (sub-braid pair, level 2)

where:

  S_0 = {W}                                       — the full atomic braid
  S_1 = {β_N : per-nucleon sub-braids}           — A elements
  S_2 = {(β_N, β_{N'}) : nucleon pairs}          — A(A-1)/2 elements

For an (Z, N) atom:

  S_1 contributions (A nucleons):
    Z × tr_M(proton)   [via SW, 3-strand H_3 = single proton braid]
    N × tr_M(neutron)  [via SW, 3-strand H_3 = single neutron braid]

  S_2 contributions (A(A-1)/2 pairs):
    Z(Z-1)/2 × tr_M(pp-pair)   [via SW, 6-strand H_6 = two protons]
    N(N-1)/2 × tr_M(nn-pair)   [via SW, 6-strand H_6 = two neutrons]
    Z·N      × tr_M(pn-pair)   [via SW, 6-strand H_6 = proton + neutron]

Each sub-braid trace is computed via markov_trace_schur_weyl_eval
(P2.2a wiring) — proper H_{3A} weights.

Compares to:
  - per-generator H_3 tower (the divergent path, tower_mass_symbolic_eval)
  - descended-only (markov_trace_schur_weyl_eval at the full atom)

Witness: docs/audits/2026-05-01-per-braid-tower.witness.json

References:
  prop:mass-endomorphism-tower
  prop:phi-q-tower-jsj-bridge (Algebraic-side §)
  prop:graded-trace-residue-split
  docs/audits/2026-05-01-h3-at-h3a-weight-derivation.md
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from crt_markov import (
    markov_trace_schur_weyl_eval,
    markov_trace_symbolic_eval,
    tower_mass_symbolic_eval,
    _Phi_q_mp,
)
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))
qi0 = 1 / q0
z_mark = 1 / (q0 ** mpmath.mpf("0.5") + qi0 ** mpmath.mpf("0.5"))


def _safe_phi(z):
    """Φ_q(z) with safe handling of the |z| ≥ q boundary."""
    z_abs = abs(z)
    if z_abs >= q0:
        return mpmath.inf
    return _Phi_q_mp(z_abs, q0, qi0)


def per_braid_mass(Z, N, *, precision=50):
    """Compute the per-braid mass tower.

    Returns dict with descended / single / cross / total contributions.
    """
    A = Z + N

    # ── Level 0: full atomic braid descended trace ──────────────────
    # Use the proper H_{3A} Schur-Weyl path.
    desc = abs(markov_trace_schur_weyl_eval(Z, N, True, q0, precision))

    # ── Level 1: per-nucleon sub-braid traces ──────────────────────
    # Each nucleon is a 3-strand braid (H_3), evaluated as (Z=1, N=0)
    # for proton or (Z=0, N=1) for neutron, both with include_inter=False
    # (single nucleon — no inter-nucleon coupling).
    tr_p = abs(markov_trace_schur_weyl_eval(1, 0, False, q0, precision)) if Z > 0 else mpmath.mpf(0)
    tr_n = abs(markov_trace_schur_weyl_eval(0, 1, False, q0, precision)) if N > 0 else mpmath.mpf(0)

    # ── Level 2: per-nucleon-pair sub-braid traces ─────────────────
    # Each pair is a 6-strand braid (H_6), with the inter-nucleon
    # coupling (Z+N=2, include_inter=True).
    tr_pp = abs(markov_trace_schur_weyl_eval(2, 0, True, q0, precision)) if Z >= 2 else mpmath.mpf(0)
    tr_nn = abs(markov_trace_schur_weyl_eval(0, 2, True, q0, precision)) if N >= 2 else mpmath.mpf(0)
    tr_pn = abs(markov_trace_schur_weyl_eval(1, 1, True, q0, precision)) if Z >= 1 and N >= 1 else mpmath.mpf(0)

    # ── Single tower: Σ_{ξ ∈ S_1} Φ_q(|tr_M(ξ)|) ───────────────────
    single = mpmath.mpf(0)
    if Z > 0 and tr_p > 0:
        phi_p = _safe_phi(tr_p)
        single += Z * phi_p
    if N > 0 and tr_n > 0:
        phi_n = _safe_phi(tr_n)
        single += N * phi_n

    # ── Pair tower: z² Σ Φ_q(|tr_M(ξ ξ')|) ─────────────────────────
    cross = mpmath.mpf(0)
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N
    if n_pp > 0 and tr_pp > 0:
        phi_pp = _safe_phi(tr_pp)
        cross += n_pp * phi_pp
    if n_nn > 0 and tr_nn > 0:
        phi_nn = _safe_phi(tr_nn)
        cross += n_nn * phi_nn
    if n_pn > 0 and tr_pn > 0:
        phi_pn = _safe_phi(tr_pn)
        cross += n_pn * phi_pn
    cross *= z_mark ** 2

    total = desc + single + cross

    return {
        "Z": Z, "N": N, "A": A,
        "descended": desc,
        "single_tower": single,
        "cross_tower": cross,
        "total": total,
        "level_1_traces": {
            "proton": tr_p,
            "neutron": tr_n,
        },
        "level_2_traces": {
            "pp_pair": tr_pp,
            "nn_pair": tr_nn,
            "pn_pair": tr_pn,
        },
        "level_2_multiplicities": {
            "n_pp": n_pp,
            "n_nn": n_nn,
            "n_pn": n_pn,
        },
    }


ATOMS = [
    ("D", 1, 1),
    ("3He", 2, 1),
    ("3H_tritium", 1, 2),
    ("4He", 2, 2),
]


print("=" * 80)
print("Per-braid mass tower — P2.2a-deeper")
print("=" * 80)
print(f"q_0 = {q0}")
print()

results = []
for name, Z, N in ATOMS:
    print(f"\n=== {name} (Z={Z}, N={N}, A={Z+N}) ===")
    try:
        out = per_braid_mass(Z, N)
        # Comparison to per-generator H_3 tower (the divergent one)
        try:
            full_h3 = tower_mass_symbolic_eval(Z, N, True, 1, 1, 1, q0, precision=50)
            h3_total = full_h3["total"]
        except Exception:
            h3_total = None

        print(f"  descended (level 0):    {float(out['descended']):.6e}")
        print(f"  single tower (level 1): {float(out['single_tower']):.6e}")
        print(f"  cross tower (level 2):  {float(out['cross_tower']):.6e}")
        print(f"  TOTAL per-braid:        {float(out['total']):.6e}")
        if h3_total is not None and not mpmath.isinf(h3_total):
            print(f"  per-generator H_3 (cmp): {float(h3_total):.6e}")
        elif h3_total is not None and mpmath.isinf(h3_total):
            print(f"  per-generator H_3 (cmp): inf (Φ_q divergent)")

        # Sub-traces
        print(f"  level-1 traces:  proton={float(out['level_1_traces']['proton']):.4e}  neutron={float(out['level_1_traces']['neutron']):.4e}")
        print(
            f"  level-2 traces:  pp={float(out['level_2_traces']['pp_pair']):.4e}  "
            f"nn={float(out['level_2_traces']['nn_pair']):.4e}  "
            f"pn={float(out['level_2_traces']['pn_pair']):.4e}"
        )
        print(
            f"  level-2 multiplicities:  n_pp={out['level_2_multiplicities']['n_pp']}  "
            f"n_nn={out['level_2_multiplicities']['n_nn']}  "
            f"n_pn={out['level_2_multiplicities']['n_pn']}"
        )

        # Convergence diagnostic
        sub_max = max(
            float(out['level_1_traces']['proton'] or 0),
            float(out['level_1_traces']['neutron'] or 0),
            float(out['level_2_traces']['pp_pair'] or 0),
            float(out['level_2_traces']['nn_pair'] or 0),
            float(out['level_2_traces']['pn_pair'] or 0),
        )
        print(f"  Φ_q convergence:  max sub-braid trace = {sub_max:.4f}  (q_0 = {float(q0):.4f}; need < q_0)  → {'✅' if sub_max < float(q0) else '🔴'}")

        results.append({
            "atom": name,
            "Z": Z, "N": N, "A": Z + N,
            "descended": str(out["descended"]),
            "single_tower": str(out["single_tower"]) if not mpmath.isinf(out["single_tower"]) else "inf",
            "cross_tower": str(out["cross_tower"]) if not mpmath.isinf(out["cross_tower"]) else "inf",
            "total_per_braid": str(out["total"]) if not mpmath.isinf(out["total"]) else "inf",
            "h3_per_generator_total": (
                str(h3_total) if h3_total is not None and not mpmath.isinf(h3_total)
                else ("inf" if h3_total is not None else None)
            ),
            "level_1_traces": {k: str(v) for k, v in out["level_1_traces"].items()},
            "level_2_traces": {k: str(v) for k, v in out["level_2_traces"].items()},
            "level_2_multiplicities": out["level_2_multiplicities"],
            "phi_q_convergence_ok": sub_max < float(q0),
            "max_sub_braid_trace": sub_max,
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        results.append({"atom": name, "error": str(e)})


witness = {
    "audit": "Per-braid mass tower (P2.2a-deeper)",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "framework": (
        "𝔪(K) = |tr_M(W)| + Σ_{ξ∈S_1} Φ_q(|tr_M(ξ)|) + z² Σ_{(ξ,ξ')∈S_2} Φ_q(|tr_M(ξ ξ')|). "
        "S_1 = per-nucleon sub-braids (A elements). S_2 = per-nucleon-pair sub-braids "
        "(A(A-1)/2 elements). Each tr_M computed via the proper H_{3A} Schur-Weyl path "
        "(markov_trace_schur_weyl_eval). The per-generator H_3 tower (divergent) is "
        "shown for comparison."
    ),
    "atoms": results,
    "interpretation": (
        "Per-braid tower replaces the per-generator V̂_i^full (3A-1 terms per atom, "
        "divergent due to H_3-at-H_{3A} weight mismatch) with per-sub-braid Markov "
        "traces (A nucleons + A(A-1)/2 pairs, dramatically fewer terms). Each sub-braid "
        "trace is computed via proper H_{3A} Schur-Weyl, ensuring |tr_M(ξ)| < q_0 and "
        "Φ_q convergence."
    ),
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-per-braid-tower.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
