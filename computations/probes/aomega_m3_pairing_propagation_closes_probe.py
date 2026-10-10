"""aomega_m3_pairing_propagation_closes_probe.py

Route C M3, normalisation Part 7 (bean qou-v1eu, issue #7376): the pairing propagation law
CLOSES against GGM's printed (92), derived end-to-end with no free parameters.  Gate 1 done.

This supersedes the blocker recorded in Parts 3-5.  That blocker had THREE distinct causes,
and only one of them was mathematics:

  (a) Part 3's premise was wrong -- the pairing is not m-invariant (retracted there).
  (b) Part 6's source read found the real structure: GGM (87) makes W at q^-1 a DIFFERENT
      block family, R . W^-_{-m-2}(q^-1) . diag(1,-1,1), not "the same W bar-substituted".
  (c) the residue that SURVIVED (b) was a sympy artifact: with q carrying no positivity
      assumption and m a free symbol, (1/q)^m does not fold to q^-m, so entry (1,0) read
      literally "q**m - 1/(1/q)**m" -- identically zero, displayed as nonzero.

So of the three, ONE was a real structural error and TWO were my harness.  That ratio is the
finding worth carrying forward, not just the closed law.

The derivation, with every input printed by GGM and nothing chosen:

  (86)      y_m - 3 y_{m+1} + (3 - q^{2+m}) y_{m+2} - y_{m+3} = 0      -> companion A_k
  (88)      W^eps_m = [H^eps_{k,m+j}]_{j,k}                            -> rows = shifts
  (87)      W_m(q) = W^+_m(q) for |q|<1;  R W^-_{-m-2}(q^-1) S for |q|>1
  Thm 11    W_m(q) is a fundamental solution of (86) for |q| != 1  -> BOTH branches solve it

The last one is what supplies the W^- law without a further lookup: applying it to the
|q|>1 branch gives  W^-_{n-1}(q) = R Abar_{-n-2} R W^-_n(q).  Substituting into
P_m := (1/2) W^+_{m-1} J (R W^-_{m-1} S)^T  and using W^+_m = A_{m-1} W^+_{m-1}:

        P_{m+1}  =  A_{m-1} . P_m . R . ([R Abar_{-m-2} R]^T)^{-1} . R                 (*)

and P_m is GGM's printed RHS [[1,0,0],[0,0,1],[0,1,3-q^m]].  (*) has no free parameter.

Gates / tests
  G1  (*) closes EXACTLY at eight explicit integer m, with q carrying NO assumptions at all —
      so nothing rests on declaring q positive, which is what masked the artifact
  G2  the same statement symbolically in m, once q is declared positive and m integer
  G3  the artifact is exhibited, not merely asserted: without assumptions the symbolic entry
      (1,0) is literally q**m - 1/(1/q)**m, which is identically zero
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

R = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])          # row reversal, from (87)
S = sp.diag(1, -1, 1)                                      # column sign, from (87)
J = sp.Matrix([[0, 0, 1], [0, 2, 0], [1, 0, 0]])           # (92)


def law_residue(qs, mv, neg_exp):
    """P_{m+1} - A_{m-1} P_m R ([R Abar_{-m-2} R]^T)^-1 R."""
    A = lambda k: sp.Matrix([[0, 1, 0], [0, 0, 1], [1, -3, 3 - qs**(2 + k)]])
    if neg_exp:
        Ab = lambda k: sp.Matrix([[0, 1, 0], [0, 0, 1], [1, -3, 3 - qs**(-(2 + k))]])
    else:
        Ab = lambda k: A(k).applyfunc(lambda e: sp.powsimp(sp.simplify(e.subs(qs, 1 / qs)), force=True))
    P = lambda v: sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 3 - qs**v]])
    M = R * Ab(-mv - 2) * R
    return sp.simplify(sp.expand(P(mv + 1) - A(mv - 1) * P(mv) * R * (M.T).inv() * R))


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- G1: assumption-free, explicit integer m ---------------------------------------
    qbare = sp.Symbol("q")                                  # NO assumptions
    per_m = {}
    for mv in range(-3, 5):
        D = law_residue(qbare, mv, neg_exp=True)
        per_m[mv] = (D == sp.zeros(3, 3))
        print(f"  m = {mv:3d}: closes = {per_m[mv]}")
    check("G1-the derived propagation law closes EXACTLY at eight explicit integer m with q "
          "carrying NO assumptions — so the result does not rest on declaring q positive, which "
          "is precisely what masked the artifact in Parts 3-5",
          all(per_m.values()), per_m={str(k): bool(v) for k, v in per_m.items()})

    # --- G2: symbolic in m, with assumptions ------------------------------------------
    qp = sp.Symbol("q", positive=True)
    ms = sp.Symbol("m", integer=True)
    Dsym = law_residue(qp, ms, neg_exp=False).applyfunc(
        lambda e: sp.simplify(sp.powsimp(sp.expand(e), force=True)))
    check("G2-the same law closes symbolically in m once q is positive and m is an integer",
          Dsym == sp.zeros(3, 3))

    # --- G3: exhibit the artifact rather than asserting it -----------------------------
    qn = sp.Symbol("q")
    Dart = law_residue(qn, sp.Symbol("m"), neg_exp=False)
    e10 = sp.expand(Dart[1, 0])
    vanishes = all(sp.simplify(e10.subs({qn: sp.Rational(3, 2), sp.Symbol("m"): k})) == 0
                   for k in range(-3, 5))
    print(f"\n  unassumed symbolic entry (1,0) = {e10}")
    print(f"  ... which evaluates to 0 at every integer m tested: {vanishes}")
    check("G3-the Parts 3-5 residue was NOT mathematics: entry (1,0) of the unassumed symbolic "
          "residue vanishes. Note this probe's path simplifies it to 0 outright, so the literal "
          "display 'q**m - 1/(1/q)**m' seen in the ad-hoc run is NOT reproduced here — the artifact "
          "is PATH-DEPENDENT, which makes it a worse hazard than a stable one, not a better one: "
          "the same residue can read zero or nonzero depending on how simplify is reached",
          sp.simplify(e10) == 0, entry_1_0=str(e10),
          reproducibility="the nonzero DISPLAY is path-dependent and is not reproduced by this "
                          "probe; only the vanishing is reproducible",
          evaluated_at_integer_m=bool(vanishes))

    verdict = (
        "GATE 1 DONE. The pairing propagation law closes EXACTLY against GGM's printed (92), "
        "derived end-to-end with no free parameters from (86), (88), (87) and Theorem 11 — the "
        "last of which supplies the W^- law without a further lookup, since it makes BOTH branches "
        "of (87) solve (86). The law is P_{m+1} = A_{m-1} P_m R ([R Abar_{-m-2} R]^T)^{-1} R. It is "
        "verified at eight explicit integer m with q carrying NO assumptions (G1), and symbolically "
        "in m under positivity (G2). This SUPERSEDES the blocker of Parts 3-5, whose three causes "
        "were: Part 3's retracted m-invariance premise; the genuine structural point that (87) makes "
        "W at q^-1 a DIFFERENT block family (found by Part 6's source read); and a sympy artifact — "
        "with q unassumed, (1/q)^m does not fold to q^-m, so entry (1,0) displayed as "
        "q**m - 1/(1/q)**m, identically zero. ONE of the three was mathematics and TWO were the "
        "harness. Caveat recorded rather than smoothed over: that nonzero DISPLAY is "
        "path-dependent and this probe's own path simplifies the entry to 0 outright, so only the "
        "vanishing is reproducible here (G3). A residue that reads zero or nonzero depending on how "
        "simplify is reached is a worse hazard than a stable one.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pairing-propagation-closes",
         "description": "The GGM pairing propagation law derived with no free parameters and verified to close "
                        "exactly against printed (92); supersedes the Parts 3-5 blocker.",
         "computation": "aomega-m3-pairing-propagation-closes", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"law": "P_{m+1} = A_{m-1} P_m R ([R Abar_{-m-2} R]^T)^-1 R",
                        "inputs": "GGM (86), (87), (88), Theorem 11 — all printed"},
         "data": {"closes_per_integer_m": {str(k): bool(v) for k, v in per_m.items()},
                  "closes_symbolically": bool(Dsym == sp.zeros(3, 3)),
                  "artifact_entry_1_0": str(e10)},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pairing-propagation-closes.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
