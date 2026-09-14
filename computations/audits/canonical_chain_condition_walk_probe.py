#!/usr/bin/env python3
"""Walking the canonical derivation chain: where do CONDITIONS emerge?

WHAT THIS IS
------------
`docs/canonical-derivation-cheat-sheet.md` states the chain as eleven steps from
the substrate q_0 to MeV observables.  Each step is written as though its output
follows from its input.  This probe walks the chain asking a different question:
**at each step, what condition enters that the previous step does not force?**

It is a PARTIAL walk.  Steps 5, 6 and 10 are measured here; steps 1, 3, 4, 7, 8,
9 and 11 are NOT and are listed as not-yet-walked in the companion audit doc.
Step 2's condition is already documented in the cheat sheet itself (§2a, the
curvature 2-form is stipulated rather than computed) and is cited, not re-derived.

Companion: `docs/audits/2026-09-14-canonical-chain-condition-walk.md`
Bean: `qou-u96j`

THE THREE MEASURED FINDINGS
---------------------------

**C5 (step 5, Wedderburn + partitions) -- the sum is over TWO-ROW partitions.**
The step is stated as `H_n(q) = (+)_{lam |- n} M_{d_lam}` with
`tr_M = sum_lam y_lam chi^lam` -- over ALL partitions of n.  Measured against the
committed `y-lambda-at-q0.witness.json`, every y_lam with three or more rows is
EXACTLY 0, at n = 2, 3, 4 and 5.  The production family is
`y_lambda_su_n(n, q, 2)` and that trailing `2` is a row cap.  So the partition
sum the chain advertises is not the sum production computes, and the restriction
is a condition the step statement does not carry.  (AGENTS.md does say
"convention D = the two-row truncation" -- so this is known; what is missing is
that the CHAIN's own step statement does not say it.)

**C5b -- `alpha` is not an ad-hoc ratio; it is a Wenzl weight.**
`y_(3)` at n = 3 equals `(q^4+1)/(q^2+1)^2` exactly.  That is the same `alpha`
that the 2026-09-08 Q_beta ruling names as the augmentation-to-z_D factor and that
`QOU/Hecke/MarkovCrossingReversal.lean` found relating the two admissible cells of
the flavour split.  It was the trivial block's Wenzl weight all along.

**C5c -- the normalisation is DIMENSION-WEIGHTED, and a naive reading gets it
wrong.**  `sum_lam d_lam * y_lam = 1` exactly at every n (this is `tr_M(1) = 1`,
since `chi^lam(1) = d_lam`).  The unweighted `sum_lam y_lam` is 1 only at n = 2,
where every d_lam is 1, and then falls: 0.7527, 0.5666, 0.3804 at n = 3, 4, 5.
Recorded because the author's first reading of the witness was the unweighted one
and it produced a false "the y are not a measure" claim.

**C10 (step 10, confinement SDP) -- `n_target` carries three inequivalent
production meanings, and the cheat sheet states an objective the code does not
have.**  Section 4 below.

WHAT THIS PROBE DOES NOT CLAIM
------------------------------
Nothing here says any of these conditions is WRONG.  A condition that is correct
and simply unstated is still worth surfacing, because the chain is the document
agents reason from.  Scope (a) throughout: measured observations about what the
corpus contains, with no invariant excluding any of the readings.

Run: python3 computations/audits/canonical_chain_condition_walk_probe.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

import sympy as sp
from mpmath import mp

mp.dps = 60

ROOT = pathlib.Path(__file__).resolve().parents[2]
_q = sp.symbols("q", positive=True)
ALPHA = (_q**4 + 1) / (_q**2 + 1) ** 2

def dim_irrep(lam) -> int:
    """d_lambda for S_n by the hook-length formula.  Computed, not tabulated --
    the witness reaches n = 12 and a hand table would be both long and a place
    for a typo to hide."""
    lam = [p for p in lam if p]
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    return num // den


def main() -> int:
    ok = True

    wit = json.loads((ROOT / "computations" / "y-lambda-at-q0.witness.json").read_text())
    by_n = wit["data"]["by_n"]
    q0 = mp.mpf(wit["q0Value"])
    print(f"source: y-lambda-at-q0.witness.json   q0Anchor = {wit['q0Anchor']}   "
          f"q0 = {mp.nstr(q0, 20)}")

    print()
    print("1. STEP 5 -- THE PARTITION SUM IS OVER TWO-ROW PARTITIONS ONLY")
    print("   cheat sheet: 'H_n(q) = (+)_{lam |- n} M_{d_lam}; tr_M = sum y_lam chi^lam'")
    allgood = True
    for n_str in sorted(by_n, key=int):
        rows = by_n[n_str]
        nz = [tuple(r["partition"]) for r in rows if mp.mpf(r["y_at_q0_50dps"]) != 0]
        zr = [tuple(r["partition"]) for r in rows if mp.mpf(r["y_at_q0_50dps"]) == 0]
        good = all(len(p) <= 2 for p in nz) and all(len(p) >= 3 for p in zr)
        allgood &= good
        print(f"   n={n_str:>2s}: {len(nz):>2d} nonzero (max rows {max(len(p) for p in nz)}), "
              f"{len(zr):>3d} zero (min rows {min((len(p) for p in zr), default=0)})   "
              f"{'OK' if good else 'PATTERN BROKEN'}")
    ok &= allgood
    print(f"   -> at EVERY n from 2 to {max(by_n, key=int)}: every partition with >= 3 rows")
    print("      is EXACTLY zero and every nonzero one has <= 2 rows.  The production")
    print("      family is y_lambda_su_n(n, q, 2); the trailing 2 is a ROW CAP.")

    print()
    print("2. STEP 5b -- alpha IS THE TRIVIAL BLOCK'S WENZL WEIGHT, EXACTLY")
    y3 = mp.mpf([r for r in by_n["3"] if r["partition"] == [3]][0]["y_at_q0_50dps"])
    a0 = mp.mpf(str(sp.N(ALPHA.subs(_q, sp.Float(str(q0), 50)), 46)))
    agree = abs(y3 - a0) < mp.mpf("1e-45")
    ok &= agree
    print(f"   y_(3) at n=3            = {mp.nstr(y3, 30)}")
    print(f"   alpha = (q^4+1)/(q^2+1)^2 = {mp.nstr(a0, 30)}")
    print(f"   agree to 45 dps: {agree}   |diff| = {mp.nstr(abs(y3-a0), 6)}")
    print("   -> the alpha of the 2026-09-08 Q_beta ruling and of the flavour-split")
    print("      fork is not an ad-hoc ratio; it is this Wenzl weight.")

    print()
    print("3. STEP 5c -- THE NORMALISATION IS DIMENSION-WEIGHTED")
    for n_str in sorted(by_n, key=int):
        rows = by_n[n_str]
        s = sum(mp.mpf(r["y_at_q0_50dps"]) for r in rows)
        sd = sum(mp.mpf(r["y_at_q0_50dps"]) * dim_irrep(r["partition"]) for r in rows)
        unit = abs(sd - 1) < mp.mpf("1e-40")
        ok &= unit
        print(f"   n={n_str:>2s}: sum(y) = {mp.nstr(s, 18):>22s}    "
              f"sum(d*y) = {mp.nstr(sd, 18):>10s}  == 1 ? {unit}")
    print("   -> sum(d_lam y_lam) = 1 is tr_M(1) = 1, since chi^lam(1) = d_lam.")
    print("      The UNWEIGHTED sum is 1 only at n=2 (all d=1).  The author's first")
    print("      reading of this witness was the unweighted one and produced a false")
    print("      'the y are not a measure' claim; recorded so it is not repeated.")

    print()
    print("4. STEP 10 -- n_target HAS THREE INEQUIVALENT PRODUCTION MEANINGS")
    callers = {
        "computations/aK_via_lp_dual_hecke_basis.py":
            (r"n_target\s*=\s*tr_M_atom", "|tr_M(W_atom)| -- a Markov trace (REAL)"),
        "computations/pn_alpha_lp_dual.py":
            (r"target_net\s*=\s*float\(pn_vec\.sum\(\)\)",
             "sum of the p/n element vector (REAL, alpha-dependent)"),
        "computations/option_b_proton_mass_full_chain.py":
            (r"n_target=float\(n_gg\)", "count of gamma-gamma insertions (INTEGER)"),
    }
    found = 0
    for rel, (pat, gloss) in callers.items():
        txt = (ROOT / rel).read_text()
        m = re.search(pat, txt)
        hit = m is not None
        ok &= hit
        found += hit
        line = txt[:m.start()].count("\n") + 1 if m else "-"
        print(f"   {rel}:{line}")
        print(f"      {gloss}   {'FOUND' if hit else 'NOT FOUND'}")
    print(f"   -> {found}/3 confirmed at source.  The spec block")
    print("      content/.../appendix-mass-binding-algorithms/mba-step10-confinement-sdp.md")
    print("      declares 'Target net constraint n_target in Z_{>=0}' -- an INTEGER.")
    print("      Two of the three production callers pass a real.")

    print()
    print("5. STEP 10b -- THE CHEAT SHEET STATES AN OBJECTIVE THE CODE DOES NOT HAVE")
    cs = (ROOT / "docs" / "canonical-derivation-cheat-sheet.md").read_text()
    has_btgt = "B_\\mathrm{tgt}" in cs or "B_tgt" in cs
    spec = (ROOT / "content" / "quantum-observable-universe"
            / "appendix-mass-binding-algorithms" / "mba-step10-confinement-sdp.md").read_text()
    spec_has_btgt = "B_tgt" in spec or "B_\\mathrm{tgt}" in spec
    spec_has_sum = "Σ_i t_i x_i" in spec or "t_i x_i" in spec
    ok &= has_btgt and (not spec_has_btgt) and spec_has_sum
    print(f"   cheat sheet mentions a B_tgt in step 10          : {has_btgt}")
    print(f"   the authoritative algorithm block mentions B_tgt : {spec_has_btgt}")
    print(f"   the algorithm block's objective is  min sum t_i x_i : {spec_has_sum}")
    print("   -> the cheat sheet renders step 10 as 'min ||tr_M(T_w) E_0 - B_tgt||',")
    print("      i.e. minimising distance to a MEASURED BINDING.  The algorithm block")
    print("      and pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)")
    print("      have no such term.  The defect points the SAFE way -- the doc looks")
    print("      MORE fitted than the code -- but it is in the PRIMARY coordination")
    print("      document, and an agent reading it would conclude the chain fits AME.")

    print()
    print("VERDICT:", "PASS -- steps 5 and 10 each carry a condition the chain's own "
          "step statement does not state; alpha is identified as a Wenzl weight"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
