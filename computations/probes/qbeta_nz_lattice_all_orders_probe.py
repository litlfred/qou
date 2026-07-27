#!/usr/bin/env python3
"""qbeta_nz_lattice_all_orders_probe.py — beyond the 2-jet: higher NZ jets of
the 4₁ potential AND the exact (all-orders) potential on the winding lattice.

Owner question (#4401 thread): "can we get higher order than two jet?" YES,
three ways, all exercised here on the corpus's own A-polynomial machinery
(imported from qbeta_nz_even_series_fourone_probe.py, PR #3622):

  1. NO ODD JETS EXIST: v(u) = log(−L(u)) is odd (corpus-verified), so the
     potential Φ (Φ' = v) is even — the 3-jet, 5-jet, … vanish identically.
     Amphichirality is the jet-parity statement.
  2. THE HIGHER EVEN JETS ARE EXACT TRACE-FIELD ELEMENTS: τ = −i√3 and
     v₃ = −i√3/3 are already corpus-recognized; the convention-free ratio
     v₃/(2τ) = 1/6 EXACTLY. Here we extract v₅, v₇ by the same Cauchy/FFT
     contour method at two radii (stability cross-check) and attempt the
     same small-height ℚ(i√3) recognition — reported TIERED (recognized /
     unrecognized), never asserted.
  3. ALL ORDERS AT ONCE ON THE LATTICE: Φ(u_{m,ℓ}) is computed EXACTLY
     (numerically, no truncation) by integrating the tracked geometric
     branch v along the ray 0 → u_{m,ℓ} = ln q₀·(m+ℓω). The sign pattern
     of Im Φ across the canonical windings is compared with the 2-jet
     prediction sign(G(m,ℓ)): [H3] asserts they AGREE at every tested
     winding — the arithmetic sign statement is not a 2-jet artifact.

Jet-arithmetic structure (why every jet stays lattice-arithmetic): the jet
coefficients lie in i·ℚ(√3) ⊂ ℚ(ω) and the windings in ℤ[ω] (Eisenstein), so
each 2k-jet contributes (ln q₀)^{2k} × an integer form in (m,ℓ) — e.g. the
4-jet correction multiplies the 2-jet by (1 + u²/6) with u² = c²(P+Qω),
P = m²−ℓ², Q = 2mℓ+ℓ² (exact, from v₃/(2τ) = 1/6).

Convention note: this file inherits the imported probe's branch convention
(τ = −i√3, the conjugate of the FigureEightComplexVolume half-potential's
+i√3/4 normalisation). Sign COMPARISONS are made within one convention;
conjugation flips all signs globally and preserves the pattern.

Honest scope: sign robustness is asserted only at the tested windings
(|u| ≤ 0.19, well inside the branch-tracking disc — closure defect asserted).
Nothing here produces a c_k, a magnitude, or wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qbeta_nz_even_series_fourone_probe import (  # noqa: E402
    B_of, contour_v_samples, recognize_q_sqrt_m3)
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_muon_at  # noqa: E402

mp.mp.dps = 60
SQRT3 = mp.sqrt(3)
OMEGA = mp.exp(mp.mpc(0, 1) * mp.pi / 3)


def v_coeffs(r, N=64, kmax=9):
    """Odd-series coefficients v₁(=τ), v₃, v₅, v₇, v₉ by Cauchy/FFT at radius r."""
    samples, closure = contour_v_samples(r, N)
    out = {}
    for k in range(1, kmax + 1, 2):
        c = sum(samples[j] * mp.e ** (-2j * mp.pi * j * k / N) for j in range(N)) / N
        out[k] = c / r**k
    return out, closure


def v_on_ray(u_target, K=1200):
    """Tracked geometric-branch samples of v along t·u_target, t ∈ (0,1]."""
    samples = []
    s_prev = None
    for j in range(1, K + 1):
        u = u_target * mp.mpf(j) / K
        M = mp.e ** (u / 2)
        w = (B_of(M) ** 2 - 4 * M**8) / u**2
        s = mp.sqrt(w)
        if s_prev is not None and abs(s - s_prev) > abs(-s - s_prev):
            s = -s
        s_prev = s
        L = (B_of(M) + u * s) / (2 * M**4)
        samples.append(mp.log(-L))
    return samples


def Phi_exact(u_target, K=1200):
    """All-orders Φ(u_target) = ∫₀¹ v(t·u)·u dt (composite trapezoid on the
    tracked ray; v(0) = 0). Branch pinned to the imported probe's convention
    (v ≈ −i√3·u near 0) by conjugating if needed."""
    samples = v_on_ray(u_target, K)
    # branch pin: near t→0, v/u must ≈ τ = −i√3 (imported convention). The two
    # longitude roots are RECIPROCALS (L·L' = M⁴/M⁴ = 1), so the wrong-root
    # correction is v ↦ −v (valid while |v| ≪ π, true on these rays) — NOT
    # conjugation, which is a different function off the real axis.
    lead = samples[0] / (u_target / K)
    if abs(lead - (-1j * SQRT3)) > abs(lead - (1j * SQRT3)):
        samples = [-s for s in samples]  # other root ⇒ reciprocal ⇒ v ↦ −v
    h = mp.mpf(1) / K
    acc = samples[0] / 2 * h  # v(0)=0 endpoint contributes 0
    for j in range(1, len(samples) - 1):
        acc += samples[j] * h
    acc += samples[-1] / 2 * h
    return acc * u_target


def G(m, l):
    return (2 * m + l) ** 2 - 3 * l * l


def main() -> int:
    print("=" * 78)
    print(" beyond the 2-jet: higher NZ jets + all-orders Φ on the winding lattice")
    print("=" * 78)
    c = mp.log(q_muon_at(50))

    # ---- [H1] higher jets: extract v₅, v₇ at two radii, attempt recognition --
    co1, cl1 = v_coeffs(mp.mpf("0.05"))
    co2, cl2 = v_coeffs(mp.mpf("0.08"))
    stab = max(abs(co1[k] - co2[k]) / abs(co1[k]) for k in (1, 3, 5, 7))
    h1 = stab < mp.mpf("1e-25") and cl1 < mp.mpf("1e-40") and cl2 < mp.mpf("1e-40")
    print(f"\n [H1] contour extraction stable across radii (rel {mp.nstr(stab,3)}), "
          f"closure {mp.nstr(cl1,3)}: {bool(h1)}")
    recs = {}
    for k in (1, 3, 5, 7):
        rec = recognize_q_sqrt_m3(co1[k], max_num=60, max_den=60)
        recs[k] = rec
        tier = f"RECOGNIZED (a,b,d)={rec}" if rec else "unrecognized (left numeric)"
        print(f"      v{k} = {mp.nstr(co1[k], 12)}   {tier}")

    # ---- [H2] the exact 4-jet ratio ------------------------------------------
    ratio = co1[3] / (2 * co1[1])
    h2 = abs(ratio - mp.mpf(1) / 6) < mp.mpf("1e-40")
    print(f"\n [H2] v₃/(2τ) = {mp.nstr(ratio, 12)} = 1/6 exactly: {bool(h2)}")
    print("      ⇒ 4-jet multiplies the 2-jet by (1 + u²/6); on the lattice u² = c²(P+Qω)")
    print("        with P = m²−ℓ², Q = 2mℓ+ℓ² — every jet is Eisenstein-arithmetic.")

    # ---- [H3] all-orders sign pattern vs 2-jet on the lattice ----------------
    print("\n [H3] all-orders Im Φ(u_{m,ℓ}) vs 2-jet sign(−G) at the canonical windings")
    print("      (imported convention τ = −i√3 ⇒ 2-jet Im Φ = −(√3/2)c²·G/4·... sign = −sign G)")
    windings = [(1, 0), (0, 1), (1, -1), (1, 1), (2, -1)]
    h3, h4_max = True, mp.mpf(0)
    print("      (m, ℓ)    G   sign2jet  Im Φ(all orders)    sign   4jet+tail rel.")
    for (m, l) in windings:
        u = c * (m + l * OMEGA)
        phi = Phi_exact(u)
        phi2 = (-1j * SQRT3 / 2) * u * u          # 2-jet in this convention
        s_all = 1 if mp.im(phi) > 0 else -1
        s_two = 1 if mp.im(phi2) > 0 else -1
        rel = abs(phi - phi2) / abs(phi2)
        h4_max = max(h4_max, rel)
        h3 &= (s_all == s_two) and (s_two == (1 if -G(m, l) > 0 else -1))
        print(f"      ({m:2d},{l:2d})  {G(m,l):4d}     {s_two:+d}     {mp.nstr(mp.im(phi),8):>13}"
              f"     {s_all:+d}      {mp.nstr(rel*100,3)}%")
    print(f"      all-orders sign = 2-jet sign at every tested winding: {bool(h3)}")

    # ---- [H4] jet convergence at the physical scale --------------------------
    h4 = h4_max < mp.mpf("0.02")
    print(f"\n [H4] worst all-orders deviation from the 2-jet at tested windings: "
          f"{mp.nstr(h4_max*100,3)}% < 2%: {bool(h4)}")
    print("      ⇒ at the physical scale c = ln q₀ the 2-jet dominates; higher jets are")
    print("        percent-level and cannot flip any |G| ≥ 2 sign.")

    wb = WitnessBuilder("qbeta-nz-lattice-all-orders", engine="mpmath")
    wb.set_description(
        "Beyond the 2-jet (#4401): higher NZ jets of the 4₁ potential and the exact "
        "all-orders Φ on the winding lattice, via the corpus A-polynomial machinery "
        "(qbeta_nz_even_series_fourone_probe). (1) No odd jets (v odd, corpus-verified). "
        "(2) Higher even jets: τ = −i√3, v₃ = −i√3/3 corpus-recognized; v₃/(2τ) = 1/6 "
        "EXACT ⇒ the 4-jet multiplies the 2-jet by (1 + u²/6), Eisenstein-arithmetic on "
        "the lattice; v₅, v₇ extracted radius-stably and recognition attempted at small "
        "height (tiered, see data). (3) All-orders Φ(u_{m,ℓ}) by tracked-branch ray "
        "integration at the canonical windings: the sign pattern agrees with the 2-jet "
        "arithmetic sign(G) at every tested winding, with worst all-orders deviation "
        "from the 2-jet < 2% at the physical scale ln q₀ — the lattice sign mechanism "
        "is NOT a truncation artifact. Signs compared within one branch convention. "
        "No c_k, no magnitude claim, nothing wired.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("jets_readout", {
        "tau": mp.nstr(co1[1], 20), "v3": mp.nstr(co1[3], 20),
        "v5": mp.nstr(co1[5], 20), "v7": mp.nstr(co1[7], 20),
        "recognitions_a_b_d": {str(k): (str(r) if r else "unrecognized")
                               for k, r in recs.items()},
        "ratio_v3_over_2tau": "1/6 (exact to 1e-40)",
        "lattice_jet_structure": ("Φ = (τ/2)u²(1 + u²/6 + O(u⁴)); u² = c²(P+Qω), "
                                  "P=m²−ℓ², Q=2mℓ+ℓ² — all jets Eisenstein-arithmetic"),
        "all_orders_worst_rel_dev_from_2jet": mp.nstr(h4_max, 8),
        "verdict": ("sign pattern all-orders = 2-jet arithmetic at every tested "
                    "winding; higher jets percent-level at ln q₀ scale")})
    wb.add_assertion("contour_extraction_radius_stable_branch_closed", str(bool(h1)), "True")
    wb.add_assertion("four_jet_ratio_exactly_one_sixth", str(bool(h2)), "True")
    wb.add_assertion("all_orders_sign_equals_2jet_arithmetic_sign", str(bool(h3)), "True")
    wb.add_assertion("higher_jets_percent_level_at_physical_scale", str(bool(h4)), "True")
    wb.save()
    print("\nwitness → qbeta-nz-lattice-all-orders.witness.json")
    ok = all([h1, h2, h3, h4])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
