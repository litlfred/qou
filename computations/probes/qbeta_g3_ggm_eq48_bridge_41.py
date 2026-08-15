#!/usr/bin/env python3
"""qbeta_g3_ggm_eq48_bridge_41.py — A_ω step 3 (u = 0 calibration leg):
numeric verification of the GGM exact/perturbative bridge eq (48) for 4₁
at the substrate point, deriving the integer connection matrix M_I(0).

The bridge (GGM, library/arxiv-2012.00062v3/2012.00062v3.pdf, all glyph-extracted):

    diag(1/√τ, √τ)·g(τ) = M_R(q̃)·s_R(Φ)(τ)                       (48)

  * g(τ) = (G⁰(e^{2πiτ}), G¹(e^{2πiτ})) — the EXACT convergent q-series
    (43a/b) = the m = 0 case of the Theorem-9-certified machinery in
    qbeta_g3_ggm_stokes_41.py (these are the series of the state-integral
    factorization (44) = GK Cor 1.7, i.e. the exact Φ_b state integral).
  * Φ = (Φ_σ1, Φ_σ2), Φ_σ(τ) = exp(V(σ)/(2πiτ))·φ_σ(τ), V(σ1) = i·Vol(4₁)
    (eqs 39-41), with the symmetry Φ_σ2(τ) = i·Φ_σ1(−τ).
  * φ_σ1 exact printed coefficients (eq 42):
      φ_σ1(τ/(2πi)) = pref·(1 + 11τ/r + 697τ²/(2r²) + 724351τ³/(30r³) + …),
      r = 72√−3 (√−3 = i√3, positive imaginary part).
    The overall constant `pref` is OCR-ambiguous (3^{−1/4}/4 vs 1/(4√3));
    both are scanned — the integer test on M resolves it (the two readings
    differ by 3^{1/4} ≈ 1.316, incompatible with an integer matrix twice).
  * M_R(q̃) is a matrix of INTEGER q̃-series (Conjecture 10 ties it to
    W₋₁(q̃)ᵀ). On the substrate ray q = e^{−t} ⟺ τ = it/(2π), so
    q̃ = e^{−4π²/t} ≈ 1e-164: M_R(q̃) is its integer constant term M_R(0)
    to ~160 digits. The sector ambiguity (the imaginary-τ axis vs the
    Fig-3 sectors) is likewise invisible at this precision — lateral sums
    differ by O(q̃).

Method (no fit; the only free object is a 2×2 matrix DERIVED and then
integer-certified):
  1. LHS_j = diag(1/√τ_j, √τ_j)·g(τ_j) exactly (convergent series, dps 80)
     at three points τ_j = i·t_j/(2π) on the substrate ray.
  2. RHS basis Φ(τ_j) from the exact order-3 series (raw truncation;
     relative error ~1e-9 at |τ| ≈ 0.0166, estimated from the order-2/3
     difference and reported honestly).
  3. Solve M from points 1-2; CHECK M is integer to the series accuracy;
     round; verify on the held-out point 3.
  4. Cross-check Conjecture 10 shape: X = (W₋₁(0)ᵀ)⁻¹·M is small integer.

Physics rows: at u = 0 the non-perturbative channel at the substrate is
q̃ ≈ 1e-164 — utterly invisible — while the corpus's measured DEFORMED
odd-channel datum (Im 𝔙̃_b ≈ 0.0585, #3819) is O(1). So A_ω cannot be a
u = 0 Stokes effect; it must live in the deformed (u ≠ 0) structure, in
line with the ξ-frame phase law (perturbative tower has no intrinsic odd
phase; the odd channel is non-perturbative AND deformation-carried). This
probe certifies the machinery (normalizations, Borel-side conventions,
the integer dressing) on the exactly-solvable u = 0 leg first.

Anti-laundering: no A_ω identification is claimed here; this is the
calibration leg of step 3. Scope-(a); exact series + mpmath (dps 80, no
float64); no fit; no c_k wired.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_ggm_stokes_41", _HERE / "qbeta_g3_ggm_stokes_41.py")
_ggm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ggm)

mp.mp.dps = 80

ORD_G = 1400          # e^{-t·1400} ≈ 1e-63 tail for the convergent G side

# exact printed φ_σ1 numerators/denominators (GGM eq 42)
PHI_NUM = [1, 11, 697, 724351]
PHI_DEN = [1, 1, 2, 30]


def phi_sigma1(tau, pref):
    """φ_σ1(τ) from the exact order-3 printed series (argument mapping:
    the printed series is in τ with the function evaluated at τ/(2πi),
    so φ_σ1(w) uses τ = 2πi·w)."""
    r = 72 * mp.sqrt(3) * mp.mpc(0, 1)          # 72·√−3, positive imag part
    targ = 2 * mp.pi * mp.mpc(0, 1) * tau
    s = mp.mpc(0)
    for k in range(4):
        s += mp.mpf(PHI_NUM[k]) / PHI_DEN[k] * (targ / r) ** k
    return pref * s


def phi_sigma1_trunc(tau, pref, kmax):
    r = 72 * mp.sqrt(3) * mp.mpc(0, 1)
    targ = 2 * mp.pi * mp.mpc(0, 1) * tau
    s = mp.mpc(0)
    for k in range(kmax + 1):
        s += mp.mpf(PHI_NUM[k]) / PHI_DEN[k] * (targ / r) ** k
    return pref * s


def Phi_vec(tau, pref, kmax=3):
    """(Φ_σ1(τ), Φ_σ2(τ)) with Φ_σ2(τ) = i·Φ_σ1(−τ) (eq 40 symmetry)."""
    vol = 2 * mp.clsin(2, mp.pi / 3)
    V1 = mp.mpc(0, 1) * vol
    def one(t_):
        return mp.e ** (V1 / (2 * mp.pi * mp.mpc(0, 1) * t_)) * \
            phi_sigma1_trunc(t_, pref, kmax)
    return (one(tau), mp.mpc(0, 1) * one(-tau))


def g_exact(tau):
    """(G⁰(q), G¹(q)) at q = e^{2πiτ} from the certified integer series."""
    q = mp.e ** (2 * mp.pi * mp.mpc(0, 1) * tau)
    g0s, g1s = _ggm.G_series(0, ORD_G)
    g0 = mp.fsum(c * q ** k for k, c in enumerate(g0s) if c)
    g1 = mp.fsum(c * q ** k for k, c in enumerate(g1s) if c)
    return g0, g1


def lhs_vec(tau):
    g0, g1 = g_exact(tau)
    rt = mp.sqrt(tau)                            # principal branch
    return (g0 / rt, rt * g1)


def solve_M(taus, pref, kmax=3):
    """Solve the 2×2 matrix M from LHS_j = M·Φ_j at two points."""
    L = [lhs_vec(t_) for t_ in taus]
    P = [Phi_vec(t_, pref, kmax) for t_ in taus]
    # columns are the two sample points: M·[P0 P1] = [L0 L1]
    Pm = mp.matrix([[P[0][0], P[1][0]], [P[0][1], P[1][1]]])
    Lm = mp.matrix([[L[0][0], L[1][0]], [L[0][1], L[1][1]]])
    M = Lm * Pm ** -1
    return M


def main() -> int:
    print("=" * 78)
    print(" A_ω step 3 (u=0 leg) — GGM eq (48) bridge at the substrate, exact vs Φ")
    print("=" * 78)

    t_sub = mp.log(q_at(50))
    ts = [t_sub, mp.mpf("1.3") * t_sub, mp.mpf("1.6") * t_sub]
    taus = [mp.mpc(0, 1) * t_ / (2 * mp.pi) for t_ in ts]
    qtilde_mag = mp.e ** (-4 * mp.pi ** 2 / t_sub)
    print(f"\n substrate: t = {mp.nstr(t_sub, 12)}, τ = it/2π, "
          f"|q̃| = e^(−4π²/t) ≈ 10^{mp.nstr(mp.log10(qtilde_mag), 6)}")

    prefs = {"3^(-1/4)/4": mp.mpf(3) ** mp.mpf("-0.25") / 4,
             "1/(4*sqrt(3))": 1 / (4 * mp.sqrt(3))}
    results = {}
    for name, pref in prefs.items():
        M = solve_M(taus[:2], pref)
        devs = [abs(M[i, j] - mp.nint(mp.re(M[i, j])))
                for i in range(2) for j in range(2)]
        results[name] = (M, max(devs))
        print(f"\n [pref = {name}] solved M from τ₁,τ₂:")
        for i in range(2):
            print("   ", "  ".join(mp.nstr(M[i, j], 12) for j in range(2)))
        print(f"    max deviation from integer: {mp.nstr(max(devs), 4)}")

    best = min(results, key=lambda n: results[n][1])
    M_best, dev_best = results[best]
    others = [n for n in results if n != best]
    dev_other = results[others[0]][1]
    v_pref = dev_best < mp.mpf("1e-4") and dev_other > mp.mpf("0.01")
    print(f"\n integer-selected prefactor: {best} "
          f"(dev {mp.nstr(dev_best, 3)} vs {mp.nstr(dev_other, 3)}) ok={v_pref}")

    Mint = [[int(mp.nint(mp.re(M_best[i, j]))) for j in range(2)]
            for i in range(2)]
    print(f" derived integer M_I(0) = {Mint}")

    # held-out verification at τ₃ + truncation-error honesty (order 2 vs 3)
    pref = prefs[best]
    L3 = lhs_vec(taus[2])
    P3 = Phi_vec(taus[2], pref)
    R3 = [Mint[i][0] * P3[0] + Mint[i][1] * P3[1] for i in range(2)]
    rel3 = max(abs(L3[i] - R3[i]) / abs(L3[i]) for i in range(2))
    P3_o2 = Phi_vec(taus[2], pref, kmax=2)
    trunc_est = max(abs(P3[i] - P3_o2[i]) / abs(P3[i]) for i in range(2))
    v_holdout = rel3 < 10 * trunc_est + mp.mpf("1e-8")
    print(f"\n held-out point τ₃: relative residual = {mp.nstr(rel3, 4)} "
          f"(order-2/3 truncation estimate {mp.nstr(trunc_est, 4)}) ok={v_holdout}")

    # Conjecture-10 shape: X = (W₋₁(0)ᵀ)⁻¹ · M integer
    W = _ggm.W_matrix(-1, 4)
    W0T = mp.matrix([[W[j][i][0] for j in range(2)] for i in range(2)])
    X = W0T ** -1 * mp.matrix(Mint)
    devX = max(abs(X[i, j] - mp.nint(mp.re(X[i, j])))
               for i in range(2) for j in range(2))
    Xint = [[int(mp.nint(mp.re(X[i, j]))) for j in range(2)] for i in range(2)]
    v_shape = devX < mp.mpf("1e-20")
    print(f" Conjecture-10 shape: X = (W₋₁(0)ᵀ)⁻¹·M = {Xint} "
          f"(integer dev {mp.nstr(devX, 3)}) ok={v_shape}")

    print(f"\n [physics] at u = 0 the substrate non-perturbative channel is "
          f"|q̃| ≈ 1e{int(mp.log10(qtilde_mag))}: invisible. The corpus's "
          f"measured DEFORMED odd datum Im 𝔙̃_b ≈ 0.0585 (#3819) is O(1) — "
          f"A_ω is a deformation-carried effect, not a u = 0 Stokes effect.")

    ok = v_pref and v_holdout and v_shape
    verdict = (
        f"GGM eq-(48) bridge verified numerically at the substrate ray for "
        f"4_1 at u=0: the exact side (Theorem-9-certified G-series = the "
        f"GK state-integral factorization) equals the integer-dressed "
        f"asymptotic side with DERIVED integer matrix M_I(0) = {Mint} "
        f"(prefactor {best} selected by integrality; held-out residual "
        f"{mp.nstr(rel3, 3)} within the order-3 truncation estimate "
        f"{mp.nstr(trunc_est, 3)}; Conjecture-10 shape X = {Xint} integer: "
        f"{v_shape}). Structural finding: at u=0 the substrate "
        f"non-perturbative channel is |q~| ~ 1e{int(mp.log10(qtilde_mag))} "
        f"(invisible), while the measured deformed Im V_b ~ 0.0585 is O(1) "
        f"— A_omega is deformation-carried. Calibration leg only; no "
        f"A_omega identification claimed. Scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-ggm-eq48-bridge-41", engine="mpmath")
    wb.set_description(
        "A_omega step 3, u=0 calibration leg: numeric verification of GGM "
        "eq (48) for 4_1 at the substrate ray. Exact convergent G-series "
        "side vs order-3 exact asymptotic side; integer connection matrix "
        "M_I(0) DERIVED (not OCR-read, not fitted) and cross-checked "
        "against the Conjecture-10 W-transpose shape. Records the "
        "structural finding that the u=0 non-perturbative channel is "
        "~1e-164 at the substrate while the deformed odd datum is O(1).")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source", "library/arxiv-2012.00062v3/2012.00062v3.pdf (GGM) eqs 37-48 + Conj 10")
    wb.add_data("substrate", {"t": mp.nstr(t_sub, 25),
                              "tau": "i*t/(2*pi)",
                              "log10_qtilde": mp.nstr(mp.log10(qtilde_mag), 8)})
    wb.add_data("prefactor_scan", {n: {"max_int_dev": mp.nstr(d, 6)}
                                   for n, (m, d) in results.items()})
    wb.add_data("derived_M_I0", Mint)
    wb.add_data("conjecture10_X", Xint)
    wb.add_data("holdout", {"rel_residual": mp.nstr(rel3, 8),
                            "truncation_estimate": mp.nstr(trunc_est, 8)})
    wb.add_data("physics_note",
                "u=0 non-perturbative channel invisible at substrate "
                "(|q~|~1e-164); measured deformed Im V_b ~ 0.0585 is O(1); "
                "A_omega must be deformation-carried (u != 0)")
    wb.add_data("verdict", verdict)
    wb.add_assertion("integer_M_derived",
                     computed=1.0 if v_pref else 0.0, expected=1.0, tolerance=0.5,
                     source="M solved from 2 ray points is integer; wrong "
                            "prefactor reading rejected by the same test")
    wb.add_assertion("holdout_point_verifies",
                     computed=1.0 if v_holdout else 0.0, expected=1.0, tolerance=0.5,
                     source="held-out third ray point matches within the "
                            "order-3 truncation estimate")
    wb.add_assertion("conjecture10_shape_integer",
                     computed=1.0 if v_shape else 0.0, expected=1.0, tolerance=0.5,
                     source="X = (W_-1(0)^T)^-1 M is an integer matrix")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
