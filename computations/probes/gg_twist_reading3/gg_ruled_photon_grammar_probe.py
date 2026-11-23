#!/usr/bin/env python3
"""gg_ruled_photon_grammar_probe.py — stage 7R: the gamma-gamma grammar on the RULED photon.

Pre-registered in bean qou-99qc (PRE-REGISTRATION 2026-11-21 12:20Z) before this file was written.
Ruled photon (#8583): gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 V, V = s0 s1^-1. Stage 7 (68ef4b266,
unmerged) used the superseded fourth term s0 s1; this redoes it with the same selection rule.
Arms: V (products of V only, the current Lean grammar), A (primary: the nine bilinear terms of
gamma(phi)gamma(psi)), B (comparison, not selectable: all twelve non-identity terms).
Selection is FrobeniusSelected (qou-ales): reading 3, chi >= 0 on every level with y > 0, convention D,
proton pin; words free-reduced, <= MAXC crossings; cost = crossing count; all minima reported.
Near-zero (< 1e-30) characters are decided exactly with symbolic q. Nothing is compared with measurement.
-- Ref: [leitner2026] bean qou-99qc; bean qou-ales
"""
from __future__ import annotations

import sys
import time
from collections import Counter
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402
sys.path.insert(0, str(HERE))
import exact_h3_level_chars_signed as ex  # noqa: E402

base = ga.base
from qou_substrate.witness import WitnessBuilder  # noqa: E402

MAXC = 10
FLOOR = mp.mpf(10) ** -30
P0, P1, N1 = (0, 1), (1, 1), (1, -1)


def reduce(w):
    out = []
    for c in w:
        if out and out[-1][0] == c[0] and out[-1][1] == -c[1]:
            out.pop()
        else:
            out.append(c)
    return tuple(out)


Vw = [P0, N1]
TERMS_BARE = {"s0": [P0], "s1": [P1], "V": Vw}
BILINEAR = {
    "s0.s0": [P0, P0], "s0.s1": [P0, P1], "s1.s0": [P1, P0], "s1.s1": [P1, P1],
    "s0.V": [P0] + Vw, "V.s0": Vw + [P0], "s1.V": [P1] + Vw, "V.s1": Vw + [P1], "V.V": Vw + Vw,
}
ARMS = {"V": {"V": Vw}, "A": BILINEAR, "B": dict(BILINEAR, **TERMS_BARE)}


def writhe(w):
    return sum(e for _, e in w)


def components(w):
    p = [0, 1, 2]
    for g, _ in w:
        p[g], p[g + 1] = p[g + 1], p[g]
    seen, c = set(), 0
    for i in range(3):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def chars(w):
    word = [(mp.mpf(1), mp.mpf(0) if e > 0 else -base.H, g) for g, e in w]
    return ga.level_chars(base.diag_of(word, 3), 3, 1)


def classify(w):
    lc = chars(w)
    exact, verdict = None, {}
    for k, v in lc.items():
        if v > FLOOR:
            verdict[k] = "+"
        elif v < -FLOOR:
            verdict[k] = "-"
        else:
            if exact is None:
                exact = ex.level_chars(list(w))
            verdict[k] = "0" if exact[k] == 0 else "undecided"
    return lc, verdict, all(s in "+0" for s in verdict.values())


def check_exact_engine():
    import sympy as sp
    q0 = sp.Float(mp.nstr(base.Q, 40), 40)
    worst = mp.mpf(0)
    for w in [(P0,), (N1,), (P0, N1), (P0, N1) * 3, ((0, -1), P1, P0), (P1, P1, (0, -1), P1)]:
        e, n = ex.level_chars(list(w)), chars(w)
        for k, v in n.items():
            worst = max(worst, abs(mp.mpf(str(sp.N(e[k].subs(ex.q, q0), 40))) - v))
    return worst


def reach(letters):
    seen = {}
    frontier = []
    for n, g in letters.items():
        r = reduce(g)
        if r and len(r) <= MAXC and r not in seen:
            seen[r] = n
            frontier.append(r)
    while frontier:
        nxt = []
        for w in frontier:
            for n, g in letters.items():
                r = reduce(w + tuple(g))
                if r and len(r) <= MAXC and r not in seen:
                    seen[r] = seen[w] + "." + n
                    nxt.append(r)
        frontier = nxt
    return seen


def show(w):
    return "".join(f"s{g}" + ("" if e > 0 else "^-1") for g, e in w)


def run(label, letters):
    t0 = time.time()
    ws = reach(letters)
    rows, nz, nu = [], 0, 0
    for i, w in enumerate(sorted(ws, key=lambda x: (len(x), x))):
        lc, verdict, feas = classify(w)
        nz += any(x == "0" for x in verdict.values())
        nu += any(x == "undecided" for x in verdict.values())
        if feas:
            rows.append({"braid": show(w), "crossings": len(w), "letters": ws[w], "writhe": writhe(w),
                         "components": components(w),
                         "chars": {f"{m}:{mu}": mp.nstr(v, 20) for (m, mu), v in lc.items()},
                         "signs": {f"{m}:{mu}": s for (m, mu), s in verdict.items()}})
        if i % 5000 == 0:
            print(f"  [{label}] {i}/{len(ws)} {time.time()-t0:.0f}s", flush=True)
    cmin = min((r["crossings"] for r in rows), default=None)
    sel = [r for r in rows if r["crossings"] == cmin]
    bor = reduce(tuple(Vw * 3))
    bor_row = next((r for r in rows if r["braid"] == show(bor)), None)
    print(f"[{label}] braids {len(ws)}, feasible {len(rows)}, min cost {cmin}, selected {len(sel)}, "
          f"exact zeros {nz}, undecided {nu}, {time.time()-t0:.0f}s")
    for r in sel:
        print("   ", r["braid"], r["letters"], "writhe", r["writhe"], "comp", r["components"], r["chars"])
    print("    beta_Bor feasible:", bor_row is not None)
    return {"letters": {k: show(reduce(g)) for k, g in letters.items()},
            "letter_writhes": {k: writhe(reduce(g)) for k, g in letters.items()},
            "candidates": len(ws), "feasible": len(rows), "exact_zero_words": nz, "undecided_words": nu,
            "min_cost": cmin, "selected": sel, "beta_Bor_reached": bor in ws,
            "beta_Bor_feasible": bor_row is not None,
            "writhe_of_candidates": dict(sorted(Counter(writhe(w) for w in ws).items())),
            "writhe_of_feasible": dict(sorted(Counter(r["writhe"] for r in rows).items())),
            "feasible_by_cost": {c: sum(1 for r in rows if r["crossings"] == c) for c in range(1, MAXC + 1)}}


def main() -> int:
    worst = check_exact_engine()
    print("exact vs mpmath engine, max |diff| at q0:", mp.nstr(worst, 5))
    out = {"exact_engine_max_diff": mp.nstr(worst, 10), "max_crossings": MAXC}
    for label, letters in ARMS.items():
        out[f"arm_{label}"] = run(label, letters)
    wb = WitnessBuilder("gg-ruled-photon-grammar-stage7r", engine="mpmath", output_dir=HERE)
    wb.add_assertion("exact_engine_agrees", computed="1" if worst < mp.mpf(10) ** -30 else "0",
                     expected="1", source="exact_h3_level_chars_signed vs h2_gg_atom_probe.level_chars")
    wb.add_assertion("no_undecided", computed=str(sum(out[f"arm_{a}"]["undecided_words"] for a in ARMS)),
                     expected="0", source="pre-registration qou-99qc 2026-11-21 12:20Z")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "reading 3 at the proton pin, convention D",
             "description": "PROBE stage 7R: gamma-gamma grammar on the ruled photon (fourth term s0 s1^-1); "
                            "FrobeniusSelected over arms V / A (bilinear terms) / B (all terms), cost = "
                            "crossing count of the free-reduced word, all ties reported.",
             **out})
    return 0


if __name__ == "__main__":
    sys.exit(main())
