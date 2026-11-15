#!/usr/bin/env python3
"""h2_order_test_probe.py — does the molecule-only rule (option 2) depend on which particle is lowest?

Owner card 2026-11-15 "Must each particle pass reading 3 on its own strands?" -> "3. Measure first".
Bean qou-a1hh, PR #7741. Recipe: preregistration.md here (committed 428919bc80b before this file).
Reuses h2_gg_atom / h2_one_rule unchanged (mpmath 40 dps, convention D, proton pin).
Nothing fitted, selected against data, or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
import h2_gg_atom_probe as gg  # noqa: E402

base, kct = gg.base, gg.kct
ONE, ZERO, TOL, N, log = base.ONE, base.ZERO, base.TOL, base.N, base.log
from qou_substrate.witness import WitnessBuilder  # noqa: E402

NUCLEONS = {f"V{k}": base.V(0) * k for k in range(1, 8)}
ELECTRONS = {"V3": base.V(0) * 3, "torus_m7": [(ONE, ZERO, 0)] * 7 + [(ONE, ZERO, 1)]}


def sh(w, s):
    return [(c, d, g + s) for c, d, g in w]


def fails(lc):
    return sorted({k for (k, mu), v in lc.items() if v < -TOL})


def alone_pass(w):
    return not fails(gg.level_chars(base.diag_of(w, 3), 3, 1))


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")

    rows, o2_ok = {}, True
    for pn, P in NUCLEONS.items():
        for en, E in ELECTRONS.items():
            for o1 in ("pe", "ep"):
                for o2 in ("pe", "ep"):
                    a1 = P + sh(E, 3) if o1 == "pe" else E + sh(P, 3)
                    a2 = P + sh(E, 3) if o2 == "pe" else E + sh(P, 3)
                    x = a1 + sh(a2, 6)
                    f = fails(gg.level_chars(base.diag_of(x, N), N, 1))
                    bottom = P if o1 == "pe" else E
                    pred = alone_pass(bottom)
                    got = not [m for m in f if m <= 3]
                    o2_ok &= (pred == got)
                    tag = f"P={pn},E={en},atom1={o1},atom2={o2}"
                    rows[tag] = {"fails": f, "every_level": not f, "bottom_alone_pass": pred}
                    log(f"{tag}: every-level={not f} fails {f} (bottom alone pass {pred})")
    check("O2_levels_1_3_equal_bottom_particle_alone", o2_ok, "tensor-product Markov factorisation")

    passing = {o1: sorted({(t.split(',')[0], t.split(',')[1]) for t, r in rows.items()
                           if r["every_level"] and f"atom1={o1}" in t}) for o1 in ("pe", "ep")}
    outcome = "i" if passing["pe"] != passing["ep"] else "ii"
    log(f"OUTCOME ({outcome}): passing with atom1=pe {passing['pe']}; with atom1=ep {passing['ep']}")

    wb = WitnessBuilder("h2-order-test", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner 'measure first'): bare H2 = (atom1)(atom2), nucleon V^k k<=7, "
                       "electron V^3 or sigma0^7 sigma1, atom orders pe/ep; reading 3 every level, convention D. "
                       "Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "outcome": outcome, "molecules": rows,
        "passing_by_atom1_order": {k: [list(v) for v in vs] for k, vs in passing.items()},
    })
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
