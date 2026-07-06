#!/usr/bin/env python3
"""DERIVATION — chain (A−1) pairwise bond-sum and the many-body residual.

The canonical braid is a CHAIN of A−1 inter-nucleon interfaces (verified from
atom_braid_word_3A: interface at gen 3k+2, k=0..A−2). This sums the DERIVED
per-bond-type bindings over the chain's adjacency, and isolates the residual
B_AME − B_chain — which is the irreducible MANY-BODY (3-/4-body) cooperative
binding the pairwise sum cannot contain.

    B_chain(K) = Σ_{adjacent pairs in the chain} B_xy ,
    B_xy = E_0·(tr_M_free − tr_M_atom)  for the 2-nucleon (Z,N) sub-braid
    (SIGNED categorical trace difference; the double-modulus |·|−|·| was a
    non-archimedean misuse, see 2026-06-01-paper-modulus-nonarchimedean-audit).

Chains (by adjacency): D = p–n; T = p–n–n; ³He = p–p–n; ⁴He = p–p–n–n.
E_0 = m_e/(q₀(q₀−1)) calibration. ZERO fit; AME for comparison only.

Finding: the pairwise chain-sum captures the T/³He ordering and the deuteron,
but under-binds — strongly for ⁴He (residual ~20.9 MeV = the 4-body α-binding).
The "per-bond embedding growth" sought earlier is NOT a per-bond correction; it
is many-body cooperativity (the α-unit), beyond ANY pairwise sum. This localizes
the open derivation precisely: sub-α (A≤3) has a pairwise path; ⁴He is the
irreducible 4-body α-unit (consistent with the α-cluster recursion treating ⁴He
as the magic input).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge
from mpmath import mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402 — CAL-1
import binding_canonical as bc  # noqa: E402

set_compute_dps()
M_E = mpf(str(M_E_MEV))
q0 = mpf(str(Q0))
E0 = M_E / (q0 * (q0 - 1))

AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
BOND_ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}
# chain adjacency (canonical braid wires nucleons in a chain)
CHAIN = {"D": ["pn"], "T": ["pn", "nn"], "3He": ["pp", "pn"],
         "4He": ["pp", "pn", "nn"]}


def bond_binding(Z, N, E0):
    # SIGNED categorical trace difference (the double-modulus form
    # |tr_free|−|tr_atom| was a non-archimedean misuse — see
    # docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md). Both
    # traces are positive at q_0, so this is value-preserving and keeps
    # the binding sign.
    r = bc.binding_canonical(Z, N)
    # `tr_M_*` are stored as STRINGS; parse via complex() and take the
    # real part (archimedean projection, Im(q_0)=0) so a complex trace
    # repr "(re+imj)" cannot crash mpf(). (complex(str).real, not the
    # str's nonexistent `.real` — cf. Gemini review on PR #1738.)
    tr_f = mpf(str(complex(r["tr_M_free"]).real))
    tr_a = mpf(str(complex(r["tr_M_atom"]).real))
    return E0 * (tr_f - tr_a)


def main() -> int:
    B = {xy: bond_binding(*zn, E0) for xy, zn in BOND_ZN.items()}
    print(f"E_0 = {float(E0):.4f} MeV   bond bindings: "
          f"pp={float(B['pp']):.3f} pn={float(B['pn']):.3f} nn={float(B['nn']):.3f}\n")
    print(f"{'iso':<5}{'chain bonds':<16}{'B_chain':<10}{'AME':<9}{'err%':<9}"
          f"{'many-body resid':<16}")
    results = {}
    for name, bonds in CHAIN.items():
        Bc = sum(B[b] for b in bonds)
        resid = AME_B[name] - Bc
        err = (Bc - AME_B[name]) / AME_B[name]
        results[name] = {"chain_bonds": bonds, "B_chain_MeV": float(Bc),
                         "AME_MeV": float(AME_B[name]), "err": float(err),
                         "many_body_residual_MeV": float(resid),
                         "fraction_pairwise": float(Bc / AME_B[name])}
        print(f"{name:<5}{str(bonds):<16}{float(Bc):<10.3f}{float(AME_B[name]):<9.3f}"
              f"{float(err)*100:<+9.1f}{float(resid):<16.3f}")

    t_gt = results["T"]["B_chain_MeV"] > results["3He"]["B_chain_MeV"]
    print(f"\nT/³He ordering (chain): B_T {'>' if t_gt else '≤'} B_³He — "
          f"{'matches AME' if t_gt else 'MISMATCH'} (AME 8.48 > 7.72)")
    print(f"⁴He pairwise fraction = {results['4He']['fraction_pairwise']*100:.0f}% "
          f"→ residual {results['4He']['many_body_residual_MeV']:.1f} MeV is the "
          "irreducible 4-body α-binding (beyond pairwise).")

    wb = WitnessBuilder("derive-binding-chain-cooperative", engine="mpmath")
    wb.set_description(
        "DERIVATION (0 fit): chain (A−1) pairwise bond-sum over the canonical "
        "braid's adjacency, and the many-body residual B_AME − B_chain. Bond "
        "types from binding_canonical (pp/pn/nn 2-nucleon sub-braids), E_0 "
        "calibration. Localizes: sub-α (A≤3) pairwise path + T/³He ordering; "
        "⁴He residual ~20.9 MeV = irreducible 4-body α-binding (beyond pairwise)."
    )
    wb.add_parameter("E0_MeV", float(E0))
    wb.add_data("bond_type_binding_MeV", {k: float(v) for k, v in B.items()})
    wb.add_data("per_atom", results)
    wb.add_data("he4_pairwise_fraction", results["4He"]["fraction_pairwise"])
    wb.add_assertion(
        name="he4_binding_is_majority_many_body",
        computed=str(int(results["4He"]["fraction_pairwise"] < 0.5)),
        expected="1",
        tolerance=0,
        source=(f"⁴He pairwise chain-sum = {results['4He']['fraction_pairwise']*100:.0f}% "
                f"of AME; residual {results['4He']['many_body_residual_MeV']:.1f} MeV is "
                "irreducible many-body (4-body α) binding — the pairwise bond-sum "
                "cannot contain it. Sub-α (A≤3) keeps the pairwise path + ordering."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
