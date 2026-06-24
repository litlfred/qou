#!/usr/bin/env python3
"""Two follow-ups to the chirality sign-carrier result, both over the H_9 joint trace.

Context. We established (this branch):
  * productModel_3body_nonpos (Lean, sorry-free): any saturating PRODUCT trace gives
    a destructive (<=0) beyond-pairwise 3-body cluster -- sign cannot be fixed by a
    convention on a product, nor by the bond topology.
  * chirality_weighted_3body_cluster_probe: the NON-product chirality combiner
    sgn(w_0^{S_l'})*chi flips the connected 3-body cluster to attractive (c3>0), but
    as a binding combiner it over-cancels (chiral total binding ~98% underbind).

This probe runs the two natural next experiments, zero fit:

(A) STRUCTURED COMBINER -- keep |chi| magnitude on the pairwise (leading) part and
    apply the chirality sign only to the 3-body correlation:
        B_struct = pair_sum^{abs} + c3^{chiral}
    i.e. the |chi| pairwise binding plus the chiral (attractive) connected 3-body
    cluster. Tests whether splitting magnitude (abs) from sign (chiral) recovers a
    sensible total binding that pure-chiral destroys.

(B) LONG-RANGE 1-3 BOND (full triangle in the JOINT-TRACE model) -- the joint trace
    of a braid with a NON-adjacent crossing does not factor over bonds, so it escapes
    productModel_3body_nonpos. We add the band generator
        b_{2,6} = s5 s4 s3 . s2 . s3^-1 s4^-1 s5^-1
    (a single long-range crossing connecting block 0's region to block 2's region) on
    top of the two adjacent interfaces s2, s5, and measure how the genuine 3-bond
    connected cluster c3 moves vs the 2-adjacent-bond value.
"""
import sys
from pathlib import Path

import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations" / "probes"))
# Reuse the validated infra from the chirality probe.
from chirality_weighted_3body_cluster_probe import (  # noqa: E402
    E0, AME, q0, atom_braid_word_3A, perblock, word_with,
)

QQI = q0 - 1 / q0  # q - q^{-1}; sigma^{-1} = (1, -QQI, g) since sigma - sigma^{-1} = q - q^{-1}


def band_2_6():
    """Long-range band generator b_{2,6} = s5 s4 s3 s2 s3^-1 s4^-1 s5^-1 as a (c,d,g) word.

    sigma_g  = (1, 0, g);  sigma_g^{-1} = (1, -(q-q^{-1}), g).  A single crossing
    between the block-0 region and the block-2 region (non-adjacent => non-product)."""
    one = mp.mpf(1)
    pos = lambda g: (one, mp.mpf(0), g)
    inv = lambda g: (one, -QQI, g)
    return [pos(5), pos(4), pos(3), pos(2), inv(3), inv(4), inv(5)]


def main():
    print(f"E_0 = {float(E0):.4f} MeV   q0 = {float(q0):.6f}   (0 tuned params)\n")
    rows = []
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        free = [x for x in full if x[2] % 3 != 2]
        gens = sorted({x[2] for x in full if x[2] % 3 == 2})
        a, b = gens[0], gens[1]
        ame = AME[name]
        print(f"=== {name}  (AME B = {float(ame):.3f} MeV) ===")

        # --- (A) structured combiner: abs pairwise + chiral 3-body correlation ---
        rec = {"atom": name}
        for mode in ("abs", "chiral"):
            g0 = perblock(free, mode)
            ga = perblock(word_with(full, free, [a]), mode)
            gb = perblock(word_with(full, free, [b]), mode)
            gab = perblock(word_with(full, free, [a, b]), mode)
            rec[mode] = dict(
                pair=E0 * (g0 - ga) + E0 * (g0 - gb),
                joint=E0 * (g0 - gab),
            )
            rec[mode]["c3"] = rec[mode]["joint"] - rec[mode]["pair"]
        b_struct = rec["abs"]["pair"] + rec["chiral"]["c3"]
        e_abs = (rec["abs"]["joint"] - ame) / ame * 100
        e_chi = (rec["chiral"]["joint"] - ame) / ame * 100
        e_str = (b_struct - ame) / ame * 100
        print("  (A) structured combiner |chi|-pairwise + chiral-3body:")
        print(f"      abs    joint      = {float(rec['abs']['joint']):+8.4f}  err {float(e_abs):+7.1f}%")
        print(f"      chiral joint      = {float(rec['chiral']['joint']):+8.4f}  err {float(e_chi):+7.1f}%")
        print(f"      pair^abs          = {float(rec['abs']['pair']):+8.4f}")
        print(f"      c3^chiral         = {float(rec['chiral']['c3']):+8.4f}")
        print(f"      B_struct          = {float(b_struct):+8.4f}  err {float(e_str):+7.1f}%   <-- (A)")

        # --- (B) long-range 1-3 bond: genuine 3-bond connected cluster ---
        lr = band_2_6()
        # 2-adjacent-bond atom (existing) and the triangle (+ long-range band):
        atom2 = word_with(full, free, [a, b])
        triangle = atom2 + lr
        print("  (B) long-range 1-3 band b_{2,6} added (non-adjacent => non-product):")
        for mode in ("abs", "chiral"):
            g0 = perblock(free, mode)
            g2 = perblock(atom2, mode)
            g3 = perblock(triangle, mode)
            j2 = E0 * (g0 - g2)
            j3 = E0 * (g0 - g3)
            d_lr = j3 - j2  # contribution of the long-range bond to the binding
            print(f"      {mode:7s}: joint(2-bond)={float(j2):+8.4f}  joint(triangle)={float(j3):+8.4f}"
                  f"  Delta_LR={float(d_lr):+7.4f}")
            rec[mode]["joint_triangle"] = j3
            rec[mode]["delta_LR"] = d_lr
        rows.append({
            "atom": name,
            "AME_MeV": mp.nstr(ame, 8),
            "abs_joint_MeV": mp.nstr(rec["abs"]["joint"], 8),
            "chiral_joint_MeV": mp.nstr(rec["chiral"]["joint"], 8),
            "pair_abs_MeV": mp.nstr(rec["abs"]["pair"], 8),
            "c3_chiral_MeV": mp.nstr(rec["chiral"]["c3"], 8),
            "B_structured_MeV": mp.nstr(b_struct, 8),
            "B_structured_err_pct": mp.nstr(e_str, 6),
            "triangle_abs_joint_MeV": mp.nstr(rec["abs"]["joint_triangle"], 8),
            "triangle_chiral_joint_MeV": mp.nstr(rec["chiral"]["joint_triangle"], 8),
            "delta_LR_abs_MeV": mp.nstr(rec["abs"]["delta_LR"], 8),
            "delta_LR_chiral_MeV": mp.nstr(rec["chiral"]["delta_LR"], 8),
        })
        print()

    import json
    witness = {
        "computation": "structured-combiner-and-triangle",
        "description": (
            "Two follow-ups over the H_9 joint trace, 0 fit. (A) structured combiner "
            "B_struct = pair_sum^abs + c3^chiral (|chi| magnitude on pairwise + chirality "
            "sign on the 3-body correlation). (B) long-range 1-3 band generator "
            "b_{2,6}=s5s4s3 s2 s3^-1 s4^-1 s5^-1 added on top of the two adjacent "
            "interfaces -- a non-adjacent (non-product) crossing that escapes "
            "productModel_3body_nonpos; reports its Delta_LR binding contribution."),
        "scriptFile": "computations/probes/structured_combiner_and_triangle_probe.py",
        "inputs": {"E0_MeV": mp.nstr(E0, 10), "q0": mp.nstr(q0, 12), "fit_params": 0},
        "data": {"rows": rows},
    }
    out = REPO / "computations" / "structured-combiner-and-triangle.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"wrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
