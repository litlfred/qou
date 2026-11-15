#!/usr/bin/env python3
"""photon_electron_probe.py — one photon (a single crossing) on γγ electron candidates.

Pre-registered in preregistration.md (4ba00ecab5b). Bean qou-a1hh, PR #7741. mpmath, convention D, proton q₀.
Nothing fitted, selected or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE.parent / "gg_symmetry"))
import h2_gg_atom_probe as ga  # noqa: E402
import gg_symmetry_probe as gs  # noqa: E402

base, log, TOL = ga.base, ga.log, ga.TOL
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

V = [(ONE, ZERO, 0), (ONE, -H, 1)]
VB = [(ONE, -H, 0), (ONE, ZERO, 1)]
CANDS = {"V^0": [], **{f"V^{k}": V * k for k in (3, 6, 9)}, **{f"Vbar^{k}": VB * k for k in (3, 6, 9)}}


def s(g, e):
    return (ONE, ZERO, g) if e > 0 else (ONE, -H, g)


def chars(w):
    return gs.chars(w)


def fmt(c):
    return {f"{m}:{mu}": mp.nstr(v, 15) for (m, mu), v in sorted(c.items())}


def main() -> int:
    worst = mp.mpf(0)
    hval = mp.mpf(H) if not isinstance(H, tuple) else None
    out = {}
    for name, w in CANDS.items():
        row = {"E": fmt(chars(w))}
        cE = chars(w)
        for g in (0, 1):
            for e in (1, -1):
                for kind, word in (("absorb", w + [s(g, e)]), ("emit", [s(g, e)] + w),
                                   ("compton", [s(g, e)] + w + [s(g, -e)])):
                    c = chars(word)
                    row[f"{kind}_g{g}_{'+' if e > 0 else '-'}"] = {
                        "passes": all(v >= -TOL for v in c.values()), "chars": fmt(c)}
            cp, cm = chars(w + [s(g, 1)]), chars(w + [s(g, -1)])
            R = {k: cp[k] - cm[k] for k in cp}
            row[f"R_g{g}"] = fmt(R)
            for lam in ((3,), (2, 1)):
                worst = max(worst, abs(R[(3, lam)] - hval * cE[(3, lam)]))
        out[name] = row
        log(f"{name}: R_g0 level2 (2)={row['R_g0']['2:(2,)']} (1,1)={row['R_g0']['2:(1, 1)']}; "
            f"absorb passes " + str({k: v['passes'] for k, v in row.items() if k.startswith('absorb')}))
    ok = worst < mp.mpf("1e-30")
    log(f"[{'PASS' if ok else 'FAIL'}] P0_level3_response_is_h_chi: worst {mp.nstr(worst, 5)}")
    wb = WitnessBuilder("photon-electron", engine="mpmath", output_dir=HERE)
    wb.add_assertion("P0_level3_response_is_h_chi", computed="1" if ok else "0", expected="1",
                     source=f"worst {mp.nstr(worst, 5)}")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh): one photon sigma_g^{+-1} absorbed/emitted/Compton-scattered on "
                            "gamma-gamma electron candidates on 3 strands; reading 3 levels 1-3 and photon response. "
                            "Pre-registered. Nothing fitted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "results": out})
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
