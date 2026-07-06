#!/usr/bin/env python3
"""Consistency bridge: the missing pairwise binding deficit vs the q-Reeb phase.

Synthesises two committed, parameter-free computes:
  * pairwise_magnitude_gap_probe.py  -> per-isotope pairwise deficit D
    (D = 3*B2 - B_pair^model, the leading-trace shortfall; uniform per bond);
  * binding_reeb_phase_decomposition.py -> Sigma|Dtheta|, the q-Reeb ROTATION-phase
    magnitude (arccos channel, |r_lambda|<=1) that the scalar |chi| trace CANCELS.

Finding (N=2, T + 3He): the deficit and the q-Reeb phase are BOTH uniform across
isotopes AND co-vary at a near-constant ratio

    D / Sigma|Dtheta| ~ 0.206 MeV/rad   (5.4% spread, T vs 3He).

Interpretation (revises the initial guess): the missing cooperative enhancement is
NOT the growth/I_nu channel -- that channel collapses free->atom and is already
the LEADING binding captured by the |chi| combiner. It is the ROTATION/J_nu PHASE
channel, invisible to |chi| (|e^{i theta}| = 1 regardless of theta), i.e. exactly
the q-Reeb |Dtheta_lambda| object of sibling #2612.

Caveats (honest, scope-(a)): N=2 isotopes is too thin for a law; 0.206 MeV/rad is
not (yet) a canonical scale (= E0*0.0493 = E0/20.3); D inherits the 3*B2 yardstick
caveat. This is a CONSISTENCY relation + a falsifiable target, not a derivation.

Falsification: if the relation holds, 4He (Sigma|Dtheta| = 17.2334 rad) should show
a leading-trace deficit ~= 0.206 * 17.2334 ~= 3.56 MeV. That is the next test.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations"))
import _path_bridge  # noqa: E402,F401 — adds qou-substrate (witness_base) to the path

# Provenance: both values are outputs of the two committed probes above (0 fit).
ROWS = {
    "T":   {"deficit_MeV": 1.6524, "sum_abs_dtheta_rad": 8.2233, "n_bonds": 2},
    "3He": {"deficit_MeV": 1.8017, "sum_abs_dtheta_rad": 8.4937, "n_bonds": 2},
}
SUM_DTHETA_4HE = 17.2334  # from binding_reeb_phase_decomposition.py (falsification target)
E0_MEV = 4.1860


def main():
    ratios = []
    print("atom   D(MeV)   Sig|dth|(rad)   D/Sig|dth|(MeV/rad)")
    out_rows = []
    for atom, v in ROWS.items():
        r = v["deficit_MeV"] / v["sum_abs_dtheta_rad"]
        ratios.append(r)
        print(f"{atom:5s}  {v['deficit_MeV']:7.4f}   {v['sum_abs_dtheta_rad']:8.4f}      {r:8.4f}")
        out_rows.append({**v, "atom": atom, "ratio_MeV_per_rad": round(r, 6)})
    mean = sum(ratios) / len(ratios)
    spread = abs(ratios[0] - ratios[1]) / mean * 100
    pred_4he = mean * SUM_DTHETA_4HE
    print(f"\nmean ratio = {mean:.4f} MeV/rad   spread = {spread:.1f}%   (= E0*{mean/E0_MEV:.4f})")
    print(f"channel: ROTATION/J_nu phase (|chi| cancels it) -- the #2612 |Dtheta_lambda| object")
    print(f"FALSIFICATION: predicted 4He leading-trace deficit ~ {pred_4he:.3f} MeV")

    witness = {
        "computation": "reeb-phase-deficit-consistency",
        "description": (
            "Consistency bridge (0 fit): the uniform A=3 pairwise binding deficit D "
            "co-varies with the q-Reeb rotation-phase magnitude Sigma|Dtheta| at "
            "~0.206 MeV/rad (5.4% spread, T+3He), identifying the missing cooperative "
            "enhancement as the rotation/J_nu PHASE channel cancelled by the scalar |chi| "
            "trace (= #2612's |Dtheta_lambda|), NOT the growth/I_nu channel. N=2; "
            "scope-(a) consistency relation + falsifiable 4He target ~3.56 MeV, not a law."),
        "scriptFile": "computations/probes/reeb_phase_deficit_consistency_probe.py",
        "sources": [
            "computations/pairwise-magnitude-gap-decomposition.witness.json",
            "computations/binding-reeb-phase-decomposition.witness.json",
        ],
        "inputs": {"E0_MeV": E0_MEV, "fit_params": 0},
        "data": {
            "rows": out_rows,
            "mean_ratio_MeV_per_rad": round(mean, 6),
            "ratio_spread_pct": round(spread, 4),
            "ratio_as_fraction_of_E0": round(mean / E0_MEV, 6),
            "falsification_4He_deficit_MeV": round(pred_4he, 4),
            "sum_abs_dtheta_4He_rad": SUM_DTHETA_4HE,
        },
    }
    from witness_base import WitnessBuilder
    out = WitnessBuilder.wrap_legacy(
        "reeb-phase-deficit-consistency", witness, script_path=__file__,
        engine="mpmath", output_dir=str(REPO / "computations")).save()
    print(f"\nwrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
