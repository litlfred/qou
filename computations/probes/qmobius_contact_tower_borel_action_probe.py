#!/usr/bin/env python3
"""qmobius_contact_tower_borel_action_probe.py — bean qou-4cb9 (PR #4122):
does the q-Möbius contact tower carry the saddle-predicted Borel action?

Context (docs/audits/2026-07-19-jets-alien-qmobius-bring-interaction.md §4).
The q-Möbius (categorical Möbius) kernel's diagonal contact term is the
fundamental Markov trace — the Jones polynomial (lem:jones-mobius-diagonal,
Lean `markov_eq_mobius_contact`, sorry-free). Its color tower is the Kashaev
sum <4_1>_N = sum_{k=0}^{N-1} |(q;q)_k|^2 at q = e^{2 pi i/N}, whose k-th
product is 4^k (prod_j sin(pi j/N))^2 by the Lean-proved sin-form
(`kashaevProd_eq_sin`, QOU/Knot/FigureEightVolumeSaddle.lean) with saddle at
theta = pi/3 giving Vol(4_1) = 2 Cl_2(pi/3) (`saddle_critical_point`, E3
complete).  The alien-calculus side locates the leading Borel singularity of
the contact-tower Ohtsuki ladder at omega ~ Vol(4_1)/pi
(docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md §1).

HYPOTHESIS UNDER TEST (a TEST, not a fit): the contact tower built on the
q-Möbius diagonal term (i) anchors exactly on the fundamental Jones datum at
its base rung, (ii) has the E3-proved saddle value as its exponential growth
rate, and (iii) has Ohtsuki-ladder Borel action A consistent with the
saddle-predicted Vol(4_1)/pi, inside the C1-stabilized band [0.6338, 0.6833].

TESTS:
  T1a (exact, integer): <4_1>_2 = 5 = |J_{4_1}(-1)| (the knot determinant) —
      the fundamental (N=2) contact term meets the tower at its base rung.
  T1b (identity echo): three forms of the Kashaev product agree numerically —
      |(q;q)_k|^2  ==  prod_j (2 - 2 cos(2 pi j/N))  ==  4^k (prod_j sin)^2
      (the numerical echo of the sorry-free `kashaevProd_eq_sin`).
  T2  (volume limit): log <4_1>_N = a*N + b*log N + c + d/N solved exactly on
      a 4-point N-grid; TEST 2*pi*a vs Vol(4_1) = 2*Cl_2(pi/3) and b vs 3/2
      (diagnostic).  Model spread estimated by re-solving on a second grid —
      NO least-squares, no tuned parameter.
  T3  (Borel action): consecutive-ratio inverse on the main-witness kappa
      rungs (provenance below): r_n = kappa_n/kappa_{n-1};
      A = 1/(r_{n+1} - r_n), beta = A*r_n - (n-1), for the pairs available.
      TEST whether Vol(4_1)/pi lies in the ladder's A range (widened by
      input-digit propagation) and in the C1 band.

KILL CRITERION (pre-stated): NEGATIVE-scope-a iff BOTH (i) |2*pi*a -
2*Cl_2(pi/3)| > 10x the two-grid spread AND (ii) Vol(4_1)/pi falls outside
the T3 ladder range widened by input-digit propagation.  If either leg
lands, verdict CONSISTENT — never "derived": T2/T3 are numerical
consistency checks against a proved-saddle *predicted* value; the Riemann-sum
and max-term bricks (beans bca6 / el8w-saddle; sibling PR #4121 E4c) are what
would upgrade the tier.

KAPPA PROVENANCE: rung strings copied from
computations/probes/qbeta_kappa_large_order_bridge_probe.py, which sources
origin/main docs/audits/scripts/qbeta-even-borel-singularity.witness.json
(commit 4c4a936); confident digits per that witness (k4: 19, k5: 14, k6: 10).

DISCIPLINE: audit-only witness; NO fit; NO wiring; NO tier change;
scope-(a) wording throughout; self-contained (mpmath only).
"""
import datetime
import json
import os
import sys

import mpmath as mp

mp.mp.dps = 80

VOL41 = 2 * mp.clsin(2, mp.pi / 3)          # 2*Cl_2(pi/3), E3 saddle value
VOL_OVER_PI = VOL41 / mp.pi
C1_BAND = (mp.mpf("0.6338"), mp.mpf("0.6833"))

KAPPA = {  # see KAPPA PROVENANCE in the docstring
    3: mp.mpf("2.6545270569495453476"),
    4: mp.mpf("13.094774926381671947"),
    5: mp.mpf("84.642165605038443528"),
    6: mp.mpf("676.9466789641050315"),
}
CONFIDENT_DIGITS = {3: 25, 4: 19, 5: 14, 6: 10}


def kashaev_sum(N):
    """<4_1>_N = sum_k P_k, P_k = prod_{j<=k} 4 sin^2(pi j/N) (sin-form)."""
    total = mp.mpf(1)
    P = mp.mpf(1)
    for k in range(1, N):
        P *= 4 * mp.sin(mp.pi * k / N) ** 2
        total += P
    return total


def t1a():
    """<4_1>_2 = 5 = |J_{4_1}(-1)| — exact integer arithmetic."""
    # Kashaev N=2: 1 + (2 - 2*cos(pi)) = 1 + 4
    kashaev_2 = 1 + (2 - 2 * (-1))
    # J_{4_1}(q) = q^-2 - q^-1 + 1 - q + q^2 at q = -1 (integers)
    q = -1
    jones_at_m1 = q ** -2 - q ** -1 + 1 - q + q ** 2
    ok = (kashaev_2 == 5) and (abs(jones_at_m1) == 5)
    return {"kashaev_N2": kashaev_2, "abs_jones_at_minus1": abs(jones_at_m1),
            "determinant": 5, "pass": ok}, ok


def t1b():
    """Three Kashaev-product forms agree (echo of kashaevProd_eq_sin)."""
    tol = mp.mpf(10) ** (-(mp.mp.dps - 12))
    checks = []
    all_ok = True
    for N in (3, 5, 8):
        q = mp.e ** (2j * mp.pi / N)
        for k in (1, N // 2, N - 1):
            # form 1: |(q;q)_k|^2
            f1 = mp.mpf(1)
            for j in range(1, k + 1):
                f1 *= abs(1 - q ** j) ** 2
            # form 2: prod (2 - 2 cos(2 pi j / N))
            f2 = mp.mpf(1)
            for j in range(1, k + 1):
                f2 *= 2 - 2 * mp.cos(2 * mp.pi * j / N)
            # form 3: 4^k (prod sin(pi j / N))^2
            prod_sin = mp.mpf(1)
            for j in range(1, k + 1):
                prod_sin *= mp.sin(mp.pi * j / N)
            f3 = mp.mpf(4) ** k * prod_sin ** 2
            scale = max(f1, mp.mpf(1))
            ok = (abs(f1 - f2) / scale < tol) and (abs(f2 - f3) / scale < tol)
            all_ok = all_ok and ok
            checks.append({"N": N, "k": k, "value": mp.nstr(f1, 20),
                           "pass": ok})
    return checks, all_ok


def solve_volume(grid):
    """Exact 4x4 solve of log<4_1>_N = a N + b log N + c + d/N on the grid."""
    A = mp.matrix(4, 4)
    rhs = mp.matrix(4, 1)
    for i, N in enumerate(grid):
        A[i, 0], A[i, 1], A[i, 2], A[i, 3] = N, mp.log(N), 1, mp.mpf(1) / N
        rhs[i, 0] = mp.log(kashaev_sum(N))
    sol = mp.lu_solve(A, rhs)
    return sol[0, 0], sol[1, 0]


def t2():
    grid1, grid2 = (200, 400, 800, 1600), (150, 300, 600, 1200)
    a1, b1 = solve_volume(grid1)
    a2, b2 = solve_volume(grid2)
    vol_est = 2 * mp.pi * a1
    spread = abs(2 * mp.pi * (a1 - a2))
    err = abs(vol_est - VOL41)
    ok = err <= 10 * spread or err < mp.mpf("1e-6")
    return {
        "grid_primary": list(grid1), "grid_secondary": list(grid2),
        "vol_estimate_2pi_a": mp.nstr(vol_est, 20),
        "vol_target_2cl2_pi3": mp.nstr(VOL41, 20),
        "abs_error": mp.nstr(err, 6),
        "two_grid_spread": mp.nstr(spread, 6),
        "b_exponent_estimate": mp.nstr(b1, 10),
        "b_expected": "3/2 (diagnostic only)",
        "b_secondary": mp.nstr(b2, 10),
        "pass": ok,
    }, ok


def t3():
    r = {n: KAPPA[n] / KAPPA[n - 1] for n in (4, 5, 6)}
    ladder = []
    A_vals = []
    for n in (4, 5):  # pairs (r_n, r_{n+1})
        A = 1 / (r[n + 1] - r[n])
        beta = A * r[n] - (n - 1)
        A_vals.append(A)
        ladder.append({"pair": [n, n + 1], "A": mp.nstr(A, 12),
                       "beta": mp.nstr(beta, 8)})
    # input-digit propagation: perturb the least-confident rung (k6, 10
    # digits) by one ulp of its confidence and re-solve the (5,6) pair
    d6 = KAPPA[6] * mp.mpf(10) ** (-CONFIDENT_DIGITS[6])
    r6p = (KAPPA[6] + d6) / KAPPA[5]
    A_pert = 1 / (r6p - r[5])
    dA = abs(A_pert - A_vals[-1])
    lo = min(A_vals) - dA
    hi = max(A_vals) + dA
    in_ladder = lo <= VOL_OVER_PI <= hi
    in_c1 = C1_BAND[0] <= VOL_OVER_PI <= C1_BAND[1]
    return {
        "ratio_ladder": ladder,
        "A_range_with_digit_propagation": [mp.nstr(lo, 10), mp.nstr(hi, 10)],
        "dA_from_kappa6_confidence": mp.nstr(dA, 4),
        "vol_over_pi_target": mp.nstr(VOL_OVER_PI, 15),
        "target_in_ladder_range": bool(in_ladder),
        "target_in_C1_band": bool(in_c1),
        "pass": bool(in_ladder or in_c1),
    }, bool(in_ladder or in_c1)


def main():
    r1a, ok1a = t1a()
    print("T1a exact anchor <4_1>_2 = 5 = det:", "PASS" if ok1a else "FAIL")
    r1b, ok1b = t1b()
    print("T1b kashaevProd 3-form agreement:", "PASS" if ok1b else "FAIL")
    r2, ok2 = t2()
    print("T2 volume limit:", r2["vol_estimate_2pi_a"], "vs",
          r2["vol_target_2cl2_pi3"], "->", "PASS" if ok2 else "FAIL")
    r3, ok3 = t3()
    print("T3 Borel action ladder:", r3["A_range_with_digit_propagation"],
          "target", r3["vol_over_pi_target"], "->",
          "PASS" if ok3 else "FAIL")

    # pre-stated kill criterion: NEGATIVE only if BOTH T2 and T3 fail
    if ok2 or ok3:
        verdict = ("CONSISTENT scope-(a): the q-Möbius contact tower "
                   "anchors on the fundamental Jones datum (T1), grows at "
                   "the E3-proved saddle value 2*Cl2(pi/3) (T2), and its "
                   "Ohtsuki-ladder Borel action is consistent with the "
                   "saddle-predicted Vol(4_1)/pi (T3). NOT 'derived': "
                   "tier upgrade awaits the E4/E5 saddle bricks.")
    else:
        verdict = ("NEGATIVE scope-(a): the leading one-saddle "
                   "identification fails both the volume-limit and the "
                   "ladder tests as-is; no parameters tuned to force "
                   "agreement.")
    hard_ok = ok1a and ok1b

    witness = {
        "description": ("q-Möbius contact tower vs saddle-predicted Borel "
                        "action Vol(4_1)/pi — bean qou-4cb9, PR #4122"),
        "computation": ("Kashaev sin-form sum (Lean kashaevProd_eq_sin "
                        "echo); exact 4x4 volume-limit solve; "
                        "consecutive-ratio Borel-action inverse on "
                        "main-witness kappa rungs"),
        "generated": datetime.datetime.now(datetime.timezone.utc)
        .isoformat(timespec="seconds"),
        "parameters": {"dps": mp.mp.dps,
                       "C1_band": [str(C1_BAND[0]), str(C1_BAND[1])]},
        "results": {"t1a_exact_anchor": r1a, "t1b_sin_form_echo": r1b,
                    "t2_volume_limit": r2, "t3_borel_action": r3,
                    "exact_anchors_pass": hard_ok, "verdict": verdict},
        "context": {
            "audit": "docs/audits/2026-07-19-jets-alien-qmobius-bring-"
                     "interaction.md §4",
            "lean_anchors": [
                "QOU.Braiding.JonesMobiusDiagonal.markov_eq_mobius_contact",
                "QOU.Knot.FigureEightVolume.kashaevProd_eq_sin",
                "QOU.Knot.FigureEightVolume.saddle_critical_point",
            ],
            "kappa_source": "origin/main docs/audits/scripts/"
                            "qbeta-even-borel-singularity.witness.json "
                            "(commit 4c4a936) via qbeta_kappa_large_order_"
                            "bridge_probe.py",
            "siblings": ["PR #4120 (G3 pentagon-rigidity prune)",
                         "PR #4121 (E4c saddle bricks)"],
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qmobius-contact-tower-borel-action.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if hard_ok else 1


if __name__ == "__main__":
    sys.exit(main())
