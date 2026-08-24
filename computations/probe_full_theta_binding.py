#!/usr/bin/env python3
"""EXPLORATORY shape-probe — FULL-ORDER per-block θ_λ binding (A≥3 absolute).

Follow-up to `probe_theta_carry_binding.py`, which showed the rotation-only
phase |Δθ| (arccos, |χ/d|≤1) is too flat for ABSOLUTE binding (it can't track
the ~13× D→⁴He growth) although it gets the T/³He DIFFERENCE to +8% with no fit.

The diagnosis (binding_reeb_phase_decomposition.py): the binding's EXTENSIVE,
A-dependent part lives in the GROWTH channels (|χ/d|>1), which the rotation-only
probe excluded. This probe carries the FULL-ORDER θ_λ via the COMPLEX arccos:

    θ_λ = arccos(χ^λ/d_λ) ∈ ℂ ,
        real      on rotation channels (|χ/d|≤1)  — the q-Reeb phase,
        imaginary on growth   channels (|χ/d|>1)  — the hyperbolic/volume part
                                                     (|Im arccos(r)| = arccosh|r|).

This is the fibre-vs-observable cut at the per-block level: Re θ = phase
(observable-real), Im θ = growth (the exp(Vol) extensive piece). We test which
component, Markov-weighted, reproduces ABSOLUTE binding for D/T/³He/⁴He:

    B(K) = E · Σ_λ y_λ(q_0) · |Δθ_λ^{component}| ,  Δθ_λ = θ_λ(atom) − θ_λ(free).

EXPLORATORY (production-vs-exploratory-discipline): asserts the refutation
(CI-safe), no production touch. Δ_λ / A≥3-absolute remains an open gate; this
probe reports whether the full-order (incl. growth) phase closes it.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos, re as mp_re, im as mp_im

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
M_E = mpf("0.51099895069")
q0 = mpf(str(Q0))
h0 = q0 - 1 / q0
mu0 = M_E / (3 * h0 / 2)

AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": mpf("7.7180"), "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}


def dim_sn(lam):
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
    # accumulate Σ y_λ |Δθ_λ^c| for c ∈ {abs, re, im}
    comps = ["abs", "re", "im"]
    S = {c: {} for c in comps}
    for name, fname in CHI.items():
        raw = json.load(open(HERE / fname))
        d = raw["data"] if "data" in raw else raw
        atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
        free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
        n = d["atom"]["n_strands"]
        y = load_y(n)
        acc = {c: mpf(0) for c in comps}
        for lam in atom:
            dl = dim_sn(list(lam))
            thf = acos(mp.mpc(free[lam] / dl))   # complex acos (real|rot, imag|growth)
            tha = acos(mp.mpc(atom[lam] / dl))
            dth = tha - thf
            acc["abs"] += y[lam] * fabs(dth)
            acc["re"] += y[lam] * fabs(mp_re(dth))
            acc["im"] += y[lam] * fabs(mp_im(dth))
        for c in comps:
            S[c][name] = acc[c]

    results = {}
    print(f"μ₀ = {float(mu0):.5f} MeV,  q₀ = {float(q0):.6f}\n")
    for c in comps:
        # one global scale fit across the four isotopes
        num = sum(S[c][k] * AME_B[k] for k in CHI)
        den = sum(S[c][k] ** 2 for k in CHI)
        scale = num / den if den else mpf(0)
        worst = mpf(0); per = {}
        for k in CHI:
            Bp = scale * S[c][k]
            err = (Bp - AME_B[k]) / AME_B[k]
            per[k] = {"S": float(S[c][k]), "B_pred": float(Bp), "err": float(err)}
            worst = max(worst, fabs(err))
        # T/³He difference, same scale, no isotope-fit
        diff = scale * (S[c]["T"] - S[c]["3He"])
        diff_err = (diff - (AME_B["T"] - AME_B["3He"])) / (AME_B["T"] - AME_B["3He"])
        results[c] = {"global_scale": float(scale), "worst_err": float(worst),
                      "per_isotope": per, "t_he3_diff_err": float(diff_err)}
        print(f"── component |Δθ.{c}|  scale={float(scale):.3f} MeV/rad  "
              f"worst|err|={float(worst)*100:.1f}%  T/³He diff err={float(diff_err)*100:+.1f}%")
        for k in CHI:
            print(f"     {k:<4} B={per[k]['B_pred']:8.4f}  AME={float(AME_B[k]):8.4f}  "
                  f"err={per[k]['err']*100:+8.1f}%")

    best_c = min(results, key=lambda c: results[c]["worst_err"])
    best_worst = results[best_c]["worst_err"]
    closes = best_worst <= 0.05
    print(f"\nbest component: |Δθ.{best_c}|  worst|err|={best_worst*100:.1f}%  "
          f"closes all 4 within 5%: {closes}")

    wb = WitnessBuilder("probe-full-theta-binding", engine="mpmath")
    wb.set_description(
        "EXPLORATORY: full-order per-block θ_λ = arccos(χ^λ/d_λ) ∈ ℂ "
        "(Re=rotation phase, Im=growth/volume). Tests which component of "
        "Σ_λ y_λ |Δθ_λ| reproduces ABSOLUTE binding D/T/³He/⁴He (1 global "
        "scale). Carries the growth (Im) channels the rotation-only probe "
        "excluded. Δ_λ / A≥3-absolute remains open."
    )
    wb.add_data("components", results)
    wb.add_data("best_component", best_c)
    wb.add_assertion(
        name="full_theta_does_not_close_A3plus_absolute_one_param",
        computed=str(int(not closes)),
        expected="1",
        tolerance=0,
        source=(f"best component |Δθ.{best_c}| worst |err| = {best_worst*100:.1f}% "
                "with one global scale; full-order θ_λ (incl. growth) does not "
                "close A≥3 absolute binding to 5% — the gate stands."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
