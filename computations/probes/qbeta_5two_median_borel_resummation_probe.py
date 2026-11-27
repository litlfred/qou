#!/usr/bin/env python3
"""A4.3 (bean qou-ea86): median Borel–Laplace resummation of the 5₂ φ_σ1
series on the A4.2 24-order basis — Padé resurgence gates, exact-object
cross-check, and the bar-odd resummed datum at the substrate.

BASIS. The A4.2 engine (qbeta-5two-phi-series-engine.witness.json, merged
#3927) delivers P_k to order 24 at 1e-59-scale gate precision, in the
x = 2πiτ units: φ(x) = 1 + Σ P_k x^k. Its ratio test already located the
nearest Borel singularity at |V(σ1)−V(σ2)| to 2.5%.

WHAT THIS PROBE DOES:
  1. Borel transform b_k = P_k/k!, Padé approximants of B(ζ); the POLE MAP
     is compared against the PREDICTED Stokes points (GGM eq 81 in the
     x-plane): ζ₁₂ = i(V₁−V₂) ≈ 5.656i and ζ₁₃ = i(V₁−V₃) ≈ −1.379+5.586i
     (V₃ = −2Cl₂-type real chirality partner; V₁ = Vol+iCS etc.) — the
     resurgence-structure gate.
  2. Directional Laplace: φ_res(x) = (1/x)∫₀^∞ B(ζ)e^{−ζ/x}dζ along
     arg ζ = arg x. The substrate direction x_sub = 2πi·(iβ) = −2πβ ≈
     −0.1043 (β = ln q₀/2π) is a singularity-free ray (nearest Stokes points
     sit at arg ≈ ±90°−14°) — the directional sum is unambiguous there; the
     median prescription is only needed ON Stokes rays, which the substrate
     never touches (recorded as a structural finding).
  3. Exact-object cross-check: F(τ) = h₁(τ)·e^{−V/(2πτ)} (the
     A4.1/A4.2-validated pipeline; V = Vol−1.379i, the dominant saddle) has
     F/φ → const C. Fit C where truncation converges (small |x|), then test
     at moderate |x| (1, 2 — approaching the singularity radius 5.66) where
     raw truncation degrades: φ_res must track F/C better than the truncated
     sum — the resummation value-add, measured.
  4. The bar-odd resummed datum: [φ(x_sub) − φ(−x_sub)]/2 (the q → 1/q
     mirror maps τ → −τ, x → −x; both rays singularity-free) — by
     truncation AND resummation, cross-consistent.
  Also recorded: at the substrate |x| = 0.104 the 24-term truncation is
  already converged far below any need for resummation (minimal term at
  k ≈ 5.66/0.104 ≈ 54); the resummation's value is at |x| ≳ 1 — an honest
  statement of where the machinery matters.

auditOnly; no c_k wired; no fit; comparison to structure only.

Run: python3 -u computations/probes/qbeta_5two_median_borel_resummation_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_median_borel.log
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402  (H_num)

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). It was the
# literal 1.1099785955573... -- the RETIRED self-certified muon pin A,
# superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. There is
# no comparison leg here, so the 2026-08-30 owner ruling puts this producer
# on the PROTON default; the pin moves 11.54 ppb.
# The NAME Q0_MUON is kept so its call sites stay legible; it holds the proton
# pin, which is what this producer computes at.
Q0_MUON = Q_MP
# Canonical GGM saddle values — computed, not hardcoded (bean qou-ty28).
from fivetwo_saddle_values import saddle_values  # noqa: E402
V1, V2, V3 = saddle_values("ggm")
# V_DOM: tau2-extraction convention (V_eff = V_GGM + pi^2/2, i-rotated).
# Retained as labelled diagnostic; NOT used as source of V1/V2/V3.
V_DOM = mp.mpc("2.82812206693", "-1.37919426157")   # extraction convention


def load_basis():
    w = record_upstream(Path(
        "computations/probes/qbeta-5two-phi-series-engine.witness.json"), _UPSTREAM_RECORDS)
    P = {0: mp.mpc(1)}
    for k, v in w["data"]["P_coefficients"].items():
        m = re.match(r"\(?\s*([-\d.e]+)\s*([+-])\s*([\d.e]+)j\)?", v)
        r_, s_, i_ = m.groups()
        P[int(k)] = mp.mpc(mp.mpf(r_), mp.mpf(i_) * (1 if s_ == "+" else -1))
    return P


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" A4.3 — median Borel–Laplace of φ_σ1(5₂) on the 24-order basis")
    print("=" * 78)

    P = load_basis()
    OMAX = max(P)
    print(f"\n  basis loaded: P_k to order {OMAX} (A4.2 engine, merged #3927)")

    # ---- 1. Borel–Padé pole map vs predicted Stokes points ----
    b = [P[k] / mp.factorial(k) for k in range(OMAX + 1)]
    p_num, p_den = mp.pade(b, 11, 12)
    poles = mp.polyroots([p_den[i] for i in range(len(p_den) - 1, -1, -1)],
                         maxsteps=200, extraprec=80)
    # ζ = V_i − V_j, with NO explicit i (corrected 2026-08-01). The Borel-Padé
    # pole is convention-free data; it sits at 0.0753 + 5.7566j. Testing both
    # forms against it in the published GGM convention:
    #
    #   V₁ − V₂     = 0 + 5.656244j   rel dev 0.0222   <- matches
    #   1j·(V₁ − V₂) = −5.656244 + 0j  rel dev 1.436    <- 90° off
    #
    # The explicit `1j *` here was calibrated against the corpus's LEGACY
    # i-rotated V (which put Vol in Re V₁): i·(V₁−V₂)_legacy = 5.656j, i.e.
    # the legacy rotation exactly cancelled this factor. The 2026-07-30
    # migration to saddle_values("ggm") switched V but kept the `1j *`,
    # double-rotating by 90° and breaking the resurgence gate (rel 0.0222 →
    # 1.369). The stale committed witness hid the regression.
    zeta12 = V1 - V2
    zeta13 = V1 - V3
    print("\n[1] Borel–Padé [11/12] pole map vs predicted Stokes points:")
    print(f"    predicted ζ₁₂ = {mp.nstr(zeta12, 8)}   ζ₁₃ = {mp.nstr(zeta13, 8)}")
    best12 = min(poles, key=lambda p: abs(p - zeta12))
    best13 = min(poles, key=lambda p: abs(p - zeta13))
    d12 = abs(best12 - zeta12) / abs(zeta12)
    d13 = abs(best13 - zeta13) / abs(zeta13)
    print(f"    nearest poles: {mp.nstr(best12, 8)} (rel {mp.nstr(d12, 3)});  "
          f"{mp.nstr(best13, 8)} (rel {mp.nstr(d13, 3)})")
    g1 = d12 < mp.mpf("0.1")
    print(f"    ζ₁₂ located within 10%: {'PASS' if g1 else 'FAIL'}  "
          f"(ζ₁₃ diagnostic: {mp.nstr(d13, 3)})")

    # ---- 2. directional Laplace along a given x ----
    def B_pade(zeta):
        num = sum(p_num[i] * zeta ** i for i in range(len(p_num)))
        den = sum(p_den[i] * zeta ** i for i in range(len(p_den)))
        return num / den

    def phi_res(x):
        ray = x / abs(x)
        f = lambda t: B_pade(t * ray) * mp.e ** (-(t * ray) / x) * ray
        return mp.quad(f, [0, 5, 20, 80]) / x

    def phi_trunc(x, n=OMAX):
        return sum(P[k] * x ** k for k in range(n + 1))

    beta = mp.log(Q0_MUON) / (2 * mp.pi)
    x_sub = -2 * mp.pi * beta
    print(f"\n[2] substrate point x_sub = −2πβ = {mp.nstr(x_sub, 10)}:")
    pt = phi_trunc(x_sub)
    pr = phi_res(x_sub)
    dsub = abs(pt - pr) / abs(pt)
    # minimal-term truncation bound at the substrate
    minterm = min(abs(P[k] * x_sub ** k) for k in range(1, OMAX + 1))
    print(f"    φ_trunc = {mp.nstr(pt, 15)}")
    print(f"    φ_res   = {mp.nstr(pr, 15)}   |Δ|/|φ| = {mp.nstr(dsub, 4)}")
    print(f"    minimal series term ≈ {mp.nstr(minterm, 3)} — truncation already "
          "converged at the substrate; resummation matters at |x| ≳ 1")
    g2 = dsub < mp.mpf("1e-8")

    # ---- 3. exact-object cross-check at moderate |x| ----
    # F(τ) = h₁(τ)e^{−V/2πτ}; x = 2πiτ ⇒ τ = x/(2πi); on the negative-real-x
    # ray τ = i|x|/(2π) is the imaginary-τ / real-q ray, q = e^{−|x|} real.
    print("\n[3] exact-object cross-check (F = h₁·e^{−V/2πτ}, real-q ray):")

    def F_exact(x):
        tau = x / (2j * mp.pi)
        q = mp.e ** (2j * mp.pi * tau)
        return sb.H_num(+1, 1, 0, q) * mp.e ** (-V_DOM / (2 * mp.pi * tau))

    # fit C at small |x| where truncation is excellent
    x_fit = mp.mpf("-0.35")
    C = F_exact(x_fit) / phi_trunc(x_fit)
    print(f"    C fitted at x={x_fit}: {mp.nstr(C, 12)}")
    rows = []
    g3 = True
    for xv in (mp.mpf("-1.0"), mp.mpf("-2.0"), mp.mpf("-3.0")):
        Fx = F_exact(xv)
        rt = abs(Fx / C - phi_trunc(xv)) / abs(Fx / C)
        rr = abs(Fx / C - phi_res(xv)) / abs(Fx / C)
        rows.append({"x": str(xv), "trunc_rel": mp.nstr(rt, 6),
                     "resum_rel": mp.nstr(rr, 6)})
        print(f"    x={xv}: truncation rel err {mp.nstr(rt, 4)}   "
              f"resummed rel err {mp.nstr(rr, 4)}   "
              f"gain ×{mp.nstr(rt / rr, 4) if rr > 0 else 'inf'}")
        g3 &= rr < rt
    print(f"    resummation beats truncation at every tested |x|: "
          f"{'PASS' if g3 else 'FAIL'}")

    # ---- 4. the bar-odd resummed datum at the substrate ----
    print("\n[4] bar-odd datum [φ(x_sub) − φ(−x_sub)]/2 (mirror x → −x):")
    odd_t = (phi_trunc(x_sub) - phi_trunc(-x_sub)) / 2
    odd_r = (phi_res(x_sub) - phi_res(-x_sub)) / 2
    dodd = abs(odd_t - odd_r) / abs(odd_t)
    print(f"    truncation: {mp.nstr(odd_t, 15)}")
    print(f"    resummed:   {mp.nstr(odd_r, 15)}   consistency {mp.nstr(dodd, 4)}")
    g4 = dodd < mp.mpf("1e-6")
    print("    structural note: both ±x_sub rays are Stokes-free (nearest "
          "singularities at arg ≈ 90°±14°) — the directional sum is unambiguous;")
    print("    the MEDIAN prescription is needed only on Stokes rays, which the "
          "substrate never touches.")

    wb = WitnessBuilder("qbeta-5two-median-borel-resummation", engine="mpmath",
                        _script_path=__file__)
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "A4.3 (bean qou-ea86): Borel–Laplace resummation of φ_σ1(5₂) on the "
        "A4.2 24-order basis. Padé pole map locates the predicted Stokes "
        "point ζ₁₂ = i(V₁−V₂) (resurgence gate; ζ₁₃ diagnostic); directional "
        "Laplace along the substrate ray (singularity-free — the median "
        "prescription is never needed at the substrate, a structural "
        "finding); exact-object cross-check F = h₁e^{−V/2πτ} at |x| = 1..3 "
        "shows the resummation beating raw truncation as the singularity "
        "radius is approached; the bar-odd resummed datum "
        "[φ(x)−φ(−x)]/2 at ±x_sub is truncation-consistent. At the substrate "
        "itself the 24-term truncation is already converged (minimal term "
        "bound) — an honest statement of where resummation matters. "
        "auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("pade_locates_zeta12",
                     computed=d12, expected=0.0, tolerance=0.1,
                     source="Borel–Padé [11/12] pole within 10% of ζ₁₂ = i(V₁−V₂)")
    wb.add_assertion("substrate_resummation_consistent",
                     computed=1.0 if g2 else 0.0, expected=1.0, tolerance=0.5,
                     source="φ_res(x_sub) = φ_trunc(x_sub) to 1e-8 (both converged "
                            "at the substrate)")
    wb.add_assertion("resummation_beats_truncation",
                     computed=1.0 if g3 else 0.0, expected=1.0, tolerance=0.5,
                     source="vs the exact F/C at x = −1, −2, −3: resummed rel err < "
                            "truncated rel err at every point")
    wb.add_assertion("barodd_datum_consistent",
                     computed=1.0 if g4 else 0.0, expected=1.0, tolerance=0.5,
                     source="[φ(x)−φ(−x)]/2 at ±x_sub: truncation vs resummation "
                            "agree to 1e-6")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("stokes_points", {"zeta12": mp.nstr(zeta12, 15),
                                  "zeta13": mp.nstr(zeta13, 15),
                                  "pade_pole_12": mp.nstr(best12, 15),
                                  "pade_pole_13": mp.nstr(best13, 15),
                                  "rel_12": mp.nstr(d12, 6), "rel_13": mp.nstr(d13, 6)})
    wb.add_data("substrate", {"x_sub": mp.nstr(x_sub, 15),
                              "phi_trunc": mp.nstr(pt, 25),
                              "phi_res": mp.nstr(pr, 25),
                              "min_term": mp.nstr(minterm, 6)})
    wb.add_data("exact_crosscheck", rows)
    wb.add_data("barodd_datum", {"truncation": mp.nstr(odd_t, 25),
                                 "resummed": mp.nstr(odd_r, 25)})
    wb.add_data("structural_finding",
                "the substrate ray arg(x) = 180° (and its mirror 0°) never "
                "touches a Stokes ray (nearest at ~90°±14°) — the directional "
                "Borel sum is unambiguous at the substrate; median averaging "
                "is not required for the physical evaluation")
    wb.add_data("verdict",
                ("A4 RESUMMATION LANDED: the 24-order basis Borel-resums with "
                 "the predicted resurgence structure (ζ₁₂ located), beats "
                 "truncation toward the singularity radius against the exact "
                 "object, and yields a truncation-consistent bar-odd datum at "
                 "the substrate — where the directional sum is unambiguous "
                 "(no median needed; structural finding). auditOnly."
                 if ok else "A gate failed — inspect before use."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic() - t0:.0f}s)")
    print("  witness -> computations/probes/qbeta-5two-median-borel-resummation.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
