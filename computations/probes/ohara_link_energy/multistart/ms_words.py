#!/usr/bin/env python3
"""Braid representatives per link class for the multi-start study, with an exact
topology check (Jones by Kauffman bracket, Alexander by Burau, lk, component
strand counts) against the class's canonical word. Pure integer / sympy; no energy.
All letters positive (braid_topology.py supports positive letters only).
"""
import sys, json
sys.path.insert(0, "..")
import braid_topology as BT

NUC9 = [0, 1] * 3 + [0, 0, 1]
D2_ALT = [0, 1, 0, 0, 1, 0]          # (s0 s1 s0)^2 = Delta^2 = (s0 s1)^3 as braids

def rot(w, k): k %= len(w); return w[k:] + w[:k]
def dconj(w): return [1 - g for g in w]          # conjugation by Delta on 3 strands
def stab_top(w): return w + [2]                  # Markov: 3 -> 4 strands, + s2
def stab_bot(w): return [g + 1 for g in w] + [0] # Markov at the bottom: shift, + s0
def rewrite(w):                                  # replace the leading Delta^2=(s0s1)^3 by (s0s1s0)^2
    assert w[:6] == [0, 1] * 3
    return D2_ALT + w[6:]

CANON = {
    "nuc9": (NUC9, 3),
    "A": (NUC9 + [1, 0], 3),                     # gluon_s1_s0 (route-1 label "B")
    "B": (NUC9 + [0, 1], 3),                     # gluon_s0_s1 (route-1 label "A")
    "G": ([0] * 7 + [1] * 4, 3),                 # nuc11_gen_grouped
    "hopf": ([0, 0], 2),
    "trefoil": ([0, 0, 0], 2),
}
REPS = {
    "nuc9": {
        "nuc9": (NUC9, 3), "nuc9_rot4": (rot(NUC9, 4), 3), "nuc9_dconj": (dconj(NUC9), 3),
        "nuc9_rewrite": (rewrite(NUC9), 3), "nuc9_stabtop": (stab_top(NUC9), 4),
        "nuc9_stabbot": (stab_bot(NUC9), 4)},
    "A": {
        "gluon_s1_s0": (NUC9 + [1, 0], 3), "gluon_s1_s1": (NUC9 + [1, 1], 3),
        "A_rot5": (rot(NUC9 + [1, 0], 5), 3), "A_dconj": (dconj(NUC9 + [1, 0]), 3),
        "A_rewrite": (rewrite(NUC9 + [1, 0]), 3), "A_stabtop": (stab_top(NUC9 + [1, 0]), 4),
        "A_stabbot": (stab_bot(NUC9 + [1, 1]), 4)},
    "B": {
        "gluon_s0_s1": (NUC9 + [0, 1], 3), "gluon_s0_s0": (NUC9 + [0, 0], 3),
        "B_rot5": (rot(NUC9 + [0, 1], 5), 3), "B_dconj": (dconj(NUC9 + [0, 0]), 3),
        "B_rewrite": (rewrite(NUC9 + [0, 1]), 3), "B_stabtop": (stab_top(NUC9 + [0, 0]), 4),
        "B_stabbot": (stab_bot(NUC9 + [0, 1]), 4)},
    "G": {
        "gen_grouped": ([0] * 7 + [1] * 4, 3), "G_rot3": (rot([0] * 7 + [1] * 4, 3), 3),
        "G_dconj": (dconj([0] * 7 + [1] * 4), 3), "G_rot9": (rot([0] * 7 + [1] * 4, 9), 3),
        "G_stabtop": (stab_top([0] * 7 + [1] * 4), 4), "G_stabbot": (stab_bot([0] * 7 + [1] * 4), 4)},
    "hopf": {"hopf_s1^2": ([0, 0], 2), "hopf_3strand": ([0, 0, 1], 3)},
    "trefoil": {"trefoil_s1^3": ([0, 0, 0], 2), "trefoil_3strand": ([0, 0, 0, 1], 3)},
}
# component knot-type Alexander polys (the certificate references), per class
COMP_ALEX = {"nuc9": ["1", "t**2 - t + 1"], "A": ["t**4 - t**3 + t**2 - t + 1", "1"],
             "B": ["t**2 - t + 1", "1"], "G": ["t**6 - t**5 + t**4 - t**3 + t**2 - t + 1", "1"],
             "hopf": ["1", "1"], "trefoil": ["t**2 - t + 1"]}

def invariants(w, n):
    comps, lk, selfw = BT.linking_and_selfwrithe(w, n)
    return dict(components=len(comps), sizes=sorted(len(c) for c in comps), lk=lk,
                jones=BT.normalise_laurent(BT.jones(w, n), BT.A),
                alex=BT.normalise_laurent(BT.burau_alexander(w, n), BT.t), selfw=selfw)

if __name__ == "__main__":
    out = {}
    for cls, reps in REPS.items():
        ref = invariants(*CANON[cls])
        for name, (w, n) in reps.items():
            inv = invariants(w, n)
            ok = all(inv[k] == ref[k] for k in ("components", "lk", "jones", "alex"))
            out[name] = dict(cls=cls, word=w, strands=n, lk=inv["lk"], components=inv["components"],
                             strand_sizes=inv["sizes"], self_writhe=inv["selfw"],
                             same_jones_alex_lk_as_canonical=ok,
                             alexander_t=str(BT.burau_alexander(w, n)))
            print(f"{cls:7s} {name:16s} n={n} len={len(w):2d} lk={inv['lk']} sizes={inv['sizes']} selfw={inv['selfw']} match={ok}")
    json.dump(out, open("ms_words.json", "w"), indent=1)
