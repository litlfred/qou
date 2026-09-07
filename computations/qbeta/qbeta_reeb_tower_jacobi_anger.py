#!/usr/bin/env python3
"""qbeta_reeb_tower_jacobi_anger.py
==================================

Make the scope-doc's "Bessel-like" tag precise, and run the falsifiable
structural test it implies.

The Q_β `c_3` residue-A scope doc
(`docs/scope/2026-06-05-qbeta-perblock-collapse-order-scope.md`) calls the
observe-last sum `Σ_λ y_λ |sinh(k_λ η)|` *"(Bessel-like)"* — "a weighted sum
of different-order sinhs whose effective order is η-dependent, with no single
ℓ to anchor-lock." This script shows that intuition is EXACT: with `q = e^η`,
the **bar-graded Jacobi–Anger identity** is

    cosh(x·sinh η) = J₀(x) + 2 Σ_{m≥1} J_{2m}(x) cosh(2mη)     (bar-EVEN, c_2)
    sinh(x·sinh η) = 2 Σ_{m≥0} J_{2m+1}(x) sinh((2m+1)η)       (bar-ODD,  c_3)

— the bar-odd generating function expands in ODD-order sinh only, with
ORDINARY Bessel weights `J_{2m+1}(x)`. That is the precise content of
"different-order sinhs, η-dependent effective order, no single ℓ".

What the script proves / tests (TIERED, no fit, nothing wired):

  (A) PROVED (numeric, 50 dps): the generating function `e^{x sinh η} =
      Σ_n J_n(x) e^{nη}` and both boxed identities, to < 1e-40 residual.
  (B) PROVED (numeric): the rotation/growth = J_ν/I_ν unification,
      `I_ν(x) = i^{-ν} J_ν(i x)` — the analytic continuation `η ↦ iη`
      (arccosh ↔ arccos) that the binding probe's rotation/growth split
      (`binding_reeb_phase_decomposition.py`, acos vs acosh) realises.
  (C) STRUCTURAL TEST of the n=3 bar-odd character spectra (the canonical
      H₃(q) β-transition characters χ_(3), χ_(2,1), χ_(1,1,1)) against a
      single-x `sinh(x sinh η)` Bessel profile:
        • parity-of-order test: are only ODD sinh-orders present?
        • single-x over-determination: do the odd-order coefficient ratios
          fix ONE x (Bessel) or not?

Honest expectation for (C): the per-block spectra are PURE ODD-ORDER (the
sinh(x sinh η) STRUCTURE), but each finite 2–3-term block does NOT collapse
to a single-x Bessel profile — confirming the audit caveat that the Bessel
object is the brane-TOWER / contraction limit, not the n=3 trace itself
(docs/audits/2026-06-13-reeb-phase-qbessel-identification.md §1).

# Ref: [koelink1994] https://doi.org/10.1215/S0012-7094-94-07617-0
# Ref: [gasper-rahman-2004] https://doi.org/10.1017/CBO9780511526251
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp
from mpmath import mp, mpf, mpc, sinh, cosh, besselj, besseli, fabs, findroot

# Canonical H₃(q) β-transition per-block characters χ_λ(Δ_T_β)(q).
# Closed forms are the single source of truth in qbeta_utils (mirrored from
# QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean). Import if available; else
# inline the identical closed forms so the script is standalone-runnable.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
try:
    from qbeta_utils import chi_block_3, chi_block_21, chi_block_111  # type: ignore
    _CHI_SOURCE = "qbeta_utils (canonical)"
except ImportError:  # pragma: no cover - portability fallback
    def chi_block_3(q):
        return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q)

    def chi_block_21(q):
        # Canonical BORROMEAN intra-nucleon ordering (beans qou-hu1f/qou-eddc,
        # 2026-09-07). This is the one block the ordering reaches; the other two
        # are 1-dimensional and provably unmoved. Keep in step with qbeta_utils.
        P = (2 * q ** 12 - 5 * q ** 10 + 5 * q ** 8 - 5 * q ** 6
             + 5 * q ** 4 - 5 * q ** 2 + 2)
        return (q ** 2 - 1) * (q ** 4 + 1) * P / (4 * q ** 9)

    def chi_block_111(q):
        return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q ** 5)

    _CHI_SOURCE = "inline fallback (identical closed forms)"

mp.dps = 60
I_UNIT = mpc(0, 1)

# `_precision` lives in `computations/substrate/`, and this file sits in the
# `qbeta/` cluster, so `sys.path[0]` is its own directory and a bare
# `from _precision import fmt` raises ModuleNotFoundError (the `_path_bridge`
# bootstrap class, bean `qou-0e1t`). This file already walks up to `substrate/`
# — at the very BOTTOM, just before it writes the witness. `fmt` is needed at
# results-assembly time, so the walk is hoisted here and the one below reuses
# the same already-inserted path.
import os as _os_boot, sys as _sys_boot  # noqa: E402
_d_boot = _os_boot.path.dirname(_os_boot.path.abspath(__file__))
while (_d_boot != _os_boot.path.dirname(_d_boot)
       and not _os_boot.path.isdir(_os_boot.path.join(_d_boot, "substrate"))):
    _d_boot = _os_boot.path.dirname(_d_boot)
_sys_boot.path.insert(0, _os_boot.path.join(_d_boot, "substrate"))
from _precision import fmt  # noqa: E402


def _fmt_or_none(v):
    """`fmt` an mpf, pass `None` through.

    The four fields this renders are legitimately `None` when the fit does not
    run, and that `None` is meaningful — it is not the same as a residual of
    zero.
    """
    return fmt(v) if v is not None else None


results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ───────────────────────────────────────────────────────────────────────
# (A) The bar-graded Jacobi–Anger identity (numeric, 50 dps)
# ───────────────────────────────────────────────────────────────────────
print("(A) bar-graded Jacobi–Anger identity  (q = e^η)")
M = 40  # truncation order; J_n(x) decays super-exponentially in n
test_pts = [(mpf("0.7"), mpf("0.31")), (mpf("1.3"), mpf("-0.45")),
            (mpf("2.1"), mpf("0.62"))]  # (x, η)

max_gen = max_odd = max_even = mpf(0)
for x, eta in test_pts:
    # generating function  e^{x sinh η} = Σ_n J_n(x) e^{nη}
    # (sum to ±2M so the truncation order matches the bar-odd/even loops, which
    #  reach order 2M−1; the e^{nη} factor converges slower than sinh((2m+1)η))
    gen = sum(besselj(n, x) * mp.exp(n * eta) for n in range(-2 * M, 2 * M + 1))
    max_gen = max(max_gen, fabs(gen - mp.exp(x * sinh(eta))))
    # bar-ODD:  sinh(x sinh η) = 2 Σ_{m≥0} J_{2m+1}(x) sinh((2m+1)η)
    odd = 2 * sum(besselj(2 * m + 1, x) * sinh((2 * m + 1) * eta)
                  for m in range(0, M))
    max_odd = max(max_odd, fabs(odd - sinh(x * sinh(eta))))
    # bar-EVEN: cosh(x sinh η) = J₀(x) + 2 Σ_{m≥1} J_{2m}(x) cosh(2mη)
    even = besselj(0, x) + 2 * sum(besselj(2 * m, x) * cosh(2 * m * eta)
                                   for m in range(1, M))
    max_even = max(max_even, fabs(even - cosh(x * sinh(eta))))

check("generating fn  e^{x sinh η} = Σ_n J_n(x) e^{nη}  (resid < 1e-40)",
      max_gen < mpf("1e-40"))
check("bar-ODD  sinh(x sinh η) = 2 Σ J_{2m+1} sinh((2m+1)η)  (resid < 1e-40)",
      max_odd < mpf("1e-40"))
check("bar-EVEN cosh(x sinh η) = J₀ + 2 Σ J_{2m} cosh(2mη)  (resid < 1e-40)",
      max_even < mpf("1e-40"))
results["jacobi_anger"] = {
    "identity_bar_odd": "sinh(x sinh η) = 2 Σ_{m≥0} J_{2m+1}(x) sinh((2m+1)η)",
    "identity_bar_even": "cosh(x sinh η) = J₀(x) + 2 Σ_{m≥1} J_{2m}(x) cosh(2mη)",
    # `float()` here floored the very numbers the VERDICT quotes as "<1e-40" —
    # a residual asserted below 1e-40 cannot be recorded in f64 and mean it.
    "max_residual_gen": fmt(max_gen),
    "max_residual_bar_odd": fmt(max_odd),
    "max_residual_bar_even": fmt(max_even),
    "truncation_M": M,
}


# ───────────────────────────────────────────────────────────────────────
# (B) rotation/growth = J_ν / I_ν   (I_ν(x) = i^{-ν} J_ν(i x))
# ───────────────────────────────────────────────────────────────────────
print("(B) rotation/growth = J_ν / I_ν  via  I_ν(x) = i^{-ν} J_ν(i x)")
max_JI = mpf(0)
for nu in range(0, 6):
    for x in [mpf("0.5"), mpf("1.7"), mpf("3.3")]:
        lhs = besseli(nu, x)
        rhs = I_UNIT ** (-nu) * besselj(nu, I_UNIT * x)
        max_JI = max(max_JI, fabs(lhs - rhs))
check("I_ν(x) = i^{-ν} J_ν(i x) for ν=0..5  (resid < 1e-40)",
      max_JI < mpf("1e-40"))
# the regime cut: J_ν is the bounded/rotation (|t|≤1, cos / arccos) world;
# I_ν the unbounded/growth (t≥1, cosh / arccosh) world. Same recurrence.
results["rotation_growth_JI"] = {
    "continuation": "I_ν(x) = i^{-ν} J_ν(i x)  (η ↦ iη)",
    "max_residual": float(max_JI),
    "rotation_channel": "J_ν: bounded, |χ/dim|≤1, θ=arccos (cos regime)",
    "growth_channel": "I_ν: unbounded, |χ/dim|>1, θ=arccosh (cosh regime)",
}


# ───────────────────────────────────────────────────────────────────────
# (C) structural test of the n=3 bar-odd character spectra
# ───────────────────────────────────────────────────────────────────────
print("(C) n=3 bar-odd character spectra vs single-x sinh(x sinh η) profile")
q = sp.symbols("q", positive=True)
blocks = {
    "(3)": chi_block_3(q),
    "(2,1)": chi_block_21(q),
    "(1,1,1)": chi_block_111(q),
}


def sinh_order_coeffs(expr) -> dict[int, sp.Rational]:
    """Bar-odd part of a Laurent polynomial χ(q), expanded as Σ_k a_k sinh(kη).

    bar_odd = (χ(q) − χ(1/q))/2 = Σ_k a_k (q^k − q^{-k})/2, so a_k = 2·[q^k].

    The shift needed to turn the Laurent polynomial into a genuine one is read
    off the expression rather than hardcoded. It used to be a literal `q**5`,
    which was right for the grouped-frame characters (|k| ≤ 5) and raised
    `PolynomialError` the moment the canonical borromean χ_(2,1) arrived with
    q⁻⁹ in it (beans qou-hu1f / qou-eddc). Failing loudly was the correct
    behaviour; hardcoding a wider literal instead would just move the wall.
    """
    bar_odd = sp.cancel(sp.together(sp.expand((expr - expr.subs(q, 1 / q)) / 2)))
    num, den = sp.fraction(bar_odd)
    den_poly = sp.Poly(den, q)
    if len(den_poly.monoms()) != 1:
        raise ValueError(
            f"bar-odd denominator is not a monomial in q: {den}. This routine "
            "reads a_k off a Laurent polynomial and cannot handle a genuine "
            "rational function.")
    shift = den_poly.degree()
    scale = den_poly.LC()
    P = sp.Poly(sp.expand(num / scale), q)
    out: dict[int, sp.Rational] = {}
    for k in range(1, P.degree() - shift + 1):
        c = P.coeff_monomial(q ** (shift + k))
        if c != 0:
            out[k] = 2 * c
    return out


all_orders_odd = True
spectra: dict = {}
combined: dict[int, sp.Expr] = {}
for name, chi in blocks.items():
    a = sinh_order_coeffs(chi)
    orders = sorted(a.keys())
    only_odd = all(k % 2 == 1 for k in orders)
    all_orders_odd = all_orders_odd and only_odd
    for k, v in a.items():
        combined[k] = combined.get(k, sp.Integer(0)) + v
    spectra[name] = {
        "orders_present": orders,
        "coeffs": {str(k): str(v) for k, v in a.items()},
        "only_odd_orders": only_odd,
    }
    print(f"  χ_{name}: orders {orders}  coeffs "
          f"{ {k: str(v) for k, v in a.items()} }  only_odd={only_odd}")

check("parity-of-order: every n=3 bar-odd block has ONLY odd sinh-orders "
      "(consistent with sinh(x sinh η) structure)", all_orders_odd)

# Over-determination needs ≥3 orders. In the grouped frame no single block had
# 3 (each carried 2), so only the unit-weighted SUM was falsifiable, at exactly
# {1,3,5}. Under the canonical borromean ordering χ_(2,1) carries {1,3,5,7,9}
# on its own, so the sum reaches order 9 and the ordering-dependent block is now
# individually over-determined — tested separately below. Both are bar-odd
# truncations, NOT the physical Wenzl-weighted Markov trace.
comb_orders = sorted(k for k, v in combined.items() if v != 0)
print(f"  unit-weighted block sum: orders {comb_orders}  coeffs "
      f"{ {k: str(combined[k]) for k in comb_orders} }")
single_x_resid = None
single_x_star = None
if {1, 3, 5} <= set(comb_orders):
    a1 = mpf(str(combined[1].evalf(60)))
    a3 = mpf(str(combined[3].evalf(60)))
    a5 = mpf(str(combined[5].evalf(60)))
    # solve a1·J_3(x) = a3·J_1(x) for x, then test the over-determined a_5/a_1
    xb = findroot(lambda xx: a1 * besselj(3, xx) - a3 * besselj(1, xx),
                  mpf("4.5"))
    single_x_star = xb
    pred = besselj(5, xb) / besselj(1, xb)
    act = a5 / a1
    single_x_resid = fabs(pred - act)
    print(f"  single-x fit: x* = {float(single_x_star):.6f}  "
          f"J_5/J_1 predicted = {float(pred):.6f}  actual = {float(act):.6f}  "
          f"residual = {float(single_x_resid):.4f}")

check(f"single-x Bessel over-determination FAILS on the "
      f"{len(comb_orders)}-order unit-weighted truncation "
      "(residual ≫ 0 ⇒ Bessel object is the tower / contraction limit, not "
      "the n=3 trace)",
      single_x_resid is not None and single_x_resid > 1e-3)

# The canonical χ_(2,1) alone now carries {1,3,5,7,9}, so the same falsification
# runs on the single ordering-dependent block — a test the grouped frame could
# not support, because there that block carried only two orders and any
# (amplitude, x) fitted it exactly. Fitting x on (a_1, a_3) and predicting
# a_5/a_1 is the same protocol as above, on a block rather than a sum.
block21_resid = None
block21_star = None
b21 = spectra["(2,1)"]
if {1, 3, 5} <= set(b21["orders_present"]):
    c = {k: mpf(str(sp.Rational(b21["coeffs"][str(k)]).evalf(60)))
         for k in (1, 3, 5)}
    xb2 = findroot(lambda xx: c[1] * besselj(3, xx) - c[3] * besselj(1, xx),
                   mpf("4.5"))
    block21_star = xb2
    pred2 = besselj(5, xb2) / besselj(1, xb2)
    block21_resid = fabs(pred2 - c[5] / c[1])
    print(f"  χ_(2,1) alone: x* = {float(block21_star):.6f}  "
          f"J_5/J_1 predicted = {float(pred2):.6f}  "
          f"actual = {float(c[5] / c[1]):.6f}  residual = {float(block21_resid):.4f}")
check("single-x Bessel over-determination ALSO fails on the canonical χ_(2,1) "
      "block alone (newly testable: the borromean form carries 5 odd orders "
      "where the grouped form carried 2)",
      block21_resid is not None and block21_resid > 1e-3)

results["n3_bar_odd_spectra"] = {
    "per_block": spectra,
    "unit_weighted_sum_orders": comb_orders,
    "unit_weighted_sum_coeffs": {str(k): str(combined[k]) for k in comb_orders},
    # `float()` stood on all four of these where they are BUILT (the `xb` /
    # `fabs(...)` lines above). They are an over-determination residual and the
    # x* it is measured at -- the numbers this probe reports -- so they are
    # carried as mpf and rendered here.
    "block_21_single_x_star": _fmt_or_none(block21_star),
    "block_21_over_determination_residual": _fmt_or_none(block21_resid),
    "single_x_star": _fmt_or_none(single_x_star),
    "single_x_over_determination_residual": _fmt_or_none(single_x_resid),
    "intra_nucleon_ordering": "borromean",
    "note": "Both truncations here are bar-odd, NOT the physical "
            "Wenzl-weighted Markov trace. Under the canonical borromean "
            "ordering the unit-weighted sum carries {1,3,5,7,9} and chi_(2,1) "
            "carries the same five orders on its own; in the superseded "
            "grouped frame the sum carried exactly {1,3,5} and no single block "
            "carried more than two, so only the sum was falsifiable.",
}
results["chi_source"] = _CHI_SOURCE


# ───────────────────────────────────────────────────────────────────────
verdict = (
    "JACOBI-ANGER + J/I PROVED (numeric, <1e-40). The n=3 bar-odd character "
    "spectra are PURE ODD-ORDER (the sinh(x sinh η) structure) — which under the "
    "canonical borromean ordering now holds out to order 9, where the grouped "
    "frame only reached 5, and did not have to. But neither the unit-weighted "
    "sum nor the canonical χ_(2,1) block alone matches a single-x Bessel profile "
    "(over-determination fails on both) — confirming the Bessel object is the "
    "brane-tower / SU_q(2)→E_q(2) contraction limit, not the n=3 trace. "
    "No fit; nothing wired; c_3 cal-anchored."
)
print("\nVERDICT:", verdict)

ok = all(v for _, v in asserts)
witness = {
    "computation": "qbeta_reeb_tower_jacobi_anger",
    "description": (
        "Bar-graded Jacobi–Anger identity making the scope-doc 'Bessel-like' tag "
        "precise (sinh(x sinh η)=2 Σ J_{2m+1} sinh((2m+1)η)); the rotation/growth "
        "= J_ν/I_ν continuation; and a falsifiable structural test of the n=3 "
        "bar-odd H₃(q) character spectra against a single-x Bessel profile. "
        "Q_β c_3 residue-A; docs/audits/2026-06-13-reeb-phase-qbessel-identification.md."
    ),
    "discipline": "no fit; derive-or-refute; TIERED; c_3 cal-anchored; nothing wired",
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok_ for name, ok_ in asserts},
    "allPassed": ok,
    "verdict": verdict,
}
out = pathlib.Path(__file__).with_name("qbeta-reeb-tower-jacobi-anger.witness.json")
import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_d = _os.path.dirname(_os.path.abspath(__file__))
while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
    _d = _os.path.dirname(_d)
_sys.path.insert(0, _os.path.join(_d, "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = _os.path.basename(__file__)
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
print(f"\nallPassed={ok}; witness → {out.name}")
raise SystemExit(0 if ok else 1)
