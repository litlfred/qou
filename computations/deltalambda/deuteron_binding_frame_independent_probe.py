#!/usr/bin/env python3
"""B(deuteron), frame-independent: the tier split (g₂, t) is convention; the frame-INVARIANT object is
the total correction C = B/(μ₀ℏ_q[3]_q[4]_q). Honest accuracy = spread of motivated single forms
(~0.5–0.8%, controlled at O(h)) — the 0.036% figure is resummation-flattered. Exact, forward, no fit.

CONTEXT (owner steer, 2026-07-26): "B(deuteron) in a frame-independent formulation." The prior audit
showed r = g₂−1 is a frame artifact (12× convention spread). This probe replaces the frame-dependent
tier decomposition with a single frame-invariant statement and reports its honest accuracy.

THE FRAME-INVARIANT FORMULATION:
  B(deuteron) = E₀ · C(q₀),   E₀ = μ₀·ℏ_q·[3]_q·[4]_q  (the naive q-deformed rotational Casimir),
  μ₀ = 2m_e/(3h),  ℏ_q = 1−q⁻¹,  h = q−q⁻¹,  [n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹).
  E₀ = 2.0195829 MeV (−9.215% vs AME 2.2245662). The total correction C = B/E₀ = 1.1014978 is the
  single frame-INVARIANT number the framework must predict — NO tier split, NO g₂, NO t.

FINDING 1 — a clean frame-invariant closed form. Because ℏ_q·q = q−1, the "×q" correction is
  B ≈ μ₀·(q−1)·[3]_q·[4]_q  (i.e. ℏ_q → its bar-conjugate q−1), err +0.77% — parameter-free, single
  closed form, no convention.

FINDING 2 — the HONEST frame-independent accuracy is ~0.5–0.8%, NOT 0.036%. Motivated single closed
forms for C and their errors on B:
    1 (naive q-Casimir)                     −9.215%
    1 + t + h²           (O(h²) additive)   −0.515%
    (1+t)(1+h²)          (O(h²) factored)   −0.308%
    exp(t)(1+h²)         (exp bar-odd)      −0.177%
    1/((1−t)(1−h²))      (both resummed)    +0.155%
    1/(1−t)·(1+h²)       (corpus resummed)  −0.036%
    q  (ℏ_q→q−1)         (bar-conj)         +0.770%
  The motivated-form error SPREAD is [−0.51%, +0.77%]. The prediction is controlled at O(h) (all
  frames agree through first order in t); the ~0.5% residual is the frame/resummation-dependent tail.
  The 0.036% figure requires the SPECIFIC (1+h²)/(1−t) resummation — it is resummation-flattered, NOT
  a frame-independent accuracy (Lean: FrameAmbiguitySecondOrder.frame_diff_second_order — competing
  resummations differ at O(t²)=O(h²), the same order as the whole bar-even signal).

VERDICT (scope-(a), answers the owner). Frame-independent statement: the framework predicts the
deuteron binding parameter-free to ~0.5% (a ~20× improvement over the naive q-Casimir's 9.2%),
controlled at O(h); the sub-0.1% accuracy and the coefficient g₂ = 1.0087 are NOT additional genuine
precision — they are one resummation's frame-flattered residual (the O(h²) frame ambiguity, Lean-
proved). The real, well-posed observable is C = B/E₀ = 1.1015 (or B/μ₀ = 1.3652); the real open
problem is predicting C below ~0.5% by a DERIVED (not resummation-chosen) higher-order structure —
i.e. the Δ_λ closure, frame-independently.

EXPLORATORY — audit + witness only. scope-(a); nothing wired; no fit, no AME inversion (E_AME/AME
enter only to expose the frame-invariant correction and calibrate accuracy, exactly as the corpus
defines the −9.2% gap).
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
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

Q0_STR = _Q0_RESOLVED
ME_MEV = "0.51099895000"
B_AME = _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)


def main() -> int:
    q = mp.mpf(Q0_STR)
    h = q - 1 / q
    hbar = 1 - 1 / q
    v = mp.sqrt(q)
    me = mp.mpf(ME_MEV)
    mu0 = 2 * me / (3 * h)
    B = mp.mpf(B_AME)

    def qn(n):
        return (q ** n - q ** (-n)) / (q - 1 / q)

    E0 = mu0 * hbar * qn(3) * qn(4)          # naive q-Casimir (frame-invariant)
    C = B / E0                                # total frame-invariant correction
    t = (v - 1 / v) / (v + 1 / v)

    # ℏ_q·q = q−1 identity (the clean ×q form)
    hbar_q_eq_qm1 = abs(hbar * q - (q - 1)) < mp.mpf("1e-38")

    forms = {
        "1 (naive q-Casimir)": mp.mpf(1),
        "1 + t + h^2  (O(h^2) additive)": 1 + t + h ** 2,
        "(1+t)(1+h^2)  (O(h^2) factored)": (1 + t) * (1 + h ** 2),
        "exp(t)(1+h^2)  (exp bar-odd)": mp.e ** t * (1 + h ** 2),
        "1/((1-t)(1-h^2))  (both resummed)": 1 / ((1 - t) * (1 - h ** 2)),
        "1/(1-t)(1+h^2)  (corpus resummed)": (1 + h ** 2) / (1 - t),
        "q  (hbar->q-1, bar-conj)": q,
    }
    errs = {name: float((val * E0 - B) / B * 100) for name, val in forms.items()}
    motivated = {k: e for k, e in errs.items() if "naive" not in k}
    spread_lo, spread_hi = min(motivated.values()), max(motivated.values())
    honest_acc = max(abs(spread_lo), abs(spread_hi))

    result = {
        "frame_invariant_formulation": {
            "B_eq": "B(deuteron) = E₀·C,  E₀ = μ₀·ℏ_q·[3]_q·[4]_q  (naive q-Casimir)",
            "E0_MeV": mp.nstr(E0, 8) + f"  (err {mp.nstr((E0-B)/B*100,4)}%)",
            "C_total_correction": mp.nstr(C, 8) + "  (= B/E₀, the single frame-INVARIANT number)",
            "B_over_mu0": mp.nstr(B / mu0, 8) + "  (equivalent frame-invariant target)",
            "no_tier_split": "C carries NO g₂, NO t — those are frame-dependent decompositions of C.",
        },
        "F1_clean_closed_form": {
            "hbar_q_times_q_eq_q_minus_1": bool(hbar_q_eq_qm1),
            "form": "B ≈ μ₀·(q−1)·[3]_q·[4]_q  (ℏ_q → bar-conjugate q−1)",
            "err_pct": mp.nstr(errs["q  (hbar->q-1, bar-conj)"], 4),
            "meaning": "a single parameter-free frame-invariant closed form, err +0.77%.",
        },
        "F2_honest_accuracy": {
            "motivated_form_errors_pct": {k: mp.nstr(e, 4) for k, e in errs.items()},
            "motivated_spread_pct": [mp.nstr(spread_lo, 3), mp.nstr(spread_hi, 3)],
            "frame_independent_accuracy_pct": "~" + mp.nstr(honest_acc, 2),
            "controlled_order": "O(h) — all frames agree through first order in t",
            "resummation_flattered": "the 0.036% figure needs the SPECIFIC (1+h²)/(1−t) resummation; "
                                     "competing resummations differ at O(t²)=O(h²) (Lean-proved) — the "
                                     "same order as the whole bar-even signal, so 0.036% is NOT a "
                                     "frame-independent accuracy.",
        },
        "verdict": {
            "frame_independent_statement": "the framework predicts B(deuteron) parameter-free to ~0.5% "
                                           "(a ~20× improvement over the naive q-Casimir's 9.2%), "
                                           "controlled at O(h).",
            "g2_precision_is_artifact": "the sub-0.1% accuracy and g₂ = 1.0087 are one resummation's "
                                        "frame-flattered residual (O(h²) frame ambiguity, Lean-proved), "
                                        "NOT additional genuine precision.",
            "real_target": "predict C = B/E₀ = 1.1015 below ~0.5% by a DERIVED higher-order structure "
                           "(not a chosen resummation) — the Δ_λ closure, frame-independently.",
            "lean": "QOU/MassTheory/FrameAmbiguitySecondOrder.lean (frame_diff_second_order, "
                    "g_frame_difference)",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "deuteron-binding-frame-independent",
        "description": ("Frame-independent formulation of B(deuteron), answering the owner steer. The "
                        "frame-INVARIANT object is the total correction C = B/(μ₀ℏ_q[3]_q[4]_q) = "
                        "1.1015 (or B/μ₀ = 1.3652) — no tier split, no g₂, no t. A clean parameter-free "
                        "closed form is B ≈ μ₀(q−1)[3]_q[4]_q (ℏ_q→q−1), err +0.77%. The HONEST frame-"
                        "independent accuracy is the spread of motivated single forms, [−0.51%, +0.77%] "
                        "→ ~0.5%, controlled at O(h); the 0.036% figure and g₂=1.0087 are resummation-"
                        "flattered (competing bar-odd resummations differ at O(t²)=O(h²), Lean-proved "
                        "FrameAmbiguitySecondOrder), NOT frame-independent precision. So: the framework "
                        "predicts B(deuteron) parameter-free to ~0.5% (20× over the naive q-Casimir's "
                        "9.2%); the real open target is C below ~0.5% by a DERIVED higher-order "
                        "structure (the Δ_λ closure), not a chosen resummation. scope-(a), audit-only, "
                        "nothing wired; no fit."),
        "audit_only": True,
        "tier": "frame-invariant reformulation + motivated-form accuracy spread + Lean-proved O(t²) "
                "frame ambiguity; answers the owner steer; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, frame-independent B(deuteron)",
            "owner_steer": "B(deuteron) in a frame-independent formulation",
            "lean": "QOU/MassTheory/FrameAmbiguitySecondOrder.lean",
            "builds_on": "#4369 (r = frame artifact / binding residual magnified 1/h²), #4158 (tiers)",
            "q0_convention": "experimental/proton pin, read by name from q_parameter.Q_50_DIGIT_STR (bean qou-9ugp)",
            "q0": Q0_STR,   # record the pin used, so a reader need not infer it
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deuteron-binding-frame-independent", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("hbar_q_times_q_eq_q_minus_1", computed=str(bool(hbar_q_eq_qm1)), expected="True")
    wb.add_assertion("clean_form_xq_err_under_1pct", computed=str(bool(abs(errs["q  (hbar->q-1, bar-conj)"]) < 1)), expected="True")
    wb.add_assertion("honest_accuracy_is_subpercent_not_subtenth", computed=str(bool(0.3 < honest_acc < 1.0)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== B(deuteron), frame-independent ===")
    print(f"B = E₀·C,  E₀ = μ₀ℏ_q[3]_q[4]_q = {mp.nstr(E0,8)} ({mp.nstr((E0-B)/B*100,4)}%);  "
          f"C = B/E₀ = {mp.nstr(C,8)}  (frame-INVARIANT, no tier split)")
    print(f"F1 clean form: B ≈ μ₀(q−1)[3]_q[4]_q  (ℏ_q·q=q−1: {hbar_q_eq_qm1}), err "
          f"{mp.nstr(errs['q  (hbar->q-1, bar-conj)'],4)}%")
    print("F2 motivated single-form errors on B:")
    for k, e in errs.items():
        print(f"     {k:38s} {mp.nstr(e,4)}%")
    print(f"   spread [{mp.nstr(spread_lo,3)}%, {mp.nstr(spread_hi,3)}%] ⇒ honest frame-independent "
          f"accuracy ~{mp.nstr(honest_acc,2)}% (controlled at O(h))")
    print("VERDICT: framework predicts B(deuteron) parameter-free to ~0.5% (20× over naive q-Casimir). "
          "0.036% + g₂=1.0087 are resummation-flattered (O(h²) frame ambiguity, Lean-proved), NOT real "
          "precision. Real target: C=1.1015 below 0.5% via DERIVED structure. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
