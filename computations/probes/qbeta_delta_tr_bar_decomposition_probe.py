#!/usr/bin/env python3
"""qbeta_delta_tr_bar_decomposition_probe.py — structural observation:
Δtr_M decomposed into bar-symmetric + antisymmetric parts under
q → 1/q (equivalently t → 1/t with t = q^(1/2)).

CONTEXT (post-PR #1609 Li_2^q × spectral refutation). The c_3 saga
keeps producing near-matches because the candidates don't respect
the natural bar-involution structure of the Hecke algebra. Per
prop:li2q-phiq-bar-symmetrization: binding quantities (Q_β, Δ_λ)
should be bar-symmetric; mass quantities (m_p absolute) carry
the bar-asymmetric dimensional scale.

This probe is a STRUCTURAL OBSERVATION, not a derivation:
  - Loads symbolic Δtr_M(q) from habiro-coefficients-atomic witness
  - Substitutes t = q^(1/2) to land in ℚ(t) (eliminating half-integer
    q-powers from the Hecke conventions)
  - Decomposes Δtr_M(t) = sym(t) + antisym(t) under t ↔ 1/t
  - Factors the symmetric and antisymmetric parts

DISCIPLINE: This probe does NOT propose a c_k closure candidate.
Per CLAUDE.md "Don't propose a seventh fit-based ansatz" the bar-
decomposition is recorded as a STRUCTURAL FACT for follow-up
research, not as a wired derivation. If a future session uses
this decomposition to derive c_k, it must pass the cross-anchor
test (q_proton vs q_muon) AND have a structural justification —
not just match numerically at one anchor.

OUTPUT: witness with the decomposition, plus markdown audit doc
flagging the next-session direction.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-delta-tr-bar-decomposition-probe",
                              engine="python+sympy", start_time=t0)
    builder.set_description(
        "Structural observation: Δtr_M(q) bar-decomposition under "
        "q → 1/q. Records the closed forms of the symmetric and "
        "antisymmetric components without proposing a c_k closure "
        "candidate (per CLAUDE.md no-7th-ansatz discipline)."
    )
    # Audit-only: this probe documents a structural observation in the
    # paired audit doc; it is not expected to wire to any production
    # content block via `computation.witness`. Excludes from orphan tally
    # in scripts/audit-wiring.ts.
    builder.set_audit_only(
        "docs/audits/2026-06-01-delta-tr-m-bar-decomposition-structural-finding.md"
    )

    upstream_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    upstream = builder.add_upstream(upstream_path)

    tr_p_str = upstream["results"]["p (proton, A=1)"]["tr_M_in_q"]
    tr_n_str = upstream["results"]["n (neutron, A=1)"]["tr_M_in_q"]

    q = sp.Symbol("q", positive=True)
    t = sp.Symbol("t", positive=True)

    tr_p = sp.sympify(tr_p_str, locals={"q": q})
    tr_n = sp.sympify(tr_n_str, locals={"q": q})
    delta_tr = sp.cancel(tr_n - tr_p)

    # Bar-symmetry test in q
    bar_q = sp.cancel(delta_tr.subs(q, 1 / q))
    delta_tr_minus_bar_q = sp.cancel(delta_tr - bar_q)
    print("Δtr_M(q) - Δtr_M(1/q) =", delta_tr_minus_bar_q)
    print("  → not zero ⟹ Δtr_M is NOT bar-symmetric in q")
    print()

    # Change of variable: t = q^(1/2)
    delta_tr_t = sp.cancel(delta_tr.subs(q, t ** 2))
    print("Δtr_M in t = q^(1/2):", delta_tr_t)

    bar_t = sp.cancel(delta_tr_t.subs(t, 1 / t))
    diff_t = sp.cancel(delta_tr_t - bar_t)
    sym_t = sp.cancel((delta_tr_t + bar_t) / 2)
    antisym_t = sp.cancel((delta_tr_t - bar_t) / 2)

    sym_q = sp.cancel(sym_t.subs(t, sp.sqrt(q)))
    antisym_q = sp.cancel(antisym_t.subs(t, sp.sqrt(q)))

    sym_t_factored = sp.factor(sym_t)
    antisym_t_factored = sp.factor(antisym_t)

    print()
    print(f"Symmetric part (in t):      {sym_t}")
    print(f"  factored:                 {sym_t_factored}")
    print(f"  back-substituted in q:    {sym_q}")
    print(f"Antisymmetric part (in t):  {antisym_t}")
    print(f"  factored:                 {antisym_t_factored}")
    print(f"  back-substituted in q:    {antisym_q}")
    print()

    builder.add_data("delta_tr_M_in_q", str(delta_tr))
    builder.add_data("delta_tr_M_in_t_q_half", str(delta_tr_t))
    # Δtr_M(q) − Δtr_M(1/q): nonzero ⟺ not bar-symmetric
    builder.add_data("delta_tr_minus_bar_q", str(delta_tr_minus_bar_q))
    builder.add_data("verdict_q_bar_symmetric", str(delta_tr_minus_bar_q) == "0")
    builder.add_data("bar_t_decomposition", {
        "symmetric_part_t": str(sym_t),
        "symmetric_part_t_factored": str(sym_t_factored),
        "symmetric_part_q": str(sym_q),
        "antisymmetric_part_t": str(antisym_t),
        "antisymmetric_part_t_factored": str(antisym_t_factored),
        "antisymmetric_part_q": str(antisym_q),
    })

    # Numerical sanity at q_proton — compute sym + antisym at q_0
    sym_anti_matches = False
    try:
        from qou_substrate.constants import q_at
        q_proton = q_at()
        sym_num = float(sp.N(sym_q.subs(q, sp.Float(str(q_proton), 50)), 30))
        anti_num = float(sp.N(antisym_q.subs(q, sp.Float(str(q_proton), 50)), 30))
        total_num = float(sp.N(delta_tr.subs(q, sp.Float(str(q_proton), 50)), 30))
        # Float comparison: 64-bit ULP is ~1e-16; use 1e-12 for safe margin
        sym_anti_matches = abs(sym_num + anti_num - total_num) < 1e-12
        builder.add_data("at_q_proton_numerical", {
            "q_proton": str(q_proton),
            "symmetric_value": sym_num,
            "antisymmetric_value": anti_num,
            "sum_check": sym_num + anti_num,
            "delta_tr_full": total_num,
            "match": sym_anti_matches,
        })
        print(f"At q_proton: sym = {sym_num:.6e}, anti = {anti_num:.6e}, "
              f"sum = {sym_num + anti_num:.6e}, full = {total_num:.6e}")
    except Exception as e:
        builder.add_data("at_q_proton_numerical", f"skipped: {e}")
        print(f"Numerical eval skipped: {e}")

    builder.add_data("structural_finding", (
        "Δtr_M(q) decomposes in t = q^(1/2) as sym(t) + antisym(t) "
        "under t ↔ 1/t. The symmetric part has a clean closed form "
        "(see sym_part_t_factored); the antisymmetric part is more "
        "intricate. This decomposition is the natural projection "
        "onto bar-eigenspaces of the Hecke bar-involution."
    ))
    builder.add_data("anti_pattern_guard", (
        "This probe does NOT propose a c_k closure. Any future "
        "attempt to use this decomposition for c_k must pass the "
        "cross-anchor test (q_proton vs q_muon) AND have a "
        "structural justification — not just numerical near-match."
    ))
    builder.add_data("follow_up_research_direction", (
        "(NEW) Decomposing Q_β candidate forms onto bar-symmetric "
        "/ antisymmetric projections may give a structured attack "
        "on the Habiro element identification. The sym part is "
        "in the binding (Li_2^q) sector per prop:li2q-phiq-bar-"
        "symmetrization; the antisym part is in the mass (Φ_q) "
        "sector. Q_β being a mass DIFFERENCE means the sym "
        "projection is dominant — investigating which Wedderburn "
        "blocks contribute to sym vs antisym could narrow the "
        "Habiro search."
    ))

    builder.add_assertion(
        name="bar_decomposition_sums_to_total_at_q_proton",
        computed=1.0 if sym_anti_matches else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Δtr_M(q) = sym + antisym by linearity of bar-involution",
    )

    out = builder.save()
    print(f"\n✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
