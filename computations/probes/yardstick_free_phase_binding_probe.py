#!/usr/bin/env python3
"""Yardstick-free phase->binding map: does B_AME - B_joint_model track Sigma|Dtheta|?

The ⁴He falsification (#2703) showed the constant 0.206 MeV/rad pairwise-deficit
relation breaks, but with two confounds tied to the `k*B2` yardstick (doubly-magic
⁴He; pairs/bonds inflation). This probe removes the yardstick entirely: instead of
`D = k*B2 - B_pair`, use the **total binding gap**

    Gap = B_AME - B_joint^model,   B_joint^model = E0 (g_free - g_atom)  (|chi|, all bonds)

which needs no B2 reference at all, and test whether `Gap / Sigma|Dtheta|` is more or
less constant than the pairwise version across T, ³He, ⁴He (0 fit).

Honest expectation either way: the total Gap includes the genuine 3-body+ physics
(not only the cancelled phase), so it may be NOISIER than the pairwise deficit -- in
which case the cleaner (if confounded) object was the pairwise one. A flat ratio
would instead say the q-Reeb phase captures the whole gap. Report the numbers, no fit.
"""
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

ATOMS = {  # name: (Z, N, n_strands, B_AME_MeV, sum_abs_dtheta_rad)
    "T":   (1, 2, 9,  mp.mpf("8.481798"),  mp.mpf("8.2233")),
    "3He": (2, 1, 9,  mp.mpf("7.718043"),  mp.mpf("8.4937")),
    "4He": (2, 2, 12, mp.mpf("28.295674"), mp.mpf("17.2334")),
}
_YCACHE = {}


def yw(n):
    if n not in _YCACHE:
        _YCACHE[n] = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                      for k, v in y_lambda_at(n, q0).items()}
    return _YCACHE[n]


def perblock(word, n):
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(n, factors, q0f)
    Y = yw(n)
    tot = mp.mpf(0)
    for s, chi in cp:
        key = tuple(s)
        if key in Y:
            tot += Y[key] * abs(mp.mpf(repr(chi)))
    return tot


def main():
    print(f"E_0 = {float(E0):.4f} MeV   q0 = {float(q0):.6f}   (0 fit)\n")
    print("atom   B_AME    B_joint^model   Gap=B_AME-B_joint   Sig|dth|   Gap/Sig|dth|")
    rows = []
    for name, (Z, N, n, ame, dth) in ATOMS.items():
        full = atom_braid_word_3A(Z, N)
        free = [x for x in full if x[2] % 3 != 2]
        g0 = perblock(free, n)
        gfull = perblock(full, n)
        b_joint = E0 * (g0 - gfull)
        gap = ame - b_joint
        ratio = gap / dth
        print(f"{name:5s}  {float(ame):7.3f}   {float(b_joint):8.4f}      "
              f"{float(gap):8.4f}          {float(dth):7.4f}    {float(ratio):.4f}")
        rows.append({"atom": name, "B_AME_MeV": mp.nstr(ame, 8),
                     "B_joint_model_MeV": mp.nstr(b_joint, 8), "gap_MeV": mp.nstr(gap, 8),
                     "sum_abs_dtheta_rad": mp.nstr(dth, 8),
                     "ratio_MeV_per_rad": mp.nstr(ratio, 8)})

    ratios = [mp.mpf(r["ratio_MeV_per_rad"]) for r in rows]
    mean = mp.fsum(ratios) / len(ratios)
    spread = (max(ratios) - min(ratios)) / mean * 100
    print(f"\nyardstick-free Gap/Sig|dth|: mean {float(mean):.4f} MeV/rad, "
          f"full spread {float(spread):.1f}% (T/3He/4He)")
    print("compare: pairwise k*B2 version was 5.4% across T/3He but +69% at 4He (#2703).")
    verdict = ("FLAT (<15%) -- phase captures the whole gap" if spread < 15 else
               "MODERATE (15-40%)" if spread < 40 else
               "NOISY (>40%) -- total gap mixes in 3-body; pairwise object was cleaner")
    print(f"VERDICT: yardstick-free ratio is {verdict}")

    import json
    witness = {
        "computation": "yardstick-free-phase-binding",
        "description": (
            "Yardstick-free phase->binding test (0 fit): Gap=B_AME-B_joint^model (|chi| "
            "joint trace, no k*B2 reference) vs q-Reeb Sigma|Dtheta| across T/3He/4He. "
            "Tests whether removing the k*B2 yardstick (the #2703 confound) yields a flatter "
            "phase->binding ratio, or whether the total gap is noisier (mixes in 3-body)."),
        "scriptFile": "computations/probes/yardstick_free_phase_binding_probe.py",
        "inputs": {"E0_MeV": mp.nstr(E0, 10), "q0": mp.nstr(q0, 12), "fit_params": 0},
        "data": {"rows": rows, "mean_ratio_MeV_per_rad": mp.nstr(mean, 8),
                 "full_spread_pct": mp.nstr(spread, 6), "verdict": verdict},
    }
    from witness_base import WitnessBuilder
    out = WitnessBuilder.wrap_legacy(
        "yardstick-free-phase-binding", witness, script_path=__file__,
        engine="mpmath", output_dir=str(REPO / "computations")).save()
    print(f"\nwrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
