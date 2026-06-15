#!/usr/bin/env python3
"""qbeta_signed_vs_abs_tower_diagnostic.py — concrete numerical test of
the user's question (2026-06-01): "do we need the |...|?"

Per `prop:li2q-phiq-bar-symmetrization`: binding (Q_β) uses Li_2^q
without |...|; MASS absolutes (m_p, m_n, m_atom) use Φ_q with |...|.
The user asked whether the |...| is necessary.

This probe replicates the mass-tower computation at q_proton with
BOTH conventions (Φ_q(|v|) — current vs Φ_q(v) — signed) and reports
whether the difference is structurally meaningful for the c_3 saga.

DISCIPLINE. This is a DIAGNOSTIC, not a new candidate. The c_3 saga
stays open per PR #1626 + #1630 (cross-anchor under-diagnostic).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from _phi_q_util import phi_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def Phi_q(z: mpf, q: mpf, q_inv: mpf) -> mpf:
    return phi_q(z, q_inv, max_k=500)


def mass_tower_value(vols: list[mpf], q: mpf, q_inv: mpf, z_mark: mpf,
                     use_abs: bool) -> dict:
    """Compute mass-tower (Φ_q sum) with EITHER signed or abs convention.

    Replicates mass_formula_6term.py logic with a switch.
    """
    if use_abs:
        single = sum(Phi_q(abs(v), q, q_inv) for v in vols)
        pair = sum(Phi_q(abs(vols[i] * vols[i + 1]), q, q_inv)
                   for i in range(len(vols) - 1))
    else:
        single = sum(Phi_q(v, q, q_inv) for v in vols)
        pair = sum(Phi_q(vols[i] * vols[i + 1], q, q_inv)
                   for i in range(len(vols) - 1))
    pair *= z_mark ** 2
    return {"single": single, "pair": pair, "total": single + pair}


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-signed-vs-abs-tower-diagnostic",
                              engine="python+mpmath", start_time=t0)
    builder.set_description(
        "Concrete test of user's 2026-06-01 question: does dropping |...| "
        "in the mass-tower formula change Q_β at q_proton? Tests with "
        "specific synthetic vols lists (single positive, mixed-sign, "
        "all negative) to show when signed != abs."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-qbeta-signed-vs-abs-tower-diagnostic.md"
    )

    q = q_at()
    q_inv = 1 / q
    z_mark = mp.mpf(1)  # symbolic z marker

    print("=" * 78)
    print(" Signed vs |...|: mass-tower convention diagnostic at q_proton")
    print("=" * 78)
    print()
    print(f"q_proton = {fmt(q)}")
    print()

    # Test cases — different sub-braid V̂ value lists
    test_cases = [
        ("all_positive_small",      [mpf("0.1"), mpf("0.2"), mpf("0.15")]),
        ("all_positive_medium",     [mpf("0.5"), mpf("0.4"), mpf("0.3")]),
        ("mixed_sign",              [mpf("0.3"), mpf("-0.2"), mpf("0.1")]),
        ("all_negative",            [mpf("-0.1"), mpf("-0.2"), mpf("-0.15")]),
        ("one_strong_negative",     [mpf("0.4"), mpf("-0.4"), mpf("0.1")]),
        ("realistic_subbraid_vols", [mpf("0.388"), mpf("0.142"), mpf("0.025")]),  # roughly trace-like
    ]

    results = {}
    for name, vols in test_cases:
        abs_result = mass_tower_value(vols, q, q_inv, z_mark, use_abs=True)
        signed_result = mass_tower_value(vols, q, q_inv, z_mark, use_abs=False)
        diff = signed_result["total"] - abs_result["total"]
        rel_diff = float(diff / abs_result["total"]) if abs_result["total"] != 0 else float("inf")
        results[name] = {
            "vols": [str(v) for v in vols],
            "abs_total": fmt(abs_result["total"]),
            "signed_total": fmt(signed_result["total"]),
            "absolute_diff": fmt(diff),
            "relative_diff": rel_diff,
        }
        print(f"  {name}:")
        print(f"    vols = {[fmt(v) for v in vols]}")
        print(f"    abs:    total = {fmt(abs_result['total'])}")
        print(f"    signed: total = {fmt(signed_result['total'])}")
        print(f"    diff:         {fmt(diff)}  (rel: {rel_diff:.4e})")
        print()

    # SIGNED-VS-ABS verdicts
    builder.add_data("q_proton", str(q))
    builder.add_data("test_cases", results)
    builder.add_data("findings", {
        "all_positive_vols": "abs == signed (no |...| effect)",
        "any_negative_vols": "abs != signed — Φ_q(z) ≠ Φ_q(|z|) for negative z; the modulation factor differs structurally",
        "magnitude_of_difference": (
            "depends on |vols| · q^(-k) ratios; for small |v|<<q the "
            "difference is small (Φ_q ≈ 1 + |v|/q for both signs), but "
            "the LEADING ORDER coefficient flips sign for negative v"
        ),
    })

    # Compute the Φ_q(v) - Φ_q(-v) sensitivity:
    # Φ_q(v) = (1 - q^(-1)·v)^(-1) · (1 - q^(-2)·v)^(-1) · ...
    # Φ_q(-v) = (1 + q^(-1)·v)^(-1) · (1 + q^(-2)·v)^(-1) · ...
    # Ratio at small v: (1 + 2·q^(-1)·v + O(v²)) — leading O(v) difference
    test_v = mpf("0.142")  # roughly Δtr_M magnitude
    phi_pos = Phi_q(test_v, q, q_inv)
    phi_neg = Phi_q(-test_v, q, q_inv)
    phi_abs = Phi_q(abs(-test_v), q, q_inv)  # = phi_pos
    print(f"At v = ±0.142 (Δtr_M scale):")
    print(f"  Φ_q(+0.142) = {fmt(phi_pos)}")
    print(f"  Φ_q(-0.142) = {fmt(phi_neg)}")
    print(f"  Φ_q(|-0.142|) = {fmt(phi_abs)}  (= Φ_q(+0.142))")
    print(f"  Φ_q(+v) / Φ_q(-v) = {fmt(phi_pos / phi_neg)}")
    print(f"  ratio - 1 = {fmt(phi_pos / phi_neg - 1)}")
    print()
    builder.add_data("sensitivity_at_delta_tr_M_scale", {
        "v": str(test_v),
        "Phi_q_pos": str(phi_pos),
        "Phi_q_neg": str(phi_neg),
        "Phi_q_abs_same_as_pos": str(phi_abs == phi_pos),
        "ratio_pos_over_neg": str(phi_pos / phi_neg),
        "leading_order_signed_minus_abs_pct": float((phi_neg - phi_pos) / phi_pos * 100),
    })

    diff_pct = float((phi_neg - phi_pos) / phi_pos * 100)
    print(f"At Δtr_M scale, Φ_q(signed) differs from Φ_q(|...|) by {diff_pct:.4f}% per term.")
    print()

    # CONCLUSION
    builder.add_data("conclusion", (
        "Φ_q(z) ≠ Φ_q(|z|) for z < 0. At Δtr_M scale (|v|=0.142, q=1.11), "
        f"Φ_q(-v) differs from Φ_q(+v) by ~{diff_pct:.2f}% per term. "
        "If the framework's per-braid mass-tower uses Φ_q(|v|) but the "
        "categorical 'correct' formula should use Φ_q(v) signed, EACH "
        f"negative-v term contributes a {abs(diff_pct):.2f}% sign-correction. "
        "Multiple negative terms compound. "
        "For PROTON / NEUTRON mass-tower: at the level of single-nucleon "
        "tr_M values (β_p ≈ +1.07, β_n ≈ +0.92), both POSITIVE, so |...| "
        "is no-op at level 0. At deeper levels (pair joints, jets) "
        "sub-braid traces CAN be negative — the |...| would change those. "
        "WHETHER THE FRAMEWORK SHOULD USE SIGNED OR ABS is a categorical "
        "question; this probe does not answer it, only quantifies that "
        "the difference is structurally meaningful when negative-v terms "
        "appear in the tower."
    ))

    builder.add_data("implications_for_ck_saga", (
        "Indirect — c_k saga is in BINDING (Li_2^q), not MASS (Φ_q). "
        "Q_β = m_n - m_p - m_e is a mass-DIFFERENCE; both m_n and m_p "
        "use Φ_q(|...|) in their per-braid towers. If signed-vs-abs "
        "changes m_p and m_n in correlated ways, the difference Q_β "
        "could be unchanged. Quantifying this requires the full per-"
        "isotope sub-braid V̂ values for proton and neutron — out of "
        "scope for this diagnostic. Marked as FOLLOW-UP."
    ))

    builder.add_assertion(
        name="phi_q_signed_differs_from_phi_q_abs_at_delta_scale",
        computed=float(abs((phi_neg - phi_pos) / phi_pos)) > 0.01,
        expected=True,
        tolerance=0.0,
        source="Φ_q(neg z) ≠ Φ_q(|z|) confirmed numerically at v = ±0.142",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
