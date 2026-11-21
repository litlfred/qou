#!/usr/bin/env python3
"""gg_entangled_pair_stage4_probe.py — stage 4: one prior γγ pair across the proton|electron boundary.

Pre-registered in preregistration.md §Stage 4 (commit 3f6f5a66d4b) before this file. Owner card 2026-11-16:
the bound electron's q^{±2} shift comes from one γγ pair created before binding (no virtual photons).
Atom = nucleon V^m (m in {3,6}) + pair P at window b in {1,2} + free electron V^3; H2 recipe of stage 2.
mpmath 40 dps, convention D, proton pin. Nothing fitted or selected.
-- Ref: [leitner2026] gamma-gamma-generates-particles; beans qou-a1hh, qou-99qc
"""
from __future__ import annotations

import sys
import time
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
PAIR = {  # each is a product of two photon letters: one L term and one V^-1
    "none": lambda b: [],
    "Lp.Vi": lambda b: [S(b), S(b + 1), S(b + 1), SI(b)],
    "Vi.Lp": lambda b: [S(b + 1), SI(b), S(b), S(b + 1)],
    "Lm.Vi": lambda b: [SI(b), SI(b + 1), S(b + 1), SI(b)],
    "Vi.Lm": lambda b: [S(b + 1), SI(b), SI(b), SI(b + 1)],
}
CFG = {}


def vpow(m, s):
    return base.V(s) * m


def atom(order, pe_letter):
    m, pair, b = CFG["m"], PAIR[CFG["pair"]], CFG["b"]
    if order == "pe":
        return vpow(m, 0) + pair(b) + vpow(3, 3), ["p", "p", "p", "e", "e", "e"]
    return vpow(3, 0) + pair(b) + vpow(m, 3), ["e", "e", "e", "p", "p", "p"]


def main() -> int:
    t0 = time.time()
    kct.atom = atom
    kct.ELECTRONS.clear()
    kct.ELECTRONS["V3"] = lambda s: vpow(3, s)
    atoms, h2 = {}, {}
    cfgs = [(m, "none", 0) for m in (3, 6)] + [(m, p, b) for m in (3, 6) for p in PAIR if p != "none" for b in (1, 2)]
    for m, p, b in cfgs:
        CFG.update(m=m, pair=p, b=b)
        tag = f"nucleon=V^{m},pair={p},b={b}"
        a = {}
        for order in ("pe", "ep"):
            w, _ = atom(order, False)
            lc = ga.level_chars(base.diag_of(w, 6), 6, 1)
            fails = sorted({k for (k, mu), v in lc.items() if v < -ga.TOL})
            a[order] = {"reading3_every_level": not fails, "failing_levels": fails,
                        "chi_6": mp.nstr(lc[(6, (6,))], 20),
                        "writhe": sum(1 if d == ZERO else -1 for _, d, _ in w)}
        atoms[tag] = a
        log(f"[{time.time()-t0:6.0f}s] {tag}: atom pe {a['pe']['reading3_every_level']} ep {a['ep']['reading3_every_level']} "
            f"chi6 {a['pe']['chi_6'][:10]}")
        h2[tag] = ga.h2_rows(None, 1)
    summary = {}
    for tag, res in h2.items():
        cell = {}
        for t2, r in res.items():
            cell[t2] = {"bare_passes": r["rows"][0]["reading3_every_level"],
                        "passing_bonds": [f"{x['K']}@{x['site']}" for x in r["rows"][1:] if x["reading3_every_level"]]}
        summary[tag] = cell
        log(f"{tag}: {cell}")
    wb = WitnessBuilder("gg-entangled-pair-stage4", engine="mpmath", output_dir=HERE)
    wb.add_assertion("ran_all_configs", computed=str(len(summary)), expected=str(len(cfgs)), source="2 nucleons x (control + 4 pairs x 2 windows)")
    out = wb.save({"q0Anchor": "proton", "q0AnchorReason": "q0 via cf.Q (proton pin)",
                   "description": "PROBE stage 4 (beans qou-a1hh, qou-99qc): atom = V^m nucleon + one γγ pair (L term x V^-1) "
                                  "across the p|e boundary + free V^3 electron; atom alone and H2 under reading 3. Pre-registered.",
                   "weight_family": "markov_y_lambda_convention_D", "atoms": atoms, "summary": summary, "h2": h2})
    log(f"witness {out} {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
