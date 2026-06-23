#!/usr/bin/env python3
"""Binding question -- candidate #1: additive / log linked-cluster interface form.

The 4-body assembly probe showed the canonical MULTIPLICATIVE deficit
    B = E0 * tau_vac * (1 - PROD_i f_i)
under-scales: the deficit (1 - PROD f) saturates to 1, so B(4He)/B(D) ~ 2.7-2.9
vs AME 12.72.  This probe tests whether an ADDITIVE / linked-cluster interface
term -- where the per-bond contributions SUM (so they grow ~ #bonds ~ A) rather
than multiply (and saturate) -- tracks binding's A-scaling.

The linked-cluster idea: log[tau_M(atom)/tau_M(vac)] = SUM_i log f_i, so the
"binding strength" carried additively per bond is the SUM of -log f_i (each
f_i < 1, so -log f_i > 0).  We scan:

  forms (all with the SAME single scale E0 = m_e/(q0(q0-1)), no per-form knob):
    M  : multiplicative deficit   B = E0 * tau_vac * (1 - PROD f)      [baseline]
    LV : log * tau_vac            B = E0 * tau_vac * SUM(-log f)       [linked-cluster x vac]
    L  : pure additive log        B = E0 * SUM(-log f)                 [pure linked-cluster]
    DV : (1-f) * tau_vac          B = E0 * tau_vac * SUM(1 - f)        [additive deficit x vac]
  x topologies:
    chain     : A-1 bonds (canonical)
    complete  : C(A,2) bonds (genuine many-body)

Decisive observable: the convention-robust A-scaling B(4He)/B(D) = 12.72, plus
the full per-atom error vs AME.  Parameter-free: tau_p, tau_n, E0, the per-bond
factors are all canonical/derived; nothing is tuned to AME.
"""
import json
import sys
from math import comb, log
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
TAU_P = mp.mpf("1.22036288908669305595736107223")
TRM_D = mp.mpf("0.7280918153466761555460727563")
TAU_N = TRM_D / (TAU_P * Z_MK)  # solved from canonical deuteron trace

AME = {"D": mp.mpf("2.224566"), "T": mp.mpf("8.481798"),
       "3He": mp.mpf("7.718043"), "4He": mp.mpf("28.295673")}
ATOMS = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def pair_factor(kind):
    return {"pp": Z_MK, "nn": Z_MK - H_MK, "pn": Z_MK}[kind]  # pn->z (chi_lambda)


def chain_pairs(Z, N):
    return ["pp"] * (Z - 1) + (["pn"] if Z and N else []) + ["nn"] * (N - 1)


def complete_pairs(Z, N):
    return ["pp"] * comb(Z, 2) + ["nn"] * comb(N, 2) + ["pn"] * (Z * N)


def binding(form, Z, N, pairs):
    tau_vac = TAU_P**Z * TAU_N**N
    fs = [pair_factor(k) for k in pairs]
    prod_f = mp.mpf(1)
    for f in fs:
        prod_f *= f
    sum_neglog = mp.fsum(-mp.log(f) for f in fs)
    sum_def = mp.fsum(1 - f for f in fs)
    if form == "M":
        return E0 * tau_vac * (1 - prod_f)
    if form == "LV":
        return E0 * tau_vac * sum_neglog
    if form == "L":
        return E0 * sum_neglog
    if form == "DV":
        return E0 * tau_vac * sum_def
    raise ValueError(form)


FORMS = {
    "M":  "E0*tau_vac*(1-PROD f)   multiplicative deficit [baseline]",
    "LV": "E0*tau_vac*SUM(-log f)  linked-cluster x vac",
    "L":  "E0*SUM(-log f)          pure additive log",
    "DV": "E0*tau_vac*SUM(1-f)     additive deficit x vac",
}


def main():
    print("=" * 84)
    print("BINDING form scan -- additive/log linked-cluster vs multiplicative deficit")
    print(f"  E0={mp.nstr(E0,8)}  tau_p={mp.nstr(TAU_P,8)}  tau_n={mp.nstr(TAU_N,8)}  (0 tuned params)")
    print("=" * 84)
    results = {}
    sc_ame = AME["4He"] / AME["D"]
    best = None
    for topo, pairs_fn in [("chain", chain_pairs), ("complete", complete_pairs)]:
        for form in FORMS:
            errs = {}
            B = {}
            for a, (Z, N) in ATOMS.items():
                b = binding(form, Z, N, pairs_fn(Z, N))
                B[a] = b
                errs[a] = (b - AME[a]) / AME[a] * 100
            scaling = B["4He"] / B["D"]
            rms = mp.sqrt(mp.fsum((errs[a] / 100) ** 2 for a in ATOMS) / 4) * 100
            key = f"{form}/{topo}"
            results[key] = {"B": {a: mp.nstr(B[a], 8) for a in ATOMS},
                            "err_pct": {a: mp.nstr(errs[a], 5) for a in ATOMS},
                            "scaling_4He_D": mp.nstr(scaling, 6),
                            "rms_err_pct": mp.nstr(rms, 5)}
            tag = ""
            if best is None or abs(scaling - sc_ame) < abs(best[1] - sc_ame):
                best = (key, scaling)
            print(f"\n[{key:14s}] {FORMS[form]}")
            print("   " + "  ".join(f"{a}:{mp.nstr(B[a],5)}({mp.nstr(errs[a],3)}%)" for a in ATOMS))
            print(f"   B(4He)/B(D) = {mp.nstr(scaling,5)}   (AME {mp.nstr(sc_ame,5)})   "
                  f"RMS|err| = {mp.nstr(rms,4)}%")

    print("\n" + "=" * 84)
    print(f"AME A-scaling target B(4He)/B(D) = {mp.nstr(sc_ame,5)}")
    print(f"closest scaling: {best[0]} -> {mp.nstr(best[1],5)} "
          f"(still {mp.nstr(sc_ame/best[1],4)}x off)" if best[1] < sc_ame
          else f"closest: {best[0]} -> {mp.nstr(best[1],5)}")
    print("\nReading: the additive/log forms (LV, L) grow ~ #bonds, so they out-scale")
    print("the multiplicative deficit (M) -- but with chi_lambda pn=z the per-atom")
    print("errors stay large. The linked-cluster form is the right DIRECTION for the")
    print("A-scaling; closing it needs the per-bond -log f weights to carry the")
    print("saturation curve (B/A ~ const), i.e. an A-dependent E0 or a bond weight")
    print("beyond the bare Markov factor. Not a parameter-free closure as-is.")

    witness = {
        "computation": "binding-additive-linked-cluster-scan",
        "description": ("Binding candidate #1: scan additive/log linked-cluster interface "
                        "forms vs the multiplicative deficit, x chain/complete topology, vs AME. "
                        "Tests whether SUM-over-bonds (grows ~A) beats PROD-over-bonds (saturates)."),
        "scriptFile": "computations/probes/binding_additive_linked_cluster_probe.py",
        "parameters": {"q_0": str(Q0), "E0_MeV": str(E0), "tau_p": str(TAU_P),
                       "tau_n": str(TAU_N), "free_parameters": 0},
        "data": {"forms": FORMS, "results": results,
                 "ame_scaling_4He_D": mp.nstr(sc_ame, 8),
                 "closest_form": best[0]},
    }
    out = COMP / "binding-additive-linked-cluster-scan.witness.json"
    with open(out, "w") as f:
        json.dump(witness, f, indent=1, default=str)
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
