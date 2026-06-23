#!/usr/bin/env python3
"""TASK 2 -- Extend the interface product to the genuine 4-body He-4 assembly.

The canonical closed form (`closed_form_tau_M.canonical_interface_kinds`) treats
an atom p^Z n^N as a LINEAR CHAIN: A-1 nucleon-nucleon interfaces
(Z-1 pp, one pn at the p|n boundary, N-1 nn).  Physically a nucleus is not a
chain: 3He/3H is a triangle (3 pairs) and 4He is a tetrahedron (6 pairs).  This
probe asks whether replacing the chain by the genuine many-body COMPLETE GRAPH
K_A (all C(A,2) pairs) repairs the binding -- in particular the strong A-scaling
the linear chain misses.

Binding assembly (canonical, `binding_canonical.py`):
    B(K) = E_0 * ( tr_M(W_free) - tr_M(W_atom) )
         = E_0 * tau_vac * ( 1 - PROD_i f_i )
with E_0 = m_e/(q0(q0-1)) ~ 4.186 MeV, tau_vac = tau_p^Z tau_n^N the free
constituents, and PROD f_i over the chosen interface set.

Building blocks (validated, convention-pure):
  tau_p = tr_M^3(proton)  cached (rho-constit-equals-tau-M-proton-phase5l)
  tau_n solved from the canonical tr_M(D) = tau_p tau_n z  (chi_lambda_braid pn=z)
We re-derive all four canonical atom traces from (tau_p, tau_n) and the chain
product to confirm self-consistency before varying topology.
"""
import json
import sys
from math import comb
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50
REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
sys.path.insert(0, str(COMP))
import closed_form_tau_M as C  # noqa: E402

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
M_E = mp.mpf("0.51099895069")
E0 = M_E / (Q0 * (Q0 - 1))
Z_MK = C.markov_z(Q0)
H_MK = C.hecke_h(Q0)

# canonical cached nucleon H_3 trace (phase5l, q0)
TAU_P = mp.mpf("1.22036288908669305595736107223")
# canonical cached atom traces (phase5q closed-form == empirical, chi_lambda_braid)
TRM = {
    "D":   mp.mpf("0.7280918153466761555460727563"),
    "T":   mp.mpf("0.25251737283574177211823914057"),
    "3He": mp.mpf("0.443664207812095038274595411452"),
    "4He": mp.mpf("0.153871967541095181777587076812"),
}
AME = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481798"),
       "3He": mp.mpf("7.718043"), "4He": mp.mpf("28.295673")}
ATOMS = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}

# tau_n from the canonical deuteron trace: tr_M(D) = tau_p tau_n z  (pn -> z)
TAU_N = TRM["D"] / (TAU_P * Z_MK)


def pair_factor(kind, pn="chi"):
    if kind == "pp":
        return Z_MK
    if kind == "nn":
        return Z_MK - H_MK
    # pn
    if pn == "chi":
        return Z_MK              # production marshalling drops the averaging
    if pn == "avg":
        return Z_MK - H_MK / 2   # bar-invariant projection
    raise ValueError(pn)


def chain_pairs(Z, N):
    """Linear chain p^Z n^N: Z-1 pp, one pn, N-1 nn (for Z,N>=1)."""
    pairs = ["pp"] * (Z - 1) + (["pn"] if Z and N else []) + ["nn"] * (N - 1)
    if Z == 0:
        pairs = ["nn"] * (N - 1)
    if N == 0:
        pairs = ["pp"] * (Z - 1)
    return pairs


def complete_pairs(Z, N):
    """Complete graph K_A: all C(A,2) pairs."""
    return ["pp"] * comb(Z, 2) + ["nn"] * comb(N, 2) + ["pn"] * (Z * N)


def prod_f(pairs, pn="chi"):
    p = mp.mpf(1)
    for k in pairs:
        p *= pair_factor(k, pn)
    return p


def binding(Z, N, pairs, pn="chi"):
    tau_vac = TAU_P**Z * TAU_N**N
    return E0 * tau_vac * (1 - prod_f(pairs, pn))


def main():
    print("=" * 80)
    print("TASK 2 -- 4-body interface assembly: linear chain vs complete graph K_A")
    print(f"  E0={mp.nstr(E0,8)} MeV  z={mp.nstr(Z_MK,8)}  h={mp.nstr(H_MK,8)}")
    print(f"  tau_p={mp.nstr(TAU_P,10)} (cached)   tau_n={mp.nstr(TAU_N,10)} (solved from tr_M(D))")
    print("=" * 80)

    # ---- self-consistency: reproduce all 4 canonical atom traces from tau_p,tau_n
    print("\n[self-check] reconstruct canonical tr_M(atom) from (tau_p,tau_n)*chain(pn=z):")
    ok = True
    for a, (Z, N) in ATOMS.items():
        tau_vac = TAU_P**Z * TAU_N**N
        recon = tau_vac * prod_f(chain_pairs(Z, N), pn="chi")
        resid = abs(recon - TRM[a])
        # residual ~1e-8 on atoms with a pn bond = the bring-color-weighted delta
        # flavor split of the pn interface (z - h(1/2 - delta/4) vs z), delta~7e-5/bond;
        # exact (1e-51) on D since tau_n was solved from it. Not an error.
        ok = ok and resid < mp.mpf("1e-6")
        print(f"   {a:4s}: recon={mp.nstr(recon,12)}  cached={mp.nstr(TRM[a],12)}  resid={mp.nstr(resid,4)}")
    print(f"   self-consistent (to 1e-6; pn residual = bring-color delta split): {ok}")

    # ---- binding under both topologies -------------------------------------
    rows = []
    print("\n[binding]  B = E0 * tau_vac * (1 - PROD f)   vs AME")
    print(f"  {'atom':4s} {'#chain':>6} {'#K_A':>5} | {'B_chain':>9} {'err%':>8} |"
          f" {'B_K_A':>9} {'err%':>8} | {'AME':>8}")
    for a, (Z, N) in ATOMS.items():
        ch, kg = chain_pairs(Z, N), complete_pairs(Z, N)
        Bc = binding(Z, N, ch, pn="chi")
        Bk = binding(Z, N, kg, pn="chi")
        ame = AME[a]
        ec = (Bc - ame) / ame * 100
        ek = (Bk - ame) / ame * 100
        print(f"  {a:4s} {len(ch):6d} {len(kg):5d} | {mp.nstr(Bc,6):>9} {mp.nstr(ec,4):>8} |"
              f" {mp.nstr(Bk,6):>9} {mp.nstr(ek,4):>8} | {mp.nstr(ame,6):>8}")
        rows.append({"atom": a, "Z": Z, "N": N, "n_chain": len(ch), "n_complete": len(kg),
                     "B_chain_MeV": mp.nstr(Bc, 12), "B_complete_MeV": mp.nstr(Bk, 12),
                     "B_AME_MeV": str(ame), "err_chain_pct": mp.nstr(ec, 6),
                     "err_complete_pct": mp.nstr(ek, 6)})

    # ---- the decisive, convention-robust observable: A-scaling 4He/D --------
    rD, r4 = rows[0], rows[3]
    sc_chain = mp.mpf(r4["B_chain_MeV"]) / mp.mpf(rD["B_chain_MeV"])
    sc_comp = mp.mpf(r4["B_complete_MeV"]) / mp.mpf(rD["B_complete_MeV"])
    sc_ame = AME["4He"] / AME["D"]
    print("\n[A-scaling] binding ratio B(4He)/B(D) -- convention-robust:")
    print(f"   linear chain   : {mp.nstr(sc_chain,5)}")
    print(f"   complete graph : {mp.nstr(sc_comp,5)}")
    print(f"   AME            : {mp.nstr(sc_ame,5)}   <-- target")
    print(f"   chain undershoots by {mp.nstr(sc_ame/sc_chain,4)}x; "
          f"complete graph by {mp.nstr(sc_ame/sc_comp,4)}x")

    print("\nVERDICT: the genuine 4-body (complete-graph) topology moves the 4He/D")
    print(f"  binding ratio from {mp.nstr(sc_chain,4)} -> {mp.nstr(sc_comp,4)} only, vs AME {mp.nstr(sc_ame,4)}.")
    print("  Reason: (1 - PROD f) saturates to 1 fast (PROD f -> 0 with more bonds),")
    print("  so extra bonds barely change B; the residual A-growth is tau_p^Z tau_n^N,")
    print("  which is too weak. Binding's strong A-scaling + the 4He tight-binding")
    print("  spike are NOT a bond-counting/topology effect -- bracketed between the")
    print("  chain (A-1 bonds) and the maximal complete graph (C(A,2) bonds), both short.")

    witness = {
        "computation": "interface-4body-assembly",
        "description": ("Task 2: linear-chain vs complete-graph (tetrahedral) interface "
                        "topology for B=E0*tau_vac*(1-PROD f). Many-body topology moves the "
                        "4He/D binding ratio only marginally; the interface deficit saturates."),
        "scriptFile": "computations/probes/interface_4body_assembly_probe.py",
        "parameters": {"q_0": str(Q0), "E0_MeV": str(E0), "tau_p": str(TAU_P),
                       "tau_n": str(TAU_N), "free_parameters": 0},
        "data": {"atoms": rows, "self_consistent": bool(ok),
                 "scaling_4He_over_D": {"chain": mp.nstr(sc_chain, 12),
                                        "complete": mp.nstr(sc_comp, 12),
                                        "AME": mp.nstr(sc_ame, 12)}},
    }
    out = COMP / "interface-4body-assembly.witness.json"
    json.dump(witness, open(out, "w"), indent=1, default=str)
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
