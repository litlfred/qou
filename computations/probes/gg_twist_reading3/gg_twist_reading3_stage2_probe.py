#!/usr/bin/env python3
"""gg_twist_reading3_stage2_probe.py — stage 2: H2 with the shortest chiral passing electrons.

Pre-registered in preregistration.md §Stage 2 (commit 72aa0c3f14b), triggered because stage 1 found passing
words of nonzero writhe. Electrons: the four length-2 words V^-1.L+, V^-1.L-, L+.V^-1, L-.V^-1.
Nucleon V^3 and V^6. Same H2 recipe as h2_gg_electron (bonds none, V, V^2, V^3 at s = 4, 5; levels 1..12).
mpmath 40 dps, convention D, proton pin. Nothing fitted or selected.

-- Ref: [leitner2026] beans qou-a1hh, qou-99qc
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, kct, log = ga.base, ga.kct, ga.log
from qou_substrate.witness import WitnessBuilder  # noqa: E402

ONE, ZERO, H = mp.mpf(1), mp.mpf(0), base.H
S = lambda g: (ONE, ZERO, g)
SI = lambda g: (ONE, -H, g)
ELEC = {
    "Vi.Lp": lambda b: [S(b + 1), SI(b), S(b), S(b + 1)],
    "Vi.Lm": lambda b: [S(b + 1), SI(b), SI(b), SI(b + 1)],
    "Lp.Vi": lambda b: [S(b), S(b + 1), S(b + 1), SI(b)],
    "Lm.Vi": lambda b: [SI(b), SI(b + 1), S(b + 1), SI(b)],
}


def main() -> int:
    corpus = dict(kct.ELECTRONS)
    results = {}
    for m in (3, 6):
        for name, fn in ELEC.items():
            log(f"nucleon V^{m}, electron {name}")
            kct.ELECTRONS.clear()
            kct.ELECTRONS[name] = fn
            results[f"nucleon=V^{m},electron={name}"] = ga.h2_rows(ga.vm(m), 1)
    kct.ELECTRONS.clear()
    kct.ELECTRONS.update(corpus)
    summary = {}
    for key, res in results.items():
        for tag, r in res.items():
            bare = r["rows"][0]
            summary[f"{key}|{tag}"] = {
                "bare_passes_every_level": bare["reading3_every_level"],
                "bare_failing_levels": bare["failing_levels"],
                "bonds_passing": [f"{x['K']}@{x['site']}" for x in r["rows"][1:] if x["reading3_every_level"]],
            }
            print(key, tag, summary[f"{key}|{tag}"], flush=True)
    wb = WitnessBuilder("gg-twist-reading3-stage2", engine="mpmath", output_dir=HERE)
    wb.add_assertion("ran_all_cells", computed=str(len(summary)), expected="16", source="2 nucleons x 4 electrons x 2 orientations")
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
        "description": "PROBE stage 2 (beans qou-a1hh, qou-99qc): H2 with nucleon V^3/V^6 and the four length-2 chiral "
                       "electrons over {V, V^-1, L+, L-}; reading 3 at levels 1..12. Pre-registered.",
        "summary": summary,
        "results": results,
    })
    return 0 if len(summary) == 16 else 1


if __name__ == "__main__":
    raise SystemExit(main())
