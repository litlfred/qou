#!/usr/bin/env python3
"""J4-projected reading 3 on the m = 6 flavour-changing gamma-gamma words (pre-registered, amendment 2).

Bean qou-a1hh / qou-wkcd. Explicit (3,1) rep of H_4(q) from draft PR #7957
(n4_left_doublet_flavour_probe.py), evaluated in mpmath at the proton q0 of the base module.
Hypothesis only; nothing adopted or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-wkcd
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = max(mp.mp.dps, 40)  # stated here: the probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_four_strand_probe as g4  # noqa: E402

ga, base, log = g4.ga, g4.base, g4.log
from qou_substrate.witness import WitnessBuilder  # noqa: E402

TOL = mp.mpf(10) ** -30
q = mp.mpf(base.Q)
n = q**2 + 1
I3 = mp.eye(3)
s1 = mp.diag([q, q, -1 / q])
s3 = mp.diag([q, -1 / q, q])
s2 = mp.matrix([[q**2 - 1, -(q**4 + 1), q**2 * (q**4 + 1)],
                [-q**2, q**4, q**4],
                [1, 1, q**4]]) / (q * n)
S = [s1, s2, s3]
Si = [s - (q - 1 / q) * I3 for s in S]
PL, PR = mp.diag([1, 1, 0]), mp.diag([0, 0, 1])
J4 = s3 * s2 * s1 * s1 * s2 * s3
Ja = PL * (J4 - q**4 * I3) / (q**-2 - q**4)
Jb = PL * (J4 - q**-2 * I3) / (q**4 - q**-2)


def tr(M):
    return sum(M[i, i] for i in range(3))


def rep(ts):
    w = I3
    for t in ts:
        o, s = t[0], int(t[1])
        w = w * (S[s] * Si[s + 1] if o == "V" else Si[s] * S[s + 1])
    return w


def main() -> int:
    wit = json.loads((HERE / "gg-four-strand.witness.json").read_text())
    cands = [p for p in wit["passing"] if p.count(".") == 5 and any(t[1] == "1" for t in p.split("."))]
    log(f"candidates (m=6, passing, contains site 1): {len(cands)}")
    rel = max(abs(x) for x in [mp.norm(Ja + Jb - PL), mp.norm(J4 * s1 - s1 * J4), mp.norm(J4 * s2 - s2 * J4)])
    t1, rows, npass = True, {}, 0
    for name in cands:
        ts = name.split(".")
        w = rep(ts)
        chi = g4.chars(ts)[(4, (3, 1))]
        if abs(tr(w) - chi) > TOL:
            t1 = False
        da, db, dR = tr(Ja * w * Ja), tr(Jb * w * Jb), tr(PR * w * PR)
        flip = tr(Ja * w * Jb * w * Ja)
        ok = all(x >= -TOL for x in (da, db, dR))
        npass += ok
        rows[name] = {k: mp.nstr(v, 12) for k, v in dict(d_a=da, d_b=db, d_R=dR, flip=flip, chi31=chi).items()}
        rows[name]["projected_pass"] = ok
    log(f"[{'PASS' if rel < TOL else 'FAIL'}] T_rep: Ja+Jb=PL, J4 commutes with s1,s2 (max {mp.nstr(rel, 3)})")
    log(f"[{'PASS' if t1 else 'FAIL'}] T1_trace_matches_chi31")
    if not t1 or rel >= TOL:
        return 1
    log(f"projected reading 3 passes: {npass} / {len(cands)}")
    for k, r in rows.items():
        log(f"  {k:24s} pass={r['projected_pass']!s:5s} d_a={r['d_a']:>16s} d_b={r['d_b']:>16s} d_R={r['d_R']:>16s} flip={r['flip']}")
    wb = WitnessBuilder("gg-four-strand-j4-projected", engine="mpmath", output_dir=HERE)
    wb.add_assertion("T1_trace_matches_chi31", computed="1", expected="1", source="gg-four-strand.witness.json")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (base.Q, proton pin)",
             "description": "PROBE (beans qou-a1hh/qou-wkcd, hypothesis): J4-projected reading 3 on m=6 passing gg words "
                            "containing a site-1 vertex, in the explicit (3,1) rep of PR #7957. Pre-registered (amendment 2).",
             "weight_family": "markov_y_lambda_convention_D", "n_candidates": len(cands),
             "n_projected_pass": npass, "results": rows})
    return 0


if __name__ == "__main__":
    sys.exit(main())
