#!/usr/bin/env python3
"""u1_neutral_cut_probe.py — D2: the phi01-psi01 cut from central U(1) colour neutrality.

Pre-registered in bean qou-99qc (PRE-REGISTRATION 2026-11-21 14:05Z). Lean first: QOU/Photon/U1NeutralCut.lean
(Neutral predicate, neutral => writhe 0, the twelve-term table). This probe:
  R-term: solves "every non-neutral braid-word term of the unreduced gamma(phi)gamma(psi) has coefficient 0".
  R-word: FrobeniusSelected (stage 7R engine) over arms A and B restricted to U(1)-neutral words, <= 10 crossings.
Nothing is compared with measurement.
-- Ref: [leitner2026] bean qou-99qc; QEDHigherOrderCovariance section U
"""
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gg_twist_reading3"))
import gg_ruled_photon_grammar_probe as g  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def neutral(w):
    """Mirror of Lean `Neutral`: every component self-writhe and pairwise crossing count is 0."""
    pos = [0, 1, 2]
    for gi, _ in w:
        pos[gi], pos[gi + 1] = pos[gi + 1], pos[gi]
    step = lambda x: pos.index(x)  # noqa: E731
    comp = {x: min(x, step(x), step(step(x))) for x in range(3)}
    cnt, pos = {}, [0, 1, 2]
    for gi, e in w:
        k = tuple(sorted((comp[pos[gi]], comp[pos[gi + 1]])))
        cnt[k] = cnt.get(k, 0) + e
        pos[gi], pos[gi + 1] = pos[gi + 1], pos[gi]
    return all(v == 0 for v in cnt.values())


def r_term():
    p0, p1, p01, s0, s1, s01 = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01")
    # term -> coefficient, braid words free-reduced (V s1 = s0)
    terms = {"s0": p0 + s0 + p01 * s1, "s1": p1 + s1, "V": p01 + s01, "s0.s0": p0 * s0, "s0.s1": p0 * s1,
             "s1.s0": p1 * s0, "s1.s1": p1 * s1, "s0.V": p0 * s01, "V.s0": p01 * s0, "s1.V": p1 * s01,
             "V.V": p01 * s01}
    words = {"s0": [g.P0], "s1": [g.P1], "V": g.Vw, "s0.s0": [g.P0, g.P0], "s0.s1": [g.P0, g.P1],
             "s1.s0": [g.P1, g.P0], "s1.s1": [g.P1, g.P1], "s0.V": [g.P0] + g.Vw, "V.s0": g.Vw + [g.P0],
             "s1.V": [g.P1] + g.Vw, "V.V": g.Vw + g.Vw}
    neut = {k: neutral(g.reduce(tuple(w))) for k, w in words.items()}
    eqs = [c for k, c in terms.items() if not neut[k]]
    sols = sp.solve(eqs, [p0, p1, p01, s0, s1, s01], dict=True)
    forced = all(all(s.get(v, v) == 0 for v in (p0, p1, s0, s1)) for s in sols)
    return {"neutral_terms": neut, "conditions": [str(e) for e in eqs],
            "solutions": [{str(k): str(v) for k, v in s.items()} for s in sols], "sigma_weights_forced_zero": forced}


def r_word(label, letters):
    ws = [w for w in g.reach(letters) if neutral(w)]
    rows = []
    for w in sorted(ws, key=lambda x: (len(x), x)):
        lc, verdict, feas = g.classify(w)
        rows.append({"braid": g.show(w), "crossings": len(w), "components": g.components(w), "feasible": feas,
                     "signs": {f"{m}:{mu}": s for (m, mu), s in verdict.items()}})
    feas = [r for r in rows if r["feasible"]]
    cmin = min((r["crossings"] for r in feas), default=None)
    sel = [r for r in feas if r["crossings"] == cmin]
    print(f"[R-word {label}] neutral {len(rows)}, feasible {len(feas)}, min {cmin}, selected {[r['braid'] for r in sel]}")
    return {"neutral_words": len(rows), "feasible": len(feas), "min_cost": cmin, "selected": sel,
            "neutral_by_cost": {c: sum(1 for r in rows if r["crossings"] == c) for c in range(1, g.MAXC + 1)},
            "feasible_list": [r["braid"] for r in feas]}


def main():
    rt = r_term()
    print("R-term:", json.dumps(rt["solutions"]), "forced:", rt["sigma_weights_forced_zero"])
    lean_table = {"s0": False, "s1": False, "V": True, "s0.s0": False, "s0.s1": False, "s1.s0": False,
                  "s1.s1": False, "s0.V": False, "V.s0": False, "s1.V": False, "V.V": True}
    lean_ok = all(rt["neutral_terms"][k] == v for k, v in lean_table.items() if k != "V.s1")
    out = {"R_term": rt, "lean_table_agrees": lean_ok,
           "R_word_arm_A": r_word("A", g.ARMS["A"]), "R_word_arm_B": r_word("B", g.ARMS["B"])}
    wb = WitnessBuilder("u1-neutral-cut-d2", engine="mpmath", output_dir=HERE)
    wb.add_assertion("lean_table_agrees", computed=str(int(lean_ok)), expected="1", source="QOU/Photon/U1NeutralCut.lean table")
    wb.add_assertion("rterm_forces_sigma_weights_zero", computed=str(int(rt["sigma_weights_forced_zero"])),
                     expected=str(int(rt["sigma_weights_forced_zero"])), source="pre-registration 2026-11-21 14:05Z (recorded, not predicted)")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "reading 3 at the proton pin, convention D",
             "description": "PROBE D2: phi01-psi01 cut from central U(1) colour neutrality; R-term solve and "
                            "R-word FrobeniusSelected over neutral words, arms A/B, <= 10 crossings.", **out})


if __name__ == "__main__":
    main()
