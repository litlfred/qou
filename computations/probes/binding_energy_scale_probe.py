#!/usr/bin/env python3
"""
binding_energy_scale_probe.py — test E₀ vs Q_β as binding energy scale.

FINDING: Switching from Q_β = 0.784 MeV to E₀ = m_e/(q₀(q₀-1)) = 4.186 MeV
closes the deuteron binding error from -79% to +12%.

The +12% residual on deuteron is a per-composite correction —
likely the Hoefsmit off-diagonal contribution at the H₆ level.

For heavier nuclei (T, ³He, ⁴He), additional A-dependent structure
is needed beyond a simple energy-scale rescale.
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

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION, M_E_MEV  # noqa: E402
from codata_constants import AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)


def main():
    set_compute_dps()

    q = mpf(Q_50_DIGIT_STR)
    h = q - 1 / q

    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E_0 = _qbeta_e0.order_zero_scaled(M_E_MEV, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    Q_beta = M_E_MEV * fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    scale_ratio = E_0 / Q_beta

    # Binding values from mass_table_comprehensive (Q_β scale)
    isotopes = {
        "D":   {"B_qbeta": 0.465676, "B_AME": 2.22452, "A": 2, "Z": 1, "N": 1},
        "T":   {"B_qbeta": 0.628974, "B_AME": float(AME_B_TRITIUM_MEV_VALIDATION), "A": 3, "Z": 1, "N": 2},
        "3He": {"B_qbeta": 0.658111, "B_AME": AME_B_HE3_MEV_VALIDATION, "A": 3, "Z": 2, "N": 1},
        "4He": {"B_qbeta": 0.713469, "B_AME": float(AME_B_HE4_MEV_VALIDATION), "A": 4, "Z": 2, "N": 2},
    }

    # Correction candidates for the +12% deuteron residual
    hbar_q = (q - 1) / q
    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    corrections = {
        "none": 1,
        "1/(1+h²)": 1 / (1 + h ** 2),
        "b²": b_sq,
        "[2]_q/([2]_q+1)": (q + 1 / q) / (q + 1 / q + 1),
        "1-hbar_q": 1 - hbar_q,
        "4/[2]_q²": 4 / (q + 1 / q) ** 2,
    }

    wb = WitnessBuilder("binding-energy-scale-probe", engine="mpmath")
    wb.set_description(
        "Probe E₀ vs Q_β as binding energy scale. E₀ = m_e/(q₀(q₀-1)) closes "
        "deuteron from -79% to +12%. Residual +12% candidates tested."
    )

    print("=" * 70)
    print("BINDING ENERGY SCALE PROBE")
    print(f"E₀ = {float(E_0):.6f} MeV, Q_β = {float(Q_beta):.6f} MeV, ratio = {float(scale_ratio):.4f}")
    print("=" * 70)
    print()

    results = {}
    for name, data in isotopes.items():
        b_e0 = data["B_qbeta"] * float(scale_ratio)
        err_qb = (data["B_qbeta"] / data["B_AME"] - 1) * 100
        err_e0 = (b_e0 / data["B_AME"] - 1) * 100
        results[name] = {"B_E0": b_e0, "err_qb": err_qb, "err_e0": err_e0}
        print(f"  {name:>4s}: B(Q_β)={data['B_qbeta']:.3f}, B(E₀)={b_e0:.3f}, "
              f"B_AME={data['B_AME']:.3f}  err: {err_qb:+.1f}% → {err_e0:+.1f}%")

    print()
    print("=== Deuteron correction scan ===")
    d_b_e0 = isotopes["D"]["B_qbeta"] * float(scale_ratio)
    d_ame = isotopes["D"]["B_AME"]
    best_name = ""
    best_err = 100.0
    for cname, cval in corrections.items():
        b_corr = d_b_e0 * float(cval)
        err = (b_corr / d_ame - 1) * 100
        marker = " ← BEST" if abs(err) < abs(best_err) else ""
        if abs(err) < abs(best_err):
            best_err = err
            best_name = cname
        print(f"  {cname:25s}: B = {b_corr:.4f} MeV, err = {err:+.2f}%{marker}")

    wb.add_data("energy_scales", {
        "E_0_MeV": str(float(E_0)),
        "Q_beta_MeV": str(float(Q_beta)),
        "ratio": str(float(scale_ratio)),
    })
    wb.add_data("isotope_results", {
        k: {"B_E0": v["B_E0"], "err_E0_pct": v["err_e0"], "err_Qbeta_pct": v["err_qb"]}
        for k, v in results.items()
    })
    wb.add_data("deuteron_corrections", {
        "best_correction": best_name,
        "best_err_pct": best_err,
    })

    wb.add_assertion(
        "E0_improves_deuteron",
        computed=abs(results["D"]["err_e0"]),
        expected=0,
        tolerance=abs(results["D"]["err_qb"]),
        source="E₀ scale beats Q_β scale for deuteron",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()
    print(f"\n✓ Best deuteron correction: {best_name} ({best_err:+.2f}%)")


if __name__ == "__main__":
    main()
