#!/usr/bin/env python3
"""bring_transposition_weierstrass_sixty_probe.py — 80-dps First-Principles Probe of
Bring's Curve Transposition Fixed-Point Cubic t^3 + 2 t^2 + 3 t + 4 = 0, the
10 x 6 = 60 Projective Weierstrass Points, Transitive S_5 Action, and Genus-1
Elliptic Quotient E_tau = B / <tau> (Zero Float64, Zero Fitting).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Brings/BringTranspositionSixFixedPointsAndEllipticQuotient.lean`
  (`namespace QOU.Brings.BringTranspositionSixFixedPointsAndEllipticQuotient`)
and Bean `qou-qhcr`.

PURPOSE & MATHEMATICAL ARCHITECTURE
-----------------------------------
Evaluates at 80 decimal places (with 95-dps internal guard precision, zero float64
conversions, and zero `math` module imports) the transposition fixed-point geometry
and degree-2 elliptic quotient of Bring's curve
  B = { [z_0 : z_1 : z_2 : z_3 : z_4] in P^4(C) | p_1(z) = p_2(z) = p_3(z) = 0 },
where p_k(z) = sum_{i=0}^4 z_i^k:

1. **Cardano + 95-dps Newton Solution of P_tau(t) = t^3 + 2 t^2 + 3 t + 4 = 0**:
   - Under a transposition tau = (0 1) in S_5 = Aut(B), the (-1)-eigenspace point
     [1 : -1 : 0 : 0 : 0] has p_2 = 2 != 0 (`antiFixedPoint_not_on_bring`), and the
     boundary z_0 = z_1 = 0 has only the trivial solution z_2 = z_3 = z_4 = 0
     (`zero_coord_fixed_locus_empty`). Every fixed point normalizes uniquely to
     z_0 = z_1 = 1, where p_1 = p_2 = p_3 = 0 reduces via Newton-Girard identities
     to e_1 = -2, e_2 = 3, e_3 = -4 (`bring_transposition_fixed_iff_vieta`), so
     {z_2, z_3, z_4} are the three roots r_0, r_1, r_2 of P_tau(t) = t^3 + 2 t^2 + 3 t + 4.
   - Depressing via t = y - 2/3 gives y^3 + (5/3) y + 70/27 = 0 with Cardano
     square root sqrt((35/27)^2 + (5/9)^3) = sqrt(1350/729) = sqrt(50/27) = (5*sqrt(6))/9,
     yielding exact radical cube roots U = (15*sqrt(6) - 35)^(1/3) / 3 and
     V = -(15*sqrt(6) + 35)^(1/3) / 3 and polynomial discriminant
     Delta(P_tau) = prod_{i<j} (r_i - r_j)^2 = -200 = -2^3 * 5^2
     (`transposition_cubic_discriminant_eq_neg_200`).

2. **All 10 x 6 = 60 Projective Weierstrass Points & Pairwise Fubini-Study Separation**:
   - Across all C(5, 2) = 10 transpositions tau_{a,b} = (a b) in S_5 and all 3! = 6
     permutations sigma in S_3 of (r_0, r_1, r_2), constructs all 60 points
     P_{(a,b), sigma} in P^4(C).
   - Verifies max |p_k(P)| < 10^{-88} (k = 1, 2, 3) on all 60 points and verifies
     pairwise projective distinctness across all C(60, 2) = 1770 pairs via the
     Fubini-Study metric d_FS([z], [w]) = sqrt(1 - |<z, w>|^2 / (||z||^2 ||w||^2)),
     confirming min_{P != Q} d_FS(P, Q) > 0.45.

3. **Transitive S_5 Action (|S_5| = 120) & Stabilizer Order 120 / 60 = 2**:
   - Acts on the 60 projective Weierstrass points by all 120 permutations g in S_5,
     verifying that the orbit of P_{(0,1), id} has cardinality 60 and that every point
     P_{(a,b), sigma} has projective stabilizer Stab_{S_5}(P_{(a,b), sigma}) = {id, tau_{a,b}}
     of order 2.

4. **Genus-1 Elliptic Quotient E_tau = B / <tau> & Exact j-Invariant j(E_tau) = -25/2**:
   - Eliminating z_0, z_1 via z_0 + z_1 = -s_1 and (z_0 - z_1)^2 = -s_1^2 - 2 s_2
     projects B / <tau_{0,1}> onto the smooth plane cubic in P^2_{[z_2 : z_3 : z_4]}:
       F_tau(z_2, z_3, z_4) = s_1^3 + 3 s_1 s_2 + 2 s_3 = 0,
     where s_k = z_2^k + z_3^k + z_4^k, branched along the conic Q_tau = s_1^2 + 2 s_2 = 0
     at deg(F_tau) * deg(Q_tau) = 3 * 2 = 6 simple branch points.
   - Birational reduction (w = 2(z_2 + z_3) + 1 = -10/X, v = z_2 - z_3 = Y / (2 X) at z_4 = 1)
     puts E_tau into Weierstrass form
       Y^2 = X^3 - 5 X^2 - 100 = t^3 - (25/3) t - 2950/27,
     with invariants c_4 = 400, c_6 = 94400, Delta = (c_4^3 - c_6^2)/1728 = -5120000,
     and exact rational j-invariant
       j(E_tau) = c_4^3 / Delta = 64000000 / (-5120000) = -25/2 = -12.5,
     cross-checked at 95 dps against the Legendre cross-ratio formula
       j(lambda) = 256 (1 - lambda + lambda^2)^3 / (lambda^2 (1 - lambda)^2)
     of the 4 branch points {0} union {roots of w^3 + 5 w + 10 = 0} of E_tau -> P^1_w.
   - By Riemann-Hurwitz (`bring_elliptic_quotient_forces_chi_eq_neg_six`),
     chi(B) = 2 * chi(E_tau) - 6 = 2 * 0 - 6 = -6 and g(B) = 4.
"""

from __future__ import annotations

import itertools
import os
import sys
from pathlib import Path
from typing import Any

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(80)

from witness_base import WitnessBuilder  # noqa: E402

COMPUTE_DPS: int = 95
OUTPUT_DPS: int = 80
mp.mp.dps = COMPUTE_DPS


def fmt80(val: mp.mpf) -> str:
    """Format an arbitrary-precision mpf to 80 significant digits."""
    return mp.nstr(val, OUTPUT_DPS)


def fmt_complex80(val: mp.mpc) -> dict[str, str]:
    """Format an arbitrary-precision mpc as real/imag 80-dps strings."""
    return {
        "re": mp.nstr(mp.re(val), OUTPUT_DPS),
        "im": mp.nstr(mp.im(val), OUTPUT_DPS),
    }


def solve_transposition_cubic_95dps() -> dict[str, Any]:
    """Solve P_tau(t) = t^3 + 2 t^2 + 3 t + 4 = 0 via exact Cardano radicals + 95-dps Newton."""
    mp.mp.dps = COMPUTE_DPS
    one = mp.mpf("1")
    two = mp.mpf("2")
    three = mp.mpf("3")
    four = mp.mpf("4")

    # Depressed cubic y^3 + (5/3) y + 70/27 = 0 with t = y - 2/3
    # Cardano radical: sqrt((35/27)^2 + (5/9)^3) = sqrt(1350/729) = sqrt(50/27) = (5*sqrt(6))/9 = (15*sqrt(6))/27
    # U = ((15*sqrt(6) - 35)/27)^(1/3) = (15*sqrt(6) - 35)^(1/3) / 3
    # V = -((15*sqrt(6) + 35)/27)^(1/3) = -(15*sqrt(6) + 35)^(1/3) / 3
    sqrt6 = mp.sqrt(mp.mpf("6"))
    u_rad = mp.root(mp.mpf("15") * sqrt6 - mp.mpf("35"), 3) / three
    v_rad = -mp.root(mp.mpf("15") * sqrt6 + mp.mpf("35"), 3) / three
    shift = -two / three
    sqrt3 = mp.sqrt(three)
    omega = mp.mpc(-one / two, sqrt3 / two)
    omega2 = mp.mpc(-one / two, -sqrt3 / two)

    roots_init = [
        mp.mpc(shift + u_rad + v_rad, mp.mpf("0")),
        shift + omega * u_rad + omega2 * v_rad,
        shift + omega2 * u_rad + omega * v_rad,
    ]

    def p_tau(z: mp.mpc) -> mp.mpc:
        return ((z + two) * z + three) * z + four

    def dp_tau(z: mp.mpc) -> mp.mpc:
        return (three * z + four) * z + three

    roots: list[mp.mpc] = []
    for z0 in roots_init:
        z = z0
        for _ in range(12):
            z = z - p_tau(z) / dp_tau(z)
        roots.append(z)
    # Enforce exact real axis on r_0 and verify Cardano radical matches r_0 to < 10^{-90}
    roots[0] = mp.mpc(mp.re(roots[0]), mp.mpf("0"))
    cardano_r0_err = abs((shift + u_rad + v_rad) - mp.re(roots[0]))
    assert cardano_r0_err < mp.mpf("1e-90")

    residuals = [abs(p_tau(r)) for r in roots]
    max_res = max(residuals)

    r0, r1, r2 = roots
    e1 = r0 + r1 + r2
    e2 = r0 * r1 + r0 * r2 + r1 * r2
    e3 = r0 * r1 * r2
    vieta_err = max(
        abs(e1 - (-two)),
        abs(e2 - three),
        abs(e3 - (-four)),
    )

    disc_prod = ((r0 - r1) ** 2) * ((r0 - r2) ** 2) * ((r1 - r2) ** 2)
    disc_err = abs(disc_prod - mp.mpc(mp.mpf("-200"), mp.mpf("0")))

    s1 = r0 + r1 + r2
    s2 = r0**2 + r1**2 + r2**2
    s3 = r0**3 + r1**3 + r2**3
    power_sum_err = max(
        abs(s1 - (-two)),
        abs(s2 - (-two)),
        abs(s3 - (-two)),
    )

    return {
        "roots": roots,
        "max_cubic_residual": max_res,
        "vieta_error": vieta_err,
        "power_sum_error": power_sum_err,
        "discriminant_product": disc_prod,
        "discriminant_error_vs_neg_200": disc_err,
        "cardano_u_cbrt_15sqrt6_minus_35_over_3": u_rad,
        "cardano_v_neg_cbrt_15sqrt6_plus_35_over_3": v_rad,
        "cardano_r0_vs_newton_error": cardano_r0_err,
    }


def fubini_study_distance(z: tuple[mp.mpc, ...], w: tuple[mp.mpc, ...]) -> mp.mpf:
    """Compute Fubini-Study projective distance sqrt(1 - |<z,w>|^2 / (||z||^2 ||w||^2)) on P^4(C)."""
    inner = mp.mpc("0", "0")
    nz = mp.mpf("0")
    nw = mp.mpf("0")
    for zk, wk in zip(z, w):
        inner += zk * mp.conj(wk)
        nz += abs(zk) ** 2
        nw += abs(wk) ** 2
    ratio = (abs(inner) ** 2) / (nz * nw)
    if ratio >= mp.mpf("1"):
        return mp.mpf("0")
    return mp.sqrt(mp.mpf("1") - ratio)


def build_sixty_weierstrass_points_and_verify_s5(
    roots: list[mp.mpc],
) -> dict[str, Any]:
    """Construct all 10 x 6 = 60 transposition fixed points on Bring's curve and verify S_5 action."""
    mp.mp.dps = COMPUTE_DPS
    one = mp.mpc(mp.mpf("1"), mp.mpf("0"))

    transpositions: list[tuple[int, int]] = [
        (a, b) for a in range(5) for b in range(a + 1, 5)
    ]
    s3_perms: list[tuple[int, int, int]] = list(itertools.permutations((0, 1, 2)))

    points: list[dict[str, Any]] = []
    max_bring_res = mp.mpf("0")

    for a, b in transpositions:
        rem = [idx for idx in range(5) if idx not in (a, b)]
        for perm in s3_perms:
            coords = [one] * 5
            coords[a] = one
            coords[b] = one
            coords[rem[0]] = roots[perm[0]]
            coords[rem[1]] = roots[perm[1]]
            coords[rem[2]] = roots[perm[2]]
            pt = tuple(coords)

            p1 = sum(pt)
            p2 = sum(c**2 for c in pt)
            p3 = sum(c**3 for c in pt)
            res = max(abs(p1), abs(p2), abs(p3))
            if res > max_bring_res:
                max_bring_res = res

            points.append(
                {
                    "transposition": (a, b),
                    "s3_perm": perm,
                    "coords": pt,
                    "max_power_sum_residual": res,
                }
            )

    # Pairwise Fubini-Study distances across all C(60, 2) = 1770 pairs
    min_fs_dist = mp.mpf("10")
    max_fs_dist = mp.mpf("0")
    pair_count = 0
    n_pts = len(points)
    for i in range(n_pts):
        ci = points[i]["coords"]
        for j in range(i + 1, n_pts):
            cj = points[j]["coords"]
            d = fubini_study_distance(ci, cj)
            pair_count += 1
            if d < min_fs_dist:
                min_fs_dist = d
            if d > max_fs_dist:
                max_fs_dist = d

    # Exact canonical lookup key for projective points with a unique repeated coordinate:
    # For each point in W_60, exactly two coordinates are equal; dividing by that repeated
    # coordinate recovers the exact normalized tuple in {1, r_0, r_1, r_2}^5.
    # Each transformed point g(P_i) is matched against P_j via Fubini-Study distance < 10^{-85}.
    s5_perms: list[tuple[int, ...]] = list(itertools.permutations(range(5)))
    tol_match = mp.mpf("1e-85")

    orbit_of_0: set[int] = set()
    stabilizer_orders: list[int] = []
    stabilizer_matches_transposition = True

    for i, p_info in enumerate(points):
        ci = p_info["coords"]
        a_i, b_i = p_info["transposition"]
        tau_perm = list(range(5))
        tau_perm[a_i], tau_perm[b_i] = tau_perm[b_i], tau_perm[a_i]
        tau_tuple = tuple(tau_perm)
        id_tuple = (0, 1, 2, 3, 4)

        stab_perms: list[tuple[int, ...]] = []
        for g in s5_perms:
            g_ci = tuple(ci[g[k]] for k in range(5))
            if fubini_study_distance(g_ci, ci) < tol_match:
                stab_perms.append(g)
            if i == 0:
                for j, q_info in enumerate(points):
                    if fubini_study_distance(g_ci, q_info["coords"]) < tol_match:
                        orbit_of_0.add(j)
                        break

        stabilizer_orders.append(len(stab_perms))
        if set(stab_perms) != {id_tuple, tau_tuple}:
            stabilizer_matches_transposition = False

    # Verify overlapping-transposition elimination identity (Section 3 of Lean file):
    # For z_0 = z_1 = z_2 = 1 and any (z_3, z_4),
    # s_1^3 - 9 s_1^2 + 36 s_1 - 3(s_1 - 3) s_2 + 2 s_3 = 60.
    z3_test, z4_test = roots[0], roots[1]
    s1_ov = mp.mpf("3") + z3_test + z4_test
    s2_ov = mp.mpf("3") + z3_test**2 + z4_test**2
    s3_ov = mp.mpf("3") + z3_test**3 + z4_test**3
    elim_val = (
        s1_ov**3
        - mp.mpf("9") * (s1_ov**2)
        + mp.mpf("36") * s1_ov
        - mp.mpf("3") * (s1_ov - mp.mpf("3")) * s2_ov
        + mp.mpf("2") * s3_ov
    )
    elim_err = abs(elim_val - mp.mpc(mp.mpf("60"), mp.mpf("0")))

    return {
        "transposition_count": len(transpositions),
        "fixed_points_per_transposition": len(s3_perms),
        "total_weierstrass_points": n_pts,
        "pair_count": pair_count,
        "max_bring_power_sum_residual": max_bring_res,
        "min_fubini_study_distance": min_fs_dist,
        "max_fubini_study_distance": max_fs_dist,
        "s5_order": len(s5_perms),
        "orbit_size_from_point_0": len(orbit_of_0),
        "min_stabilizer_order": min(stabilizer_orders),
        "max_stabilizer_order": max(stabilizer_orders),
        "stabilizer_equals_unique_transposition_subgroup": stabilizer_matches_transposition,
        "overlapping_elimination_identity_error": elim_err,
        "points": points,
    }


def evaluate_elliptic_quotient_j_invariant(
    roots: list[mp.mpc],
) -> dict[str, Any]:
    """Verify the genus-1 quotient E_tau = B / <tau> plane cubic, 6 branch points, and j(E_tau) = -25/2."""
    mp.mp.dps = COMPUTE_DPS
    two = mp.mpf("2")
    three = mp.mpf("3")
    five = mp.mpf("5")
    ten = mp.mpf("10")

    # 1. Verify all 6 fixed points (z_2, z_3, z_4) = sigma(r_0, r_1, r_2) satisfy both
    # the plane cubic F_tau = s_1^3 + 3 s_1 s_2 + 2 s_3 = 0 and the branch conic Q_tau = s_1^2 + 2 s_2 = 0
    max_cubic_branch_res = mp.mpf("0")
    for perm in itertools.permutations((0, 1, 2)):
        z2, z3, z4 = roots[perm[0]], roots[perm[1]], roots[perm[2]]
        s1 = z2 + z3 + z4
        s2 = z2**2 + z3**2 + z4**2
        s3 = z2**3 + z3**3 + z4**3
        f_tau = s1**3 + three * s1 * s2 + two * s3
        q_tau = s1**2 + two * s2
        res = max(abs(f_tau), abs(q_tau))
        if res > max_cubic_branch_res:
            max_cubic_branch_res = res

    # 2. Weierstrass invariants of E_tau: Y^2 = X^3 - 5 X^2 - 100 = t^3 - (25/3) t - 2950/27
    a_weier = -mp.mpf("25") / three
    b_weier = -mp.mpf("2950") / mp.mpf("27")
    c4 = -mp.mpf("48") * a_weier  # = 400
    c6 = -mp.mpf("864") * b_weier  # = 94400
    delta_weier = (c4**3 - c6**2) / mp.mpf("1728")  # = -5120000
    j_weier = (c4**3) / delta_weier  # = -25/2 = -12.5

    # 3. Independent 95-dps evaluation from the Legendre cross-ratio lambda of the 4 branch points
    # of E_tau -> P^1_w given by 4 w v^2 = -(w^3 + 5 w + 10), so the 4 branch points in w are
    # w_0 = 0 and the 3 roots w_1, w_2, w_3 of w^3 + 5 w + 10 = 0.
    # For w^3 + 5 w + 10 = 0: p = 5, q = 10, D = 25 + 125/27 = 800/27.
    disc_w = mp.sqrt(mp.mpf("800") / mp.mpf("27"))
    u_w = mp.root(-five + disc_w, 3)
    v_w = -mp.root(five + disc_w, 3)
    sqrt3 = mp.sqrt(three)
    omega = mp.mpc(-mp.mpf("1") / two, sqrt3 / two)
    omega2 = mp.mpc(-mp.mpf("1") / two, -sqrt3 / two)

    w_roots_init = [
        mp.mpc(u_w + v_w, mp.mpf("0")),
        omega * u_w + omega2 * v_w,
        omega2 * u_w + omega * v_w,
    ]
    w_roots: list[mp.mpc] = [mp.mpc("0", "0")]
    for z0 in w_roots_init:
        z = z0
        for _ in range(12):
            z = z - (z**3 + five * z + ten) / (three * (z**2) + five)
        w_roots.append(z)

    z0, z1, z2, z3 = w_roots
    lam = ((z0 - z2) * (z1 - z3)) / ((z0 - z3) * (z1 - z2))
    j_legendre = (
        mp.mpf("256")
        * ((mp.mpf("1") - lam + lam**2) ** 3)
        / ((lam**2) * ((mp.mpf("1") - lam) ** 2))
    )
    j_diff = abs(j_legendre - mp.mpc(j_weier, mp.mpf("0")))

    return {
        "max_cubic_and_conic_branch_residual": max_cubic_branch_res,
        "bezout_branch_point_count": 3 * 2,
        "weierstrass_A": a_weier,
        "weierstrass_B": b_weier,
        "c4": c4,
        "c6": c6,
        "discriminant_delta": delta_weier,
        "j_invariant_exact_rational": "-25/2",
        "j_invariant_weierstrass": j_weier,
        "j_invariant_legendre_cross_ratio": j_legendre,
        "j_invariant_agreement_error": j_diff,
        "quotient_genus": 1,
        "quotient_euler_characteristic": 0,
        "bring_riemann_hurwitz_euler_characteristic": 2 * 0 - 6,
        "bring_genus": 4,
    }


def main() -> int:
    mp.mp.dps = COMPUTE_DPS

    cubic_res = solve_transposition_cubic_95dps()
    roots = cubic_res["roots"]
    w60_res = build_sixty_weierstrass_points_and_verify_s5(roots)
    ell_res = evaluate_elliptic_quotient_j_invariant(roots)

    wb = WitnessBuilder("bring-transposition-weierstrass-sixty", engine="mpmath")
    wb.set_description(
        "80-dps / 95-dps-guard first-principles verification of the Bring transposition "
        "fixed-point cubic P_tau(t) = t^3 + 2 t^2 + 3 t + 4 = 0 (Delta = -200), all "
        "10 x 6 = 60 projective Weierstrass points across the 10 transpositions of S_5, "
        "pairwise Fubini-Study separation (> 0.45), transitive S_5 action with stabilizer "
        "order 120 / 60 = 2, and the genus-1 elliptic quotient E_tau = B / <tau> with "
        "Weierstrass form Y^2 = X^3 - 5 X^2 - 100 and exact j-invariant j(E_tau) = -25/2."
    )
    wb.set_content_block("lem:brings-euler-characteristic")

    wb.add_data(
        "transposition_cubic_P_tau",
        {
            "polynomial": "t^3 + 2*t^2 + 3*t + 4",
            "depressed_cubic": "y^3 + (5/3)*y + 70/27 (t = y - 2/3)",
            "cardano_sqrt_D": "(5*sqrt(6))/9",
            "cardano_U_cbrt_15sqrt6_minus_35_over_3": fmt80(
                cubic_res["cardano_u_cbrt_15sqrt6_minus_35_over_3"]
            ),
            "cardano_V_neg_cbrt_15sqrt6_plus_35_over_3": fmt80(
                cubic_res["cardano_v_neg_cbrt_15sqrt6_plus_35_over_3"]
            ),
            "cardano_r0_vs_newton_error": fmt80(
                cubic_res["cardano_r0_vs_newton_error"]
            ),
            "roots": [fmt_complex80(r) for r in roots],
            "max_cubic_residual": fmt80(cubic_res["max_cubic_residual"]),
            "vieta_error": fmt80(cubic_res["vieta_error"]),
            "power_sum_error": fmt80(cubic_res["power_sum_error"]),
            "discriminant_product": fmt_complex80(cubic_res["discriminant_product"]),
            "discriminant_error_vs_neg_200": fmt80(
                cubic_res["discriminant_error_vs_neg_200"]
            ),
        },
    )

    wb.add_data(
        "weierstrass_sixty_locus",
        {
            "transposition_count_C5_2": w60_res["transposition_count"],
            "fixed_points_per_transposition_3fact": w60_res[
                "fixed_points_per_transposition"
            ],
            "total_weierstrass_points": w60_res["total_weierstrass_points"],
            "pair_count_C60_2": w60_res["pair_count"],
            "max_bring_power_sum_residual": fmt80(
                w60_res["max_bring_power_sum_residual"]
            ),
            "min_fubini_study_distance": fmt80(w60_res["min_fubini_study_distance"]),
            "max_fubini_study_distance": fmt80(w60_res["max_fubini_study_distance"]),
            "s5_group_order": w60_res["s5_order"],
            "orbit_size_under_s5": w60_res["orbit_size_from_point_0"],
            "min_stabilizer_order": w60_res["min_stabilizer_order"],
            "max_stabilizer_order": w60_res["max_stabilizer_order"],
            "stabilizer_equals_unique_transposition_subgroup": w60_res[
                "stabilizer_equals_unique_transposition_subgroup"
            ],
            "overlapping_elimination_identity_error": fmt80(
                w60_res["overlapping_elimination_identity_error"]
            ),
        },
    )

    wb.add_data(
        "elliptic_quotient_E_tau",
        {
            "plane_cubic_equation": "(z_2 + z_3 + z_4)^3 + 3*(z_2 + z_3 + z_4)*(z_2^2 + z_3^2 + z_4^2) + 2*(z_2^3 + z_3^3 + z_4^3) = 0",
            "branch_conic_equation": "(z_2 + z_3 + z_4)^2 + 2*(z_2^2 + z_3^2 + z_4^2) = 0",
            "bezout_branch_point_count": ell_res["bezout_branch_point_count"],
            "max_cubic_and_conic_branch_residual": fmt80(
                ell_res["max_cubic_and_conic_branch_residual"]
            ),
            "weierstrass_model": "Y^2 = X^3 - 5*X^2 - 100 = t^3 - (25/3)*t - 2950/27",
            "c4": fmt80(ell_res["c4"]),
            "c6": fmt80(ell_res["c6"]),
            "discriminant_delta": fmt80(ell_res["discriminant_delta"]),
            "j_invariant_exact_rational": ell_res["j_invariant_exact_rational"],
            "j_invariant_weierstrass": fmt80(ell_res["j_invariant_weierstrass"]),
            "j_invariant_legendre_cross_ratio": fmt_complex80(
                ell_res["j_invariant_legendre_cross_ratio"]
            ),
            "j_invariant_agreement_error": fmt80(
                ell_res["j_invariant_agreement_error"]
            ),
            "quotient_genus": ell_res["quotient_genus"],
            "quotient_euler_characteristic": ell_res["quotient_euler_characteristic"],
            "bring_riemann_hurwitz_euler_characteristic": ell_res[
                "bring_riemann_hurwitz_euler_characteristic"
            ],
            "bring_genus": ell_res["bring_genus"],
        },
    )

    # Assertions
    wb.add_assertion(
        name="transposition_cubic_roots_max_residual_lt_1e_90",
        computed=fmt80(cubic_res["max_cubic_residual"]),
        expected="0",
        tolerance="1e-90",
        unit="dimensionless",
        source="Cardano + 95-dps Newton solution of P_tau(t) = t^3 + 2 t^2 + 3 t + 4 = 0",
    )
    wb.add_assertion(
        name="transposition_cubic_discriminant_eq_neg_200_lt_1e_88",
        computed=fmt80(mp.re(cubic_res["discriminant_product"])),
        expected="-200",
        tolerance="1e-88",
        unit="dimensionless",
        source="transposition_cubic_discriminant_eq_neg_200 in BringTranspositionSixFixedPointsAndEllipticQuotient.lean",
    )
    wb.add_assertion(
        name="sixty_weierstrass_points_on_bring_curve_lt_1e_88",
        computed=fmt80(w60_res["max_bring_power_sum_residual"]),
        expected="0",
        tolerance="1e-88",
        unit="dimensionless",
        source="p_1 = p_2 = p_3 = 0 across all 10 x 6 = 60 transposition fixed points on Bring's curve",
    )
    wb.add_assertion(
        name="sixty_weierstrass_points_pairwise_fubini_study_distinct",
        computed="1"
        if (
            w60_res["pair_count"] == 1770
            and w60_res["min_fubini_study_distance"] > mp.mpf("0.4")
        )
        else "0",
        expected="1",
        tolerance="0",
        unit="dimensionless",
        source="Fubini-Study projective distance > 0.4 across all C(60, 2) = 1770 pairs in P^4(C)",
    )
    wb.add_assertion(
        name="s5_acts_transitively_with_stabilizer_order_two",
        computed=str(w60_res["orbit_size_from_point_0"])
        if (
            w60_res["s5_order"] == 120
            and w60_res["min_stabilizer_order"] == 2
            and w60_res["max_stabilizer_order"] == 2
            and w60_res["stabilizer_equals_unique_transposition_subgroup"]
            and w60_res["overlapping_elimination_identity_error"] < mp.mpf("1e-88")
        )
        else "0",
        expected="60",
        tolerance="0",
        unit="cardinality",
        source="Transitive S_5 action on W_60 with Stab_{S_5}(P_{(a,b),sigma}) = {e, tau_{a,b}} of order 120/60 = 2",
    )
    wb.add_assertion(
        name="elliptic_quotient_j_invariant_eq_neg_25_over_2_lt_1e_88",
        computed=fmt80(mp.re(ell_res["j_invariant_legendre_cross_ratio"])),
        expected="-12.5",
        tolerance="1e-88",
        unit="dimensionless",
        source="Weierstrass and Legendre cross-ratio j-invariant j(E_tau) = -25/2 of E_tau = B / <tau>",
    )

    out_path = wb.save(
        {
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Purely algebro-geometric calculation on Bring's curve B in P^4(C) "
                "and its transposition quotient E_tau = B / <tau>; no substrate "
                "parameter q0 is read."
            ),
        }
    )
    print(f"Wrote witness to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
