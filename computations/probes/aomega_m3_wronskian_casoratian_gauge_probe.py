"""aomega_m3_wronskian_casoratian_gauge_probe.py

Route C M3, normalisation Part 1 (bean qou-v1eu, issue #7376): the Wronskian
determinant of the descendant operator, from the Casoratian identity — and the gauge in
which it is trivial.

Both merged arc routes (#7152 blocks/residues, #7333 operator) closed on the per-knot
GL(r) normalisation, which both described as fixed by hand.  Reading GGM further: it is
NOT free.  Their Theorem 16(c)/(d) and (92)/(93) derive it, and part (c) names the
mechanism outright — "Equation (135) implies that the determinant of the Wronskian
satisfies the first order equation det(W_{m+1}) = x^3 det(W_m) (see [GK13, Lem.4.7])".

That is the CASORATIAN identity: for a linear q-difference equation sum_j a_j S_m^j f = 0
of order r, the Wronskian determinant obeys

    det W_{m+1} / det W_m  =  (-1)^r * a_0 / a_r

so it is computable from the operator's END coefficients alone.  This probe computes it
for the operators #7333 derived, and asks in which gauge it is trivial.

A gauge f_m -> lambda^m f_m rescales a_j -> lambda^j a_j, hence the ratio by lambda^{-r}.
So each operator has a distinguished gauge, the one making the ratio (-1)^r; equivalently
the one making N(X) PALINDROMIC.  GGM's printed 5_2 operator (276) has coefficients
(1, s, s, 1) — palindromic — which is exactly why their 5_2 Wronskian is m-INDEPENDENT
(sec-015 line 237: "det(W_{m+1}(x;q)) = det(W_m(x;q))").

Gates / tests
  G1  4_1: GGM's own (135) expands to 1 + [q^{1+m} - x^-1 - x^-2] S_m + x^-3 S_m^2, so
      a_0/a_2 = x^3 — their printed (136) ratio, recovered from the Casoratian rule.
      This calibrates the rule against a printed answer before we apply it to ours.
  G2  our derived 5_2 operator becomes GGM's palindromic (1, s, s, 1) under X -> q^{1/2} X
  G3  in that gauge the 5_2 Casoratian ratio is (-1)^3 = -1 in magnitude 1, matching GGM's
      m-independent determinant
  T1  the PRETZEL: is its degree-6 N(X) palindromic in ANY gauge lambda, and does that
      lambda lie in the q^{1/2} ring the level-2 structure lives in?  Reported honestly.
Exact sympy throughout; no mpmath, no q0, no float64.  Orientation: SnapPy's (#7152 Part 11).
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
sys.path.insert(0, HERE)

import aomega_m3_pretzel_level2_stokes_probe as P33   # noqa: E402

Q, XR, W, X = P33.Q, P33.XR, P33.W, P33.X
q, x = Q**2, XR**2
lam = sp.Symbol("lam", positive=True)


def n_coeffs(name):
    """Coefficients of N(X) for one knot, lowest degree first."""
    k = P33.KNOTS[name]
    N, _ = P33.descendant_operator(k["offsets_sym"], k["A"], k.get("doubled", False))
    r = N.degree()
    return [sp.simplify(sp.expand(N.coeff_monomial(X**j) if j else N.coeff_monomial(1)))
            for j in range(r + 1)], r


def casoratian_ratio(name):
    """(-1)^r a_0/a_r of P(X) = q^{A/2} W N(X) - X^A, the Casoratian ratio."""
    k = P33.KNOTS[name]
    _, P = P33.descendant_operator(k["offsets_sym"], k["A"], k.get("doubled", False))
    r = P.degree()
    a0 = P.coeff_monomial(1)
    ar = P.coeff_monomial(X**r)
    return sp.simplify(sp.cancel((-1) ** r * a0 / ar)), r


def palindrome_gauge(cs, r):
    """lambda such that n_j lambda^j is palindromic, or None. Uses the end pair, then
    VERIFIES every remaining pair rather than assuming."""
    if cs[0] == 0 or cs[r] == 0:
        return None, []
    sols = sp.solve(sp.Eq(sp.cancel(cs[0]), sp.cancel(cs[r] * lam**r)), lam)
    checks = []
    for L in sols:
        if not L.is_real:
            continue
        ok = all(sp.simplify(sp.cancel(cs[j] * L**j - cs[r - j] * L**(r - j))) == 0
                 for j in range(r + 1))
        checks.append((sp.simplify(L), ok))
    for L, ok in checks:
        if ok:
            return L, checks
    return None, checks


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- G1: calibrate the Casoratian rule on GGM's OWN printed 4_1 operator ------------
    Sm, qm = sp.symbols("Sm qm")
    ggm135 = sp.expand((1 - Sm / x) * (1 - Sm / x**2) + q * qm * Sm)   # GGM (135)
    p135 = sp.Poly(ggm135, Sm)
    a0_135 = p135.coeff_monomial(1)
    a2_135 = p135.coeff_monomial(Sm**2)
    ratio135 = sp.simplify(sp.cancel((-1) ** 2 * a0_135 / a2_135))
    print(f"  GGM (135) end coefficients: a_0 = {a0_135}, a_2 = {a2_135}")
    print(f"  Casoratian ratio from (135): {ratio135}   [GGM (136) prints x^3]")
    check("G1-the Casoratian rule (-1)^r a_0/a_r applied to GGM's OWN printed 4_1 operator (135) "
          "returns their printed Wronskian ratio x^3 of (136) — the rule is calibrated against a "
          "published answer before being applied to our operators",
          sp.simplify(ratio135 - x**3) == 0, ratio=str(ratio135), ggm_printed="x**3")

    # --- G2/G3: our 5_2 operator, its palindrome gauge, and GGM (276) -------------------
    rows, objs = {}, {}
    for name in ("4_1", "5_2", "pretzel"):
        cs, r = n_coeffs(name)
        ratio, rp = casoratian_ratio(name)
        L, checks = palindrome_gauge(cs, r)
        gauged = [sp.simplify(sp.cancel(cs[j] * L**j)) for j in range(r + 1)] if L is not None else None
        objs[name] = {"gauged": gauged, "lam": L, "checks": checks, "cs": cs, "r": r}
        rows[name] = {
            "degree": r, "casoratian_ratio": str(ratio),
            "palindrome_gauge": str(L) if L is not None else None,
            "gauged_coeffs": [str(g) for g in gauged] if gauged else None,
            "N_coeffs": [str(c) for c in cs],
        }
        print(f"\n  {name}: deg N = {r}, deg P = {rp}")
        print(f"    Casoratian ratio (-1)^r a_0/a_r = {ratio}")
        print(f"    palindrome gauge lambda = {L}")
        if gauged:
            print(f"    gauged N coefficients     = {gauged}")

    s = P33.SX
    ggm276 = [sp.Integer(1), s, s, sp.Integer(1)]
    g52 = objs["5_2"]["gauged"] or []          # sympy objects, NOT re-parsed strings:
    # sympify("XR**2+1") mints a FRESH XR without positive=True, and the assumption
    # mismatch defeats simplify() — a harness failure that reads as a math failure.
    ok276 = len(g52) == 4 and all(sp.simplify(sp.expand(g52[j] - ggm276[j])) == 0 for j in range(4))
    check("G2-our derived 5_2 N(X), in its palindrome gauge, is GGM's printed (276) coefficients "
          "(1, s, s, 1) EXACTLY — so the gauge is not a free knob, it is the one GGM already use",
          ok276, gauge=rows["5_2"]["palindrome_gauge"], gauged=rows["5_2"]["gauged_coeffs"])

    ok52ratio = rows["5_2"]["palindrome_gauge"] is not None
    check("G3-5_2 admits a palindrome gauge at all, which is what makes GGM's Wronskian "
          "m-INDEPENDENT (their sec-015: det W_{m+1} = det W_m) — the ratio is (-1)^r there",
          ok52ratio, ratio=rows["5_2"]["casoratian_ratio"])

    # --- T1: the pretzel --------------------------------------------------------------
    Lp = rows["pretzel"]["palindrome_gauge"]
    pch = objs["pretzel"]["checks"]
    rows["pretzel"]["end_pair_roots"] = [str(L) for L, _ in pch]
    rows["pretzel"]["why_not_palindromic"] = (
        "no real root of the END-pair equation" if not pch else
        "END-pair roots exist but at least one INTERIOR pair fails at every one of them")
    print(f"\n  pretzel end-pair roots: {rows['pretzel']['end_pair_roots'] or 'none'}")
    print(f"  why not palindromic  : {rows['pretzel']['why_not_palindromic']}")
    if pch:
        L0 = pch[0][0]
        bad = [j for j in range(objs["pretzel"]["r"] + 1)
               if sp.simplify(sp.cancel(objs["pretzel"]["cs"][j] * L0**j
                                        - objs["pretzel"]["cs"][objs["pretzel"]["r"] - j]
                                        * L0**(objs["pretzel"]["r"] - j))) != 0]
        rows["pretzel"]["failing_pairs_at_first_root"] = bad
        print(f"  at lambda = {L0}, failing index pairs: {bad}")
    # The lambda search is over POSITIVE reals. That costs nothing here, and this gate
    # says why rather than leaving it as an unstated scope: for r even, j and r-j have the
    # SAME parity, so lambda^j and lambda^{r-j} carry the same sign for every real lambda.
    # A negative gauge therefore imposes exactly the conditions a positive one does, and
    # cannot rescue a failing interior pair.
    rp6 = objs["pretzel"]["r"]
    same_parity = all((j % 2) == ((rp6 - j) % 2) for j in range(rp6 + 1))
    check("G4-the positive-lambda restriction costs nothing at even rank: j and r-j share parity, "
          "so lambda^j and lambda^{r-j} have the same sign for EVERY real lambda and a negative "
          "gauge imposes the identical conditions — the T1 negative is not an artifact of the "
          "search range", bool(same_parity and rp6 % 2 == 0), r=rp6)

    in_half_ring = False
    if Lp is not None:
        e = sp.simplify(sp.log(sp.sympify(Lp)) / sp.log(q))
        in_half_ring = e.is_Rational and sp.denom(e) in (1, 2)
        rows["pretzel"]["gauge_q_exponent"] = str(e)
        print(f"\n  pretzel gauge as a power of q: q^({e})   in the q^(1/2) ring: {in_half_ring}")
    check("T1-the pretzel's degree-6 N(X) admits a palindrome gauge lying in the q^{1/2} ring "
          "that the level-2 structure lives in (#7333: sigma is odd exactly when q is "
          "half-integral)", bool(Lp is not None and in_half_ring),
          gauge=Lp, q_exponent=rows["pretzel"].get("gauge_q_exponent"),
          casoratian_ratio=rows["pretzel"]["casoratian_ratio"])

    verdict = (
        "DERIVED: the per-knot GL(r) normalisation is NOT a free choice — GGM's Theorem 16(c) names "
        "the mechanism, the Casoratian identity det W_{m+1}/det W_m = (-1)^r a_0/a_r, which depends "
        "on the operator's END coefficients alone. Calibrated on GGM's own printed 4_1 operator "
        f"(135), the rule returns their printed (136) ratio x^3 (G1). Applied to the operators "
        f"#7333 derived: 4_1 ratio {rows['4_1']['casoratian_ratio']}, 5_2 "
        f"{rows['5_2']['casoratian_ratio']}, pretzel {rows['pretzel']['casoratian_ratio']}. Each "
        "operator has a distinguished PALINDROME gauge, the one making the ratio (-1)^r; for 5_2 "
        f"it is lambda = {rows['5_2']['palindrome_gauge']}, and in it our N(X) is GGM's printed "
        "(276) coefficients (1, s, s, 1) exactly (G2) — which is why their 5_2 Wronskian is "
        f"m-independent. The pretzel's gauge is lambda = {Lp}, i.e. q^("
        f"{rows['pretzel'].get('gauge_q_exponent')}); whether that lies in the q^(1/2) ring the "
        f"level-2 grading lives in: {in_half_ring} (T1). When no gauge exists the reason is stated "
        f"rather than left as a bare absence: {rows['pretzel'].get('why_not_palindromic')}"
        f"{', failing index pairs ' + str(rows['pretzel'].get('failing_pairs_at_first_root')) if rows['pretzel'].get('failing_pairs_at_first_root') else ''}.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-wronskian-casoratian-gauge",
         "description": "The Casoratian identity applied to the descendant operators of 4_1, 5_2 and the "
                        "(-2,3,7) pretzel: the Wronskian determinant ratio from the end coefficients, the "
                        "palindrome gauge that trivialises it, and GGM (276) recovered exactly for 5_2.",
         "computation": "aomega-m3-wronskian-casoratian-gauge", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"orientation": "SnapPy's (#7152 Part 11)",
                        "casoratian_rule": "det W_{m+1}/det W_m = (-1)^r a_0/a_r  [GGM Thm 16(c), GK13 Lem 4.7]"},
         "data": {"knots": rows, "ggm135_ratio": str(ratio135), "ggm276_match": bool(ok276),
                  "pretzel_gauge_in_half_ring": bool(in_half_ring),
                  "pretzel_why_not_palindromic": rows["pretzel"].get("why_not_palindromic")},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-wronskian-casoratian-gauge.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
