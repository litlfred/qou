#!/usr/bin/env python3
"""EXPLORATORY — content-energy weight + signed phase: is w_λ^bind = (Casimir energy) × (phase)?

Two linked questions from the binding-measure search
(2026-06-02-binding-measure-search.md), which found `abs_content` (Σ|content|)
matches the binding A-growth (13.40 vs 12.72) but breaks the T/³He difference:

1. DERIVE the content weight as a Hecke-ENERGY density. The cell content
   c = j−i is the Jucys–Murphy eigenvalue; Σ_cells content = the L₀ grading,
   and the quadratic Casimir of the S_n irrep λ is c₂(λ) = Σ_cells c·(c+1)·...
   ~ Σ content (and the energy ~ Σ content²). We test which content invariant
   (|content|, content², the Casimir Σ c(c−1)+... ) best matches the binding
   A-growth — i.e. WHICH content-energy is the density.

2. COMBINE content-energy × signed phase to recover the T/³He difference the
   isospin-blind |content| lost. We test a SMALL, structurally-motivated set
   (no multiple-comparisons fishing):
     w_λ ∈ { |content|, content², |content|·y_λ, content²·y_λ }
   against B = E·Σ_λ w_λ |Δθ_λ| (full-order complex θ_λ), reporting BOTH the
   absolute worst |err| AND the T/³He difference. Joint closure = small in both.

EXPLORATORY: asserts the refutation (CI-safe). A positive (a structural weight
closing both) is surfaced for promotion + categorical derivation. Δ_λ open.
"""
from __future__ import annotations

import json
from pathlib import Path

import _path_bridge  # noqa: F401, E402 — Phase-6 bridge: flat imports from substrate/
import mpmath as mp  # noqa: E402
from mpmath import mpf, fabs, acos  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402 — AME validation refs

set_compute_dps()
HERE = Path(__file__).resolve().parent

# AME 2020 binding-energy comparison targets (validation-only; this probe
# fits a global scale, so no MeV calibration constant is used).
AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}
BIND_RATIO = 12.72   # AME B(⁴He)/B(D)


def hooks(lam):
    colh = [0] * (max(lam) if lam else 0)
    for ri in lam:
        for j in range(ri):
            colh[j] += 1
    return [(ri - j - 1) + (colh[j] - i - 1) + 1
            for i, ri in enumerate(lam) for j in range(ri)]


def dim_classical(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= h
    return mp.factorial(sum(lam)) / den


def contents(lam):
    return [j - i for i, ri in enumerate(lam) for j in range(ri)]


def abs_content(lam):
    return mpf(sum(abs(c) for c in contents(lam)))


def content_sq(lam):
    """Σ content² — the quadratic-Casimir energy of the S_n irrep λ."""
    return mpf(sum(c * c for c in contents(lam)))


def casimir(lam):
    """Σ_cells content·(content+1) (the standard 2nd Casimir summand)."""
    return mpf(sum(c * (c + 1) for c in contents(lam)))


_y_cache = None


def load_y(n):
    global _y_cache
    if _y_cache is None:
        with open(HERE / "y-lambda-at-q0.witness.json") as f:
            _y_cache = json.load(f)
    byn = _y_cache.get("data", _y_cache)["by_n"][str(n)]
    return {tuple(e["partition"]): mpf(e["y_at_q0_50dps"]) for e in byn}


def main() -> int:
    # ── (1) content-energy A-growth check ──
    energy_fns = {"abs_content": abs_content, "content_sq": content_sq,
                  "casimir_c(c+1)": casimir}
    print("(1) which content-energy matches the binding A-growth 12.72?")
    egrow = {}
    atoms_parts = {}
    for k in ("D", "4He"):
        with open(HERE / CHI[k]) as f:
            data = json.load(f)
        data = data.get("data", data)
        atoms_parts[k] = [tuple(e["partition"]) for e in data["atom"]["by_partition"]]
    for ename, efn in energy_fns.items():
        s_d = sum(efn(list(p)) for p in atoms_parts["D"])
        s_4 = sum(efn(list(p)) for p in atoms_parts["4He"])
        ratio = float(s_4 / s_d) if s_d != 0 else None
        egrow[ename] = {"S4_over_SD": ratio,
                        "abs_diff_from_12.72":
                            abs(ratio - BIND_RATIO) if ratio is not None else None}
        print(f"    {ename:<16} weight-only S(⁴He)/S(D) = {ratio:.2f}")

    # ── (2) content-energy × |Δθ| (and × y_λ) joint test ──
    weights = {
        "abs_content": lambda lam, y: abs_content(lam),
        "content_sq": lambda lam, y: content_sq(lam),
        "abs_content*y": lambda lam, y: abs_content(lam) * y,
        "content_sq*y": lambda lam, y: content_sq(lam) * y,
    }
    S = {w: {} for w in weights}
    for name, fname in CHI.items():
        with open(HERE / fname) as f:
            d = json.load(f)
        d = d.get("data", d)
        atom = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["atom"]["by_partition"]}
        free = {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d["free"]["by_partition"]}
        y = load_y(d["atom"]["n_strands"])
        acc = {w: mpf(0) for w in weights}
        for lam in atom:
            dl = dim_classical(list(lam))
            a = abs(acos(mp.mpc(atom[lam] / dl)) - acos(mp.mpc(free[lam] / dl)))
            for w, wf in weights.items():
                acc[w] += wf(list(lam), y[lam]) * a
        for w in weights:
            S[w][name] = acc[w]

    print("\n(2) content-energy × phase — joint absolute + T/³He difference:")
    results = {}
    best = None
    for w in weights:
        num = sum(S[w][k] * AME_B[k] for k in CHI)
        den = sum(S[w][k] ** 2 for k in CHI)
        scale = num / den if den else mpf(0)
        worst = mpf(0); per = {}
        for k in CHI:
            err = (scale * S[w][k] - AME_B[k]) / AME_B[k]
            per[k] = float(err); worst = max(worst, fabs(err))
        diff = scale * (S[w]["T"] - S[w]["3He"])
        diff_err = (diff - (AME_B["T"] - AME_B["3He"])) / (AME_B["T"] - AME_B["3He"])
        joint = max(float(worst), float(fabs(diff_err)))
        results[w] = {"worst_abs_err": float(worst),
                      "t_he3_diff_err": float(diff_err), "joint": joint,
                      "per_isotope": per}
        if best is None or joint < results[best]["joint"]:
            best = w
        print(f"    {w:<16} abs worst |err|={float(worst)*100:7.1f}%  "
              f"T/³He diff={float(diff_err)*100:+7.1f}%  joint={joint*100:.1f}%")

    print(f"\nbest (min joint): {best}  joint={results[best]['joint']*100:.1f}%")
    closes = results[best]["joint"] <= 0.05

    wb = WitnessBuilder("probe-content-energy-signed-phase", engine="mpmath")
    wb.set_description(
        "EXPLORATORY: (1) which content-energy (|content|, content², Casimir) "
        "matches the binding A-growth 12.72; (2) content-energy × |Δθ_λ| "
        "(optionally × y_λ) joint test of absolute binding + T/³He difference "
        "on D/T/³He/⁴He. Searches whether w_λ^bind = content-energy × phase "
        "closes both. Δ_λ / A≥3-absolute remains open."
    )
    wb.add_data("content_energy_A_growth", egrow)
    wb.add_data("joint_weights", results)
    wb.add_data("best_weight", best)
    wb.add_data("target_A_growth", BIND_RATIO)
    wb.add_assertion(
        name="no_content_energy_phase_weight_jointly_closes",
        computed=str(int(not closes)),
        expected="1",
        tolerance=0,
        source=(f"best {best} joint (max of abs-worst, |T/³He diff|) = "
                f"{results[best]['joint']*100:.1f}%; no content-energy×phase "
                "weight jointly closes absolute + difference to 5%."),
    )
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
