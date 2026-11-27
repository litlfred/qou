#!/usr/bin/env python3
"""COMPARISON (written after PREREGISTRATION.md was committed): the pre-registered bond counts of
nucleus_bond_valence_probe.py against AME2020 total binding. Comparison only: nothing here feeds
back into the choice of premise, and nothing here is fitted.

Reads the probe's witness (bond values, formulas) and computations/data/ame2020.json (parsed as
decimal strings into mpmath, never float). Experimental entries only, A >= 2.

AME binding includes Coulomb and asymmetry, which the pre-registered strong bond count does not
model; the ratio is therefore the strong count against the whole measured binding.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
from nucleus_bond_valence_probe import PREMISES, bound  # noqa: E402

mp.mp.dps = 40


def main():
    w = json.loads((HERE / "nucleus-bond-valence.witness.json").read_text())
    b = {"alpha": mp.mpf(w["bond"]["b_alpha_MeV"]), "E0": mp.mpf(w["bond"]["b_E0_MeV"])}
    ame = json.loads((ROOT / "computations/data/ame2020.json").read_text(), parse_float=str)["entries"]
    rows = [e for e in ame if int(e["A"]) >= 2 and not e["binding_energy_per_A_estimated"]
            and e["binding_energy_per_A_keV"] not in (None, "0.0")]

    def B_ame(e):
        return mp.mpf(e["binding_energy_per_A_keV"]) * int(e["A"]) / 1000

    stats = {}
    for prem in PREMISES:
        for s in ("alpha", "E0"):
            r_all = [bound(prem, int(e["A"])) * b[s] / B_ame(e) for e in rows]
            r_16 = [bound(prem, int(e["A"])) * b[s] / B_ame(e) for e in rows if int(e["A"]) >= 16]
            mean16 = mp.fsum(r_16) / len(r_16)
            sd16 = mp.sqrt(mp.fsum((x - mean16) ** 2 for x in r_16) / len(r_16))
            stats[f"{prem}/{s}"] = {"n": len(r_all), "n_A_ge_16": len(r_16),
                                    "mean_ratio_A_ge_16": mp.nstr(mean16, 6), "sd_ratio_A_ge_16": mp.nstr(sd16, 6),
                                    "min_ratio": mp.nstr(min(r_all), 6), "max_ratio": mp.nstr(max(r_all), 6)}

    named = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He"), (3, 3, "6Li"), (3, 4, "7Li"),
             (6, 6, "12C"), (8, 8, "16O"), (20, 20, "40Ca"), (26, 30, "56Fe"), (50, 70, "120Sn"),
             (82, 126, "208Pb")]
    idx = {(int(e["Z"]), int(e["N"])): e for e in rows}
    light = []
    for Z, N, name in named:
        e = idx[(Z, N)]
        A = Z + N
        Ba = B_ame(e)
        light.append({"nuclide": name, "A": A, "B_AME_MeV": mp.nstr(Ba, 9),
                      "bonds_needed_per_nucleon_alpha": mp.nstr(Ba / (A * b["alpha"]), 5),
                      "bonds_needed_per_nucleon_E0": mp.nstr(Ba / (A * b["E0"]), 5),
                      **{f"{p}_ratio_{s}": mp.nstr(bound(p, A) * b[s] / Ba, 5)
                         for p in ("chain", "T3", "V3", "V6") for s in ("alpha", "E0")}})

    print("nuclide  A   B_AME   need/nucl(a) need/nucl(E0)  chain(E0)  T3(a)  T3(E0)  V6(E0)")
    for r in light:
        print(f'{r["nuclide"]:6} {r["A"]:4} {r["B_AME_MeV"]:>10} {r["bonds_needed_per_nucleon_alpha"]:>8}'
              f' {r["bonds_needed_per_nucleon_E0"]:>8}   {r["chain_ratio_E0"]:>8} {r["T3_ratio_alpha"]:>7}'
              f' {r["T3_ratio_E0"]:>7} {r["V6_ratio_E0"]:>7}')
    print()
    for k, v in stats.items():
        print(k, v)

    out = {"producer": "computations/probes/nucleus_bond_valence/compare_ame.py",
           "comparison_only": True, "q0Anchor": "proton", "reads_AME": True,
           "preregistration": "computations/probes/nucleus_bond_valence/PREREGISTRATION.md",
           "ame_source": "computations/data/ame2020.json (experimental entries, A >= 2)",
           "named": light, "stats": stats}
    (HERE / "nucleus-bond-valence-ame-comparison.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
