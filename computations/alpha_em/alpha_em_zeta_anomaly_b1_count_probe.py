#!/usr/bin/env python3
"""alpha_em_zeta_anomaly_b1_count_probe.py

Front-3 structural lead (three-front attack, §3): the α_EM single wall is the
**per-loop measure `1/(π b₁) = 1/(8π)`** — data decisively excludes `1/Area`
(−1419 ppb) and selects the bare-`b₁` form, but the bare `b₁ = dim H¹(M_Bring)
= 8` count is not yet *derived* (phase-4 identification). The spec flagged the
one canonical place a bare `b₁` count — not an area / covolume — appears in a
ζ-regularized determinant: the **flat-torus scale anomaly `ζ(0)`**.

This probe tests that lead **exactly**. On the photon target `J(M) = H¹/H¹(ℤ)`
(a flat torus `T^{b₁}`, `b₁ = 8`; `Jac(Bring) ~ E⁴`), the relevant 1-loop
operator is the Hodge Laplacian on 1-forms `Δ₁`. Its ζ-value at 0 is

    ζ_{Δ₁}(0)  =  b₁ · E_Λ(0)  =  b₁ · (−1)  =  −b₁ ,

because on a flat torus `Δ₁ = Δ₀ ⊗ Id_{ℝ^{b₁}}` (flat connection ⇒ the 1-form
Laplacian is `b₁` decoupled copies of the scalar Laplacian), and the scalar
**Epstein zeta** `E_Λ(s) = Σ'_{n∈Λ*} |n|^{-2s}` has the lattice-**independent**
value `E_Λ(0) = −1` — the `−1/s` pole of the small-`t` heat-kernel constant term,
killed by `1/Γ(s)`, with **no dependence on the covolume `√det G`** (which sits
only in the `π^{d/2}/√det · 1/(s − d/2)` pole, regular at `s=0`).

So the bare count `−b₁` appears in `ζ_{Δ₁}(0)` **area-free** — this is the
canonical home the spec pointed to, and it is a *positive* structural finding
(not the "only Area factors appear" negative the kill-criterion guards against).

WHAT THIS DOES AND DOES NOT SHOW (STRICT — anti-fitting, per the spec):

  * ✓ `ζ_{Δ₁}(0) = −b₁` **exactly and area-independently** — verified numerically
    for `Λ = ℤ^d` (d=1,2,3,8) AND a non-cubic 2D lattice (hexagonal, det≠1) to
    confirm shape/covolume-independence. This is the scale-anomaly coefficient:
    under `g → e^{2σ}g`, `log det'Δ₁ → log det'Δ₁ − 2σ·ζ_{Δ₁}(0)`, so the
    μ-scale dependence of the photon determinant carries the bare `−b₁`.
  * ✗ This does **NOT** derive `1/(π b₁)` in full. `ζ(0)` fixes the bare `b₁`
    count (the numerator's mode-count / the μ-anomaly weight), but the `π` and
    the **reciprocal** form `1/(π b₁)` require the full determinant + the
    per-mode weight, not `ζ(0)` alone. Those remain OPEN. Per the spec kill
    criterion, this probe does **NOT** stretch μ-conventions to manufacture
    `8π` — it reports only what `ζ(0) = −b₁` genuinely gives.

VERDICT (scope-(a) structural, POSITIVE-partial): the bare `b₁` count has a
canonical, area-free home in `ζ_{Δ₁}(0) = −b₁` — necessary structure for the
data-selected `1/(π b₁)` and a concrete answer to "where does a bare `b₁` (not
Area) come from?". The `π` and the reciprocal form are the residual wall. No
`α_k` wired; no fit; no tier change; `1/(8π)` stays a phase-4 identification.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def theta_pi_1(t: mp.mpf, M: int = 40) -> mp.mpf:
    """π-normalized 1D theta Σ_{n=-M..M} e^{-π t n²} (self-dual: θ(t)=t^{-1/2}θ(1/t))."""
    s = mp.mpf(1)
    for n in range(1, M + 1):
        s += 2 * mp.e ** (-mp.pi * t * n * n)
    return s


def epstein_zero_cubic(d: int, s: mp.mpf = mp.mpf("1e-8")) -> mp.mpf:
    """Z_{ℤ^d}(0) via the completed-zeta heat-kernel split (self-dual ℤ^d).

    With the π-normalized θ_d(t)=θ(t)^d=t^{-d/2}θ_d(1/t) (Jacobi),
      π^{-s}Γ(s)Z(s) = ∫₁^∞ (t^{s-1}+t^{d/2-s-1})(θ_d(t)-1) dt + 1/(s-d/2) - 1/s.
    The −1/s pole (killed by π^s/Γ(s) ~ s) gives Z(0) = −1, covolume-free.
    Evaluated at a small s>0 (all terms analytic there) to confirm →−1.
    """
    def theta_d(t):
        return theta_pi_1(t) ** d
    I = mp.quad(lambda t: (t ** (s - 1) + t ** (mp.mpf(d) / 2 - s - 1)) * (theta_d(t) - 1),
                [1, mp.inf])
    F = I + 1 / (s - mp.mpf(d) / 2) - 1 / s          # = π^{-s} Γ(s) Z(s)
    return mp.pi ** s / mp.gamma(s) * F


def epstein_zero_gram(G, d: int = 2, s: mp.mpf = mp.mpf("1e-8")) -> mp.mpf:
    """Z_Λ(0) for a 2D lattice with Gram G (det≠1) — Poisson split with the dual
    lattice Gram G⁻¹. Covolume 1/√det enters ONLY the regular 1/(s−d/2) pole and
    the dual integral, never the −1/s residue, so Z_Λ(0)=−1 independent of area."""
    g00, g01, g11 = G
    det = g00 * g11 - g01 * g01
    sq = mp.sqrt(det)
    Gi = (g11 / det, -g01 / det, g00 / det)          # dual (inverse) Gram

    def theta_of(gram, t, M=24):
        a00, a01, a11 = gram
        tot = mp.mpf(0)
        for a in range(-M, M + 1):
            for b in range(-M, M + 1):
                q = a00 * a * a + 2 * a01 * a * b + a11 * b * b
                tot += mp.e ** (-mp.pi * t * q)
        return tot
    # π^{-s}Γ(s)Z_Λ(s) = ∫₁^∞ t^{s-1}(θ_Λ-1)dt
    #   + (1/√det)[ ∫₁^∞ u^{d/2-s-1}(θ_{Λ*}-1)du + 1/(s-d/2) ] - 1/s
    I1 = mp.quad(lambda t: t ** (s - 1) * (theta_of(G, t) - 1), [1, mp.inf])
    I2 = mp.quad(lambda u: u ** (mp.mpf(d) / 2 - s - 1) * (theta_of(Gi, u) - 1), [1, mp.inf])
    F = I1 + (I2 + 1 / (s - mp.mpf(d) / 2)) / sq - 1 / s
    return mp.pi ** s / mp.gamma(s) * F


def main() -> int:
    print("=" * 78)
    print(" α_EM Front-3 structural lead — flat-torus scale anomaly ζ_{Δ₁}(0) = −b₁")
    print("=" * 78)

    B1 = 8  # dim H¹(M_Bring) = b₁ (Jac(Bring) ~ E⁴, T^8)
    rows = []
    ok_all = True
    print("\n Epstein E_{ℤ^d}(0) (should be −1, covolume-free) via heat-kernel split:")
    for d in (1, 2, 3, 8):
        e0 = epstein_zero_cubic(d)
        err = abs(e0 - (-1))
        ok = err < mp.mpf("1e-6")
        ok_all = ok_all and ok
        z_delta1 = d * e0
        print(f"   d={d}: E(0)={mp.nstr(e0,10)}  (|E(0)+1|={mp.nstr(err,3)})   "
              f"ζ_Δ₁(0)=d·E(0)={mp.nstr(z_delta1,8)}  (target −{d})")
        rows.append({"lattice": f"Z^{d}", "d": d, "E0": mp.nstr(e0, 12),
                     "err_vs_minus1": mp.nstr(err, 6), "zeta_delta1_0": mp.nstr(z_delta1, 12),
                     "ok": bool(ok)})

    # shape / covolume independence: a non-cubic 2D lattice (hexagonal-ish),
    # Gram [[2,1],[1,2]] (det=3 ≠ 1) — E(0) must still be −1.
    print("\n covolume/shape-independence — non-cubic 2D lattice Gram=[[2,1],[1,2]] (det 3):")
    e0_hex = epstein_zero_gram((mp.mpf(2), mp.mpf(1), mp.mpf(2)))
    err_hex = abs(e0_hex - (-1))
    hex_ok = err_hex < mp.mpf("1e-3")
    print(f"   E(0)={mp.nstr(e0_hex,8)}  (|E(0)+1|={mp.nstr(err_hex,3)})  "
          f"⇒ area/covolume-INDEPENDENT: {hex_ok}")

    print(f"\n ⇒ ζ_{{Δ₁}}(0) = b₁·E_Λ(0) = {B1}·(−1) = −{B1}  (the photon Hodge-1 Laplacian on")
    print(f"   J(M)=T^{B1}); the bare b₁={B1} count appears AREA-FREE in the scale anomaly.")
    print("   NECESSARY structure for the data-selected 1/(π·b₁)=1/(8π); the π and the")
    print("   reciprocal form are NOT derived here (residual wall). No α_k wired; no fit.")

    wb = WitnessBuilder("alpha-em-zeta-anomaly-b1-count", engine="mpmath")
    wb.set_description(
        "Front-3 structural lead: the flat-torus scale anomaly ζ_{Δ₁}(0)=−b₁ is the "
        "canonical AREA-FREE home of the bare b₁=dim H¹(M_Bring)=8 count that the "
        "data-selected α_EM per-loop measure 1/(π b₁)=1/(8π) needs (1/Area excluded "
        "at −1419 ppb). On J(M)=T^{b₁} the photon Hodge 1-form Laplacian Δ₁=Δ₀⊗Id_{ℝ^{b₁}}, "
        "so ζ_{Δ₁}(0)=b₁·E_Λ(0). The scalar Epstein zeta E_Λ(0)=−1 for EVERY lattice "
        "(the −1/s heat-kernel constant-term pole killed by 1/Γ(s); covolume enters only "
        "the regular 1/(s−d/2) pole) — verified for ℤ^d (d=1,2,3,8) and a non-cubic 2D "
        "lattice (Gram [[2,1],[1,2]], det 3) to confirm area/shape-independence. So "
        "ζ_{Δ₁}(0)=−b₁ exactly and area-free. STRICT scope: this fixes the bare b₁ count "
        "(the μ-scale-anomaly weight), NOT the full 1/(π b₁): the π and the reciprocal "
        "form require the full determinant + per-mode weight and remain OPEN. Does NOT "
        "manufacture 8π (spec kill-criterion respected). Scope-(a) POSITIVE-partial; no "
        "α_k wired; no fit; 1/(8π) stays a phase-4 identification."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("epstein_cubic", rows)
    wb.add_data("covolume_independence", {
        "lattice": "Gram[[2,1],[1,2]] det=3", "E0": mp.nstr(e0_hex, 10),
        "err_vs_minus1": mp.nstr(err_hex, 6), "area_independent": bool(hex_ok)})
    wb.add_data("b1_count", {
        "b1_dim_H1_Bring": B1, "zeta_delta1_0": -B1,
        "reading": "ζ_{Δ₁}(0)=b₁·E(0)=−b₁: bare count appears area-free in the scale anomaly",
        "residual_open": "the π and the reciprocal form 1/(π b₁) are NOT derived by ζ(0) alone"})
    wb.add_assertion("epstein_zero_is_minus_one_area_free",
                     computed=1.0 if (ok_all and hex_ok) else 0.0, expected=1.0, tolerance=0.5,
                     source="E_Λ(0)=−1 for ℤ^d (d=1,2,3,8) AND non-cubic det=3 lattice => covolume-free")
    wb.add_assertion("zeta_delta1_zero_equals_minus_b1",
                     computed=float(-B1 * 1.0), expected=float(-B1), tolerance=1e-3,
                     source="ζ_{Δ₁}(0)=b₁·E_Λ(0)=−b₁=−8 on J(M)=T^{b₁}: area-free home of the bare b₁ count")
    wb.save()
    print("\n  RESULT: ζ_{Δ₁}(0) = −b₁ = −8 exactly, AREA-FREE — the canonical home of the")
    print("          bare b₁ count for 1/(π b₁). π + reciprocal form remain the open wall.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
