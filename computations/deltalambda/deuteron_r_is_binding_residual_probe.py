#!/usr/bin/env python3
"""`r = g₂ − 1` is the deuteron binding residual, magnified by 1/h² — NOT a separable special-function
puzzle. The decisive reframing of the four-session g₂ chase: g₂ is an AFFINE image of the measured
binding, so deriving r ≡ predicting B(deuteron) to ~36 ppm. Exact, forward, **no fit**.

CHAIN (read first):
  * The bar-even coefficient is DEFINED (#4158 Magnus/E_unit route, eunit_magnus_order2_probe.py +
    2026-07-24-eunit-magnus-order2.md) as g₂ = (E_AME/E⁺ − 1)/h², E⁺ = E_rot/(1−t), with:
      - E_rot = μ₀·ℏ_q·[j]_q[j+1]_q = 2.0195829 MeV (first-order rotational energy, j=3; pure theory)
      - t = (v−v⁻¹)/[2]_v (bar-odd impurity, v=√q₀; pure theory)
      - h = q−q⁻¹ (pure theory)
      - E_AME = 2.2245662 MeV (MEASURED deuteron binding)
  * g₂_leading = 1 is derived exact (#4339, real coloring). r = g₂ − 1 ≈ +0.87% is the residual.
  * The frontier (#4347) + this session's lifted-dilog refutation (#4369) reduced r to "the geometric
    quantum-dilog on the 4-shape octahedron" and showed every principled amplitude gives g₂ ∈ {0, 1,
    9/8, 0.979} — never 1.00865. THIS probe explains why.

THE DECISIVE STRUCTURE (exact; reproduces the corpus g₂ = 1.00865 to 6 sig figs):
  Because E⁺ and h are PURE THEORY, g₂ = (E_AME/E⁺ − 1)/h² is an AFFINE function of the measured
  binding E_AME, with amplification dg₂/(dE_AME/E_AME) = E_AME/(E⁺·h²) ≈ 23.9 (Lean-proved
  `g2_amplification`, BindingResidualAmplification.lean). The 1/h² MAGNIFIES the binding's relative
  error ~24×. Consequences:
    A. g₂ = 1.0086522, r = +0.8652% — EXACTLY the corpus value (bookkeeping confirmed correct).
    B. To pin r to 10% one must predict B(deuteron) to ~36 ppm — ~2540× tighter than the framework's
       current first-order binding accuracy (−9.21% = 92100 ppm). To even DISTINGUISH g₂=1.0087 from
       g₂=1 needs ~362 ppm.
    C. Even the TABULATED input precision limits r: rounding E_rot to 2.0196 (a 1e-4 MeV display
       rounding) shifts g₂ by 2.3% of r. r lives below the noise floor of the tabulated theory input.

VERDICT (scope-(a), decisive): r is NOT a special-function target separable from the binding —
deriving r ≡ predicting the deuteron binding to ~36 ppm, i.e. r IS the Δ_λ deuteron-binding closure
(the Track A blocker) viewed through a 1/h² magnifier. Every categorical amplitude correctly
reproduces the DERIVED leading g₂ ≈ 1; the residual r is the still-open binding the framework cannot
predict at 36 ppm. This QUANTIFIES the §2e entropy warning: a ~36-ppm target carries essentially zero
fit-information. RECOMMENDATION: pause the g₂/r chase; bank g₂_leading = 1 (derived); r reduces to the
general Δ_λ closure (open-for-all per the 2026-07-13 reversal) at a precision far beyond current reach.

EXPLORATORY — audit + witness only. scope-(a); nothing wired; no fit, no AME inversion (E_AME is used
as the measured target the residual is DEFINED against, exactly as the corpus defines g₂ — not fitted).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0_STR = "1.10997859555733471"   # muon-canonical (computations/ layer)


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    h = q0 - 1 / q0
    v = mp.sqrt(q0)
    E_rot = mp.mpf("2.0195829")            # pure theory, j=3 (binding-qhamiltonian-rotational-scale)
    E_AME = mp.mpf("2.2245662")            # measured deuteron binding
    t = (v - 1 / v) / (v + 1 / v)          # bar-odd impurity, pure theory
    Eplus = E_rot / (1 - t)
    g2 = (E_AME / Eplus - 1) / h ** 2
    r = g2 - 1

    amp = (E_AME / Eplus) / h ** 2         # dg2 / (dE_AME/E_AME) — Lean g2_amplification coefficient
    prec_r10 = mp.mpf("0.1") * r / amp     # rel precision on B needed to pin r to 10%
    prec_see = r / amp                     # rel precision to distinguish g2=1.0087 from 1
    ratio_vs_current = mp.mpf("0.0921") / prec_r10

    # C. tabulated-input sensitivity
    g2_rounded = (E_AME / (mp.mpf("2.0196") / (1 - t)) - 1) / h ** 2
    round_shift_frac = (g2_rounded - g2) / r

    result = {
        "A_exact_g2_reproduced": {
            "E_rot_MeV": "2.0195829 (theory, j=3)",
            "E_AME_MeV": "2.2245662 (measured)",
            "t_bar_odd": mp.nstr(t, 8),
            "h2": mp.nstr(h ** 2, 8),
            "Eplus": mp.nstr(Eplus, 10),
            "g2": mp.nstr(g2, 8) + "  (corpus value 1.00865 — bookkeeping confirmed)",
            "r_pct": mp.nstr(r * 100, 5),
        },
        "B_amplification_and_precision": {
            "amplification_dg2_per_relE": mp.nstr(amp, 6) + " (Lean-proved g2_amplification coeff)",
            "B_precision_to_pin_r_10pct_ppm": mp.nstr(prec_r10 * 1e6, 4),
            "B_precision_to_see_r_ppm": mp.nstr(prec_see * 1e6, 4),
            "current_first_order_accuracy_ppm": "92100 (−9.21%)",
            "ratio_needed_vs_current": mp.nstr(ratio_vs_current, 5) + "× tighter",
            "meaning": "g₂ is AFFINE in the measured binding (E⁺,h pure theory); the 1/h² magnifies "
                       "B's relative error ~24×. Deriving r ≡ predicting B(deuteron) to ~36 ppm.",
        },
        "C_tabulated_input_floor": {
            "g2_shift_from_Erot_1e-4_rounding": mp.nstr(g2_rounded - g2, 4),
            "as_fraction_of_r": mp.nstr(round_shift_frac * 100, 3) + "%",
            "meaning": "a 1e-4 MeV display rounding of E_rot moves g₂ by 2.3% of r — r lives below the "
                       "noise floor of the tabulated theory input.",
        },
        "verdict": {
            "classification": "scope-(a), decisive reframing: r is NOT a separable special-function "
                              "target. Deriving r ≡ predicting the deuteron binding to ~36 ppm, i.e. r "
                              "IS the Δ_λ deuteron-binding closure (Track A blocker) magnified by 1/h².",
            "why_amplitudes_give_1": "every categorical amplitude reproduces the DERIVED leading g₂≈1; "
                                     "the residual r is the still-open binding, unreachable at 36 ppm.",
            "entropy_2e_quantified": "a ~36 ppm target carries ~zero fit-information — the four-session "
                                     "g₂ chase was chasing a magnified image of the unclosed binding.",
            "recommendation": "pause the g₂/r chase; bank g₂_leading=1 (derived); r reduces to the "
                              "general Δ_λ closure at a precision far beyond current reach.",
            "no_fit": True,
            "no_ame_inversion": "E_AME is the measured target r is DEFINED against (corpus g₂ "
                                "definition), not a fitted parameter.",
        },
    }

    payload = {
        "computation": "deuteron-r-is-binding-residual",
        "description": ("Decisive reframing of the g₂ chase: the bar-even coefficient g₂ = "
                        "(E_AME/E⁺ − 1)/h² (#4158 Magnus definition; E⁺=E_rot/(1−t), all pure theory "
                        "except the MEASURED E_AME) is an AFFINE image of the deuteron binding, with "
                        "amplification E_AME/(E⁺·h²) ≈ 23.9 (Lean-proved, BindingResidualAmplification). "
                        "Reproduces the corpus g₂ = 1.00865 exactly. So r = g₂−1 ≈ +0.87% is the binding "
                        "residual magnified ~24× by 1/h²: deriving r ≡ predicting B(deuteron) to ~36 ppm "
                        "(~2540× tighter than the current −9.21% accuracy; finer than the tabulated "
                        "E_rot's 1e-4 MeV precision, which already moves r by 2.3%). r is NOT a "
                        "separable special-function puzzle — it IS the Δ_λ deuteron-binding closure "
                        "viewed through a 1/h² magnifier, which quantifies the §2e entropy warning and "
                        "explains why every amplitude gives the derived leading g₂≈1 but never the "
                        "residual. Recommendation: pause the g₂/r chase. scope-(a), audit-only, nothing "
                        "wired; no fit, no AME inversion."),
        "audit_only": True,
        "tier": "exact affine/amplification structure (Lean-proved) + precision-requirement derivation; "
                "reproduces corpus g₂; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the exact residual r = g₂ − 1",
            "lean": "QOU/MassTheory/BindingResidualAmplification.lean (g2_affine, g2_amplification)",
            "builds_on": "#4158 (Magnus g₂ definition), #4339 (g₂_leading=1), #4347 (frontier), "
                         "#4369 (lifted-dilog refutation + pinch degeneracy)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deuteron-r-is-binding-residual", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("g2_reproduces_corpus", computed=mp.nstr(g2, 6), expected="1.00865")
    wb.add_assertion("amplification_factor", computed=mp.nstr(amp, 4), expected="23.89")
    wb.add_assertion("B_precision_ppm_for_r10pct", computed=mp.nstr(prec_r10 * 1e6, 3), expected="36.2")
    out = wb.save(extra={"auditOnly": True})

    print("=== r = g₂ − 1 is the deuteron binding residual, magnified by 1/h² ===")
    print(f"A. g₂ = (E_AME/E⁺−1)/h² = {mp.nstr(g2,8)}  (corpus 1.00865 — exact)   r = +{mp.nstr(r*100,4)}%")
    print(f"B. amplification dg₂/(dE/E) = {mp.nstr(amp,6)}  ⇒  B(deuteron) to {mp.nstr(prec_r10*1e6,4)} ppm "
          f"to pin r@10%  ({mp.nstr(ratio_vs_current,4)}× tighter than −9.21%)")
    print(f"C. E_rot 1e-4 rounding shifts g₂ by {mp.nstr(round_shift_frac*100,3)}% of r — below tabulated "
          f"input floor")
    print("VERDICT (decisive, scope-a): r is NOT a separable special-function target; deriving r ≡ "
          "predicting B(deuteron) to ~36 ppm = the Δ_λ closure magnified 1/h². Every amplitude gives "
          "the derived g₂≈1; r is the unclosed binding. Recommend PAUSE the g₂ chase. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
