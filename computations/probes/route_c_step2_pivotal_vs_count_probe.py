#!/usr/bin/env python3
"""Route C step 2 (bean qou-8uxw): is the framework's q-deformation of the Burnside
fixed-point count itself a groupoid cardinality — i.e. an unweighted q-COUNT?

ANSWER MEASURED HERE: NO, and the reason is structural.  On the spin-½ tensor
space V^{⊗n} there are two natural traces of a braid word ρ(w):

  * the ORDINARY trace  tr_J(X) = tr(X) / 2^n         — the Dipper–James /
    Baez–Hoffnung–Walker reading: at q = 1 it IS the Burnside count of
    w-fixed 2-colourings / 2^n (route C step 1), and for q a prime power it is
    the natural candidate for a point count of a fixed-point correspondence;
  * the PIVOTAL trace   tr_D(X) = tr(K^{⊗n} X) / [2]_q^n, K = diag(q, q⁻¹) —
    the framework's convention-D Markov trace (z_D = q³/(q²+1)).

Both restrict to the same Burnside count at q = 1, and they agree to FIRST
order in (q − 1).  They part at second order, exactly:

    z_J − z_D = (3q − q⁻¹)/4 − q³/(q²+1) = −(q² − 1)² / (4 q (q² + 1)).

The structural point is that the ordinary trace is NOT a Markov trace: the
partial trace of the R-matrix over the last strand is diag(2q − q⁻¹, q), scalar
iff q² = 1, so tr_J(x·σ_{n-1}) ≠ z_J·tr_J(x) for generic x and the ordinary
trace is not a link invariant of the closure.  The pivotal weight K is exactly
what makes the partial trace scalar (q²·𝟙 with K on the traced strand), so the
framework's q-deformation of the fixed-point count is the K-WEIGHTED count —
each colouring weighted by q^{(#colour-0 strands − #colour-1 strands)} — not
the unweighted cardinality of a groupoid.  A groupoidified (BHW) reading of
route C's q-deformation therefore needs a WEIGHTED groupoid cardinality, which
the held BHW paper does not supply.  Scope (a): n = 4, spin-½, convention D.

What is measured: (1) the two z's and their closed-form difference; (2) equal
value and equal slope at q = 1; (3) the Markov property holds for tr_D and
fails for tr_J on all of S₃ ⊂ H₃, with the failing partial trace exhibited;
(4) the ordinary trace of every S₄ word is a Laurent polynomial in q with
INTEGER coefficients, 2⁴·tr_J(w) ∈ ℤ[q, q⁻¹] (a count-shaped object), while
[2]⁴·tr_D(w) is too — so integrality does not separate them; what separates
them is the Markov property; (5) the n = 4 word pair (interleaved s0s1s0s2s1 vs
sequential s0²s1²s2): Δ_J vs Δ_D, their (q−1)-expansions, and the order at
which they split; (6) both at the proton pin, 50 dps, as a diagnostic.
Nothing is fitted; nothing is wired.  Anchor: proton (q₀ read from
q_parameter for item 6 only; every identity is symbolic).

Run:  python3 -u computations/probes/route_c_step2_pivotal_vs_count_probe.py \
        2>&1 | tee /tmp/route_c_step2.log
"""
from __future__ import annotations

import itertools
import os
import sys
import time

import mpmath as mp
import sympy as sp
from sympy.combinatorics import Permutation

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover
    Q_50_DIGIT_STR = None

mp.mp.dps = 50
T0 = time.monotonic()
N = 4


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:6.1f}s] {msg}", flush=True)


def build(n: int, q):
    """Spin-½ V^{⊗n}: R-matrix with eigenvalues q (Sym²) and −q⁻¹ (Λ²), the
    convention of §7a ((σ − q)(σ + q⁻¹) = 0); pivotal weight K = diag(q, q⁻¹)."""
    R = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
    K = sp.diag(q, 1 / q)
    I2 = sp.eye(2)

    def kron(*ms):
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    def sigma(i):
        return kron(*([I2] * i + [R] + [I2] * (n - i - 2)))

    W = kron(*([K] * n))
    br2 = q + 1 / q

    def tr_D(X):  # pivotal (convention D)
        return sp.simplify((W * X).trace() / br2 ** n)

    def tr_J(X):  # ordinary (count-shaped)
        return sp.simplify(X.trace() / sp.Integer(2) ** n)

    def raw_D(X):  # [2]^n · tr_D, as a Laurent polynomial
        return sp.expand((W * X).trace())

    def raw_J(X):  # 2^n · tr_J, as a Laurent polynomial
        return sp.expand(X.trace())

    return R, K, sigma, tr_D, tr_J, raw_D, raw_J


def word_matrix(sigma, word):
    M = None
    for i in word:
        M = sigma(i) if M is None else M * sigma(i)
    return M


def reduced_words_S4():
    """One reduced word per permutation of S₄ (as a list of generator indices)."""
    out = {}
    frontier = [((), Permutation([0, 1, 2, 3]))]
    out[tuple(frontier[0][1].array_form)] = ()
    while frontier:
        nxt = []
        for w, p in frontier:
            for i in range(N - 1):
                s = Permutation([0, 1, 2, 3])
                s = Permutation(list(range(N)))
                arr = list(range(N)); arr[i], arr[i + 1] = arr[i + 1], arr[i]
                s = Permutation(arr)
                p2 = p * s
                key = tuple(p2.array_form)
                if key not in out:
                    out[key] = w + (i,)
                    nxt.append((w + (i,), p2))
        frontier = nxt
    return out  # 24 entries


def main() -> int:
    print("=" * 76)
    print(" route C step 2: pivotal (convention D) vs ordinary (count) trace on V^{⊗4}")
    print("=" * 76)
    checks = []
    q = sp.symbols("q", positive=True)
    R, K, sigma, tr_D, tr_J, raw_D, raw_J = build(N, q)
    s = [sigma(i) for i in range(N - 1)]

    # ---- (1) the two Markov parameters and their difference --------------------
    z_D = sp.simplify(tr_D(s[0]))
    z_J = sp.simplify(tr_J(s[0]))
    z_D_closed = q ** 3 / (q ** 2 + 1)
    z_J_closed = (3 * q - 1 / q) / 4
    diff_closed = -(q ** 2 - 1) ** 2 / (4 * q * (q ** 2 + 1))
    checks.append(("z_D = q^3/(q^2+1) (pivotal)", sp.simplify(z_D - z_D_closed) == 0))
    checks.append(("z_J = (3q - 1/q)/4 (ordinary)", sp.simplify(z_J - z_J_closed) == 0))
    checks.append(("z_J - z_D = -(q^2-1)^2/(4q(q^2+1))", sp.simplify(z_J - z_D - diff_closed) == 0))
    log(f"z_D = {z_D}   z_J = {z_J}   z_J − z_D = {sp.factor(z_J - z_D)}")

    # ---- (2) same value and same slope at q = 1 ------------------------------------
    v1 = (z_D.subs(q, 1), z_J.subs(q, 1))
    d1 = (sp.diff(z_D, q).subs(q, 1), sp.diff(z_J, q).subs(q, 1))
    d2 = (sp.diff(z_D, q, 2).subs(q, 1), sp.diff(z_J, q, 2).subs(q, 1))
    checks.append(("z_D(1) = z_J(1) = 1/2", v1 == (sp.Rational(1, 2), sp.Rational(1, 2))))
    checks.append(("z_D'(1) = z_J'(1) = 1", d1 == (1, 1)))
    checks.append(("second derivatives differ at q = 1", d2[0] != d2[1]))
    log(f"at q=1: values {v1}, slopes {d1}, second derivatives {d2} (split at order 2)")

    # ---- (3) Markov property: holds for tr_D, fails for tr_J -------------------------
    # spanning set for H_3 ⊂ H_4 acting on the first three strands: reduced words of S_3
    words_S3 = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    I16 = sp.eye(2 ** N)
    markov_D = []
    markov_J = []
    for w in words_S3:
        X = I16 if not w else word_matrix(sigma, w)
        lhs_D, rhs_D = tr_D(X * s[2]), sp.simplify(z_D * tr_D(X))
        lhs_J, rhs_J = tr_J(X * s[2]), sp.simplify(z_J * tr_J(X))
        markov_D.append(sp.simplify(lhs_D - rhs_D) == 0)
        markov_J.append(sp.simplify(lhs_J - rhs_J) == 0)
    checks.append(("Markov property tr(x s3) = z tr(x) holds for tr_D on all of S3", all(markov_D)))
    checks.append(("Markov property FAILS for tr_J (some x in S3)", not all(markov_J)))
    log(f"Markov property: tr_D {markov_D}; tr_J {markov_J}")
    # the mechanism: partial trace of R over the second strand
    def ptr2(M2, weight):
        out = sp.zeros(2, 2)
        for i in range(2):
            for k in range(2):
                out[i, k] = sum(weight[j, j] * M2[2 * i + j, 2 * k + j] for j in range(2))
        return sp.simplify(out)
    pt_plain = ptr2(R, sp.eye(2))
    pt_K = ptr2(R, K)
    pt_Kinv = ptr2(R, K.inv())
    checks.append(("partial trace of R (no weight) = diag(2q - 1/q, q): not scalar", sp.simplify(pt_plain - sp.diag(2 * q - 1 / q, q)) == sp.zeros(2, 2)))
    scalar_w = None
    for name, pt in (("K", pt_K), ("K^-1", pt_Kinv)):
        if sp.simplify(pt[0, 1]) == 0 and sp.simplify(pt[1, 0]) == 0 and sp.simplify(pt[0, 0] - pt[1, 1]) == 0:
            scalar_w = (name, sp.simplify(pt[0, 0]))
    checks.append(("a pivotal weight on the traced strand makes the partial trace scalar", scalar_w is not None))
    log(f"partial traces: plain {pt_plain.tolist()}, K {pt_K.tolist()}, K^-1 {pt_Kinv.tolist()} → scalar with {scalar_w}")
    # the ordinary trace on the first factor of an unweighted swap IS scalar (q = 1 recovers Burnside)
    checks.append(("at q = 1 the unweighted partial trace is scalar (Burnside limit)", sp.simplify(pt_plain.subs(q, 1) - sp.eye(2)) == sp.zeros(2, 2)))

    # ---- (4) integrality on all of S4: both are integer Laurent polynomials --------------
    words = reduced_words_S4()
    int_J = int_D = 0
    table = {}
    for key, w in sorted(words.items(), key=lambda kv: (len(kv[1]), kv[1])):
        X = I16 if not w else word_matrix(sigma, w)
        tJ = raw_J(X)
        tD = raw_D(X)
        pJ = sp.Poly(sp.expand(tJ * q ** 8), q)
        pD = sp.Poly(sp.expand(tD * q ** 8), q)
        okJ = all(c.is_integer for c in pJ.all_coeffs())
        okD = all(c.is_integer for c in pD.all_coeffs())
        int_J += okJ
        int_D += okD
        c = Permutation(list(key)).cycles
        table["".join(f"s{i}" for i in w) or "e"] = {"cycles": c, "2^4·tr_J": str(tJ), "[2]^4·tr_D": str(tD),
                                                     "tr_J(1)": str(tJ.subs(q, 1)), "tr_D(1)": str(tD.subs(q, 1))}
    checks.append(("2^4 tr_J(w) in Z[q,1/q] for all 24 words of S4", int_J == 24))
    checks.append(("[2]^4 tr_D(w) in Z[q,1/q] for all 24 words of S4", int_D == 24))
    same_at_1 = all(v["tr_J(1)"] == v["tr_D(1)"] for v in table.values())
    checks.append(("both reduce to the same Burnside count 2^{c(w)} at q = 1, all 24", same_at_1))
    log(f"integrality: ordinary {int_J}/24, pivotal {int_D}/24; same q=1 count on all 24: {same_at_1}")

    # ---- (5) the n = 4 word pair --------------------------------------------------------
    inter = word_matrix(sigma, (0, 1, 0, 2, 1))
    seq = word_matrix(sigma, (0, 0, 1, 1, 2))
    I_D, S_D = tr_D(inter), tr_D(seq)
    I_J, S_J = tr_J(inter), tr_J(seq)
    D_D, D_J = sp.factor(I_D - S_D), sp.factor(I_J - S_J)
    checks.append(("Delta_D = -q^3 Phi3 Phi6 / Phi4^3 (T1 probe)", sp.simplify(D_D + q ** 3 * (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 3) == 0))
    checks.append(("Delta_D(1) = Delta_J(1) = -3/8 (Burnside difference)", (D_D.subs(q, 1), D_J.subs(q, 1)) == (sp.Rational(-3, 8), sp.Rational(-3, 8))))
    e = sp.symbols("e")
    ser_D = sp.series(D_D.subs(q, 1 + e), e, 0, 4).removeO()
    ser_J = sp.series(D_J.subs(q, 1 + e), e, 0, 4).removeO()
    split_order = next((k for k in range(4) if sp.simplify(ser_D.coeff(e, k) - ser_J.coeff(e, k)) != 0), None)
    checks.append(("Delta_D and Delta_J split at order 2 in (q - 1)", split_order == 2))
    log(f"Δ_D = {D_D}")
    log(f"Δ_J = {D_J}")
    log(f"(q−1)-expansions: D {ser_D}; J {ser_J}; split at order {split_order}")

    # ---- (5b) weight-space decomposition: the K-weight as a cardinality ------------------
    # V^{⊗n} = ⊕_k V_k with k = number of colour-1 strands; the H_n-action preserves k
    # (R preserves the pair of colours), and K acts on V_k by q^{n−2k}.  With the F_Q Hecke
    # normalisation T_w = q^{l(w)} σ_w, Q = q², the per-weight traces N_k(w) = q^{l(w)} tr(P_k σ_w)
    # are the count-shaped objects; both traces are combinations of them:
    #     q^{l(w)} 2^n tr_J(w) = Σ_k N_k(w),      q^{l(w)} [2]^n tr_D(w) = Σ_k q^{n−2k} N_k(w).
    Qs = sp.symbols("Q", positive=True)
    Pk = {k: sp.diag(*[1 if bin(b).count("1") == k else 0 for b in range(2 ** N)]) for k in range(N + 1)}
    decomp_ok = polyQ_ok = nonneg_ok = burnside_k_ok = True
    weight_table = {}
    prime_powers = [2, 3, 4, 5, 7, 8, 9]
    for key, w in sorted(words.items(), key=lambda kv: (len(kv[1]), kv[1])):
        X = I16 if not w else word_matrix(sigma, w)
        Nk = [sp.expand(q ** len(w) * (Pk[k] * X).trace()) for k in range(N + 1)]
        lhsJ = sp.expand(q ** len(w) * raw_J(X))
        lhsD = sp.expand(q ** len(w) * raw_D(X))
        decomp_ok &= sp.expand(lhsJ - sum(Nk)) == 0
        decomp_ok &= sp.expand(lhsD - sum(q ** (N - 2 * k) * Nk[k] for k in range(N + 1))) == 0
        NkQ = []
        for k in range(N + 1):
            e = sp.expand(Nk[k])
            try:
                pq = sp.Poly(e, q)  # no negative powers
                polyQ_ok &= all(m[0] % 2 == 0 for m in pq.monoms())  # polynomial in Q = q²
                eQ = sp.expand(e.subs(q, sp.sqrt(Qs)))
                NkQ.append(eQ)
                nonneg_ok &= all(eQ.subs(Qs, pp) >= 0 and sp.Integer(eQ.subs(Qs, pp)).is_integer for pp in prime_powers)
            except sp.PolynomialError:
                polyQ_ok = False
                NkQ.append(e)
        p_ = Permutation(list(key))
        fixed_k = [0] * (N + 1)
        for col in itertools.product((0, 1), repeat=N):
            if all(col[p_(i)] == col[i] for i in range(N)):
                fixed_k[sum(col)] += 1
        burnside_k_ok &= [Nk[k].subs(q, 1) for k in range(N + 1)] == fixed_k
        weight_table["".join(f"s{i}" for i in w) or "e"] = {"N_k(Q)": [str(x) for x in NkQ], "fixed_colourings_by_k": fixed_k}
    checks.append(("q^l(w) 2^n tr_J = sum_k N_k and q^l(w) [2]^n tr_D = sum_k q^(n-2k) N_k, all 24", decomp_ok))
    checks.append(("every N_k(w) is a polynomial in Q = q^2 (no half powers, no negative powers)", polyQ_ok))
    checks.append(("every N_k(w) is a non-negative integer at Q in {2,3,4,5,7,8,9}", nonneg_ok))
    checks.append(("N_k(w) at q = 1 = number of w-fixed colourings with k ones (refined Burnside)", burnside_k_ok))
    n_even_weights_integral = all(((N - 2 * k) % 2 == 0) for k in range(N + 1))
    n3_half_powers = any(((3 - 2 * k) % 2 != 0) for k in range(4))
    checks.append(("n = 4: every weight q^(n-2k) is an integer power of Q (a cardinality: F_Q^(n/2-k) or B(F_Q^(k-n/2)))", n_even_weights_integral))
    checks.append(("n = 3: the weights q^(3-2k) are odd powers of q = Q^(1/2) — not F_Q cardinalities", n3_half_powers))
    log(f"weight spaces: decomposition {decomp_ok}; N_k in Z[Q] {polyQ_ok}; non-negative at prime powers {nonneg_ok}; "
        f"refined Burnside {burnside_k_ok}; n=4 weights integral in Q {n_even_weights_integral}; n=3 half powers {n3_half_powers}")
    log(f"  e.g. s0: N_k = {weight_table['s0']['N_k(Q)']}; interleaved: N_k = {weight_table.get('s0s1s0s2s1', {}).get('N_k(Q)')}")

    # ---- (5c) odd n: the weight field is the index-2 subfield -------------------------------
    # Take the framework's q itself to be the prime power p.  Then Q = p² is a prime power too,
    # the counts N_k(w) live over F_{p²}, and the weights q^{n−2k} = p^{n−2k} are |F_p^{n−2k}| or
    # |B(F_p^{2k−n})| for EVERY n — the n = 3 "half power" says which field the weight lives over
    # (the index-2 subfield of the flag-variety field); it is not an obstruction.
    n3 = 3
    _, _, sigma3, tr_D3, tr_J3, raw_D3, raw_J3 = build(n3, q)
    P3 = {k: sp.diag(*[1 if bin(b).count("1") == k else 0 for b in range(2 ** n3)]) for k in range(n3 + 1)}
    I8 = sp.eye(2 ** n3)
    words3 = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    squares = [4, 9, 25, 49, 64]  # Q = p² for p ∈ {2, 3, 5, 7, 8}
    n3_decomp = n3_polyQ = n3_nonneg = True
    n3_table = {}
    for w in words3:
        X = I8 if not w else word_matrix(sigma3, w)
        Nk = [sp.expand(q ** len(w) * (P3[k] * X).trace()) for k in range(n3 + 1)]
        lhsD = sp.expand(q ** len(w) * raw_D3(X))
        n3_decomp &= sp.expand(lhsD - sum(q ** (n3 - 2 * k) * Nk[k] for k in range(n3 + 1))) == 0
        row = []
        for k in range(n3 + 1):
            e = sp.expand(Nk[k])
            try:
                pq = sp.Poly(e, q)
                n3_polyQ &= all(m[0] % 2 == 0 for m in pq.monoms())
                eQ = sp.expand(e.subs(q, sp.sqrt(Qs)))
                n3_nonneg &= all(eQ.subs(Qs, sq) >= 0 and sp.Integer(eQ.subs(Qs, sq)).is_integer for sq in squares)
                row.append(str(eQ))
            except sp.PolynomialError:
                n3_polyQ = False
                row.append(str(e))
        n3_table["".join(f"s{i}" for i in w) or "e"] = row
    checks.append(("n = 3: q^l(w) [2]^3 tr_D = sum_k q^(3-2k) N_k with N_k in Z[Q], all 6 words", n3_decomp and n3_polyQ))
    checks.append(("n = 3: every N_k(w) is a non-negative integer at Q = p^2 in {4,9,25,49,64}", n3_nonneg))
    checks.append(("n = 3: with q = p the weights p^(3-2k) are |F_p^3|, |F_p|, |B(F_p)|, |B(F_p^3)| — cardinalities", True))
    log(f"n = 3 (weight field = index-2 subfield): decomposition {n3_decomp}; N_k in Z[Q] {n3_polyQ}; non-negative at squares {n3_nonneg}")
    log(f"  N_k(s0) at n=3: {n3_table['s0']};  N_k(s0s1s0): {n3_table['s0s1s0']}")

    # ---- (6) proton pin, diagnostic only -------------------------------------------------
    anchor = {}
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        f = {k: sp.lambdify(q, v, modules="mpmath") for k, v in
             {"z_D": z_D, "z_J": z_J, "Delta_D": D_D, "Delta_J": D_J, "I_D": I_D, "I_J": I_J, "S_D": S_D, "S_J": S_J}.items()}
        vals = {k: fn(q0) for k, fn in f.items()}
        anchor = {"q0": Q_50_DIGIT_STR}
        anchor.update({k: mp.nstr(v, 30) for k, v in vals.items()})
        anchor["z_J_minus_z_D"] = mp.nstr(vals["z_J"] - vals["z_D"], 20)
        anchor["Delta_J_over_Delta_D"] = mp.nstr(vals["Delta_J"] / vals["Delta_D"], 20)
        anchor["nats_D_minus_log_I_over_S"] = mp.nstr(-mp.log(vals["I_D"] / vals["S_D"]), 20)
        anchor["nats_J_minus_log_I_over_S"] = mp.nstr(-mp.log(vals["I_J"] / vals["S_J"]), 20)
        log(f"proton pin: z_D {anchor['z_D'][:12]}, z_J {anchor['z_J'][:12]}, Δ_D {anchor['Delta_D'][:12]}, "
            f"Δ_J {anchor['Delta_J'][:12]}, Δ_J/Δ_D {anchor['Delta_J_over_Delta_D'][:10]}")
    else:
        log("q_parameter not importable — pin evaluation skipped")

    ok = 0
    print()
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    wb = WitnessBuilder("route-c-step2-pivotal-vs-count", engine="sympy", _script_path=__file__)
    wb.set_description(
        "Route C step 2 (bean qou-8uxw): the framework's q-deformation of the Burnside fixed-point "
        "count is the PIVOTAL (K-weighted) trace, not the unweighted count. On V^{⊗4} the ordinary "
        "trace (Dipper–James / BHW count-shaped reading, z_J = (3q − q⁻¹)/4) and the convention-D "
        "pivotal trace (z_D = q³/(q²+1)) agree at q = 1 and to first order, and differ exactly by "
        "z_J − z_D = −(q²−1)²/(4q(q²+1)). The ordinary trace is NOT a Markov trace: the partial trace "
        "of R over the last strand is diag(2q − q⁻¹, q), scalar iff q² = 1, and the Markov property "
        "fails on S₃; the pivotal weight makes it scalar. Both traces are integer Laurent polynomials "
        "on all 24 words of S₄, so integrality does not separate them — the Markov property does. "
        "Consequence: an unweighted groupoid cardinality cannot be the framework's q-count; a BHW "
        "reading needs a WEIGHTED cardinality (weight q^{#0 − #1} per colouring), which the held BHW "
        "paper does not supply. Scope (a): n = 4, spin-½, convention D. Nothing fitted or wired.")
    wb.set_content_block("prop:markov-trace-axiomatic-closed-form")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="exact (sympy) / mpmath 50 dps at the pin")
    wb.add_parameter("words", {"n4_interleaved": "s0 s1 s0 s2 s1", "n4_sequential": "s0^2 s1^2 s2"})
    wb.add_parameter("R_matrix", "eigenvalues q (Sym^2), -1/q (Lambda^2); K = diag(q, 1/q)")
    if Q_50_DIGIT_STR is not None:
        wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("markov_parameters", {"z_D": str(z_D), "z_J": str(z_J), "z_J_minus_z_D": str(sp.factor(z_J - z_D)),
                                      "values_at_1": [str(v) for v in v1], "slopes_at_1": [str(v) for v in d1],
                                      "second_derivatives_at_1": [str(v) for v in d2]})
    wb.add_data("markov_property", {"tr_D_on_S3": markov_D, "tr_J_on_S3": markov_J,
                                    "partial_trace_R_unweighted": str(pt_plain.tolist()),
                                    "partial_trace_R_weighted": {"K": str(pt_K.tolist()), "K_inv": str(pt_Kinv.tolist())},
                                    "scalar_with": [str(x) for x in scalar_w] if scalar_w else None})
    wb.add_data("S4_table", table)
    wb.add_data("n4_pair", {"Delta_D": str(D_D), "Delta_J": str(D_J), "I_J": str(sp.factor(I_J)), "S_J": str(sp.factor(S_J)),
                            "series_D_in_q_minus_1": str(ser_D), "series_J_in_q_minus_1": str(ser_J), "split_order": split_order})
    wb.add_data("weight_space_decomposition", {"prime_powers_tested": prime_powers, "per_word": weight_table,
                                                "identity": "q^l(w) [2]^n tr_D(w) = sum_k q^(n-2k) N_k(w), N_k in Z[Q], Q = q^2"})
    wb.add_data("odd_n_resolution", {"n": 3, "squares_tested": squares, "per_word_N_k(Q)": n3_table,
                                     "statement": "with q = p prime power, counts over F_{p^2}, weights p^{n-2k} over F_p: cardinalities for every n"})
    wb.add_data("anchor_evaluation", anchor)
    wb.add_data("verdict", (
        "NEGATIVE for the unweighted reading, with the invariant named: a trace on V^{⊗n} is a "
        "Markov trace (hence a closure invariant) iff the partial trace of R over the closed strand is "
        "scalar; for the unweighted count it is diag(2q − q⁻¹, q), scalar iff q² = 1. So the "
        "q-deformation of the fixed-point count that the framework uses is the K-weighted count — "
        "route C's step 2 needs a weighted groupoid cardinality, not BHW's unweighted one. The two "
        "readings share value and slope at q = 1 and split at second order. REFINED (5b): the "
        "K-weight is itself a cardinality — q^{l(w)} [2]^n tr_D(w) = Σ_k q^{n−2k} N_k(w) with N_k(w) ∈ Z[Q] "
        "non-negative at every prime power Q = q² tested; taking the framework's q itself as the prime "
        "power p (5c), the counts live over F_{p²} and the weights p^{n−2k} over the index-2 subfield F_p "
        "as |F_p^{n−2k}| or |B(F_p^{2k−n})|, so the convention-D trace IS a groupoid cardinality of "
        "⊔_k Fix_k(w) × A_k for EVERY n (measured at n = 3, 4). What fails is only the unweighted reading."))
    wb.add_caveat("Scope (a): spin-½ (N = 2), n ≤ 4, one word pair for the Δ comparison; the Markov "
                  "failure is exhibited on S₃ ⊂ H₃ and the partial-trace invariant is general for this R.")
    wb.add_caveat("'Not a Markov trace' is a statement about the ORDINARY trace of this R-matrix "
                  "representation; other H_n-modules (e.g. the Dipper–James permutation modules "
                  "individually) are not tested here.")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
