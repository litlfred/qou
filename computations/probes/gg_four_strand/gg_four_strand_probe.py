#!/usr/bin/env python3
"""gg_four_strand_probe.py — γγ words on 4 strands, both orientations (pre-registered, ba70b76ef7a).

Bean qou-a1hh. Convention D, proton q₀ (base module, 40 dps). Hypothesis only; nothing adopted or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-wkcd
"""
from __future__ import annotations

import itertools
import json
import sys
from collections import Counter
from pathlib import Path

import mpmath as mp

mp.mp.dps = max(mp.mp.dps, 40)  # stated here: the probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, log = ga.base, ga.log
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

TOL = mp.mpf(10) ** -30
TYPES = [f"{o}{s}" for s in range(2) for o in "VB"]


def vert(t):
    o, s = t[0], int(t[1])
    return [(ONE, ZERO, s), (ONE, -H, s + 1)] if o == "V" else [(ONE, -H, s), (ONE, ZERO, s + 1)]


def word(ts):
    return [x for t in ts for x in vert(t)]


def chars(ts, n=4):
    return ga.level_chars(base.diag_of(word(ts), n), n, 1)


def main() -> int:
    ref = json.loads((HERE.parent / "gg_two_orientations" / "gg-two-orientations.witness.json").read_text())["results"]
    t0 = True
    for k, r in ref.items():
        if len(k) > 4:
            continue
        c = chars([f"{x}0" for x in k])
        for key, v in r["chars"].items():
            lvl, mu = key.split(":")
            if abs(c[(int(lvl), tuple(json.loads(mu.replace("(", "[").replace(")", "]").replace(",]", "]"))))] - mp.mpf(v)) > mp.mpf(10) ** -12:
                t0 = False
    log(f"[{'PASS' if t0 else 'FAIL'}] T0_restriction_matches_3_strand")
    if not t0:
        return 1
    rows, passing = {}, []
    for m in range(1, 7):
        for ts in itertools.product(TYPES, repeat=m):
            c = chars(ts)
            ok = all(v >= -TOL for v in c.values())
            name = ".".join(ts)
            rows[name] = {"passes_alone": ok, "chi31": mp.nstr(c[(4, (3, 1))], 12),
                          "min_char": mp.nstr(min(c.values()), 8)}
            if ok:
                passing.append(name)
        log(f"m={m}: {sum(1 for p in passing if p.count('.') == m - 1)} / {4 ** m} pass")
    by_m = Counter(p.count(".") + 1 for p in passing)
    all_sites = [p for p in passing if {t[1] for t in p.split('.')} == {"0", "1"}]
    log(f"R2 pass a function of m alone: {all(by_m.get(m, 0) in (0, 4 ** m) for m in range(1, 5))}")
    log(f"R3 passing words using all three sites: {len(all_sites)}; first {all_sites[:12]}")
    wb = WitnessBuilder("gg-four-strand", engine="mpmath", output_dir=HERE)
    wb.add_assertion("T0_restriction_matches_3_strand", computed="1", expected="1", source="gg-two-orientations.witness.json")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh, hypothesis): gg words in {V_s, Vbar_s}, s=0..1, on 4 strands, "
                            "length 1..6; reading 3 alone at levels 1-4. Pre-registered. Nothing adopted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "pass_count_by_m": dict(by_m),
             "passing": passing, "passing_all_sites": all_sites, "results": rows})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
