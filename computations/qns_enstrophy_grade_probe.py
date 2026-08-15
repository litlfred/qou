#!/usr/bin/env python3
"""qns_enstrophy_grade_probe — measure the realized enstrophy exponent α on the q→1⁺ ladder.

EXPLORATORY PROBE (not production; not wired to canonical scripts).

Context (q-NS surreal-bridge campaign, sessions qou-ohre..qou-zurg): the Lean
grade trichotomy (`QOU/FluidDynamics/surreal_enstrophy_finite_modes.lean`,
`grade_trichotomy` / `saturated_implies_infinite`) reduces the open critical-
exponent question of the super-classical side to one criterion: is ε·Ω(1+ε)
infinitesimal? Numerically we measure the SCALING exponent α in
Ω(1+ε) ~ ε^{−α} on a ladder ε = 10^{-1}..10^{-6} and bin it:

  α ≈ 0        → grade 0 (regular)
  α ≈ 1        → saturated (dissipation-closure cap, blow-up)
  0 < α < 1    → intermediate
  α > 1        → EXCEEDS the ω-grade-1 cap ⇒ the dissipation closure fails
                 for that spectrum (resolves the α=1 vs 4/3 tension, Finding 2)

Model: truncated spectral sum Ω(q) = Σ_{k<N_eff} [k]_q² a_k, with the Lean
convention [k]_q = (q^k − 1)/(q − 1) (so [k]_1 = k) and the corpus cascade
cutoff N_eff = ⌊(3/4)·ln Re / ln q⌋ (p2-critical-exponent). Two amplitude
models:
  A (sustained Kolmogorov): a_k = k^{-5/3}  (E(k) ~ k^{-5/3}; classical
    enstrophy density k^{1/3}, the turbulent-forcing scenario)
  B (Gevrey / smooth data): a_k = e^{-σk}, σ = 1/2

Honest scope: this decides which regime the MODELED spectrum realizes; it does
not decide the true q-NS flow (open analytic content). Precision tier: float64
+ math.fsum (scaling fit needs ~6 digits; not a 50-dps canonical derivation).

Run:  python3 -u computations/qns_enstrophy_grade_probe.py 2>&1 | tee /tmp/qns_grade_probe.log
"""
from __future__ import annotations

import math
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

try:
    from _precision import fmt  # noqa: E402
except Exception:  # pragma: no cover - fallback keeps the probe runnable
    def fmt(value, dps=None, strip_zeros=False):  # type: ignore[misc]
        return str(value)


def _f(x):
    """Serialize float64-tier values as strings.

    Witnesses must not carry raw float64 (AGENTS.md §"QA is agent-owned";
    `computations/witness_raw_float64_audit.py`). This probe's declared tier is
    *"float64+fsum (scaling fit)"* — a closed-form ladder plus a least-squares
    slope, with no integrator, so the `float64-integrator` carve-out
    (`qou-7kq3`) does **not** apply and serialization is the right treatment:
    `_precision.fmt` renders a float via `str()`, which round-trips exactly.
    Non-floats pass through untouched so counts and flags keep their JSON types.
    """
    return fmt(x) if isinstance(x, float) else x


RE = 1.0e4          # Reynolds number for the cascade cutoff
SIGMA = 0.5         # Gevrey decay rate (model B)
EPS_LADDER = [10.0 ** (-e) for e in range(1, 7)]  # 1e-1 .. 1e-6


def n_eff(q: float) -> int:
    return int((0.75 * math.log(RE)) / math.log(q))


def omega(q: float, model: str) -> float:
    """Truncated Ω(q) = Σ_{k=1}^{N_eff} [k]_q² a_k, [k]_q = (q^k−1)/(q−1)."""
    n = n_eff(q)
    qm1 = q - 1.0
    lnq = math.log(q)
    terms = []
    for k in range(1, n + 1):
        # [k]_q = (q^k − 1)/(q − 1); exponent kept in log form for stability
        qk = math.exp(k * lnq)
        bracket = (qk - 1.0) / qm1
        if model == "A":
            a_k = k ** (-5.0 / 3.0)
        else:
            a_k = math.exp(-SIGMA * k)
            if a_k < 1e-300:
                break
        terms.append(bracket * bracket * a_k)
    return math.fsum(terms)


def fit_alpha(eps_list, omega_list) -> float:
    """Least-squares slope of log Ω against −log ε."""
    xs = [-math.log(e) for e in eps_list]
    ys = [math.log(o) for o in omega_list]
    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    num = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    den = sum((x - xbar) ** 2 for x in xs)
    return num / den


def classify(alpha: float) -> str:
    if alpha < 0.1:
        return "grade0-regular"
    if alpha < 0.9:
        return "intermediate"
    if alpha <= 1.1:
        return "saturated-alpha1"
    return "exceeds-grade1-cap"


def main() -> None:
    w = WitnessBuilder("qns-enstrophy-grade-probe", engine="python")
    t0 = time.time()
    print("=" * 78)
    print("q-NS enstrophy grade probe: realized α on the q→1⁺ ladder (EXPLORATORY)")
    print("=" * 78)

    results = {}
    for model, label in (("A", "sustained Kolmogorov a_k=k^(-5/3)"),
                         ("B", f"Gevrey a_k=exp(-{SIGMA}k)")):
        print(f"\n[model {model}] {label}")
        oms = []
        for eps in EPS_LADDER:
            q = 1.0 + eps
            om = omega(q, model)
            oms.append(om)
            w.add_data(f"model{model}_eps_{eps:.0e}_omega", _f(om))
            w.add_data(f"model{model}_eps_{eps:.0e}_eps_omega", _f(eps * om))
            print(f"  eps={eps:.0e}  N_eff={n_eff(q):>8d}  Omega={om:.6e}  eps*Omega={eps*om:.6e}  [{time.time()-t0:5.1f}s]")
        alpha = fit_alpha(EPS_LADDER, oms)
        verdict = classify(alpha)
        results[model] = (alpha, verdict)
        w.add_data(f"model{model}_alpha_fit", _f(alpha))
        w.add_data(f"model{model}_regime", verdict)
        print(f"  → fitted α_{model} = {alpha:.4f}  regime: {verdict}")

    aA, vA = results["A"]
    aB, vB = results["B"]

    w.add_assertion(
        "Model B (Gevrey smooth data) is grade-0 regular (α ≈ 0)",
        computed=(vB == "grade0-regular"), expected=True,
        source=f"alpha_B = {aB:.4f}; bounded Ω as q→1⁺ for exponentially decaying spectra",
    )
    w.add_assertion(
        "Model A fitted α is finite and recorded",
        computed=math.isfinite(aA), expected=True,
        source=f"alpha_A = {aA:.4f}, regime {vA}",
    )
    w.add_assertion(
        "Model A EXCEEDS the ω-grade-1 dissipation-closure cap (α > 1.1): the "
        "dissipation closure fails for sustained Kolmogorov spectra",
        computed=(aA > 1.1), expected=True,
        source="enstrophy_grade_one_of_dissipation_closure caps α at 1 UNDER the "
               "dissipation closure; the measured α ≈ 4/3 therefore falsifies that "
               "closure for sustained spectra (resolves the Finding-2 α tension "
               "in favor of the cascade value in-model)",
    )
    w.add_assertion(
        "Model A fitted α matches the cascade value 4/3 to within 0.05",
        computed=(abs(aA - 4.0 / 3.0) < 0.05), expected=True,
        source=f"alpha_A = {aA:.4f} vs 4/3 = {4.0/3.0:.4f} "
               f"(|Δ| = {abs(aA - 4.0/3.0):.4f}); p2-critical-exponent cascade estimate",
    )

    w.set_description(
        "Exploratory probe of the q-NS surreal-bridge grade trichotomy "
        "(QOU/FluidDynamics/surreal_enstrophy_finite_modes.lean): measures the realized "
        "enstrophy scaling exponent α in Ω(1+ε) ~ ε^(−α) on the ladder ε=1e-1..1e-6, "
        "with the Lean convention [k]_q = (q^k−1)/(q−1) and the corpus cascade cutoff "
        "N_eff = (3/4)ln Re/ln q (Re=1e4). Model A: sustained Kolmogorov a_k=k^(-5/3) "
        "(turbulent forcing). Model B: Gevrey a_k=exp(-k/2) (fixed smooth data). Bins: "
        "α≈0 grade-0 regular; α≈1 saturated; 0<α<1 intermediate; α>1 exceeds the "
        "Lean-proved grade-1 cap, falsifying the dissipation closure for that spectrum. "
        "Decides the regime of the MODELED spectrum only — not the true q-NS flow (open). "
        "Precision tier: float64+fsum (scaling fit), not a 50-dps canonical derivation."
    )
    w.add_data("tier", "exploratory")
    w.add_data("re", _f(RE))
    w.add_data("sigma", _f(SIGMA))
    w.add_data("qint_convention", "one-sided (q^k-1)/(q-1), matches Lean qInt")
    w.add_data("finding",
               f"alpha_A={aA:.4f} ({vA}); alpha_B={aB:.4f} ({vB}). "
               "See per-eps omega + eps*omega traces for the surreal criterion.")

    w.save()
    print(f"\nSaved witness: qns-enstrophy-grade-probe.witness.json  [{time.time()-t0:.1f}s total]")


if __name__ == "__main__":
    main()
