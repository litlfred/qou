#!/usr/bin/env python3
"""DERIVATION — bond-TYPE per-bond binding sum (level 1, pure-Python, 0 fit).

Level-0 (derive_binding_bond_sum.py) used one isospin-symmetric bond and got
A-growth 1.65×→6.00×, but couldn't distinguish T from ³He (both C(A,2)=3). This
level derives the three bond TYPES from their 2-nucleon sub-braids and sums by
composition:

    B(K) = n_pp·B_pp + n_pn·B_pn + n_nn·B_nn ,
    B_xy = E_0 · ( tr_M(W_free^{xy}) − tr_M(W_atom^{xy}) ) ,   xy ∈ {pp, pn, nn},

with the 2-nucleon traces from the canonical pure-Python Markov trace
(binding_canonical.binding_canonical(Z,N): pn=(1,1)=deuteron, pp=(2,0)=diproton,
nn=(0,2)=dineutron) and E_0 = m_e/(q₀(q₀−1)) ≈ 4.186 MeV (calibration-fixed). The
deuteron (pn) is the derived base case. Bond composition from (Z,N):
    n_pp = C(Z,2),  n_nn = C(N,2),  n_pn = Z·N.

ZERO fit. AME used only for the final comparison.

Note: this uses the SCALAR signed Δtr_M (collapse-first; the double-modulus
|tr_free|−|tr_atom| was a non-archimedean misuse, see
2026-06-01-paper-modulus-nonarchimedean-audit). The observe-per-block
Σ_λ y_λ|χ^λ| version (deuteron +3.6% vs scalar +12%; |·| is the archimedean
per-block realization, bar-pairing χ^λ(q)·χ^λ(q⁻¹) is the general form) and
the per-bond GROWTH
(bonds embedded in the A-nucleon braid, the ⁴He residual) both need the Rust
per-partition χ kernel (CI) — this level isolates the bond-TYPE effect, which is
the T-vs-³He discriminator.
"""
from __future__ import annotations

from math import comb
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge
from mpmath import mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402 — CAL-1
import binding_canonical as bc  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E = mpf(str(M_E_MEV))
q0 = mpf(str(Q0))
E0 = M_E / (q0 * (q0 - 1))   # 𝔈₀ ≈ 4.186 MeV (calibration-fixed)

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
BOND_ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}


def bond_binding(Z, N):
    """E_0·(tr_M_free − tr_M_atom) for the 2-nucleon (Z,N) sub-braid.

    SIGNED categorical trace difference; the double-modulus form
    |tr_free|−|tr_atom| was a non-archimedean misuse (see
    docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md). Both
    traces are positive at q_0 → value-preserving and sign-correct.
    """
    r = bc.binding_canonical(Z, N)
    # `tr_M_*` are stored as STRINGS; a complex trace would serialize as
    # "(re+imj)" which mpf() cannot parse. Parse via complex() and take
    # the real part (archimedean projection, Im(q_0)=0) for robustness.
    # NB: Gemini's literal `r["tr_M_free"].real` is wrong here — the value
    # is a str, which has no `.real`; complex(str).real is the fix.
    tr_f = mpf(str(complex(r["tr_M_free"]).real))
    tr_a = mpf(str(complex(r["tr_M_atom"]).real))
    return E0 * (tr_f - tr_a)


def main() -> int:
    B = {xy: bond_binding(*zn) for xy, zn in BOND_ZN.items()}
    print(f"E_0 = {float(E0):.4f} MeV (calibration)\n")
    print("Derived per-bond-type binding (E_0·Δtr_M, scalar, 0 fit):")
    for xy in ("pp", "pn", "nn"):
        print(f"    B_{xy} = {float(B[xy]):.4f} MeV   ({BOND_ZN[xy]})")
    print(f"  ordering: B_pp={float(B['pp']):.4f} < B_pn={float(B['pn']):.4f} "
          f"< B_nn={float(B['nn']):.4f}\n")

    print(f"{'iso':<5}{'(pp,pn,nn)':<14}{'B_pred':<10}{'AME':<10}{'err%':<9}")
    results = {}
    for name, (Z, N) in ZN.items():
        npp, npn, nnn = comb(Z, 2), Z * N, comb(N, 2)
        Bk = npp * B["pp"] + npn * B["pn"] + nnn * B["nn"]
        err = (Bk - AME_B[name]) / AME_B[name]
        results[name] = {"n_pp": npp, "n_pn": npn, "n_nn": nnn,
                         "B_pred_MeV": float(Bk), "AME_MeV": float(AME_B[name]),
                         "err": float(err)}
        print(f"{name:<5}({npp},{npn},{nnn}){'':<{14-len(f'({npp},{npn},{nnn})')}}"
              f"{float(Bk):<10.4f}{float(AME_B[name]):<10.4f}{float(err)*100:<+9.1f}")

    # T vs ³He ordering check (the bond-type discriminator)
    t_gt_he3 = results["T"]["B_pred_MeV"] > results["3He"]["B_pred_MeV"]
    ame_t_gt = float(AME_B["T"]) > float(AME_B["3He"])
    print(f"\nT vs ³He ordering: pred B_T {'>' if t_gt_he3 else '≤'} B_³He ; "
          f"AME B_T {'>' if ame_t_gt else '≤'} B_³He — "
          f"{'MATCHES' if t_gt_he3 == ame_t_gt else 'MISMATCH'}")
    g = results["4He"]["B_pred_MeV"] / results["D"]["B_pred_MeV"]
    print(f"A-growth B(⁴He)/B(D) = {g:.2f}  (level-0 6.00; AME 12.72)")
    print("Residual = per-bond GROWTH (⁴He bonds embedded in 12-strand braid); "
          "needs embedded sub-braid χ (Rust kernel, CI).")

    wb = WitnessBuilder("derive-binding-bond-type", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit, level-1): bond-TYPE per-bond binding sum "
        "B(K)=n_pp·B_pp+n_pn·B_pn+n_nn·B_nn, B_xy=E_0·Δtr_M of the 2-nucleon "
        "(Z,N) sub-braid (pure-Python canonical Markov trace; pn=deuteron). "
        "E_0=m_e/(q₀(q₀−1)) calibration. Isolates the bond-type T-vs-³He "
        "discriminator; per-block + per-bond-growth need the Rust χ kernel."
    )
    wb.add_parameter("E0_MeV", float(E0))
    wb.add_data("bond_type_binding_MeV",
                {xy: float(B[xy]) for xy in BOND_ZN})
    wb.add_data("per_atom", results)
    wb.add_data("t_he3_ordering_matches", bool(t_gt_he3 == ame_t_gt))
    wb.add_data("A_growth", float(g))
    wb.add_assertion(
        name="bond_type_reproduces_T_He3_ordering",
        computed=str(int(t_gt_he3 == ame_t_gt)),
        expected="1",
        tolerance=0,
        source=(f"bond-type sum gives B_T={results['T']['B_pred_MeV']:.3f} vs "
                f"B_³He={results['3He']['B_pred_MeV']:.3f}; AME 8.48 vs 7.72 — "
                f"ordering {'matches' if t_gt_he3==ame_t_gt else 'MISMATCH'} "
                "(the bond-type discriminator, 0 fit)."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
