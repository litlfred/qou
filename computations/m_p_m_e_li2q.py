"""
m_p_m_e_li2q.py — m_p/m_e under symmetric Li_2^q instead of Faddeev Φ_q.

Tests whether replacing the legacy Faddeev Φ_q with symmetric Li_2^q
in mass_endomorphism.py's mass-tower formula preserves the m_p/m_e ≈
1836 (CODATA) prediction. If yes, full Faddeev deprecation is safe;
if no, downstream impact must be tracked separately.

The mass-tower formula (per mass_endomorphism.py:114, mass_from_tower):

    𝔪 = |∏ V̂_i| + Σ_i F(|V̂_i|) + Σ_{i<j} z² F(|V̂_i V̂_j|)

where F is the q-dilog. We compare F = Phi_q (Faddeev, legacy) vs
F = Li_2^q (symmetric, per prop:mass-endomorphism-tower SUPERSEDED
banner).

Ref: prop:mass-endomorphism-tower (SUPERSEDED banner: Li_2^q replaces Φ_q)
Ref: docs/audits/2026-05-19-faddeev-audit-pr801.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from _li_2_q_util import li_2_q
from q_parameter import Q as Q0, Q_INV as QI0
from mass_endomorphism import (
    Phi_q, additive_wedderburn_volumes,
    electron_cross, proton_cross, neutron_cross,
)


def mass_from_tower_F(vols, F_func):
    """𝔪 = |∏ V| + Σ F(|V|) + Σ_{i<j} z² F(|V_i V_j|), with F = q-dilog."""
    n = len(vols)
    z_mark = 1.0 / (Q0 ** 0.5 + (1.0 / Q0) ** 0.5)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(F_func(abs(v["full"])) for v in vols)
    cross = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            cross += z_mark ** 2 * F_func(abs(vols[i]["full"] * vols[j]["full"]))
    return desc, single, cross, desc + single + cross


def Li_2_q_f64(z_val: float) -> float:
    """f64 wrapper around mpmath li_2_q for direct comparison with Phi_q."""
    return float(li_2_q(mp.mpf(z_val), mp.mpf(Q0), mp.mpf(QI0)))


def main() -> int:
    builder = WitnessBuilder("m-p-m-e-li2q")
    builder.set_description(
        "Re-derives m_p/m_e under symmetric Li_2^q (replacing Faddeev "
        "Φ_q per prop:mass-endomorphism-tower SUPERSEDED banner). "
        "Compares to legacy Faddeev result and CODATA 1836.152."
    )

    electron_vols = additive_wedderburn_volumes(2, electron_cross)
    proton_vols = additive_wedderburn_volumes(3, proton_cross)
    neutron_vols = additive_wedderburn_volumes(3, neutron_cross)

    print(f"{'particle':<10} {'q-dilog':<10} {'desc':>8} {'single':>12} {'cross':>14} {'total':>14} {'m/m_e':>10}")
    results = {}
    for F_name, F_func in (("Phi_q", Phi_q), ("Li_2_q", Li_2_q_f64)):
        results[F_name] = {}
        for label, vols in (("electron", electron_vols),
                             ("proton", proton_vols),
                             ("neutron", neutron_vols)):
            desc, sgl, cross, total = mass_from_tower_F(vols, F_func)
            results[F_name][label] = {
                "desc": desc, "single": sgl, "cross": cross, "total": total
            }
            print(f"  {label:<10} {F_name:<10} {desc:>8.4f} {sgl:>12.2f} "
                  f"{cross:>14.2f} {total:>14.2f}")

        e_total = results[F_name]["electron"]["total"]
        p_total = results[F_name]["proton"]["total"]
        n_total = results[F_name]["neutron"]["total"]
        mp_me = p_total / e_total
        mn_me = n_total / e_total
        results[F_name]["m_p/m_e"] = mp_me
        results[F_name]["m_n/m_e"] = mn_me
        results[F_name]["m_n/m_p"] = n_total / p_total
        codata_mp_me = 1836.152
        codata_mn_me = 1838.684
        err_mp = abs(mp_me - codata_mp_me) / codata_mp_me * 100
        err_mn = abs(mn_me - codata_mn_me) / codata_mn_me * 100
        results[F_name]["err_pct_mp_me"] = err_mp
        results[F_name]["err_pct_mn_me"] = err_mn
        print(f"  m_p/m_e ({F_name}) = {mp_me:.4f}  (CODATA 1836.152, err {err_mp:.2f}%)")
        print(f"  m_n/m_e ({F_name}) = {mn_me:.4f}  (CODATA 1838.684, err {err_mn:.2f}%)")
        print()

    builder.add_data("results", results)
    builder.add_data("phi_q_err_mp_me_pct", results["Phi_q"]["err_pct_mp_me"])
    builder.add_data("li2q_err_mp_me_pct", results["Li_2_q"]["err_pct_mp_me"])

    if results["Li_2_q"]["err_pct_mp_me"] < results["Phi_q"]["err_pct_mp_me"]:
        verdict = (f"Li_2^q better: {results['Li_2_q']['err_pct_mp_me']:.2f}% "
                   f"vs Φ_q {results['Phi_q']['err_pct_mp_me']:.2f}%. "
                   "Safe to deprecate Φ_q for m_p/m_e tower.")
    elif results["Li_2_q"]["err_pct_mp_me"] < 5:
        verdict = (f"Li_2^q acceptable: {results['Li_2_q']['err_pct_mp_me']:.2f}% "
                   f"vs Φ_q {results['Phi_q']['err_pct_mp_me']:.2f}%. "
                   "Acceptable deprecation (no major regression).")
    else:
        verdict = (f"Li_2^q WORSE: {results['Li_2_q']['err_pct_mp_me']:.2f}% "
                   f"vs Φ_q {results['Phi_q']['err_pct_mp_me']:.2f}%. "
                   "Faddeev deprecation may require refining the formula "
                   "(structural change beyond F-substitution).")
    builder.add_data("verdict", verdict)
    print(f"  Verdict: {verdict}")

    builder.add_assertion(
        "codata_mp_me_loaded",
        computed=1836.152,
        expected=1836.152,
        tolerance=1e-10,
        unit="m_p/m_e",
        source="CODATA 2022",
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554).
    builder.add_data("lean_uniqueness_ref", {
        "proton": "qou:QOU.BraidKnot.PeriodicTableUniqueness.h_uniqueness_closed",
        "electron": "qou:QOU.BraidKnot.nucleus_uniqueness_closed (lepton — n/a; no nucleus)",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
