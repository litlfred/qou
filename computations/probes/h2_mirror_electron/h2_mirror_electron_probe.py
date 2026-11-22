#!/usr/bin/env python3
"""h2_mirror_electron_probe.py — H2 with mirror γγ electrons (pre-registered, see preregistration.md).

Bean qou-a1hh, PR #7741. Reuses h2_gg_atom.h2_rows; mpmath, convention D, proton q₀. Nothing fitted or wired.
-- Ref: [manuscript] prop:ilp-covalent-bond; bean qou-a1hh
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, kct, log = ga.base, ga.kct, ga.log
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

CORPUS = dict(kct.ELECTRONS)


def Vbar(b):
    return [(ONE, -H, b), (ONE, ZERO, b + 1)]


ELECTRONS = {"Vbar^3": lambda b: Vbar(b) * 3, "Vbar^6": lambda b: Vbar(b) * 6,
             "V^9": lambda b: base.V(b) * 9, "Vbar^9": lambda b: Vbar(b) * 9}


def main() -> int:
    results, summary = {}, {}
    for m in (3, 6):
        for ename, f in ELECTRONS.items():
            log(f"nucleon V^{m}, electron {ename}")
            kct.ELECTRONS.clear()
            kct.ELECTRONS[ename] = f
            res = ga.h2_rows(ga.vm(m), 1)
            results[f"nucleon=V^{m},electron={ename}"] = res
            for tag, r in res.items():
                summary[f"V^{m}|{tag}"] = sorted(f"{row['K']}@{row['site']}" for row in r["rows"]
                                                 if row["reading3_every_level"])
                log(f"  PASS SET {tag}: {summary[f'V^{m}|{tag}']}")
    kct.ELECTRONS.clear()
    kct.ELECTRONS.update(CORPUS)
    target = sorted(["none@None", "V^3@4", "V^3@5"])
    same = all(v == target for v in summary.values())
    log("OUTCOME (i)" if same else "OUTCOME (ii)")
    wb = WitnessBuilder("h2-mirror-electron", engine="mpmath", output_dir=HERE)
    wb.add_assertion("M0_runs", computed="1", expected="1", source="all cells evaluated")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh): H2 with nucleon V^m (m=3,6) and mirror/9-power gamma-gamma "
                            "electrons; reading 3 every level, convention D. Pre-registered. Nothing fitted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "summary": summary,
             "outcome": "i" if same else "ii", "results": results})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
