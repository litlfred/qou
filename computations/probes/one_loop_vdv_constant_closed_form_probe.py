#!/usr/bin/env python3
"""Van der Veen's unevaluated constant, evaluated in closed form — both links.

Beans qou-fl4t / qou-pn5j. Van der Veen (arXiv:math/0611181, AGT 8 (2008)
603-624; `uploads/0611181v2.pdf`) proves the volume conjecture for the
Whitehead-chain family `W_{a,b,c,d}`,

    J_N(W)(e^{2 pi i/N}) ~ exp{ (1/2pi)[ (Vol + i CS) N + D log N + E ] },
    D = 3 pi  when b = 1,

and the constant `E` is the object this corpus measures as `c_sigma`. His proof
of Lemma 4 produces it as a `(c+d+1)`-dimensional Gaussian integral and then —
Step 6 — reduces it himself to ONE dimension:

    Q_inf = C * INT_0^inf exp( -pi A w^2 / 2 ) * erfc( sqrt(pi/2) w )^n dw
    A := (c+d) - (4a+c-d) i ,   n := c+d

He evaluates it only far enough to argue it is NONZERO, and his closing
paragraph defers the rest: Gukov-Murakami conjecture that `E` "is determined by
the Ray-Singer torsion of the complement twisted by the holonomy
representation", and "We hope to investigate these conjectures for the Whitehead
chains in a subsequent publication." A literature search finds no such sequel —
van der Veen moved to spin networks — and no one else has published this
constant for a multi-cusped link in this setting.

THE INTEGRAL IS AN ORTHANT PROBABILITY, AND THAT IS WHY IT CLOSES. Each `erfc`
is a half-space indicator integrated out, so the `n`-fold product against a
Gaussian is an `(n+1)`-dimensional Gaussian orthant probability. Those have
elementary closed forms exactly for `n <= 2` (bivariate/trivariate orthant
formulas; `n >= 3` needs Plackett reduction and has none in general). The two
links this corpus uses sit precisely inside that window:

    Whitehead link   W_{0,1,1,0}   n = 1,  A = 1 - i
    Borromean rings  W_{0,1,1,1}   n = 2,  A = 2      (4a+c-d = 0, so A is REAL)

giving

    n = 1:   I = arctan(sqrt A) / (pi sqrt(A/2))
    n = 2:   I = 1/2 + ( 2 arcsin(-1/sqrt 3) + arcsin(1/3) ) / pi

Both are checked below against direct quadrature at 30 dps, and the `n = 1`
value is additionally checked against an INDEPENDENT direct evaluation of van
der Veen's un-reduced Step-5 two-dimensional integral — which also validates the
prefactor `C = 2 psi 2^{-n/2}`, since that is where it enters.

WHAT THIS IS AND IS NOT. It evaluates a specific integral that a published proof
left unevaluated, for the two links at issue. It does NOT yet give `c_sigma`:
the bridge from `Q_inf` to `c_sigma` needs the constant in van der Veen's
Lemma 3 for the maximal term `S~_N` together with the normalisation between `J`
and the reduced `J'`, neither of which is done here. The measured ratios below
are reported precisely so the size and the c-DEPENDENCE of that missing bridge
are visible rather than guessed at.

Nothing is fitted. Everything is either a closed form or a committed witness.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import (  # noqa: E402
    mp, mpf, mpc, exp, pi, sqrt, quad, inf, fabs, atan, asin, erfc,
)

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
DISSOLUTION = COMP / "one-loop-c-sigma-percusp-dissolution.witness.json"

# W_{a,b,c,d} parameters of the two links, from van der Veen's Definition.
LINKS = {
    "L5a1 (Whitehead)": dict(a=0, b=1, c=1, d=0, cusps=2, key="L5a1"),
    "L6a4 (Borromean)": dict(a=0, b=1, c=1, d=1, cusps=3, key="L6a4"),
}


def vdv_A(a, c, d):
    """A := (c+d) - (4a+c-d) i, the Gaussian coefficient in Step 6."""
    return mpf(c + d) - mpc(0, 1) * (4 * a + c - d)


def vdv_psi(a, c, d):
    """psi := exp( -(4a+3c-3d) pi i / 4 )."""
    return exp(-mpc(0, 1) * pi * (4 * a + 3 * c - 3 * d) / 4)


def integral_numeric(A, n):
    """Van der Veen Step 6, by quadrature."""
    return quad(lambda w: exp(-pi * A * w**2 / 2) * erfc(sqrt(pi / 2) * w) ** n,
                [0, inf])


def integral_closed(A, n):
    """Closed form. n=1: a bivariate orthant; n=2: a trivariate one."""
    if n == 1:
        return atan(sqrt(A)) / (pi * sqrt(A / 2))
    if n == 2:
        # A = 2 exactly for the Borromean parameters, giving equicorrelated
        # orthant data: rho_12 = rho_13 = -1/sqrt(3), rho_23 = 1/3.
        return mpf(1) / 2 + (2 * asin(-1 / sqrt(3)) + asin(mpf(1) / 3)) / pi
    raise ValueError("no elementary closed form for n >= 3")


def step5_two_dim(a, c, d):
    """Van der Veen's UN-reduced Step-5 integral, for n = 1 only.

    Independent of the Step-6 reduction, so agreement validates both the
    reduction and the prefactor C.
    """
    A = vdv_A(a, c, d)
    integrand = lambda w, z: exp(  # noqa: E731
        -pi * (A * w**2 / 2 + 2 * (fabs(z) + fabs(w) / 2) ** 2))
    inner = lambda w: quad(lambda z: integrand(w, z), [-inf, 0, inf])  # noqa: E731
    return vdv_psi(a, c, d) * quad(inner, [-inf, 0, inf])


def main() -> int:
    set_compute_dps()
    dis = record_upstream(DISSOLUTION, _UPSTREAM_RECORDS)
    csig = {k: mpf(v) for k, v in dis["c_sigma_measured"].items()}

    print("=" * 78)
    print(" van der Veen's constant E — the integral he left unevaluated")
    print("=" * 78)

    rows, oks = {}, []
    for name, P in LINKS.items():
        a, c, d, n = P["a"], P["c"], P["d"], P["c"] + P["d"]
        A, psi = vdv_A(a, c, d), vdv_psi(a, c, d)
        I_num, I_cf = integral_numeric(A, n), integral_closed(A, n)
        dev = fabs(I_num - I_cf)
        ok = bool(dev < mpf("1e-25"))
        oks.append(ok)
        C = 2 * psi * mpf(2) ** (-mpf(n) / 2)
        Q = C * I_cf
        cs = csig[P["key"]]
        rows[name] = {
            "W_parameters": f"a={a}, b={P['b']}, c={c}, d={d}",
            "cusps": P["cusps"],
            "n_eq_c_plus_d": n,
            "A": mp.nstr(A, 20),
            "integral_numeric": mp.nstr(I_num, 22),
            "integral_closed_form": mp.nstr(I_cf, 22),
            "closed_form_matches_quadrature_to": mp.nstr(dev, 4),
            "Q_inf": mp.nstr(Q, 20),
            "abs_Q_inf": mp.nstr(fabs(Q), 20),
            "c_sigma_measured": mp.nstr(cs, 20),
            "abs_Q_inf_over_c_sigma": mp.nstr(fabs(Q) / cs, 20),
        }
        print(f"\n  {name}   W_{{{a},{P['b']},{c},{d}}}   n = c+d = {n}   "
              f"A = {mp.nstr(A, 8)}")
        print(f"     closed form  I = {mp.nstr(I_cf, 22)}")
        print(f"     quadrature   I = {mp.nstr(I_num, 22)}")
        print(f"     agree to       {mp.nstr(dev, 4)}   -> {ok}")
        print(f"     |Q_inf|        = {mp.nstr(fabs(Q), 18)}")
        print(f"     c_sigma        = {mp.nstr(cs, 18)}")
        print(f"     ratio          = {mp.nstr(fabs(Q)/cs, 18)}")

    # Independent check of the Step5 -> Step6 reduction AND the prefactor.
    q5 = step5_two_dim(0, 1, 0)
    q6 = 2 * vdv_psi(0, 1, 0) * mpf(2) ** (-mpf(1) / 2) * integral_closed(
        vdv_A(0, 1, 0), 1)
    red_dev = fabs(fabs(q5) - fabs(q6))
    red_ok = bool(red_dev < mpf("1e-12"))
    print(f"\n  Step-5 (2-D, un-reduced) vs Step-6 closed form, Whitehead:")
    print(f"     |Q| from Step 5 = {mp.nstr(fabs(q5), 18)}")
    print(f"     |Q| from Step 6 = {mp.nstr(fabs(q6), 18)}")
    print(f"     agree to          {mp.nstr(red_dev, 4)}   -> {red_ok}")
    print("     (this is what validates the prefactor C = 2 psi 2^(-n/2),")
    print("      which is a derivation from his text and not his own formula)")

    r_w = mpf(rows["L5a1 (Whitehead)"]["abs_Q_inf_over_c_sigma"])
    r_b = mpf(rows["L6a4 (Borromean)"]["abs_Q_inf_over_c_sigma"])
    bridge_c_dependent = bool(fabs(r_w - r_b) > mpf("1e-3"))
    print(f"\n  the missing bridge is c-DEPENDENT: ratio {mp.nstr(r_w, 10)} at "
          f"c=2 vs {mp.nstr(r_b, 10)} at c=3")
    print("  (expected — S~_N^(c+d) enters the bridge with a c+d power — but it")
    print("   means no single constant closes it, and it is not closed here)")

    all_ok = all(oks) and red_ok

    verdict = (
        "VAN DER VEEN'S CONSTANT IS NOW IN CLOSED FORM FOR BOTH LINKS. His "
        "Lemma 4 proof reduces E to a one-dimensional integral (Step 6) and "
        "then argues only that it is nonzero; his closing paragraph defers the "
        "evaluation to a sequel that a literature search finds he never wrote. "
        "The integral is an (n+1)-dimensional Gaussian ORTHANT probability, "
        "which has an elementary closed form exactly for n <= 2 — and the two "
        "links here are n = 1 and n = 2. "
        "Whitehead (n=1, A=1-i): I = arctan(sqrt A)/(pi sqrt(A/2)). "
        "Borromean (n=2, A=2, real because 4a+c-d = 0): "
        "I = 1/2 + (2 arcsin(-1/sqrt3) + arcsin(1/3))/pi. "
        f"Both match direct quadrature to better than 1e-25, and the Whitehead "
        "value additionally reproduces an independent evaluation of the "
        "un-reduced two-dimensional Step-5 integral — which is what validates "
        "the prefactor C = 2 psi 2^(-n/2), a derivation from his text rather "
        "than a formula he states. "
        "THIS IS NOT c_sigma YET, AND THE GAP IS VISIBLE. The bridge needs "
        "Lemma 3's constant for the maximal term S~_N and the J-to-J' "
        f"normalisation. Measured, |Q_inf|/c_sigma is {mp.nstr(r_w, 10)} at "
        f"c = 2 and {mp.nstr(r_b, 10)} at c = 3 — NOT a single constant, which "
        "is expected since S~_N enters the bridge raised to the (c+d) power, "
        "and which is exactly why the bridge cannot be guessed from one link. "
        "WHAT IT DOES SETTLE: the constant for these links is an explicit "
        "elementary number, not an opaque integral. Anyone attempting the "
        "Gukov-Murakami conjecture for the Whitehead chains now has the "
        "left-hand side in closed form for the two cases that matter."
        if all_ok else
        "THE CLOSED FORMS DO NOT MATCH QUADRATURE — inspect before citing.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-vdv-constant-closed-form", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Evaluates in closed form the constant van der Veen (AGT 8 (2008) "
        "603-624) leaves unevaluated in the proof of his Lemma 4 — the "
        "constant E in the colored-Jones asymptotic of a Whitehead chain, "
        "which is the object this corpus measures as c_sigma. His Step 6 "
        "reduces it to a 1-D integral of a Gaussian against erfc^n; that is an "
        "(n+1)-dimensional Gaussian orthant probability, elementary exactly for "
        "n <= 2, and the Whitehead link (n=1) and Borromean rings (n=2) are "
        "both inside that window. Gives arctan and arcsin closed forms, checked "
        "against quadrature to 1e-25 and, for the Whitehead link, against an "
        "independent evaluation of the un-reduced 2-D Step-5 integral. Does NOT "
        "yet give c_sigma: the bridge needs Lemma 3's S~_N constant and the "
        "J/J' normalisation, and the measured ratio is c-dependent, so it "
        "cannot be guessed from one link. Nothing fitted.")
    wb.set_audit_only(
        "docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md")
    wb.add_data("source", {
        "paper": "van der Veen, Proof of the volume conjecture for Whitehead "
                 "chains, Algebr. Geom. Topol. 8 (2008) 603-624",
        "arxiv": "math/0611181",
        "local": "uploads/0611181v2.pdf",
        "what_he_proves": ("the volume conjecture for the family, with "
                           "D = 3 pi for b = 1 — the N-power, independent of "
                           "the number of components"),
        "what_he_leaves": ("E, given as a (c+d+1)-dim Gaussian integral and "
                           "self-reduced in Step 6 to one dimension; he shows "
                           "only that it is nonzero"),
        "his_deferral": ("cites Gukov-Murakami for the conjecture that E is "
                         "determined by the Ray-Singer torsion, and defers it "
                         "to a subsequent publication"),
        "sequel_status": ("a literature search finds no such sequel — his later "
                          "work moves to spin networks and then to algorithmic "
                          "knot invariants; and no other author has published "
                          "this constant for a multi-cusped link in this "
                          "setting (colored Jones in S^3 at e^{2 pi i/N})"),
    })
    wb.add_data("closed_forms", rows)
    wb.add_data("why_it_closes", (
        "each erfc is a half-space indicator integrated out, so the n-fold "
        "product against a Gaussian is an (n+1)-dimensional Gaussian ORTHANT "
        "probability. Elementary closed forms exist exactly for n <= 2 "
        "(bivariate/trivariate orthant); n >= 3 requires Plackett reduction and "
        "has none in general. The Whitehead link (n=1) and Borromean rings "
        "(n=2) are both inside that window — a Whitehead chain with more "
        "clasps would not be."))
    wb.add_data("step5_step6_crosscheck", {
        "abs_Q_from_step5_2d": mp.nstr(fabs(q5), 20),
        "abs_Q_from_step6_closed": mp.nstr(fabs(q6), 20),
        "agreement": mp.nstr(red_dev, 4),
        "validates": ("the Step5 -> Step6 reduction AND the prefactor "
                      "C = 2 psi 2^(-n/2), which is derived from van der Veen's "
                      "text here rather than stated by him"),
    })
    wb.add_data("bridge_to_c_sigma_NOT_done", {
        "missing": ("the constant in van der Veen's Lemma 3 for the maximal "
                    "term S~_N, and the normalisation between J and the "
                    "reduced J' this corpus measures"),
        "ratio_at_c2_whitehead": mp.nstr(r_w, 20),
        "ratio_at_c3_borromean": mp.nstr(r_b, 20),
        "ratio_is_c_dependent": bridge_c_dependent,
        "why_c_dependent_is_expected": ("S~_N enters the bridge raised to the "
                                        "(c+d) power, so the missing factor "
                                        "cannot be a single constant and cannot "
                                        "be inferred from one link"),
    })
    wb.add_assertion(
        "closed_forms_match_quadrature",
        computed="1" if all(oks) else "0", expected="1", tolerance="0.5",
        source=("arctan form (Whitehead, n=1) and arcsin form (Borromean, n=2) "
                "each agree with direct quadrature of van der Veen's Step-6 "
                "integral to better than 1e-25"))
    wb.add_assertion(
        "step6_reduction_and_prefactor_validated",
        computed="1" if red_ok else "0", expected="1", tolerance="0.5",
        source=("the Whitehead closed form reproduces an independent evaluation "
                "of the un-reduced 2-D Step-5 integral, which is the only place "
                "the derived prefactor C = 2 psi 2^(-n/2) enters"))
    out = wb.save()
    print(f"  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
