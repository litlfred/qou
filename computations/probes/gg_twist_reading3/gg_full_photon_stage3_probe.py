#!/usr/bin/env python3
"""gg_full_photon_stage3_probe.py — stage 3: the full-photon γγ word set on 3 strands is B3; reading 3 alone selects.

Pre-registered in preregistration.md (commit 3df55fdc6d7) before this file. Every freely reduced word over
{s0, s0^-1, s1, s1^-1} of length 1..7. mpmath 40 dps, convention D, proton pin. Nothing fitted.
-- Ref: [leitner2026] gamma-gamma-generates-particles; bean qou-a1hh
"""
from __future__ import annotations
import itertools, sys, time
from pathlib import Path
import mpmath as mp
mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

b = ga.base
ONE, ZERO, H = mp.mpf(1), mp.mpf(0), b.H
LET = {"a": (0, 1), "A": (0, -1), "b": (1, 1), "B": (1, -1)}
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}


def hecke(w):
    return [(ONE, ZERO if s > 0 else -H, g) for g, s in (LET[c] for c in w)]


def components(w):
    p = [0, 1, 2]
    for c in w:
        g = LET[c][0]
        p[g], p[g + 1] = p[g + 1], p[g]
    seen, n = set(), 0
    for i in range(3):
        if i not in seen:
            n += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return n


def words(maxlen):
    for L in range(1, maxlen + 1):
        for t in itertools.product("aAbB", repeat=L):
            if all(t[i + 1] != INV[t[i]] for i in range(L - 1)):
                yield "".join(t)


FLIP = {"a": "b", "A": "B", "b": "a", "B": "A"}
_PASS = {}


def passes(w):
    if w not in _PASS:
        lc = ga.level_chars(b.diag_of(hecke(w), 3), 3, 1)
        _PASS[w] = min(lc.values()) >= -ga.TOL
    return _PASS[w]


def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == INV[c]:
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def orbit(w):
    """Cyclic rotations, conjugation by each letter, and the s0<->s1 flip (a closure invariance set)."""
    base = {w[i:] + w[:i] for i in range(len(w))}
    base |= {reduce_word(x + v + INV[x]) for v in list(base) for x in "aAbB"}
    base |= {"".join(FLIP[c] for c in v) for v in list(base)}
    return {v for v in base if v}


def main() -> int:
    t0 = time.time()
    rows, k = [], 0
    for w in words(7):
        lc = ga.level_chars(b.diag_of(hecke(w), 3), 3, 1)
        mn = min(lc.values())
        _PASS[w] = bool(mn >= -ga.TOL)
        rows.append({"word": w, "pass": bool(mn >= -ga.TOL), "components": components(w),
                     "writhe": sum(LET[c][1] for c in w), "min_level_char": mp.nstr(mn, 15)})
        k += 1
        if k % 500 == 0:
            print(f"[{time.time()-t0:7.1f}s] {k} words", flush=True)
    for r in rows:
        r["pass_conj_invariant"] = all(passes(v) for v in orbit(r["word"]))
    inv_viol = [r["word"] for r in rows if r["pass_conj_invariant"] != (r["components"] == 3)]
    passing = [r for r in rows if r["pass"]]
    pure = [r for r in rows if r["components"] == 3]
    viol = [r for r in rows if r["pass"] != (r["components"] == 3)]
    summ = {"words": len(rows), "pass": len(passing), "pure": len(pure),
            "pass_iff_pure": not viol, "violations": viol[:50], "n_violations": len(viol),
            "passing_knots": [r for r in passing if r["components"] == 1],
            "passing_2comp": [r for r in passing if r["components"] == 2][:50],
            "conj_invariant_pass_iff_pure": not inv_viol, "conj_invariant_violations": inv_viol[:50],
            "n_conj_invariant_violations": len(inv_viol)}
    print({k: v for k, v in summ.items() if k not in ("violations", "passing_2comp", "passing_knots")}, flush=True)
    print("violations:", [(r["word"], r["components"], r["pass"], r["min_level_char"]) for r in viol[:30]])
    wb = WitnessBuilder("gg-full-photon-stage3", engine="mpmath", output_dir=HERE)
    wb.add_assertion("no_knot_passes", computed=str(len(summ["passing_knots"])), expected="0",
                     source="reading 3 levels 1..3")
    wb.add_assertion("conj_invariant_pass_iff_pure", computed=str(len(inv_viol)), expected="0",
                     source="orbit = rotations, letter conjugations, s0<->s1 flip")
    out = wb.save({"q0Anchor": "proton", "q0AnchorReason": "q0 via cf.Q (proton pin)",
                   "description": "Stage 3: all freely reduced 3-strand words length 1..7 (full-photon γγ set = B3) under reading 3.",
                   "weight_family": "markov_y_lambda_convention_D", "summary": summ, "rows": rows})
    print("witness", out, f"{time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
