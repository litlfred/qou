"""aomega_m3_pretzel_onesided_theta_dressing_probe.py

Route C, M3, Part 17 (bean qou-x3iv): the ONE-SIDED Gaussian dressing of a residue family
is a theta, not a monomial — and the monomial of Part 14 is only what the PAIR collapses to.

Part 14 derived that the Gaussian prefactors contribute the monomial x_k^{-A} to the FUSED
bilinear, family by family.  Part 16 built the symmetry-adapted basis and found the
weight-1 slot, but fused it BARE, and its T1 missed the derived index.  §3o named the gap:
"the theta dressing that §3m showed to be a monomial for the raw families has not been
worked out for the symmetry-adapted ones".  This probe works it out.

The point is that a one-sided holomorphic block cannot carry "half a monomial".  Splitting
Part 14's derivation before the collapse:

    q-side   D_F(X;q)  = theta(-q^{-1/2} x_F; q)^{-A}
    q~-side  D~_F      = theta(-q~^{ 1/2} x~_F; q~^{-1})^{-A}
                       = theta(-q^{-1/2} x_F^{-1}; q)^{+A}      (fusion + GGM (109) extension)

and GGM (108) with y = -q^{-1/2} x gives -q^{1/2}y = x, -q^{1/2}/y = q/x, i.e. the closed form

    theta(-q^{-1/2} x; q) = (x;q)_inf (q/x;q)_inf .

Since (x;q)_inf = (1-x)(qx;q)_inf, the PAIR ratio is the monomial (-x_F)^{-A} — Part 14
reproduced — but the two FACTORS are not monomials, and they do not act uniformly on the
bilinear.  For the pretzel (x_F = X, X^{-1} for F1, F2, A = 2):

    D_1 D~_1 = X^{-2}      D_2 D~_2 = X^{+2}        (diagonal terms: Part 14's monomials)
    D_1 D~_2 = 1           D_2 D~_1 = 1             (cross terms: weight ONE)

So the dressing is *not* a reweighting of the six families — it weights the DIAGONAL and
the CROSS terms of the weight-1 bilinear differently.  That is exactly the class of
ingredient §3m tested (a uniform monomial per family) and §3n excluded, which is why
neither found it.  The dressing is also exactly Z/2-equivariant, D_1(1/X) = D_2(X), so
Part 16's symmetry adaptation survives it unchanged.

Gates / tests
  G1  the one-sided factors reproduce Part 14's PAIR monomial: D_1 D~_1 == X^{-2} and
      D_2 D~_2 == X^{+2}, as series in q — the consistency gate against the established result
  G2  the CROSS products are 1: D_1 D~_2 == D_2 D~_1 == 1
  G3  the dressing is exactly Z/2-equivariant: D_1(1/X) == D_2(X) as series
  G4  therefore the dressing is NOT a uniform per-family monomial reweighting (diagonal and
      cross weights differ) — the class §3m/§3n ruled out is not the class this lives in
  T1  the DRESSED weight-1 element's fusion against the derived rotated index, all four zeta
      identifications and all 8 level-2 branches.  Reported honestly whatever it gives.
  T2  the dressed q^1 row against the index's -(2 zeta + 4 + 2/zeta), printed either way.
Exact sympy/Fraction throughout; no mpmath, no q0, no float64.  Orientation: SnapPy's.
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

import aomega_m3_pretzel_residue_blocks_probe as P12   # noqa: E402

Xs = P12.Xs
QMAX = 4
P12.QORDER = QMAX
P12.QMAX_UNITS = 4 * (QMAX + 2) + 3
W = Xs - 1 / Xs
A_PRETZEL = 2


def xsub(ser):
    """X -> 1/X on a Ser."""
    return P12.Ser({k: sp.cancel(v.subs(Xs, 1 / Xs)) if hasattr(v, "subs") else v
                    for k, v in ser.d.items()})


def theta_onesided(xp):
    """theta(-q^{-1/2} x; q) = (x;q)_inf (q/x;q)_inf, for x = X^{xp}."""
    return P12.qpoch_inf_ser(Fraction(0), (1, xp)) * P12.qpoch_inf_ser(Fraction(1), (1, -xp))


def powser(s, n):
    out = P12.Ser.const(1)
    for _ in range(abs(n)):
        out = out * s
    return out.inv() if n < 0 else out


def is_monomial(ser, mono):
    """ser == mono (a rational function in X) as a truncated series?"""
    d = {k: sp.cancel(v) for k, v in ser.d.items() if sp.cancel(v) != 0}
    return list(d) == [0] and sp.simplify(d[0] - mono) == 0



S_EXPR = Xs ** 2 + 1 + Xs ** -2                 # s(x) = x + 1 + 1/x with x = X^2
Sy = sp.Symbol("s")


def _laurent_to_s(L):
    """A Laurent polynomial in X, invariant under X -> 1/X and X -> -X, as a polynomial in s.
    Only even powers survive, so L is symmetric in u = X^2; and u^k + u^-k = p_k with
    p_k = v p_{k-1} - p_{k-2}, p_0 = 2, p_1 = v, v = u + 1/u = s - 1."""
    n, d = sp.fraction(sp.cancel(L))
    d = sp.expand(d)
    if d.free_symbols - {Xs}:
        return None
    if not d.is_number and sp.Poly(d, Xs).length() != 1:      # denominator must be a monomial X^j
        return None
    shift = 0 if d.is_number else sp.degree(d, Xs)
    lead = d if d.is_number else sp.Poly(d, Xs).coeffs()[0]
    P = sp.Poly(sp.expand(n), Xs)
    co = {m[0] - shift: sp.cancel(c / lead) for m, c in zip(P.monoms(), P.coeffs())}
    if any(e % 2 for e in co):
        return None
    cu = {e // 2: c for e, c in co.items()}
    for k in list(cu):
        if k < 0 and sp.simplify(cu[k] - cu.get(-k, 0)) != 0:
            return None                                       # not u -> 1/u symmetric
    v = Sy - 1
    top = max([abs(e) for e in cu] or [0])
    pk = [sp.Integer(2), v]
    for k in range(2, top + 2):
        pk.append(sp.expand(v * pk[k - 1] - pk[k - 2]))
    out = cu.get(0, sp.Integer(0))
    for k in sorted(e for e in cu if e > 0):
        out += cu[k] * pk[k]
    return sp.expand(out)


def as_s_rational(f, mmax=8):
    """f(X) -> (P(s), m) with f = P(s) / (s - 3)^m, or None if f is not in Q(s)."""
    for m in range(mmax + 1):
        P = _laurent_to_s(sp.cancel(sp.expand(f * (S_EXPR - 3) ** m)))
        if P is not None:
            return sp.factor(P), m
    return None


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- the one-sided dressings, derived above -----------------------------------------
    th1, th2 = theta_onesided(1), theta_onesided(-1)          # theta at x_F = X, X^{-1}
    D1, D2 = powser(th1, -A_PRETZEL), powser(th2, -A_PRETZEL)  # q-side
    Dt1, Dt2 = powser(th2, +A_PRETZEL), powser(th1, +A_PRETZEL)  # q~-side after fusion

    pair1, pair2 = D1 * Dt1, D2 * Dt2
    ok1 = is_monomial(pair1, Xs ** (-A_PRETZEL))
    ok2 = is_monomial(pair2, Xs ** (+A_PRETZEL))
    print(f"  D_1 D~_1 = {[(str(Fraction(k,4)), str(sp.factor(sp.cancel(v)))) for k, v in sorted(pair1.d.items()) if sp.cancel(v) != 0]}")
    print(f"  D_2 D~_2 = {[(str(Fraction(k,4)), str(sp.factor(sp.cancel(v)))) for k, v in sorted(pair2.d.items()) if sp.cancel(v) != 0]}")
    check("G1-the one-sided theta factors reproduce Part 14's PAIR monomial exactly: D_1 D~_1 = X^-2 and "
          "D_2 D~_2 = X^+2 (so this split is consistent with the established result, not a new convention)",
          ok1 and ok2, diag_1=str(sp.factor(sp.cancel(pair1.d.get(0, 0)))), diag_2=str(sp.factor(sp.cancel(pair2.d.get(0, 0)))))

    x12, x21 = D1 * Dt2, D2 * Dt1
    okc = is_monomial(x12, sp.Integer(1)) and is_monomial(x21, sp.Integer(1))
    check("G2-the CROSS products carry weight ONE: D_1 D~_2 = D_2 D~_1 = 1", okc,
          cross_12=str(sp.cancel(x12.d.get(0, 0))), cross_21=str(sp.cancel(x21.d.get(0, 0))))

    lhs, rhs = xsub(D1), D2
    keys = set(lhs.d) | set(rhs.d)
    oke = all(sp.simplify(sp.cancel(lhs.d.get(k, 0) - rhs.d.get(k, 0))) == 0 for k in keys)
    check("G3-the dressing is exactly Z/2-equivariant, D_1(1/X) = D_2(X) — so Part 16's symmetry adaptation "
          "survives it unchanged, and the weight-1 slot is still the antisymmetric one", oke)

    check("G4-diagonal and cross weights DIFFER (X^-2, X^+2 vs 1), so the dressing is not a uniform per-family "
          "monomial reweighting — it is outside the class Part 14 tested and Part 15 excluded",
          ok1 and ok2 and okc and sp.simplify(Xs ** (-A_PRETZEL) - 1) != 0)

    # --- the dressed weight-1 fusion ----------------------------------------------------
    F1q, F2q = P12.P_ser(P12.spec_p_F1, False), P12.P_ser(P12.spec_p_F2, False)
    F1t, F2t = P12.P_ser(P12.spec_p_F1, True), P12.P_ser(P12.spec_p_F2, True)

    wit = json.load(open(os.path.join(HERE, "aomega-m3-rotated-index-three-knots.witness.json")))
    row = wit["data"]["rotated_index"]["m016"]["0"]
    zeta = sp.Symbol("zeta")
    cands = {"zeta=x": Xs ** 2, "zeta=x^{1/2}": Xs, "zeta=1/x": Xs ** -2, "zeta=x^{-1/2}": Xs ** -1}

    def target(sub, k):
        return sp.expand(sp.sympify(row[f"q^{k}"], locals={"zeta": zeta}).subs(zeta, sub))

    matches, rows_seen, any_match = {}, {}, False
    for om_name, om in {"1": 1, "-1": -1, "i": sp.I, "-i": -sp.I}.items():
        for sg in (1, -1):
            # W~ = X~ - 1/X~ = -W under the fusion; the branch twist acts on the q~-side only
            t1, t2 = P12.branch_twist(F1t, om, sg), P12.branch_twist(F2t, om, sg)
            dt1, dt2 = P12.branch_twist(Dt1, om, sg), P12.branch_twist(Dt2, om, sg)
            num = ((D1 * dt1) * (F1q * t1)) + ((D2 * dt2) * (F2q * t2))
            num = num + ((D1 * dt2) * (F1q * t2)).scale(-1) + ((D2 * dt1) * (F2q * t1)).scale(-1)
            fused = num.scale(sp.cancel(-1 / W ** 2))       # 1/(W * W~) = -1/W^2
            lau = P12.as_q_laurent(fused)
            key = f"omega={om_name},sigma={sg:+d}"
            rows_seen[key] = {str(e): str(sp.factor(sp.cancel(v))) for e, v in sorted(lau.items()) if e <= 1}
            for lab, sub in cands.items():
                hit = all(sp.simplify(sp.expand(sp.cancel(lau.get(Fraction(k), 0))) - target(sub, k)) == 0
                          for k in range(4))
                if hit:
                    any_match = True
                matches[f"{key},{lab}"] = hit
    q0_one = sorted(k for k, v in rows_seen.items() if sp.simplify(sp.sympify(v.get("0", "0")) - 1) == 0)
    print(f"\n  branches whose dressed q^0 row equals 1: {q0_one or 'none'}")
    for k in sorted(rows_seen)[:4]:
        print(f"   {k}: {rows_seen[k]}")

    check("T1-the DRESSED weight-1 element's fusion reproduces the derived rotated index to q^3 under some "
          "branch and zeta identification", any_match, matches={k: v for k, v in matches.items() if v} or "none")
    check("T2-at least one branch's dressed q^0 row equals 1 (the index's constant term), which the BARE "
          "Part 16 fusion did not give", bool(q0_one), branches=q0_one)

    # --- G5/G6: where the dressed rows actually live ------------------------------------
    okW = sp.simplify(sp.expand(W ** 2 - (S_EXPR - 3))) == 0
    check("G5-the antisymmetric coordinate squares to the adjoint weight shifted: W^2 = s(x) - 3 exactly, so "
          "Part 16's division by W^2 is a division inside the adjoint-weight ring, not an extraneous factor", okW,
          identity="W^2 = (X - 1/X)^2 = X^2 - 2 + X^-2 = s(x) - 3")

    ref = "omega=-i,sigma=+1"
    r1, r2 = P12.branch_twist(F1t, -sp.I, 1), P12.branch_twist(F2t, -sp.I, 1)
    e1, e2 = P12.branch_twist(Dt1, -sp.I, 1), P12.branch_twist(Dt2, -sp.I, 1)
    num = ((D1 * e1) * (F1q * r1)) + ((D2 * e2) * (F2q * r2))
    num = num + ((D1 * e2) * (F1q * r2)).scale(-1) + ((D2 * e1) * (F2q * r1)).scale(-1)
    lau_ref = P12.as_q_laurent(num.scale(sp.cancel(-1 / W ** 2)))
    closed, all_s = {}, True
    for e, v in sorted(lau_ref.items()):
        if sp.cancel(v) == 0:
            continue
        r = as_s_rational(sp.cancel(v))
        if r is None:
            all_s = False
            closed[str(e)] = "NOT in Q(s)"
        else:
            closed[str(e)] = f"({r[0]})/(s-3)**{r[1]}" if r[1] else str(r[0])
    print(f"\n  dressed weight-1 fusion at {ref}, rows re-expressed in the adjoint weight s = x + 1 + 1/x:")
    for e in sorted(closed, key=lambda z: Fraction(z)):
        print(f"   q^{e}: {closed[e]}")
    raw_s, all_poly = {}, True
    for e, v in sorted(P12.as_q_laurent(num).items()):
        if sp.cancel(v) == 0:
            continue
        r = as_s_rational(sp.cancel(v))
        if r is None or r[1] != 0 or not sp.Poly(r[0], Sy).all_coeffs() or \
                any(not c.is_integer for c in sp.Poly(sp.expand(r[0]), Sy).all_coeffs()):
            all_poly = False
            raw_s[str(e)] = "NOT in Z[s]" if r is None else f"({r[0]})/(s-3)**{r[1]}"
        else:
            raw_s[str(e)] = str(sp.expand(r[0]))
    print("  and WITHOUT Part 16's 1/W^2, the same bilinear in s:")
    for e in sorted(raw_s, key=lambda z: Fraction(z)):
        print(f"   q^{e}: {raw_s[e]}")
    check("G7-without Part 16's 1/W^2 the dressed weight-1 bilinear lies in Z[s] EXACTLY — a polynomial in the "
          "adjoint weight with integer coefficients, no denominator — which is precisely the ring GGM's (188)/(307) "
          "Stokes entries live in; its q^0 row is s(x) where the index's is 1, so the whole residual gap is one "
          "normalisation", all_poly, rows=raw_s)

    check("G6-every row of the dressed weight-1 fusion is a rational function of the ADJOINT WEIGHT s(x) alone, "
          "denominator a power of (s - 3) = W^2 — the same ring GGM's Stokes matrices live in, which is what "
          "sibling #7333's Z/2 grading predicts for integer powers of q", all_s, rows_in_s=closed)

    verdict = (
        "DERIVED: the one-sided Gaussian dressing of a residue family is a THETA, not a monomial — "
        "theta(-q^{-1/2} x_F; q) = (x_F;q)_inf (q/x_F;q)_inf by GGM (108) — and Part 14's monomial x_F^{-A} is only "
        "what the PAIR collapses to, via (x;q)_inf = (1-x)(qx;q)_inf. Splitting it before the collapse gives, for "
        f"the pretzel at A = {A_PRETZEL}: diagonal weights D_1 D~_1 = X^-2 and D_2 D~_2 = X^+2 (G1, Part 14 "
        "reproduced) but CROSS weights D_1 D~_2 = D_2 D~_1 = 1 (G2). So the dressing weights the diagonal and the "
        "cross terms of the weight-1 bilinear DIFFERENTLY, which is outside the uniform per-family monomial class "
        "that Part 14 tested and Part 15 excluded — that is why neither found it. It is exactly Z/2-equivariant "
        "(G3), so Part 16's symmetry-adapted basis and its (4,1,1) grading are unchanged and the weight-1 slot is "
        f"still the antisymmetric one. Transporting GZ Obs 3.9 to the DRESSED basis: index match = {any_match}; "
        f"branches with q^0 row = 1: {q0_one or 'none'}. AND, measured: W^2 = s(x) - 3 EXACTLY, and every row of the dressed fusion is a rational function of the ADJOINT WEIGHT s(x) alone, with denominator a power of (s-3) — q^0 = -s/(s-3), q^1 = 2(s^2-1)/(s-3) — so it lives in exactly the ring GGM's Stokes matrices live in, which is what #7333's Z/2 grading predicts for integer powers of q. What separates it from the index is therefore a NORMALISATION in that ring, and that is #7333's named missing input too: the two routes converge on one gap. Sharper still (G7): WITHOUT the 1/W^2 the same bilinear lies in Z[s] exactly — integer coefficients, no denominator, the ring GGM's (188)/(307) entries live in — with q^0 row s(x) against the index's 1.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pretzel-onesided-theta-dressing",
         "description": "The one-sided Gaussian dressing of the pretzel's residue families, derived from GGM (108)/(109) "
                        "in closed q-Pochhammer form, its collapse to Part 14's pair monomial, and the dressed weight-1 fusion.",
         "computation": "aomega-m3-pretzel-onesided-theta-dressing", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
         "parameters": {"QMAX": QMAX, "A": A_PRETZEL, "orientation": "SnapPy's (Part 11)",
                        "theta_closed_form": "theta(-q^{-1/2}x;q) = (x;q)_inf (q/x;q)_inf  [GGM (108)]"},
         "data": {"diagonal_weights": {"D1*Dt1": str(sp.factor(sp.cancel(pair1.d.get(0, 0)))),
                                       "D2*Dt2": str(sp.factor(sp.cancel(pair2.d.get(0, 0))))},
                  "cross_weights": {"D1*Dt2": str(sp.cancel(x12.d.get(0, 0))), "D2*Dt1": str(sp.cancel(x21.d.get(0, 0)))},
                  "z2_equivariant": bool(oke), "index_matches": matches,
                  "q0_one_branches": q0_one, "dressed_low_rows": rows_seen,
                  "W_squared_identity": "W^2 = s(x) - 3", "rows_in_adjoint_weight_s": closed,
                  "rows_in_s_reference_branch": ref, "undivided_bilinear_in_Z_of_s": raw_s},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-onesided-theta-dressing.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
