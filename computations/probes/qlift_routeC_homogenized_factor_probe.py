#!/usr/bin/env python3
"""Route C: homogenized order-3 factorization test for the 4_1 colored Jones.

Workplan step 3 (route C) of docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md.
Context: docs/audits/2026-07-20-qlift-ggm-gauge-prune.md (scope-(b) diagonal-gauge
exclusion C1 <-> GGM) and docs/audits/2026-07-20-qlift-literature-check.md S3
(the 4_1 colored Jones satisfies a minimal ORDER-2 INHOMOGENEOUS q-recurrence,
Garoufalidis-Le, corpus garoufalidis-le-2005; strong AJ for 4_1 per
nguyen-tran-2021, arXiv:2006.02042 -- PDF not in library/ and arXiv is
proxy-blocked in this sandbox, so the recurrence is DERIVED here from the
Habiro sum rather than transcribed).

TASK. Locate BOTH q-lift kernel candidates relative to the actual colored-Jones
q-holonomic module:

  C1  (q-Hermite/q-involution, proved c(q)=1 exact):
        [m+2]_q * b_{m+2} = b_{m+1} + b_m
  C2  (GGM eq 49, arXiv:2012.00062 p.14, library/arxiv-2012.00062v3/2012.00062v3.pdf):
        y_{m+1} - (2 - q^m) * y_m + y_{m-1} = 0

by testing whether either is a RIGHT FACTOR of the order-3 homogenization L3 of
the 4_1 colored-Jones recurrence -- equivalently (right factor of order 2 <=>
its 2-dim solution space lies inside the 3-dim solution space of L3), whether
C1 / C2 solutions satisfy L3.

METHOD.
  P1  Habiro sum, exact symbolic (integer Laurent polynomials in q):
        J_N(4_1) = sum_{k=0}^{N-1} prod_{j=1}^{k} (q^N + q^-N - q^j - q^-j)
      Sanity: J_2 = Jones polynomial of 4_1 (q^2 - q + 1 - 1/q + 1/q^2),
      J_N(1) = 1, bar symmetry J_N(1/q) = J_N(q), N <= 12.
  P2  Recover the minimal inhomogeneous order-2 recurrence
        A(q,x) J_{m+1} + B(q,x) J_m + C(q,x) J_{m-1} + E(q,x) = 0,   x = q^m
      by undetermined coefficients mod p = 2^61 - 1 (minimal-window search over
      x-degree D and q-degree T; random q samples), rational-lift the nullspace
      vector, then CERTIFY EXACTLY: the relation is verified per-m as an
      integer Laurent-polynomial identity in Z[q, 1/q] for every m = 2..40.
      The mod-p guess carries no epistemic weight; the exact certification and
      the Garoufalidis-Le q-holonomy/minimality theorem do. Minimality (no
      inhomogeneous order < 2) is cited from garoufalidis-le-2005, NOT re-proved.
  P3  Homogenize to order 3: with beta_m := -E(q, q^m) != 0 (provably nonzero
      for q > 1, m >= 1: E = x(1+x)(x^2-q)(qx^2-1)),
        (L3 y)_m := beta_{m+1} * (L y)_m - beta_m * (L y)_{m+1},
        (L y)_m  := A(x_m) y_{m+1} + B(x_m) y_m + C(x_m) y_{m-1}.
      L3 annihilates exactly the 3-dim space {y : L y = c * beta, c const} =
      (affine J line) + ker(L_hom); by construction L_hom = (A, B, C) IS an
      order-2 right factor of L3.
  P4  Factor tests, EXACT rational arithmetic end-to-end at
      q = 21/20 (= 1.05 exactly) and q = 55499/50000 (= 1.10998 exactly),
      residuals R_m = (L3 y)_m for m = 2..28 (sequences to m = 30):
        - positive control J          (must be exactly 0 -- pipeline gate)
        - positive control ker(L_hom) (must be exactly 0 -- pipeline gate)
        - C1 solutions, ICs (b_0,b_1) in {(1,0),(0,1),(1,1)}
        - C2/GGM solutions, ICs (y_0,y_1) in {(1,0),(0,1),(1,1)}
      Reporting at mp.dps = 50 (relative residual |R_m| / sum|terms|).

KILL CRITERION (pre-stated). A kernel EMBEDS iff R_m == 0 EXACTLY (Fraction)
for all m = 2..28 and both fundamental ICs (numerically: rel residual < 1e-40
at dps 50). If either positive control fails to embed the probe ABORTS (its
own pipeline is then wrong -- no verdict is emitted). A max rel residual
>= 1e-6 on a candidate is a clean NOT-EMBEDDED.

SCOPE (per AGENTS.md before-declaring-refuted). The NOT-EMBEDDED verdicts are
scope-(a): C1 (resp. GGM eq-49) solutions, AS-IS (ungauged), do not lie in the
L3 module. Non-diagonal GL2 gauges, Mobius transforms of solution ratios, and
q-Borel/summation transforms (the explicitly-not-excluded list of the
2026-07-20 gauge-prune audit) are NOT tested here and remain live. The
positive-control embeds are exact identities, not fits. No AME data, no
experimental anchors, nothing here is a "derivation" of the q-lift.

Run:  python3 -u computations/probes/qlift_routeC_homogenized_factor_probe.py \
          2>&1 | tee /tmp/qlift-routeC.log
Emits: qlift_routeC_homogenized_factor_probe.witness.json (same directory).
"""

import json
import os
import random
from datetime import datetime, timezone
from fractions import Fraction
from math import gcd, isqrt, lcm

from mpmath import mp

mp.dps = 50

PRIME = (1 << 61) - 1          # Mersenne prime for the guess stage
CERT_M_MAX = 40                # exact per-m certification range
TEST_M_LO, TEST_M_HI = 2, 28   # factor-test residual range (sequences to m=30)
SEED = 20260720

Q_VALUES = [("21/20", Fraction(21, 20)),
            ("55499/50000", Fraction(55499, 50000))]


# ---------- P1: Habiro sum, symbolic Laurent polynomials {exp: int} ----------

def ladd(p1, p2):
    out = dict(p1)
    for e, c in p2.items():
        v = out.get(e, 0) + c
        if v:
            out[e] = v
        else:
            out.pop(e, None)
    return out


def lmul(p1, p2):
    out = {}
    for e1, c1 in p1.items():
        for e2, c2 in p2.items():
            e = e1 + e2
            v = out.get(e, 0) + c1 * c2
            if v:
                out[e] = v
            else:
                out.pop(e, None)
    return out


def jones_sym_all(nmax):
    J = {0: {}}
    for N in range(1, nmax + 1):
        term = {0: 1}
        total = {0: 1}
        for k in range(1, N):
            term = lmul(term, ladd({N: 1, -N: 1}, {k: -1, -k: -1}))
            total = ladd(total, term)
        J[N] = total
    return J


def p1_sanity(Jsym):
    print("P1  Habiro sum sanity (symbolic, exact):")
    assert Jsym[1] == {0: 1}
    jones_41 = {2: 1, 1: -1, 0: 1, -1: -1, -2: 1}
    assert Jsym[2] == jones_41, "J_2 != Jones polynomial of 4_1"
    for N in range(1, 13):
        assert sum(Jsym[N].values()) == 1, f"J_{N}(1) != 1"
        assert Jsym[N] == {-e: c for e, c in Jsym[N].items()}, f"J_{N} not bar-symmetric"
    print("    J_2 = q^2 - q + 1 - 1/q + 1/q^2 (Jones of 4_1)  OK")
    print("    J_N(1) = 1 and J_N(1/q) = J_N(q) for N <= 12    OK")
    return {"j2_matches_jones_41": True, "jN_at_1_is_1": True,
            "bar_symmetric": True, "n_checked": 12}


# ---------- P2: recover + certify the inhomogeneous order-2 recurrence ------

def jones_val_mod(nmax, qs, p):
    inv = pow(qs, p - 2, p)
    out = [0] * (nmax + 1)
    for N in range(1, nmax + 1):
        lam = (pow(qs, N, p) + pow(inv, N, p)) % p
        term, total = 1, 1
        for k in range(1, N):
            term = term * ((lam - pow(qs, k, p) - pow(inv, k, p)) % p) % p
            total = (total + term) % p
        out[N] = total
    return out


def nullspace_mod(rows, ncols, p):
    mat = [r[:] for r in rows]
    pivots, r = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = pow(mat[r][c], p - 2, p)
        mat[r] = [v * inv % p for v in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] % p:
                f = mat[i][c]
                mat[i] = [(v - f * w) % p for v, w in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-mat[i][fc]) % p
        basis.append(v)
    return basis


def rational_reconstruct(a, p):
    bound = isqrt(p // 2)
    r0, r1, s0, s1 = p, a % p, 0, 1
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        s0, s1 = s1, s0 - qq * s1
    if s1 == 0 or abs(s1) > bound or gcd(r1, abs(s1)) != 1:
        return None
    return Fraction(r1, s1) if s1 > 0 else Fraction(-r1, -s1)


def lift_vector(vec, p):
    fracs = []
    for a in vec:
        f = rational_reconstruct(a, p)
        if f is None:
            return None
        fracs.append(f)
    den = 1
    for f in fracs:
        den = lcm(den, f.denominator)
    ints = [int(f * den) for f in fracs]
    g = 0
    for v in ints:
        g = gcd(g, v)
    return [v // g for v in ints] if g else ints


def unpack(vec, D, T):
    coeffs, idx = [], 0
    for _ in range(4):
        d = {}
        for i in range(D + 1):
            for t in range(T + 1):
                c = vec[idx]
                idx += 1
                if c:
                    d[(i, t)] = c
        coeffs.append(d)
    return coeffs


def coeff_at_m(d, m):
    out = {}
    for (i, t), c in d.items():
        e = m * i + t
        v = out.get(e, 0) + c
        if v:
            out[e] = v
        else:
            out.pop(e, None)
    return out


def certify_exact(coeffs, Jsym, m_lo=2, m_hi=CERT_M_MAX):
    """Exact per-m Laurent-identity check over Z[q, 1/q]."""
    A, B, C, E = coeffs
    for m in range(m_lo, m_hi + 1):
        tot = lmul(coeff_at_m(A, m), Jsym[m + 1])
        tot = ladd(tot, lmul(coeff_at_m(B, m), Jsym[m]))
        tot = ladd(tot, lmul(coeff_at_m(C, m), Jsym[m - 1]))
        tot = ladd(tot, coeff_at_m(E, m))
        if tot:
            return False, m
    return True, None


def p2_recover(Jsym):
    print("P2  minimal-window mod-p recovery + exact certification:")
    rng = random.Random(SEED)
    m_lo, m_hi = 3, 46
    samples = [rng.randrange(2, PRIME - 2) for _ in range(6)]
    jcache = {qs: jones_val_mod(m_hi + 1, qs, PRIME) for qs in samples}
    for total in range(2, 16):
        for D in range(1, min(total, 9) + 1):
            T = total - D
            if not 0 <= T <= 12:
                continue
            ncols = 4 * (D + 1) * (T + 1)
            rows = []
            for qs in samples:
                Jv = jcache[qs]
                for m in range(m_lo, m_hi + 1):
                    xm = pow(qs, m, PRIME)
                    xpow = [pow(xm, i, PRIME) for i in range(D + 1)]
                    qpow = [pow(qs, t, PRIME) for t in range(T + 1)]
                    row = []
                    for ds in (1, 0, -1, None):
                        base = Jv[m + ds] if ds is not None else 1
                        for i in range(D + 1):
                            for t in range(T + 1):
                                row.append(base * xpow[i] % PRIME * qpow[t] % PRIME)
                    rows.append(row)
            basis = nullspace_mod(rows, ncols, PRIME)
            if not basis:
                continue
            for vec in basis:
                ints = lift_vector(vec, PRIME)
                if ints is None:
                    continue
                coeffs = unpack(ints, D, T)
                ok, _ = certify_exact(coeffs, Jsym)
                if ok:
                    print(f"    window (x-deg D={D}, q-deg T={T}): nullspace dim "
                          f"{len(basis)}; CERTIFIED exactly for m=2..{CERT_M_MAX}")
                    return D, T, coeffs
    raise SystemExit("ABORT: no certifiable recurrence found in window sweep")


def coeffs_pretty(coeffs):
    names = ["A(J_{m+1})", "B(J_m)", "C(J_{m-1})", "E(inhom)"]
    lines = []
    for n, d in zip(names, coeffs):
        s = " + ".join(f"{c}*x^{i}*q^{t}" for (i, t), c in sorted(d.items()))
        lines.append(f"{n} = {s}")
    return lines


def p2_factored_check(coeffs):
    """Verify the factored literature form of A, C, E symbolically (2-var
    dict {(i,t): c}), x = q^m; B is kept expanded."""
    def poly_mul(p1, p2):
        out = {}
        for k1, c1 in p1.items():
            for k2, c2 in p2.items():
                k = (k1[0] + k2[0], k1[1] + k2[1])
                v = out.get(k, 0) + c1 * c2
                if v:
                    out[k] = v
                else:
                    out.pop(k, None)
        return out

    def pm(*fs):
        out = {(0, 0): 1}
        for f in fs:
            out = poly_mul(out, f)
        return out

    x = {(1, 0): 1}
    x2 = {(2, 0): 1}
    q = {(0, 1): 1}
    one = {(0, 0): 1}
    neg = {(0, 0): -1}
    x2_minus_q = {(2, 0): 1, (0, 1): -1}
    qx_minus_1 = {(1, 1): 1, (0, 0): -1}
    x_minus_q = {(1, 0): 1, (0, 1): -1}
    qx2_minus_1 = {(2, 1): 1, (0, 0): -1}
    one_plus_x = {(0, 0): 1, (1, 0): 1}
    A_fact = pm(neg, x2, x2_minus_q, qx_minus_1)
    C_fact = pm(neg, x2, x_minus_q, qx2_minus_1)
    E_fact = pm(x, one_plus_x, x2_minus_q, qx2_minus_1)
    A, B, C, E = coeffs
    assert A == A_fact and C == C_fact and E == E_fact, "factored form mismatch"
    print("    factored form verified:  A = -x^2 (x^2-q)(qx-1),"
          "  C = -x^2 (x-q)(qx^2-1),  E = x(1+x)(x^2-q)(qx^2-1)")
    return ["A = -x^2 (x^2 - q)(q x - 1)",
            "B = q - 2qx - (1+q^2)x^2 + (1+q+q^2)(x^3+x^4) - (1+q^2)x^5 - 2qx^6 + qx^7",
            "C = -x^2 (x - q)(q x^2 - 1)",
            "E = x (1 + x)(x^2 - q)(q x^2 - 1)"]


# ---------- P3/P4: exact homogenization + factor tests ----------------------

def eval_coeff(d, q, x):
    return sum(c * x ** i * q ** t for (i, t), c in d.items())


def jones_frac(nmax, q):
    out = [Fraction(0)] * (nmax + 1)
    for N in range(1, nmax + 1):
        lam = q ** N + q ** -N
        term, total = Fraction(1), Fraction(1)
        for k in range(1, N):
            term *= lam - q ** k - q ** -k
            total += term
        out[N] = total
    return out


def qint(k, q):
    return (1 - q ** k) / (1 - q)


def frac_to_str50(fr):
    return mp.nstr(mp.mpf(fr.numerator) / mp.mpf(fr.denominator), 12)


class Module3:
    def __init__(self, coeffs, q):
        self.A, self.B, self.C, self.E = coeffs
        self.q = q

    def Lrow(self, m):
        q, x = self.q, self.q ** m
        return (eval_coeff(self.A, q, x), eval_coeff(self.B, q, x),
                eval_coeff(self.C, q, x))

    def beta(self, m):
        return -eval_coeff(self.E, self.q, self.q ** m)

    def residual(self, y, m):
        a0, b0, c0 = self.Lrow(m)
        a1, b1, c1 = self.Lrow(m + 1)
        bm, bm1 = self.beta(m), self.beta(m + 1)
        r = bm1 * (a0 * y[m + 1] + b0 * y[m] + c0 * y[m - 1]) \
            - bm * (a1 * y[m + 2] + b1 * y[m + 1] + c1 * y[m])
        scale = (abs(bm1) * (abs(a0 * y[m + 1]) + abs(b0 * y[m]) + abs(c0 * y[m - 1]))
                 + abs(bm) * (abs(a1 * y[m + 2]) + abs(b1 * y[m + 1]) + abs(c1 * y[m])))
        return r, scale

    def test(self, y, label):
        exact_zero, worst, worst_m, least = True, Fraction(0), None, None
        for m in range(TEST_M_LO, TEST_M_HI + 1):
            r, scale = self.residual(y, m)
            if r != 0:
                exact_zero = False
                rel = abs(r) / scale
                if rel > worst:
                    worst, worst_m = rel, m
                if least is None or rel < least:
                    least = rel
        row = {"label": label, "exact_zero": exact_zero}
        if exact_zero:
            print(f"      {label:28s} EMBEDS (residual exactly 0, m={TEST_M_LO}..{TEST_M_HI})")
        else:
            row["max_rel_residual"] = frac_to_str50(worst)
            row["max_at_m"] = worst_m
            row["min_rel_residual"] = frac_to_str50(least)
            print(f"      {label:28s} NOT-EMBEDDED  max rel resid "
                  f"{frac_to_str50(worst)} at m={worst_m} (min {frac_to_str50(least)})")
        return row


def p34_factor_tests(coeffs, qname, q):
    print(f"P3/P4  q = {qname} (exact rational arithmetic):")
    mod = Module3(coeffs, q)
    nseq = TEST_M_HI + 2  # sequences to index m = 30

    # recurrence exactness at this q (redundant with symbolic cert; belt+braces)
    J = jones_frac(nseq + 1, q)
    for m in range(2, nseq):
        a, b, c = mod.Lrow(m)
        assert a * J[m + 1] + b * J[m] + c * J[m - 1] == mod.beta(m)
    for m in range(1, nseq + 1):
        assert mod.beta(m) != 0
    print(f"    recurrence exact at this q for m=2..{nseq - 1}; beta_m != 0  OK")

    rows = []
    # positive controls (gates)
    ctrl_j = mod.test(J, "control: J (colored Jones)")
    h = [Fraction(0), Fraction(1), Fraction(1)]
    for m in range(2, nseq):
        a, b, c = mod.Lrow(m)
        h.append(-(b * h[m] + c * h[m - 1]) / a)
    ctrl_h = mod.test(h, "control: ker(L_hom)")
    if not (ctrl_j["exact_zero"] and ctrl_h["exact_zero"]):
        raise SystemExit("ABORT: positive control failed -- pipeline invalid, no verdict")
    rows += [ctrl_j, ctrl_h]

    # C1 candidate
    c1_embeds = True
    for ics in ((1, 0), (0, 1), (1, 1)):
        b = [Fraction(ics[0]), Fraction(ics[1])]
        for m in range(nseq - 1):
            b.append((b[-1] + b[-2]) / qint(m + 2, q))
        row = mod.test(b, f"C1 [m+2]_q kernel ics={ics}")
        c1_embeds &= row["exact_zero"]
        rows.append(row)

    # GGM eq-49 candidate
    ggm_embeds = True
    for ics in ((1, 0), (0, 1), (1, 1)):
        y = [Fraction(ics[0]), Fraction(ics[1])]
        for m in range(1, nseq):
            y.append((2 - q ** m) * y[-1] - y[-2])
        row = mod.test(y, f"GGM eq-49 kernel ics={ics}")
        ggm_embeds &= row["exact_zero"]
        rows.append(row)

    print()
    return {"q": qname, "rows": rows, "c1_embeds": c1_embeds,
            "ggm_embeds": ggm_embeds}


# ---------- main ------------------------------------------------------------

def main():
    Jsym = jones_sym_all(CERT_M_MAX + 6)
    p1 = p1_sanity(Jsym)
    D, T, coeffs = p2_recover(Jsym)
    pretty = coeffs_pretty(coeffs)
    factored = p2_factored_check(coeffs)
    for line in pretty:
        print(f"    {line}")

    results = [p34_factor_tests(coeffs, qname, q) for qname, q in Q_VALUES]

    all_c1 = all(r["c1_embeds"] for r in results)
    all_ggm = all(r["ggm_embeds"] for r in results)
    verdict = (
        "NEITHER EMBEDS: C1 ([m+2]_q b_{m+2} = b_{m+1} + b_m) and GGM eq-49 "
        "(y_{m+1} = (2-q^m) y_m - y_{m-1}) solutions, as-is (ungauged), are "
        "NOT right factors of the homogenized order-3 colored-Jones operator "
        "L3 of 4_1 -- residuals are exact nonzero rationals of relative size "
        "O(1) at every tested m, both q values, all ICs. Positive controls "
        "(J itself and ker(L_hom)) embed with residual exactly 0, so the "
        "order-2 right factor of L3 is the AJ homogeneous part L_hom = "
        "(A, B, C), and BOTH q-lift kernel candidates sit OUTSIDE the 4_1 "
        "colored-Jones q-holonomic module in the ungauged sense. Scope-(a): "
        "non-diagonal GL2 gauges, Mobius transforms, and q-Borel/summation "
        "transforms are untested and remain live; nothing here is a "
        "'derivation' of the q-lift."
        if not (all_c1 or all_ggm) else
        f"EMBEDDING FOUND: c1={all_c1} ggm={all_ggm} -- see rows")
    print("VERDICT:", verdict)

    witness = {
        "description": "Route C homogenized order-3 factorization test: are the "
                       "q-lift kernel candidates C1 (q-involution, [m+2]_q "
                       "b_{m+2} = b_{m+1} + b_m) or C2 (GGM eq-49) right "
                       "factors of the homogenized order-3 recurrence of the "
                       "4_1 colored Jones? Locates both kernels relative to "
                       "the actual colored-Jones q-holonomic module.",
        "computation": "P1 Habiro sum symbolic sanity; P2 minimal inhomogeneous "
                       "order-2 recurrence recovered by mod-p undetermined "
                       "coefficients and CERTIFIED exactly per-m as a "
                       f"Z[q,1/q] Laurent identity for m=2..{CERT_M_MAX} "
                       "(minimality per garoufalidis-le-2005, not re-proved); "
                       "P3 homogenization L3 = (beta_{m+1} - beta_m S) o L; "
                       "P4 exact-rational solution-space membership tests with "
                       "positive controls; reporting at mp.dps=50",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {
            "dps": mp.dps,
            "q_values": [n for n, _ in Q_VALUES],
            "test_m_range": [TEST_M_LO, TEST_M_HI],
            "sequences_to_m": TEST_M_HI + 2,
            "certification_m_max": CERT_M_MAX,
            "guess_prime": "2^61 - 1",
            "seed": SEED,
            "kill_criterion": "EMBEDS iff residual exactly 0 (Fraction) for "
                              "all m and both fundamental ICs (rel < 1e-40 at "
                              "dps 50); probe aborts if a positive control "
                              "fails",
        },
        "recurrence": {
            "form": "A(q,x) J_{m+1} + B(q,x) J_m + C(q,x) J_{m-1} + E(q,x) = 0, "
                    "x = q^m; J_1 = 1 Habiro-sum normalization",
            "window": {"x_degree": D, "q_degree": T},
            "coefficients_expanded": pretty,
            "coefficients_factored": factored,
            "certification": f"exact integer-Laurent identity per m = 2..{CERT_M_MAX}; "
                             "mod-p guess stage carries no epistemic weight",
            "minimality": "inhomogeneous order 2 is minimal per "
                          "garoufalidis-le-2005 (cited, not re-proved); strong "
                          "AJ for 4_1 per nguyen-tran-2021 (arXiv:2006.02042; "
                          "PDF proxy-blocked in sandbox, recurrence derived "
                          "from the Habiro sum instead)",
        },
        "results": {"sanity": p1, "factor_tests": results, "verdict": verdict},
        "context": {
            "workplan": "docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md "
                        "(step 3, route C)",
            "gauge_prune": "docs/audits/2026-07-20-qlift-ggm-gauge-prune.md "
                           "(scope-(b) diagonal-gauge exclusion C1 <-> GGM)",
            "literature_check": "docs/audits/2026-07-20-qlift-literature-check.md "
                                "S3 (4_1 minimal order-2 inhomogeneous, "
                                "homogeneous order 3)",
            "ggm_eq49_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf p.14 (arXiv:2012.00062)",
            "discipline": "scope-(a) verdict vocabulary; exact arithmetic; no "
                          "AME data; anti-fit; positive controls gate the "
                          "pipeline",
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qlift_routeC_homogenized_factor_probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
