#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath evaluation at q0; no symbolic-q polynomial output.
"""ρ-FREE A=3 mirror binding-RATIO prediction from the q-Reeb phase (lever 3).

The q-Reeb phase binding model is `B(K) = ρ · S(K)`, where
`S(K) = Σ_λ y_λ dim_λ |Δθ_λ(K)|` is the Markov-weighted free→bound rotation-phase
sum (substrate-only: χ_λ braid characters, y_λ Wenzl weights, θ_λ = arccos(χ/dim))
and ρ is a single energy-per-radian scale.

**The key observation (this probe).** The ABSOLUTE binding needs ρ, and ρ ≈ 18.5
MeV/rad is currently a *fitted* normalisation (`ρ_need = B_AME/S`, CAL-4-gated —
see `2026-06-22-charge-slambda-reeb-phase-crack.md`). But the A=3 mirror **RATIO**

    B(³H) / B(³He)  =  [ρ·S(³H)] / [ρ·S(³He)]  =  S(³H) / S(³He)

is **ρ-INDEPENDENT** — ρ cancels. So the ratio is a *genuine substrate prediction*
with **no fit and no free parameter**, unlike the absolute scale. This probe makes
that prediction explicit and witnessed: compute `S(³H)/S(³He)` (substrate-only) and
compare to the AME ratio `B_AME(³H)/B_AME(³He)`.

**Scope (honest).** This does NOT close lever 3. The ABSOLUTE scale ρ remains
fitted / CAL-4-gated, and deriving a *per-λ* ρ_λ from one total binding is exactly
the underdetermined Δ_λ gate (six ansätze failed). What is established here: the
1.7% A=3 result is a ρ-free PREDICTION (not post-hoc), cleanly separated from the
gated absolute scale.

Output: binding-reeb-ratio-rho-free.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, acos

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_TRITIUM_MEV_VALIDATION as B_T_AME,
    AME_B_HE3_MEV_VALIDATION as B_HE3_AME,
)
# Reuse the validated q-Reeb machinery from the lead probe (no reimplementation).
from binding_rotation_phase_lead import load_chi, load_y, dim_sn, clamp  # noqa: E402


def phase_sum(chi_fname: str, ydict) -> mpf:
    """S(K) = Σ_λ y_λ dim_λ |Δθ_λ|  (Markov-weighted q-Reeb phase sum).

    Substrate-only — χ_λ from the braid-character witness, y_λ Wenzl weights,
    θ_λ = arccos(χ_λ/dim_λ). Contains NO B_AME and NO ρ.
    """
    chi_f = load_chi(chi_fname, "free")
    chi_a = load_chi(chi_fname, "atom")
    S = mpf(0)
    for lam in chi_f:
        d = dim_sn(list(lam))
        if fabs(chi_f[lam] / d) > 1 + 1e-14 or fabs(chi_a[lam] / d) > 1 + 1e-14:
            continue  # only rotation blocks (both ends on the unit circle)
        dth = acos(clamp(chi_a[lam] / d)) - acos(clamp(chi_f[lam] / d))
        S += ydict.get(lam, mpf(0)) * d * fabs(dth)
    return S


def main() -> int:
    set_compute_dps()
    y_H9 = load_y("wenzl-y-lambda-h9.witness.json", ["per_partition"])
    S_T = phase_sum("atom-chi-rust-t.witness.json", y_H9)     # ³H  (Z=1,N=2)
    S_He3 = phase_sum("atom-chi-rust-3he.witness.json", y_H9)  # ³He (Z=2,N=1)

    ratio_pred = S_T / S_He3                       # ρ-FREE prediction (ρ cancels)
    ratio_ame = mpf(str(B_T_AME)) / mpf(str(B_HE3_AME))
    rel_err = ratio_pred / ratio_ame - 1

    # The fitted absolute scale, for contrast (uses B_AME — CAL-4-gated).
    rho_T = mpf(str(B_T_AME)) / S_T
    rho_He3 = mpf(str(B_HE3_AME)) / S_He3
    rho_spread = rho_T / rho_He3 - 1

    wb = WitnessBuilder("binding-reeb-ratio-rho-free", engine="mpmath")
    wb.set_description(
        "ρ-FREE A=3 mirror binding-ratio prediction from the q-Reeb phase. "
        "B(K)=ρ·S(K), S=Σ_λ y_λ dim_λ|Δθ_λ| (substrate-only). The RATIO "
        "B(³H)/B(³He)=S(³H)/S(³He) is ρ-INDEPENDENT (ρ cancels) ⇒ a genuine "
        "no-fit prediction: predicted "
        f"{mp.nstr(ratio_pred, 6)} vs AME {mp.nstr(ratio_ame, 6)} "
        f"({mp.nstr(rel_err * 100, 3)}%). The ABSOLUTE scale ρ stays fitted "
        "(CAL-4-gated): ρ_need(³H)="
        f"{mp.nstr(rho_T, 6)}, ρ_need(³He)={mp.nstr(rho_He3, 6)} MeV/rad. "
        "NOT a closure — per-λ ρ_λ from one total binding is the underdetermined "
        "Δ_λ gate."
    )
    wb.add_data("rho_free_ratio", {
        "S_tritium": mp.nstr(S_T, 10),
        "S_he3": mp.nstr(S_He3, 10),
        "ratio_predicted_rho_free": mp.nstr(ratio_pred, 10),
        "ratio_AME": mp.nstr(ratio_ame, 10),
        "rel_err_pct": mp.nstr(rel_err * 100, 4),
        "note": "ratio = S(³H)/S(³He); ρ cancels — no fit, no free parameter",
    })
    wb.add_data("absolute_scale_fitted", {
        "rho_need_tritium_MeV_per_rad": mp.nstr(rho_T, 8),
        "rho_need_he3_MeV_per_rad": mp.nstr(rho_He3, 8),
        "rho_universal_spread_pct": mp.nstr(rho_spread * 100, 4),
        "note": "ρ_need = B_AME/S uses the experimental binding ⇒ CAL-4-gated "
                "(fitted); the ~1.7% spread is the universal-ρ consistency, "
                "not a derivation.",
    })
    # Assertion 1: the ρ-FREE ratio prediction matches AME within 2% (the result).
    wb.add_assertion(
        "rho_free_a3_ratio_within_2pct",
        computed=float(fabs(rel_err)), expected=0.0, tolerance=0.02,
        source=f"|S(³H)/S(³He) / (B_AME(³H)/B_AME(³He)) − 1| = "
               f"{mp.nstr(fabs(rel_err) * 100, 3)}% — ρ-free, no fit.",
    )
    out = wb.save()

    print("=" * 78)
    print(" ρ-FREE A=3 mirror binding RATIO from the q-Reeb phase (ρ cancels)")
    print("=" * 78)
    print(f"   S(³H)  = {mp.nstr(S_T, 8)}   S(³He) = {mp.nstr(S_He3, 8)}  (substrate-only)")
    print(f"   ratio predicted (ρ-free) = {mp.nstr(ratio_pred, 7)}")
    print(f"   ratio AME                = {mp.nstr(ratio_ame, 7)}  ({mp.nstr(B_T_AME,7)}/{mp.nstr(B_HE3_AME,7)})")
    print(f"   rel err                  = {mp.nstr(rel_err * 100, 3)}%   ← genuine no-fit prediction")
    print("-" * 78)
    print(f"   [absolute scale, FITTED]  ρ_need(³H)={float(rho_T):.3f}  "
          f"ρ_need(³He)={float(rho_He3):.3f} MeV/rad  (spread {float(rho_spread)*100:.2f}%)")
    print(f"   ρ is CAL-4-gated; per-λ ρ_λ = the underdetermined Δ_λ gate.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
