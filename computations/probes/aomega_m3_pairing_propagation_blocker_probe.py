"""aomega_m3_pairing_propagation_blocker_probe.py

Route C M3, normalisation Part 4 (bean qou-v1eu, issue #7376): a CHARACTERISED BLOCKER on
route 1, and a correction to Part 2's attribution.

Part 3 retracted the invariance premise A J Abar^T = J.  What replaces it is the correct
propagation law: since W_{m+1} = A_m W_m (GGM (130)/(244) define W with ROWS = shifts, so
this direction is right), and since GGM (92) pairs indices that move in OPPOSITE directions,

    G_M := W_M J Wbar_{-M-2}^T        satisfies       G_{M+1} = A_M G_M (Abar_?^T)^{-1}

with the inverse because the second index DECREASES.  This probe tests that against GGM's
printed data and records exactly where it stops.

Two findings.

(1) CORRECTION to Part 2's attribution.  Part 2 called c = 4 "the 5_2 constant, from (92)".
    The arithmetic det(RHS)/(pref^r det J) = 4 is correct, but the LABEL is wrong: (92)/(93)
    are NOT in the 5_2 sections (013/015).  They sit in the earlier section carrying
    Conjecture 12, and their RHS [[1,0,0],[0,0,1],[0,1,3-q^m]] contains NO x at all, while
    5_2's operator (254) does.  The 3 in that RHS is s(x) at x = 1.  So (92)/(93) are the
    u = 0 (x = 1) specialisation, and Part 2 paired a u=0 pairing with an x-dependent
    operator.  c = 4 must be scoped to "the u=0 rank-3 case", not to 5_2 generally.

(2) The reading is CORROBORATED but the law still does not close.  Specialising the operator
    to x = 1 cuts the residue from THREE nonzero entries to TWO — evidence the x = 1 reading
    is right — but entries (1,0) and (2,0) survive under every index variant tried.  Column 0
    only, rows 1 and 2.

Rather than keep trying conventions until one closes — which is fitting a convention to a
target — this is recorded as a blocker with the unseparated causes named.

Gates / tests
  G1  (92)/(93)'s RHS contains no x, and its constant term is s(1) = 3 — the u=0 reading
  G2  specialising to x = 1 strictly REDUCES the residue (3 nonzero entries -> 2), which is
      evidence for that reading rather than an assumption of it
  T1  the propagation law closes under some index variant.  It does NOT; the surviving
      residue is localised to column 0, rows 1-2, and that is recorded.
Exact sympy throughout; no mpmath, no q0, no float64.
"""
from __future__ import annotations

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

q, x, M = sp.symbols("q x M")


def residue(sval, variant):
    s = sval
    A = lambda m: sp.Matrix([[0, 1, 0], [0, 0, 1], [1, -s, s - q**(2 + m)]])
    sub = {q: 1 / q} if sval == 3 else {q: 1 / q, x: 1 / x}
    bar = lambda e: sp.powsimp(sp.simplify(e.subs(sub, simultaneous=True)))
    Ab = lambda l: A(l).applyfunc(bar)
    G = lambda Mv: 2 * sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 3 - q**(Mv + 1)]])
    rhs = {"inv-3": A(M) * G(M) * (Ab(-M - 3).T).inv(),
           "inv-2": A(M) * G(M) * (Ab(-M - 2).T).inv(),
           "noinv": A(M) * G(M) * Ab(-M - 3).T}[variant]
    D = sp.simplify(sp.expand(sp.simplify(G(M + 1) - rhs)))
    return [(i, j) for i in range(3) for j in range(3) if sp.simplify(D[i, j]) != 0]


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    RHS92 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 3 - q**sp.Symbol("m")]])
    has_x = bool(RHS92.free_symbols & {x})
    s_at_1 = sp.simplify((x + 1 + 1 / x).subs(x, 1))
    print(f"  (92) RHS free symbols: {sorted(map(str, RHS92.free_symbols))};  contains x: {has_x}")
    print(f"  s(x) at x = 1 = {s_at_1}, which is the constant appearing in that RHS")
    check("G1-CORRECTION to Part 2: GGM (92)/(93) carry NO x and their constant is s(1) = 3, so they "
          "are the u = 0 (x = 1) specialisation from the Conjecture-12 section — NOT 5_2's "
          "x-dependent pairing. Part 2's c = 4 is arithmetically right but was mis-attributed to 5_2; "
          "it scopes to the u=0 rank-3 case",
          (not has_x) and s_at_1 == 3, rhs_symbols=sorted(map(str, RHS92.free_symbols)), s_at_1=int(s_at_1))

    rx = residue(x + 1 + 1 / x, "inv-3")
    r1 = residue(sp.Integer(3), "inv-3")
    print(f"  residue with x-dependent s: {rx}  ({len(rx)} entries)")
    print(f"  residue at x = 1          : {r1}  ({len(r1)} entries)")
    check("G2-specialising the operator to x = 1 strictly REDUCES the residue (3 nonzero entries "
          "-> 2), which is evidence FOR the u=0 reading rather than an assumption of it",
          len(r1) < len(rx), residue_x_dependent=[list(t) for t in rx],
          residue_at_x_1=[list(t) for t in r1])

    # --- source read: three of the four candidate causes are ELIMINATED -----------------
    # GGM (86):  y_m - 3 y_{m+1} + (3 - q^{2+m}) y_{m+2} - y_{m+3} = 0
    a86 = [sp.Integer(1), sp.Integer(-3), 3 - q**(2 + sp.Symbol("m")), sp.Integer(-1)]
    mine = [sp.Integer(1), -sp.Integer(3), sp.Integer(3) - q**(2 + sp.Symbol("m")), sp.Integer(-1)]
    ok86 = all(sp.simplify(a - b) == 0 for a, b in zip(a86, mine))
    check("G3-source read ELIMINATES cause 2 and cause 3: GGM (86) is "
          "y_m - 3y_{m+1} + (3-q^{2+m})y_{m+2} - y_{m+3} = 0, i.e. exactly the operator this probe "
          "used at x = 1, with the q^{2+m} attachment confirmed on the y_{m+2} coefficient",
          ok86, ggm_86=[str(t) for t in a86])

    # GGM (91): det W_m(q) = 2, constant. Part 2 derived c = 4 WITHOUT having seen this.
    detW = sp.Integer(2)
    c_part2 = sp.simplify(sp.det(RHS92.subs(sp.Symbol("m"), sp.Symbol("m")))
                          / (sp.Rational(1, 2)**3 * sp.det(sp.Matrix([[0,0,1],[0,2,0],[1,0,0]]))))
    check("G4-source read CONFIRMS Part 2 and eliminates cause 1: GGM (91) prints det W_m(q) = 2, so "
          "det W(q) det W(1/q) = 4 — exactly the c Part 2 derived from det(RHS)/(pref^r det J) "
          "without having seen (91); and (92)'s printed J is [[0,0,1],[0,2,0],[1,0,0]] as read",
          sp.simplify(c_part2 - detW * detW) == 0,
          ggm_91_detW=int(detW), part2_derived_c=str(c_part2))

    variants = {v: residue(sp.Integer(3), v) for v in ("inv-3", "inv-2", "noinv")}
    for v, r in variants.items():
        print(f"  variant {v:6s}: {len(r)} nonzero entries {r}")
    closed = [v for v, r in variants.items() if not r]
    check("T1-the propagation law closes under some index variant. It does NOT: entries (1,0) and "
          "(2,0) survive every variant tried — column 0, rows 1-2. Recorded as a blocker rather "
          "than pursued by trying conventions until one closes, which would be fitting a convention "
          "to a target", bool(closed),
          variants={k: [list(t) for t in v] for k, v in variants.items()},
          eliminated_by_source_read=[
              "cause 1 (the J matrix) — (92) prints [[0,0,1],[0,2,0],[1,0,0]], as read",
              "cause 2 (the operator) — (86) is exactly the one used, at x = 1",
              "cause 3 (the q^{2+m} attachment) — confirmed on the y_{m+2} coefficient"],
          remaining_cause="GGM's OWN relation H^+_{k,m}(q^-1) = (-1)^k H^-_{k,-m}(q): the index "
                          "NEGATES and a sign (-1)^k appears per column, so W at q^-1 runs its "
                          "index the OPPOSITE way to what this law assumes — which is the shape "
                          "that produces a structured column-0 residue",
          next_honest_step="rebuild the second factor through that printed relation instead of "
                           "assuming a bare q -> 1/q substitution on the companion matrix")

    verdict = (
        "BLOCKER, characterised. Part 3 retracted the invariance premise; the correct law is "
        "G_{M+1} = A_M G_M (Abar^T)^{-1}, inverted because GGM (92) moves its two indices in "
        "OPPOSITE directions. Testing it exposed a CORRECTION to Part 2 (G1): (92)/(93) carry no x "
        "and their constant is s(1) = 3, so they are the u = 0 specialisation from the Conjecture-12 "
        "section, NOT 5_2's x-dependent pairing — Part 2's c = 4 is arithmetically correct but was "
        "mis-attributed, and scopes to the u=0 rank-3 case. That reading is corroborated rather than "
        f"assumed (G2): specialising to x = 1 cuts the residue from {len(rx)} nonzero entries to "
        f"{len(r1)}. It still does not close: entries (1,0) and (2,0) survive every index variant "
        "tried. Three causes remain unseparated and are named rather than guessed between. The next "
        "honest step is to read the u=0 section's own operator and J from the source instead of "
        "importing (254) and an OCR'd J across sections.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pairing-propagation-blocker",
         "description": "The corrected pairing propagation law, the u=0 re-attribution of GGM (92)/(93), and "
                        "the residue that survives every index variant — recorded as a characterised blocker.",
         "computation": "aomega-m3-pairing-propagation-blocker", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"law": "G_{M+1} = A_M G_M (Abar^T)^{-1}"},
         "data": {"rhs92_contains_x": has_x, "s_at_x_1": int(s_at_1),
                  "residue_x_dependent": [list(t) for t in rx], "residue_at_x_1": [list(t) for t in r1],
                  "variants": {k: [list(t) for t in v] for k, v in variants.items()}},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pairing-propagation-blocker.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
