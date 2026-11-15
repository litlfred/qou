#!/usr/bin/env python3
"""gg_four_strand_shortest_failing_pure_probe.py — shortest failing pure γγ word at q₀ (amendment 5).

Bean qou-a1hh. Convention D, proton q₀, mpmath 40 dps, amendment-3 seminormal representation.
S1: every pure word of length 9, 10, 11. S2: powers u^k (k ≥ 2, k·|u| ≤ 23) of every pure u with 7 ≤ |u| ≤ 11.
Pre-registered in preregistration.md (amendment 5). Nothing fitted or selected. Scope (a).
-- Ref: [manuscript] bean qou-a1hh
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_four_strand_pure_long_q0_probe as a4  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

TOL = a4.TOL
TYPES = a4.TYPES
LAMS = a4.LAMS
PERM = {t: None for t in TYPES}
MAXLEN = 23
CAP = 200


def tperm(t):
    s = int(t[1]) + 1
    p = list(range(4))
    for g in (s, s + 1):
        p[g - 1], p[g] = p[g], p[g - 1]
    return p


def compose(p, t):
    """Apply a3.perm's update rule for one more letter."""
    q = list(p)
    s = int(t[1]) + 1
    for g in (s, s + 1):
        q[g - 1], q[g] = q[g], q[g - 1]
    return tuple(q)


def run(ev, m, t0):
    res = {"n_pure": 0, "pure_fail": 0, "pure_fail_words": [], "min_char_pure": mp.inf, "argmin": None,
           "powers": {}}
    ident = (0, 1, 2, 3)
    I = {lam: mp.eye(len(a4.a3.TAB[lam])) for lam in LAMS}
    leaves = [0]

    def rec(prefix, W, p):
        if len(prefix) == m:
            leaves[0] += 1
            if leaves[0] % 200000 == 0:
                print(f"  m={m} leaves {leaves[0]} pure {res['n_pure']} {time.time()-t0:.0f}s", flush=True)
            if p != ident:
                return
            res["n_pure"] += 1
            word = ".".join(prefix)
            if m >= 9:
                v = min(ev.chars_from(W).values())
                if v < res["min_char_pure"]:
                    res["min_char_pure"], res["argmin"] = v, word
                if v < -TOL:
                    res["pure_fail"] += 1
                    if len(res["pure_fail_words"]) < CAP:
                        res["pure_fail_words"].append(word)
            P = W
            k = 1
            while (k + 1) * m <= MAXLEN:
                k += 1
                P = {lam: P[lam] * W[lam] for lam in LAMS}
                v = min(ev.chars_from(P).values())
                rec_k = res["powers"].setdefault(str(k), {"tested": 0, "fail": 0, "fail_words": [],
                                                          "min_char": mp.inf})
                rec_k["tested"] += 1
                rec_k["min_char"] = min(rec_k["min_char"], v)
                if v < -TOL:
                    rec_k["fail"] += 1
                    if len(rec_k["fail_words"]) < CAP:
                        rec_k["fail_words"].append(word)
            return
        for t in TYPES:
            rec(prefix + (t,), {lam: W[lam] * ev.rep.vert(lam, t) for lam in LAMS}, compose(p, t))

    rec((), I, ident)
    res["min_char_pure"] = mp.nstr(res["min_char_pure"], 15) if res["n_pure"] and m >= 9 else None
    for r in res["powers"].values():
        r["min_char"] = mp.nstr(r["min_char"], 12)
    return res


def main() -> int:
    t0 = time.time()
    ev = a4.Eval(a4.a3.Q0)
    rel = a4.a3.check_relations(ev.rep)
    print("relations err at q0:", mp.nstr(rel, 5), flush=True)
    if rel > mp.mpf(10) ** -30:
        return 1
    ms = [int(x) for x in sys.argv[1:]] or [7, 8, 9, 10, 11]
    out = {}
    for m in ms:
        out[str(m)] = run(ev, m, t0)
        r = out[str(m)]
        print("m", m, "pure", r["n_pure"], "pure_fail", r["pure_fail"], "min", r["min_char_pure"],
              "powers", {k: (v["tested"], v["fail"]) for k, v in r["powers"].items()}, f"{time.time()-t0:.0f}s",
              flush=True)
    lengths = [int(m) for m, r in out.items() if r["pure_fail"]]
    lengths += [int(m) * int(k) for m, r in out.items() for k, v in r["powers"].items() if v["fail"]]
    shortest = min(lengths) if lengths else None
    print("shortest failing length found:", shortest)
    wb = WitnessBuilder("gg-four-strand-shortest-failing-pure", engine="mpmath", output_dir=HERE)
    wb.add_assertion("H4_relations_at_q0_below_1e-30", computed="1", expected="1", source="a3.check_relations")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, amendment 5): shortest failing pure gg word at q0 on 4 strands. "
                            "Scope (a); nothing wired.",
             "weight_family": "markov_y_lambda_convention_D", "relations_err_q0": mp.nstr(rel, 5),
             "shortest_failing_length_found": shortest, "results": out})
    return 0


if __name__ == "__main__":
    sys.exit(main())
