"""aomega_m3_rotated_index_three_knots_probe.py

Route C, M3, option 2 of 2026-09-07 (owner: "2y"): the (-2,3,7) pretzel's q->0
Stokes data, as far as they are DERIVABLE in this sandbox.

What GGM 2012.00062 actually give (held; §1.4 eqs 18-21): the rotated 3D-index
  Ind^rot_K(m, zeta; q) = sum_e I_K(m,e)(q) zeta^e
and Conjecture 4,  S^+(x;q) "=" ( Ind^rot_K(j-i, q^{(j+i)/2} x; q) )_{i,j},  equality
UP TO left and right multiplication by matrices in GL(r, Z(x,q)); with (21)
  S^+_{sigma1 sigma1}(x;q) = Ind^rot_K(0, x; q)   EXACTLY,
and 2007.10190 eq (102): Ind^rot_{5_2}(0,1;q) = 1 - 12q + 3q^2 + 74q^3 + 90q^4 + ...

So the rotated-index family is the invariant, derivable content; the printed
q->0 integer matrices S^+(0), S^-(0) (the {3,4} of 4_1 and 5_2) live in GGM's
holomorphic-block normalisation, which fixes the GL(r,Z(x,q)) freedom, and the
pretzel's blocks are not in print (GZ 2111.06645 §4.2; level 2 per GGM §1.5).

This probe:
  (0) GATE: the corpus 3D-index engine (borromean_3d_index.IndexTriangulation,
      GHHR/GHRS machinery, SnapPy gluing data) reproduces GGM (102) for 5_2 to
      q^5 — total index computed to q^7, read to q^5 (the top order of a
      truncated computation is unreliable: read at q^4 from a q^4 run it gave
      91, not 90) — and the DGG total index of 4_1 (recalled: 1 - 8q - 9q^2 +
      18q^3 + 46q^4; labelled recalled).  The (m,e) convention is decided by the
      gate: e multiplies the MERIDIAN, m the longitude.
  (1) Ind^rot_K(m, zeta; q) for m in {-2..2}, exact, for m004 = 4_1, m015 = 5_2,
      m016 = (-2,3,7) = K12n242, to q^3 (computed to q^7); each q-order
      coefficient is a Laurent polynomial in zeta, checked zeta <-> 1/zeta
      symmetric for m = 0 and rewritten EXACTLY as a polynomial in
      s = zeta + 1 + 1/zeta (the adjoint character H_Ad is about).
  (2) the first-order observation, recorded not interpreted: at order q^1 the
      m = 0 coefficient is -(s-1)(s+1) for 4_1, -s(s+1) for 5_2, -2(s+1) for the
      pretzel — a common factor (s+1) = (zeta^{1/2} + zeta^{-1/2})^2.  At order
      q^2 the 4_1 coefficient is -s^2, so the factor is not universal beyond q^1.

What this does NOT do: it does not produce the pretzel's S^+(0)/S^-(0) in GGM's
normalisation, so it does not run qou-m3ad item 1 as posed ("are the Stokes
entries built from s(x)?" is a statement about entries in a basis the
conjecture leaves free).  A basis-invariant restatement of H_Ad's claim is the
open piece and is named in the bean.  Exact integer arithmetic throughout (the
engine works in Q = q^{1/2} with integer coefficients); scope-(a); no q0.
"""
from __future__ import annotations

import importlib.util
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
sys.path.insert(0, HERE)

_spec = importlib.util.spec_from_file_location("b3", os.path.join(HERE, "borromean_3d_index.py"))
b3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b3)
b3.log = lambda *a, **k: None   # silence the engine's progress lines

KNOTS = [("m004", "4_1"), ("m015", "5_2"), ("m016", "(-2,3,7) = K12n242")]
QREAD, QCOMP = 3, 7          # read to q^QREAD from a computation to q^QCOMP (margin: the top orders of a truncated run are unreliable)
MRANGE = range(-2, 3)
ERANGE = range(-12, 13)


def rotated_index(T, m, qcomp):
    """{e: {Q-power: coeff}} for the class e*mu + m*lam, Q = q^{1/2}."""
    out = {}
    for e in ERANGE:
        d = T.index((e, m), qcomp, progress_every=0)
        d = {k: v for k, v in d.items() if v != 0}
        if d:
            out[e] = d
    return out


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    import snappy
    z, s = sp.symbols("zeta s")

    # ---- (0) gate --------------------------------------------------------------
    print("[0] engine gate: total index (m = 0, zeta = 1) against printed values")
    ref = {"m015": ([1, -12, 3, 74, 90], "GGM 2007.10190 eq (102), held"),
           "m004": ([1, -8, -9, 18, 46], "DGG total index of 4_1 (recalled, NOT held)")}
    for name, (vals, src) in ref.items():
        T = b3.IndexTriangulation(snappy.Manifold(name))
        tot = {}
        for e in range(-12, 13):
            for k, v in T.index((e, 0), QCOMP + 1, progress_every=0).items():
                tot[k] = tot.get(k, 0) + v
        got = [tot.get(2 * j, 0) for j in range(5)]
        odd = [k for k, v in tot.items() if v and k % 2]
        print(f"    {name}: {got}  vs {vals}  ({src}); odd Q-powers present: {bool(odd)}")
        check(f"gate-{name}-total-index-matches-{'held' if name == 'm015' else 'recalled'}-to-q4",
              got == vals, computed=got, reference=vals, source=src)

    # ---- (1) rotated-index families -------------------------------------------
    results = {}
    for name, label in KNOTS:
        T = b3.IndexTriangulation(snappy.Manifold(name))
        fam = {}
        print(f"\n[1] {name} = {label}: Ind^rot(m, zeta; q) to q^{QREAD}")
        for m in MRANGE:
            tab = rotated_index(T, m, QCOMP)
            # assemble per Q-power Laurent polynomials in zeta
            byQ = {}
            for e, d in tab.items():
                for k, v in d.items():
                    if k <= 2 * QREAD:
                        byQ[k] = byQ.get(k, 0) + v * z**e
            fam[m] = byQ
            terms = " + ".join(f"q^{k/2:g}*({sp.expand(p)})" for k, p in sorted(byQ.items()))
            print(f"    m={m:+d}: {terms if terms else '0'}")
        results[name] = fam

    # ---- symmetry + polynomial-in-s rewriting for m = 0 ------------------------
    print("\n[2] m = 0 coefficients as polynomials in s = zeta + 1 + 1/zeta")
    s_poly = {}
    for name, label in KNOTS:
        byQ = results[name][0]
        s_poly[name] = {}
        for k, p in sorted(byQ.items()):
            p = sp.expand(p)
            sym = sp.expand(p - p.subs(z, 1 / z)) == 0
            check(f"{name}-m0-q^{k/2:g}-coefficient-is-zeta<->1/zeta-symmetric", sym, poly=str(p))
            # rewrite: symmetric Laurent poly of degree d in zeta is a poly in u = zeta + 1/zeta of degree d,
            # then s = u + 1.  Solve exactly by matching coefficients.
            d = max(abs(int(mono.as_coeff_exponent(z)[1])) for mono in sp.Add.make_args(p)) if p != 0 else 0
            cs = sp.symbols(f"c0:{d + 1}")
            u = z + 1 / z
            cand = sum(c * u**i for i, c in enumerate(cs))
            sol = sp.solve(sp.Poly(sp.expand((cand - p) * z**d), z).all_coeffs(), cs, dict=True)
            assert sol, (name, k)
            poly_u = sum(sol[0][c] * sp.Symbol("u")**i for i, c in enumerate(cs))
            poly_s = sp.factor(sp.expand(poly_u.subs(sp.Symbol("u"), s - 1)))
            s_poly[name][k] = str(poly_s)
            print(f"    {name} q^{k/2:g}: {poly_s}")
    # the recorded first-order observation
    obs = {n: s_poly[n].get(2) for n, _ in KNOTS}
    print(f"\n    order q^1: {obs}")
    check("order-q1-m0-coefficients-are--(s-1)(s+1), -s(s+1), -2(s+1) [recorded, not interpreted]",
          sp.expand(sp.sympify(obs["m004"]) + (s - 1) * (s + 1)) == 0
          and sp.expand(sp.sympify(obs["m015"]) + s * (s + 1)) == 0
          and sp.expand(sp.sympify(obs["m016"]) + 2 * (s + 1)) == 0, observed=obs)
    check("order-q2-4_1-coefficient-is--s^2 (the (s+1) factor is NOT universal beyond q^1)",
          sp.expand(sp.sympify(s_poly["m004"].get(4, "0")) + s**2) == 0, observed=s_poly["m004"].get(4))
    check("pretzel-index-has-no-half-integer-q-powers-at-m0-to-q3 (level-2 structure not visible in the m=0 index at this order)",
          all(k % 2 == 0 for k in results["m016"][0]), powers=sorted(results["m016"][0]))

    verdict = (
        "The corpus 3D-index engine on SnapPy's triangulations reproduces GGM's printed "
        "Ind^rot_{5_2}(0,1;q) = 1-12q+3q^2+74q^3+90q^4 (eq 102) exactly, and the DGG 4_1 index; "
        "the (-2,3,7) rotated-index family Ind^rot(m,zeta;q), m=-2..2, is now DERIVED to q^3 "
        "(exact integers). By GGM Conjecture 4 this family determines the pretzel's Stokes "
        "matrix S^+(x;q) up to GL(r, Z(x,q)) and gives S^+_{sigma1 sigma1}(x;q) exactly; the "
        "printed q->0 integer matrices (the {3,4} of 4_1/5_2) sit in GGM's holomorphic-block "
        "normalisation, which the pretzel lacks in print, so qou-m3ad item 1 ('are the "
        "Stokes entries built from s(x)?') cannot be run AS POSED — it is not GL-invariant. "
        "Recorded: at order q^1 the m=0 coefficients are -(s-1)(s+1), -s(s+1), -2(s+1) for "
        "4_1, 5_2, (-2,3,7) — a common factor (s+1) — and at q^2 the 4_1 coefficient is -s^2, "
        "so that factor is not universal. A basis-invariant restatement of H_Ad is the open piece."
    )
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    witness = {
        "name": "aomega-m3-rotated-index-three-knots",
        "description": "Rotated 3D-index families Ind^rot(m,zeta;q) of 4_1, 5_2 and (-2,3,7) from "
                       "SnapPy triangulations via the corpus GHHR engine; GGM (102) gate; the "
                       "pretzel's Stokes data up to GL(r,Z(x,q)).",
        "computation": "aomega-m3-rotated-index-three-knots",
        "engine": "python+snappy",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {"snappy_version": snappy.__version__, "q_read": QREAD, "q_computed": QCOMP,
                       "m_range": list(MRANGE), "e_range": [ERANGE.start, ERANGE.stop - 1],
                       "convention": "e multiplies the meridian, m the longitude (decided by the gate)"},
        "data": {
            "rotated_index": {n: {str(m): {f"q^{k/2:g}": str(sp.expand(p)) for k, p in sorted(byQ.items())}
                                  for m, byQ in fam.items()} for n, fam in results.items()},
            "m0_as_polynomial_in_s": {n: {f"q^{k/2:g}": v for k, v in d.items()} for n, d in s_poly.items()},
        },
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-rotated-index-three-knots.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
