#!/usr/bin/env python3
"""qbeta_dladder_qborel_2adic_transport_probe.py

Formalize-first step of the D-ladder Jackson q-Borel / Écalle acceleration
program (audit `docs/audits/2026-07-17-dladder-qborel-acceleration.md` §2):
transport the **exact 2-adic bar-parity grading** (anchor A1,
`QOU.QBeta.DLadderTwoAdicGrading.bDen_two_adic_graded`; KC22) through the
scalar acceleration family, BEFORE any numerical scan.

## The invariant (exact, one-line)

Every member of the scalar acceleration family — classical Borel `÷k!`,
Borel–Leroy `÷(k!)^s`, Jackson q-Borel `÷[k]_Q!` or `÷(Q;Q)_k`, and any
Écalle acceleration built from scalar kernels — acts **diagonally** on the
ℚ(√3) components of `d_k = a_k + b_k√3`:

    a_k ↦ a_k / f_k,   b_k ↦ b_k / f_k,   with the SAME f_k ∈ ℚ^×.

Since `v₂` is a valuation on ℚ, `v₂(x/f) = v₂(x) − v₂(f)` exactly, so the
**signed component gap**

    g_k = v₂(a_k) − v₂(b_k)

is invariant under the ENTIRE family. The ℤ/2 bar-parity grading in gap form
(`sign(g_k)` alternates with `k`-parity: odd k ⇒ the rational part is
2-adically singular, g_k < 0; even k ⇒ mirrored, g_k > 0) therefore SURVIVES
into every accelerated plane — the grading does NOT obstruct the resummation
shape; it is carried verbatim by the ℚ(√3)-direction, which no scalar
transform touches.

## The absolute law transports by v₂(f_k) — computed exactly

The absolute form `v₂(den b_k) = 0 ⟺ k odd` shifts by `−v₂(f_k)` on the
valuation (den picks up `2^{v₂(f_k)}` when `v₂(b_k) < v₂(f_k)`). The 2-adic
valuation of the q-factorial bases is closed-form (LTE, odd base Q):

    v₂([j]_Q) = 0                      (j odd)
    v₂([j]_Q) = v₂(Q²−1) − v₂(Q−1) + v₂(j) − 1   (j even)

so v₂([k]_Q!) = Σ_{even j ≤ k} (…) — verified here against exact arithmetic.
Notable special case: **base Q = 2** has `[j]_2 = 2^j − 1` odd for all j, so
`v₂([k]_2!) = 0` — the base-2 Jackson q-Borel (the base matching the unique
graded prime) transports the ABSOLUTE grading law verbatim. Classical `÷k!`
adds `v₂(k!) = k − s₂(k)` (Legendre) to both components and destroys the
absolute law from k = 2 on (gap form still survives).

Scope-(a); exact rational arithmetic only; no floats on the claim path; no
c_k wired; no fit; no tier change. KC22's closed (q-)holonomic classes are
not re-run.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 43
core.ORD = ORD
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
dlad.ORD = ORD

R3 = sp.sqrt(3)


def v2(x: sp.Rational) -> int | None:
    """2-adic valuation of a nonzero rational (num minus den); None for 0."""
    x = sp.Rational(x)
    if x == 0:
        return None
    return sp.multiplicity(2, x.p) - sp.multiplicity(2, x.q)


def qint(j: int, Q: sp.Rational) -> sp.Rational:
    """[j]_Q = (Q^j − 1)/(Q − 1) (Q ≠ 1); [j]_1 = j (classical limit)."""
    Q = sp.Rational(Q)
    if Q == 1:
        return sp.Rational(j)
    return sp.Rational((Q**j - 1) / (Q - 1))


def qfact(k: int, Q: sp.Rational) -> sp.Rational:
    f = sp.Rational(1)
    for j in range(1, k + 1):
        f *= qint(j, Q)
    return f


def v2_qfact_lte(k: int, Q: sp.Rational) -> int:
    """Closed-form v₂([k]_Q!) for odd-numerator/odd-denominator base Q via LTE.

    For Q ≡ odd/odd (v₂(Q) = 0, Q ≠ ±1): v₂(Q^j − 1) = v₂(Q − 1) for j odd,
    and v₂(Q − 1) + v₂(Q + 1) + v₂(j) − 1 for j even; subtract v₂(Q − 1) for
    the [j]_Q normalization. Q = 1 falls back to Legendre v₂(k!) = k − s₂(k).
    """
    Q = sp.Rational(Q)
    if Q == 1:
        return k - bin(k).count("1")
    a = v2(Q - 1)
    b = v2(Q + 1)
    tot = 0
    for j in range(2, k + 1, 2):
        tot += a + b + sp.multiplicity(2, j) - 1 - a
    return int(tot)


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" D-ladder q-Borel 2-adic transport — exact (ORD {ORD})")
    print("=" * 78)

    dk, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    print(f"  built exact d_1..d_{KMAX} (valid_top s^{valid_top}, over-det zero: {odd_ok})")
    a = {k: sp.Rational(sp.expand(dk[k]).coeff(R3, 0)) for k in dk}
    b = {k: sp.Rational(sp.expand(dk[k]).coeff(R3, 1)) for k in dk}

    # ---- 1. re-verify the untransformed grading (A1) + the gap form ----
    abs_law = all((sp.Rational(b[k]).q % 2 == 1) == (k % 2 == 1) for k in b)
    mirror = all((sp.multiplicity(2, sp.Rational(a[k]).q) <= 1) == (k % 2 == 0) for k in a)
    g = {k: v2(a[k]) - v2(b[k]) for k in dk}
    gap_alternates = all((g[k] < 0) == (k % 2 == 1) for k in g)
    print(f"\n  [1] untransformed: absolute law v₂(den b_k)=0 ⟺ k odd: {abs_law};"
          f" mirror v₂(den a_k)≤1 ⟺ k even: {mirror}")
    print(f"      gap g_k = v₂(a_k)−v₂(b_k): {[g[k] for k in sorted(g)]}")
    print(f"      sign(g_k) alternates with parity (odd k ⇒ g<0): {gap_alternates}")

    # ---- 2. transport through the scalar family — gap invariance (exact) ----
    bases = {
        "classical k! (Borel s=1)": [qfact(k, sp.Integer(1)) for k in range(KMAX + 1)],
        "[k]_2! (Jackson base 2)": [qfact(k, sp.Integer(2)) for k in range(KMAX + 1)],
        "[k]_3! (Jackson base 3)": [qfact(k, sp.Integer(3)) for k in range(KMAX + 1)],
        "[k]_{1/3}! (reciprocal base)": [qfact(k, sp.Rational(1, 3)) for k in range(KMAX + 1)],
        "[k]_{1/2}! (reciprocal base 2)": [qfact(k, sp.Rational(1, 2)) for k in range(KMAX + 1)],
        "(3;3)_k (unnormalized q-Poch)": [
            sp.Rational(sp.prod([sp.Integer(3)**j - 1 for j in range(1, k + 1)]) if k else 1)
            for k in range(KMAX + 1)],
    }
    gap_invariant_all = True
    abs_law_survives = {}
    v2f_match_lte = True
    print("\n  [2] transport a_k/f_k, b_k/f_k — exact per-base results:")
    for name, f in bases.items():
        ta = {k: a[k] / f[k] for k in a}
        tb = {k: b[k] / f[k] for k in b}
        tg = {k: v2(ta[k]) - v2(tb[k]) for k in a}
        inv = all(tg[k] == g[k] for k in g)
        gap_invariant_all &= inv
        alaw = all((sp.Rational(tb[k]).q % 2 == 1) == (k % 2 == 1) for k in tb)
        abs_law_survives[name] = alaw
        # closed-form LTE check where applicable (odd rational base or Q=1)
        lte_note = ""
        Qmap = {"classical k! (Borel s=1)": sp.Integer(1),
                "[k]_3! (Jackson base 3)": sp.Integer(3),
                "[k]_{1/3}! (reciprocal base)": sp.Rational(1, 3)}
        if name in Qmap:
            ok = all(v2(f[k]) == v2_qfact_lte(k, Qmap[name]) for k in range(1, KMAX + 1))
            v2f_match_lte &= ok
            lte_note = f"; v₂(f_k) matches LTE closed form: {ok}"
        print(f"      {name:32s} gap invariant: {inv}; absolute law survives: {alaw}"
              f"; v₂(f_KMAX) = {v2(f[KMAX])}{lte_note}")

    base2_preserves = abs_law_survives["[k]_2! (Jackson base 2)"]
    classical_destroys = not abs_law_survives["classical k! (Borel s=1)"]

    # ---- 3. verdict ----
    print("\n  [3] structural verdict:")
    print("      - gap form of the ℤ/2 grading is invariant under the ENTIRE scalar")
    print("        acceleration family (exact; v₂ is a valuation) — the grading does")
    print("        NOT obstruct any q-Borel resummation shape;")
    print("      - the ABSOLUTE law survives exactly under 2-adically-unit bases —")
    print(f"        notably Jackson base 2 (the graded prime): {base2_preserves};")
    print(f"      - classical ÷k! destroys the absolute law (Legendre v₂>0): {classical_destroys}.")

    verdict = (
        "2-adic transport of the bar-parity grading through the scalar q-Borel/"
        "acceleration family (exact, k=1..%d): the signed component gap g_k = "
        "v₂(a_k)−v₂(b_k) is INVARIANT under every scalar transform (valuation "
        "additivity), so the ℤ/2 grading survives into every accelerated plane — "
        "the invariant is PERMISSIVE (no obstruction to resummation), scope: "
        "structural-exact, not a refutation. The absolute law v₂(den b_k)=0 ⟺ k "
        "odd transports by −v₂(f_k): preserved verbatim by 2-adically-unit bases "
        "(Jackson base 2 — the unique graded prime's own base: [j]_2 = 2^j−1 odd), "
        "destroyed by classical ÷k! (Legendre). v₂([k]_Q!) verified against the "
        "LTE closed form. No c_k wired; no fit." % KMAX
    )
    print(f"\n  VERDICT: {verdict}")
    print(f"  ({time.monotonic() - t0:.1f}s)")

    wb = WitnessBuilder("qbeta-dladder-qborel-2adic-transport", engine="sympy")
    wb.set_description(
        "Formalize-first step of the D-ladder Jackson q-Borel acceleration "
        "program: exact 2-adic transport of the bar-parity grading (anchor "
        "QOU.QBeta.DLadderTwoAdicGrading.bDen_two_adic_graded, KC22) through "
        "the scalar acceleration family. Result: the grading in gap form "
        "g_k = v2(a_k)-v2(b_k) is invariant under EVERY scalar transform "
        "(valuation additivity — one-line, Lean-able), hence permissive: no "
        "obstruction to any q-Borel resummation shape. The absolute law "
        "v2(den b_k)=0 iff k odd is preserved verbatim exactly by 2-adically-"
        "unit factorial bases (notably Jackson base 2, the graded prime's own "
        "base) and destroyed by classical /k!. v2([k]_Q!) cross-checked against "
        "the LTE closed form. Scope-(a) structural-exact; no c_k wired; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("KMAX", KMAX)
    wb.add_data("gap_g_k", {str(k): int(g[k]) for k in sorted(g)})
    wb.add_data("gap_sign_alternates_with_parity", bool(gap_alternates))
    wb.add_data("absolute_law_untransformed", bool(abs_law))
    wb.add_data("mirror_law_untransformed", bool(mirror))
    wb.add_data("gap_invariant_under_all_tested_bases", bool(gap_invariant_all))
    wb.add_data("absolute_law_survival_by_base",
                {k: bool(v) for k, v in abs_law_survives.items()})
    wb.add_data("v2_qfact_matches_lte_closed_form", bool(v2f_match_lte))
    wb.add_data("lean_anchor", "qou:QOU.QBeta.DLadderTwoAdicGrading.bDen_two_adic_graded")
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a)/structural-exact — permissive invariant; no wiring")
    wb.add_assertion("untransformed_grading_holds", bool(abs_law and mirror), True)
    wb.add_assertion("gap_sign_alternates_with_parity", bool(gap_alternates), True)
    wb.add_assertion("gap_invariant_under_all_scalar_bases", bool(gap_invariant_all), True)
    wb.add_assertion("base2_jackson_preserves_absolute_law", bool(base2_preserves), True)
    wb.add_assertion("classical_borel_destroys_absolute_law", bool(classical_destroys), True)
    wb.add_assertion("v2_qfact_lte_closed_form_verified", bool(v2f_match_lte), True)
    out = wb.save()
    print(f"  Witness: {out}")
    ok = (abs_law and mirror and gap_alternates and gap_invariant_all
          and base2_preserves and classical_destroys and v2f_match_lte)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
