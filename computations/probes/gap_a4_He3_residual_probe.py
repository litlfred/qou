#!/usr/bin/env python3
"""GAP-A-4 §4 direction 3 — ³He L1b residual structural probe.

Investigates the post-#1874 finding: L1b's ³He row was the ONLY
single-atom NEAR-MATCH (<25 %) in the entire L1 6×3 grid:

  L1b(³He) = A_Phase-4(³He) · Vol_hyp(³He)/Vol(𝓑₃) · ℏ_q² = 3.5177
  λ_emp(³He) = m(³He)·ℏ_q²/(m_e·Vol(³He)) = 4.2978
  residual_ratio = λ_emp / L1b = 1.2218

§4 direction 3 of [`docs/audits/2026-06-05-gap-a4-L1-retrospective.md`](../../docs/audits/2026-06-05-gap-a4-L1-retrospective.md):

  *"Compute L1b's per-(Z, N) contributions at the ³He row in
   isolation; see whether the -18.15 % residual factors as a clean
   substrate quantity (e.g. q-deformed mass-ratio correction).
   If yes, that's the structural lead."*

The probe tests ~15 closed-form substrate quantities at q₀ against
1.2218 and reports the best match.  No fitting; each candidate is a
fixed closed-form expression.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-He3-residual-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

from pathlib import Path

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402
from closed_form_tau_M import compute_tau_M_nucleon_H3, closed_form_tau_M  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = Q_50_DIGIT_STR

M_E_MEV = mp.mpf("0.51099895069")
M_P_MEV = mp.mpf(M_P_MEV_VALIDATION)  # CODATA validation (codata_constants registry)
M_N_MEV = mp.mpf(M_N_MEV_VALIDATION)  # CODATA validation (codata_constants registry)
M_HE3_MEV = mp.mpf("2808.39160743")
VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z2 = mp.mpf("12.554")


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    # `sp.Add(*...)` builds the sum in one efficient step instead of
    # `sum()`'s n-1 sequential pairwise additions (Gemini review on
    # PR #1882).
    return sp.Add(*(q ** (2 * k - (n - 1)) for k in range(n)))


def linking_weight_family_a_sym(q: sp.Expr) -> sp.Expr:
    return (3 * q ** 2 + 4 + 3 * q ** (-2)) / 4


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def evaluate(expr: sp.Expr, q_0: mp.mpf) -> mp.mpf:
    """Substitute every free symbol in `expr` with `q_0` and return
    the numerical value at the working precision.

    Robust to the symbol's exact `Symbol(...)` instance (substitutes
    every free symbol, not a freshly-constructed `Symbol('q')` —
    Copilot review on PR #1882).  Substitution + final precision both
    follow the live mp.mp.dps so this stays in sync with the probe's
    `set_compute_dps()` (Copilot review on PR #1882).
    """
    dps = mp.mp.dps
    q_float = sp.Float(str(q_0), dps)
    subs = {sym: q_float for sym in expr.free_symbols}
    return mp.mpf(str(sp.N(expr.subs(subs), dps)))


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-He3-residual-probe", engine="sympy+mpmath"
    )
    w.set_audit_only("docs/audits/2026-06-05-gap-a4-L1-retrospective.md")
    w.set_description(
        "GAP-A-4 §4 direction 3 probe: investigate the L1b ³He "
        "-18.15 % NEAR-MATCH (the only sub-25 % row in PR #1874's "
        "6×3 grid).  Tests ~15 closed-form substrate quantities "
        "against the residual_ratio λ_emp/L1b = 1.2218 to see if a "
        "clean structural factor explains the gap.  No fitting; "
        "each candidate is a fixed closed-form expression at q₀."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    q_sym = sp.Symbol("q", positive=True)

    # Compute L1b(³He) and λ_emp(³He) precisely
    A_he3 = (VOL_PHASE4_Z2 / evaluate(q_number_sym(8, q_sym), q_0)
             * evaluate(q_number_sym(3, q_sym) ** 2, q_0)
             * evaluate((sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** 4, q_0))
    L1b_he3 = A_he3 * VOL_PHASE4_Z2 / VOL_BORROMEAN_8G * hbar_q_sq(q_0)
    lambda_emp_he3 = M_HE3_MEV * hbar_q_sq(q_0) / (M_E_MEV * VOL_PHASE4_Z2)
    residual_ratio = lambda_emp_he3 / L1b_he3

    tau_p_H3 = compute_tau_M_nucleon_H3("p", q_0)
    tau_n_H3 = compute_tau_M_nucleon_H3("n", q_0)
    tr_M_he3 = closed_form_tau_M(2, 1, q_0, tau_p_H3, tau_n_H3)

    print("=" * 78)
    print("GAP-A-4 §4 direction 3 — ³He L1b residual structural probe")
    print("=" * 78)
    print(f"  A_Phase-4(³He)             = {float(A_he3):.10f}")
    print(f"  L1b(³He)                   = {float(L1b_he3):.10f}")
    print(f"  λ_emp(³He)                 = {float(lambda_emp_he3):.10f}")
    print(f"  residual_ratio = λ_emp/L1b = {float(residual_ratio):.10f}")
    print(f"  (matches PR #1874's -18.15 % verdict: "
          f"1 - 1/r = {float(1 - 1/residual_ratio):.4%})")

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("A_phase4_He3", str(A_he3))
    w.add_parameter("L1b_He3", str(L1b_he3))
    w.add_parameter("lambda_emp_He3", str(lambda_emp_he3))
    w.add_parameter("residual_ratio", str(residual_ratio))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data(
        "scope_doc",
        "docs/audits/2026-06-05-gap-a4-L1-retrospective.md",
    )

    print("-" * 78)
    print(f"  {'candidate':<32s} {'value':>14s} {'rel_err':>10s} {'verdict':>14s}")
    print("-" * 78)

    candidates = [
        ("tr_M(³He)",                        tr_M_he3),
        ("q_0",                              q_sym),
        ("q_0**2",                           q_sym ** 2),
        ("q_0**(1/2)",                       sp.sqrt(q_sym)),
        ("[2]_q",                            q_number_sym(2, q_sym)),
        ("[3]_q",                            q_number_sym(3, q_sym)),
        ("[4]_q",                            q_number_sym(4, q_sym)),
        ("[3]_q/[2]_q",                      q_number_sym(3, q_sym) / q_number_sym(2, q_sym)),
        ("[4]_q/[3]_q",                      q_number_sym(4, q_sym) / q_number_sym(3, q_sym)),
        ("sqrt([3]_q/[2]_q)",                sp.sqrt(q_number_sym(3, q_sym) / q_number_sym(2, q_sym))),
        ("(q^(1/2) + q^(-1/2))/2",           (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) / 2),
        ("(q^(1/2) + q^(-1/2))/[2]_q",       (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) / q_number_sym(2, q_sym)),
        ("linking_weight/2",                 linking_weight_family_a_sym(q_sym) / 2),
        ("(linking_weight/[2]_q)^(1/2)",     sp.sqrt(linking_weight_family_a_sym(q_sym) / q_number_sym(2, q_sym))),
        ("6/5  (Catalan-like rational)",     sp.Rational(6, 5)),
        ("[3]_q^(1/4)·q_0^(1/2)",            q_number_sym(3, q_sym) ** sp.Rational(1, 4) * sp.sqrt(q_sym)),
    ]

    # Mass-ratio candidates (substrate-free; included for completeness).
    # `log(residual)/log(m_n/m_p) ≈ 145.4`, so the ratio CAN be
    # numerically reproduced by `(m_n/m_p)^145` to better than 0.1 %
    # — but 145 is a large ad-hoc integer with no categorical
    # justification, exactly the numerology the §6 discipline warns
    # against (Copilot review on PR #1882 caught the original 160/145
    # mismatch).  The low-power `m_n/m_p` IS included to confirm the
    # residual is NOT a simple O(1) mass-ratio correction (the high
    # exponent IS that confirmation).  The high-power case is
    # deliberately omitted.
    mass_candidates_num: list[tuple[str, mp.mpf]] = [
        ("m_n / m_p",      M_N_MEV / M_P_MEV),
        ("VOL(³He)/VOL(𝓑₃) · ℏ_q²",
                           VOL_PHASE4_Z2 / VOL_BORROMEAN_8G * hbar_q_sq(q_0)),
    ]

    results = []
    best_label = ""
    best_rel = mp.mpf("inf")
    for label, expr in candidates:
        if isinstance(expr, mp.mpf):
            val = expr
        else:
            val = evaluate(expr, q_0)
        rel = (val - residual_ratio) / residual_ratio
        if abs(rel) < mp.mpf("5e-3"):
            verdict = "EXACT-MATCH (<0.5%)"
        elif abs(rel) < mp.mpf("5e-2"):
            verdict = "NEAR-MATCH (<5%)"
        elif abs(rel) < mp.mpf("0.25"):
            verdict = "NEAR-MATCH (<25%)"
        else:
            verdict = "REFUTED"
        if abs(rel) < abs(best_rel):
            best_rel = rel
            best_label = label
        print(f"  {label:<32s} {float(val):>14.6f} {float(rel):>+10.2%} {verdict:>14s}")
        results.append({
            "label": label,
            "value_at_q0": str(val),
            "relative_error": str(rel),
            "verdict": verdict,
        })

    for label, val in mass_candidates_num:
        rel = (val - residual_ratio) / residual_ratio
        if abs(rel) < mp.mpf("5e-3"):
            verdict = "EXACT-MATCH (<0.5%)"
        elif abs(rel) < mp.mpf("5e-2"):
            verdict = "NEAR-MATCH (<5%)"
        elif abs(rel) < mp.mpf("0.25"):
            verdict = "NEAR-MATCH (<25%)"
        else:
            verdict = "REFUTED"
        if abs(rel) < abs(best_rel):
            best_rel = rel
            best_label = label
        print(f"  {label:<32s} {float(val):>14.6f} {float(rel):>+10.2%} {verdict:>14s}")
        results.append({
            "label": label,
            "value_at_q0": str(val),
            "relative_error": str(rel),
            "verdict": verdict,
        })

    w.add_data("candidates", results)
    w.add_data("best_candidate", {
        "label": best_label,
        "relative_error": str(best_rel),
    })

    print("-" * 78)
    print(f"  best candidate: {best_label}  rel_err {float(best_rel):+.2%}")

    if abs(best_rel) < mp.mpf("5e-3"):
        synthesis = (
            f"The ³He L1b residual ratio {float(residual_ratio):.6f} "
            f"matches the substrate quantity '{best_label}' to "
            f"<0.5 %.  **Filed as NUMEROLOGY**: this is a single-atom "
            f"numerical coincidence pending a categorical derivation. "
            f"Per the author's 'fix as numerology unless derivable' "
            f"rule, the match becomes a 'structural lead' only when "
            f"(a) the same factor closes the corresponding L1b "
            f"residuals at D, T, ⁴He under a derived per-(Z, N) "
            f"exponent rule, AND (b) the categorical content of the "
            f"factor (e.g. a half-step Schur-Weyl projection or a "
            f"q-Plancherel weight) is identified.  Until both, this "
            f"is a coincidence."
        )
    elif abs(best_rel) < mp.mpf("5e-2"):
        synthesis = (
            f"The ³He L1b residual {float(residual_ratio):.6f} is "
            f"within 5 % of '{best_label}' but not exact (rel_err "
            f"{float(best_rel):+.2%}).  **Filed as NUMEROLOGY**: a "
            f"non-exact near-match is by definition suggestive but "
            f"not derivative.  The 'fix as numerology unless "
            f"derivable' discipline requires (a) cross-isotope "
            f"closure under a derived per-(Z, N) exponent rule and "
            f"(b) categorical identification of the factor before "
            f"this can be promoted to a structural lead.  Until both, "
            f"this is a coincidence and direction 3 doesn't close "
            f"productively at the single-atom layer."
        )
    else:
        synthesis = (
            f"No tested substrate quantity matches the ³He L1b "
            f"residual {float(residual_ratio):.6f} to better than 5 %. "
            f"Closest match: '{best_label}' at rel_err "
            f"{float(best_rel):+.2%}.  §4 direction 3 closes as a "
            f"clean negative: the L1b ³He NEAR-MATCH is NOT a "
            f"single-factor substrate residual; it's either a "
            f"coincidence at this single atom or a sum of competing "
            f"factors that don't decompose cleanly.  Productive "
            f"direction shifts to §4 direction 2 (additive S(K) "
            f"sub-leading) or §4 direction 4 (re-examine Vol(K) "
            f"convention)."
        )
    w.add_data("synthesis_verdict", synthesis)
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Sanity assertion: L1b reproduces the PR #1874 -18.15 % rel_err
    pr1874_rel_err = (L1b_he3 - lambda_emp_he3) / lambda_emp_he3
    w.add_assertion(
        "L1b_He3_matches_PR1874_value",
        computed=float(pr1874_rel_err),
        expected=-0.1815,
        tolerance=2e-3,
        source=(
            "Sanity check: this probe re-derives L1b(³He) from the "
            "Phase-4 formula and should reproduce PR #1874's -18.15 % "
            "rel_err verdict to better than 0.2 %."
        ),
    )

    out_path = w.save()
    repo_root = COMPUTE_DIR.parent.parent
    try:
        rel = out_path.relative_to(repo_root)
    except ValueError:
        rel = out_path
    print(f"\nWrote witness: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
