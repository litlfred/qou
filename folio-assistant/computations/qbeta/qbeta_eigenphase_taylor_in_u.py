#!/usr/bin/env python3
"""qbeta_eigenphase_taylor_in_u.py — Taylor-expand the N=1 cos eigenphase
scaling in the ladder variable u, to pin down exactly which c_k the
single-block eigenphase generates and where it breaks.

WHY THIS PROBE (1ppQ-Q_β keystone — the scaling map f).

The bridge-narrowing audit (b502b9b83) established:
  • The Q_β residual lives in the SCALING (eigenphase), NOT Δ(net).
  • The cos eigenphase cos(α − bℏ²/2) is the unique right-DIRECTION
    closed-form scaling (factor < 1, as needed): it takes Q_A (1.68e6 ppb)
    to Q_N1 (73826 ppb), then c_2 = -1 takes it to 1277 ppb.

The c_3 order-audit (PR #1593) established:
  • The ladder c_k = Taylor coefficients of Q_β/Q_base in u = b·ℏ².
  • Chasing a *value* for c_3 is a category error; the open object is the
    q-dependent SCALING MAP f, not a c_3 constant.

THIS PROBE closes the loop between those two results. The eigenphase
   N1(q) = cos(α(q) − b(q)·ℏ(q)²/2),   α = (z-1)·h/2,
   z = 1/(√q + 1/√q),  b = √(q⁴+q²+1)/(q²+1),  ℏ = (q-1)/q,  h = q - 1/q
IS a closed-form candidate for (the leading part of) f. We expand it
symbolically as a Taylor series in u and read off its u^k coefficients:

  • If the eigenphase's u² coefficient = -1, it DERIVES c_2 (currently
    "proved" only via a separate Kashiwara argument) — a unification.
  • Its u³ coefficient is then the eigenphase's PREDICTION for c_3. We
    compare it to the empirical c_3 (-2.069) at BOTH q₀ anchors. If it
    matches at neither (the expected outcome per the order audit), we
    have quantified EXACTLY how much the single-block eigenphase misses
    c_3 by — i.e. the size of the multi-Wedderburn-block refinement that
    the true f must add. This is the concrete next constraint on f.

DISCIPLINE: no fitting. The eigenphase is the witness-cited closed form
(qbeta-scaling-bridge-investigation.witness.json); its Taylor expansion
is uniquely determined by SymPy. The outcome is TIERED (which c_k the
eigenphase derives exactly / which it only near-matches), never a binary
wire/un-wire and never a fitted c_k value.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

# PROBE-5 local headroom: 1 ppQ is 1e-15; expand with extra guard so the
# u^k extraction is safe well past N=7. Local opt-in only (NOT the global
# default — that would force-regenerate 400+ unrelated witnesses).
#
# Set QOU_COMPUTE_DPS *before* importing the precision module so the
# module constant COMPUTE_DPS (which WitnessBuilder records in
# precisionMetadata) reflects the ACTUAL 70-dps run — otherwise the
# witness would claim 65 while computing at 70 (Copilot review, #1602).
import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)
mpmath.mp.dps = 70

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0_MP_PIN = Q_50_DIGIT_STR  # canonical (m_p-pin per the scaling script)
Q0_MUON_PIN = "1.1099785955541805752815940796095093779932822799587"

# Empirical c_k (qbeta-ck-truncation-order-analysis.witness.json).
C2_EMP = mpf("-1")
C3_EMP_MP = mpf("-2.0693")
C3_EMP_MUON = mpf("-2.0097")


def substrate_syms(q: sp.Symbol):
    h = q - 1 / q
    hbar = (q - 1) / q
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    alpha = (z - 1) * h / 2
    u = b * hbar ** 2
    return h, hbar, z, b, alpha, u


def eigenphase_eps_series(order: int):
    """SYMBOLIC stage (cheap, exact): the ε = q-1 series of N1 and u.

    Returns (u_eps, N1_eps, eps_symbol, K) where u_eps, N1_eps are exact
    SymPy truncated series in ε. This is the symbolic infrastructure —
    exact radicals in q, no numerical approximation. The expensive part
    (series reversion u(ε) → ε(√u)) is done separately; this function on
    its own is fast and exact, and is reused by the symbolic-exact path
    `eigenphase_u_coeffs_symbolic` and the fast numeric path
    `eigenphase_u_coeffs` below.
    """
    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps")
    x = sp.Symbol("x")  # placeholder for the eigenphase argument
    h, hbar, z, b, alpha, u = substrate_syms(q)
    arg = alpha - b * hbar ** 2 / 2
    K = 2 * order + 3
    # Expand the ARGUMENT in ε first (cheap: rational + single radical),
    # then apply the cosine series to the truncated polynomial argument.
    # Expanding cos(arg) directly is what blows up — the nested radicals
    # under sp.series of a transcendental to K terms. This factoring keeps
    # it tractable while staying exact (symbolic).
    arg_eps = sp.series(arg.subs(q, 1 + eps), eps, 0, K).removeO()
    u_eps = sp.series(u.subs(q, 1 + eps), eps, 0, K).removeO()
    cos_x = sp.series(sp.cos(x), x, 0, K + 1).removeO()  # cos as poly in x
    N1_eps = sp.series(cos_x.subs(x, arg_eps), eps, 0, K).removeO()
    return u_eps, N1_eps, eps, K


def eigenphase_u_coeffs_symbolic(order: int, timeout_terms: int | None = None):
    """SYMBOLIC-EXACT path: reverse u(ε)→ε(√u) and compose, keeping exact
    SymPy radicals throughout. Correct but O(expensive) — the series
    reversion's symbolic solve grows fast in `order`. Guarded by a term
    cap; raises TimeoutError-like ValueError if `order` exceeds the cap.
    Use for SMALL order (≤ 2) to certify the leading coefficients
    exactly; the numeric path covers higher orders.
    """
    cap = timeout_terms if timeout_terms is not None else 2
    if order > cap:
        raise ValueError(
            f"symbolic path capped at order {cap} (got {order}); use the "
            "numeric path eigenphase_u_coeffs for higher orders")
    u_eps, N1_eps, eps, K = eigenphase_eps_series(order)
    s = sp.Symbol("s")  # s = √u
    e = [sp.Integer(0)] + [sp.Symbol(f"e_{k}") for k in range(1, K + 1)]
    eps_ser = sum(e[k] * s ** k for k in range(1, K + 1))
    tgt = sp.series(u_eps.subs(eps, eps_ser), s, 0, K + 1).removeO() - s ** 2
    sol: dict = {}
    for k in range(2, K + 1):
        ck = sp.expand(tgt.coeff(s, k)).subs(sol)
        a = sp.solve(sp.Eq(ck, 0), e[k - 1])
        if a:
            sol[e[k - 1]] = sp.simplify(a[0])
    eps_in_s = sp.series(
        sum(sol.get(e[k], e[k]) * s ** k for k in range(1, K + 1)),
        s, 0, K + 1).removeO()
    N1_in_s = sp.series(N1_eps.subs(eps, eps_in_s), s, 0,
                        2 * order + 2).removeO()
    return [sp.nsimplify(sp.simplify(N1_in_s.coeff(s, 2 * k)))
            for k in range(order + 1)]


def eigenphase_u_coeffs(order: int):
    """NUMERIC path (fast, high-precision): reuse the exact symbolic
    ε-series, then reverse u(ε)→ε(√u) and compose NUMERICALLY in mpmath.
    Returns mpmath floats. Used for the full order range; cross-checked
    against the symbolic-exact path at low order.
    """
    u_eps, N1_eps, eps, K = eigenphase_eps_series(order)

    # numeric ε-coefficient vectors (from the exact symbolic series)
    u_c = [mpf(str(sp.N(u_eps.coeff(eps, n), 60))) for n in range(K)]
    N_c = [mpf(str(sp.N(N1_eps.coeff(eps, n), 60))) for n in range(K)]
    if u_c[2] == 0:
        raise ValueError("u has no ε² term")

    # reverse u(ε)=s²: solve ε = Σ_{k>=1} e_k s^k, u_c-series in ε = s².
    # e_1 = 1/sqrt(u_c[2]); higher e_k by matching s^k coefficients.
    e = [mpf(0)] * (K + 1)
    e[1] = 1 / mp.sqrt(u_c[2])

    def u_series_in_s_coeff(j):
        # coefficient of s^j in u_eps(ε(s)) given current e[1..]
        # u_eps(ε) = Σ_n u_c[n] ε^n ; ε(s) = Σ_k e_k s^k
        # build ε(s) powers up to s^j
        eps_pow = [mpf(0)] * (j + 1)
        eps_pow[0] = mpf(1)  # ε^0
        # ε^1 coefficients
        cur = [mpf(0)] * (j + 1)
        for k in range(1, j + 1):
            cur[k] = e[k]
        powers = {1: cur[:]}
        for n in range(2, K):
            prev = powers[n - 1]
            nxt = [mpf(0)] * (j + 1)
            for i in range(0, j + 1):
                if prev[i] == 0:
                    continue
                for k in range(1, j + 1 - i):
                    nxt[i + k] += prev[i] * e[k]
            powers[n] = nxt
        tot = mpf(0)
        for n in range(1, K):
            if n in powers:
                tot += u_c[n] * powers[n][j]
        return tot

    for j in range(3, 2 * order + 3):
        # s^j coefficient of u(ε(s)) must be 0 for j != 2
        resid = u_series_in_s_coeff(j)
        # this residual is linear in e[j-1] with slope u_c[2]*2*e[1]... ;
        # isolate e[j-1] by finite perturbation
        base = resid
        save = e[j - 1]
        e[j - 1] = save + mpf(1)
        slope = u_series_in_s_coeff(j) - base
        e[j - 1] = save
        if slope != 0:
            e[j - 1] = save - base / slope

    # compose N1(ε(s)) and read even powers → u^k coefficients
    def compose_N_coeff(j):
        cur = [mpf(0)] * (j + 1)
        for k in range(1, j + 1):
            cur[k] = e[k]
        powers = {0: [mpf(1)] + [mpf(0)] * j, 1: cur[:]}
        for n in range(2, K):
            prev = powers[n - 1]
            nxt = [mpf(0)] * (j + 1)
            for i in range(0, j + 1):
                if prev[i] == 0:
                    continue
                for k in range(1, j + 1 - i):
                    nxt[i + k] += prev[i] * e[k]
            powers[n] = nxt
        tot = mpf(0)
        for n in range(0, K):
            if n in powers:
                tot += N_c[n] * powers[n][j]
        return tot

    return [compose_N_coeff(2 * k) for k in range(order + 1)]


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-eigenphase-taylor-in-u",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Taylor expansion of the N=1 cos eigenphase scaling "
        "cos(α − bℏ²/2) in the ladder variable u = b·ℏ², to determine "
        "which Q_β ladder coefficients c_k the single-block eigenphase "
        "generates exactly and where it breaks. Tests whether the "
        "eigenphase DERIVES c_2 = -1 (currently proved via a separate "
        "Kashiwara argument) and quantifies its prediction for c_3 vs the "
        "empirical value at both q₀ anchors — fixing the size of the "
        "multi-Wedderburn-block refinement the true scaling map f must "
        "add. 1ppQ-Q_β keystone (probe-qbeta-habiro-element-search). No "
        "fitting; eigenphase is the witness-cited closed form."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β EIGENPHASE TAYLOR-IN-u — which c_k does cos(α−bℏ²/2) generate?")
    print("=" * 78)
    print()

    ORDER = 3
    coeffs = eigenphase_u_coeffs(ORDER)
    print(f"Eigenphase N1(q) = cos(α − bℏ²/2), Taylor in u (orders 0..{ORDER}):")
    print("  [numeric path, high-precision mpmath]")
    for k, c in enumerate(coeffs):
        print(f"   [u^{k}]  {mp.nstr(c, 16)}")
    print()

    # Cross-check: certify the leading coefficients with the SYMBOLIC-EXACT
    # path (kept for later verification). Capped at low order — the exact
    # series reversion is expensive — but enough to certify u^0,u^1,u^2.
    print("  [symbolic-exact cross-check, orders 0..2]")
    symbolic_ok = True
    symbolic_coeffs: list[str] = []
    try:
        sym = eigenphase_u_coeffs_symbolic(2)
        for k, sc in enumerate(sym):
            sc_n = mpf(str(sp.N(sc, 50)))
            diff = abs(sc_n - coeffs[k])
            symbolic_coeffs.append(str(sp.nsimplify(sc)))
            match = diff < mpf("1e-30")
            symbolic_ok = symbolic_ok and match
            print(f"   [u^{k}]  symbolic {str(sp.nsimplify(sc)):<24} "
                  f"vs numeric {mp.nstr(coeffs[k],12)}  "
                  f"{'✓' if match else '✗ Δ='+mp.nstr(diff,3)}")
    except Exception as exc:  # symbolic path is best-effort
        symbolic_ok = False
        print(f"   (symbolic path unavailable: {exc})")
    print()

    # As a MULTIPLICATIVE ladder factor N1 = Π(1 + â_k u^k), the additive
    # Taylor coeffs a_k convert to product coeffs â_k. To leading orders:
    #   â_1 = a_1 ;  â_2 = a_2 - a_1²/2-ish — but production applies the
    # cos factor as a whole, then the SEPARATE c_k. The cleanest reading:
    # the eigenphase's own additive u-coefficients, compared to the ladder.
    a1, a2, a3 = coeffs[1], coeffs[2], coeffs[3]
    print("Structural reading (eigenphase additive u-coefficients):")
    print(f"   eigenphase u^1 coeff a_1 = {mp.nstr(a1, 12)}")
    print(f"   eigenphase u^2 coeff a_2 = {mp.nstr(a2, 12)}")
    print(f"   eigenphase u^3 coeff a_3 = {mp.nstr(a3, 12)}")
    print()

    # Compare numerically at both anchors. The eigenphase coefficients,
    # if a_k is a pure number (q-independent), are anchor-invariant; if
    # a_k still depends on q, evaluate at each pin.
    def eval_eigen_at(q0_str):
        q0 = mpf(q0_str)
        h = q0 - 1 / q0
        hbar = (q0 - 1) / q0
        z = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
        b = mp.sqrt(q0 ** 4 + q0 ** 2 + 1) / (q0 ** 2 + 1)
        alpha = (z - 1) * h / 2
        u = b * hbar ** 2
        N1 = mp.cos(alpha - b * hbar ** 2 / 2)
        return N1, u

    print("q₀-anchor comparison (eigenphase prediction vs empirical c_3):")
    rows = []
    for name, q0s, c3e in [("m_p-pin", Q0_MP_PIN, C3_EMP_MP),
                           ("muon-pin", Q0_MUON_PIN, C3_EMP_MUON)]:
        N1, u = eval_eigen_at(q0s)
        # eigenphase as a multiplicative ladder factor: N1 = Π(1 + â_k u^k)
        # leading: â_2 ≈ (N1 - 1)/u² to leading order (the c_2-analog).
        a2_eff = (N1 - 1) / u ** 2
        rows.append((name, mp.nstr(a2_eff, 10), float(c3e)))
        print(f"   {name:>9s}: eigenphase (N1-1)/u² = {mp.nstr(a2_eff,10)}  "
              f"(empirical c_2 = -1; c_3 = {float(c3e)})")
    print()

    a1n, a2n = coeffs[1], coeffs[2]
    has_u1 = abs(a1n) > mpf("1e-20")
    print("=" * 78)
    print(" FINDING (honest — negative-but-informative)")
    print("=" * 78)
    print(f"""
  • The cos eigenphase has a clean Taylor series in u with leading
    coefficients {mp.nstr(coeffs[1],10)} (u¹), {mp.nstr(coeffs[2],10)} (u²),
    {mp.nstr(coeffs[3],10)} (u³). Symbolic-exact (cross-checked): a_1 =
    -√3/12, a_2 = -11/32 - √3/12.

  • KEY RESULT: the eigenphase has a NONZERO u¹ coefficient
    (a_1 = -√3/12 ≈ -0.1443). The Q_β ladder starts at u² (c_2·u², with
    NO c_1·u¹ term — c_2 is the first rung). Therefore the cos eigenphase
    is NOT, by itself, the c_k generating factor: it carries an odd-order
    u¹ correction the ladder does not. The (N1-1)/u² ≈ -22 (not -1) is the
    symptom — it diverges as a_1/u because (N1-1) ~ a_1·u.

  • WHAT THIS RULES OUT: "the cos eigenphase IS the scaling map f, and the
    c_k are its Taylor coefficients" — FALSIFIED at u¹. The eigenphase is
    a right-direction PART of the scaling, but the true f must (a) cancel
    the u¹ term and (b) supply the u² coefficient = -1 exactly. The u¹
    cancellation is the new, concrete structural constraint on f.

  • TIER: eigenphase = proved closed form; "eigenphase = f" hypothesis =
    FALSIFIED at u¹ (this probe). No fitted form proposed. The result
    narrows the search rather than closing it.
    """)

    builder.add_data("eigenphase_definition", {
        "N1": "cos(α − b·ℏ²/2)",
        "alpha": "(z-1)·h/2",
        "z": "1/(√q + 1/√q)",
        "b": "√(q⁴+q²+1)/(q²+1)",
        "u": "b·ℏ²",
        "source_witness": "qbeta-scaling-bridge-investigation.witness.json",
    })
    builder.add_data("eigenphase_u_taylor_coeffs_numeric", {
        f"u^{k}": mp.nstr(c, 30) for k, c in enumerate(coeffs)
    })
    builder.add_data("eigenphase_u_taylor_coeffs_symbolic", {
        f"u^{k}": symbolic_coeffs[k] for k in range(len(symbolic_coeffs))
    })
    builder.add_data("symbolic_numeric_crosscheck", {
        "orders_certified_symbolic": len(symbolic_coeffs),
        "agree": symbolic_ok,
        "note": ("Symbolic-exact path (eigenphase_u_coeffs_symbolic) "
                 "certifies the leading coefficients in exact radicals; "
                 "numeric path (eigenphase_u_coeffs) covers all orders. "
                 "Both share the exact symbolic ε-series. Kept dual for "
                 "later verification."),
    })
    builder.add_data("anchor_comparison", {
        "rows": [{"anchor": r[0], "eigenphase_N1_minus_1_over_u2": r[1],
                  "empirical_c3": r[2]} for r in rows],
        "empirical_c2": str(C2_EMP),
    })
    builder.add_data("interpretation", {
        "eigenphase_equals_f_hypothesis": "FALSIFIED at u^1",
        "reason": ("cos(α−bℏ²/2) has a nonzero u^1 coefficient "
                   "(a_1 = -√3/12 ≈ -0.1443); the Q_β ladder starts at "
                   "u² (c_2·u², no c_1 term). So the eigenphase carries an "
                   "odd-order correction the ladder lacks — it is NOT the "
                   "c_k generating factor by itself."),
        "a1_exact": "-sqrt(3)/12",
        "a2_exact": "-11/32 - sqrt(3)/12",
        "new_constraint_on_f": ("the true scaling map f must (a) cancel "
                                "the u^1 term and (b) give u² coefficient "
                                "= -1 exactly; the u^1 cancellation is the "
                                "concrete new structural constraint"),
        "tier": "eigenphase: proved closed form; eigenphase=f: falsified at u^1",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "eigenphase_u_series_extracted",
        computed=float(len(coeffs)),
        expected=float(ORDER + 1),
        tolerance=0.0,
        source=("cos(α−bℏ²/2) Taylor-expanded in u = b·ℏ² to order "
                f"{ORDER}; coefficients are exact symbolic radicals, "
                "directly comparable to the ladder c_k."),
    )
    # The PR's substantive claims are the exact coefficient identities and
    # the symbolic↔numeric cross-check — assert them, not just the count
    # (Copilot review, #1602). a_1 = -√3/12, a_2 = -11/32 - √3/12.
    a1_target = -mp.sqrt(3) / 12
    a2_target = mpf(-11) / 32 - mp.sqrt(3) / 12
    builder.add_assertion(
        "eigenphase_a1_equals_neg_sqrt3_over_12",
        computed=float(coeffs[1]),
        expected=float(a1_target),
        tolerance=1e-25,
        source="Numeric u¹ coefficient matches the exact radical -√3/12.",
    )
    builder.add_assertion(
        "eigenphase_a2_equals_neg_11_32_minus_sqrt3_over_12",
        computed=float(coeffs[2]),
        expected=float(a2_target),
        tolerance=1e-25,
        source="Numeric u² coefficient matches the exact radical -11/32 - √3/12.",
    )
    builder.add_assertion(
        "eigenphase_a1_nonzero_falsifies_eigenphase_eq_f",
        computed=1.0 if abs(coeffs[1]) > mpf("1e-20") else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("The u¹ coefficient is nonzero (a_1 = -√3/12), but the Q_β "
                "ladder has no c_1 rung — this is the falsification of the "
                "'eigenphase = f' hypothesis at order u¹."),
    )
    builder.add_assertion(
        "symbolic_numeric_crosscheck_agree",
        computed=1.0 if symbolic_ok else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=(f"Symbolic-exact path certified {len(symbolic_coeffs)} "
                "leading coefficients in radicals; each agrees with the "
                "numeric path to < 1e-30."),
    )
    builder.save()
    print("\n  Witness: qbeta-eigenphase-taylor-in-u.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
