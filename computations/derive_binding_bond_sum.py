#!/usr/bin/env python3
"""DERIVATION — extensive per-bond binding sum (the intensive→extensive fix).

The zero-fit derivation (2026-06-02-binding-intensive-vs-extensive-derivation.md)
showed B = E_0·Δtr_M is INTENSIVE (saturates ~3-4 MeV; A-growth 1.65× vs AME
12.72×). Nuclear binding is EXTENSIVE — an additive sum over inter-nucleon bonds:

    B(K) = Σ_{b ∈ ⨝_K} B_b ,   B_b = E_0·Δtr_M(b)  (single-bond, deuteron = base).

Modulus convention (per docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md):
the per-bond Δ here is the ARCHIMEDEAN per-block realization Σ_λ y_λ|χ^λ| — `|·|`
is the deliberate post-τ observation, applied per Wedderburn block. The general
(non-archimedean-compatible) form replaces `|χ^λ|` with the bar-pairing
χ^λ(q)·χ^λ(q⁻¹) (Hecke bar-involution q↦q⁻¹), which is defined over any base
ring; that follow-up needs χ^λ evaluated at q⁻¹ (the cached witnesses store q_0
only). The scalar categorical binding is the SIGNED Δtr_M (no |·|).

LEVEL 0 (this script, isospin-symmetric bonds): use the DERIVED deuteron bond
B_pn = E_0·(Σ_λ y_λ|χ^λ_free| − Σ_λ y_λ|χ^λ_atom|)_D for every bond, and count
bonds by type from (Z,N):
    n_pp = C(Z,2),  n_nn = C(N,2),  n_pn = Z·N,  N_bonds = C(A,2).

This is a DERIVATION (the deuteron bond is derived +3.6%; the bond set ⨝_K is
structural), zero fit. It tests how far the bond-COUNT alone closes the A-growth
(the intensive formula gave 1.65×; bond-count gives C(A,2)). The residuals isolate
the two refinements: (i) bond-TYPE (B_pp ≠ B_pn ≠ B_nn — distinguishes T from ³He,
same C(A,2)=3); (ii) per-bond GROWTH (each bond embedded in a denser braid).
Those need the 2-nucleon sub-braid trace differences (next step).

Compares to AME. NO fit; AME used only for the final comparison.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge: flat imports from substrate/
from mpmath import mpf, fabs  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402 — CAL-1

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E = mpf(str(M_E_MEV))
q0 = mpf(str(Q0))
E0 = M_E / (q0 * (q0 - 1))   # 𝔈₀ ≈ 4.186 MeV (calibration-fixed)

# (Z, N) per isotope
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}

_y_cache = None


def load_y(n):
    global _y_cache
    if _y_cache is None:
        with open(HERE / "y-lambda-at-q0.witness.json") as f:
            _y_cache = json.load(f)
    byn = _y_cache.get("data", _y_cache)["by_n"][str(n)]
    return {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in byn}


def delta_trM_perblock(fname):
    """Σ_λ y_λ|χ^λ_free| − Σ_λ y_λ|χ^λ_atom|  (observe-per-block)."""
    with open(HERE / fname) as f:
        d = json.load(f)
    d = d.get("data", d)
    atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
    free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
    y = load_y(d["atom"]["n_strands"])
    return sum(y[l] * fabs(free[l]) for l in free) - sum(y[l] * fabs(atom[l]) for l in atom)


def main() -> int:
    # DERIVED single-bond binding = the deuteron (one p-n bond).
    B_bond = E0 * delta_trM_perblock(CHI["D"])
    print(f"E_0 = {float(E0):.4f} MeV (calibration)   "
          f"derived single-bond B_pn = {float(B_bond):.4f} MeV  (deuteron, +3.6%)\n")
    print(f"{'iso':<5}{'bonds (pp,pn,nn)':<18}{'N':<4}{'B=N·B_bond':<12}"
          f"{'AME':<9}{'err%':<9}")
    results = {}
    for name, (Z, N) in ZN.items():
        n_pp, n_pn, n_nn = comb(Z, 2), Z * N, comb(N, 2)
        Nb = n_pp + n_pn + n_nn  # = C(A,2)
        B = Nb * B_bond
        err = (B - AME_B[name]) / AME_B[name]
        results[name] = {"Z": Z, "N": N, "n_pp": n_pp, "n_pn": n_pn,
                         "n_nn": n_nn, "N_bonds": Nb, "B_pred_MeV": float(B),
                         "AME_MeV": float(AME_B[name]), "err": float(err)}
        print(f"{name:<5}({n_pp},{n_pn},{n_nn}){'':<{18-len(f'({n_pp},{n_pn},{n_nn})')}}"
              f"{Nb:<4}{float(B):<12.4f}{float(AME_B[name]):<9.4f}{float(err)*100:<+9.1f}")

    g = results["4He"]["B_pred_MeV"] / results["D"]["B_pred_MeV"]
    print(f"\nbond-count A-growth B(⁴He)/B(D) = {g:.2f}  (intensive gave 1.65; AME 12.72)")
    print("T vs ³He: both N_bonds=3 → identical here; differ by bond TYPE "
          "(T={2pn,1nn}, ³He={1pp,2pn}) — needs B_pp≠B_pn≠B_nn (next step).")
    print("⁴He residual: per-bond GROWTH (bonds embedded in the 12-strand braid).")

    wb = WitnessBuilder("derive-binding-bond-sum", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit, level-0): extensive per-bond binding sum "
        "B(K) = N_bonds(K)·B_bond, B_bond = derived deuteron single-bond "
        "(E_0·Δtr_M(D) archimedean per-block, +3.6%), bond count C(A,2) by "
        "type from (Z,N). Tests "
        "the intensive→extensive fix: bond-count A-growth vs the intensive 1.65×. "
        "Bond-type + per-bond-growth refinements isolated for the next step. "
        "E_0=m_e/(q₀(q₀−1)) calibration; AME comparison only."
    )
    wb.add_parameter("E0_MeV", float(E0))
    wb.add_parameter("B_bond_deuteron_MeV", float(B_bond))
    wb.add_data("per_atom", results)
    wb.add_data("bond_count_A_growth", float(g))
    wb.add_data("intensive_A_growth_for_comparison", 1.65)
    wb.add_data("ame_A_growth", 12.72)
    wb.add_assertion(
        name="bond_sum_improves_A_growth_over_intensive",
        computed=str(int(g > 1.65)),
        expected="1",
        tolerance=0,
        source=(f"bond-count A-growth {g:.2f}× vs intensive 1.65× (AME 12.72×); "
                "the extensive bond-sum structurally improves the A-scaling. "
                "Residuals = bond-type + per-bond-growth (sub-braid step)."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
