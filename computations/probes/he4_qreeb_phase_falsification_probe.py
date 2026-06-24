#!/usr/bin/env python3
"""4He falsification of the q-Reeb-phase / pairwise-deficit relation (H_12, 0 fit).

PR #2681 found, for the two A=3 mirror nuclei (T, 3He), that the pairwise
leading-trace binding deficit D and the q-Reeb rotation-phase magnitude Sigma|Dtheta|
co-vary at

    D / Sigma|Dtheta| ~ 0.206 MeV/rad   (5.4% spread, N=2).

The falsifiable prediction was: 4He (Sigma|Dtheta| = 17.2334 rad, from
binding_reeb_phase_decomposition.py) should show a pairwise deficit
D_4He ~= 0.206 * 17.2334 ~= 3.56 MeV.

This probe computes D_4He with the SAME machinery as the A=3 probe, now on the
canonical 4He braid `atom_braid_word_3A(2,2)` (47 crossings on H_12, 3 adjacent
interfaces at gens 2/5/8), |chi| combiner over the H_12 joint trace (Rust kernel):

    B_pair^model = sum over the 3 adjacent bonds of  E0 (g0 - g_bond)
    pair_target  = n_pairs * B2 = C(4,2) * B2 = 6 * B2   (tetrahedron, same yardstick)
    D_4He        = pair_target - B_pair^model

CAVEATS (carried from #2681 + new): (i) the n_pairs*B2 yardstick is a modeling
reference, NOT derived; (ii) 4He is DOUBLY MAGIC / anomalously bound (B_AME=28.3 MeV
>> 6*B2=13.35), so the pairwise yardstick is on its weakest footing here -- a near-
miss neither confirms nor a large miss cleanly refutes the q-Reeb identification, it
also tests the yardstick. Report tiered, no fit.
"""
import math
import sys
from pathlib import Path

import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
for d in ("", "hecke", "habiro", "substrate"):
    p = str(REPO / "computations" / d) if d else str(REPO / "computations")
    if p not in sys.path:
        sys.path.insert(0, p)
import _path_bridge  # noqa: E402,F401
import pyhecke_native  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

q0 = mp.mpf(str(Q0)); q0f = float(Q0)
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
B2 = mp.mpf("2.224566")
AME_4HE = mp.mpf("28.295674")
SUM_DTHETA_4HE = mp.mpf("17.2334")   # from binding_reeb_phase_decomposition.py
RATIO_A3 = mp.mpf("0.2065")          # MeV/rad, from PR #2681 (T+3He mean)
_Y12 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
        for k, v in y_lambda_at(12, q0).items()}


def perblock12(word, mode="abs"):
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(12, factors, q0f)
    tot = mp.mpf(0)
    for s, chi in cp:
        key = tuple(s)
        if key not in _Y12:
            continue
        c = mp.mpf(repr(chi))
        tot += _Y12[key] * (abs(c) if mode == "abs" else c)
    return tot


def word_with(full, iface_gens):
    keep = set(iface_gens)
    return [x for x in full if x[2] % 3 != 2 or x[2] in keep]


def main():
    print(f"E_0 = {float(E0):.4f} MeV   q0 = {float(q0):.6f}   B2 = {float(B2):.4f}   (0 fit)\n")
    full = atom_braid_word_3A(2, 2)
    free = [x for x in full if x[2] % 3 != 2]
    gens = sorted({x[2] for x in full if x[2] % 3 == 2})
    n_pairs = math.comb(4, 2)
    pair_target = n_pairs * B2

    print(f"4He braid: {len(full)} crossings, interface gens {gens} (pp/pn/nn)")
    g0 = perblock12(free)
    per_bond = []
    for gi in gens:
        gb = perblock12(word_with(full, [gi]))
        bb = E0 * (g0 - gb)
        per_bond.append(bb)
        print(f"    bond gen {gi}: B_bond = {float(bb):+.4f} MeV")
    b_pair = mp.fsum(per_bond)
    deficit = pair_target - b_pair
    ratio = deficit / SUM_DTHETA_4HE
    pred = RATIO_A3 * SUM_DTHETA_4HE
    rel = (ratio - RATIO_A3) / RATIO_A3 * 100

    print(f"\n  B_pair (model, 3 adjacent bonds) = {float(b_pair):+.4f} MeV")
    print(f"  pair_target (= 6*B2)             = {float(pair_target):+.4f} MeV")
    print(f"  D_4He (deficit)                  = {float(deficit):+.4f} MeV")
    print(f"  Sigma|Dtheta| (4He)              = {float(SUM_DTHETA_4HE):.4f} rad")
    print(f"  ---")
    print(f"  PREDICTED D_4He (= 0.2065 * 17.2334) = {float(pred):.4f} MeV")
    print(f"  OBSERVED  D_4He                      = {float(deficit):.4f} MeV")
    print(f"  D/Sigma|Dtheta| (4He) = {float(ratio):.4f} MeV/rad   "
          f"vs A=3 mean 0.2065  ({float(rel):+.1f}%)")
    verdict = ("SURVIVES (<15%)" if abs(rel) < 15 else
               "STRAINED (15-40%)" if abs(rel) < 40 else "FALSIFIED (>40%)")
    print(f"\n  VERDICT: relation {verdict} at 4He "
          f"(remember: doubly-magic, yardstick on weakest footing)")

    import json
    witness = {
        "computation": "he4-qreeb-phase-falsification",
        "description": (
            "4He falsification of the q-Reeb-phase/pairwise-deficit relation "
            "D/Sigma|Dtheta|~0.2065 MeV/rad (PR #2681, A=3). Per-bond pairwise binding on "
            "the canonical H_12 braid atom_braid_word_3A(2,2), |chi| combiner, 0 fit; "
            "deficit vs 6*B2 yardstick compared to 0.2065*17.2334=3.56 MeV prediction. "
            "Caveat: 4He is doubly magic, yardstick weakest here."),
        "scriptFile": "computations/probes/he4_qreeb_phase_falsification_probe.py",
        "inputs": {"E0_MeV": mp.nstr(E0, 10), "q0": mp.nstr(q0, 12), "B2_MeV": mp.nstr(B2, 8),
                   "sum_abs_dtheta_4He_rad": mp.nstr(SUM_DTHETA_4HE, 8),
                   "ratio_A3_MeV_per_rad": mp.nstr(RATIO_A3, 6), "fit_params": 0},
        "data": {
            "per_bond_MeV": [mp.nstr(b, 8) for b in per_bond],
            "B_pair_model_MeV": mp.nstr(b_pair, 8),
            "pair_target_MeV": mp.nstr(pair_target, 8),
            "deficit_observed_MeV": mp.nstr(deficit, 8),
            "deficit_predicted_MeV": mp.nstr(pred, 8),
            "ratio_observed_MeV_per_rad": mp.nstr(ratio, 8),
            "ratio_rel_to_A3_pct": mp.nstr(rel, 6),
            "verdict": verdict,
        },
    }
    from witness_base import WitnessBuilder
    out = WitnessBuilder.wrap_legacy(
        "he4-qreeb-phase-falsification", witness, script_path=__file__,
        engine="mpmath", output_dir=str(REPO / "computations")).save()
    print(f"\nwrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
