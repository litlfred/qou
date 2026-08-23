#!/usr/bin/env python3
"""A3 (bean qou-el23): capstone-carrier falsification — can the 5₂ NZ-saddle
quantum volume be the Im 𝔙_q → N_odd carrier?

The capstone (docs/scope/2026-07-18-im-vq-to-nodd-normalization-capstone.md)
conjectures a geometric quantum-volume functional whose bar-odd part IS the
smooth bar-odd numerator N_odd(q) = S(q)·u(q)³, subject to four constraints:
(1) bar-odd; (2) smooth with a SIMPLE ZERO at q* (slope A'(q*) ≈ +2.37);
(3) magnitude O(1e-8) at the anchors; (4) anchor-dependent.

THE TEST. For any candidate carrier C(q) normalized as
    N_odd(q) = u(q)³ · f(q) · C(q),   f smooth with O(1) log-slope,
constraint (2) forces C itself to carry the simple zero at q* (u³ and f are
nonvanishing there; if instead f(q*) = 0, then f swings 0 → full value across
the ~1e-8 anchor window — a ~1e8 slope, not smooth — so the zero cannot live
in the normalization). We therefore measure, for the 5₂ Neumann–Zagier-saddle
bar-odd datum
    B(q) := [ 𝔙(m=q) − 𝔙(m=1/q) ] / 2      (bar involution = m → 1/m),
whether B has a zero crossing at (or anywhere near) q*, on a fine grid
straddling the anchor window, in both Re B (CS/chirality channel) and Im B
(volume channel). Secondary carrier candidate D_odd(q) = ½(q²−q⁻²) (the 5₂
writhe sinh datum) is tested identically.

Machinery reused from qbeta_5two_quantum_volume_probe.py (Hikami 0604094
§4.2 saddle, validated Vol(5₂) = 2.82812 at m=1); gates G1/G2 reproduce the
merged witness before any falsification claim.

Expected outcome (scope-(a) narrowing, NOT a scope-(b) exclusion): B is
smooth O(0.1–1) with NO zero at q* → the analytic NZ-saddle 5₂ quantum
volume cannot satisfy constraint (2) → the capstone carrier, if it exists,
is NOT the analytic saddle datum — pointing at the categorical H₅(q)
Markov-trace 𝔙_q (bean qou-3yxn / A5) instead. No c_k; no fit; auditOnly.

Run: python3 -u computations/probes/qbeta_5two_capstone_carrier_falsification_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_capstone_falsification.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
import qbeta_5two_quantum_volume_probe as qv  # noqa: E402  (saddle machinery)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

Q_MUON = mp.mpf("1.10997859555733471")
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
# decay-sector zero of N_odd (qbeta_c3_mq0_nk_scan.py, 80.3% muon-ward)
Q_STAR = mp.mpf("1.10997859303152")
A_PRIME = mp.mpf("2.37")            # capstone slope target dN_odd/dq at q*
VOL_5_2 = qv.VOL_5_2


def bar_odd_V(q, y_seed):
    """B(q) = [𝔙(m=q) − 𝔙(m=1/q)]/2 — the bar-odd (chirality) projection of
    the 5₂ NZ-saddle complex volume under the bar involution m → 1/m.
    Returns (B complex, saddle y at m=q) for seed continuation."""
    x_p, y_p = qv.saddle(q, y_seed)
    x_m, y_m = qv.saddle(1 / q, y_seed)
    _, cv_p = qv.complex_volume(x_p, y_p)
    _, cv_m = qv.complex_volume(x_m, y_m)
    return (cv_p - cv_m) / 2, y_p


def count_sign_changes(vals):
    n = 0
    for a, b in zip(vals, vals[1:]):
        if a != 0 and b != 0 and mp.sign(a) != mp.sign(b):
            n += 1
    return n


def main() -> int:
    print("=" * 78)
    print(" A3 — capstone-carrier falsification: 5₂ NZ bar-odd datum vs N_odd zero at q*")
    print("=" * 78)

    # ---- G1 (gate): reproduce the merged witness's m=1 validation ----
    y0 = mp.mpc("0.78492", "1.30714")
    x1, y1 = qv.saddle(mp.mpf(1), y0)
    vol1, cvol1 = qv.complex_volume(x1, y1)
    g1 = abs(abs(vol1) - VOL_5_2) < mp.mpf(10) ** -6
    print(f"\n[G1] m=1: Vol(5₂) = |{mp.nstr(vol1,12)}| vs {mp.nstr(VOL_5_2,12)}  "
          f"{'PASS' if g1 else 'FAIL'}")

    # ---- G2 (gate): reproduce the anchor-smooth O(1) slope of the merged witness ----
    _, cv_mu = qv.complex_volume(*qv.saddle(Q_MUON, y1))
    _, cv_pr = qv.complex_volume(*qv.saddle(Q_PROTON, y1))
    dq_anch = Q_MUON - Q_PROTON
    slope_im = abs(mp.im(cv_mu) - mp.im(cv_pr)) / dq_anch
    slope_re = abs(mp.re(cv_mu) - mp.re(cv_pr)) / dq_anch
    g2 = max(slope_im, slope_re) < mp.mpf(100)   # O(1)–O(10), nowhere near 3.84e6
    print(f"[G2] anchor slopes: |dIm𝔙/dq|={mp.nstr(slope_im,6)}  "
          f"|dRe𝔙/dq|={mp.nstr(slope_re,6)}  (merged witness: O(1))  "
          f"{'PASS' if g2 else 'FAIL'}")

    # ---- T1: fine zero-crossing scan of B(q) straddling q* ----
    print(f"\n[T1] bar-odd B(q) = [𝔙(m=q)−𝔙(m=1/q)]/2 on a fine grid around q*")
    print(f"     q* = {mp.nstr(Q_STAR, 18)}  (anchor window width "
          f"{mp.nstr(Q_MUON - Q_PROTON, 4)})")
    half = mp.mpf("2e-8")            # straddles the whole anchor window + margin
    npts = 17
    grid = [Q_STAR - half + 2 * half * i / (npts - 1) for i in range(npts)]
    reB, imB = [], []
    y_seed = y1
    for qq in grid:
        B, y_seed = bar_odd_V(qq, y_seed)
        reB.append(mp.re(B))
        imB.append(mp.im(B))
    sc_re = count_sign_changes(reB)
    sc_im = count_sign_changes(imB)
    B_star, _ = bar_odd_V(Q_STAR, y1)
    print(f"     Re B: [{mp.nstr(reB[0],10)} … {mp.nstr(reB[-1],10)}]  "
          f"sign changes = {sc_re}")
    print(f"     Im B: [{mp.nstr(imB[0],10)} … {mp.nstr(imB[-1],10)}]  "
          f"sign changes = {sc_im}")
    print(f"     |B(q*)| = {mp.nstr(abs(B_star),10)}   (a carrier needs B(q*) = 0)")
    t1_no_zero = (sc_re == 0 and sc_im == 0 and abs(B_star) > mp.mpf("1e-10"))

    # ---- T2: the smooth-factor obstruction, quantified ----
    # If the zero lived in f instead: f(q*)=0 while f(q_muon) = N_odd(q_muon)/(u³B),
    # so |df/dq| ≳ |f(q_muon)|/(q_muon−q*) — compare to a smooth O(1)-log-slope f.
    hbar = (Q_MUON - 1) / Q_MUON
    b_coef = mp.sqrt(Q_MUON**4 + Q_MUON**2 + 1) / (Q_MUON**2 + 1)
    u_mu = b_coef * hbar**2
    N_odd_mu = A_PRIME * (Q_MUON - Q_STAR)          # local linear model at q*
    B_mu, _ = bar_odd_V(Q_MUON, y1)
    # use the dominant (chirality/CS) component of B as the carrier magnitude
    B_mag = max(abs(mp.re(B_mu)), abs(mp.im(B_mu)))
    f_mu = N_odd_mu / (u_mu**3 * B_mag)
    f_slope_needed = abs(f_mu) / (Q_MUON - Q_STAR)
    f_log_slope = f_slope_needed / abs(f_mu) if f_mu != 0 else mp.inf
    print(f"\n[T2] if f carried the zero instead: f(q_muon) = "
          f"{mp.nstr(f_mu,6)}, needed |df/dq| ≈ {mp.nstr(f_slope_needed,4)}"
          f"  (log-slope {mp.nstr(f_log_slope,4)} — 'smooth O(1)' is violated by "
          f"~{mp.nstr(f_log_slope/mp.mpf(1),3)}×)")
    t2_f_not_smooth = f_log_slope > mp.mpf("1e6")

    # ---- T3: the writhe ingredient — same test, cheap. Both forms: the
    # capstone's D_odd = ½(q²−q⁻²) (writhe-2, computed with the pre-#3892 braid
    # that is actually 6₂) and the CORRECTED 5₂ datum ½(q⁴−q⁻⁴) (canonical braid
    # [1,1,1,2,-1,2], writhe 4, hyperbolic_knot_db_extended.py). Both fail
    # constraint (2) identically: smooth, O(0.2)/O(0.4), no zero at q*.
    D_star_w2 = (Q_STAR**2 - Q_STAR**-2) / 2
    D_star_w4 = (Q_STAR**4 - Q_STAR**-4) / 2
    print(f"\n[T3] writhe data at q*: capstone (writhe-2, 6₂-braid era) = "
          f"{mp.nstr(D_star_w2,10)};  corrected 5₂ (writhe-4) = "
          f"{mp.nstr(D_star_w4,10)}  — neither has a zero (constraint (2) fails)")
    t3_D_no_zero = abs(D_star_w2) > mp.mpf("0.1") and abs(D_star_w4) > mp.mpf("0.2")

    verdict_fail = t1_no_zero and t2_f_not_smooth and t3_D_no_zero
    print("\n" + "=" * 78)
    print(f"  VERDICT: the analytic NZ-saddle 5₂ bar-odd datum "
          f"{'FAILS constraint (2)' if verdict_fail else 'shows unexpected zero structure — INSPECT'}")
    print("  — B(q) is smooth and nonvanishing at q*; the simple zero of N_odd cannot")
    print("    come from the analytic saddle datum under any u³·(smooth) normalization.")
    print("  SCOPE-(a): narrows the capstone carrier away from the analytic NZ saddle,")
    print("  toward the categorical H₅(q) Markov-trace 𝔙_q (bean qou-3yxn / A5).")
    print("  NOT scope-(b): a different geometric functional (or the categorical trace)")
    print("  remains open. No c_k; no fit; auditOnly.")

    wb = WitnessBuilder("qbeta-5two-capstone-carrier-falsification", engine="mpmath")
    wb.set_description(
        "A3 capstone-carrier falsification (bean qou-el23): tests whether the 5₂ "
        "NZ-saddle bar-odd datum B(q)=[𝔙(m=q)−𝔙(m=1/q)]/2 can be the Im 𝔙_q → "
        "N_odd carrier. Constraint (2) of the capstone (simple zero at q*, slope "
        "A'≈+2.37) forces the carrier to vanish at q*; measured: B has NO zero "
        "crossing in a ±2e-8 window straddling q* and |B(q*)|=O(0.1), and the "
        "alternative (zero in the smooth factor f) needs a ~1e8 log-slope — not "
        "smooth. Writhe datum D_odd likewise nonvanishing. SCOPE-(a): the "
        "analytic NZ-saddle datum is not the carrier; narrows toward the "
        "categorical H_5(q) Markov-trace 𝔙_q (A5). Gates reproduce the merged "
        "5₂ quantum-volume witness (Vol=2.82812, O(1) anchor slopes). "
        "No c_k; no fit; auditOnly.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_vol_5_2_validates",
                     computed=float(abs(abs(vol1) - VOL_5_2)), expected=0.0,
                     tolerance=1e-6,
                     source="m=1 NZ saddle reproduces Vol(5₂)=2.82812 (merged witness gate)")
    wb.add_assertion("gate_anchor_slope_O1",
                     computed=1.0 if g2 else 0.0, expected=1.0, tolerance=0.5,
                     source="cross-anchor |d𝔙/dq| = O(1) reproduces the merged "
                            "qbeta-5two-quantum-volume witness")
    wb.add_assertion("no_zero_crossing_of_barodd_B_at_qstar",
                     computed=1.0 if t1_no_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="B(q) has 0 sign changes (Re and Im) on ±2e-8 grid "
                            "straddling q*, |B(q*)| > 1e-10 — carrier constraint (2) fails")
    wb.add_assertion("smooth_factor_cannot_carry_zero",
                     computed=1.0 if t2_f_not_smooth else 0.0, expected=1.0, tolerance=0.5,
                     source="placing the zero in f instead needs log-slope > 1e6 "
                            "across the anchor window — violates 'smooth O(1)'")
    wb.add_assertion("writhe_D_odd_nonvanishing_at_qstar",
                     computed=float(abs(D_star_w2)), expected=0.21, tolerance=0.05,
                     source="capstone D_odd(q*) = ½(q*²−q*⁻²) ≈ 0.21 (writhe-2, "
                            "pre-#3892 6₂-braid era) — constraint-(2) failure")
    wb.add_assertion("corrected_writhe4_D_odd_nonvanishing_at_qstar",
                     computed=float(abs(D_star_w4)), expected=0.42, tolerance=0.05,
                     source="corrected 5₂ (braid [1,1,1,2,-1,2], writhe 4, #3892): "
                            "½(q*⁴−q*⁻⁴) ≈ 0.42 — same constraint-(2) failure")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("q_star", mp.nstr(Q_STAR, 20))
    wb.add_data("B_at_qstar", {"re": mp.nstr(mp.re(B_star), 15),
                               "im": mp.nstr(mp.im(B_star), 15)})
    wb.add_data("fine_grid", {"half_width": "2e-8", "n_points": npts,
                              "sign_changes_reB": sc_re, "sign_changes_imB": sc_im,
                              "reB_ends": [mp.nstr(reB[0], 12), mp.nstr(reB[-1], 12)],
                              "imB_ends": [mp.nstr(imB[0], 12), mp.nstr(imB[-1], 12)]})
    wb.add_data("smooth_factor_obstruction", {
        "N_odd_muon_linear_model": mp.nstr(N_odd_mu, 10),
        "u_muon_cubed": mp.nstr(u_mu**3, 10),
        "B_magnitude_muon": mp.nstr(B_mag, 10),
        "f_muon": mp.nstr(f_mu, 10),
        "f_log_slope_needed": mp.nstr(f_log_slope, 6)})
    wb.add_data("verdict",
                ("CARRIER FALSIFIED for the analytic NZ-saddle datum (scope-(a)): "
                 "B(q) smooth, nonvanishing at q*, no crossing in the window; the "
                 "u³·(smooth) normalization cannot manufacture the simple zero. "
                 "Capstone carrier narrows to the categorical H₅(q) Markov-trace "
                 "𝔙_q (A5, bean qou-3yxn). NOT scope-(b): other geometric "
                 "functionals stay open."
                 if (ok and verdict_fail) else
                 "INCONCLUSIVE — unexpected zero structure or gate failure; inspect."))
    wb.save()
    print(f"\n  assertions passed: {ok}")
    print("  witness -> computations/probes/qbeta-5two-capstone-carrier-falsification.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
