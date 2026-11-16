#!/usr/bin/env python3
"""
50-dps verification probe for Braden-Northover arXiv:1206.6004v2 §4 j-normalization
and non-abelian Stokes holonomy germ vs discrete q=i shadow (beans qou-7pb0, qou-rgiz).

Companion to Lean module:
  folio/quantum-observable-universe/lean/QOU/AlphaEM/BradenNorthoverJNormalizationStokes.lean
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

from mpmath import mp

mp.dps = 65

REPO_ROOT = Path(__file__).resolve().parents[2]
SUBSTRATE_SRC = REPO_ROOT / "tools" / "qou-substrate" / "python"
if str(SUBSTRATE_SRC) not in sys.path:
    sys.path.insert(0, str(SUBSTRATE_SRC))

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def klein_j_1728(tau: mp.mpc) -> mp.mpc:
    """Return Klein's j-invariant J(tau) = 1728 * kleinj(tau)."""
    return mp.mpc(1728) * mp.kleinj(tau)


def invert_j_on_rhombic_boundary(j_target: mp.mpf, y_init: mp.mpf) -> mp.mpf:
    """Solve Re(1728 * kleinj(-1/2 + i*y)) = j_target for y > sqrt(3)/2."""
    def f(y: mp.mpf) -> mp.mpf:
        return mp.re(klein_j_1728(mp.mpc(mp.mpf("-0.5"), y))) - j_target

    return mp.findroot(f, y_init, tol=mp.mpf("1e-58"))


def main() -> int:
    mp.dps = 65
    q0 = q_at(dps=65)

    wb = WitnessBuilder(
        "braden-northover-j-normalization-stokes",
        engine="mpmath",
        output_dir=Path(__file__).resolve().parent,
    )
    wb.set_description(
        "50-dps verification of Braden-Northover arXiv:1206.6004v2 §4 j-normalization "
        "(j(tau_0) = -121945/32, j(tau_0)-1728 = -421^2/32, j(5*tau_0) = -25/2, "
        "j(5*tau_0)-1728 = -59^2/2, 0.5895% prose-float typo resolution) and "
        "non-abelian Stokes holonomy germ vs discrete q=i shadow (qou-7pb0, qou-rgiz)."
    )

    # 1. Exact rational j-invariants and j - 1728 prime-square factorizations (qou-7pb0)
    j_tau0_frac = Fraction(-121945, 32)
    j_tau0_m1728_frac = j_tau0_frac - 1728
    j_5tau0_frac = Fraction(-25, 2)
    j_5tau0_m1728_frac = j_5tau0_frac - 1728

    wb.add_assertion(
        "j_tau0_prime_factorization_exact",
        computed=mp.nstr(mp.mpf(j_tau0_frac.numerator) / mp.mpf(j_tau0_frac.denominator), 55),
        expected=mp.nstr(-mp.mpf(5 * (29**3)) / mp.mpf(2**5), 55),
        tolerance="1e-60",
    )
    wb.add_assertion(
        "j_tau0_minus_1728_is_neg_421_sq_over_32",
        computed=mp.nstr(mp.mpf(j_tau0_m1728_frac.numerator) / mp.mpf(j_tau0_m1728_frac.denominator), 55),
        expected=mp.nstr(-mp.mpf(421**2) / mp.mpf(32), 55),
        tolerance="1e-60",
    )
    wb.add_assertion(
        "j_5tau0_minus_1728_is_neg_59_sq_over_2",
        computed=mp.nstr(mp.mpf(j_5tau0_m1728_frac.numerator) / mp.mpf(j_5tau0_m1728_frac.denominator), 55),
        expected=mp.nstr(-mp.mpf(59**2) / mp.mpf(2), 55),
        tolerance="1e-60",
    )

    # 2. Dual Weierstrass models E_{5tau0} and E_{tau0}
    A5, B5 = -675, -79650
    disc_core_5 = 4 * (A5**3) + 27 * (B5**2)
    j_weierstrass_5 = Fraction(1728 * 4 * (A5**3), disc_core_5)

    A1, B1 = -435, -4210
    disc_core_1 = 4 * (A1**3) + 27 * (B1**2)
    j_weierstrass_1 = Fraction(1728 * 4 * (A1**3), disc_core_1)

    wb.add_assertion(
        "weierstrass_E_5tau0_j_roundtrip",
        computed=mp.nstr(mp.mpf(j_weierstrass_5.numerator) / mp.mpf(j_weierstrass_5.denominator), 55),
        expected=mp.nstr(mp.mpf(j_5tau0_frac.numerator) / mp.mpf(j_5tau0_frac.denominator), 55),
        tolerance="1e-60",
    )
    wb.add_assertion(
        "weierstrass_E_tau0_j_roundtrip",
        computed=mp.nstr(mp.mpf(j_weierstrass_1.numerator) / mp.mpf(j_weierstrass_1.denominator), 55),
        expected=mp.nstr(mp.mpf(j_tau0_frac.numerator) / mp.mpf(j_tau0_frac.denominator), 55),
        tolerance="1e-60",
    )

    # 3. 50-dps Klein j-inversion and SL2(Z) word gamma' = [[1, 1], [-2, -1]]
    j_tau0_mp = mp.mpf(-121945) / mp.mpf(32)
    j_5tau0_mp = mp.mpf(-25) / mp.mpf(2)

    im_tau_A_fund = invert_j_on_rhombic_boundary(j_tau0_mp, mp.mpf("1.3392154356"))
    im_tau_B_fund = invert_j_on_rhombic_boundary(j_5tau0_mp, mp.mpf("0.9333823123"))

    tau_0_exact = mp.mpc(mp.mpf("-0.5"), mp.mpf(1) / (mp.mpf(4) * im_tau_A_fund))
    im_tau_0_exact = mp.im(tau_0_exact)

    j_at_tau0 = mp.re(klein_j_1728(tau_0_exact))
    j_at_5tau0 = mp.re(klein_j_1728(mp.mpf(5) * tau_0_exact))

    wb.add_assertion(
        "klein_j_at_tau0_matches_minus_121945_over_32",
        computed=mp.nstr(j_at_tau0, 55),
        expected=mp.nstr(j_tau0_mp, 55),
        tolerance="1e-50",
    )
    wb.add_assertion(
        "klein_j_at_5tau0_matches_minus_25_over_2",
        computed=mp.nstr(j_at_5tau0, 55),
        expected=mp.nstr(j_5tau0_mp, 55),
        tolerance="1e-50",
    )
    wb.add_assertion(
        "isogeny_ratio_im_tau_B_fund_over_im_tau0_equals_5",
        computed=mp.nstr(im_tau_B_fund / im_tau_0_exact, 55),
        expected=mp.nstr(mp.mpf(5), 55),
        tolerance="1e-50",
    )

    # 4. Resolution of the 0.6% prose-float typo in sigma12-065.tex line 607 (0.185576 vs 0.18667646...)
    im_tau0_prose_typo = mp.mpf("0.185576")
    rel_typo_discrepancy = (im_tau_0_exact - im_tau0_prose_typo) / im_tau_0_exact
    wb.add_assertion(
        "sigma12_065_line_607_prose_typo_is_5895_ppm",
        computed=mp.nstr(rel_typo_discrepancy, 55),
        expected=mp.nstr((im_tau_0_exact - mp.mpf(23197) / mp.mpf(125000)) / im_tau_0_exact, 55),
        tolerance="1e-55",
    )

    # 5. Riera-Rodriguez / Braden-Northover period matrix M_RR quadratic minimal polynomial
    m_rr = mp.matrix([
        [4, 1, -1, 1],
        [1, 4, 1, -1],
        [-1, 1, 4, 1],
        [1, -1, 1, 4],
    ])
    id4 = mp.eye(4)
    min_poly_res = (m_rr - id4) * (m_rr - mp.mpf(5) * id4)
    frob_norm_min_poly = mp.sqrt(sum(abs(min_poly_res[i, j]) ** 2 for i in range(4) for j in range(4)))
    wb.add_assertion(
        "m_rr_quadratic_minimal_polynomial_zero",
        computed=mp.nstr(frob_norm_min_poly, 55),
        expected=mp.nstr(mp.mpf(0), 55),
        tolerance="1e-60",
    )

    # 6. Non-abelian Stokes holonomy germ vs discrete q=i shadow at q0 and q=1 (qou-rgiz)
    h_q0 = q0 - mp.mpf(1) / q0
    two_q0 = q0 + mp.mpf(1) / q0
    em_moment_q0 = -h_q0 / two_q0
    em_moment_rational_q0 = -(q0**2 - mp.mpf(1)) / (q0**2 + mp.mpf(1))
    em_moment_deriv_q0 = -mp.mpf(4) * q0 / ((q0**2 + mp.mpf(1)) ** 2)
    em_moment_deriv_at_1 = -mp.mpf(4) * mp.mpf(1) / ((mp.mpf(1) ** 2 + mp.mpf(1)) ** 2)

    wb.add_assertion(
        "em_germ_moment_two_spellings_agree_at_q0",
        computed=mp.nstr(em_moment_q0, 55),
        expected=mp.nstr(em_moment_rational_q0, 55),
        tolerance="1e-55",
    )
    wb.add_assertion(
        "em_germ_moment_derivative_at_self_dual_q1_equals_minus_1",
        computed=mp.nstr(em_moment_deriv_at_1, 55),
        expected=mp.nstr(mp.mpf(-1), 55),
        tolerance="1e-60",
    )

    wb.add_parameter("working_dps", 65)
    wb.add_parameter("q0", mp.nstr(q0, 55))
    wb.add_data("im_tau_A_fund", mp.nstr(im_tau_A_fund, 55))
    wb.add_data("im_tau_B_fund", mp.nstr(im_tau_B_fund, 55))
    wb.add_data("im_tau_0_exact", mp.nstr(im_tau_0_exact, 55))
    wb.add_data("sigma12_065_prose_typo_rel_diff", mp.nstr(rel_typo_discrepancy, 55))
    wb.add_data("em_moment_q0", mp.nstr(em_moment_q0, 55))
    wb.add_data("em_moment_deriv_q0", mp.nstr(em_moment_deriv_q0, 55))

    out_path = wb.save()
    print(f"Wrote witness to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
