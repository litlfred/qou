#!/usr/bin/env python3
"""Trace-level bar product tr_M(q₀)·tr_M(q₀⁻¹) as a binding object — HONEST NEGATIVE.

EXPLORATORY (no production wiring). Tests the owner's proposed binding
object: the **non-archimedean bar product at the TRACE level**,
`tr_M(q₀)·ȟtr_M = tr_M(q₀)·tr_M(q₀⁻¹)` (real, base-ring-defined), as
distinct from #1742's *per-block* bar `Σ_λ y_λ√(χ·barχ)` (which goes
imaginary per-block, −70.3%).

Machinery (validated): the matrix-M Markov trace at ARBITRARY q via the
native bindings — `tr_M(β_K, q) = Σ_{λ⊢3A} y_λ(q)·χ^λ(β_K; q)` with
`pyhecke_native.trace_weights_n(3A, q)` and
`pyhecke_native.chi_via_matrix_m_mpfr(λ, word_left, bridge_sign,
word_right, k_split=3, q_str, dps)`. CROSS-CHECK: tr_M(deuteron, q₀)
reproduces the catalogue witness 1.3317821792991125 to <1e-9, validating
the q-agnostic wiring → the q₀⁻¹ value is trustworthy.

RESULT (deuteron): tr_M(q₀)=1.332 but tr_M(q₀⁻¹)=0.000291 (the q<1 mirror
is tiny), so the bar product = 0.000387 and the required Δ'=B/(m_e·BP) =
11245 — i.e. it **underbinds massively**, far worse than signed-tr_M
(Δ̄=3.27) or #1742's archimedean |·| (+3.6%). Conclusion: the trace-level
bar product is NOT the binding realization; #1742's bar negative extends
from per-block to the trace. (Records the negative so nobody re-tries it.)

Output: atom-vhyp-bar-trace-test.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))

import pyhecke_native as nat  # noqa: E402
from chi_at_q0_via_matrix_m_mpfr import _split_atom_braid  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV as _M_E  # noqa: E402

mp.mp.dps = 55
DPS = 50
K_SPLIT = 3  # proton|neutron parabolic split (chi_at_q0_via_matrix_m_mpfr:124)
M_E = float(_M_E)

# AME2020 binding (MeV), same source as ame-2020-binding-energies.witness.json
AME_B = {"deuteron": (1, 1, float(AME_B_DEUTERON_MEV_VALIDATION)), "tritium": (1, 2, float(AME_B_TRITIUM_MEV_VALIDATION))}
TRM_Q0_WITNESS = {"deuteron": mp.mpf("1.3317821792991125061382939027504490778795270468692")}


def tr_M(Z: int, N: int, q) -> mp.mpf:
    n, wl, bs, wr = _split_atom_braid(Z, N)
    qs = mp.nstr(q, DPS + 3, strip_zeros=False)
    parts = nat.partitions_of(n)
    y = nat.trace_weights_n(n, float(q))   # native y_λ wants a float q
    tot = mp.mpf(0)
    for lam, ylam in zip(parts, y):
        chi = mp.mpf(nat.chi_via_matrix_m_mpfr(list(lam), wl, bs, wr, K_SPLIT, qs, DPS))
        tot += mp.mpf(str(ylam)) * chi
    return tot


def main() -> int:
    t0 = time.monotonic()
    q0 = q_at(50)
    qi = 1 / q0
    rows = []
    cross_ok = None
    for label, (Z, N, B) in AME_B.items():
        # tritium (n=9) is minutes-slow; gate it behind an env flag
        import os
        if label == "tritium" and os.environ.get("QOU_BAR_INCLUDE_T") != "1":
            rows.append({"label": label, "status": "skipped (set QOU_BAR_INCLUDE_T=1; n=9 slow)"})
            continue
        tq0 = tr_M(Z, N, q0)
        if label in TRM_Q0_WITNESS:
            cross_ok = bool(abs(tq0 - TRM_Q0_WITNESS[label]) < mp.mpf("1e-9"))
        tqi = tr_M(Z, N, qi)
        BP = tq0 * tqi
        delta_bar_prod = B / (M_E * BP)        # required Δ' for the bar product
        delta_signed = B / (M_E * tq0)         # #2082 signed-tr_M comparison
        rows.append({
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "B_AME_MeV": B,
            "tr_M_q0": mp.nstr(tq0, 18),
            "tr_M_q0_inv": mp.nstr(tqi, 18),
            "bar_product": mp.nstr(BP, 12),
            "m_e_times_BP_MeV": mp.nstr(M_E * BP, 8),
            "required_delta_bar_product": mp.nstr(delta_bar_prod, 8),
            "required_delta_signed_trM": mp.nstr(delta_signed, 8),
        })

    w = WitnessBuilder("atom-vhyp-bar-trace-test", engine="mpmath", start_time=t0)
    w.set_description(
        "Trace-level bar product tr_M(q₀)·tr_M(q₀⁻¹) as a binding object — "
        "HONEST NEGATIVE (EXPLORATORY). Validated matrix-M tr_M at arbitrary q "
        "(cross-check tr_M(deuteron,q₀)=1.33178 vs catalogue). The q<1 mirror "
        "tr_M(q₀⁻¹)≈0.0003 is tiny → the bar product underbinds (deuteron "
        "required Δ'≈11245, vs signed-tr_M 3.27, vs #1742 archimedean |·| "
        "+3.6%). The q→q⁻¹ bar is not the binding realization at any level."
    )
    w.add_data("rows", rows)
    w.add_data("k_split", K_SPLIT)
    w.add_data("conclusion", (
        "trace-level bar product REJECTED as the binding object: tr_M(q₀⁻¹) "
        "is tiny (q<1), so it underbinds far worse than signed-tr_M (#2082) "
        "or the archimedean |·| (#1742). Confirms #1742's per-block bar "
        "negative extends to the trace level. Mirror-trace machinery (tr_M at "
        "arbitrary q via native matrix-M) is validated and reusable."
    ))
    w.add_assertion(
        name="matrixM_trM_q0_crosscheck",
        computed=1.0 if cross_ok else 0.0, expected=1.0, tolerance=0.0,
        source="tr_M(deuteron,q₀) == catalogue 1.3317821792991125 (<1e-9)",
    )
    out = w.save()
    print(f"cross-check tr_M(deuteron,q0) matches catalogue: {cross_ok}")
    for r in rows:
        if "bar_product" in r:
            print(f"  {r['label']:9s}  tr_M(q0)={r['tr_M_q0'][:8]}  "
                  f"tr_M(q0^-1)={r['tr_M_q0_inv'][:10]}  "
                  f"Δ'_bar={r['required_delta_bar_product']}  "
                  f"(Δ_signed={r['required_delta_signed_trM']})")
    print("CONCLUSION: trace-level bar product underbinds → rejected (honest negative).")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
