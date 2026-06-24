#!/usr/bin/env python3
"""Chirality-weighted joint-trace 3-body cluster — the one untested sign lever.

We proved (Lean productModel_3body_nonpos) that any saturating PRODUCT trace —
signed closed-form OR |chi| combiner — gives a non-positive (destructive) 3-body
cluster, and that no pairwise interface factor can enhance (markovParam_le_half).
The one remaining sign-flip candidate is a NON-product combiner: weight each
partition by the chirality sign sgn(w_0^{S_{lambda'}}) (the Delta_lambda sign,
= (-1)^{n(lambda)}), which is mixed-sign and breaks the product structure, so the
obstruction does not apply to it.

This probe computes the connected 3-body cluster c3 = joint - pair_sum =
E0(g_a + g_b - g_0 - g_ab) for THREE combiners over the H_9 joint trace
(per-partition chi via the Rust kernel), zero fit:
  abs    : g(S) = sum_lambda y_lambda |chi_lambda|        (production baseline; c3<0)
  signed : g(S) = sum_lambda y_lambda  chi_lambda          (factorises; proved c3<0)
  chiral : g(S) = sum_lambda y_lambda sgn(w0^{S_l'}) chi_l (the untested lever)

If the chiral c3 > 0 (attractive) and ~ +1.5 MeV (empirical b3), the chirality
involution is the missing ingredient. If still <0, that route is closed too.
"""
import math
import sys
from pathlib import Path

import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
for d in ("", "hecke", "habiro", "substrate"):
    p = str(COMP / d) if d else str(COMP)
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
AME = {"T": mp.mpf("8.481798"), "3He": mp.mpf("7.718043")}
_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}


def conjugate(lam):
    lam = [p for p in lam if p > 0]
    if not lam:
        return []
    m = lam[0]
    return [sum(1 for p in lam if p >= i) for i in range(1, m + 1)]


def sgn_w0_conj(lam):
    """sgn(w_0^{S_{lambda'}}) = prod_j (-1)^{C(lambda'_j, 2)} = (-1)^{n(lambda)}."""
    return math.prod((-1) ** (p * (p - 1) // 2) for p in conjugate(lam))


def perblock(word, mode):
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    tot = mp.mpf(0)
    for s, chi in cp:
        key = tuple(s)
        if key not in _Y9:
            continue
        c = mp.mpf(repr(chi))
        if mode == "abs":
            w = abs(c)
        elif mode == "signed":
            w = c
        elif mode == "chiral":
            w = sgn_w0_conj(list(key)) * c
        tot += _Y9[key] * w
    return tot


def word_with(full, free, iface_gens):
    keep = set(iface_gens)
    return [x for x in full if x[2] % 3 != 2 or x[2] in keep]


def main():
    print(f"E_0 = {float(E0):.4f} MeV   q0 = {float(q0):.6f}")
    print("connected 3-body cluster c3 = joint - pair_sum, three combiners:\n")
    import json
    rows = []
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        free = [x for x in full if x[2] % 3 != 2]
        gens = sorted({x[2] for x in full if x[2] % 3 == 2})
        a, b = gens[0], gens[1]
        print(f"--- {name}  (b3_empirical = +{float(AME[name]-3*mp.mpf('2.224566')):.3f} MeV) ---")
        atom = {"atom": name}
        for mode in ("abs", "signed", "chiral"):
            g0 = perblock(free, mode)
            ga = perblock(word_with(full, free, [a]), mode)
            gb = perblock(word_with(full, free, [b]), mode)
            gab = perblock(word_with(full, free, [a, b]), mode)
            pair_sum = E0 * (g0 - ga) + E0 * (g0 - gb)
            joint = E0 * (g0 - gab)
            c3 = joint - pair_sum
            sign = "+" if c3 > 0 else "-"
            print(f"    {mode:7s}: c3 = {float(c3):+.4f} MeV  (sign {sign})")
            atom[mode + "_c3_MeV"] = mp.nstr(c3, 8)
        b3 = AME[name] - 3 * mp.mpf("2.224566")
        atom["b3_empirical_MeV"] = mp.nstr(b3, 8)
        rows.append(atom)
        print()

    print("VERDICT: if chiral c3 > 0 (+~1.5 MeV) the chirality involution flips the")
    print("3-body force to attractive; if still <0, that lever is closed too.")
    witness = {
        "computation": "chirality-weighted-3body-cluster",
        "description": ("Connected 3-body cluster c3=joint-pair_sum for abs/signed/chiral "
                        "combiners over the H_9 joint trace (Rust kernel, 0 fit). Tests whether "
                        "the chirality sign sgn(w0^{S_l'}) flips c3 to attractive."),
        "scriptFile": "computations/probes/chirality_weighted_3body_cluster_probe.py",
        "parameters": {"q_0": str(Q0), "E0_MeV": str(E0), "free_parameters": 0},
        "data": {"rows": rows},
    }
    out = COMP / "chirality-weighted-3body-cluster.witness.json"
    with open(out, "w") as f:
        json.dump(witness, f, indent=1, default=str)
    print(f"witness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
