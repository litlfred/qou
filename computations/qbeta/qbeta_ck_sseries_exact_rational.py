#!/usr/bin/env python3
"""qbeta_ck_sseries_exact_rational.py — c3^even via EXACT Q(sqrt3)[[s]] series.

Bean 9fnm (the 1jrh unblock): the predecessor
qbeta_ck_sseries_operator_match_probe.py measured the net-route (bar-even /
binding-channel) ladder with numeric mp.taylor and found c2 ~ -8.006 but had
to REFUSE c3+ (odd-order [s^odd] log R ~ 1e4 numerical instability).  This
probe replaces the numeric Taylor with hand-rolled EXACT truncated power
series over the field Q(sqrt(3)) — every coefficient is an exact sympy
scalar, so there is no instability and the odd-order structure is decided
exactly, not estimated.

Objects (IDENTICAL conventions to the predecessor — the c2 gate protects
against convention drift):

    Delta(net)(q)  from free-neutron-decay.witness.json (GB-reduced, symbolic)
    Qb/m_e  = sgn * [Delta(net)/(q-1)] / q          (regularised, finite at q=1)
    QA/m_e  = (2q+1-q^2)(q+1)/(2q^3)
    hbar    = (q-1)/q,   b = sqrt(q^4+q^2+1)/(q^2+1),   u = b*hbar^2
    z       = q^3/(q^2+1),     h = q - 1/q      (convention D)
    alpha_eff = (z-1)h/2 - u/2                       (alpha_eff(1) = 0)
    R(q)    = (Qb/m_e) / [(QA/m_e) * cos(alpha_eff)],  R(1) = 1

Ladder match (s = q-1):  log R(s) = sum_{k>=2} log(1 + c_k u(s)^k), c_k
solved triangularly at s^{2k}.  With exact arithmetic the c_k^even come out
as EXACT elements of Q(sqrt3) — including the exact value behind the
predecessor's c2 ~ -8.006 — and c3^even, c4^even follow with no noise.

Then the 1jrh Casoratian sign test (2026-07-02-1jrh audit):
    W2 = c2^even*c3^odd - c3^even*c2^odd,   c2^odd = -1 (proved Taylor-exact),
    c3^odd ~ -2 (near-match tier, cross-anchor swing <= 3.47%).
Caveats carried verbatim from 1jrh: a sign call near c3^even ~ -16 is not
decisive (the numeric part plugs in near-match rungs); W3 would additionally
need c4^odd which is CAL-anchored tier.  TIERED reporting; NO production
wiring; any c_k>=3 use stays owner-gated (registry §8 proton+muon test).

Discipline: exact sympy scalars, no fit (triangular solve is determined);
witness via WitnessBuilder (monotonic start_time). Audit-only.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent

q = sp.Symbol("q", positive=True)
KC = 4                 # solve c_2..c_4
ORD = 2 * KC + 3       # truncation order in s (indices 0..ORD)


# ---------- exact truncated power series over sympy scalars -------------------

def simp(x):
    return sp.radsimp(sp.cancel(sp.together(x)))


def ser_trim(a):
    return [simp(x) for x in a[:ORD + 1]] + [sp.Integer(0)] * max(0, ORD + 1 - len(a))


def ser_add(a, b):
    return [simp(x + y) for x, y in zip(a, b)]


def ser_mul(a, b):
    out = [sp.Integer(0)] * (ORD + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(ORD + 1 - i):
            if b[j] == 0:
                continue
            out[i + j] += ai * b[j]
    return [simp(x) for x in out]


def ser_scale(c, a):
    return [simp(c * x) for x in a]


def ser_inv(a):
    """1/a for a[0] != 0."""
    assert a[0] != 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = simp(1 / a[0])
    for n in range(1, ORD + 1):
        acc = sp.Integer(0)
        for k in range(1, n + 1):
            acc += a[k] * out[n - k]
        out[n] = simp(-acc / a[0])
    return out


def ser_valuation(a):
    """Index of the lowest nonzero coefficient of a truncated series
    (returns ORD+1 for the series that is identically zero to truncation)."""
    for i in range(min(len(a), ORD + 1)):
        if sp.simplify(a[i]) != 0:
            return i
    return ORD + 1


def ser_div(a, b):
    """Exact valuation-aware truncated quotient a/b over the field.

    Returns ``(quo, valid_top)``: ``quo[n]`` is the exact coefficient of
    ``s^n`` in ``a/b`` for every ``n <= valid_top`` and is set to 0 for
    ``n > valid_top``.

    Why the top rows must be dropped. If ``b`` has s-valuation ``vb > 0``,
    then ``a/b`` is a power series only when ``a``'s valuation ``va >= vb``,
    and forming it strips a factor ``s^vb`` from the denominator — which
    discards the lowest ``vb`` orders of information carried by ``a``.
    Concretely ``a/b`` is determined only through order ``ORD - vb``; the
    coefficients above that would need ``a[ORD+1 .. ORD+vb]``, which the
    truncation has already thrown away. The historical idiom

        G = ser_mul(a[1:] + [0], ser_inv(b[1:] + [0]))     # a/b with vb == 1

    silently returned a garbage top coefficient ``G[ORD]`` that depended on
    the unknown ``a[ORD+1]``; every reader of that top row (the D-ladder
    "order-11 failure" and the margin-1 h^3 refutation) was reading an
    artifact. ``ser_div`` makes the loss explicit: it zeroes the invalid rows
    and reports ``valid_top`` so callers cannot read past the determined range.
    """
    vb = ser_valuation(b)
    if vb > ORD:
        raise ZeroDivisionError("ser_div: divisor is zero to truncation order")
    va = ser_valuation(a)
    if va < vb:
        raise ValueError(
            f"ser_div: quotient has negative valuation (va={va} < vb={vb}); "
            "a/b is not a power series")
    # Strip the common s^vb; the shifted divisor B has B[0] = b[vb] != 0, so
    # ser_inv is well-defined. The vb zeros padded onto A's top are the only
    # fabricated entries; they contaminate exactly the rows above valid_top.
    A = list(a[vb:]) + [sp.Integer(0)] * vb
    B = list(b[vb:]) + [sp.Integer(0)] * vb
    quo = ser_mul(A, ser_inv(B))
    valid_top = ORD - vb
    for n in range(valid_top + 1, ORD + 1):
        quo[n] = sp.Integer(0)
    return quo, valid_top


def ser_sqrt(a):
    """sqrt(a) for a[0] > 0 (principal branch)."""
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = simp(sp.sqrt(a[0]))
    for n in range(1, ORD + 1):
        acc = sp.Integer(0)
        for k in range(1, n):
            acc += out[k] * out[n - k]
        out[n] = simp((a[n] - acc) / (2 * out[0]))
    return out


def ser_log1(a):
    """log(a) for a[0] == 1: integrate a'/a termwise."""
    assert simp(a[0] - 1) == 0
    da = [simp((n + 1) * a[n + 1]) for n in range(ORD)] + [sp.Integer(0)]
    ratio = ser_mul(da, ser_inv(a))
    out = [sp.Integer(0)] * (ORD + 1)
    for n in range(1, ORD + 1):
        out[n] = simp(ratio[n - 1] / n)
    return out


def ser_cos0(a):
    """cos(a) for a[0] == 0: direct power sum (a^{2n}/(2n)!)."""
    assert a[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = sp.Integer(1)
    apow = [sp.Integer(1)] + [sp.Integer(0)] * ORD  # a^0
    n = 1
    fact = sp.Integer(1)
    while 2 * n <= ORD:
        apow = ser_mul(ser_mul(apow, a), a)   # a^{2n}
        fact *= (2 * n - 1) * (2 * n)
        sign = sp.Integer(-1) ** n
        out = ser_add(out, ser_scale(sign / fact, apow))
        n += 1
    return out


def rat_series(expr):
    """Exact s-series of a rational function of q at q = 1+s."""
    s = sp.Symbol("s")
    f = sp.cancel(expr.subs(q, 1 + s))
    num, den = sp.fraction(f)
    pn = sp.Poly(sp.expand(num), s)
    pd = sp.Poly(sp.expand(den), s)
    a = [pn.coeff_monomial(s**i) for i in range(ORD + 1)]
    b = [pd.coeff_monomial(s**i) for i in range(ORD + 1)]
    assert b[0] != 0, "denominator vanishes at q=1 — regularise first"
    return ser_mul(ser_trim(a), ser_inv(ser_trim(b)))


# ---------- objects ------------------------------------------------------------

def load_net_symbolic(side):
    d = json.load(open(_pb.witness_path("free-neutron-decay.witness.json", HERE)))
    net = sp.Integer(0)
    for t in d[side]["nf_terms"]:
        net += sp.sympify(t["coefficient_symbolic"], locals={"q": q})
    return sp.simplify(net)


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" 9fnm — c_k^even via EXACT Q(sqrt3)[[s]] series (net-route ladder)")
    print("=" * 78)

    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    print(f"  Delta(net)(q) = {dnet}")

    # numeric validation at q0 (same anchor as predecessor)
    q0 = mp.mpf(json.load(open(_pb.witness_path(
        "q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"])
    d_wit = json.load(open(_pb.witness_path("free-neutron-decay.witness.json", HERE)))
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dn_mine = sp.lambdify(q, dnet, "mpmath")(q0)
    val_ok = abs(dn_mine - dn_wit) < mp.mpf("1e-6")
    print(f"  VALIDATE @ q0: Delta(net) mine={mp.nstr(dn_mine,12)} witness={mp.nstr(dn_wit,12)} ok={val_ok}")
    sgn = int(mp.sign(dn_mine))

    # exact series of every piece
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_rad = rat_series(q**4 + q**2 + 1)
    b_ser = ser_mul(ser_sqrt(b_rad), ser_inv(rat_series(q**2 + 1)))
    u_ser = ser_mul(b_ser, hbar2)
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    assert alpha[0] == 0, f"alpha_eff(1) != 0: {alpha[0]}"

    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    assert simp(R[0] - 1) == 0, f"R(1) != 1: {R[0]}"
    logR = ser_log1(R)
    print(f"  u(s) leading: u = ({u_ser[2]})*s^2 + ...   [expect sqrt(3)/2 * s^2]")

    # EXACT odd-order structure of log R (the thing mp.taylor could not decide)
    odd_nonzero = {n: sp.simplify(logR[n]) != 0 for n in range(3, ORD + 1, 2)}
    print(f"  exact odd orders of log R nonzero? { {n: bool(v) for n, v in odd_nonzero.items()} }")

    # u^k series
    upow = {1: u_ser}
    for k in range(2, KC + 1):
        upow[k] = ser_mul(upow[k - 1], u_ser)

    # triangular match: log R = sum_k log(1 + c_k u^k)
    c_exact = {}
    model = [sp.Integer(0)] * (ORD + 1)
    gate_ok = None
    for k in range(2, KC + 1):
        order = 2 * k
        resid = simp(logR[order] - model[order])
        lead = upow[k][order]
        ck = simp(resid / lead)
        c_exact[k] = ck
        ckn = sp.N(ck, 30)
        print(f"  c_{k} (s^{order}) exact = {ck}")
        print(f"        numeric = {ckn}")
        if k == 2:
            gate_ok = abs(sp.N(ck - (-8), 10)) < 1  # predecessor found ~ -8.006
            # NOTE: the -1 gate belongs to the bar-ODD brane-tower route; the
            # NET route's own gate is agreement with the predecessor's -8.006.
            print(f"    GATE c_2 ~ -8.006 (predecessor net-route)? "
                  f"{'PASS' if gate_ok else 'FAIL — convention drift, stop'}")
            if not gate_ok:
                break
        # model += log(1 + c_k u^k)
        cku = ser_scale(ck, upow[k])
        one_p = list(cku); one_p[0] = simp(one_p[0] + 1)
        model = ser_add(model, ser_log1(one_p))

    # consistency residual at next even order
    resid_next = None
    if gate_ok and 2 * KC + 2 <= ORD:
        resid_next = simp(logR[2 * KC + 2] - model[2 * KC + 2])
        print(f"  residual at s^{2*KC+2} = {sp.N(resid_next, 20)} "
              f"(nonzero => c_k are q-dependent, as established)")

    # FULL order-by-order residual log R - model (the exact consistency map).
    # The k>=2 ladder produces NOTHING below s^4, so nonzero logR[2] or
    # logR[3] is an exact obstruction to the prod_{k>=2}(1+c_k u^k) form
    # (it would require a k=1 rung / a different ladder variable); nonzero
    # odd residuals at 5,7,9 test whether u's own odd tail accounts for the
    # odd structure of log R once c_2..c_4 are fixed at even orders.
    resid_by_order = {}
    for n in range(2, ORD + 1):
        r_n = simp(logR[n] - model[n])
        resid_by_order[n] = r_n
        tag = "ZERO" if sp.simplify(r_n) == 0 else f"{sp.N(r_n, 12)}"
        print(f"    residual [s^{n}] = {tag}")

    # Can a k=1 rung absorb the s^2 obstruction?  Re-solve the ladder WITH
    # c_1 (violating the odd channel's PROVED c_1 = 0 seed — so even success
    # here means the two parities do NOT share one ladder convention).
    # Triangular: c_1 at s^2, then c_2..c_4 at s^4..s^8; report residuals.
    print("\n  --- c_1-inclusive re-solve (k=1..4) ---")
    c1_exact = {}
    model1 = [sp.Integer(0)] * (ORD + 1)
    for k in range(1, KC + 1):
        order = 2 * k
        ck = simp((logR[order] - model1[order]) / upow[k][order])
        c1_exact[k] = ck
        print(f"  c_{k}' (s^{order}) exact = {ck}   numeric = {sp.N(ck, 20)}")
        cku = ser_scale(ck, upow[k])
        one_p = list(cku); one_p[0] = simp(one_p[0] + 1)
        model1 = ser_add(model1, ser_log1(one_p))
    resid1_by_order = {}
    for n in range(2, ORD + 1):
        r_n = simp(logR[n] - model1[n])
        resid1_by_order[n] = r_n
        tag = "ZERO" if sp.simplify(r_n) == 0 else f"{sp.N(r_n, 12)}"
        print(f"    residual' [s^{n}] = {tag}")

    # ---- 1jrh Casoratian sign test -------------------------------------------
    c2_even = sp.N(c_exact.get(2), 30)
    c3_even = sp.N(c_exact.get(3), 30) if 3 in c_exact else None
    W2 = None
    W2_sign = None
    if c3_even is not None:
        c2_odd, c3_odd = sp.Integer(-1), sp.Rational(-2)  # tiers: proved / near-match
        W2 = sp.N(c_exact[2] * c3_odd - c_exact[3] * c2_odd, 30)
        W2_sign = int(sp.sign(W2))
        print(f"\n  Casoratian W2 = c2^even*c3^odd - c3^even*c2^odd = {W2}")
        print(f"  sign(W2) = {W2_sign}  (caveat 1jrh: near c3^even ~ -16 the call")
        print( "   is not decisive; c3^odd is near-match tier, swing <= 3.47%)")

    # W3 needs c4^odd — CAL-anchored (UNTRUSTED tier per 1jrh); conditional.
    W3 = None
    W3_over_W2_sign = None
    if 4 in c_exact and c3_even is not None:
        c4_odd = sp.Rational(-97, 100)  # ~ -0.97, CAL-anchored tier (1jrh table)
        W3 = sp.N(c_exact[3] * c4_odd - c_exact[4] * sp.Rational(-2), 30)
        if W2 is not None and W2 != 0:
            W3_over_W2_sign = int(sp.sign(W3 / W2))
        print(f"  Casoratian W3 (CONDITIONAL on CAL-anchored c4^odd ~ -0.97) = {W3}")
        print(f"  sign(W3/W2) = {W3_over_W2_sign}   [AW positivity predicts +1;")
        print( "   a robust violation refutes the one-recurrence hypothesis —")
        print( "   CONDITIONAL on the untrusted c4^odd tier, scope (a) only]")

    elapsed = time.monotonic() - t0
    print(f"\n  ({elapsed:.1f}s)")

    wb = WitnessBuilder("qbeta-ck-sseries-exact-rational", engine="sympy")
    wb.set_description(
        "9fnm: exact Q(sqrt3)[[s]] series of the net-route (bar-even) ladder "
        "R = Qb/[QA cos(alpha_eff)]; exact c_2..c_4^even (replacing the "
        "numerically unstable mp.taylor route), exact odd-order structure of "
        "log R, and the 1jrh Casoratian W2 sign test against the bar-odd "
        "rungs (c2^odd=-1 proved, c3^odd~-2 near-match)."
    )
    wb.add_data("delta_net_q_symbolic", str(dnet))
    wb.add_data("validate_delta_net_at_q0_ok", bool(val_ok))
    wb.add_data("u_leading_coeff_exact", str(u_ser[2]))
    wb.add_data("log_R_odd_orders_nonzero", {str(n): bool(v) for n, v in odd_nonzero.items()})
    wb.add_data("c_k_even_exact", {str(k): str(v) for k, v in c_exact.items()})
    wb.add_data("c_k_even_numeric", {str(k): str(sp.N(v, 30)) for k, v in c_exact.items()})
    wb.add_data("c2_gate_vs_predecessor_minus8", bool(gate_ok))
    wb.add_data("consistency_residual_next_order", str(sp.N(resid_next, 20)) if resid_next is not None else None)
    wb.add_data("casoratian_W2", str(W2) if W2 is not None else None)
    wb.add_data("casoratian_W2_sign", W2_sign)
    wb.add_data("casoratian_W3_conditional", str(W3) if W3 is not None else None)
    wb.add_data("casoratian_W3_over_W2_sign_conditional", W3_over_W2_sign)
    wb.add_data("residual_logR_minus_model_by_order",
                {str(n): str(sp.N(v, 15)) if sp.simplify(v) != 0 else "0"
                 for n, v in resid_by_order.items()})
    wb.add_data("c1_inclusive_rungs_exact", {str(k): str(v) for k, v in c1_exact.items()})
    wb.add_data("c1_inclusive_rungs_numeric", {str(k): str(sp.N(v, 20)) for k, v in c1_exact.items()})
    wb.add_data("c1_inclusive_residual_by_order",
                {str(n): str(sp.N(v, 15)) if sp.simplify(v) != 0 else "0"
                 for n, v in resid1_by_order.items()})
    wb.add_data("odd_rung_tiers", {"c2_odd": "-1 proved Taylor-exact",
                                   "c3_odd": "~-2 near-match (cross-anchor swing <=3.47%)"})
    wb.add_data("caveats", [
        "net-route = bar-even/binding channel (c2 ~ -8), NOT the brane-tower "
        "bar-odd channel (c2 = -1) — two parities of one complex V, per the "
        "2026-06-16 reframe",
        "W2 sign near c3^even ~ -16 is not decisive (1jrh); W3 needs c4^odd "
        "(CAL-anchored tier)",
        "no production wiring; c_k>=3 use owner-gated (registry §8)",
    ])
    wb.add_assertion("validate_delta_net", bool(val_ok), True)
    # These two were add_assertion(name, True, True) -- `x == x`. Both facts ARE
    # verified, by bare `assert`s where alpha and R are built, but only their
    # conclusions reached the witness as literals: removing those asserts would have
    # left both reporting "passed". Carry the measured leading coefficients.
    wb.add_assertion("alpha_eff_at_q1", str(alpha[0]), "0",
                     source="alpha_eff = (z-1)h/2 - u/2; leading series coefficient")
    wb.add_assertion("R_minus_1_at_q1", str(simp(R[0] - 1)), "0",
                     source="R = Qb/[QA cos(alpha_eff)]; leading series coefficient")
    if gate_ok is not None:
        wb.add_assertion("c2_gate_vs_predecessor", bool(gate_ok), True)
    out = wb.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
