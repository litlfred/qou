#!/usr/bin/env python3
"""gg_symmetry_probe.py — Vᵏ on 3 strands under inverse / mirror / reverse / swap.

Pre-registered in preregistration.md (commit 8b642ae0784). Bean qou-a1hh, PR #7741.
mpmath 40 dps, convention D, proton q₀ (via h2_gg_atom). Nothing fitted, selected or wired.

-- Ref: [manuscript] bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, log, TOL = ga.base, ga.log, ga.TOL
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

V = [(ONE, ZERO, 0), (ONE, -H, 1)]


def inv(tok):
    c, d, g = tok
    return (ONE, -H, g) if d == ZERO else (ONE, ZERO, g)


def sym_inverse(w):
    return [inv(t) for t in reversed(w)]


def sym_mirror(w):
    return [inv(t) for t in w]


def sym_reverse(w):
    return list(reversed(w))


def sym_swap(w):
    return [(c, d, 1 - g) for c, d, g in w]


SYMS = {"inverse": sym_inverse, "mirror": sym_mirror, "reverse": sym_reverse, "swap": sym_swap}


def chars(w):
    if not w:
        w = []
    return ga.level_chars(base.diag_of(w, 3), 3, 1)


def main() -> int:
    worst = mp.mpf(0)
    results = {}
    for k in range(1, 10):
        w = V * k
        c0 = chars(w)
        row = {"Vk": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in sorted(c0.items())},
               "passes_alone": all(v >= -TOL for v in c0.values())}
        for name, f in SYMS.items():
            c1 = chars(f(w))
            d = max(abs(c1[key] - c0[key]) for key in c0)
            worst = max(worst, d)
            row[name] = {"max_char_diff": mp.nstr(d, 5), "passes_alone": all(v >= -TOL for v in c1.values())}
        results[f"V^{k}"] = row
        log(f"V^{k}: passes alone {row['passes_alone']}; diffs "
            + ", ".join(f"{n} {row[n]['max_char_diff']}" for n in SYMS))
    ok = worst < mp.mpf("1e-30")
    log(f"[{'PASS' if ok else 'FAIL'}] S0_symmetries_preserve_levels_1_3: worst {mp.nstr(worst, 5)}")
    log("OUTCOME (i)" if ok else "OUTCOME (ii)")
    wb = WitnessBuilder("gg-symmetry", engine="mpmath", output_dir=HERE)
    wb.add_assertion("S0_symmetries_preserve_levels_1_3", computed="1" if ok else "0", expected="1",
                     source=f"worst diff {mp.nstr(worst, 5)}")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh): V^k (k=1..9) on 3 strands under inverse, mirror, reverse, swap; "
                            "characters at levels 1-3, convention D. Pre-registered. Nothing fitted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "results": results})
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
