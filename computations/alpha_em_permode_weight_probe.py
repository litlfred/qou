#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical spectral-zeta witness; no symbolic-q
# polynomial output (substrate q₀ does not enter — the objects are topological/analytic).
"""alpha_em_permode_weight_probe.py — where the 1/π per-mode weight can (and cannot) come from.

Follow-up to the ζ_Λ(0)=−b₁ structural lead
([`alpha_em_zeta_anomaly_b1_probe.py`](alpha_em_zeta_anomaly_b1_probe.py), PR #3831):
that established the b₁ COUNT of the photon loop measure `1/(π·b₁)=1/(8π)` as a
bare topological integer. The identified open next piece is the **1/π per-mode
weight** — the analog of the proved `1/(12π)` template's *geometric-identity*
factor. This probe determines, honestly, where that `1/π` can be forced from and
where it CANNOT — the spec-§3 fitting-trap test ("the ζ-determinant μ-dependence
can absorb any constant; a derivation must force it, not reverse-engineer it").

Decisive findings (all exact / machine-verified):

  1. **The flat-torus ζ-determinant per-mode weight is NOT the source of 1/π.**
     `det'(−∂²)` on a circle S¹ of circumference L is exactly `L²` (the 2π
     cancels in ζ'(0)): scale-dependent, μ-absorbable, no bare 1/π. So the naive
     "per-mode weight = flat ζ-determinant" route is the fitting trap the spec
     warned of — RULED OUT (scope-(a)).
  2. **The proved 1/(12π) template's π is topological — Gauss–Bonnet 2πχ.**
     Area = −2πχ = 4π(g−1) = 12π at g=4, and `2/(3π) = 8/(12π) = b₁/Area`.
     The π there is the Euler-characteristic 2π, not a Gaussian/loop 2π.
  3. **The loop measure is `1/(8π) = 1/(π·b₁) = 1/(2π·g)`** — its π, if
     topological, needs a **2π·g** (genus) source, DISTINCT from the template's
     **2π·χ = 4π(g−1)** (Euler-characteristic) source. So `1/(8π)` is not the
     same geometric identity as `2/(3π)`; a fresh `2πg` identification is
     required.

Conclusion (scope-(a); no fit; not reverse-engineered to 8π): the `1/π`
per-mode weight is NOT derivable from the flat ζ-determinant (that gives L²,
scale-dependent — the fitting trap confirmed). A μ-independent `1/π` must come
from a topological/anomaly source; the framework's canonical such π is the
**archimedean dilogarithm regulator** (Bloch–Suslin pentagon-uniqueness forcing
the Bloch–Wigner `D`; `conj:dilogarithm-archimedean-limit`,
`em-coupling-bring-zero-mode.md`). Closing `1/(8π)` therefore REDUCES to that
named open conjecture PLUS an explicit `2π·g` (genus, not Euler-χ) identity on
Bring's surface — it does not close by ζ-determinant bookkeeping alone. This
confirms the spec's own warning and localizes the remaining work precisely.

Run: python3 -u computations/alpha_em_permode_weight_probe.py 2>&1 | tee /tmp/permode.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

G = 4                      # Bring genus
B1 = 2 * G                 # b₁ = 8
CHI = 2 - 2 * G            # χ = −6


def detprime_S1(L):
    """det'(−∂²) on S¹ of circumference L, via ζ_{S¹}(s)=2(L/2π)^{2s}ζ_R(2s):
    returns (det', ζ'(0), ζ(0)). Closed form det' = L² (the 2π cancels)."""
    L = mp.mpf(L)
    f = lambda s: 2 * (L / (2 * mp.pi)) ** (2 * s) * mp.zeta(2 * s)
    zp0 = mp.diff(f, 0)
    z0 = f(0)
    return mp.e ** (-zp0), zp0, z0


def main() -> int:
    wb = WitnessBuilder("alpha-em-permode-weight", engine="mpmath")
    print("=" * 78)
    print(" α_EM 1/π per-mode weight — where it can (and cannot) come from")
    print("=" * 78)

    # ---- 1. flat-torus per-mode determinant = L² (no bare 1/π) ----
    print("\n[1] flat-torus per-mode ζ-determinant det'(−∂²)_{S¹}(L) = L² "
          "(scale-dependent, NO 1/π):")
    worst = mp.mpf(0)
    z0_worst = mp.mpf(0)
    rows = {}
    for L in ("1", "2", "3.14159265", "6.28318531"):
        d, zp, z0 = detprime_S1(L)
        err = abs(d - mp.mpf(L) ** 2)
        worst = max(worst, err)
        z0_worst = max(z0_worst, abs(z0 + 1))
        rows[L] = float(d)
        print(f"    L={L:>12}: det' = {mp.nstr(d,10):>14}  L² = {mp.nstr(mp.mpf(L)**2,10):>14}  "
              f"ζ_{{S¹}}(0) = {mp.nstr(z0,4)}")
    print(f"    ⇒ det' = L² to {float(worst):.1e}; the 2π cancels — no bare 1/π "
          f"(fitting-trap route RULED OUT)")
    wb.add_assertion("flat_permode_det_is_L_squared_no_pi", computed=float(worst),
                     expected=0.0, tolerance=1e-20,
                     source="det'(−∂²)_{S¹}(L)=L² exactly (ζ'(0)=−2lnL; the 2π "
                            "cancels) — scale-dependent, no bare 1/π: the naive "
                            "per-mode-weight route is the μ-absorbable fitting trap")
    wb.add_assertion("flat_permode_zeta0_is_minus_one", computed=float(z0_worst),
                     expected=0.0, tolerance=1e-25,
                     source="ζ_{S¹}(0)=2ζ_R(0)=−1 (consistency with the b₁-count lead)")

    # ---- 2. template π is Gauss–Bonnet 2πχ (topological) ----
    area = -2 * mp.pi * CHI
    print(f"\n[2] proved 1/(12π) template — the π is Gauss–Bonnet 2πχ:")
    print(f"    Area = −2πχ = 4π(g−1) = {mp.nstr(area,8)} = 12π  ({-2*CHI==12})")
    id1 = abs(mp.mpf(2) / (3 * mp.pi) - B1 / area)
    print(f"    2/(3π) = 8/(12π) = b₁/Area : {mp.nstr(mp.mpf(2)/(3*mp.pi),8)} "
          f"= {mp.nstr(B1/area,8)}  (Δ={float(id1):.1e})")
    wb.add_assertion("template_pi_is_gauss_bonnet_2pichi",
                     computed=float(id1), expected=0.0, tolerance=1e-25,
                     source="2/(3π)=8/(12π)=b₁/Area with Area=−2πχ=12π (g=4): the "
                            "template's π is the Euler-characteristic 2π")

    # ---- 3. loop measure 1/(8π)=1/(πb₁)=1/(2πg): needs a 2πg (genus) source ----
    lm = 1 / (8 * mp.pi)
    id2 = max(abs(lm - 1 / (mp.pi * B1)), abs(lm - 1 / (2 * mp.pi * G)))
    print(f"\n[3] loop measure 1/(8π) = 1/(π·b₁) = 1/(2π·g):")
    print(f"    {mp.nstr(lm,8)} = {mp.nstr(1/(mp.pi*B1),8)} = {mp.nstr(1/(2*mp.pi*G),8)}  "
          f"(Δ={float(id2):.1e})")
    print(f"    ⇒ its π needs a 2π·g (GENUS) source, DISTINCT from the template's "
          f"2π·χ = 4π(g−1) (Euler-char).")
    wb.add_assertion("loop_measure_is_one_over_2pi_g",
                     computed=float(id2), expected=0.0, tolerance=1e-25,
                     source="1/(8π)=1/(π·b₁)=1/(2π·g) at g=4 — a genus (2πg) source, "
                            "not the template's Euler-char (2πχ) area")

    # ---- verdict ----
    verdict = (
        "The 1/π per-mode weight is NOT derivable from the flat ζ-determinant: "
        "det'(−∂²)_{S¹}(L)=L² exactly (the 2π cancels), scale-dependent and "
        "μ-absorbable — the naive per-mode-weight route is the spec-§3 fitting "
        "trap, RULED OUT (scope-(a)). A μ-independent 1/π must be topological. "
        "The proved 1/(12π) template's π IS topological — Gauss–Bonnet 2πχ (Area="
        "12π) — but the loop measure is 1/(8π)=1/(2π·g), whose π needs a GENUS "
        "(2πg) source, DISTINCT from the template's Euler-char (2πχ). So 1/(8π) "
        "is not the same geometric identity as 2/(3π); it does not close by "
        "ζ-determinant bookkeeping. The framework's canonical μ-independent π is "
        "the archimedean dilogarithm regulator (Bloch–Suslin pentagon-uniqueness "
        "→ Bloch–Wigner D; conj:dilogarithm-archimedean-limit). CONCLUSION: "
        "closing 1/(8π) reduces to that named open conjecture PLUS an explicit "
        "2π·g (genus) identity on Bring's surface — the b₁ count (PR #3831) is "
        "topological, but the 1/π per-mode weight is not forced by the "
        "ζ-determinant alone. No fit; nothing wired; not reverse-engineered to 8π.")
    print(f"\n VERDICT: {verdict}")

    wb.set_description(
        "α_EM 1/π per-mode weight localization (follow-up to the ζ_Λ(0)=−b₁ lead, "
        "PR #3831). Machine-verified: (1) the flat-torus per-mode ζ-determinant "
        "det'(−∂²)_{S¹}(L)=L² (no bare 1/π; the fitting-trap route ruled out, "
        "scope-(a)); (2) the proved 1/(12π) template's π is Gauss–Bonnet 2πχ "
        "(Area=12π, 2/(3π)=b₁/Area); (3) the loop measure 1/(8π)=1/(π·b₁)=1/(2π·g) "
        "needs a GENUS (2πg) source, distinct from the template's Euler-char (2πχ). "
        "Conclusion: the 1/π is not forced by the ζ-determinant; it reduces to the "
        "open conj:dilogarithm-archimedean-limit (Bloch–Suslin archimedean π) plus "
        "an explicit 2πg identity on Bring. No fit; nothing wired; not "
        "reverse-engineered to 8π.")
    wb.add_data("flat_permode_det_by_L", rows)
    wb.add_data("area_gauss_bonnet_12pi", float(area))
    wb.add_data("template_pi_source", "Gauss-Bonnet 2πχ (Euler characteristic)")
    wb.add_data("loop_measure_pi_source", "2πg (genus) — distinct from 2πχ")
    wb.add_data("reduces_to_open_conjecture", "conj:dilogarithm-archimedean-limit "
                "(Bloch-Suslin archimedean π) + explicit 2πg identity on Bring")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\n witness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
