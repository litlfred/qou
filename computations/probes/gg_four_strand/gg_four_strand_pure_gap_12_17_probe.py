#!/usr/bin/env python3
"""gg_four_strand_pure_gap_12_17_probe.py — pure γγ words of length 12..17 at q₀ (amendment 6).

Bean qou-a1hh. Convention D, proton q₀, mpmath 40 dps, amendment-3 seminormal representation.
G1: every pure word of length 12. G2: 20000 seeded pure words for each m = 13..17.
Pre-registered in preregistration.md (amendment 6). Nothing fitted or selected. Scope (a).
-- Ref: [manuscript] bean qou-a1hh
"""
from __future__ import annotations

import random
import sys
import time
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_four_strand_shortest_failing_pure_probe as a5  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

a4 = a5.a4
TOL = a4.TOL


def g2(ev, m, n=20000):
    rng = random.Random(6000 + m)
    seen, fails, fail_words = set(), 0, []
    vmin, arg = mp.inf, None
    while len(seen) < n:
        ts = tuple(rng.choice(a4.TYPES) for _ in range(m))
        if ts in seen or not a4.is_pure(ts):
            continue
        seen.add(ts)
        v, _ = ev.minchar(ts)
        if v < vmin:
            vmin, arg = v, ".".join(ts)
        if v < -TOL:
            fails += 1
            if len(fail_words) < 200:
                fail_words.append(".".join(ts))
    return {"n": n, "fail": fails, "fail_words": fail_words, "min_char": mp.nstr(vmin, 12), "argmin": arg}


def main() -> int:
    t0 = time.time()
    ev = a4.Eval(a4.a3.Q0)
    rel = a4.a3.check_relations(ev.rep)
    print("relations err at q0:", mp.nstr(rel, 5), flush=True)
    if rel > mp.mpf(10) ** -30:
        return 1
    out = {"G1": {}, "G2": {}}
    if "--skip-g1" not in sys.argv:
        r = a5.run(ev, 12, t0)
        r.pop("powers", None)
        out["G1"]["12"] = r
        print("G1 m=12 pure", r["n_pure"], "fail", r["pure_fail"], "min", r["min_char_pure"],
              f"{time.time()-t0:.0f}s", flush=True)
    for m in range(13, 18):
        out["G2"][str(m)] = g2(ev, m)
        g = out["G2"][str(m)]
        print("G2 m", m, "fail", g["fail"], "min", g["min_char"], f"{time.time()-t0:.0f}s", flush=True)
    lengths = [12] if out["G1"].get("12", {}).get("pure_fail") else []
    lengths += [int(m) for m, g in out["G2"].items() if g["fail"]]
    shortest = min(lengths) if lengths else None
    print("shortest failing length found in 12..17:", shortest)
    wb = WitnessBuilder("gg-four-strand-pure-gap-12-17", engine="mpmath", output_dir=HERE)
    wb.add_assertion("H4_relations_at_q0_below_1e-30", computed="1", expected="1", source="a3.check_relations")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, amendment 6): pure gg words of length 12-17 at q0 on 4 strands. "
                            "Scope (a); nothing wired.",
             "weight_family": "markov_y_lambda_convention_D", "relations_err_q0": mp.nstr(rel, 5),
             "shortest_failing_length_found_12_17": shortest, "results": out})
    return 0


if __name__ == "__main__":
    sys.exit(main())
