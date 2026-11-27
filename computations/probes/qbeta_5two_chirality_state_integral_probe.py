#!/usr/bin/env python3
"""A1 (bean qou-u5xq): the 5₂ Andersen–Kashaev state integral on the substrate
ray — quadrature vs factorization, and the frame-reduced chirality (odd) part.

The state integrals (GGM 2007.10190 eqs 37/39/72; transcribed + verified
2026-07-18 from the owner-supplied PDF):

    Z_4₁(τ) = ∫_C Φ_b(v)² e^{−πiv²} dv          (A,B) = (1,2)
    Z_5₂(τ) = ∫_C Φ_b(v)³ e^{−2πiv²} dv         (A,B) = (2,3),  τ = b²

The SUBSTRATE RAY is τ = iβ, β = ln(q₀)/(2π) ≈ 0.01658 (the imaginary-τ /
real-q ray: q = e^{2πiτ} = 1/q₀ and q̃ = e^{−2πi/τ} = e^{−2π/β} ≈ 1e-165,
both real) — exactly the corpus `phi_b_substrate_regime.b_substrate(q₀)`
branch b = √β·e^{iπ/4} (Im b² > 0).

GATES:
  G1 — 4₁ at b = 1 against the EXACT closed form (Garoufalidis–Kashaev
       1411.6062 eq 2):  I_{1,2}(1) = (e^{πi/6}/√3)·(e^{V/2π} − e^{−V/2π}),
       V = Vol(4₁) = 2·Im Li₂(e^{iπ/3}).  Tests the Φ_b evaluator + the bent
       contour quadrature end-to-end.
  G2 — 5₂ at the substrate τ = iβ: quadrature vs the GGM eq-110/Peacock eq-82
       FACTORIZATION  Z_5₂ = −(e^{πi/4}/2)(q/q̃)^{1/8}·(τ·H⁺₂(q)H⁻₀(q̃)
       − 2H⁺₁(q)H⁻₁(q̃) + (1/τ)H⁺₀(q)H⁻₂(q̃)) — two INDEPENDENT evaluations
       of the same analytic object (the H-series side is the A2-validated
       machinery, 18 printed tables + Conjecture-1b gates).

MEASUREMENT — the chirality decomposition on the substrate ray. On τ = iβ the
H-series are all real, so with the universal framing phase e^{πi/4} peeled
off (GGM Thm 3 prefactor e^{πi(B+2(A+1))/4} = e^{9πi/4} ≡ e^{πi/4}):

    Ẑ := e^{−πi/4}·Z_5₂ = −(R^{1/8}/2)·( −2·H⁺₁H⁻₁  +  i·[β·H⁺₂H⁻₀ − (1/β)·H⁺₀H⁻₂] )

    Re Ẑ  = R^{1/8}·H⁺₁H⁻₁            — the bar-EVEN part (the index channel:
                                         2H⁺₁H⁻₁ = Ind^rot, GGM eq 102)
    Im Ẑ  = −(R^{1/8}/2)·[β·H⁺₂H⁻₀ − (1/β)·H⁺₀H⁻₂]  — the CHIRALITY-ODD part

(mirror convention, GZ 2111.06645 §10.1: K* ⇒ conjugated trace field,
⟨K*⟩_N = conj⟨K⟩_N; on the real-q ray the mirror flips i → −i, so the
frame-reduced odd channel is Im Ẑ). Report Im Ẑ at both anchors — a DERIVED,
fibre-level, calibration-free odd datum of the chiral 5₂ — with the honest
anchor-smoothness statement (SRigidityPrune binds; this is the odd
INGREDIENT, not the swing). No fit; no c_k wired; auditOnly.

Run: python3 -u computations/probes/qbeta_5two_chirality_state_integral_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_chirality_zint.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "qbeta"))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from phi_b_evaluator import log_phi_b  # noqa: E402  (corpus-validated Φ_b)
import qbeta_5two_stokes_barodd_index_probe as sb  # noqa: E402  (A2 H_num)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Both pins read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). The
# muon leg was the literal 1.1099785955573... -- the RETIRED self-certified
# pin A, superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. A
# mu-vs-p comparison whose muon leg is a retired literal compares live proton
# against yesterday's muon, which is the failure it exists to measure.
# Exception E1 of the 2026-08-30 ruling: both pins are read here on purpose.
Q0 = {"muon": q_muon_at(50),
      "proton": Q_MP}


QUAD_DPS = 30  # see z_state_integral


def z_state_integral(b, B_pow, A_coef, T=mp.mpf(8)):
    """∫ Φ_b(v)^B e^{−A·πi·v²} dv on the bent contour
    [−T·e^{−iθ}, 0, T·e^{iθ}] (decay at both ends for B > A > 0).

    STRIP CONSTRAINT (first-run lesson, cost 1033s of garbage): the corpus
    `log_phi_b` integral representation is valid only in |Im v| < Im c_b,
    c_b = i(b+1/b)/2. The bend angle is chosen so the whole contour stays
    inside 85% of the strip: sin θ = min(sin π/8, 0.85·Im(c_b)/T). The end
    decay rate |e^{∓πi·(B−A or A)v²}| = e^{−c·t²·sin 2θ} survives any θ>0;
    smaller θ just delays the falloff (T=8 gives e^{−40}-scale tails even at
    the b=1 minimum θ ≈ 6°). Pole lattice (angle ≈π/4 substrate, imaginary
    axis at b=1) stays far from the low-angle contour."""
    c_b = 1j * (b + 1 / b) / 2
    strip = mp.im(c_b)
    s_theta = min(mp.sin(mp.pi / 8), mp.mpf("0.85") * strip / T)
    theta = mp.asin(s_theta)

    def f(v):
        return mp.e ** (B_pow * log_phi_b(v, b) - A_coef * mp.pi * 1j * v * v)
    p1 = -T * mp.e ** (-1j * theta)
    p3 = T * mp.e ** (1j * theta)
    # QUADRATURE PRECISION IS PINNED, not inherited (bean qou-0xe1). The inner
    # `log_phi_b` sizes its truncation from mp.dps, and mpmath's quad targets
    # 10^-dps, so at the canonical COMPUTE_DPS = 70 the nested tanh-sinh goes
    # on to degree 8 (~2400 inner evaluations per point vs ~1000, hours). The
    # gates need 1e-8 / 1e-6, and the result is floored near 1e-19 by the
    # T = 8 contour cut anyway. 30 is the precision of the validated run
    # (witness 2026-07-18, qou-he82: G1 rel err 1.097e-19).
    with mp.workdps(QUAD_DPS):
        return +mp.quad(f, [p1, mp.mpf(0), p3])


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" A1 — 5₂ chirality state integral on the substrate ray (τ = iβ)")
    print("=" * 78)

    # ---- G1: 4₁ at b = 1 vs the exact closed form (1411.6062 eq 2) ----
    print("\n[G1] 4₁ quadrature at b=1 vs the GK closed form ...", flush=True)
    V41 = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))
    exact41 = (mp.e ** (1j * mp.pi / 6) / mp.sqrt(3)) * \
        (mp.e ** (V41 / (2 * mp.pi)) - mp.e ** (-V41 / (2 * mp.pi)))
    t1 = time.monotonic()
    quad41 = z_state_integral(mp.mpf(1), 2, 1)
    rel41 = abs(quad41 - exact41) / abs(exact41)
    g1 = rel41 < mp.mpf("1e-8")
    print(f"     exact  = {mp.nstr(exact41, 15)}")
    print(f"     quad   = {mp.nstr(quad41, 15)}   ({time.monotonic()-t1:.0f}s)")
    print(f"     rel err = {mp.nstr(rel41, 4)}  {'PASS' if g1 else 'FAIL'}")

    # ---- G2 + M: the substrate ray, both anchors ----
    results = {}
    for name, q0v in Q0.items():
        beta = mp.log(q0v) / (2 * mp.pi)
        tau = 1j * beta
        b_sub = mp.sqrt(beta) * mp.e ** (1j * mp.pi / 4)   # b² = iβ ✓
        x = 1 / q0v                                        # q = e^{2πiτ} = 1/q₀
        qt = mp.e ** (-2 * mp.pi / beta)                   # ≈ 1e-165

        # factorization side (A2-validated H machinery)
        Hp = [sb.H_num(+1, j, 0, x) for j in range(3)]
        Hm = [sb.H_num(-1, j, 0, qt) for j in range(3)]
        R18 = (x / qt) ** mp.mpf("0.125")
        bilin = tau * Hp[2] * Hm[0] - 2 * Hp[1] * Hm[1] + (1 / tau) * Hp[0] * Hm[2]
        Z_fact = -(mp.e ** (1j * mp.pi / 4) / 2) * R18 * bilin

        # frame-reduced parts
        Zhat = mp.e ** (-1j * mp.pi / 4) * Z_fact
        even = R18 * Hp[1] * Hm[1]
        odd = -(R18 / 2) * (beta * Hp[2] * Hm[0] - (1 / beta) * Hp[0] * Hm[2])
        results[name] = {"beta": beta, "b": b_sub, "Z_fact": Z_fact,
                         "Zhat": Zhat, "even": even, "odd": odd}
    r_mu = results["muon"]

    print(f"\n[G2] 5₂ at substrate τ = iβ (muon): β = {mp.nstr(r_mu['beta'], 10)}")
    print(f"     Z_fact = {mp.nstr(r_mu['Z_fact'], 15)}", flush=True)
    t2 = time.monotonic()
    Z_quad = z_state_integral(r_mu["b"], 3, 2)
    rel52 = abs(Z_quad - r_mu["Z_fact"]) / abs(r_mu["Z_fact"])
    g2 = rel52 < mp.mpf("1e-6")
    print(f"     Z_quad = {mp.nstr(Z_quad, 15)}   ({time.monotonic()-t2:.0f}s)")
    print(f"     rel err = {mp.nstr(rel52, 4)}  {'PASS' if g2 else 'FAIL'}")

    # consistency of the frame-reduced split (arithmetic identity check)
    split_res = abs(r_mu["Zhat"] - (r_mu["even"] + 1j * r_mu["odd"])) / abs(r_mu["Zhat"])
    g3 = split_res < mp.mpf("1e-25")
    print(f"\n[G3] Ẑ = even + i·odd split residual: {mp.nstr(split_res, 4)}  "
          f"{'PASS' if g3 else 'FAIL'}")

    print("\n[M] frame-reduced chirality decomposition at the substrate:")
    for name, r in results.items():
        print(f"     {name}:  Re Ẑ (even) = {mp.nstr(r['even'], 15)}   "
              f"Im Ẑ (ODD) = {mp.nstr(r['odd'], 15)}")
    odd_nonzero = abs(r_mu["odd"]) > mp.mpf("1e-6") * abs(r_mu["even"])
    print(f"     odd channel nonzero (chiral 5₂): {'YES' if odd_nonzero else 'NO'}")

    dq = Q0["muon"] - Q0["proton"]
    d_odd = abs(results["muon"]["odd"] - results["proton"]["odd"])
    rel_slope = float(d_odd / abs(r_mu["odd"]) / dq)
    print(f"\n[H] anchor-dependence of the odd datum: |d ln(odd)/dq| ≈ {rel_slope:.4e}")
    print("     (S-swing needs ~3.84e6 in S-units; SRigidityPrune binds — this is")
    print("      the derived odd ingredient, NOT the swing)")
    honest_smooth = rel_slope < 1e5

    wb = WitnessBuilder("qbeta-5two-chirality-state-integral", engine="mpmath")
    wb.set_description(
        "A1 (bean qou-u5xq): the 5₂ Andersen–Kashaev state integral "
        "Z = ∫Φ_b(v)³e^{−2πiv²}dv on the substrate ray τ = iβ (b = √β·e^{iπ/4}, "
        "q = 1/q₀, q̃ ≈ 1e-165), computed TWO independent ways: bent-contour "
        "quadrature with the corpus-validated Φ_b evaluator, and the GGM "
        "eq-110/Peacock eq-82 H-series factorization (A2-validated machinery). "
        "Gated by the exact 4₁ b=1 closed form (GK 1411.6062 eq 2). "
        "Measurement: the frame-reduced chirality split Ẑ = e^{−πi/4}Z = "
        "[R^{1/8}H⁺₁H⁻₁] + i·[−(R^{1/8}/2)(βH⁺₂H⁻₀ − (1/β)H⁺₀H⁻₂)] — the real "
        "part is the bar-even index channel, the imaginary part is the DERIVED "
        "chirality-odd datum of 5₂ at the substrate (calibration-free, "
        "fibre-level). Honest: anchor-smooth (SRigidityPrune binds — odd "
        "ingredient, not the swing). No fit; no c_k wired; auditOnly.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("gate_4one_b1_closed_form",
                     computed=float(rel41), expected=0.0, tolerance=1e-8,
                     source="quadrature of ∫Φ₁²e^{−πiv²} matches the exact GK closed "
                            "form (e^{πi/6}/√3)·2sinh(V/2π), V = Vol(4₁)")
    wb.add_assertion("gate_5two_quadrature_vs_factorization",
                     computed=float(rel52), expected=0.0, tolerance=1e-6,
                     source="Z_5₂(iβ) by bent-contour quadrature = the GGM/Peacock "
                            "H-series factorization (independent evaluations)")
    wb.add_assertion("frame_reduced_split_exact",
                     computed=float(split_res), expected=0.0, tolerance=1e-25,
                     source="Ẑ = even + i·odd with even = R^{1/8}H⁺₁H⁻₁, "
                            "odd = −(R^{1/8}/2)(βH⁺₂H⁻₀ − (1/β)H⁺₀H⁻₂)")
    wb.add_assertion("odd_channel_nonzero_chiral",
                     computed=1.0 if odd_nonzero else 0.0, expected=1.0, tolerance=0.5,
                     source="Im Ẑ ≠ 0 at the substrate — the 5₂ chirality-odd channel "
                            "is live in the state integral")
    wb.add_assertion("anchor_smooth_honest",
                     computed=1.0 if honest_smooth else 0.0, expected=1.0, tolerance=0.5,
                     source="|d ln(odd)/dq| ≪ 3.84e6 — derived odd ingredient, not the "
                            "swing (SRigidityPrune)")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("substrate", {name: {"beta": mp.nstr(r["beta"], 25),
                                     "b": mp.nstr(r["b"], 25)}
                              for name, r in results.items()})
    wb.add_data("Z_factorization_muon", mp.nstr(r_mu["Z_fact"], 25))
    wb.add_data("Z_quadrature_muon", mp.nstr(Z_quad, 25))
    wb.add_data("chirality_split", {name: {"even_ReZhat": mp.nstr(r["even"], 25),
                                           "odd_ImZhat": mp.nstr(r["odd"], 25)}
                                    for name, r in results.items()})
    wb.add_data("anchor_rel_log_slope_odd", f"{rel_slope:.6e}")
    wb.add_data("verdict",
                ("DERIVED CHIRALITY STATE-INTEGRAL DATUM LANDED: Z_5₂ on the "
                 "substrate ray computed two independent ways (quadrature vs "
                 "factorization) and gated by the exact 4₁ closed form; the "
                 "frame-reduced odd part Im Ẑ is the fibre-level chirality datum "
                 "at q₀ — the state-integral face of the same odd channel as "
                 "A2's Stokes datum. Anchor-smooth (honest: not the swing). "
                 "No fit; no c_k wired; auditOnly."
                 if ok else "INCONCLUSIVE — a gate failed; inspect."))
    # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
    # pins deliberately, so no anchor list can classify it and it was going
    # out unstamped. Carries the values actually computed with.
    wb.save(q0_comparison(
        muon=Q0["muon"], proton=Q0["proton"],
        reason='computes the 5_2 chirality state integral at BOTH pins and reports each under its own key; the mu-vs-p difference is the subject',
    ))
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-t0:.0f}s total)")
    print("  witness -> computations/probes/qbeta-5two-chirality-state-integral.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
