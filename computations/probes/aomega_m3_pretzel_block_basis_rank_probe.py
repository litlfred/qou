"""aomega_m3_pretzel_block_basis_rank_probe.py

Route C, M3, Part 15 (bean qou-x3iv): why the six residue families cannot be the
pretzel's holomorphic blocks — a rank statement, measured.

Parts 12b/14 established that the six u-deformed residue families factorise the
pretzel's state integral exactly (validated to 1e-19, every pole checked) and yet
their fusion is not the sigma_1 sigma_1 index, for any branch or monomial
reweighting.  Part 13 established, from held text, that the index is the weight-1
component of an eps-expansion at collided triple poles (Garoufalidis-Zagier
Obs 3.9), whose twelve q^{1/2}-series span weight spaces of dimensions 1, 4, 1.

This probe asks the structural question those two leave open: ARE the six
families a block basis at all?  The test is their behaviour as the meridian
deformation is switched off, u -> 0 (X = x^{1/2} -> 1), which is the limit in
which GZ's poles collide.

Measured, exactly (each family's q-side series, coefficients in Q(X), evaluated
at X -> 1 term by term):

  F1            1 - 2q + 3q^3 + ...
  F2            1 - 2q + 3q^3 + ...       <- identical to F1
  F3(0,0)       1 - 2q + 3q^3 + ...       <- identical to F1
  F3(0,1)       1 + 2q + 4q^2 + 7q^3 + ...
  F3(1,0)      -q^{3/4} - q^{7/4} + 2q^{9/4} - q^{11/4} + ...
  F3(1,1)      -q^{3/4} - q^{7/4} - 2q^{9/4} - q^{11/4} + ...

So THREE of the six — precisely the two unit factors and the even-even parity
class, i.e. exactly the three whose poles collide into GZ's triple pole — share
one limit.  The family has rank 4, not 6, at u = 0.

That is the obstruction, stated structurally: a set of six functions that
degenerates to four cannot be a basis of the six-dimensional block space GZ's
weight decomposition (1 + 4 + 1) requires, so no pairing of them — diagonal,
off-diagonal, reweighted or branch-twisted — can be the index.  What the index
needs at the collision is the eps-EXPANSION of the colliding triple (their
value, first and second derivatives: GZ's H_0, H_1, H_2), and the meridian
deformation u is not a regularisation of that expansion: it separates the poles
without separating the limits.

This does not weaken Parts 12b/14.  The families do factorise the integral, and
that is a statement about the integral, not about the index; the two objects are
related by GGM (19), which pairs BLOCKS.  The negative is scope (a) for
"the residue families as a block basis", with the invariant exhibited: a rank
drop from 6 to 4.

Gates / tests
  G1  F1, F2 and F3(0,0) have the same u -> 0 limit, to the computed order
  G2  the other three limits are pairwise distinct and distinct from that one
  G3  so the u -> 0 rank of the six q-side families is 4, not 6
  G4  the q^0 coefficient of the Part 12b bilinear at X -> 1 is 7/8, whereas the
      derived index at zeta = 1 has q^0 coefficient 1 — the failure survives the
      limit, so it is not a zeta-identification artefact
  G5  GZ's twelve DO span 6 (their H_0..H_5 q-sides are pairwise independent),
      so the shortfall is in our basis, not in the target
Exact sympy/Fraction throughout; no mpmath, no q0, no float64.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))
sys.path.insert(0, HERE)

import aomega_m3_pretzel_residue_blocks_probe as P12      # noqa: E402
import aomega_m3_pretzel_gz_blocks_index_probe as P13      # noqa: E402

Xs = P12.Xs
# Truncation matters for BOTH claims here, so it is raised deliberately and stated.
# The degeneracy G1 asserts is an identity claim: at q^3 the three colliding families agree on only
# four coefficients, which is not enough to call them equal.  P12's series length is a module global,
# so it is raised here and every limit below is computed at the longer length.
QORDER = 6
P12.QMAX_UNITS = 4 * (QORDER + 2) + 3


def limit_series(spec):
    """The family's q-side series with X -> 1, as {q-exponent: rational}."""
    ser = P12.P_ser(spec, False)
    out = {}
    for k, v in sorted(ser.d.items()):
        e = Fraction(k, 4)
        if e > QORDER:
            continue
        vv = sp.cancel(v)
        lim = sp.limit(vv, Xs, 1) if vv.has(Xs) else sp.nsimplify(vv)
        lim = sp.nsimplify(lim)
        if lim != 0:
            out[e] = lim
    return out


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    fams = {"F1": P12.spec_p_F1, "F2": P12.spec_p_F2}
    for e_ in (0, 1):
        for d_ in (0, 1):
            fams[f"F3({e_},{d_})"] = P12.spec_p_F3(e_, d_)

    print("the six q-side families as the meridian deformation is switched off (X -> 1):")
    lims = {}
    for name, spec in fams.items():
        lims[name] = limit_series(spec)
        print(f"   {name:9s} " + "  ".join(f"{c}q^{e}" for e, c in lims[name].items()))

    collide = ["F1", "F2", "F3(0,0)"]
    same = all(lims[c] == lims["F1"] for c in collide)
    check("G1-the two unit factors and the even-even parity class share ONE u -> 0 limit (the three whose poles collide "
          "into GZ's triple pole)", same, limit={str(k): str(v) for k, v in lims["F1"].items()})

    others = ["F3(0,1)", "F3(1,0)", "F3(1,1)"]
    distinct = all(lims[a] != lims[b] for i, a in enumerate(others) for b in others[i + 1:]) \
        and all(lims[o] != lims["F1"] for o in others)
    check("G2-the other three limits are pairwise distinct, and distinct from the collided one", distinct)

    rank = len({tuple(sorted((str(k), str(v)) for k, v in d.items())) for d in lims.values()})
    check("G3-the u -> 0 rank of the six families is 4, not 6 — they cannot be a basis of the six-dimensional block "
          "space GZ's weight decomposition (1 + 4 + 1) requires", rank == 4, rank=rank, of=len(lims))

    fam12b = [(P12.spec_p_F1, P12.spec_p_F1, 1), (P12.spec_p_F2, P12.spec_p_F2, 1)]
    for e_ in (0, 1):
        for d_ in (0, 1):
            fam12b.append((P12.spec_p_F3(e_, d_), P12.spec_p_F3(d_, e_), sp.Rational(1, 2) * (-1) ** (e_ * d_)))
    B = P12.as_q_laurent(P12.bilinear(fam12b))
    q0 = sp.cancel(B.get(Fraction(0), 0))
    q0_at_1 = sp.nsimplify(sp.limit(q0, Xs, 1)) if q0.has(Xs) else sp.nsimplify(q0)
    wit = json.load(open(os.path.join(HERE, "aomega-m3-rotated-index-three-knots.witness.json")))
    zeta = sp.Symbol("zeta")
    idx_q0 = sp.sympify(wit["data"]["rotated_index"]["m016"]["0"]["q^0"], locals={"zeta": zeta}).subs(zeta, 1)
    print(f"\n   Part 12b bilinear q^0 = {sp.factor(q0)};  at X -> 1: {q0_at_1};  derived index q^0 at zeta = 1: {idx_q0}")
    check("G4-the Part 12b bilinear's q^0 tends to 7/8 as u -> 0, against the index's 1 — the failure survives the limit, "
          "so it is not an artefact of the zeta identification", q0_at_1 == sp.Rational(7, 8) and idx_q0 == 1,
          bilinear_q0=str(sp.factor(q0)), at_X_1=str(q0_at_1), index_q0=str(idx_q0))

    H = P13.gz_series()          # P13 carries its own truncation (q^8), ample for a rank-6 test
    Hq = {k: {e: c for e, c in H[k].q_dict().items() if e <= 7} for k in ["0+", "1+", "2+", "3+", "4+", "5+"]}
    exps = sorted({e for d in Hq.values() for e in d})
    M = sp.Matrix([[sp.Rational(Hq[k].get(e, 0)) for e in exps] for k in Hq])
    check("G5-GZ's six q-side blocks H_0..H_5 ARE independent (rank 6) once enough orders are carried, so the shortfall "
          "is in our basis, not the target", M.rank() == 6, gz_rank=int(M.rank()), columns=len(exps))

    verdict = (f"MEASURED, structural: the six residue families have u -> 0 rank {rank}, not 6. The two unit factors and "
               "the even-even parity class — exactly the three whose poles collide into GZ's triple pole — share one "
               "limit (1 - 2q + 3q^3 + ...), while GZ's own six blocks are independent (rank 6). So no pairing of the "
               "residue families, diagonal or otherwise, can be the sigma_1 sigma_1 index: they are not a block basis. "
               "The q^0 failure survives the limit (7/8 against the index's 1), which rules out a zeta-identification "
               "artefact. What the index needs at the collision is the eps-EXPANSION of the colliding triple (value, "
               "first and second derivatives = GZ's H_0, H_1, H_2); the meridian deformation separates the poles "
               "WITHOUT separating the limits, so u is not a regularisation of that expansion. Scope (a) for 'the "
               "residue families as a block basis', with the invariant exhibited (a rank drop 6 -> 4). Parts 12b/14 are "
               "unaffected: they factorise the INTEGRAL, which is a different object, related to the index only through "
               "GGM (19) — which pairs blocks.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pretzel-block-basis-rank",
         "description": "The u -> 0 rank of the pretzel's six residue families is 4, not 6: the three colliding families share one "
                        "limit, so they cannot be a holomorphic-block basis and no pairing of them is the index.",
         "computation": "aomega-m3-pretzel-block-basis-rank", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
         "parameters": {"QORDER": QORDER, "orientation": "SnapPy's (Part 11)",
                        "families": "Part 12b's validated six (2 unit + 4 parity classes)"},
         "data": {"limits": {k: {str(e): str(c) for e, c in v.items()} for k, v in lims.items()},
                  "rank_at_u_to_0": rank, "bilinear_q0_at_X_1": str(q0_at_1), "index_q0_at_zeta_1": str(idx_q0),
                  "gz_block_rank": int(M.rank())},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-block-basis-rank.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
