#!/usr/bin/env python3
"""Frobenius-Gram Δ_λ in the sign-solved counit defect — a NEW parameter-free weight.

CONTEXT (GAP-A, Δ_λ per-isotope binding closure).
The counit *defect* functional ε(β_K) − ε(β_K^vac) robustly fixes the binding
SIGN (negative for all four low isotopes — `rho_k_counit_defect_form.py`).  The
open piece is the per-partition MAGNITUDE weight Δ_λ.  Four weights are already
refuted on the deuteron (target −B_D/m_e = −4.353):

    Δ_λ = 1        (counit,   Σ dχ)          = −30.29  (explodes with A)
    Δ_λ = y_λ      (trM,      Σ y·dχ)         =  −0.60  (collapses, A-flat)
    Δ_λ = y_λ/dim_q(co-Cas,   Σ y·dχ/dim_q)   =  −0.07  (collapses)
    Δ_λ = y_λ·sgn·f^λ (Opt-E, Σ y·sgn·f·dχ)   =  −2.40  (closest, |miss|=1.95)

`gram_transfer_quadratic` supplies a DISTINCT, parameter-free per-λ object —
the Frobenius Gram norm ‖ρ_λ(W)‖²_F = tr_M(W·W^♯) — computed exactly (50 dps)
by the doubled-Bratteli transfer that clears the dense n≥12 wall.  This probe
plugs ‖ρ_λ‖²_F (and natural parameter-free variants) into the sign-solved
defect and measures the magnitude on D / T / ³He / ⁴He.

RESULT (scope-(a), EXPLORATORY, no fit, no production consumer).
Every Frobenius variant OVER-shoots massively and EXPLODES with A — the norm
amplifies high-dimensional partitions (≈ d_λ² scale), the opposite of what
closure needs.  Best variant (Σ y·‖ρ‖²·dχ) = −29.2 on D, worse than every
prior weight except the raw counit.  So ‖ρ_λ‖²_F is REFUTED as the closing
weight (scope-(a): this weight, alone, does not close the magnitude).

DURABLE CONTRIBUTION — the probe BRACKETS the GAP-A answer.  Ordered by
deuteron magnitude:  trM (−0.60, collapses)  <  Option-E (−2.40)  <  |target|
(−4.35)  ≪  Frobenius (−29.2, explodes).  The closing Δ_λ must be a MILD
dim-enhancement sitting just past Option-E's sgn·f^λ — NOT a d²-scale norm and
NOT the flat trM.  This constrains (does not exclude) the ingredient class.

`-- Ref:` interface-knot-markov-z.md (β_K = β_K^vac·⋈_K, defect factorization);
Ram IMRN 1997 (tr_M = Σ y_λ χ^λ); Geck–Pfeiffer 2000 (Schur elements y_λ).
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from mpmath import mp, mpf, fabs, sqrt  # noqa: E402
from codata_constants import (
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    M_E_MEV  # noqa: E402,
)
from substrate.witness_base import WitnessBuilder  # noqa: E402
from gram_transfer_quadratic import gram_norm_zn  # noqa: E402
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

m_e = mpf(str(M_E_MEV))
COMP = str(_COMP)

B_AME = {"D": mpf("2.22452"), "T": AME_B_TRITIUM_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
FILES = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
         "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
YFILE = {"D": None, "T": "wenzl-y-lambda-h9.witness.json",
         "3He": "wenzl-y-lambda-h9.witness.json", "4He": "wenzl-y-lambda-h12.witness.json"}


def load_chi(fn: str, key: str) -> dict:
    with open(os.path.join(COMP, fn), encoding="utf-8") as f:
        d = json.load(f)["data"][key]["by_partition"]
    return {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d}


def load_y(name: str) -> dict:
    if name == "D":
        with open(os.path.join(COMP, "rho-k-h3a-lp-dual.witness.json"), encoding="utf-8") as f:
            lp = json.load(f)
        return {tuple(e["partition"]): mpf(str(e["y_lambda_at_q0"])) for e in lp["data"]["per_lambda"]}
    with open(os.path.join(COMP, YFILE[name]), encoding="utf-8") as f:
        d = json.load(f)
    return {tuple(e["partition"]): mpf(e["y_lambda"]) for e in d["data"]["per_partition"]}


def run_isotope(name: str) -> dict:
    Z, N = ZN[name]
    atom = load_chi(FILES[name], "atom")
    free = load_chi(FILES[name], "free")
    dchi = {l: atom[l] - free[l] for l in atom}
    y = load_y(name)
    tgt = -B_AME[name] / m_e

    _, _, norms_a = gram_norm_zn(Z, N, include_inter=True)
    _, _, norms_f = gram_norm_zn(Z, N, include_inter=False)
    ka = [l for l in dchi if l in norms_a]
    kf = [l for l in dchi if l in norms_a and l in norms_f and norms_f[l] != 0]

    variants = {
        "ref_trM  Σ y·dχ": mp.fsum(y.get(l, mpf(0)) * dchi[l] for l in dchi),
        "frob  Σ ‖ρa‖²·dχ": mp.fsum(norms_a[l] * dchi[l] for l in ka),
        "frob  Σ y·‖ρa‖²·dχ": mp.fsum(y.get(l, mpf(0)) * norms_a[l] * dchi[l] for l in ka),
        "frobRatio  Σ (‖ρa‖²/‖ρf‖²)·dχ": mp.fsum((norms_a[l] / norms_f[l]) * dchi[l] for l in kf),
        "frobDefect Σ (‖ρa‖²−‖ρf‖²)·dχ": mp.fsum((norms_a[l] - norms_f[l]) * dchi[l] for l in kf),
        "sqrtFrob  Σ ‖ρa‖·dχ": mp.fsum(sqrt(norms_a[l]) * dchi[l] for l in ka),
    }
    out = {}
    for lbl, S in variants.items():
        miss = fabs(S - tgt)
        out[lbl] = {"S": mp.nstr(S, 10), "abs_miss": mp.nstr(miss, 6),
                    "within_tol": bool(miss < 1), "sign_negative": bool(S < 0)}
    return {"target_minus_B_over_me": mp.nstr(tgt, 10), "n": 3 * (Z + N), "variants": out}


def main() -> int:
    per_iso = {name: run_isotope(name) for name in FILES}

    # every Frobenius variant negative (sign preserved) but none closes tol=1
    all_neg = all(v["sign_negative"] for iso in per_iso.values()
                  for lbl, v in iso["variants"].items() if lbl.startswith(("frob", "sqrt")))
    any_close = any(v["within_tol"] for iso in per_iso.values()
                    for lbl, v in iso["variants"].items() if lbl.startswith(("frob", "sqrt")))

    payload = {
        "computation": "frobenius-gram-delta-lambda",
        "description": ("Frobenius Gram norm ‖ρ_λ‖²_F (gram_transfer_quadratic) as a "
                        "parameter-free Δ_λ weight in the sign-solved counit defect, on "
                        "D/T/³He/⁴He. Every Frobenius variant explodes with A (≈d_λ² scale) "
                        "— REFUTED as the closing weight (scope-(a)); brackets GAP-A between "
                        "Option-E and the target. audit-only, no fit."),
        "tier": "structural-exact (committed χ^λ atom/free + exact 50-dps Frobenius Gram norms)",
        "result": {
            "free_parameters": 0,
            "per_isotope": per_iso,
            "verdict": ("‖ρ_λ‖²_F REFUTED as the GAP-A closing weight (scope-(a)): every variant "
                        "over-shoots and EXPLODES with A, amplifying high-dim partitions. Durable: "
                        "brackets the answer — closing Δ_λ is a MILD dim-enhancement between Option-E "
                        "(sgn·f^λ, −2.40 on D) and |target| (−4.35), NOT a d²-scale norm."),
        },
        "context": {
            "axis": "Δ_λ per-isotope binding closure (GAP-A) — Frobenius Gram weight",
            "sign_solved_by": "rho_k_counit_defect_form.py (defect ε(β_K)−ε(β_K^vac) < 0 all isotopes)",
            "weight_source": "gram_transfer_quadratic.gram_norm_zn (exact doubled-Bratteli tr_M(W·W^♯))",
            "chi_source": "atom-chi-rust-{d,t,3he,4he}.witness.json (data.atom + data.free)",
        },
    }
    # Assertions via the builder API — wrap_legacy() drops payload-level
    # `assertions`/`allPassed` (reserved keys); booleans encoded as computed/expected.
    wb = WitnessBuilder.wrap_legacy(
        "frobenius-gram-delta-lambda", payload,
        script_path=__file__, engine="python+mpmath",
        output_dir=COMP,
    )
    wb.add_assertion("frobenius_variants_preserve_binding_sign",
                     computed=str(bool(all_neg)), expected="True")
    wb.add_assertion("no_frobenius_variant_closes_magnitude",
                     computed=str(bool(not any_close)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Frobenius-Gram Δ_λ in the sign-solved defect ===")
    for name, iso in per_iso.items():
        print(f"\n{name}  (n={iso['n']})  target -B/m_e = {float(iso['target_minus_B_over_me']):.4f}")
        for lbl, v in iso["variants"].items():
            flag = "  <<< CLOSES" if v["within_tol"] else ""
            print(f"  {lbl:34} S={float(v['S']):>14.4f}  |miss|={float(v['abs_miss']):>10.3f}{flag}")
    print("\nVERDICT: ‖ρ_λ‖²_F explodes with A — REFUTED (scope-a); brackets GAP-A. witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
