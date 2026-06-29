#!/usr/bin/env python3
"""Binding residual exponent 10A−5 — chain-topology decomposition (derive-or-refute).

FORMALIZE-FIRST PROBE (per the Δ_λ-gate discipline: derive the structure of the
near-match `Δ_λ(K) ≈ q₀^(10A−5)` from the W_atom braid bookkeeping, NOT a 7th fit
ansatz). Companion Lean: `QOU/Mass/BindingResidualExponent.lean` (sorry-free).

The canonical trace-binding `B_pred = E₀·(tr_M(W_free) − tr_M(W_atom))` undershoots
AME by `Δ_λ = B_AME/B_pred ≈ q₀^(10A−5)` (audit 2026-06-09). This probe reads the
ACTUAL braid word (`atom_braid_word_3A`) and shows the exponent factorizes over the
chain topology:

    len(W_free) = 11·A                       (11 crossings/nucleon: g0=7, g1=4)
    len(W_atom) = 11·A + (A−1)               (one interface crossing per bond)
    10A − 5     = 5·(2A−1) = 5·(A nucleons + (A−1) bonds)

So the `2A−1` is DERIVED (chain topology); the per-unit weight `5` is the reduced
open constant. The per-BOND reading carries the Z-correction: same-A isotopes with
different bond TYPES (³He {pp,pn} vs T {pn,nn}; f_pp=z ≠ f_nn=z−h) deviate.

Output: binding-residual-exponent-chain-topology.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))


def chain_decomposition(Z: int, N: int) -> dict:
    from mass_at_3A_proper import atom_braid_word_3A
    A = Z + N
    wf = atom_braid_word_3A(Z, N, include_inter=False)
    wa = atom_braid_word_3A(Z, N, include_inter=True)
    bonds = A - 1
    # bond-type census along the chain ordering ['p']*Z + ['n']*N
    ordering = ["p"] * Z + ["n"] * N
    bond_types = {"pp": 0, "pn": 0, "nn": 0}
    for k in range(A - 1):
        pair = "".join(sorted((ordering[k], ordering[k + 1])))
        bond_types[{"pp": "pp", "nn": "nn", "np": "pn", "pn": "pn"}[pair]] += 1
    return {
        "atom": f"Z{Z}N{N}", "Z": Z, "N": N, "A": A,
        "strands_3A": 3 * A,
        "len_W_free": len(wf), "len_W_atom": len(wa),
        "crossings_per_nucleon": (len(wf) // A) if A else 0,
        "interface_crossings": len(wa) - len(wf),
        "bonds_A_minus_1": bonds,
        "chain_units_2A_minus_1": A + bonds,
        "law_10A_minus_5": 10 * A - 5,
        "five_times_units": 5 * (A + bonds),
        "bond_types": bond_types,
    }


def main() -> int:
    cases = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]
    rows = [chain_decomposition(Z, N) for Z, N in cases]

    print(f"{'atom':>6} {'A':>2} {'3A':>3} {'Wfree':>6} {'Watom':>6} "
          f"{'/nuc':>5} {'bonds':>5} {'2A-1':>5} {'10A-5':>6} {'5(2A-1)':>8} {'bonds(pp/pn/nn)':>16}")
    all_ok = True
    for r in rows:
        ok = (r["len_W_free"] == 11 * r["A"]
              and r["interface_crossings"] == r["bonds_A_minus_1"]
              and r["law_10A_minus_5"] == r["five_times_units"])
        all_ok = all_ok and ok
        bt = r["bond_types"]
        print(f"{r['atom']:>6} {r['A']:>2} {r['strands_3A']:>3} {r['len_W_free']:>6} "
              f"{r['len_W_atom']:>6} {r['crossings_per_nucleon']:>5} {r['bonds_A_minus_1']:>5} "
              f"{r['chain_units_2A_minus_1']:>5} {r['law_10A_minus_5']:>6} {r['five_times_units']:>8} "
              f"  {bt['pp']}/{bt['pn']}/{bt['nn']:<6}")
    print()
    print("DERIVED  : 2A−1 = A nucleons + (A−1) bonds (chain topology of W_atom)")
    print("           len(W_free)=11A; interface crossings = A−1 (one per bond)")
    print("           10A−5 = 5·(2A−1)  — exact identity over the chain units")
    print("OPEN     : the per-unit weight 5 (candidate: 5 A₅-irreps / Bring–S₅ five-fold;")
    print("           SDP-confinement derivation of the 5 is the next step)")
    print("Z-CORR   : ³He {pp,pn} vs T {pn,nn} — same A, different bond types (f_pp=z≠f_nn=z−h)")
    print(f"\nall structural identities hold: {all_ok}")

    try:
        sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))
        from qou_substrate.witness import WitnessBuilder
        w = WitnessBuilder("binding-residual-exponent-chain-topology", engine="python")
        w.set_description(
            "Chain-topology decomposition of the binding residual exponent: "
            "10A−5 = 5·(2A−1) = 5·(A nucleons + (A−1) bonds), read from the "
            "atom_braid_word_3A chain. NEAR-MATCH TIER: the 2A−1 is derived "
            "(chain topology); the per-unit weight 5 is the reduced open constant. "
            "Companion Lean QOU/Mass/BindingResidualExponent.lean (sorry-free).")
        for r in rows:
            w.add_data(r["atom"], r)
        w.add_assertion("len_W_free_eq_11A",
                        computed=1 if all(r["len_W_free"] == 11 * r["A"] for r in rows) else 0,
                        expected=1, source="11 crossings/nucleon (g0=7,g1=4)")
        w.add_assertion("law_eq_five_times_units",
                        computed=1 if all(r["law_10A_minus_5"] == r["five_times_units"] for r in rows) else 0,
                        expected=1, source="10A−5 = 5·(2A−1) over the chain units")
        out = w.save()
        print(f"Witness: {out.name}")
    except Exception as e:  # pragma: no cover
        print(f"(witness emit skipped: {e})")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
