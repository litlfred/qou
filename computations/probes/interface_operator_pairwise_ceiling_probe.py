#!/usr/bin/env python3
"""Interface-operator PAIRWISE-ASSEMBLY ceiling — the assembly-side mirror of
the term-side ℓ¹ ceiling.

Context
-------
Two ℓ¹-ceiling prunes (`delta_lambda_l1_ceiling_sign_prune`,
`binding_qgaussian_ell1_ceiling_measurement`) bounded the *single Σ_λ term*
of the binding closure: neither a sign re-derivation nor the q-Gaussian
magnitude closes the deficit, so a separate **interface / many-body operator**
(PROBE 2) must supply the rest. The 4-body assembly audit
(`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`)
found the *multiplicative* deficit form `1−∏f` structurally incapable of the
A-scaling — chain gives B(⁴He)/B(D) = 2.70, the complete-graph (tetrahedron)
2.89, both far below AME's 12.72.

But the multiplicative form is only ONE pairwise-assembly model. This probe
measures the **ceiling over the whole pairwise class** — both assembly forms
{multiplicative `1−∏f`, additive linked-cluster `Σ(−log f)`} × both bond
graphs {linear chain (A−1 bonds), complete graph (C(A,2) bonds)} — using the
**categorically-forced, zero-fit** per-bond factors

    p-p → z,   n-n → z − h,   p-n → z − h·(½ − δ/4),

with z = 1/(√q+1/√q), h = q−1/q, δ = flavor_split_leading(q) (the PROVEN
leading split, de-wired 2026-06-29). No free parameter: all binding A-scaling
is read as the scale-free ratio B(X)/B(D), so the per-atom scale E₀·τ_vac
cancels.

The measurement (this script)
-----------------------------
For each pairwise model, compute the binding A-scaling ratio R_model(X) =
proxy(X)/proxy(D) and compare to the AME ratio R_AME(X) = B_AME(X)/B_AME(D).
Report per isotope the **pairwise ceiling** = max over the four models of
R_model, and the **super-pairwise enhancement** = R_AME / ceiling — the factor
of genuinely ≥3-body cooperative structure that NO 2-body bond assembly
(either form, either topology) can supply.

This is a measurement, not a closure: nothing is fitted (anti-flip-flop). It
quantifies precisely how much of the ⁴He binding is the α-particle
shell-closure / supermultiplet spike — the cooperative term the interface
operator must carry beyond pairwise bonds — and is the assembly-side analogue
of the term-side ℓ¹ ceiling.

Producer for: computations/probes/interface-operator-pairwise-ceiling.witness.json
"""
from __future__ import annotations

# Path bridge (probes/ subdirectory → flat compute namespace).
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401,E402
del _sys, _Path, _bridge

import sys
from itertools import combinations
from pathlib import Path

from mpmath import mp, mpf, log  # noqa: E402

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))

from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

set_compute_dps()

M_E_MEV = 0.51099895069  # CODATA 2022 CAL-1

# name : (B_AME MeV, Z, N)   — AME2020 total nuclear binding (matches the prune)
ISOTOPES = {
    "D":   (AME_B_DEUTERON_MEV_VALIDATION, 1, 1),
    "T":   (AME_B_TRITIUM_MEV_VALIDATION, 1, 2),
    "3He": (AME_B_HE3_MEV_VALIDATION, 2, 1),
    "4He": (AME_B_HE4_MEV_VALIDATION, 2, 2),
    "6Li": (31.994564, 3, 3),  # A-scaling trend check (chain n=3A consistent)
}


def _bond_factor(a, b, z, h, fpn):
    """Categorical per-bond factor for a nucleon pair (a,b) ∈ {p,n}²."""
    if a == "p" and b == "p":
        return z
    if a == "n" and b == "n":
        return z - h
    return fpn  # p-n (either order)


def _chain_bonds(Z, N):
    order = ["p"] * Z + ["n"] * N
    return [(order[i], order[i + 1]) for i in range(len(order) - 1)]


def _complete_bonds(Z, N):
    order = ["p"] * Z + ["n"] * N
    return list(combinations(order, 2))


def _proxy(bonds, form, z, h, fpn):
    """Unnormalized binding proxy for a bond list under an assembly form."""
    prod = mpf(1)
    logsum = mpf(0)
    for a, b in bonds:
        f = _bond_factor(a, b, z, h, fpn)
        prod *= f
        logsum += -log(f)
    if form == "multiplicative":
        return 1 - prod          # B ∝ E₀·τ_vac·(1 − ∏ f)
    return logsum                # additive linked-cluster: B ∝ Σ (−log f)


MODELS = [
    ("mult_chain", "multiplicative", _chain_bonds),
    ("mult_complete", "multiplicative", _complete_bonds),
    ("add_chain", "additive", _chain_bonds),
    ("add_complete", "additive", _complete_bonds),
]


def measure(q):
    z = markov_z(q)
    h = hecke_h(q)
    fpn = z - h * (mpf(1) / 2 - flavor_split_leading(q) / 4)

    proxies = {}  # model -> {iso -> proxy}
    for mname, form, graph in MODELS:
        proxies[mname] = {
            iso: _proxy(graph(Z, N), form, z, h, fpn)
            for iso, (_, Z, N) in ISOTOPES.items()
        }

    rows = []
    bD = ISOTOPES["D"][0]
    for iso, (B, Z, N) in ISOTOPES.items():
        r_ame = mpf(B) / mpf(bD)
        model_ratios = {m: proxies[m][iso] / proxies[m]["D"] for m, _, _ in MODELS}
        ceiling = max(model_ratios.values())
        best_model = max(model_ratios, key=lambda m: model_ratios[m])
        rows.append({
            "atom": iso, "Z": Z, "N": N, "A": Z + N, "B_AME_MeV": B,
            "ame_ratio_over_D": str(r_ame),
            "pairwise_ratios_over_D": {m: str(v) for m, v in model_ratios.items()},
            "pairwise_ceiling_over_D": str(ceiling),
            "ceiling_model": best_model,
            "super_pairwise_enhancement": str(r_ame / ceiling),
        })
    return {"q0": str(q), "z": str(z), "h": str(h), "f_pn": str(fpn), "rows": rows}


def main() -> int:
    q = Q_MP
    res = measure(q)
    print("Interface-operator PAIRWISE-ASSEMBLY ceiling")
    print("=" * 72)
    print(f"  q0={mp.nstr(q,9)}  z={mp.nstr(mpf(res['z']),6)}  "
          f"h={mp.nstr(mpf(res['h']),6)}  f_pn={mp.nstr(mpf(res['f_pn']),6)}")
    print(f"\n  {'iso':>4}{'A':>3}{'B_AME':>9}{'R_AME':>8}{'mC':>7}{'mK':>7}"
          f"{'aC':>7}{'aK':>7}{'ceil':>7}{'super×':>8}")
    for d in res["rows"]:
        pr = d["pairwise_ratios_over_D"]
        print(f"  {d['atom']:>4}{d['A']:>3}{d['B_AME_MeV']:>9.3f}"
              f"{float(d['ame_ratio_over_D']):>8.2f}"
              f"{float(pr['mult_chain']):>7.2f}{float(pr['mult_complete']):>7.2f}"
              f"{float(pr['add_chain']):>7.2f}{float(pr['add_complete']):>7.2f}"
              f"{float(d['pairwise_ceiling_over_D']):>7.2f}"
              f"{float(d['super_pairwise_enhancement']):>8.2f}")
    print("\n  cols: mC=mult-chain mK=mult-complete aC=add-chain aK=add-complete")
    print("        ceil=max pairwise ratio  super×=R_AME/ceil (≥3-body factor)")

    he4 = next(r for r in res["rows"] if r["atom"] == "4He")
    super_he4 = float(he4["super_pairwise_enhancement"])
    print(f"\n  ⁴He super-pairwise enhancement: {super_he4:.2f}×  "
          f"(best pairwise = {he4['ceiling_model']})")
    print("  VERDICT: no 2-body bond assembly (mult/add × chain/complete) with")
    print("  categorical zero-fit factors reproduces the ⁴He/D binding ratio —")
    print(f"  a genuine {super_he4:.1f}× ≥3-body cooperative term (α-shell closure)")
    print("  is required. The interface operator must be super-pairwise, not a")
    print("  pairwise bond sum. Assembly-side mirror of the term-side ℓ¹ ceiling.")

    w = WitnessBuilder("interface-operator-pairwise-ceiling", engine="mpmath")
    w.set_description(
        "Interface-operator pairwise-assembly ceiling: the binding A-scaling "
        "ratio B(X)/B(D) reachable by ANY 2-body bond assembly — {multiplicative "
        "1−∏f, additive Σ(−log f)} × {chain, complete graph} — using the "
        "categorically-forced zero-fit per-bond factors (p-p→z, n-n→z−h, p-n→"
        "z−h(½−δ/4), δ=flavor_split_leading). Scale-free (E₀ cancels in the "
        "ratio). Measures the super-pairwise enhancement R_AME/ceiling per "
        "isotope — the ≥3-body cooperative factor (⁴He α-shell closure) that no "
        "pairwise bond model supplies. Assembly-side mirror of the term-side ℓ¹ "
        "ceiling. Measurement, not a fit (anti-flip-flop)."
    )
    w.add_data("m_e_MeV", str(M_E_MEV))
    w.add_data("measurement", res)
    w.add_assertion(
        name="he4_requires_super_pairwise_enhancement",
        computed=1 if super_he4 > 1.5 else 0,
        expected=1,
        source="⁴He's AME binding ratio exceeds the best pairwise-assembly "
               "ceiling by >1.5× — a genuine ≥3-body cooperative term is needed",
    )
    w.save()
    print("\n  Witness: interface-operator-pairwise-ceiling.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
