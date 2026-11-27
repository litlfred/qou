#!/usr/bin/env python3
"""Scalar (rank-1) q-difference kernel is EXCLUDED on the SURVIVING binding carrier.

FRONT 4 / bean qou-o37w (epic qou-v2om).  Derivation, not extraction: nothing here
is fitted, no AME/CODATA anchor is read, and no functional form is chosen to match
data.  The result is a scope-(b) structural exclusion with a named invariant.

WHERE THIS SITS
---------------
`prop:binding-genfun-qdifference` posits the RANK-1 (scalar) relation

    G(qx;q) = R(q,x)*G(x;q),      R in Q(q)[x,x^-1] of bounded depth d.

Two carriers have been proposed for G.

  (RAW)  the ordinary generating function of the raw body terms B_n = I(n)/n.
         ALREADY EXCLUDED, sorry-free, by the confluent/Gevrey growth argument
         QOU.Mass.QDifferenceConfluentObstruction.no_bounded_depth_first_order_kernel
         (audit 2026-07-20-qdifference-kernel-confluent-narrowing.md §4).

  (NORM) the q-Borel / Gevrey-normalized carrier b_n = f_n/[n]_q!, to which §5 of
         that same audit explicitly RE-TARGETED the conjecture, stating "the
         obstruction vanishes" there and predicting depth d = 2.  That carrier
         provably satisfies the depth-2 kernel (sorry-free,
         QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists)

             [m+2]_q * b_{m+2} = b_{m+1} + b_m,     [k]_q = (q^k - 1)/(q - 1),

         which, with x = q^m and sigma : x |-> qx, is exactly the operator named
         as the kernel's carrier K by `conj:qdifference-kernel-prolongation-symbol`

             L_K = (q^2 x - 1) sigma^2 - (q - 1) sigma - (q - 1).

THE QUESTION THIS PROBE ANSWERS.  Does the SURVIVING (NORM) carrier admit the
scalar rank-1 kernel that `prop:binding-genfun-qdifference` requires?

THE ANSWER: NO, and the obstruction is a parity of polynomial degrees.
A scalar kernel is a first-order right factor sigma - a of L_K, i.e. a solution
a in K(x) of the q-Riccati equation

    (q^2 x - 1) a(qx) a(x) - (q - 1) a(x) - (q - 1) = 0.

Writing a = P/Q in lowest terms and clearing denominators,

    (q^2 x - 1) P(qx) P(x) - (q-1) P(x) Q(qx) - (q-1) Q(qx) Q(x) = 0,

whose three terms have degrees T1 = 1+2p, T2 = p+u, T3 = 2u (p = deg P,
u = deg Q).  T1 is ODD-SHAPED (2p+1) and T3 is EVEN (2u), so T1 = T3 is
impossible for every p,u; a short case split then shows the MAXIMUM of
{T1,T2,T3} is attained EXACTLY ONCE for every (p,u).  A single top-degree term
cannot cancel, and its leading coefficient is a product of nonzero factors
whenever q not in {0,1}.  Hence NO rational a exists, L_K has no first-order
right factor, K is irreducible of rank 2, and no nonzero solution of L_K obeys
any scalar relation sigma G = R G with R in K(x).

This parity IS the Newton-slope invariant: L_K is pure isoclinic of slope 1/2
at infinity, and 1/2 is not an integer while every rank-1 q-difference module
has INTEGER slope.  Corroborated independently by the van der Put-Reversat
structure theorem for pure modules of non-integral slope d/r (gcd(d,r)=1): such
a module of rank r is E(r,d,b) and is IRREDUCIBLE -- held in this corpus at
library/crmath-2011-349-19-20-1037-0/ (Bugeaud, C. R. Acad. Sci. Paris 349
(2011) 1037-1039, sec-002).  Slope 1/2 has r = 2 = rank(K).

SCOPE, stated before the run (AGENTS.md "refuted"/"ruled out" discipline):
  * scope (b) STRUCTURAL EXCLUSION, invariant cited: no scalar kernel
    R in K(x) (a fortiori none in K[x,x^-1] of any depth d) on the (NORM)
    carrier, for any field K and any q in K with q != 0, 1.
  * It is NOT a refutation of the carrier, of the depth-2 prediction, or of the
    prolongation-symbol identification.  The carrier and the depth-2 shape both
    SURVIVE -- as a RANK-2 matrix kernel.  What dies is only the scalar form.
  * The exclusion is over K(x).  After a degree-2 RAMIFIED base change the slope
    becomes the integer 1 and a scalar kernel does exist on the double cover;
    that is the precise missing structure, not a loophole in the proof.

T5 is logically independent and sharpens the conjecture block's "supplies a
derived target but does not determine it" into an exact count: with R an
UNCONSTRAINED formal power series the map {kernel coefficients} <-> {body terms}
is a BIJECTION, one new kernel coefficient per body order, so the ansatz then
constrains nothing at all.  Every bit of content lives in the finiteness of the
Laurent window -- which is exactly what T1-T4 remove for the scalar form.

PRECISION.  Exact throughout: sympy over Q(q) with q a free symbol (T1-T3, T5)
and Fraction/mpmath.mpf at >= 220 dps for the asymptotic corroboration (T4).
No float64 anywhere; no float() outside display.  Emits no witness (structural
probe, no derived numeric quantity enters production).

Run:  python3 -u computations/probes/binding_qdiff_scalar_kernel_parity_exclusion_probe.py \
          2>&1 | tee /tmp/qdiff-parity.log
"""
from __future__ import annotations

import sys
from fractions import Fraction

import mpmath as mp
import sympy as sp

mp.mp.dps = 220

q = sp.Symbol("q")
x = sp.Symbol("x")

RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}", flush=True)


# ---------------------------------------------------------------- T1
def t1_operator_transcription() -> None:
    """L_K really is the recurrence [m+2]_q b_{m+2} = b_{m+1} + b_m."""
    m = sp.Symbol("m")
    b2, b1, b0 = sp.symbols("b2 b1 b0")
    qint = lambda k: (q ** k - 1) / (q - 1)          # noqa: E731
    recurrence = sp.simplify(qint(m + 2) * b2 - b1 - b0)
    # L_K applied to (b0,b1,b2) at x = q^m, then divided by (q-1):
    L_K = ((q ** 2 * q ** m - 1) * b2 - (q - 1) * b1 - (q - 1) * b0) / (q - 1)
    diff = sp.simplify(sp.expand(recurrence - L_K))
    record(
        "T1_operator_transcription",
        diff == 0,
        "L_K = (q^2 x - 1)s^2 - (q-1)s - (q-1) at x=q^m is exactly "
        f"(q-1)*([m+2]_q b_{{m+2}} - b_{{m+1}} - b_m); residual = {diff}",
    )


# ---------------------------------------------------------------- T2
def t2_degree_parity_core(pmax: int = 80) -> None:
    """THE INVARIANT.  max(T1,T2,T3) is attained exactly once, for every (p,u)."""
    bad: list[tuple[int, int]] = []
    t1_wins = t3_wins = 0
    for p in range(pmax + 1):
        for u in range(pmax + 1):
            T = (1 + 2 * p, p + u, 2 * u)
            M = max(T)
            if T.count(M) != 1:
                bad.append((p, u))
            elif M == T[0]:
                t1_wins += 1
            else:
                t3_wins += 1
    record(
        "T2_degree_parity_core",
        not bad,
        f"exhaustive p,u <= {pmax} ({(pmax+1)**2} pairs): unique strict maximum in "
        f"every case ({t1_wins} won by T1=1+2p when p>=u, {t3_wins} by T3=2u when "
        f"p<u); T1=T3 needs 2u-2p=1, impossible over Z (the parity). "
        f"violations = {len(bad)}",
    )


# ---------------------------------------------------------------- T3
def t3_symbolic_riccati_no_solution(dmax: int = 4) -> None:
    """Exact symbolic check: the top-degree coefficient is a nonzero monomial."""
    failures: list[str] = []
    checked = 0
    for p in range(dmax + 1):
        for u in range(dmax + 1):
            c = sp.symbols(f"c0:{p+1}")
            d = sp.symbols(f"d0:{u+1}")
            P = sum(c[i] * x ** i for i in range(p + 1))
            Q = sum(d[j] * x ** j for j in range(u + 1))
            Pq = P.subs(x, q * x)
            Qq = Q.subs(x, q * x)
            E = sp.expand(
                (q ** 2 * x - 1) * Pq * P
                - (q - 1) * P * Qq
                - (q - 1) * Qq * Q
            )
            M = max(1 + 2 * p, p + u, 2 * u)
            top = sp.simplify(sp.expand(sp.Poly(E, x).coeff_monomial(x ** M)))
            # predicted: T1 alone if p >= u, else T3 alone
            want = (
                q ** (p + 2) * c[p] ** 2 if p >= u
                else -(q - 1) * q ** u * d[u] ** 2
            )
            ok = sp.simplify(top - want) == 0
            checked += 1
            if not ok:
                failures.append(f"(p={p},u={u}) top={top} want={want}")
    record(
        "T3_symbolic_riccati_top_coefficient",
        not failures,
        f"{checked} degree pairs (p,u <= {dmax}) expanded exactly over Q(q): the "
        "coefficient of the top power of x is q^(p+2)*lc(P)^2 (p>=u) or "
        "-(q-1)*q^u*lc(Q)^2 (p<u) -- a single nonzero monomial in each case, so it "
        "cannot vanish for q != 0,1 with lc(P),lc(Q) != 0. Hence NO rational "
        f"a = P/Q solves the q-Riccati. failures = {len(failures)}",
    )


# ---------------------------------------------------------------- T4
def t4_slope_half_corroboration(M: int = 160) -> None:
    """Independent corroboration of the slope, via its QUADRATIC coefficient.

    The naive statistic log_q|b_m|/m^2 does NOT converge to the slope at usable m,
    and reading its raw value as a failure would be an error of the test, not of
    the mathematics.  Peeling the recurrence two steps at a time,

        b_{m+2} ~ b_m / [m+2]_q ~ b_m * (q-1) * q^-(m+2)
        =>  log_q|b_m| = -m^2/4 + (m/2)*log_q(q-1) + O(1),

    so the statistic carries a SUB-LEADING LINEAR term (m/2)*log_q(q-1) that is
    large here: log_q(q-1)/2 = -10.6 at the proton q0, contributing -10.6/m ~
    -0.066 at m = 160 on top of the true -1/4.  Both the leading and sub-leading
    terms are PREDICTED above, so both are tested, and the leading one is tested
    by a statistic the linear term cannot reach:

        D2(m) = log_q|b_{m+2}| - 2 log_q|b_{m+1}| + log_q|b_m|  ->  2*(-1/4) = -1/2

    (second differences annihilate every affine term exactly).  D2 -> -1/2 is
    slope 1/2 (ramified, denominator 2, IRREDUCIBLE);  D2 -> -1 would be the
    integer slope 1, i.e. the reducible multiset {0,1} in which a scalar kernel
    WOULD exist.

    RAMIFICATION IS VISIBLE IN D2 AND MUST NOT BE TESTED AWAY.  Order-2
    ramification adds a PERIOD-2 term p(m) (p(m+1) = -p(m)) to log_q|b_m|, and
    second differences AMPLIFY it: D2(m) = -1/2 + 4p(m).  So D2 itself oscillates
    about -1/2 by an O(1) amount and converges to nothing.  That oscillation is
    the ramification -- the very fact that makes the slope non-integer -- so it is
    MEASURED here, not suppressed.  Two statistics are clean because both kill the
    period-2 term exactly:

        mean(D2(m), D2(m+1)) -> -1/2          (p cancels: +4p and -4p)
        D2_2(m) = lg b_{m+4} - 2 lg b_{m+2} + lg b_m -> -2   (step 2, never sees p)

    and the half-spread |D2(m) - D2(m+1)|/2 = 4|p(m)| is reported as the
    ramification AMPLITUDE: nonzero amplitude with mean -1/2 is the signature of
    slope 1/2; an unramified integer slope would give amplitude 0.
    """
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP

    q0 = Q_MP              # proton pin (AGENTS.md default)
    lnq = mp.log(q0)
    qint = lambda k: (q0 ** k - 1) / (q0 - 1)   # noqa: E731

    def run(b0: mp.mpf, b1: mp.mpf) -> list[mp.mpf]:
        b = [b0, b1]
        for m in range(M + 8):
            b.append((b[m + 1] + b[m]) / qint(m + 2))
        return b

    seeds = [
        ("basis (1,0)", mp.mpf(1), mp.mpf(0)),
        ("basis (0,1)", mp.mpf(0), mp.mpf(1)),
        ("mixed (1,-1)", mp.mpf(1), mp.mpf(-1)),
        ("mixed (3,7)", mp.mpf(3), mp.mpf(7)),
    ]
    lg = lambda v: mp.log(abs(v)) / lnq       # noqa: E731

    d2s: list[tuple[str, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
    for name, b0, b1 in seeds:
        b = run(b0, b1)
        m = M
        d2a = lg(b[m + 2]) - 2 * lg(b[m + 1]) + lg(b[m])
        d2b = lg(b[m + 3]) - 2 * lg(b[m + 2]) + lg(b[m + 1])
        d2_mean = (d2a + d2b) / 2                 # period-2 term cancels exactly
        ramif = abs(d2a - d2b) / 2                # = 4|p(m)|, the ramification
        d2_2 = lg(b[m + 4]) - 2 * lg(b[m + 2]) + lg(b[m])
        # sub-leading linear coefficient, recovered after removing -m^2/4
        lin = (lg(b[m]) + mp.mpf(m) ** 2 / 4) / m
        d2s.append((name, d2_mean, d2_2, lin, ramif))

    lin_pred = mp.log(q0 - 1) / lnq / 2       # = log_q(q-1)/2, the predicted slope
    worst_d2 = max(abs(d2 - mp.mpf(-1) / 2) for _, d2, _, _, _ in d2s)
    worst_d2_2 = max(abs(d - mp.mpf(-2)) for _, _, d, _, _ in d2s)
    worst_lin = max(abs(l - lin_pred) for _, _, _, l, _ in d2s)
    min_ramif = min(r for _, _, _, _, r in d2s)

    detail = "; ".join(
        f"{n}: mean(D2)={mp.nstr(a, 8)} D2_2={mp.nstr(bb, 8)} ramif={mp.nstr(r, 4)} "
        f"lin={mp.nstr(c, 6)}"
        for n, a, bb, c, r in d2s
    )
    ok = (
        worst_d2 < mp.mpf("1e-3")
        and worst_d2_2 < mp.mpf("1e-3")
        and worst_lin < mp.mpf("0.5")
        and min_ramif > mp.mpf("1e-3")        # ramification must be PRESENT
    )
    record(
        "T4_slope_one_half_corroboration",
        ok,
        f"m={M}, {mp.mp.dps} dps, proton q0. {detail} | targets mean(D2)=-1/2, "
        f"D2_2=-2 (slope 1/2, ramified) vs -1 / -4 (integer slope 1, reducible); "
        f"predicted sub-leading lin=log_q(q-1)/2={mp.nstr(lin_pred, 6)}. max dev: "
        f"mean(D2) {mp.nstr(worst_d2, 3)}, D2_2 {mp.nstr(worst_d2_2, 3)}, lin "
        f"{mp.nstr(worst_lin, 3)}; min ramification amplitude "
        f"{mp.nstr(min_ramif, 3)} (must be > 0). EVERY seed lands on -1/2 with a "
        "NONZERO period-2 amplitude: no solution has moderate (slope-0) growth, "
        "the multiset is NOT the integer pair {0,1}, and the ramification that "
        "makes the slope non-integer is directly observed. Corroboration only -- "
        "the proof is T2/T3, which needs no asymptotics.",
    )


# ---------------------------------------------------------------- T5
def t5_unconstrained_kernel_is_a_bijection(N: int = 14) -> None:
    """An UNCONSTRAINED scalar kernel constrains nothing: exact round-trip."""
    # arbitrary exact body terms, deliberately not from any model
    h = [Fraction(2, 3), Fraction(-5, 7), Fraction(11, 4), Fraction(1, 9)]
    while len(h) < N:
        k = len(h)
        h.append(Fraction((-1) ** k * (k * k + 3), 2 * k + 5))

    qv = Fraction(11, 10)  # exact rational q, not a root of unity in range
    # forward: solve for the kernel coefficients r_k of R = q^n0 (1 + sum r_k x^k)
    r: list[Fraction] = []
    for k in range(1, N):
        acc = (qv ** k - 1) * h[k]
        for j in range(1, k):
            acc -= r[j - 1] * h[k - j]
        r.append(acc / h[0])
    # backward: reconstruct the body terms from the kernel alone
    g = [h[0]]
    for k in range(1, N):
        acc = sum(r[j - 1] * g[k - j] for j in range(1, k + 1))
        g.append(acc / (qv ** k - 1))
    ok = all(g[i] == h[i] for i in range(N))
    record(
        "T5_unconstrained_kernel_bijection",
        ok,
        f"exact Fraction round-trip over {N} orders at q={qv}: an ARBITRARY body "
        "sequence determines a unique kernel and is exactly recovered from it. So "
        "with R unconstrained the ansatz G(qx)=R G(x) imposes ZERO constraints -- "
        "one new kernel coefficient per body order, a bijective reparametrisation, "
        "not a determination. All content sits in the finiteness of the Laurent "
        "window, which T2/T3 show is unattainable in the scalar form.",
    )


def main() -> int:
    print(__doc__.split("Run:")[0], flush=True)
    t1_operator_transcription()
    t2_degree_parity_core()
    t3_symbolic_riccati_no_solution()
    t4_slope_half_corroboration()
    t5_unconstrained_kernel_is_a_bijection()

    print("\n" + "=" * 72)
    ok = all(r[1] for r in RESULTS)
    for name, passed, _ in RESULTS:
        print(f"  {'PASS' if passed else 'FAIL':4}  {name}")
    print("=" * 72)
    print(
        "\nVERDICT (scope (b), structural exclusion; invariant: Newton slope 1/2 at\n"
        "infinity, equivalently the degree parity 2u-2p=1 being unsolvable over Z):\n"
        "  The q-Borel/Gevrey-normalized binding carrier -- the SURVIVOR of the\n"
        "  2026-07-20 §4 exclusion, and the carrier K named by\n"
        "  conj:qdifference-kernel-prolongation-symbol -- admits NO scalar kernel\n"
        "  R(q,x) in K(x), hence none in K[x,x^-1] of any depth d.  The rank-1 form\n"
        "  of prop:binding-genfun-qdifference is therefore unsatisfiable on BOTH\n"
        "  proposed carriers: raw (prior §4) and normalized (here).\n"
        "\nWHAT SURVIVES, and what it costs:\n"
        "  The carrier and the depth-2 prediction both stand.  'Depth 2' means RANK\n"
        "  2: the kernel is a 2x2 matrix A(q,x) acting on (G, sigma G), not a scalar.\n"
        "  Consequence: the closure needs TWO base cases, not one.  The claim that\n"
        "  the recurrence 'determines every body term from the deuteron base case'\n"
        "  is wrong by exactly one initial condition -- the genuine three-body n=3\n"
        "  term is independently required (bean qou-hh9q).\n"
        "  A scalar kernel returns only after a degree-2 RAMIFIED base change\n"
        "  (adjoining q^(1/2), x^(1/2)), where slope 1/2 becomes the integer 1; it\n"
        "  then relates half-shifts, i.e. even and odd body orders separately.\n"
        "  That ramification is the precise missing structure.\n"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
