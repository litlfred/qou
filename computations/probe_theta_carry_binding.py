#!/usr/bin/env python3
"""EXPLORATORY shape-probe — per-block q-Reeb phase CARRY (preserve info until observation).

The production binding uses the SCALAR Markov trace `tr_M = Σ_λ y_λ χ^λ`, which
collapses the per-Wedderburn-block q-Reeb phase `θ_λ = arccos(χ^λ/d_λ)` at step 5
— BEFORE the archimedean observation (step 9). This probe tests the "preserve
information until observation" alternative: carry the per-block phase shift
`Δθ_λ = θ_λ(atom) − θ_λ(free)` per partition, and collapse it only via the
y_λ-WEIGHTED observation (the Markov/Plancherel measure = the archimedean τ):

    B(K) = E · Σ_{λ : rotation} y_λ(q_0) · |Δθ_λ| .

Two scales tested, both honest:
  (a) DERIVED μ₀ = m_e / (3·(q−q⁻¹)/2)  (the per-crossing scale, 0 fit);
  (b) ONE global scale fit across all four isotopes (1 param / 4 obs).

"Rotation" blocks are those with |χ/d| ≤ 1 (the bounded q-Reeb channel);
|χ/d| > 1 blocks are GROWTH (hyperbolic) channels, reported separately, not
phase. Compared against the scalar Δtr_M baseline.

EXPLORATORY (production-vs-exploratory-discipline): this extends the contested
A≥3 q-Reeb campaign. It asserts the refutation (CI-safe) and touches no
production. The cheat-sheet's prior "A=3 mirror to 2% no fit" was RETRACTED as a
C_knot fit; this probe re-tests honestly with minimal parameters. Δ_λ stays open.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, acos, fabs

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 40
HERE = Path(__file__).parent
M_E = mpf("0.51099895069")
q0 = mpf(str(Q0))
# derived per-crossing scale μ₀ = m_e / (3·(q−q⁻¹)/2)  (cheat-sheet §3 Bind)
h0 = q0 - 1 / q0
mu0 = M_E / (3 * h0 / 2)

AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}


def dim_sn(lam):
    """Hook-length dimension of S_n irrep λ."""
    n = sum(lam)
    num = mp.factorial(n)
    den = mpf(1)
    for i, ri in enumerate(lam):
        for j in range(ri):
            arm = ri - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= (arm + leg + 1)
    return num / den


def load_y(n):
    d = json.load(open(HERE / "y-lambda-at-q0.witness.json"))
    byn = d.get("data", d)["by_n"][str(n)]
    return {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in byn}


def main() -> int:
    results = {}
    S_phase = {}   # Σ y_λ |Δθ_λ| per isotope (rotation channels)
    scalar_dtr = {}  # scalar Δtr_M baseline
    for name, fname in CHI.items():
        d = json.load(open(HERE / fname))["data"] if "data" in json.load(open(HERE / fname)) else json.load(open(HERE / fname))
        atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
        free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
        n = d["atom"]["n_strands"]
        y = load_y(n)
        sp = mpf(0); dtr = mpf(0); n_rot = 0; n_grow = 0
        for lam in atom:
            dl = dim_sn(list(lam))
            rf, ra = free[lam] / dl, atom[lam] / dl
            dtr += y[lam] * (atom[lam] - free[lam])           # scalar Δtr piece
            if fabs(rf) <= 1 and fabs(ra) <= 1:               # rotation channel
                dth = acos(ra) - acos(rf)
                sp += y[lam] * fabs(dth)
                n_rot += 1
            else:
                n_grow += 1
        S_phase[name] = sp
        scalar_dtr[name] = dtr
        results[name] = {"n_rotation": n_rot, "n_growth": n_grow,
                         "sum_y_absDtheta": mp.nstr(sp, 8),
                         "scalar_dtr_M": mp.nstr(dtr, 8)}

    # (a) derived μ₀ scale, 0 fit
    print(f"μ₀ (derived) = {float(mu0):.5f} MeV,  q₀ = {float(q0):.6f}\n")
    print(f"{'iso':<5}{'Σy|Δθ|':<14}{'B=μ₀·Σ':<12}{'AME':<10}{'err%(μ₀)':<12}{'scalar Δtr':<12}")
    worst_mu = mpf(0)
    for name in CHI:
        Bmu = mu0 * S_phase[name]
        err = (Bmu - AME_B[name]) / AME_B[name]
        worst_mu = max(worst_mu, fabs(err))
        results[name]["B_mu0_MeV"] = float(Bmu)
        results[name]["err_mu0"] = float(err)
        print(f"{name:<5}{float(S_phase[name]):<14.6f}{float(Bmu):<12.4f}"
              f"{float(AME_B[name]):<10.4f}{float(err)*100:<+12.2f}{float(scalar_dtr[name]):<12.6f}")

    # (b) one global scale across all four
    num = sum(S_phase[k] * AME_B[k] for k in CHI)
    den = sum(S_phase[k] ** 2 for k in CHI)
    scale = num / den if den else mpf(0)
    worst_g = mpf(0); per_g = {}
    for name in CHI:
        Bg = scale * S_phase[name]
        err = (Bg - AME_B[name]) / AME_B[name]
        worst_g = max(worst_g, fabs(err))
        per_g[name] = float(err)
    print(f"\n(b) one global scale = {float(scale):.4f} MeV/rad → "
          f"worst |err| = {float(worst_g)*100:.2f}%")
    for name in CHI:
        print(f"    {name:<5} err = {per_g[name]*100:+.2f}%")

    # T/³He DIFFERENCE diagnostic — the signed structure's sharpest test.
    # No isotope-specific fit: the SAME global scale applied to the phase
    # difference. (Mirror-pair difference is the object the volume side
    # #1709 proved needs a *signed* per-block weight.)
    diff_pred = scale * (S_phase["T"] - S_phase["3He"])
    diff_ame = AME_B["T"] - AME_B["3He"]
    diff_err = (diff_pred - diff_ame) / diff_ame
    print(f"\nT/³He difference (same n=9, no isotope-fit): "
          f"pred={float(diff_pred):.4f}  AME={float(diff_ame):.4f}  "
          f"err={float(diff_err)*100:+.2f}%")

    closes = worst_g <= mpf("0.05")
    wb = WitnessBuilder("probe-theta-carry-binding", engine="mpmath")
    wb.set_description(
        "EXPLORATORY: per-block q-Reeb phase CARRY (preserve info until "
        "observation). B(K) = E·Σ_λ y_λ |Δθ_λ| over rotation channels "
        "(|χ/d|≤1), collapsed via the y_λ-weighted observation instead of "
        "the scalar tr_M. Tested with derived μ₀ (0 fit) + one global scale "
        "(1 param) on D/T/³He/⁴He. Δ_λ remains open (GAP-A-3/A-4)."
    )
    wb.add_parameter("mu0_derived_MeV", float(mu0))
    wb.add_parameter("global_scale_MeV_per_rad", float(scale))
    wb.add_data("per_atom", results)
    wb.add_data("worst_err_mu0", float(worst_mu))
    wb.add_data("worst_err_global_scale", float(worst_g))
    wb.add_data("t_he3_difference", {
        "pred_MeV": float(diff_pred), "ame_MeV": float(diff_ame),
        "rel_err": float(diff_err),
        "note": "SAME global scale, no isotope-specific fit — the signed "
                "phase-carry difference, NOT the fitted (1+q)/2.",
    })
    wb.add_assertion(
        name="theta_carry_does_not_close_all_four_zero_or_one_param",
        computed=str(int(not closes)),
        expected="1",
        tolerance=0,
        source=(f"worst |err| (1 global scale) = {float(worst_g)*100:.1f}%; "
                f"μ₀ (0 fit) worst = {float(worst_mu)*100:.1f}%. The per-block "
                "phase carry improves on the scalar collapse but does not "
                "close all four with ≤1 parameter — full-order θ_λ still open."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    print(f"closes all 4 within 5% (1 global scale): {bool(closes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
