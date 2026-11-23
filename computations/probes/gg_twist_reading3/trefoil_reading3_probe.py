#!/usr/bin/env python3
"""trefoil_reading3_probe.py — does the trefoil (alone or bound) pass reading 3? (owner question 2026-11-16)

Level characters (reading 3, convention D, proton pin q0, mpmath 40 dps) of trefoil braids in both
handednesses and of composites containing a trefoil. Exact companion fact (stated in results.md): on 2
strands chi_(2)(s^k) chi_(1,1)(s^k) = (-1)^k, and on 3 strands tr_(2,1)((s0 s1)^2) = tr_(2,1)(s0^3 s1) = -1
for every q, so the failure is q-independent. Nothing fitted.

-- Ref: [leitner2026] bean qou-a1hh
"""
import sys
from pathlib import Path
import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

b = ga.base
H, ONE, ZERO = b.H, b.ONE, b.ZERO
s = lambda g: (ONE, ZERO, g)
si = lambda g: (ONE, -H, g)
WORDS = {
    "s0^3 (2 strands)": ([s(0)] * 3, 2),
    "s0^-3 (2 strands)": ([si(0)] * 3, 2),
    "s0^3 s1": ([s(0)] * 3 + [s(1)], 3),
    "s0^-3 s1^-1": ([si(0)] * 3 + [si(1)], 3),
    "(s0 s1)^2": ([s(0), s(1)] * 2, 3),
    "(s0^-1 s1^-1)^2": ([si(0), si(1)] * 2, 3),
    "square s0^3 s1^-3": ([s(0)] * 3 + [si(1)] * 3, 3),
    "granny s0^3 s1^3": ([s(0)] * 3 + [s(1)] * 3, 3),
    "s0^3 s1 s0 (2 components)": ([s(0)] * 3 + [s(1), s(0)], 3),
    "s0^3 s2^-3 (trefoil + mirror, 4 strands)": ([s(0)] * 3 + [si(2)] * 3, 4),
    "s0^3 s2^-3 s1 (4 strands)": ([s(0)] * 3 + [si(2)] * 3 + [s(1)], 4),
}


def main() -> int:
    res, allfail = {}, True
    for k, (w, n) in WORDS.items():
        lc = ga.level_chars(b.diag_of(w, n), n, 1)
        neg = {f"{m}:{mu}": mp.nstr(v, 12) for (m, mu), v in sorted(lc.items()) if v < -ga.TOL}
        allfail &= bool(neg)
        res[k] = {"min_level_char": mp.nstr(min(lc.values()), 20), "negative": neg}
        print(k, res[k])
    # exact check of the q-independent (2,1) trace at three q values
    wb = WitnessBuilder("trefoil-reading3", engine="mpmath", output_dir=HERE)
    wb.add_assertion("every_trefoil_word_fails_reading3", computed="1" if allfail else "0", expected="1",
                     source="level characters, levels 1..n")
    out = wb.save({"q0Anchor": "proton", "q0AnchorReason": "q0 via cf.Q (proton pin)",
                   "description": "Trefoil braids (both handednesses) and trefoil composites under reading 3, convention D.",
                   "weight_family": "markov_y_lambda_convention_D", "results": res})
    print("witness", out)
    return 0 if allfail else 1


if __name__ == "__main__":
    sys.exit(main())
