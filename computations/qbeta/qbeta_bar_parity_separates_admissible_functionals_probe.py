#!/usr/bin/env python3
"""The bar involution separates the admissible Q_beta functionals from the
inadmissible ones — and the published one fails on the same side as convention C.

CONTEXT. `2026-09-05-qbeta-functional-decision-options.md` (qou-99qc) lays out
seven options for which linear functional `eps` evaluates `Delta = B_n - B_p`.
Three cells of the `Delta_S` column are measured there as NUMBERS:

    z = 1   (published)      +0.16775687 %     INADMISSIBLE under convention D
    z = q   (augmentation)   +12.470022  %     admissible
    z_D     (Markov, D)      -43.157175  %     admissible

and the document's own framing is that choosing among them is a decision with no
structural discriminator — "bracketing is not evidence", both candidate elements
bracket the measured value. This probe supplies a discriminator that is not a
number: a bar-involution parity that the two admissible roots satisfy EXACTLY and
that the published functional and the excised convention C both fail.

WHAT IS DERIVED HERE (and what is not)

1. CLOSED FORMS. The corpus carries the three cells as decimals. All three are
   elementary rational functions of q, and they share a factor:

       Q_beta/m_e  =  (q+1)/(2 q^3)  x  M(q)

       z = 1    M = |q^2 - 2q - 1|          <- NOT palindromic
       z = q    M = (q^2 + 1)               <- palindromic
       z_D      M = (q^4 + 1)/(q^2 + 1)     <- palindromic

   Verified against the recorded percentages to the digits those carry.

2. THE PARITY, AND IT IS EXACT. With `h = q - 1/q` and bar the involution
   q -> 1/q, `bar(h) = -h` identically, so for `N(z) = tr_M(Delta_S) = h^2/2 - h z`

       bar(N) = h^2/2 + h*bar(z)     hence     bar(N) = -N  <=>  z - bar(z) = h.

   Equivalently — and this is the cleaner statement — `z - h/2` is bar-INVARIANT.
   Measured symbolically, exactly, no anchor involved:

       z = q     z - bar(z) = h    ✓        bar(Q)/Q = q^3
       z_D       z - bar(z) = h    ✓        bar(Q)/Q = q^3
       z = 1     z - bar(z) = 0    ✗        bar(Q)/Q not a monomial
       z_C       z - bar(z) = 0    ✗        bar(Q)/Q not a monomial

   Both admissible roots pass; the published functional and convention C fail,
   and they fail the SAME way — both are bar-INVARIANT (`bar(z) = z`) where the
   admissible ones are bar-SHIFTED. That z_C is bar-invariant is already on the
   record in qou-cds1 ("bar(z_C) = z_C, bar(z_D) = q^-4 z_D"); this probe
   reproduces that as a cross-check rather than assuming it.

3. 🛑 WHAT THIS DOES **NOT** ESTABLISH — stated so it is not over-read.
   This is NOT a proof that bar-parity characterises admissibility. The condition
   "`z - h/2` bar-invariant" defines an INFINITE family of rational z(q); the two
   admissible roots lie in it, but so do many others (the probe exhibits one).
   So the honest scope is:

       scope-(a): a NECESSARY condition satisfied by both admissible roots and
                  violated by both inadmissible ones on the tested set.

   It is a PRUNE, not a characterisation. A candidate functional failing it is
   excluded; one passing it is not thereby admissible.

WHY IT IS WORTH HAVING. Option E of the decision document — keep an admissible
functional and derive the element it acts on — is the only route that could give
a parameter-free admissible result rather than a choice among existing misses.
A structural test that runs with NO anchor and NO experimental input prunes
candidates before any number is computed, which is the formalize-first shape
AGENTS.md asks for over a wide numerical search.

Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md (qou-99qc)
Ref: computations/qbeta/qbeta_published_form_is_the_inadmissible_z1_probe.py (15/15)
Ref: folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDAdmissibleRoots.lean
Ref: beans qou-99qc, qou-cds1, qou-avt5, qou-37j2
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import _path_bridge  # noqa: F401, E402
from mpmath import mp, mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

q = sp.symbols("q", positive=True)
h = q - 1 / q
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(1, q)          # E_0 = m_e/(q(q-1)); everything below is in units of m_e
zsym = sp.symbols("z")
N = h**2 / 2 - h * zsym          # tr_M(Delta_S) as a function of the Markov parameter


def bar(e):
    """The bar involution q -> 1/q."""
    return sp.simplify(e.subs(q, 1 / q))


#: The four functionals under test. `admissible` records what
#: ConventionDAdmissibleRoots.lean proves, and is an INPUT here, not a conclusion.
FUNCTIONALS = {
    "z=1 (published)":        (sp.Integer(1),            False),
    "z=q (augmentation)":     (q,                        True),
    "z_D (Markov, conv D)":   (q**3 / (q**2 + 1),        True),
    "z_C (excised conv C)":   (sp.sqrt(q) / (q + 1),     False),
}

#: Recorded percentages from the decision document's grid, for calibration.
RECORDED_PCT = {
    "z=1 (published)":      "0.16775687",
    "z=q (augmentation)":   "12.470022",
    "z_D (Markov, conv D)": "-43.157175",
}


def is_monomial(expr) -> bool:
    """True when `expr` is +-c*q^k — i.e. bar-symmetry up to a power of q."""
    e = sp.cancel(sp.simplify(expr))
    num, den = sp.fraction(e)
    try:
        return sp.Poly(num, q).is_monomial and sp.Poly(den, q).is_monomial
    except sp.PolynomialError:
        return False


def main() -> int:
    print("=" * 78)
    print(" Bar parity separates the admissible Q_beta functionals from the rest")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-bar-parity-separates-admissible-functionals", engine="sympy+mpmath")
    wb.set_description(
        "Structural discriminator for the Q_beta functional question (qou-99qc). "
        "With h = q - 1/q and bar: q -> 1/q, bar(h) = -h identically, so for "
        "N(z) = tr_M(Delta_S) = h^2/2 - h z one has bar(N) = -N iff z - bar(z) = h, "
        "equivalently iff z - h/2 is bar-INVARIANT. Measured exactly: BOTH admissible "
        "roots (z = q the augmentation, z_D = q^3/(q^2+1) the convention-D Markov "
        "point) satisfy it and give bar(Q_beta)/Q_beta = q^3; the PUBLISHED functional "
        "z = 1 and the excised convention C z_C = sqrt(q)/(q+1) both FAIL it, and fail "
        "the same way (both are bar-invariant, bar(z) = z). Also supplies closed forms "
        "for all three cells of the Delta_S column, which the corpus carried only as "
        "decimals: Q_beta/m_e = (q+1)/(2q^3) * M with M = |q^2-2q-1| (z=1, NOT "
        "palindromic), (q^2+1) (z=q), (q^4+1)/(q^2+1) (z_D) -- both admissible M "
        "palindromic. SCOPE-(a) PRUNE, NOT a characterisation: 'z - h/2 bar-invariant' "
        "defines an INFINITE family (one non-admissible member is exhibited), so a "
        "functional failing the test is excluded but one passing it is not thereby "
        "admissible. No anchor and no experimental input enter the parity test; the "
        "numeric section is calibration only. Nothing wired."
    )
    wb.set_content_block("rem:qbeta-functional-admissibility")

    # ── 1. bar(h) = -h, the identity everything rests on ────────────────
    print("\nCHECK 1 — bar(h) = -h identically")
    hb = bar(h)
    ok = sp.simplify(hb + h) == 0
    print(f"    bar(h) = {sp.factor(hb)}     bar(h) + h = {sp.simplify(hb + h)}")
    wb.add_assertion("bar_h_is_minus_h", computed=("1" if ok else "0"), expected="1",
                     tolerance="0.5", source="bar(h) + h simplifies to 0 over Q(q)")

    # ── 2. the parity criterion, derived not asserted ───────────────────
    print("\nCHECK 2 — bar(N) = -N  <=>  z - bar(z) = h   (derived, symbolic)")
    zb = sp.symbols("zb")
    lhs = sp.simplify((h**2 / 2 + h * zb) + (h**2 / 2 - h * zsym))   # bar(N) + N
    solved = sp.simplify(sp.solve(sp.Eq(lhs, 0), zb)[0])             # bar(z) making bar(N) = -N
    crit_ok = sp.simplify(solved - (zsym - h)) == 0
    print(f"    bar(N) + N = 0  =>  bar(z) = {sp.factor(solved)}     equals z - h? {crit_ok}")
    wb.add_assertion("parity_criterion_is_z_minus_bar_z_equals_h",
                     computed=("1" if crit_ok else "0"), expected="1", tolerance="0.5",
                     source="solving bar(N) + N = 0 for bar(z) gives exactly z - h")

    # ── 3. each functional against the criterion ────────────────────────
    print("\nCHECK 3 — the four functionals")
    rows = {}
    for name, (zv, admissible) in FUNCTIONALS.items():
        bz = bar(zv)
        crit = sp.simplify(zv - bz - h)                 # 0 <=> passes
        passes = crit == 0
        Qz = sp.simplify(N.subs(zsym, zv) * E0)
        ratio = sp.simplify(sp.cancel(bar(Qz) / Qz))
        mono = is_monomial(ratio)
        print(f"    {name:24} z - bar(z) - h = {sp.factor(crit)!s:22} "
              f"parity {'PASS' if passes else 'FAIL'}   bar(Q)/Q = {sp.factor(ratio)}")
        rows[name] = {
            "z": str(sp.factor(zv)),
            "bar_z": str(sp.factor(bz)),
            "z_minus_bar_z_minus_h": str(sp.factor(crit)),
            "passes_bar_parity": bool(passes),
            "admissible_under_D": bool(admissible),
            "Q_over_me_closed_form": str(sp.factor(Qz)),
            "bar_Q_over_Q": str(sp.factor(ratio)),
            "bar_Q_over_Q_is_monomial": bool(mono),
        }
        # the headline: parity agrees with admissibility on every tested functional
        wb.add_assertion(
            f"parity_matches_admissibility__{name.split()[0].replace('=', '_')}",
            computed=("1" if passes == admissible else "0"), expected="1", tolerance="0.5",
            source=f"{name}: bar-parity {'passes' if passes else 'fails'}, "
                   f"admissible={admissible} — they agree")
        wb.add_assertion(
            f"monomial_iff_parity__{name.split()[0].replace('=', '_')}",
            computed=("1" if mono == passes else "0"), expected="1", tolerance="0.5",
            source=f"{name}: bar(Q)/Q monomial={mono}, parity={passes} — they agree")

    # ── 4. THE LIMIT: this is a prune, not a characterisation ───────────
    print("\nCHECK 4 — the criterion does NOT characterise admissibility")
    # z - h/2 bar-invariant defines an infinite family. Exhibit one member that is
    # NOT an admissible root: take w = q + 1/q (manifestly bar-invariant), z = w + h/2.
    w = q + 1 / q
    z_extra = sp.simplify(w + h / 2)
    passes_extra = sp.simplify(z_extra - bar(z_extra) - h) == 0
    # is it a root of the (1^3) weight numerator? the admissible roots are q and z_D
    is_admissible_root = (sp.simplify(z_extra - q) == 0
                          or sp.simplify(z_extra - q**3 / (q**2 + 1)) == 0)
    print(f"    z_extra = {sp.factor(z_extra)}")
    print(f"      passes bar-parity? {passes_extra}      is an admissible root? {is_admissible_root}")
    print("    => an infinite family passes; the test EXCLUDES, it does not certify.")
    wb.add_assertion("counterexample_passes_parity_but_is_not_an_admissible_root",
                     computed=("1" if (passes_extra and not is_admissible_root) else "0"),
                     expected="1", tolerance="0.5",
                     source=f"z = {sp.factor(z_extra)} satisfies z - bar(z) = h yet is neither "
                            f"q nor z_D, so bar-parity is necessary-not-sufficient")

    # ── 5. numeric calibration against the recorded grid ────────────────
    print("\nCHECK 5 — closed forms reproduce the decision document's grid")
    Q0 = mpf(Q_50_DIGIT_STR)
    numeric = {}
    for name in RECORDED_PCT:
        zv = FUNCTIONALS[name][0]
        f = sp.lambdify(q, sp.Abs(sp.simplify(N.subs(zsym, zv) * E0)), "mpmath")
        Qpred = M_E_MEV * f(Q0)
        err_pct = (Qpred - Q_BETA_MEV) / Q_BETA_MEV * 100
        rec = mpf(RECORDED_PCT[name])
        agree = abs(err_pct - rec) < mpf("1e-5")
        print(f"    {name:24} Q_beta = {mp.nstr(Qpred, 12):>15} MeV   "
              f"err = {mp.nstr(err_pct, 8):>12} %   recorded {RECORDED_PCT[name]}   "
              f"{'OK' if agree else 'MISMATCH'}")
        numeric[name] = {"Q_beta_MeV": fmt(Qpred, 20), "err_pct": fmt(err_pct, 20),
                         "recorded_pct": RECORDED_PCT[name]}
        wb.add_assertion(f"grid_calibration__{name.split()[0].replace('=', '_')}",
                         computed=("1" if agree else "0"), expected="1", tolerance="0.5",
                         source=f"closed form reproduces the recorded {RECORDED_PCT[name]} %")

    wb.add_data("functionals", rows)
    wb.add_data("numeric_calibration", numeric)
    wb.add_data("scope", {
        "tier": "scope-(a) prune",
        "established": ("both admissible roots satisfy z - bar(z) = h and give "
                        "bar(Q)/Q = q^3; the published z = 1 and the excised z_C both "
                        "fail, both by being bar-INVARIANT"),
        "NOT_established": ("that bar-parity characterises admissibility — the criterion "
                            "defines an infinite family and CHECK 4 exhibits a member "
                            "that is not an admissible root"),
        "use": ("a candidate Q_beta functional FAILING the parity is excluded; one "
                "passing it is not thereby admissible. Runs with no anchor and no "
                "experimental input, so it prunes before any number is computed."),
    })
    wb.save()
    print("\n  RESULT: bar-parity agrees with admissibility on all four tested "
          "functionals; it is a necessary condition, not a characterisation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
