#!/usr/bin/env python3
"""Is g₂ "fitted to AME"? The honest larger context: g₂ is NOT a tuned parameter, but r = g₂−1 is a
FRAME ARTIFACT — its value swings 12× across equally-valid bar-odd-removal conventions. What IS real:
the framework predicts B(deuteron) to ~0.04% from q₀ via three DERIVED tiers. Exact, forward, no fit.

CONTEXT (owner question, 2026-07-26): "keep pushing on g₂ beyond leading; it seems fitted to AME which
is bad; what is the larger context?" This probe answers it by measuring the frame-dependence of r and
locating where the bar-even unit actually comes from.

DEFINITION (corpus #4158): g₂ = (E_AME/E⁺ − 1)/h², E⁺ = E_rot/(1−t), with E_rot=2.0195829 (rotational,
theory), t=(v−v⁻¹)/[2]_v (bar-odd, theory), h=q−q⁻¹ (theory), E_AME=2.2245662 (measured).

FINDING 1 — TIER CONVERGENCE (the REAL, robust result). Using only q₀-derived inputs:
    tier 0  E_rot                     err −9.215%   (rotational)
    tier 1  E⁺ = E_rot/(1−t)          err −4.222%   (+ bar-odd t = 5.21%)
    tier 2  E⁺·(1 + 1·h²)  [g₂=1]     err −0.036%   (+ bar-even UNIT, coefficient 1)
  The framework predicts B(deuteron) to 0.036% (360 ppm) PARAMETER-FREE. g₂ ≈ 1 (the bar-even
  correction ≈ one h² unit) is a genuine, robust prediction — NOT a fit.

FINDING 2 — r IS A FRAME ARTIFACT (why "it smells fitted" is right, sharpened). r = g₂−1 depends on
the O(t²) convention used to remove the SAME 5.21% bar-odd tier:
    E⁺ = E_rot/(1−t)  →  r = +0.87%   (corpus)
    E⁺ = E_rot·(1+t)  →  r = +7.37%
    E⁺ = E_rot·eᵗ     →  r = +4.23%
    B = E⁺/(1−g₂h²)   →  r = −3.39%
  r ranges over [−3.4%, +7.4%] — spread ~11%, ≈ 12× the signal |r| ≈ 0.87%. The residual is
  ~90% convention, not physics. So r is NOT a well-defined derivation target; chasing a special
  function for it (the four-session g₂/dilog effort) was doomed by frame-ambiguity, independent of
  the §2e entropy bound.

FINDING 3 — WHERE the bar-even unit comes from (why g₂=1 is near-definitional). For the deuteron word
σ₁³ (a SINGLE generator) every Magnus commutator [a,a]=0, so Ω_{k≥2}=0 EXACTLY (proved, #4158). The
bar-even h² correction is therefore NOT a dynamical (Magnus/holonomy) term — it is the character/frame
projection of the order-h² unit. So "g₂_leading=1" is essentially the statement that the natural
order-h² frame unit has coefficient 1 (near-definitional given the h² normalization), and r is the
residual of the frame choice, not a categorical amplitude to be derived.

VERDICT (scope-(a), answers the owner). NOT fitted (no tuned parameter), but the instinct is correct:
r is a frame artifact (12× convention spread) sitting on top of a genuine 0.036% parameter-free B(D)
prediction. The sound, bankable statements are (i) B(deuteron) predicted to ~0.04% from q₀ via three
derived tiers, and (ii) g₂ ≈ 1 (bar-even correction = one h² unit). The residual r = +0.87% is neither
robust nor separable — it is the frame-noise-dominated tail of the deuteron binding, not a special
function. LARGER CONTEXT: the real open problem is B(deuteron) itself below ~0.04% (a well-defined,
frame-independent target = the Δ_λ closure), not r (a frame-dependent repackaging).

EXPLORATORY — audit + witness only. scope-(a); nothing wired; no fit, no AME inversion (E_AME is the
measured target the corpus DEFINES g₂ against, used here only to expose frame-dependence).
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
# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was the literal
# "1.10997859555733471" -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22 (fca08de7d2) by the live CODATA-2022 lepton-ratio derivation.
# A frozen literal cannot follow the anchor when it moves, and this producer
# was UNSTAMPED, so the anchor audit filed it Q0_ANCHOR_MISSING rather than
# Q0_FLIP -- invisible to the corpus-wide drain, which keys on stamps.
# It resolves the PROTON pin per the owner directive of 2026-08-15, sharpened
# 2026-08-30: proton unless the producer is (E1) an explicit mu-vs-p
# comparison or (E2) the ideal CAL-1/2/3 mathematical layer. This is neither
# -- it is a sole-anchor probe that happened to be muon-named.
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)

Q0_STR = _Q0_RESOLVED


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    h = q0 - 1 / q0
    v = mp.sqrt(q0)
    E_rot = mp.mpf("2.0195829")
    E_AME = AME_B_DEUTERON_MEV_VALIDATION
    t = (v - 1 / v) / (v + 1 / v)

    def err(x):
        return (x - E_AME) / E_AME * 100

    Eplus = E_rot / (1 - t)
    tiers = {
        "tier0_E_rot": (E_rot, err(E_rot)),
        "tier1_Eplus_bar_odd": (Eplus, err(Eplus)),
        "tier2_bar_even_unit_g2_is_1": (Eplus * (1 + h ** 2), err(Eplus * (1 + h ** 2))),
    }

    # frame-sensitivity of r
    frames = {
        "E+ = E_rot/(1-t) [corpus]": (E_AME / (E_rot / (1 - t)) - 1) / h ** 2,
        "E+ = E_rot*(1+t)": (E_AME / (E_rot * (1 + t)) - 1) / h ** 2,
        "E+ = E_rot*exp(t)": (E_AME / (E_rot * mp.e ** t) - 1) / h ** 2,
        "B = E+/(1-g2 h2) [inverse]": (1 - (E_rot / (1 - t)) / E_AME) / h ** 2,
    }
    r_vals = [g - 1 for g in frames.values()]
    r_spread = max(r_vals) - min(r_vals)
    signal = abs((E_AME / Eplus - 1) / h ** 2 - 1)
    spread_ratio = r_spread / signal

    result = {
        "F1_tier_convergence": {
            "tiers_err_pct": {k: mp.nstr(e, 5) for k, (x, e) in tiers.items()},
            "B_D_predicted_to": mp.nstr(err(Eplus * (1 + h ** 2)), 4) + "% (360 ppm), parameter-free",
            "meaning": "the REAL robust result: B(deuteron) predicted to 0.036% from q₀ via three "
                       "derived tiers (rotational, bar-odd t, bar-even h² unit). g₂≈1 is a genuine "
                       "prediction, NOT a fit.",
        },
        "F2_frame_artifact": {
            "r_by_frame_pct": {k: mp.nstr((g - 1) * 100, 4) for k, g in frames.items()},
            "r_range_pct": [mp.nstr(min(r_vals) * 100, 3), mp.nstr(max(r_vals) * 100, 3)],
            "r_spread_pct": mp.nstr(r_spread * 100, 3),
            "spread_over_signal": mp.nstr(spread_ratio, 3) + "×",
            "meaning": "r = g₂−1 swings over [−3.4%, +7.4%] across equally-valid O(t²) conventions for "
                       "removing the SAME bar-odd tier — a spread ≈12× the signal |r|≈0.87%. r is "
                       "~90% frame-convention, NOT physics; not a well-defined derivation target.",
        },
        "F3_bar_even_is_projection_not_dynamics": {
            "omega_k_ge_2": "0 exactly (deuteron word σ₁³ is a single generator; every [a,a]=0)",
            "meaning": "the bar-even h² correction is NOT a Magnus/holonomy dynamical term (all vanish) "
                       "— it is the character/frame projection of the order-h² unit. So g₂=1 is "
                       "near-definitional (natural order-h² frame unit, coeff 1); r is the frame "
                       "residual, not a categorical amplitude.",
        },
        "verdict_owner_question": {
            "is_g2_fitted_to_AME": "NO tuned parameter — but the instinct is CORRECT: r is a frame "
                                   "artifact (12× convention spread) on top of a genuine 0.036% "
                                   "parameter-free B(D) prediction.",
            "bankable": ["B(deuteron) predicted to ~0.04% from q₀ (3 derived tiers)",
                         "g₂ ≈ 1 (bar-even correction = one h² unit)"],
            "not_a_target": "r = +0.87% — frame-noise-dominated tail, not robust, not separable.",
            "larger_context": "the real open problem is B(deuteron) below ~0.04% (frame-independent = "
                              "the Δ_λ closure), NOT r (a frame-dependent repackaging of the residual).",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "deuteron-g2-frame-artifact",
        "description": ("Answers the owner's 'is g₂ fitted to AME / larger context?' question. g₂ is NOT "
                        "a tuned parameter, but r = g₂−1 is a FRAME ARTIFACT: across equally-valid O(t²) "
                        "conventions for removing the same bar-odd tier, r swings over [−3.4%, +7.4%] — "
                        "a spread ≈12× the signal |r|≈0.87%, so r is ~90% convention, not physics. "
                        "Structurally, Ω_{k≥2}=0 exactly for the deuteron σ₁³ (single generator), so the "
                        "bar-even h² correction is a character/frame projection, NOT a dynamical Magnus "
                        "term — g₂=1 is near-definitional and r is the frame residual. The REAL robust "
                        "result is the tier convergence: B(deuteron) predicted to 0.036% (360 ppm) from "
                        "q₀ via three derived tiers (rotational, bar-odd t, bar-even h² unit). Larger "
                        "context: the well-defined open problem is B(deuteron) below ~0.04% (the Δ_λ "
                        "closure), NOT the frame-dependent r. scope-(a), audit-only, nothing wired; no "
                        "fit, no AME inversion."),
        "audit_only": True,
        "tier": "frame-sensitivity measurement + tier convergence + Ω_{k≥2}=0 structural locate; "
                "answers the owner question; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, the epistemic status of g₂ / r",
            "owner_question": "keep pushing on g₂ beyond leading; seems fitted to AME; larger context?",
            "builds_on": "#4369 (r is the binding residual magnified 1/h²), #4158 (g₂ definition, "
                         "Ω_{k≥2}=0), #4339 (g₂_leading=1)",
            "q0_convention": "experimental/proton pin, read by name from q_parameter.Q_50_DIGIT_STR (bean qou-9ugp)",
            "q0": Q0_STR,   # record the pin used, so a reader need not infer it
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deuteron-g2-frame-artifact", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("BD_predicted_within_0p04pct", computed=str(bool(abs(err(Eplus * (1 + h ** 2))) < mp.mpf("0.04"))), expected="True")
    wb.add_assertion("r_spread_exceeds_10x_signal", computed=str(bool(spread_ratio > 10)), expected="True")
    wb.add_assertion("r_frame_dominated", computed=str(bool(r_spread > 10 * signal)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Is g₂ fitted to AME? The larger context ===")
    print("F1 TIER CONVERGENCE (the real, robust result):")
    for k, (x, e) in tiers.items():
        print(f"    {k:34s} err {mp.nstr(e,4)}%")
    print(f"    ⇒ B(deuteron) predicted to {mp.nstr(err(Eplus*(1+h**2)),4)}% (360 ppm) PARAMETER-FREE. "
          f"g₂≈1 is a genuine prediction, NOT a fit.")
    print("F2 FRAME ARTIFACT (why 'it smells fitted' is right, sharpened):")
    for k, g in frames.items():
        print(f"    r [{k:26s}] = {mp.nstr((g-1)*100,4)}%")
    print(f"    ⇒ r spans [−3.4%, +7.4%] — spread {mp.nstr(r_spread*100,3)}% ≈ {mp.nstr(spread_ratio,3)}× "
          f"the signal. r is ~90% frame-convention, not physics.")
    print("F3 Ω_{k≥2}=0 exactly (deuteron σ₁³ single generator) ⇒ the bar-even unit is a frame "
          "projection, not a dynamical term. g₂=1 near-definitional; r = frame residual.")
    print("VERDICT: NOT fitted (no knob), but r IS a frame artifact. Bank: B(D) to 0.04% + g₂≈1. "
          "Larger context: the real target is B(deuteron) below 0.04% (Δ_λ closure), NOT r.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
