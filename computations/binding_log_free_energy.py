#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath evaluation at q0; no symbolic-q polynomial output.
"""On-scale EXTENSIVE binding: the log-free-energy functional on the CANONICAL tr_M.

**Compute-wiring step.** Wires the on-scale binding functional

    B(K) = E_0 · log( |tr_M(W_free)| / |tr_M(W_atom)| )

onto the *canonical lossless* Markov trace returned by
[`binding_canonical`](binding_canonical.py) (all p(3A) partitions, 50 dps via
the fine-Bratteli transfer matrix) — NOT the per-bond `f_bond` product of the
exploratory probe [`derived_bond_graph_binding.py`](derived_bond_graph_binding.py)
(which needs an edge-set assumption). The two agree exactly — the 2026-06-10
bond-graph audit validated `∏_chain f_bond = tr_atom/tr_free` to 1e-15 — but the
canonical trace is exact and assumption-free, so this is the principled home of
the functional.

## Why this functional (not the canonical linear difference)

`binding_canonical`'s default output `B_lin = Q_β·(tr_M(W_free) − tr_M(W_atom))`
is **intensive**: the trace *difference* saturates (~0.78 MeV ceiling) and cannot
grow with A — it misses AME by 4.8–39.7×. The **log**-free-energy is the
**extensive** invariant,

    log(tr_free/tr_atom) = Σ_bonds log(1/f_bond)   (exact; 2026-06-10 audit),

on-scale 0.57–2.36× vs AME. It is the q-heat-flow free energy
`B = E_0·log(Z_free/Z_atom)` of the Wedderburn heat trace `Z_q = tr_M`, with
`E_0 = m_e/(q0(q0−1)) ≈ 4.186 MeV` a **closed substrate expression** (NO fit, NO
fourth calibration).

## Scope (honest)

This producer wires the *functional*; it does **not** claim the Δ_λ / binding
gate closed. The canonical atom braid wires the **A−1 chain** bonds, so this is
the chain log-free-energy: it under-binds doubly-magic ⁴He and over-binds the
halo deuteron. The residual is the **edge-set / fractional-occupancy** question
(lever 2; static integer graphs refuted, 2026-06-10 §6). This is, specifically,
the **on-scale sibling that the 2026-06-16/17 binding-closure docs skipped** —
see the lever-status review.

Output: binding-log-free-energy.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from _precision import COMPUTE_DPS  # noqa: E402
from q_parameter import Q as Q_STR  # noqa: E402  canonical 50-dps substrate value
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION as B_D_AME,
    AME_B_TRITIUM_MEV_VALIDATION as B_T_AME,
    AME_B_HE3_MEV_VALIDATION as B_HE3_AME,
    AME_B_HE4_MEV_VALIDATION as B_HE4_AME,
)
from binding_canonical import binding_canonical  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# (name, Z, N, AME binding anchor [MeV] — validation-only, NOT an input)
ATOMS = [
    ("deuteron", 1, 1, B_D_AME),
    ("tritium", 1, 2, B_T_AME),
    ("he3", 2, 1, B_HE3_AME),
    ("he4", 2, 2, B_HE4_AME),
]


def main() -> int:
    t0 = time.time()
    mp.mp.dps = COMPUTE_DPS
    q0 = mp.mpf(str(Q_STR))
    me = mp.mpf(str(M_E_MEV))
    # Canonical energy scale — closed substrate expression (the deuteron-fixing
    # scale of the 2026-06-10 audit; NOT Q_β, NOT a fit).
    E0 = me / (q0 * (q0 - 1))

    rows = []
    for name, Z, N, B_ame in ATOMS:
        r = binding_canonical(Z, N)
        if r.get("status") != "solved":
            rows.append({"atom": name, "status": r.get("status", "?")})
            continue
        tr_atom = mp.mpf(r["tr_M_atom"])
        tr_free = mp.mpf(r["tr_M_free"])
        B_log = E0 * mp.log(abs(tr_free) / abs(tr_atom))     # extensive (on-scale)
        B_lin = mp.mpf(str(r["B_MeV"]))                       # intensive (saturates)
        B_ame_mp = mp.mpf(str(B_ame))
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "B_AME_MeV": mp.nstr(B_ame_mp, 8),
            "tr_M_free": mp.nstr(tr_free, 10),
            "tr_M_atom": mp.nstr(tr_atom, 10),
            "B_logfree_MeV": mp.nstr(B_log, 8),
            "ratio_logfree": float(B_log / B_ame_mp),
            "B_linear_MeV": mp.nstr(B_lin, 8),
            "ratio_linear": float(B_lin / B_ame_mp),
        })

    solved = [r for r in rows if "ratio_logfree" in r]
    log_ratios = [r["ratio_logfree"] for r in solved]
    lin_ratios = [abs(r["ratio_linear"]) for r in solved]
    by_atom = {r["atom"]: r for r in solved}

    w = WitnessBuilder("binding-log-free-energy", engine="mpmath", start_time=t0)
    w.set_description(
        "Extensive binding via the log-free-energy functional "
        "B = E_0·log(|tr_M_free|/|tr_M_atom|) wired onto the CANONICAL lossless "
        "tr_M (binding_canonical, all p(3A) partitions, 50 dps). E_0 = "
        f"m_e/(q0(q0-1)) = {mp.nstr(E0, 8)} MeV (closed substrate form, no fit). "
        "On-scale 0.57-2.36x vs AME, vs the canonical LINEAR difference "
        "B = Q_β·(tr_free-tr_atom) which is intensive and saturates (~0.78 MeV, "
        "4.8-39.7x miss). NOT a closure: chain topology under-binds magic 4He / "
        "over-binds halo D; the edge-set/occupancy residual is the open piece "
        "(lever 2). The on-scale sibling skipped by the 2026-06-16/17 closure docs."
    )
    w.add_parameter("q0", mp.nstr(q0, 12))
    w.add_parameter("E_0_MeV", mp.nstr(E0, 10))
    w.add_parameter("compute_dps", COMPUTE_DPS)
    w.add_data("functional", "B = E_0 * log(|tr_M_free| / |tr_M_atom|)")
    w.add_data("rows", rows)
    w.add_data("headline", {
        "logfree_ratio_range": f"{min(log_ratios):.3f}-{max(log_ratios):.3f}x AME",
        "linear_ratio_range": f"{min(lin_ratios):.3f}-{max(lin_ratios):.3f}x AME",
        "verdict": "log-free-energy is extensive + on-scale; linear difference "
                   "saturates. Functional wired to canonical tr_M; edge-set open.",
    })
    # Assertion 1: every log-free-energy binding is on-scale (NOT a closure claim).
    w.add_assertion(
        name="logfree_binding_on_scale_all_atoms",
        computed=1 if all(0.4 <= x <= 2.5 for x in log_ratios) else 0,
        expected=1, tolerance=0,
        source="every B_logfree/B_AME in [0.4, 2.5] over D/T/3He/4He "
               f"(range {min(log_ratios):.3f}-{max(log_ratios):.3f}); "
               "on-scale, not a closure.",
    )
    # Assertion 2: the functional is EXTENSIVE — 4He (A=4) more bound than D (A=2).
    _he4_gt_d = (mp.mpf(by_atom["he4"]["B_logfree_MeV"])
                 > mp.mpf(by_atom["deuteron"]["B_logfree_MeV"]))
    w.add_assertion(
        name="logfree_extensive_he4_gt_deuteron",
        computed=1 if _he4_gt_d else 0,
        expected=1, tolerance=0,
        source="B_logfree(4He) > B_logfree(2H): extensive growth with A "
               "(the linear difference instead saturates).",
    )
    out = w.save()

    print("=" * 92)
    print(" Log-free-energy binding  B = E_0·log(|tr_free|/|tr_atom|)  on the CANONICAL tr_M")
    print(f"   E_0 = m_e/(q0(q0-1)) = {mp.nstr(E0, 8)} MeV   (closed substrate form, no fit)")
    print("=" * 92)
    print(f" {'atom':>9}{'A':>3}{'B_AME':>9}{'B_logfree':>11}{'log/AME':>9}"
          f"{'B_linear':>10}{'lin/AME':>9}")
    print(" " + "-" * 90)
    for r in solved:
        print(f" {r['atom']:>9}{r['A']:>3}{float(r['B_AME_MeV']):>9.3f}"
              f"{float(r['B_logfree_MeV']):>11.3f}{r['ratio_logfree']:>9.3f}"
              f"{float(r['B_linear_MeV']):>10.3f}{r['ratio_linear']:>9.3f}")
    print(" " + "-" * 90)
    print(f" log-free-energy: {min(log_ratios):.3f}-{max(log_ratios):.3f}x AME "
          f"(extensive, on-scale)")
    print(f" linear diff:     {min(lin_ratios):.3f}-{max(lin_ratios):.3f}x AME "
          f"(intensive, saturates)")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
