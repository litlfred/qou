#!/usr/bin/env python3
"""The Z=1..20 mass table, regenerated in convention D. (bean qou-1jw9)

AUTHORISED by the owner 2026-08-29: "recompute Phi_1 (and anything else
convention C -> D)", after the measurement in phi1_convention_d_probe.py showed
the carried Phi_1 is a convention-C artifact that convention D cannot reach.

WHAT CHANGES, AND WHY EACH IS A DERIVATION RATHER THAN A CARRY.

  Phi_2, Phi_3 -- no longer carried from the recovered witness at all. Both are
  now COMPUTED from the strand content and the crossing values proved
  sorry-free in HeckeLinearReduction.lean:

      Phi_3 = (-2Z - N(N-1)) * ln q          [= 2(2C(Z,2) - C(N,2) - Z^2) ln q]
      Phi_2 = Z*N * ln(1 + h^2/4)

  Each reproduced all 19 non-hydrogen carried values exactly
  (phi_allpairs_reconstruction.py), so replacing the carry with the derivation
  is value-neutral for these two. Both are CONVENTION-FREE -- neither uses the
  Markov parameter z -- so the C->D move does not touch them.

  Phi_1 -- recomputed. It is the only invariant that uses z, hence the only one
  the convention ruling can move. Computed here in convention D only
  (z = q^3/(q^2+1)), under the ALL-PAIRS chain structure the theorem's own
  prose specifies ("chaining the crossing matrices of all strands j > i" =
  for strand i, cross with every strand j > i), minimised over orderings per
  def:atomic-braid's ground-state rule.

THE MINIMISATION IS EXPONENTIAL AND IS NOT BRUTE-FORCED. C(40,20) = 1.4e11 at
Ca. This uses swap hill-climbing with restarts over nuclear arrangements. It is
VALIDATED, not assumed: on the five atoms where exhaustive enumeration is
feasible (He, Li, Be, B, C -- up to 924 arrangements) the local search finds the
exact global minimum in all five cases. For heavier atoms the result is a local
minimum that may not be global; every row records which regime it is in.

H IS EXCLUDED from the accuracy statistics. def:atomic-braid gives hydrogen a
special pe crossing (B_3-dressed eigenvalues), which this construction does not
implement, and its carried Phi_3 = +10 ln q is outside the Table-1 accounting.

NO FITTING. alpha = m_e * 8G, beta_2 = -2[3]_q and beta_3 = h_A^2 are the
published coefficients evaluated at q0; the AME2020 column is used only to
report error, never to choose anything.
"""
from __future__ import annotations

import random
import sys
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

from qou_substrate.constants import q_at  # mpmath-native proton pin; NOT the f64 `Q`
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION
from codata_constants import M_C12_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

# q0 at full working precision. `constants.Q` is `_solve_q_proton_f64` -- a
# float64 solve -- so `mpf(str(Q))` would inflate a double's error to 50 dps
# and every value below would carry it. `q_at` solves in mpmath at the same
# (proton) pin. Flagged as the corpus's only `mpf(str(<f64>))` laundering
# site by computations/f64_into_mpmath_audit.py.
Q = q_at(50)
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)
M_E, M_P, M_N = mp.mpf("0.51099895"), M_P_MEV_VALIDATION, M_N_MEV_VALIDATION
ALPHA = M_E * 8 * mp.catalan
BETA2 = -2 * (Q ** 2 + 1 + Q ** -2)
BETA3 = H ** 2

def s20(x, n=20):
    """mpf -> decimal string at n digits. Never float() -- the value must reach
    the witness as text carrying its own precision, per the NO-FLOAT64 rule."""
    return mp.nstr(x, n, strip_zeros=False)


TBL = {("p", "p"): (1, mp.mpf(0)), ("n", "n"): (1, -H), ("p", "n"): (1, -H / 2),
       ("p", "e"): (1, -H), ("n", "e"): (0, mp.mpf(1)), ("e", "e"): (1, mp.mpf(0))}
EXACT_UPTO = 924          # arrangements we are willing to enumerate exhaustively


def cr(a, b):
    return TBL[(a, b)] if (a, b) in TBL else TBL[(b, a)]


def V(chain):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c = mp.mpf(c)
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return Z_D * a + b


def phi1(seq):
    n = len(seq)
    t = mp.mpf(0)
    for i in range(n):
        ch = [cr(seq[i], seq[j]) for j in range(i + 1, n)]
        if ch:
            t += mp.log(abs(V(ch)))
    return t


def phi2(Z, N):
    return Z * N * mp.log(1 + H ** 2 / 4)


def phi3(Z, N, lnq):
    return mp.mpf(-2 * Z - N * (N - 1)) * lnq


def nuc_to_seq(nuc):
    s = []
    for c in nuc:
        s.extend(["e", "p"]) if c == "p" else s.append("n")
    return s


def minimise(Z, N, restarts=4, seed=0):
    """Swap hill-climbing; validated against exhaustive search on Z<=6."""
    rng = random.Random(seed)
    base = list("p" * Z + "n" * N)
    k = min(Z, N)
    starts = [list("pn" * k) + list("n" * (N - k)) + list("p" * (Z - k))]
    for _ in range(restarts - 1):
        c = base[:]
        rng.shuffle(c)
        starts.append(c)
    best = None
    for st in starts:
        cur, cv = st[:], phi1(nuc_to_seq(st))
        improved = True
        while improved:
            improved = False
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    if cur[i] == cur[j]:
                        continue
                    cand = cur[:]
                    cand[i], cand[j] = cand[j], cand[i]
                    v = phi1(nuc_to_seq(cand))
                    if v < cv:
                        cur, cv, improved = cand, v, True
        if best is None or cv < best[0]:
            best = (cv, cur[:])
    return best


# (atom, Z, N, M_obs AME2020 as recorded, M_pred as published in convention C)
ROWS = [
    ("H", 1, 0, "938.78313", "938.910"),      ("He", 2, 2, _ame_nstr(M_HE4_ATOMIC_MEV_VALIDATION, 30), "3734.624"),
    ("Li", 3, 4, "6535.367", "6534.188"),     ("Be", 4, 5, "8394.7937", "8378.704"),
    ("B", 5, 6, "10255.103", "10237.301"),    ("C", 6, 6, _ame_nstr(M_C12_ATOMIC_MEV_VALIDATION, 30), "11168.874"),
    ("N", 7, 7, "13043.7816", "13029.983"),   ("O", 8, 8, "14899.1693", "14890.701"),
    ("F", 9, 10, "17696.901", "17690.792"),   ("Ne", 10, 10, "18622.8354", "18615.219"),
    ("Na", 11, 12, "21414.8301", "21418.256"), ("Mg", 12, 12, "22341.908", "22342.658"),
    ("Al", 13, 14, "25133.1432", "25143.149"), ("Si", 14, 14, "26060.3443", "26067.918"),
    ("P", 15, 16, "28851.873", "28872.696"),  ("S", 16, 16, "29781.8", "29797.187"),
    ("Cl", 17, 18, "32573.283", "32597.913"), ("Ar", 18, 22, "37224.719", "37273.796"),
    ("K", 19, 20, "36294.464", "36324.625"),  ("Ca", 20, 20, "37213.777", "37248.739"),
]


def main() -> int:
    lnq = mp.log(Q)
    print(f"convention D:  z = q^3/(q^2+1) = {mp.nstr(Z_D, 16)}")
    print(f"q0 (proton pin) = {mp.nstr(Q, 18)}")
    print(f"alpha = m_e*8G = {mp.nstr(ALPHA, 12)}   beta2 = {mp.nstr(BETA2, 12)}"
          f"   beta3 = h_A^2 = {mp.nstr(BETA3, 12)}\n")
    print(f"{'atom':>5} {'Z':>3} {'N':>3} {'Phi_1 (D)':>13} {'Phi_2':>11} "
          f"{'Phi_3':>12} {'M_pred D':>12} {'M_obs':>12} {'err %':>9} "
          f"{'vs C-pub':>10} {'regime':>7}")
    print("-" * 122)
    errs = []
    rows = []
    for el, Z, N, mobs, mpub in ROWS:
        p1, _ = minimise(Z, N)
        p2 = phi2(Z, N)
        p3 = phi3(Z, N, lnq)
        corr = ALPHA * (p1 + BETA2 * p2 + BETA3 * p3)
        base = Z * M_P + N * M_N + Z * M_E
        pred = base + corr
        obs = mp.mpf(mobs)
        err = (pred - obs) / obs * 100
        shift = pred - mp.mpf(mpub)
        regime = "exact" if comb(Z + N, Z) <= EXACT_UPTO else "local"
        if el != "H":
            errs.append(abs(err))
        rows.append({
            "atom": el, "Z": Z, "N": N, "A": Z + N,
            "Phi_1": s20(p1), "Phi_2": s20(p2), "Phi_3": s20(p3),
            "M_pred_MeV": s20(pred), "M_obs_MeV": mobs,
            "delta_MeV": s20(pred - obs), "err_pct": s20(err),
            "shift_from_published_C_MeV": s20(shift),
            "ordering_regime": regime,
        })
        print(f"{el:>5} {Z:>3} {N:>3} {mp.nstr(p1,8):>13} {mp.nstr(p2,7):>11} "
              f"{mp.nstr(p3,8):>12} {mp.nstr(pred,10):>12} {mobs:>12} "
              f"{mp.nstr(err,4):>9} {mp.nstr(shift,6):>10} {regime:>7}")
    mean = mp.fsum(errs) / len(errs)
    print(f"\n  convention D, H excluded: mean |err| = {mp.nstr(mean,6)} %   "
          f"max = {mp.nstr(max(errs),6)} %   over {len(errs)} rows")
    print(f"  published convention-C table reported mean 0.0745925 %, max 0.190854 %")
    print("\n  'exact' = the ordering minimum is the global one (exhaustive search")
    print("  feasible); 'local' = hill-climbing minimum, validated against exhaustive")
    print("  search on all five feasible atoms but not proved global here.")

    wb = WitnessBuilder("wedderburn-mass-table-convention-d", engine="mpmath")
    wb.set_description(
        "Z=1-20 atomic mass table under the CANONICAL Markov convention D "
        "(z = q^3/(q^2+1)), owner ruling 2026-08-15. Supersedes the "
        "convention-C table for publication. Phi_2 and Phi_3 are DERIVED "
        "(convention-free, no z); only Phi_1 is convention-dependent and is "
        "recomputed here. Accuracy is WORSE than the superseded C table -- "
        "reported as measured, not presented as an improvement.")
    wb.set_content_block("tbl:mass-table-z1-20-table-data")
    wb.add_parameter("q0", s20(Q))
    wb.add_parameter("q0_anchor", "physical_proton")
    wb.add_parameter("markov_convention", "D")
    wb.add_parameter("markov_z", s20(Z_D))
    wb.add_parameter("m_e_MeV", s20(M_E))
    wb.add_parameter("m_p_MeV", s20(M_P))
    wb.add_parameter("m_n_MeV", s20(M_N))
    wb.add_parameter("alpha", s20(ALPHA))
    wb.add_parameter("beta2", s20(BETA2))
    wb.add_parameter("beta3", s20(BETA3))
    wb.add_parameter("fitted_parameters", 0)
    wb.add_data("rows", rows)
    wb.add_data("summary", {
        "n_rows_scored": len(errs),
        "hydrogen_excluded": True,
        "mean_abs_err_pct": s20(mean),
        "max_abs_err_pct": s20(max(errs)),
        "superseded_C_mean_abs_err_pct": "0.0745925",
        "superseded_C_max_abs_err_pct": "0.190854",
        "accuracy_note": (
            "D is LESS accurate than the superseded C table by a factor of "
            "~2.4 on the mean. Recorded as measured. The C/D choice was made "
            "on convention grounds (owner ruling 2026-08-15), not accuracy."),
    })
    wb.add_data("ordering_regimes", {
        "exact": sum(1 for r in rows if r["ordering_regime"] == "exact"),
        "local": sum(1 for r in rows if r["ordering_regime"] == "local"),
        "note": ("'exact' = exhaustive ordering search feasible and the "
                 "minimum is global. 'local' = hill-climbing; validated "
                 "against exhaustive search on every atom where exhaustive "
                 "is feasible, but not proved global on the rest."),
    })
    # Both assertions below were `computed=X, expected=X` on the same literal
    # (bean `qou-26f2`) — `True==True` and `0==0` — so each recorded
    # `passed:true` without evaluating anything. Both restated as measurements.

    # (1) CONVENTION-FREENESS, MEASURED. The claim is that Phi_2 and Phi_3 do
    #     not read the Markov parameter z, so only Phi_1 can move under the
    #     C -> D ruling. Re-evaluate all three at a SECOND z and compare. The
    #     Phi_1 leg is the positive control and is the part that can fail
    #     informatively: without it, "Phi_2 and Phi_3 did not move" would also
    #     hold if z had stopped reaching the pipeline at all, which is the
    #     failure the ruling is most exposed to.
    #
    #     The perturbation rebinds the MODULE GLOBAL rather than passing a
    #     parameter, because the claim is about what these functions read, and
    #     a parameter this file added for the test would not be that.
    seq_probe = nuc_to_seq(list("ppnn"))     # fixed arrangement, no search
    base_p1 = phi1(seq_probe)
    base_23 = [(phi2(Z_, N_), phi3(Z_, N_, lnq)) for _, Z_, N_, _, _ in ROWS]
    _z_saved = Z_D
    try:
        globals()["Z_D"] = _z_saved * 2 + 1   # any z != z_D; not a convention
        alt_p1 = phi1(seq_probe)
        alt_23 = [(phi2(Z_, N_), phi3(Z_, N_, lnq)) for _, Z_, N_, _, _ in ROWS]
    finally:
        globals()["Z_D"] = _z_saved
    dphi1 = abs(alt_p1 - base_p1)
    n_phi23_stable = sum(1 for a, b in zip(base_23, alt_23) if a == b)
    print(f"\n  convention-freeness: Phi_1 moves by {mp.nstr(dphi1, 8)} under a "
          f"second z; Phi_2/Phi_3 unmoved on {n_phi23_stable}/{len(ROWS)} rows")
    wb.add_assertion(
        "phi_2_and_phi_3_unmoved_by_z",
        computed=str(n_phi23_stable),
        expected=str(len(ROWS)),
        tolerance=0,
        unit="table rows whose (Phi_2, Phi_3) are bit-identical at a second z",
        source=("z_D rebound to 2·z_D + 1 and both invariants recomputed for "
                "every row. Phi_2 = Z·N·ln(1 + h²/4), Phi_3 = (−2Z − N(N−1))·ln q "
                "— neither should see the Markov parameter."),
    )
    wb.add_assertion(
        "phi_1_does_move_with_z",
        computed=str(int(dphi1 > 0)),
        expected="1",
        tolerance=0,
        unit="1 if Phi_1 responds to the same z perturbation",
        source=("positive control for the assertion above: without it, "
                "'Phi_2/Phi_3 did not move' would also hold if z had stopped "
                f"reaching V() at all. Measured |ΔPhi_1| = {mp.nstr(dphi1, 8)} "
                f"on the fixed ppnn arrangement."),
    )

    # (2) THE PHI_3 IDENTITY THE DOCSTRING STATES BUT NEVER CHECKED. The module
    #     header gives two forms — (−2Z − N(N−1))·ln q and
    #     2(2·C(Z,2) − C(N,2) − Z²)·ln q — and only the first is used. The
    #     second is an independent route to the same integer coefficient.
    n_phi3_comb = sum(
        1 for (el, Z_, N_, _, _) in ROWS
        if (-2 * Z_ - N_ * (N_ - 1))
        == 2 * (2 * comb(Z_, 2) - comb(N_, 2) - Z_ ** 2)
    )
    wb.add_assertion(
        "phi_3_coefficient_matches_its_combinatorial_form",
        computed=str(n_phi3_comb),
        expected=str(len(ROWS)),
        tolerance=0,
        unit="rows where both docstring forms of the Phi_3 coefficient agree",
        source=("module docstring: Phi_3 = (−2Z − N(N−1))·ln q "
                "[= 2(2·C(Z,2) − C(N,2) − Z²)·ln q]. Only the first is used to "
                "build the table; the second is evaluated here as a check."),
    )

    # (3) NO FITTED PARAMETERS, MADE MECHANICAL. "Every coefficient from q0,
    #     m_e and Catalan" is refutable: re-derive each of the three from a
    #     second closed form. A coefficient nudged to improve the AME column
    #     stops reproducing.
    #       alpha  = m_e·8G,  G re-derived as the Dirichlet beta series
    #                Σ (−1)^k/(2k+1)² rather than mp.catalan
    #       beta_2 = −2[3]_q, [3]_q re-derived as (q³−q⁻³)/(q−q⁻¹) rather than
    #                the expanded q²+1+q⁻²
    #       beta_3 = h_A²,   re-derived as q² − 2 + q⁻² rather than (q−1/q)²
    G_series = mp.nsum(lambda k: (-1) ** k / (2 * k + 1) ** 2, [0, mp.inf])
    redrv = {
        "alpha": (ALPHA, M_E * 8 * G_series),
        "beta2": (BETA2, -2 * (Q ** 3 - Q ** -3) / (Q - Q ** -1)),
        "beta3": (BETA3, Q ** 2 - 2 + Q ** -2),
    }
    coef_resid = max(abs(a - b) / abs(a) for a, b in redrv.values())
    coef_floor = mp.mpf(10) ** -(mp.mp.dps - 10)
    print(f"  coefficient re-derivation: max relative residual "
          f"{mp.nstr(coef_resid, 6)} (floor {mp.nstr(coef_floor, 3)})")
    wb.add_data("coefficient_rederivation", {
        k: {"used": s20(a), "second_route": s20(b),
            "rel_residual": mp.nstr(abs(a - b) / abs(a), 8)}
        for k, (a, b) in redrv.items()})
    wb.add_assertion(
        "coefficients_reproduce_from_a_second_closed_form",
        computed=mp.nstr(coef_resid, 8),
        expected="0",
        tolerance=mp.nstr(coef_floor, 3),
        unit="max relative residual over alpha, beta_2, beta_3",
        source=("alpha = m_e·8G vs Dirichlet beta series for G; beta_2 = "
                "−2(q²+1+q⁻²) vs −2(q³−q⁻³)/(q−q⁻¹); beta_3 = (q−1/q)² vs "
                "q²−2+q⁻². None of the three reads the AME column. "
                "Floor = 10^-(dps−10)."),
    )
    out = wb.save()
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
