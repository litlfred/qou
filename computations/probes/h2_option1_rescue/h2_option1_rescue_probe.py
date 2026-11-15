#!/usr/bin/env python3
"""h2_option1_rescue_probe.py — can a p-e letter sigma_2^a rescue H2 with the trefoil electron?

Owner card 2026-11-15 "Measure option 1 first". Bean qou-a1hh, PR #7741.
Recipe: preregistration.md here (committed 595351ba20a before this file).
Reuses h2_gg_atom / h2_one_rule unchanged (mpmath 40 dps, convention D, proton pin).
Trace ratios reported, never used to select. Nothing fitted, selected against data, or wired.

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
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
import h2_gg_atom_probe as gg  # noqa: E402

base, kct = gg.base, gg.kct
ONE, ZERO, TOL, N, y, log = base.ONE, base.ZERO, base.TOL, base.N, base.y, base.log
H = base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

P = base.V(0) * 3
E_WORD = kct.ELECTRONS["trefoil_s0s0s0s1"]


def sig(g, a):
    """sigma_g^a as a token list (a may be negative)."""
    return [(ONE, ZERO, g)] * a if a > 0 else [(ONE, -H, g)] * (-a)


def hydrogen(a, order="pe"):
    if order == "pe":
        return P + sig(2, a) + E_WORD(3)
    return E_WORD(0) + sig(2, a) + kct.shift(P, 3)


def summarise(lc):
    fails = sorted({m for (m, mu), v in lc.items() if v < -TOL})
    return {"reading3_every_level": not fails, "failing_levels": fails,
            "negative": [f"{m}:{mu}={mp.nstr(v, 10)}" for (m, mu), v in sorted(lc.items()) if v < -TOL],
            "chars": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in sorted(lc.items())}}


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")

    # Stage 1: hydrogen atom on 6 strands
    stage1 = {}
    for a in range(-3, 4):
        lc = gg.level_chars(base.diag_of(hydrogen(a), 6), 6, 1)
        stage1[a] = summarise(lc)
        r = stage1[a]
        log(f"stage1 a={a:+d}: every-level={r['reading3_every_level']} fails {r['failing_levels']} {r['negative'][:3]}")
    pred = mp.mpf("-0.31373335326276292589")
    c0 = stage1[0]["chars"]
    r0 = mp.mpf(c0["6:(3, 3)"]) / mp.mpf(c0["6:(6,)"])
    check("A0_control_a0_matches_derivation", abs(r0 - pred) < mp.mpf("1e-18"), f"(3,3)/(6) = {mp.nstr(r0, 20)}")

    # J1: bare trefoil H2 plus one junction letter sigma_5^-1, level 6 ratio unchanged
    w1 = hydrogen(0)
    x = w1 + sig(5, -1) + kct.shift(w1, 6)
    lcj = gg.level_chars(base.diag_of(x, N), N, 6)
    rj = lcj[(6, (3, 3))] / lcj[(6, (6,))]
    check("J1_single_junction_letter_keeps_level6_ratio", abs(rj - pred) < mp.mpf("1e-18"),
          f"(3,3)/(6) = {mp.nstr(rj, 20)}")

    # Stage 2: full H2 for every a passing stage 1
    stage2 = {}
    for a in [a for a in stage1 if stage1[a]["reading3_every_level"]]:
        for atom2 in ("pe", "ep"):
            w1, w2 = hydrogen(a, "pe"), hydrogen(a, atom2)
            x = w1 + kct.shift(w2, 6)
            prefix = {}
            for lam in base.two_row(N):
                dim = kct.cols(list(lam))[1]
                I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
                prefix[lam] = kct.right_apply(I, x, list(lam))
            dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
            trx = mp.fsum(y(l) * mp.fsum(dx[l]) for l in base.two_row(N))
            rows = []
            for k in (0, 1, 2, 3):
                for s in ((None,) if k == 0 else (4, 5)):
                    d = dx if k == 0 else base.diag_of(base.V(s) * k, N, prefix)
                    lc = gg.level_chars(d, N, 1)
                    tr = mp.fsum(y(l) * lc[(N, l)] for l in base.two_row(N))
                    row = {"K": "none" if k == 0 else f"V^{k}", "site": s, "ratio": mp.nstr(tr / trx, 20)}
                    row.update(summarise(lc))
                    rows.append(row)
                    log(f"stage2 a={a:+d} atom2={atom2} K={row['K']}@{s}: every-level={row['reading3_every_level']} "
                        f"fails {row['failing_levels']} ratio {row['ratio'][:10]}")
            stage2[f"a={a},atom2={atom2}"] = {"tr_x": mp.nstr(trx, 30), "rows": rows}

    passing = [(t, r["K"], r["site"]) for t, v in stage2.items() for r in v["rows"]
               if r["reading3_every_level"] and r["K"] != "none"]
    bare_pass = [t for t, v in stage2.items() if v["rows"][0]["reading3_every_level"]]
    s1_pass = [a for a in stage1 if stage1[a]["reading3_every_level"]]
    if not s1_pass:
        outcome = "iii"
    elif bare_pass or passing:
        outcome = "i"
    else:
        outcome = "ii"
    log(f"OUTCOME ({outcome}): stage1 pass a={s1_pass}; bare H2 pass {bare_pass}; bonded passes {passing}")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-option1-rescue", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (bean qou-a1hh, owner card 'Measure option 1 first'): nucleon V^3, trefoil electron "
                       "s0^3 s1, p-e letter sigma_2^a, a in -3..3; stage 1 hydrogen atom levels 1..6, stage 2 full H2 "
                       "levels 1..12 with bonds V^k at s=4,5. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "outcome": outcome,
        "stage1": {str(a): v for a, v in stage1.items()},
        "stage2": stage2,
        "stage1_passing_a": s1_pass, "bare_h2_passing": bare_pass,
        "bonded_passing": [list(map(str, p)) for p in passing],
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
