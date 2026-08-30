#!/usr/bin/env python3
"""
Fusion-process LR support probe — does D + T -> 4He + n conserve the induced
Wedderburn support in H_15?  (bean qou-89xc, parent qou-dpy1)

The two sides of the channel live in different algebras (H_6 x H_9 initial,
H_12 x H_3 final), so their SDP active sets cannot be compared block-by-block.
Both sides DO embed in H_15 by Littlewood-Richardson induction, giving a
common frame: for each side, induce the product of its active sets

    S_side = { nu |- 15 : c^nu_{lambda,mu} > 0,
               lambda in active(side_1), mu in active(side_2) }

and compare the two subsets of the 176 partitions of 15. Everything here is
exact integer combinatorics (LR coefficients via the repo's cached
lr_coefficients tables); there is no float surface.

Reading discipline: the active sets are the duals' choice of receptive
channels at each subject's OWN level; LR induction answers only "which H_15
blocks can these channels reach", not anything about magnitudes. A support
mismatch would be a structural obstruction to any H_15-level channel model
built on these active sets; support agreement is necessary-not-sufficient.
Conclusions live in docs/audits/2026-08-29-mass-provenance-breakdown-and-
gap-map.md §4b and bean qou-89xc. No witness emitted; nothing wired.
"""
from __future__ import annotations

import ast
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "substrate"))

from lr_coefficients import get_lr_table  # noqa: E402


def active_blocks(atom):
    w = json.load(open(os.path.join(ROOT, f"nucleus-real-sdp-{atom}.witness.json")))
    d = w.get("data", w)
    s = d.get("positive_norm_subspace_solve", {})
    return [tuple(ast.literal_eval(b)) for b in s.get("active_blocks", [])]


def induced_support(acts1, acts2, n1, n2):
    """Union over active pairs of the LR support in H_{n1+n2}.

    Table format (lr_coefficients.get_lr_table): flat dict
    (lambda, mu, nu) -> c with |lambda| = n1, |mu| = n2, |nu| = n1+n2.
    """
    table = get_lr_table(n1, n2)
    a1, a2 = set(acts1), set(acts2)
    seen_pairs, out = set(), set()
    for (lam, mu, nu), c in table.items():
        if c > 0 and lam in a1 and mu in a2:
            seen_pairs.add((lam, mu))
            out.add(nu)
    missing = {(l, m) for l in a1 for m in a2} - seen_pairs
    if missing:
        raise KeyError(f"LR table ({n1},{n2}) has no entries for pairs: {sorted(missing)[:4]}")
    return out


def main() -> int:
    init_1, init_2 = active_blocks("deuteron"), active_blocks("tritium")
    fin_1, fin_2 = active_blocks("he4"), active_blocks("neutron")
    print("FUSION-PROCESS LR SUPPORT — D + T vs 4He + n, induced into H_15")
    print(f"  active sets: 2H {len(init_1)} (H_6) x 3H {len(init_2)} (H_9)  |  "
          f"4He {len(fin_1)} (H_12) x n {len(fin_2)} (H_3)")

    s_init = induced_support(init_1, init_2, 6, 9)
    s_fin = induced_support(fin_1, fin_2, 12, 3)
    inter = s_init & s_fin
    only_i = s_init - s_fin
    only_f = s_fin - s_init

    print(f"  |S_init| = {len(s_init)}   |S_fin| = {len(s_fin)}   "
          f"|S_init ∩ S_fin| = {len(inter)}   (176 partitions of 15 total)")
    print(f"  S_init \\ S_fin: {len(only_i)}   S_fin \\ S_init: {len(only_f)}")
    if only_f and len(only_f) <= 12:
        print(f"    final-only blocks: {sorted(only_f)}")
    if only_i and len(only_i) <= 12:
        print(f"    initial-only blocks: {sorted(only_i)}")

    contained = s_fin <= s_init
    print(f"\n  final support ⊆ initial support: {contained}")
    verdict = "PASS" if (s_init and s_fin and inter) else "FAIL"
    print(f"RESULT: {verdict} — supports nonempty with nonempty overlap; "
          "containment reported above (exact integer LR, no tolerance)")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
