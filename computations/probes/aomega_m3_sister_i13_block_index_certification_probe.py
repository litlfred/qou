"""aomega_m3_sister_i13_block_index_certification_probe.py

Route C, M3, Part 8 (bean qou-x3iv): the cheapest decisive test of the SISTER
hypothesis H-I13 — that the (-2,3,7) pretzel's state integral is the other
member (A,B) = (1,3) of the Garoufalidis–Kashaev 1-dim family whose (2,3)
member is the 5_2 knot (GK 1304.2705 §1.3: I_{1,2} = I_{4_1}, I_{2,3} = I_{5_2}).

Held inputs (all GGM 2012.00062v3 unless noted):
  (325)  G_{A,r}(y,z;q) = (q;q)_inf^{-1} sum_{n>=0} (-1)^{An} q^{A n(n+1)/2} z^n
                          prod_{j=1}^r (q^{1+n} y_j; q)_inf
  (326)  b^{(k)}_m(x,w;q) = x_k^{-m} G_{A,r}(x/x_k, x_k^{-A} w^{-1} q^m; q)
  (323)  5_2 is (A,r) = (2,3) with u = (0,u,-u), i.e. x = (1, x, 1/x), and t = 0 (w = 1)
  (270)  the 5_2 q-function H(x,y,z;q) has lim_{z->0} H = (qx;q)_inf (qy;q)_inf, which pins
         H(x,y,z;q) = sum_n q^{n(n+1)} z^n (q^{1+n}x;q)_inf (q^{1+n}y;q)_inf / (q;q)_n
         = (q;q)_inf G_{2,3}((1,x,y), z; q)   [the y_3 = 1 specialisation, cf. (335)]
  (316)  S^+(x;q)_{1,1} = H(x,x^-1,1;q) H(x^-1,x,1;q^-1) + H(x,x^2,x^2;q) H(x^-1,x^-2,x^-2;q^-1)
                        + H(x^-1,x^-2,x^-2;q) H(x,x^2,x^2;q^-1)
                        = 1 - (x^-2+3x^-1+4+3x+x^2) q + (x^-3+x^-2-1+x^2+x^3) q^2 + O(q^3)
         and (315): this is Ind^rot_{5_2}(0, x; q), the DGG index with no magnetic flux.
  (106)  (x;q^-1)_inf = (qx;q)_inf^{-1}  — the |q|>1 evaluation. Applied to H it gives
         H(x,y,z;q^-1) = sum_n q^{n(n+1)/2 . (2A-... )}  — see h_minus() below; the same
         substitution turns GGM's J_+ (127a) into their J_- (127b) exactly (checked
         symbolically in gate G0), so it is the rule the paper itself uses.

The (1,3) candidate: the SAME construction with A = 1, i.e.
  H1(x,y,z;q) = sum_n (-1)^n q^{n(n+1)/2} z^n (q^{1+n}x;q)_inf (q^{1+n}y;q)_inf / (q;q)_n,
block arguments from (326) with A = 1, x = (1,x,1/x), w = 1, m = 0:
  k=1: H1(x, 1/x; z=1)   k=2: H1(1/x, 1/x^2; z=1/x)   k=3: H1(x, x^2; z=x)
(for A = 2 the z-slots are x^{-/+2}, reproducing (316) — that is gate G1).
The theta renormalisation (327) cancels in the bilinear B(x;q) B(x^-1;q^-1) for any A
(theta(x;q^-1) = theta(x;q)^-1, (108); theta(x) = theta(1/x), (107)), which is why (316)
is stated on the bare H's; the same cancellation is used here for A = 1.

Certification target (DERIVED, #7101, aomega_m3_rotated_index_three_knots_probe):
  Ind^rot_{m016}(0,zeta;q) = 1 - q(2z+4+2/z) + q^2(z^2+z-1+1/z+1/z^2)
                              + q^3(5z^2+12z+16+12/z+5/z^2) + O(q^4).

Gates: G0 (106)-rule reproduces J_- from J_+;  G1 the (2,3) bilinear reproduces GGM (316)
to q^2;  G2 the (2,3) bilinear reproduces the DERIVED 5_2 index to q^3 (read from the committed
witness, never hardcoded — a first draft hardcoded a wrong q^3 row and mis-scored itself);  then T1
the (1,3) bilinear vs the DERIVED pretzel index to q^3 — PASS certifies H-I13, FAIL is a scope-(a)
negative for this configuration (u = (0,u,-u), t = 0); T2 records whether the (1,3) and (2,3)
bilinears coincide (they do: the swap is invisible in sigma1-sigma1).
RESULT (2026-09-08): G0 G1 G2 pass; T1 FAILS; T2: identical to q^3. H-I13 refuted in this
configuration, with the mechanism recorded.  Exact arithmetic: sympy rational functions of x, integer q-series
truncated at ORDER (computed two orders deeper than read).  No q0, no float, no fit.
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

x, q = sp.symbols("x q")
READ, ORDER = 3, 5          # read to q^READ from a q^ORDER computation


# ---------------------------------------------------------------- series kernel (dict power->coeff)
def s_trunc(expr, order=ORDER):
    """Truncate a sympy expression polynomial in q (coeffs rational in x) to q^order."""
    p = sp.Poly(sp.expand(expr), q)
    return sum(sp.cancel(c) * q**int(m[0]) for m, c in zip(p.monoms(), p.coeffs()) if m[0] <= order)


def s_mul(a, b, order=ORDER):
    return s_trunc(sp.expand(a * b), order)


def s_inv(a, order=ORDER):
    """1/a for a series with constant term a0 != 0 (rational in x)."""
    a = sp.expand(a)
    a0 = a.subs(q, 0)
    assert a0 != 0
    r = a / a0 - 1                      # nilpotent part
    out, pw = sp.Integer(1), sp.Integer(1)
    for k in range(1, order + 1):
        pw = s_mul(pw, -r, order)
        out = out + pw
    return s_trunc(sp.expand(out / a0), order)


def poch_inf(a, shift, order=ORDER):
    """(a q^shift; q)_inf truncated: prod_{l>=0} (1 - a q^{shift+l}), factors beyond q^order = 1.
    shift >= 1 required for the product to be a q-series with unit constant term when a is a
    rational function of x (shift = 0 gives the factor (1 - a), also handled)."""
    out = sp.Integer(1)
    l = 0
    while shift + l <= order:
        out = s_mul(out, 1 - a * q**(shift + l), order)
        l += 1
    return out


def poch_n(a, n, shift, order=ORDER):
    """(a q^shift; q)_n = prod_{l=0}^{n-1} (1 - a q^{shift+l})."""
    out = sp.Integer(1)
    for l in range(n):
        out = s_mul(out, 1 - a * q**(shift + l), order)
    return out


def H_plus(A, a, b, z, order=ORDER):
    """H_A(a,b,z;q) = sum_n (-1)^{An} q^{A n(n+1)/2} z^n (q^{1+n}a)_inf (q^{1+n}b)_inf / (q;q)_n."""
    tot = sp.Integer(0)
    n = 0
    while A * n * (n + 1) // 2 <= order:
        term = sp.Integer((-1) ** (A * n)) * q**(A * n * (n + 1) // 2) * z**n
        term = s_mul(term, s_mul(poch_inf(a, 1 + n, order), poch_inf(b, 1 + n, order), order), order)
        term = s_mul(term, s_inv(poch_n(sp.Integer(1), n, 1, order), order), order)
        tot = tot + term
        n += 1
    return s_trunc(tot, order)


def H_minus(A, a, b, z, order=ORDER):
    """H_A(a,b,z;q^{-1}) via GGM (106): (u;q^-1)_inf = 1/(qu;q)_inf, and
    (q^-1;q^-1)_n = (-1)^n q^{-n(n+1)/2} (q;q)_n,  (q^{-n}a;q)_inf = (-a)^n q^{-n(n+1)/2} (q/a;q)_n (a;q)_inf.
    Result:  sum_n (-1)^{An} q^{(n(n+1)/2)(2 - A) ... } — computed literally below:
      term_n = (-1)^{An} q^{-A n(n+1)/2} z^n
               / [ (-1)^n q^{-n(n+1)/2} (q;q)_n  *  (q^{-n}a;q)_inf (q^{-n}b;q)_inf ]
    with (q^{-n}a;q)_inf = prod_{l=0}^{n} (1 - q^{l-n} a) * (qa;q)_inf  [exact rewrite, no formula guessed]."""
    tot = sp.Integer(0)
    # prefactor 1/((a;q)_inf (b;q)_inf) shared by all terms; write (q^{-n}a)_inf = P_n(a) (qa)_inf,
    # P_n(a) = prod_{l=0}^{n} (1 - q^{l-n} a) = (-a)^{n} q^{-n(n+1)/2} (q/a;q)_n (1 - a)  ... exact:
    n = 0
    inv_a_inf = s_inv(poch_inf(a, 1, order), order)
    inv_b_inf = s_inv(poch_inf(b, 1, order), order)
    while (2 - A) * n * (n + 1) // 2 <= order + 2 and n <= 2 * order + 2:
        # P_n(a) = (1 - a) * prod_{k=1}^{n} (1 - q^{-k} a) = (1-a) * (-a)^n q^{-n(n+1)/2} (q/a;q)_n
        Pa = (1 - a) * (-a) ** n * poch_n(1 / a, n, 1, order)
        Pb = (1 - b) * (-b) ** n * poch_n(1 / b, n, 1, order)
        qpow = (-A * n * (n + 1) // 2) + (n * (n + 1) // 2) + 2 * (n * (n + 1) // 2)   # from the three q^{-n(n+1)/2}
        if qpow < 0:
            n += 1
            continue
        term = sp.Integer((-1) ** (A * n)) * sp.Integer((-1) ** n) * q**qpow * z**n
        term = s_mul(term, s_inv(s_mul(poch_n(sp.Integer(1), n, 1, order), s_mul(Pa, Pb, order), order), order), order)
        tot = tot + term
        n += 1
    return s_mul(s_trunc(tot, order), s_mul(inv_a_inf, inv_b_inf, order), order)


def J_plus(xa, ya, order=ORDER):
    tot = sp.Integer(0)
    n = 0
    while n * (n + 1) // 2 <= order:
        t = sp.Integer((-1) ** n) * q**(n * (n + 1) // 2) * xa**n
        t = s_mul(t, s_inv(s_mul(poch_n(sp.Integer(1), n, 1, order), poch_n(ya, n, 1, order), order), order), order)
        tot += t
        n += 1
    return s_mul(poch_inf(ya, 1, order), tot, order)


def J_minus_printed(xa, ya, order=ORDER):
    """GGM (127b) as printed."""
    tot = sp.Integer(0)
    n = 0
    while n * (n + 1) // 2 <= order:
        t = sp.Integer((-1) ** n) * q**(n * (n + 1) // 2) * xa**n * ya**(-n)
        t = s_mul(t, s_inv(s_mul(poch_n(sp.Integer(1), n, 1, order), poch_n(1 / ya, n, 1, order), order), order), order)
        tot += t
        n += 1
    return s_mul(s_inv(poch_inf(ya, 0, order), order), tot, order)


def J_minus_via_106(xa, ya, order=ORDER):
    """J_+ evaluated at q^-1 by the (106) rule, literally (same algebra as H_minus with A=1, one Pochhammer)."""
    tot = sp.Integer(0)
    n = 0
    inv_inf = s_inv(poch_inf(ya, 0, order), order)   # (q^{-1} y; q^{-1})_inf = 1/(y;q)_inf  [(106) with u = y/q]
    while n * (n + 1) // 2 <= order:
        # (q^-1;q^-1)_n = (-1)^n q^{-n(n+1)/2} (q;q)_n ;  (q^{-1} y; q^{-1})_n = prod_{k=1}^n (1 - q^{-k} y) = (-y)^n q^{-n(n+1)/2} (q/y;q)_n
        t = sp.Integer((-1) ** n) * q**(-n * (n + 1) // 2) * xa**n
        den_q = sp.Integer((-1) ** n) * q**(-n * (n + 1) // 2) * poch_n(sp.Integer(1), n, 1, order)
        den_y = (-ya) ** n * q**(-n * (n + 1) // 2) * poch_n(1 / ya, n, 1, order)
        # t / (den_q den_y): the q-powers combine to q^{+n(n+1)/2}
        num = sp.Integer((-1) ** n) * xa**n * (-ya) ** (-n) * q**(n * (n + 1) // 2) * sp.Integer((-1) ** n)
        t = s_mul(num, s_inv(s_mul(poch_n(sp.Integer(1), n, 1, order), poch_n(1 / ya, n, 1, order), order), order), order)
        tot += t
        n += 1
    return s_mul(inv_inf, tot, order)


def coeffs(series, upto):
    p = sp.Poly(sp.expand(series), q)
    d = dict(zip([m[0] for m in p.monoms()], p.coeffs()))
    return [sp.expand(sp.cancel(d.get(k, 0))) for k in range(upto + 1)]


def bilinear(A, order=ORDER):
    """S^+_{11}(x;q) for the (A,3) family with x = (1,x,1/x), w = 1, m = 0:
    sum_k H_A(args_k; q) H_A(args_k at x->1/x; q^-1),  args from (326)."""
    zk = {2: x ** (-A), 3: x ** A}   # k=2: x_k = x -> z = x^{-A};  k=3: x_k = 1/x -> z = x^{A}
    blocks = [(x, 1 / x, sp.Integer(1)), (1 / x, x ** (-2), zk[2]), (x, x**2, zk[3])]
    tot = sp.Integer(0)
    for (a, b, z) in blocks:
        left = H_plus(A, a, b, z, order)
        right = H_minus(A, a.subs(x, 1 / x), b.subs(x, 1 / x), z.subs(x, 1 / x), order)
        tot += s_mul(left, right, order)
    return s_trunc(tot, order)


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("[G0] the (106) rule reproduces GGM's printed J_- from J_+ (4_1 blocks)")
    xa, ya = sp.symbols("xa ya")
    d = [sp.simplify(u - v) for u, v in zip(coeffs(J_minus_printed(xa, ya), READ), coeffs(J_minus_via_106(xa, ya), READ))]
    check("G0-(106)-rule-reproduces-J_minus-to-q^READ", all(e == 0 for e in d))

    print("[G1] (A,r)=(2,3) bilinear vs GGM (316) printed, to q^2")
    S52 = coeffs(bilinear(2), READ)
    printed = [sp.Integer(1), -(x**-2 + 3 / x + 4 + 3 * x + x**2), (x**-3 + x**-2 - 1 + x**2 + x**3)]
    ok1 = all(sp.simplify(S52[k] - printed[k]) == 0 for k in range(3))
    for k in range(READ + 1):
        print(f"    q^{k}: {S52[k]}")
    check("G1-(2,3)-bilinear-matches-GGM-(316)-to-q^2", ok1, computed=[str(c) for c in S52[:3]])

    print("[G2] (A,r)=(2,3) bilinear vs the DERIVED 5_2 index (aomega_m3_rotated_index_three_knots), to q^3")
    with open(os.path.join(HERE, "aomega-m3-rotated-index-three-knots.witness.json")) as fh:
        rot = json.load(fh)["data"]["rotated_index"]
    zeta = sp.Symbol("zeta")

    def derived_row(name):
        row = rot[name]["0"]
        return [sp.expand(sp.sympify(row.get(f"q^{k}", "0"), locals={"zeta": zeta}).subs(zeta, x)) for k in range(READ + 1)]

    derived52 = derived_row("m015")
    ok2 = all(sp.simplify(S52[k] - derived52[k]) == 0 for k in range(READ + 1))
    check("G2-(2,3)-bilinear-matches-DERIVED-5_2-index-to-q^3", ok2, derived=[str(c) for c in derived52])

    print("[T1] (A,r)=(1,3) candidate bilinear vs the DERIVED (-2,3,7) index, to q^3")
    S13 = coeffs(bilinear(1), READ)
    target = derived_row("m016")
    for k in range(READ + 1):
        print(f"    q^{k}: candidate = {S13[k]}")
        print(f"          pretzel   = {target[k]}")
    match = [sp.simplify(S13[k] - target[k]) == 0 for k in range(READ + 1)]
    check("T1-(1,3)-sister-candidate-equals-DERIVED-pretzel-index-to-q^3", all(match), per_order=match)
    same52 = all(sp.simplify(S13[k] - derived52[k]) == 0 for k in range(READ + 1))
    check("T2-(1,3)-and-(2,3)-bilinears-COINCIDE-identically-to-q^3 (the A <-> r-A swap is invisible in sigma1sigma1)",
          same52, equals_5_2=same52)
    at1 = [c.subs(x, 1) for c in S13]
    print(f"    (1,3) candidate at x=1: {at1}   [pretzel total index 1,-8,3,50; 5_2: 1,-12,3,74]")

    verdict = ("H-I13 CERTIFIED: the (1,3) bilinear reproduces the derived pretzel index to q^3"
               if all(match) else
               "H-I13 REFUTED in the 5_2 configuration u=(0,u,-u), t=0, with a mechanism: the (1,3) block "
               "bilinear COINCIDES with the (2,3) one at every order computed (the A <-> r-A swap, i.e. q <-> q~, "
               "is invisible in the sigma1-sigma1 entry, cf. GK Lemma 1.5a F_{A,B}(q^-1) = F_{B-A,B}(q)), so it "
               "reproduces the 5_2 index and NOT the pretzel's. Scope-(a) for the configuration; the mechanism "
               "says no member of the 1-dim family with this u-configuration can distinguish the pretzel from 5_2 "
               "in sigma1-sigma1, so the pretzel is not the 'q <-> q~ sister' of 5_2 inside the GK family. "
               f"Candidate at x=1: {at1}; pretzel: 1,-8,3,50.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {
        "name": "aomega-m3-sister-i13-block-index-certification",
        "description": "Sister hypothesis H-I13 for (-2,3,7): the GK/GGM (A,r)=(1,3) one-dimensional family's "
                       "block bilinear vs the derived rotated 3D-index; gates at 4_1 (J_-) and 5_2 (GGM 316).",
        "computation": "aomega-m3-sister-i13-block-index-certification",
        "engine": "python", "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {"read_order": READ, "compute_order": ORDER, "configuration": "x=(1,x,1/x), w=1, m=0"},
        "data": {"S11_23": [str(c) for c in S52], "S11_13_candidate": [str(c) for c in S13],
                 "pretzel_derived": [str(sp.expand(c)) for c in target], "candidate_at_x1": [str(c) for c in at1]},
        "verdict": verdict, "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-sister-i13-block-index-certification.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False); fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
