#!/usr/bin/env python3
"""h2_gg_electron_probe.py — H2 with a γγ electron V^k and γγ nucleon V^m (owner 2026-11-15).

Bean `qou-a1hh`, PR #7741. Recipe: `preregistration.md` here (committed e1e22ebfb1d before this file).
Reuses `../h2_gg_atom/h2_gg_atom_probe.h2_rows` unchanged; the electron is supplied via kct.ELECTRONS.
mpmath 40 dps, convention D, proton pin. Trace ratio reported only (ruling B). Nothing fitted or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, kct, mjw, log, TOL = ga.base, ga.kct, ga.mjw, ga.log, ga.TOL
from qou_substrate.witness import WitnessBuilder  # noqa: E402

CORPUS_ELECTRONS = dict(kct.ELECTRONS)


def use_electrons(d):
    kct.ELECTRONS.clear()
    kct.ELECTRONS.update(d)


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}")

    # E0: hook reproduces h2_gg_atom rows for V^3 nucleon, T_w0 electron
    old = json.loads((HERE.parent / "h2_gg_atom" / "h2-gg-atom.witness.json").read_text())["results"]["V^3"]
    use_electrons({"Tw0_s0s1s0": CORPUS_ELECTRONS["Tw0_s0s1s0"]})
    new = ga.h2_rows(ga.vm(3), 1)
    worst = mp.mpf(0)
    for tag, res in new.items():
        for rn, ro in zip(res["rows"], old[tag]["rows"]):
            for key, v in ro["chars"].items():
                worst = max(worst, abs(mp.mpf(v) - mp.mpf(rn["chars"][key])))
    check("E0_hook_reproduces_h2_gg_atom", worst < mp.mpf("1e-18"), f"max diff {mp.nstr(worst, 5)}")

    ok1 = True
    for k in range(0, 8):
        w = base.V(0) * k
        if k:
            lc = ga.level_chars(base.diag_of(w, 3), 3, 1)
            ok1 &= abs(lc[(3, (3,))] - 1) < TOL
    check("E1_chi3_Vk_is_1", ok1, "trivial rep")

    results = {}
    for m in (3, 6):
        for k in range(0, 8):
            log(f"nucleon V^{m}, electron V^{k}")
            use_electrons({f"V^{k}": (lambda b, k=k: base.V(b) * k)})
            results[f"nucleon=V^{m},electron=V^{k}"] = ga.h2_rows(ga.vm(m), 1)
    use_electrons(CORPUS_ELECTRONS)

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-gg-electron", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner 2026-11-15 'test a gamma-gamma electron'): H2 with nucleon V^m "
                       "(m=3,6) and electron V^k (k=0..7), no p-e or junction letter, bond K in {none,V,V^2,V^3} at "
                       "s=4,5; reading 3 at every level 1..12, convention D. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "results": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
