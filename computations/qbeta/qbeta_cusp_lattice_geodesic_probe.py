#!/usr/bin/env python3
"""qbeta_cusp_lattice_geodesic_probe.py — SP2/W: the braid word's geodesic on the
cusp torus. Does the WINDING LATTICE supply the spin-dominated regime that SP1
found no smooth candidate could reach?

Author steering (2026-07-27): "if we think about the odd and even channels, and
the particle/torus knots, we can associate to a braid word a geodesic (flow) on
the torus for the particle/vortex path. sinh/cosh should align at this geometry."

DERIVE (two proved corpus inputs, no fit):
  1. `meridian-holonomy-boost.md` (proved): one meridian turn is a boost of
     rapidity `ln q₀`, and barEven(q)² − barOdd(q)² = 4 is the cosh²−sinh²=1
     hyperbola (holonomy_hyperbola, barEven_mul, barOdd_mul — rapidity adds).
  2. `cusp-shape-bar-parity.md` (proved, `cusp_barParity_split`): the cusp shape
     of 4₁ is `ω = e^{iπ/3}`, a primitive 6th root of unity (Φ₆), with
     barEven(ω)=1 (Volume face) and barOdd(ω)² = −3 (Chern–Simons face).

So the cusp torus is the flat torus ℂ/Λ, Λ = ℤ⟨1, ω⟩ (hexagonal/Eisenstein). A
closed geodesic — the particle/vortex path of a braid word — is a lattice class
(m, ℓ) [m meridian turns, ℓ longitude turns] with log-holonomy

        u_{m,ℓ} = ln q₀ · (m + ℓ ω),     ω = e^{iπ/3} = 1/2 + i·√3/2.

CHECK (assertions), under the corrected Im 𝔙₄₁ = (√3/4)(Re²u − Im²u) (#4372):

  [W1] Im 𝔙₄₁(u_{m,ℓ}) = (√3/16)·(ln q₀)²·[(2m+ℓ)² − 3ℓ²] EXACTLY. The winding
       dependence collapses onto the integer form G(x,y) = x² − 3y² in the
       coordinates x = 2m+ℓ, y = ℓ — the NORM FORM of ℤ[√3] (discriminant 12),
       the real quadratic field matching the cusp's own √−3 (barOdd(ω)² = −3).
  [W2] G is never 0 on the lattice (√3 is irrational), so every geodesic is
       strictly boost-dominated (G>0) or SPIN-dominated (G<0) — never null. The
       spin sector is the winding-slope window m/ℓ ∈ (−1/2−√3/2, −1/2+√3/2),
       i.e. the longitude-dominated directions m/ℓ ∈ {0, −1}.
  [W3] SINH/COSH ALIGNMENT (the author's prediction, made precise). G(x,y) = 1
       is the PELL equation x² − 3y² = 1, whose solutions are the units
       (2+√3)^n of ℤ[√3]: x_n = cosh(nρ), √3·y_n = sinh(nρ) with fundamental
       rapidity ρ = arccosh 2 = ln(2+√3). Under (barEven, barOdd) = (2x, 2√3 y)
       this is EXACTLY the proved holonomy hyperbola barEven²−barOdd² = 4. So
       the proved cosh/sinh boost identity IS the Pell equation of the cusp
       winding lattice, and its integer solutions form a discrete boost subgroup
       of rapidity n·arccosh 2 — the even/odd channels of a closed geodesic.
  [W4] meridian (1,0): G = 4 > 0 (boost) — reproduces the #4391 geometric-boost
       probe value to 40 digits. longitude (0,1): G = −2 < 0 ⇒ Im 𝔙₄₁ < 0, the
       SPIN-dominated regime. **The diagonal IS crossed on the lattice.** SP1's
       wall ("no geometric holonomy from q₀≈1.11 supplies Im u > Re u") was an
       artifact of the OFF-LATTICE fibre ansatz u = ln q₀(1 + i/2): the 60° cusp
       angle gives the longitude Im/Re = √3 > 1 for free, independent of q₀.
  [W5] HONEST NEGATIVE (scope-(a)). At the single derived scale c = ln q₀ the
       magnitudes are forced: S/B must be a G value (B = (√3/16)(ln q₀)²).
       Observed S_muon/B ≈ 8.2, S_proton/B ≈ −33.5 are not G values, and the
       canonical (meridian, longitude) pair predicts ratio G(0,1)/G(1,0) = −1/2
       against the observed ≈ −4.08. Worse, the lattice is expressive enough
       that SOME (m,ℓ) pair matches −4.08 to ~1% by chance (≈10⁴ candidate
       ratios from |m|,|ℓ| ≤ 5) — so ratio-matching here is NOT evidence, it is
       a fit trap. No (m,ℓ) is adopted.

CONCLUSION. The winding lattice is the first *derivable, non-smooth* candidate
for the SP2 crux: the sign of Im 𝔙₄₁ is a discrete ARITHMETIC invariant
(sign G) of the braid word's geodesic and carries NO q₀-dependence at all — so
the sign-flip need not come from q₀ hypersensitivity. Magnitudes remain open.
No u wired; no c_k; no SDeformedVolumeChannel instance; nothing fitted.
"""
from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
KAPPA = mp.sqrt(3) / 4
OMEGA = mp.exp(mp.mpc(0, 1) * mp.pi / 3)          # 4₁ cusp shape, primitive Φ₆ root


def S(q):
    """The target S-channel value at anchor q (c₃ target + Vol(4₁))."""
    return c3_target_at(q, QCOD, ME) + VOL41


def imV41(u: mp.mpc) -> mp.mpf:
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


def u_geodesic(q, m: int, ell: int) -> mp.mpc:
    """Log-holonomy of the (m,ℓ) closed geodesic on the 4₁ cusp torus."""
    return mp.log(q) * (m + ell * OMEGA)


def G(m: int, ell: int) -> int:
    """The disc-12 integer form (2m+ℓ)² − 3ℓ² = norm of (2m+ℓ) + ℓ√3 in ℤ[√3]."""
    return (2 * m + ell) ** 2 - 3 * ell * ell


def main() -> int:
    print("=" * 78)
    print(" SP2/W: braid-word geodesic on the 4₁ cusp torus — the winding lattice")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    B = KAPPA * mp.log(q_mu) ** 2 / 4             # the G = 1 quantum, (√3/16)(ln q₀)²
    print(f"\n cusp shape ω = e^{{iπ/3}} = {mp.nstr(OMEGA, 8)}   (Im/Re = √3 = {mp.nstr(mp.sqrt(3),6)})")
    print(f" anchors: S(muon) = {mp.nstr(S_mu,7)} (+)   S(proton) = {mp.nstr(S_pr,7)} (−)")
    print(f" quantum  B = (√3/16)(ln q₀)² = {mp.nstr(B,8)}   S_muon/B = {mp.nstr(S_mu/B,6)}"
          f"   S_proton/B = {mp.nstr(S_pr/B,6)}")

    # ---- [W1] winding dependence collapses onto the disc-12 norm form --------
    print("\n [W1] Im 𝔙₄₁(u_{m,ℓ}) = (√3/16)(ln q₀)²·G,  G = (2m+ℓ)² − 3ℓ²  (norm form of ℤ[√3])")
    w1_max_err = mp.mpf(0)
    print("      (m, ℓ)    G    Im 𝔙₄₁        regime")
    for (m, ell) in [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (1, 3), (3, 1), (-1, 1)]:
        u = u_geodesic(q_mu, m, ell)
        lhs, rhs = imV41(u), B * G(m, ell)
        w1_max_err = max(w1_max_err, abs(lhs - rhs))
        regime = "boost-dominated (+)" if G(m, ell) > 0 else "SPIN-dominated (−)"
        print(f"      ({m:2d},{ell:2d})  {G(m,ell):4d}   {mp.nstr(lhs,8):>13}  {regime}")
    w1 = w1_max_err < mp.mpf("1e-40")
    print(f"      max |Im 𝔙₄₁ − B·G| = {mp.nstr(w1_max_err,3)}   ⇒ exact: {bool(w1)}")

    # ---- [W2] no null geodesic; the spin sector is a slope window ------------
    lat = [(m, e) for m, e in product(range(-60, 61), repeat=2) if (m, e) != (0, 0)]
    no_null = all(G(m, e) != 0 for m, e in lat)
    lo, hi = -mp.mpf(1) / 2 - mp.sqrt(3) / 2, -mp.mpf(1) / 2 + mp.sqrt(3) / 2
    window_ok = all((G(m, e) < 0) == (lo < mp.mpf(m) / e < hi)
                    for m, e in lat if e != 0)
    spin_slopes = sorted({m for m in range(-3, 4) if lo < m < hi})
    w2 = no_null and window_ok
    print(f"\n [W2] G ≠ 0 on all {len(lat)} lattice classes (√3 irrational ⇒ no null geodesic): "
          f"{bool(no_null)}")
    print(f"      spin sector ⟺ winding slope m/ℓ ∈ ({mp.nstr(lo,5)}, {mp.nstr(hi,5)}); "
          f"integer slopes there: {spin_slopes} (longitude-dominated): {bool(window_ok)}")

    # ---- [W3] sinh/cosh alignment: Pell = the proved holonomy hyperbola ------
    rho = mp.acosh(2)                              # = ln(2+√3), fundamental rapidity
    pell, pell_err, hyper_err = [], mp.mpf(0), mp.mpf(0)
    for n in range(1, 7):
        xn, yn = mp.cosh(n * rho), mp.sinh(n * rho) / mp.sqrt(3)
        xi, yi = int(mp.nint(xn)), int(mp.nint(yn))
        pell.append((n, xi, yi, xi * xi - 3 * yi * yi))
        pell_err = max(pell_err, abs(xn - xi), abs(yn - yi))
        # (barEven, barOdd) = (2x, 2√3 y) satisfies the proved barEven²−barOdd² = 4
        hyper_err = max(hyper_err, abs((2 * xn) ** 2 - (2 * mp.sqrt(3) * yn) ** 2 - 4))
    w3 = (pell_err < mp.mpf("1e-30") and hyper_err < mp.mpf("1e-30")
          and all(v == 1 for _, _, _, v in pell) and abs(rho - mp.log(2 + mp.sqrt(3))) < mp.mpf("1e-40"))
    print(f"\n [W3] sinh/cosh alignment: Pell x²−3y²=1 ⟺ units (2+√3)ⁿ, ρ = arccosh 2 = "
          f"{mp.nstr(rho,8)}")
    print("      n:  (x_n, y_n) = (cosh nρ, sinh nρ/√3)   x²−3y²")
    for n, xi, yi, v in pell:
        print(f"      {n}:  ({xi:6d}, {yi:6d}){'':14s}{v:4d}")
    print(f"      integrality err {mp.nstr(pell_err,3)}; and (barEven,barOdd)=(2x,2√3y) satisfies")
    print(f"      the PROVED barEven²−barOdd²=4 to {mp.nstr(hyper_err,3)}  ⇒ aligned: {bool(w3)}")

    # ---- [W4] meridian vs longitude: the diagonal IS crossed -----------------
    u_mer, u_lon = u_geodesic(q_mu, 1, 0), u_geodesic(q_mu, 0, 1)
    ratio = mp.im(u_lon) / mp.re(u_lon)
    w4 = (abs(imV41(u_mer) - 4 * B) < mp.mpf("1e-40") and imV41(u_mer) > 0
          and imV41(u_lon) < 0 and ratio > 1 and imV41(u_lon) * S_pr > 0)
    print(f"\n [W4] meridian (1,0): G=+4, Im 𝔙₄₁ = {mp.nstr(imV41(u_mer),8)} (= #4391 boost value)")
    print(f"      longitude (0,1): Im u/Re u = {mp.nstr(ratio,6)} = √3 > 1 ⇒ "
          f"Im 𝔙₄₁ = {mp.nstr(imV41(u_lon),8)} < 0")
    print(f"      SPIN-dominated regime REACHED (proton-side sign): {bool(w4)}")
    print("      ⇒ SP1's 'no geometric holonomy supplies Im u > Re u' was an artifact of the")
    print("        OFF-LATTICE fibre ansatz; the 60° cusp angle supplies √3 free of q₀.")

    # ---- [W5] honest negative + the fit trap ---------------------------------
    obs_ratio = S_pr / S_mu
    canonical_ratio = mp.mpf(G(0, 1)) / G(1, 0)    # longitude / meridian = −1/2
    vals = sorted({G(m, e) for m, e in product(range(-40, 41), repeat=2)})
    near_mu = min(vals, key=lambda v: abs(mp.mpf(v) - S_mu / B))
    near_pr = min(vals, key=lambda v: abs(mp.mpf(v) - S_pr / B))
    small = [v for v in vals if 0 < v <= 50]
    # how easily does the lattice hit the observed ratio by chance?
    cand = [(a, b) for a in vals for b in vals if b != 0 and abs(mp.mpf(a) / b - obs_ratio) < abs(obs_ratio) / 100]
    w5 = (abs(S_mu / B - near_mu) > mp.mpf("0.5") and abs(S_pr / B - near_pr) > mp.mpf("0.5")
          and abs(obs_ratio - canonical_ratio) > mp.mpf("3") and len(cand) > 10)
    print(f"\n [W5] magnitudes at the derived scale c = ln q₀:")
    print(f"      S_muon/B   = {mp.nstr(S_mu/B,6)}   nearest G value = {near_mu}   (miss)")
    print(f"      S_proton/B = {mp.nstr(S_pr/B,6)}   nearest G value = {near_pr}   (miss)")
    print(f"      G spectrum ≤50: {small}")
    print(f"      observed S_p/S_m = {mp.nstr(obs_ratio,6)}  vs canonical longitude/meridian "
          f"= {mp.nstr(canonical_ratio,4)}")
    print(f"      FIT TRAP: {len(cand)} G-value pairs match the observed ratio within 1% by chance")
    print(f"      ⇒ SIGN mechanism only; magnitudes NOT reproduced, ratio-matching is not "
          f"evidence: {bool(w5)}")

    print("\n ⇒ the winding lattice gives the first DERIVABLE, NON-SMOOTH sign mechanism")
    print("   (sign Im 𝔙₄₁ = sign G(m,ℓ), an arithmetic invariant of the braid word's")
    print("   geodesic, carrying NO q₀-dependence). Magnitudes remain open.")

    wb = WitnessBuilder("qbeta-cusp-lattice-geodesic", engine="mpmath")
    wb.set_description(
        "SP2/W of the u(q₀) spin-part derivation (#4401): the braid word's closed geodesic on "
        "the 4₁ cusp torus (author steering — braid word ↦ geodesic flow, odd/even channels, "
        "sinh/cosh alignment). Combining two proved corpus inputs — meridian log-holonomy = "
        "ln q₀ (meridian-holonomy-boost) and cusp shape ω = e^{iπ/3} (cusp-shape-bar-parity) — "
        "the (m,ℓ) winding geodesic has u = ln q₀·(m+ℓω) and Im 𝔙₄₁ = (√3/16)(ln q₀)²·"
        "[(2m+ℓ)²−3ℓ²], the norm form of ℤ[√3] (disc 12), matching the cusp's own √−3. The form "
        "never vanishes (√3 irrational): every geodesic is strictly boost- or spin-dominated. "
        "The sinh/cosh alignment is exact: G=1 is the Pell equation whose units (2+√3)ⁿ give "
        "(x,y)=(cosh nρ, sinh nρ/√3), ρ=arccosh 2, and (barEven,barOdd)=(2x,2√3y) satisfies the "
        "PROVED holonomy hyperbola barEven²−barOdd²=4 — the proved boost identity IS the Pell "
        "equation of the winding lattice. The longitude (0,1) gives G=−2<0: the spin-dominated "
        "regime SP1 called unreachable IS reached (SP1's wall was an artifact of its off-lattice "
        "fibre ansatz; the 60° cusp angle gives Im/Re=√3>1 free of q₀). So the sign of Im 𝔙₄₁ "
        "is a discrete ARITHMETIC invariant of the winding, not a q₀-hypersensitivity — the "
        "first derivable non-smooth candidate for the SP2 crux. HONEST NEGATIVE (scope-(a)): at "
        "the derived scale the magnitudes are not reproduced — S_muon/B ≈ 8.2, S_proton/B ≈ "
        "−33.5 are not G values and the canonical meridian/longitude pair predicts ratio −1/2 "
        "vs observed ≈ −4.08; moreover many G-pairs match that ratio within 1% by chance, so "
        "ratio-matching is a fit trap. Sign mechanism only; no (m,ℓ) adopted. No fit, no c_k, "
        "no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("cusp_lattice_readout", {
        "cusp_shape_omega": "e^{iπ/3} (primitive Φ₆ root; cusp-shape-bar-parity, proved)",
        "u_geodesic": "u_{m,ℓ} = ln q₀ · (m + ℓ ω)",
        "imV41_form": "(√3/16)(ln q₀)² · [(2m+ℓ)² − 3ℓ²]  (norm form of ℤ[√3], disc 12)",
        "quantum_B": mp.nstr(B, 12),
        "no_null_geodesic": "G ≠ 0 on every lattice class (√3 irrational)",
        "spin_sector_slope_window": f"m/ℓ ∈ ({mp.nstr(lo,6)}, {mp.nstr(hi,6)}); integer slopes {spin_slopes}",
        "pell_fundamental_rapidity": f"ρ = arccosh 2 = ln(2+√3) = {mp.nstr(rho,12)}",
        "pell_units": str([(n, x, y) for n, x, y, _ in pell]),
        "meridian_1_0_G": "+4  (boost-dominated, Im 𝔙₄₁ > 0; reproduces #4391)",
        "longitude_0_1_G": "−2  (SPIN-dominated, Im 𝔙₄₁ < 0; diagonal CROSSED)",
        "S_muon_over_B": mp.nstr(S_mu / B, 10),
        "S_proton_over_B": mp.nstr(S_pr / B, 10),
        "observed_S_ratio": mp.nstr(obs_ratio, 10),
        "canonical_lattice_ratio": "−1/2 (longitude/meridian)",
        "fit_trap_pairs_within_1pct": str(len(cand)),
        "verdict": ("sign mechanism DERIVED and non-smooth (arithmetic in the winding, no q₀ "
                    "dependence); sinh/cosh alignment exact via Pell = proved holonomy "
                    "hyperbola; SP1's diagonal wall falls on the lattice; magnitudes NOT "
                    "reproduced at scale ln q₀ (scope-(a)), left open, no (m,ℓ) fitted")})
    wb.add_assertion("imV41_equals_disc12_norm_form", str(bool(w1)), "True")
    wb.add_assertion("no_null_geodesic_spin_sector_is_slope_window", str(bool(w2)), "True")
    wb.add_assertion("pell_units_are_proved_holonomy_hyperbola", str(bool(w3)), "True")
    wb.add_assertion("longitude_crosses_diagonal_meridian_matches_4391", str(bool(w4)), "True")
    wb.add_assertion("magnitudes_miss_and_ratio_matching_is_fit_trap", str(bool(w5)), "True")
    wb.save()
    print("\nwitness → qbeta-cusp-lattice-geodesic.witness.json")
    ok = all([w1, w2, w3, w4, w5])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
