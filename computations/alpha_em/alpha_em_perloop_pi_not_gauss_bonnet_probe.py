#!/usr/bin/env python3
"""alpha_em_perloop_pi_not_gauss_bonnet_probe.py

Does the π in the α_EM per-loop 1/(8π) come from Gauss–Bonnet (the surface's
Euler / area) rather than the flat 2-D heat kernel (#3909)? This probe tests
that hypothesis against the polarized-determinant value on Jac(Bring) and
against Bring's genuine Gauss–Bonnet invariants.

SETUP. The polarized (holomorphic, factorized) determinant measure on
Jac(Bring)=E_5τ₀³×E_τ₀ is 8.2263 (probe alpha_em_polarized_determinant_removes_
blowup_probe.py, #4064): O(1), nearest simple candidate b₁=8 (2.8% off), NOT 8π.
The open question is which geometric object supplies the π in the per-loop 1/(8π).

GAUSS–BONNET FACTS (hyperbolic uniformization, K=−1). For a genus-g surface,
χ = 2−2g, the GB Euler number is −χ = 2g−2, the GB area is −2πχ = 2π(2g−2):
  g=3 → −χ=4, area=8π ;  g=4 (Bring) → −χ=6, area=12π ;  g=5 → −χ=8, area=16π.
So `8π` is the GB area only at genus 5 (and `8`=−χ only at genus 5). Bring is
genus 4: its GB invariants are 6 and 12π.

FINDINGS (both negative for the Gauss–Bonnet hypothesis).
  1. THE "8" IS HOMOLOGICAL, NOT GAUSS–BONNET. The settled count (#3896) is
     b₁ = 2g = 8. Bring's Gauss–Bonnet Euler number is −χ = 2g−2 = 6 ≠ 8. So the
     "8" in 8π is the first Betti number, not the Euler characteristic.
  2. THE π IS NOT A GB AREA. The polarized determinant measure 8.2263 matches no
     Gauss–Bonnet invariant of Bring: measure/12π=0.218, measure/6=1.371,
     measure/(−χ·π)=measure/6π=0.436. It is π-free, sitting at b₁=8 (2.8% off).
     The Polyakov/conformal-anomaly π (∫R=4πχ, χ=−6) is divided out by holomorphic
     factorization — the polarized object carries no anomaly π.

CONCLUSION. The α_EM per-loop 8π splits as (count b₁=8) × (flat heat-kernel π,
#3909), NOT as a single Gauss–Bonnet area (which would be 12π for Bring) and NOT
with an Euler-number count (which would be 6). Gauss–Bonnet is the wrong origin
for both factors at Bring's genus. The residual 2.8% (8.2263 vs 8) is not a
χ-correction and remains for the q-holomorphic (Φ_b) deformation.

DISCIPLINE: scope-(a). Tests + rejects the Gauss–Bonnet attribution on the
numbers; keeps the homological-count × heat-kernel split. No 8π manufactured; no
fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40
MEAS = mp.mpf("8.22628522198")   # polarized measure (from #4064)
G = 4                            # Bring genus


def gb_invariants(g):
    chi = 2 - 2 * g
    return {"chi": chi, "euler_neg_chi": -chi, "b1_2g": 2 * g,
            "gb_area": -2 * mp.pi * chi}


def main() -> int:
    pi = mp.pi
    inv = gb_invariants(G)
    phi2 = ((1 + mp.sqrt(5)) / 2) ** 2

    print(f"  Bring genus g={G}:  b1=2g={inv['b1_2g']},  -chi=2g-2={inv['euler_neg_chi']},  "
          f"GB area=-2pi*chi={mp.nstr(inv['gb_area'],8)} (=6pi)", flush=True)
    print(f"  polarized measure = {mp.nstr(MEAS,10)}", flush=True)
    cands = {
        "8 (b1)": mp.mpf(8), "8pi": 8 * pi, "6 (-chi)": mp.mpf(6),
        "6pi (-chi*pi)": 6 * pi, "12pi (GB area)": 12 * pi, "pi*phi^2": pi * phi2,
    }
    for k, v in cands.items():
        print(f"    measure/({k}) = {mp.nstr(MEAS / v, 7)}", flush=True)

    # (1) the "8" is b1=2g, NOT the GB Euler number -chi=2g-2
    eight_is_b1_not_euler = (inv["b1_2g"] == 8) and (inv["euler_neg_chi"] == 6)
    # (2) measure matches no GB invariant (all >5% off a clean ratio)
    r_gbarea = MEAS / (12 * pi)
    r_euler = MEAS / mp.mpf(6)
    r_eulerpi = MEAS / (6 * pi)
    not_gb_area = abs(r_gbarea - round(float(r_gbarea))) > mp.mpf("0.05")
    not_euler = abs(r_euler - round(float(r_euler))) > mp.mpf("0.05")
    not_eulerpi = abs(r_eulerpi - round(float(r_eulerpi))) > mp.mpf("0.05")
    # (3) still sits at b1=8, 2.8% off (the homological count survives)
    at_b1 = abs(MEAS / 8 - 1) < mp.mpf("0.05") and abs(MEAS / 8 - 1) > mp.mpf("0.005")
    # (4) pi*phi^2 near-hit is a coincidence, not an identity (>1e-4)
    phi_coincidence = abs(MEAS / (pi * phi2) - 1) > mp.mpf("1e-4")

    assertions = [
        ("eight_is_b1_not_gauss_bonnet_euler", bool(eight_is_b1_not_euler)),
        ("measure_not_gb_area_12pi", bool(not_gb_area)),
        ("measure_not_euler_6", bool(not_euler)),
        ("measure_not_euler_times_pi_6pi", bool(not_eulerpi)),
        ("measure_still_at_b1_2p8pct", bool(at_b1)),
        ("pi_phi2_is_coincidence_not_identity", bool(phi_coincidence)),
    ]

    verdict = (
        f"THE α_EM PER-LOOP 8π IS NOT GAUSS–BONNET (scope-(a)). Bring is genus 4: its "
        f"Gauss–Bonnet invariants are −χ=2g−2=6 and area=−2πχ=12π. The per-loop constant "
        f"is 8 / 8π — neither the Euler number 6 nor the area 12π (8π is the GB area only at "
        f"genus 5). (1) The '8' is the homological b₁=2g=8 (#3896), NOT the GB Euler number "
        f"−χ=6. (2) The polarized determinant measure {mp.nstr(MEAS,7)} matches no GB "
        f"invariant of Bring: measure/12π={mp.nstr(r_gbarea,5)}, measure/6={mp.nstr(r_euler,5)}, "
        f"measure/6π={mp.nstr(r_eulerpi,5)}; it is π-free, at b₁=8 (2.8% off). The "
        f"Polyakov/conformal-anomaly π (∫R=4πχ) is divided out by holomorphic factorization. "
        f"So 8π splits as (count b₁=8)×(flat heat-kernel π, #3909), not a single GB area. The "
        f"π·φ²={mp.nstr(MEAS/(pi*phi2),8)} near-hit (0.018%) is a coincidence (Bring A₅/golden "
        f"symmetry is tempting but the digits kill it), not an identity. Residual 2.8% remains "
        f"for the q-holomorphic Φ_b deformation. No 8π manufactured; no fit; no c_k; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("alpha-em-perloop-pi-not-gauss-bonnet", engine="mpmath")
    wb.set_description(
        "α_EM per-loop 8π is NOT Gauss–Bonnet: Bring (g=4) has −χ=6, GB area=12π, but the "
        "constant is 8/8π (=GB only at g=5). The '8' is homological b₁=2g (#3896) not the Euler "
        "number −χ=6; the polarized determinant measure 8.226 is π-free (at b₁=8, 2.8% off), "
        "matching no GB invariant. 8π = (count b₁=8)×(heat-kernel π, #3909), not a GB area.")
    wb.set_audit_only("docs/audits/2026-07-19-alpha-em-perloop-pi-not-gauss-bonnet.md")
    for name, passed in assertions:
        wb.add_assertion(name, str(passed), "True")
    wb.add_data("polarized_measure", mp.nstr(MEAS, 15))
    wb.add_data("bring_genus", str(G))
    wb.add_data("bring_euler_neg_chi", str(inv["euler_neg_chi"]))
    wb.add_data("bring_b1_2g", str(inv["b1_2g"]))
    wb.add_data("bring_gb_area_over_pi", "12")
    wb.add_data("measure_over_gb_area_12pi", mp.nstr(r_gbarea, 10))
    wb.add_data("measure_over_euler_6", mp.nstr(r_euler, 10))
    wb.add_data("measure_over_pi_phi2", mp.nstr(MEAS / (pi * phi2), 12))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all(p for _, p in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
