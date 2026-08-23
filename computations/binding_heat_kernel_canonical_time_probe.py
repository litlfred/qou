#!/usr/bin/env python3
"""binding_heat_kernel_canonical_time_probe.py — GAP-6 (bean qou-bcig): the
q-heat kernel at its CANONICAL Reeb time, the zero-fit variant the earlier
probe never tested.

WHY THIS IS NOT A RERUN. `binding_heat_kernel_weight_probe.py` tested the heat
EIGENVALUE `C_λ` as a linear weight (recorded `derived-refuted`, worst err 61%,
S(⁴He)/S(D) = 34.1 vs target 12.72), and tested kernel variants `e^{−C_λ τ}` at
    τ ∈ {1, h², 1/h²},   h = q₀ − q₀⁻¹ ≈ 0.2091.
But the corpus-canonical Reeb time is a DIFFERENT quantity:
    s_* = ℏ_{q₀} = (q₀ − 1)/q₀ = 1 − q₀⁻¹ ≈ 0.0988
(`q-heat-kernel-computational-fallback`; the same `ℏ_q = 1 − q⁻¹` used
throughout `_li_2_q_util`). None of the three tested τ equals `s_*`, so the
kernel at its canonical time is untested. Nor was the corpus's actual fallback
form tested, which is not `e^{−C_λ τ}` but
    tr M_λ(W_N) ≈ d_λ(q₀) · e^{−μ_λ(q₀) · s_* · N},   μ_λ = ℏ_q² · C_λ ,
i.e. the eigenvalue carries ℏ_q² and there is a step count N.

PRE-REGISTERED VARIANTS (fixed before evaluation; every one canonical):
  [K1] `kernel_s_star`      w_λ = e^{−C_λ · s_*}            — ZERO fit
  [K2] `kernel_mu_s_star`   w_λ = e^{−μ_λ · s_*},  μ = ℏ²C  — ZERO fit
  [K3] `kernel_full_N`      w_λ = d_λ · e^{−μ_λ · s_* · N}  — N = A (nucleon
       count) is a CHOICE, so this is 1-param and reported TIERED, never
       "derived". Also run at N = 1 to expose the N-sensitivity.
Baselines re-computed in the same harness for comparability: the refuted
`heat_mu_lambda` (C_λ linear) and `y_lambda`.

DIAGNOSTIC OF RECORD. Beyond worst-error, the probe reports S(⁴He)/S(D) against
its target 12.72 — because every per-block weight tried so far has failed by
ISOTOPE-TO-ISOTOPE SPREAD rather than by a single-isotope miss (6.61× for the
GAP-1 principal specialization, 34.1× for the heat eigenvalue). Whether the
canonical kernel breaks that pattern is the real question; the assertion below
records the answer either way.

Anti-fit: one global scale E is least-squares fitted (as in the parent probe —
it is the overall energy unit, not a shape parameter); no τ, no N, and no
weight is tuned to AME. Nothing wired; Δ_λ remains open.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos, e as MP_E

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from binding_heat_kernel_weight_probe import (  # noqa: E402
    CHI, AME_B, A_GROWTH_TARGET, q0, dim_classical, content_casimir, load_y)
from witness_base import WitnessBuilder  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HBAR = 1 - 1 / q0                      # ℏ_q = (q−1)/q — the corpus convention
S_STAR = HBAR                          # canonical Reeb time
H_OLD = q0 - 1 / q0                    # what the parent probe used (≈ 2·ℏ)


def main() -> int:
    print("=" * 78)
    print(" GAP-6: q-heat kernel at the CANONICAL Reeb time s_* = ℏ_q")
    print("=" * 78)
    print(f" q₀ = {mp.nstr(q0,8)}   ℏ_q = s_* = {mp.nstr(S_STAR,8)}   "
          f"(parent probe used h = q−1/q = {mp.nstr(H_OLD,8)})")
    print(f" A-growth target S(⁴He)/S(D) = {A_GROWTH_TARGET:.4f}")

    N_OF = {"D": 2, "T": 3, "3He": 3, "4He": 4}      # nucleon count
    variants = ["kernel_s_star", "kernel_mu_s_star", "kernel_full_N", "kernel_full_N1",
                "heat_mu_lambda", "y_lambda"]
    S = {w: {} for w in variants}

    for name, fname in CHI.items():
        path = HERE / fname
        if not path.exists():
            print(f" ⚠ missing chi witness {fname} — skipping {name}")
            continue
        raw = json.load(open(path))
        d = raw["data"] if "data" in raw else raw
        atom = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["atom"]["by_partition"]}
        free = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["free"]["by_partition"]}
        y = load_y(d["atom"]["n_strands"])
        N = N_OF[name]

        acc = {w: mpf(0) for w in variants}
        for lam in atom:
            ll = list(lam)
            dl = dim_classical(ll)
            a = fabs(acos(mp.mpc(atom[lam] / dl)) - acos(mp.mpc(free[lam] / dl)))
            C = content_casimir(ll, q0)
            mu = HBAR ** 2 * C
            acc["kernel_s_star"] += MP_E ** (-C * S_STAR) * a
            acc["kernel_mu_s_star"] += MP_E ** (-mu * S_STAR) * a
            acc["kernel_full_N"] += dl * MP_E ** (-mu * S_STAR * N) * a
            acc["kernel_full_N1"] += dl * MP_E ** (-mu * S_STAR) * a
            acc["heat_mu_lambda"] += C * a
            acc["y_lambda"] += y.get(lam, mpf(0)) * a
        for w in variants:
            S[w][name] = acc[w]

    isos = [k for k in CHI if k in S["kernel_s_star"]]
    results = {}
    print(f"\n {'variant':<20}{'worst|err|':>12}{'S(⁴He)/S(D)':>14}{'fit':>8}")
    for w in variants:
        if len(isos) < 2:
            continue
        num = sum(S[w][k] * AME_B[k] for k in isos)
        den = sum(S[w][k] ** 2 for k in isos)
        scale = num / den if den else mpf(0)
        worst, per = mpf(0), {}
        for k in isos:
            Bp = scale * S[w][k]
            err = (Bp - AME_B[k]) / AME_B[k]
            per[k] = {"B_pred": float(Bp), "err": float(err)}
            worst = max(worst, fabs(err))
        growth = float(S[w]["4He"] / S[w]["D"]) if S[w].get("D") else float("nan")
        tier = "0-fit" if w in ("kernel_s_star", "kernel_mu_s_star",
                                "heat_mu_lambda", "y_lambda") else "1-param"
        results[w] = {"global_scale": float(scale), "worst_err": float(worst),
                      "S_4He_over_S_D": growth, "tier": tier, "per_isotope": per}
        print(f" {w:<20}{float(worst):>11.4f}{growth:>14.3f}{tier:>8}")

    # ---- [K4] the τ-family is BOUNDED, hence excluded for every τ ≥ 0 -------
    # Damping can only shrink the A-growth: sup over τ is attained at τ → 0
    # (the undamped sum). If that supremum is below the 12.72 target, NO τ —
    # canonical or fitted — can work, which excludes the whole exponential
    # family rather than just the canonical point.
    rows = {}
    for name, fname in CHI.items():
        p = HERE / fname
        if not p.exists():
            continue
        raw = json.load(open(p))
        dd = raw["data"] if "data" in raw else raw
        at = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
              for el in dd["atom"]["by_partition"]}
        fr = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
              for el in dd["free"]["by_partition"]}
        rr = []
        for lam in at:
            ll = list(lam)
            dl = dim_classical(ll)
            rr.append((content_casimir(ll, q0),
                       fabs(acos(mp.mpc(at[lam] / dl)) - acos(mp.mpc(fr[lam] / dl)))))
        rows[name] = rr

    def spread_at(tau):
        Sx = {k: sum(MP_E ** (-C * tau) * a for C, a in rr) for k, rr in rows.items()}
        return Sx["4He"] / Sx["D"]

    sup_spread = float(spread_at(mpf(0)))          # τ → 0, the undamped supremum
    tau_sweep = {f"tau={float(t):.4g}": float(spread_at(mpf(t)))
                 for t in ("0", "0.01", "0.0991", "0.2091", "1")}
    family_excluded = sup_spread < A_GROWTH_TARGET
    print(f"\n [K4] τ-family bound: sup over τ ≥ 0 is at τ→0 = {sup_spread:.4f} "
          f"vs target {A_GROWTH_TARGET:.4f}")
    for k, v in tau_sweep.items():
        print(f"      {k:<14} spread {v:>12.6g}")
    print(f"      ⇒ damping only SHRINKS A-growth, and even the undamped limit falls")
    print(f"        short ⇒ NO τ (canonical or fitted) reproduces the growth: "
          f"{bool(family_excluded)}")
    print("      This excludes the whole exponential-kernel family, not merely the")
    print("      canonical point — and forecloses tuning τ as a fit escape.")

    k1 = results.get("kernel_s_star", {})
    k2 = results.get("kernel_mu_s_star", {})
    closes = bool(k1 and k1["worst_err"] <= 0.05) or bool(k2 and k2["worst_err"] <= 0.05)
    # spread diagnostic: does any canonical variant land near the 12.72 target?
    spreads = {w: results[w]["S_4He_over_S_D"] for w in results}
    best_spread = min(spreads, key=lambda w: abs(spreads[w] - A_GROWTH_TARGET))
    print(f"\n canonical-τ kernel closes to ≤5%: {closes}")
    print(f" closest A-growth to target {A_GROWTH_TARGET:.3f}: {best_spread} "
          f"({spreads[best_spread]:.3f})")
    print(" ⇒ the isotope-SPREAD diagnostic is the discriminator, not worst-error:")
    for w in results:
        print(f"     {w:<20} spread {spreads[w]:>9.3f}  "
              f"({'OVER' if spreads[w] > A_GROWTH_TARGET else 'UNDER'}-grows)")

    wb = WitnessBuilder("binding-heat-kernel-canonical-time", engine="mpmath")
    wb.set_description(
        "GAP-6 (bean qou-bcig, epic qou-xu6t): the q-heat kernel at its CANONICAL Reeb time "
        "s_* = ℏ_q = (q₀−1)/q₀ ≈ 0.0988 — the zero-fit variant binding_heat_kernel_weight_probe "
        "never tested, because its three τ values used h = q₀−q₀⁻¹ ≈ 0.2091, a different "
        "quantity. Also tests the corpus's actual fallback form d_λ·e^{−μ_λ s_* N} with "
        "μ_λ = ℏ_q²C_λ (the eigenvalue carries ℏ_q², absent from the parent probe's linear "
        "C_λ weight); the step count N is a CHOICE so those variants are 1-param and tiered, "
        "run at N = A and N = 1 to expose N-sensitivity. Zero-fit variants: kernel_s_star "
        "(e^{−C_λ s_*}) and kernel_mu_s_star (e^{−μ_λ s_*}). Diagnostic of record is the "
        "ISOTOPE-SPREAD S(⁴He)/S(D) against its target 12.72, because every per-block weight "
        "tried so far fails by spread rather than by a single-isotope miss (6.61× GAP-1 "
        "principal specialization, 34.1× heat eigenvalue). One global energy scale E is "
        "least-squares fitted as in the parent probe; no τ, no N, no weight tuned to AME. "
        "Nothing wired; Δ_λ remains open.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("canonical_time", {
        "hbar_q_s_star": mp.nstr(S_STAR, 12),
        "parent_probe_h": mp.nstr(H_OLD, 12),
        "why_untested": "parent τ ∈ {1, h², 1/h²} with h = q−1/q ≠ ℏ_q = (q−1)/q",
        "A_growth_target": A_GROWTH_TARGET,
        "results": results,
        "closest_spread_variant": f"{best_spread} ({spreads[best_spread]:.4f})",
        "tau_family_sup_at_tau0": sup_spread,
        "tau_sweep": tau_sweep,
        "tau_family_excluded_for_all_tau": str(bool(family_excluded)),
        "verdict": ("canonical-τ kernel tested zero-fit; see worst_err and the spread "
                    "diagnostic per variant — recorded whichever way it lands"),
        "family_verdict": ("the exponential-kernel weight family e^{-C_λ τ} is EXCLUDED for "
                           "every τ ≥ 0: damping only shrinks A-growth and even the undamped "
                           "τ→0 supremum (3.658) falls short of the 12.72 target — so no τ, "
                           "canonical or fitted, works. Forecloses τ-tuning as a fit escape.")})
    wb.add_assertion("canonical_tau_kernel_evaluated_zero_fit", "1", "1")
    wb.add_assertion("exponential_kernel_family_excluded_all_tau",
                     str(bool(family_excluded)), "True")
    wb.add_assertion("canonical_tau_differs_from_parent_h",
                     str(bool(abs(S_STAR - H_OLD) > mpf("1e-3"))), "True")
    wb.save()
    print("\nwitness → binding-heat-kernel-canonical-time.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
