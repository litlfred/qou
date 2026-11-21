#!/usr/bin/env python3
"""h2_bond_min_action_probe.py — the H2 bond by minimum Markov trace, gamma-gamma words up to 6 photons.

Issue #8879. Recipe: PREREGISTRATION.md here (committed 0e083dfc960 before this file).

Candidates: words in V4, V5 of length 1..6 that are atom-preserving and not split across the atom
cut (Python mirrors of `atomPreserving` / `splitAcross` in QOU/Molecular/H2BondSelectionRoutes.lean).
For each, in the four cells of h2_ruled_electron: reading 3 at every level, and tr_M ratio.
Hypothesis H: the least ratio among passing candidates is at V4^3 or V5^3 in every cell.
Reuses ../h2_ruled_electron (and through it h2_gg_atom, h2_one_rule) unchanged. Nothing fitted or wired.

-- Ref: [leitner2026] prop:ilp-covalent-bond; prop:confinement-lp; issue #8879
"""
from __future__ import annotations

import itertools
import json
import sys
from multiprocessing import Pool
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_ruled_electron"))
import h2_ruled_electron_probe as re_  # noqa: E402

ga, base, kct, log, TOL, N = re_.ga, re_.base, re_.kct, re_.log, re_.TOL, re_.N
ONE, ZERO, y = re_.ONE, re_.ZERO, re_.y
from qou_substrate.witness import WitnessBuilder  # noqa: E402

LOCAL = {"V4": [(0, 1), (1, -1)], "V5": [(1, 1), (2, -1)]}
MAXLEN = 6


def local_word(tup):
    return [c for t in tup for c in LOCAL[t]]


def atom_preserving(tup):
    p = [0, 1, 2, 3]
    for i, _ in local_word(tup):
        p[i], p[i + 1] = p[i + 1], p[i]
    return all(v < 2 for v in p[:2])


def free_reduce(w):
    acc = []
    for i, e in w:
        if acc and acc[-1][0] == i and acc[-1][1] + e == 0:
            acc.pop()
        else:
            acc.append((i, e))
    return acc


def split_across(tup):
    return all(i != 1 for i, _ in free_reduce(local_word(tup)))


def candidates():
    out = []
    for n in range(1, MAXLEN + 1):
        for tup in itertools.product(("V4", "V5"), repeat=n):
            if atom_preserving(tup) and not split_across(tup):
                out.append(tup)
    return out


def rows_for(m, atom2, cands):
    kct.proton_block = ga.vm(m)
    kct.ELECTRON = re_.ELECTRON
    w1, _ = kct.atom("pe", False)
    w2, _ = kct.atom(atom2, False)
    x = w1 + kct.shift(w2, 6)
    prefix = {}
    for lam in ga.two_row(N):
        dim = kct.cols(list(lam))[1]
        I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
        prefix[lam] = kct.right_apply(I, x, list(lam))
    dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
    lcx = ga.level_chars(dx, N, 1)
    trx = mp.fsum(y(l) * lcx[(N, l)] for l in ga.two_row(N))
    rows = []
    for tup in cands:
        word = sum((re_.LETTERS[t] for t in tup), [])
        d = base.diag_of(word, N, prefix)
        lc = ga.level_chars(d, N, 1)
        tr = mp.fsum(y(l) * lc[(N, l)] for l in ga.two_row(N))
        fails = sorted({k for (k, mu), v in lc.items() if v < -TOL})
        rows.append({"K": ".".join(tup), "photons": len(tup), "reading3_every_level": not fails,
                     "failing_levels": fails, "ratio": mp.nstr(tr / trx, 25)})
    return {"m": m, "atom2": atom2, "tr_x": mp.nstr(trx, 30), "rows": rows}


def _job(args):
    m, atom2, cands = args
    r = rows_for(m, atom2, cands)
    log(f"done V^{m} atom2={atom2}: {sum(r_['reading3_every_level'] for r_ in r['rows'])}/{len(cands)} pass")
    return r


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name} — {src}")

    cands = candidates()
    short = sorted(".".join(t) for t in cands if len(t) <= 3)
    check("C1_short_candidates_match_gg_atom_bonds", short == ["V4.V4.V4", "V5.V5.V5"],
          f"length<=3 kept: {short} (Lean gg_atom_bonds)")
    log(f"{len(cands)} candidates of length <= {MAXLEN}: " + ", ".join(".".join(t) for t in cands))

    jobs = [(m, a, cands) for m in (3, 6) for a in ("pe", "ep")]
    with Pool(len(jobs)) as pool:
        res = pool.map(_job, jobs)
    results = {f"nucleon=V^{r['m']},atom2={r['atom2']}": r for r in res}

    # C2: V^3 ratios and reading-3 verdicts reproduce h2_ruled_electron
    old = json.loads((HERE.parent / "h2_ruled_electron" / "h2-ruled-electron.witness.json").read_text())["results"]
    worst, matched = mp.mpf(0), 0
    for tag, r in results.items():
        orows = {row["K"]: row for row in old[tag]["rows"]}
        for row in r["rows"]:
            if row["K"] in orows:
                o = orows[row["K"]]
                worst = max(worst, abs(mp.mpf(o["ratio"]) - mp.mpf(row["ratio"])))
                matched += int(o["reading3_every_level"] == row["reading3_every_level"])
    check("C2_V3_rows_reproduce_h2_ruled_electron", matched == 8 and worst < mp.mpf("1e-18"),
          f"{matched}/8 verdicts match, max ratio diff {mp.nstr(worst, 5)}")

    summary, h_all = {}, True
    for tag, r in results.items():
        passing = [row for row in r["rows"] if row["reading3_every_level"]]
        ranked = sorted(passing, key=lambda row: mp.mpf(row["ratio"]))
        if ranked:
            mn = mp.mpf(ranked[0]["ratio"])
            argmin = [row["K"] for row in ranked if abs(mp.mpf(row["ratio"]) - mn) < TOL]
        else:
            argmin = []
        h = bool(argmin) and all(k in ("V4.V4.V4", "V5.V5.V5") for k in argmin)
        h_all &= h
        summary[tag] = {"n_candidates": len(r["rows"]), "n_pass": len(passing),
                        "argmin_ratio": argmin, "min_ratio": ranked[0]["ratio"] if ranked else None,
                        "ranked_passing": [(row["K"], row["ratio"]) for row in ranked],
                        "failing": [row["K"] for row in r["rows"] if not row["reading3_every_level"]],
                        "H_holds": h}
        log(f"{tag}: pass {len(passing)}/{len(r['rows'])}, argmin {argmin}, H={h}")
        for k, v in summary[tag]["ranked_passing"]:
            log(f"    {k:28s} {v}")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-bond-min-action", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (issue #8879): H2 bond by minimum Markov trace (prop:confinement-lp read on words) "
                       "over gamma-gamma V4/V5 words of length 1..6 that are atom-preserving and not split; "
                       "reading 3 at every level 1..12, convention D, proton pin. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "hypothesis_H_all_cells": h_all,
        "candidates": [".".join(t) for t in cands],
        "summary": summary,
        "results": results,
    })
    log(f"witness: {out}")
    log(f"H holds in all cells: {h_all}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
