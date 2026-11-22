#!/usr/bin/env python3
"""segment_collision_probe.py — the owner's 2026-10-12 reformulation of the relative Reeb datum, tested.
Bean `qou-jfx8` (reformulation), companion to `QOU/MassTheory/SegmentCollisionDatum.lean`.

The owner's picture: two particles meet at the exceptional divisor, but only ONE braid segment from each meets
at the point; the history (the γγ entanglement tower) enters as a categorical trace; the incoming angle is the
relative minimum of the local rotational energy (O'Hara + Bring). Three questions, each answered by measurement:

  Q1  Does the single-segment collision forget the histories (Lean Part A, conditional on the disjoint-block
      law)? Measured on the production nucleon words in H_6: tr(a·c·b) / (tr a · tr b) for c ∈ {1, σ₂, σ₂⁻¹}
      must equal (1, z_D, z_D − h) for EVERY pair (a, b). Then the dichotomy: a two-segment probe
      (c = σ₁σ₂, reaching one strand into a's history) must NOT be universal.
  Q2  The two fundamental channels (Lean Part B): with P_S = (σ + q⁻¹)/(q + q⁻¹), the Sym weight of the
      collision state must be (q⁴+q²+1)/(q²+1)² and the Alt weight q²/(q²+1)².
  Q3  The local O'Hara cross term (Lean Part C): E(θ) = ∫∫_{[−ℓ,ℓ]²} ds dt / (d² + s² + t² − 2st cos θ).
      Measured: symmetry E(π−θ) = E(θ), the location of the minimum on a θ grid at several ℓ/d, and the
      large-ℓ log coefficient against 2π/sin θ.

Evaluator: the self-contained mpmath Hoefsmit evaluator of `composition_feasibility_a2_probe.py`, re-validated
here against the committed H_3 nucleon characters before anything is measured. q₀ from the committed
`y-lambda-at-q0.witness.json` string (proton anchor). mpmath throughout; no float arithmetic.
Nothing is fitted, selected or wired.
-- Ref: [manuscript] rem:light-cone-affine; bean qou-jfx8, qou-pzsi
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import composition_feasibility_a2_probe as cf  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402  (path set by cf)

mp.mp.dps = 60
Q, H, Z_D = cf.Q, cf.H, cf.Z_D
ZINV = Z_D - H                     # σ⁻¹ = σ − h
SIG = lambda g: [(1, mp.mpf(0), g)]          # noqa: E731
SIGINV = lambda g: [(1, -H, g)]              # noqa: E731


def tr(n, word, y):
    return mp.fsum(y[l] * cf.chi(l, word) for l in cf.partitions_of(n))


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-40")
    y3, y6 = cf.load_y(3), cf.load_y(6)
    sum3 = mp.fsum(y3[l] * cf.chi(l, []) for l in cf.partitions_of(3))
    sum6 = mp.fsum(y6[l] * cf.chi(l, []) for l in cf.partitions_of(6))
    print("tr(1) at n=3, 6:", mp.nstr(sum3, 20), mp.nstr(sum6, 20))
    check("trace_normalised_tr1_eq_1_at_n3_and_n6", abs(sum3 - 1) < TOL and abs(sum6 - 1) < TOL, "y-lambda-at-q0")

    # validation against committed characters
    P3 = cf.partitions_of(3)
    wp, wn = cf.nucleon_word(cf.B_P, 0, 1), cf.nucleon_word(cf.B_N, 0, 1)
    chi_p, chi_n = cf.load_nucleon("proton"), cf.load_nucleon("neutron")
    dev = max(max(abs(cf.chi(l, wp) - chi_p[l]) for l in P3), max(abs(cf.chi(l, wn) - chi_n[l]) for l in P3))
    check("evaluator_reproduces_committed_H3_nucleon_characters", dev < TOL, "chi-{proton,neutron}-h3-at-q0-50dps")

    # ── Q1: single-segment universality and the two-segment dichotomy ──
    words = {"p": cf.nucleon_word(cf.B_P, 0, 1), "n": cf.nucleon_word(cf.B_N, 0, 1),
             "sigma0^3": SIG(0) * 3, "core": [(1, mp.mpf(0), 0), (1, -H, 1)] * 3}
    tr3 = {k: tr(3, w, y3) for k, w in words.items()}
    shift = lambda w: [(c, d, g + 3) for c, d, g in w]          # noqa: E731  b above the bridge σ₂
    rows, worst, two_seg = [], mp.mpf(0), {}
    for ka in ("p", "n", "core"):
        for kb in ("p", "n", "sigma0^3"):
            a, b = words[ka], shift(words[kb])
            base = tr3[ka] * tr3[kb]
            r_free = tr(6, a + b, y6) / base
            r_sig = tr(6, a + SIG(2) + b, y6) / base
            r_inv = tr(6, a + SIGINV(2) + b, y6) / base
            r_two = tr(6, a + SIG(1) + SIG(2) + b, y6) / base      # one strand of a's side + bridge
            dev_ab = max(abs(r_free - 1), abs(r_sig - Z_D), abs(r_inv - ZINV))
            worst = max(worst, dev_ab)
            two_seg[f"{ka}|{kb}"] = r_two
            rows.append({"a": ka, "b": kb, "free_ratio": mp.nstr(r_free, 30), "sigma_ratio": mp.nstr(r_sig, 30),
                         "sigma_inv_ratio": mp.nstr(r_inv, 30), "two_segment_ratio": mp.nstr(r_two, 30)})
            print(f"  a={ka:<5} b={kb:<9} free {mp.nstr(r_free, 15)}  σ {mp.nstr(r_sig, 15)}  σ⁻¹ {mp.nstr(r_inv, 15)}"
                  f"   two-seg {mp.nstr(r_two, 15)}")
    print("z_D =", mp.nstr(Z_D, 15), " z_D − h =", mp.nstr(ZINV, 15), " worst single-segment dev:", mp.nstr(worst, 5))
    check("single_segment_marginal_universal_(1,zD,zD-h)_for_all_pairs", worst < TOL,
          "Lean bridge_free / bridge_crossing / bridge_crossing_inv; 9 pairs incl. p, n, alternating core")
    spread = max(two_seg.values()) - min(two_seg.values())
    print("two-segment ratio spread across pairs:", mp.nstr(spread, 10))
    check("two_segment_probe_is_NOT_universal_(spread>1e-3)", spread > mp.mpf("1e-3"),
          "c = σ₁σ₂ reaches one strand into a's history")
    pn_sep = abs(two_seg["p|p"] - two_seg["n|p"])
    print("two-segment |ratio(p|p) − ratio(n|p)| =", mp.nstr(pn_sep, 10))

    # ── Q2: channel weights ──
    qi = 1 / Q
    wS = (Z_D + qi) / (Q + qi)
    wA = 1 - wS
    wS_D = (Q ** 4 + Q ** 2 + 1) / (Q ** 2 + 1) ** 2
    wA_D = Q ** 2 / (Q ** 2 + 1) ** 2
    a, b = words["p"], shift(words["n"])
    base = tr3["p"] * tr3["n"]
    PS = [(1 / (Q + qi), qi / (Q + qi), 2)]                        # P_S = (σ + q⁻¹)/(q + q⁻¹)
    wS_meas = tr(6, a + PS + b, y6) / base
    print("channel weights: Sym", mp.nstr(wS_meas, 20), "(closed form", mp.nstr(wS_D, 20), ")  Alt", mp.nstr(wA_D, 20))
    check("sym_channel_weight_eq_(q4+q2+1)/(q2+1)^2", abs(wS_meas - wS_D) < TOL and abs(wS - wS_D) < TOL, "Lean channel_weights_conventionD")
    check("alt_channel_weight_eq_q2/(q2+1)^2_and_positive", abs(wA - wA_D) < TOL and wA_D > 0, "Lean alt_weight_ne_zero_conventionD")

    # ── Q3: local O'Hara cross term ──
    mp.mp.dps = 25
    d = mp.mpf(1)

    def E(theta, ell):
        c = mp.cos(theta)
        return mp.quad(lambda s, t: 1 / (d ** 2 + s ** 2 + t ** 2 - 2 * s * t * c), [-ell, 0, ell], [-ell, 0, ell])

    grid = [mp.pi * k / 12 for k in range(1, 12)]
    ohara_rows = {}
    sym_worst, argmins = mp.mpf(0), {}
    for ell in (mp.mpf("0.5"), mp.mpf(2), mp.mpf(10), mp.mpf(50)):
        vals = [E(th, ell) for th in grid]
        for i in range(len(grid)):
            sym_worst = max(sym_worst, abs(vals[i] - vals[-1 - i]) / vals[i])
        kmin = min(range(len(grid)), key=lambda i: vals[i])
        argmins[mp.nstr(ell, 4)] = grid[kmin]
        ohara_rows[mp.nstr(ell, 4)] = [mp.nstr(v, 15) for v in vals]
        print(f"  ℓ/d = {mp.nstr(ell, 4):>4}: argmin θ = {mp.nstr(grid[kmin] / mp.pi, 6)}·π   "
              f"E(π/12) {mp.nstr(vals[0], 8)}  E(π/2) {mp.nstr(vals[5], 8)}")
    check("ohara_cross_term_reflection_symmetric_E(pi-theta)=E(theta)", sym_worst < mp.mpf("1e-15"), "Lean segEnergy_reflect")
    check("ohara_cross_term_minimum_at_pi/2_on_grid_at_every_ell", all(abs(v - mp.pi / 2) < mp.mpf("1e-20") for v in argmins.values()),
          "Lean minimiser_eq_pi_div_two (achiral case)")
    log_coef = {}
    for th in (mp.pi / 2, mp.pi / 3, mp.pi / 6):
        slope = (E(th, mp.mpf(400)) - E(th, mp.mpf(100))) / mp.log(4)
        log_coef[mp.nstr(th / mp.pi, 4)] = (slope, 2 * mp.pi / mp.sin(th))
        print(f"  θ = {mp.nstr(th / mp.pi, 4)}π: dE/dlog ℓ = {mp.nstr(slope, 10)}   2π/sin θ = {mp.nstr(2 * mp.pi / mp.sin(th), 10)}")
    check("ohara_log_coefficient_approaches_2pi/sin(theta)_(1e-2_rel)",
          all(abs(s / t - 1) < mp.mpf("1e-2") for s, t in log_coef.values()), "polar asymptotics, ∫dφ/(1 − cosθ sin2φ) = 2π/|sinθ|")
    mp.mp.dps = 60

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("segment-collision", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0_anchor_reason": "q0 read from the committed y-lambda-at-q0 witness string",
        "description": ("PROBE (bean qou-jfx8): the owner's segment-collision reformulation. Q1 the single-segment collision "
                        "state is universal (1, z_D, z_D − h)·tr a·tr b on every pair; a two-segment probe is not. Q2 Sym/Alt "
                        "channel weights at convention D. Q3 the local O'Hara cross term of two segments is reflection-symmetric, "
                        "minimal at θ = π/2, log coefficient 2π/sin θ. Nothing fitted, selected or wired."),
        "weight_family": "markov_y_lambda_convention_D",
        "z_D": mp.nstr(Z_D, 50), "z_inv": mp.nstr(ZINV, 50),
        "q1_rows": rows, "q1_single_segment_worst_dev": mp.nstr(worst, 5),
        "q1_two_segment_spread": mp.nstr(spread, 20), "q1_two_segment_p_vs_n_separation": mp.nstr(pn_sep, 20),
        "q2_sym_weight": mp.nstr(wS_D, 50), "q2_alt_weight": mp.nstr(wA_D, 50),
        "q3_theta_grid_over_pi": [mp.nstr(t / mp.pi, 6) for t in grid], "q3_energy_d1": ohara_rows,
        "q3_argmin_over_pi": {k: mp.nstr(v / mp.pi, 6) for k, v in argmins.items()},
        "q3_log_coefficient": {k: {"measured": mp.nstr(s, 15), "2pi_over_sin": mp.nstr(t, 15)} for k, (s, t) in log_coef.items()},
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
