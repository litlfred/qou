#!/usr/bin/env python3
"""COMPARISON ONLY (scope a): strand-end merge ceiling readings against AME2020 total binding.

Reads strand-end-merge-ceiling.witness.json (q0, t1, E0) and computations/data/ame2020.json.
Nothing here feeds any proof or producer. AME includes Coulomb and asymmetry, which none of the
strong readings model, so a strong-only reading should sit ABOVE 1 by that amount, not at 1.

Readings (none chosen by this comparison; all fixed before it, see the audit section 3):
  Ra   rule (3-inf) as PR #9659 defines it:      -ln r = -ln y(3A) + A ln t1
  Rb   inter-nucleon part only, Ra - A*Ra(1):     A ln(1+u+u^2+u^3) + ln(1-u) - ln(1-u^(3A+1))
  s    the per-nucleon part, Ra(1)
  T3   PR #9710 (colour valence), for reference:  min(C(A,2), 3*floor(A/2)) bonds * (-ln(z - h/2))
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main() -> int:
    w = json.loads((HERE / "strand-end-merge-ceiling.witness.json").read_text(), parse_float=str)
    q = mp.mpf(w["q0Value"])
    u = q ** -2
    lt = mp.mpf(w["data"]["ln_t1"])
    E0 = mp.mpf(w["parameters"]["E0_tower_MeV"])
    bv = json.loads((ROOT / "computations/probes/nucleus_bond_valence/nucleus-bond-valence.witness.json").read_text(),
                    parse_float=str)
    b_E0 = mp.mpf(bv["bond"]["b_E0_MeV"])

    def Ra(A):
        return E0 * (3 * A * mp.log(1 + u) + A * lt + mp.log(1 - u) - mp.log(1 - u ** (3 * A + 1)))

    def Rb(A):
        return E0 * (A * mp.log(1 + u + u ** 2 + u ** 3) + mp.log(1 - u) - mp.log(1 - u ** (3 * A + 1)))

    def T3(A):   # PR #9710 bound(): min(C(A,2), 3*floor(A/2)), and 1 at A = 2
        c = A * (A - 1) // 2
        return (min(c, 3 * (A // 2)) if A >= 3 else 1) * b_E0

    assert abs(Rb(16) - (Ra(16) - 16 * Ra(1))) < mp.mpf("1e-30")
    ame = json.loads((ROOT / "computations/data/ame2020.json").read_text(), parse_float=str)["entries"]
    rows = [e for e in ame if int(e["A"]) >= 2 and not e["binding_energy_per_A_estimated"]
            and e["binding_energy_per_A_keV"] not in (None, "0.0")]

    def Ba(e):
        return mp.mpf(e["binding_energy_per_A_keV"]) * int(e["A"]) / 1000

    named = {(1, 2): "2H", (1, 3): "3H", (2, 3): "3He", (2, 4): "4He", (3, 6): "6Li", (6, 12): "12C",
             (8, 16): "16O", (20, 40): "40Ca", (26, 56): "56Fe", (50, 120): "120Sn", (82, 208): "208Pb"}
    light = []
    for e in rows:
        k = (int(e["Z"]), int(e["A"]))
        if k in named:
            A = k[1]
            light.append({"nuclide": named[k], "A": A, "B_AME_MeV": mp.nstr(Ba(e), 9),
                          "Ra_MeV": mp.nstr(Ra(A), 9), "Ra_ratio": mp.nstr(Ra(A) / Ba(e), 4),
                          "Rb_MeV": mp.nstr(Rb(A), 9), "Rb_ratio": mp.nstr(Rb(A) / Ba(e), 4),
                          "T3_ratio": mp.nstr(T3(A) / Ba(e), 4)})
    stats = {}
    for name, f in (("Ra", Ra), ("Rb", Rb), ("T3", T3)):
        rs = [f(int(e["A"])) / Ba(e) for e in rows if int(e["A"]) >= 16]
        m = sum(rs) / len(rs)
        sd = mp.sqrt(sum((r - m) ** 2 for r in rs) / len(rs))
        stats[name] = {"n": len(rs), "mean_ratio_A_ge_16": mp.nstr(m, 6), "sd": mp.nstr(sd, 4)}
    out = {"producer": "computations/probes/strand_end_merge_ceiling/compare_ame.py", "scope": "a",
           "comparisonOnly": True,
           "per_nucleon_bulk_MeV": {"Ra": mp.nstr(E0 * (3 * mp.log(1 + u) + lt), 12),
                                    "Rb": mp.nstr(E0 * mp.log(1 + u + u ** 2 + u ** 3), 12),
                                    "s_nucleon_self_term": mp.nstr(Ra(1), 12),
                                    "T3": mp.nstr(mp.mpf(3) / 2 * b_E0, 12)},
           "named": light, "stats": stats}
    (HERE / "strand-end-merge-ceiling-ame-comparison.witness.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
