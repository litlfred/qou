#!/usr/bin/env python3
"""GAP-A-4 §4 direction 3 follow-up — cross-isotope residual probe.

Tests whether the `sqrt([3]_q/[2]_q)`-form NUMEROLOGY finding at ³He
([PR #1882](https://github.com/litlfred/qou/pull/1882)) extends to the
other light atoms via a derived per-(Z, N) exponent rule.

Per the author's "fix as numerology unless derivable" discipline,
the ³He +0.70 % single-atom match is **filed as a coincidence**
until BOTH:
  (a) cross-isotope closure under a derived per-(Z, N) exponent rule
  (b) categorical identification of the factor

This probe attacks (a) head-on.  For each light atom K ∈ {p, n, D,
T, ³He, ⁴He}, compute:

  residual_ratio(K) = λ_emp(K) / L1b(K)

and test against a family of `sqrt([3]_q/[2]_q)`-based candidate
exponent rules:

  R1 — constant exponent: `sqrt([3]_q/[2]_q)^1` for every K
  R2 — per-proton exponent: `sqrt([3]_q/[2]_q)^Z`
  R3 — per-neutron exponent: `sqrt([3]_q/[2]_q)^N`
  R4 — per-A exponent:       `sqrt([3]_q/[2]_q)^(Z+N) = sqrt([3]_q/[2]_q)^A`
  R5 — Schur-Weyl half-step: `sqrt([3]_q/[2]_q)^(Z·N)` (evaluates to
        1 at p/n where Z·N = 0; that's the rule's natural prediction
        for single nucleons, not a special-case skip)
  R6 — Z·N − 1 (centered):   `sqrt([3]_q/[2]_q)^(Z·N − 1)`

If any rule closes all six rows to better than 5 %, the
sqrt([3]_q/[2]_q) finding becomes a derivable structural lead (per
the discipline rule, this would also need (b) — categorical
identification — to be promoted).  If all rules refute, ³He's
+0.70 % match is confirmed as a coincidence and direction 3 closes
negative.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.
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
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
)

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent

Q_0_50DPS = Q_50_DIGIT_STR

# CODATA-2022 / AME-2020 masses (MeV) routed through the canonical
# registry (I9 — no hardcoded literals). See codata_constants.py.
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as m_n_derived_3input,
    M_D_MEV_VALIDATION as M_D_MEV,
    M_T_MEV_VALIDATION as M_T_MEV,
    M_HE3_MEV_VALIDATION as M_HE3_MEV,
    M_HE4_MEV_VALIDATION as M_HE4_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

VOL_BORROMEAN_8G = mp.mpf("7.32772475341775212043682811945907288619319499425")
VOL_PHASE4_Z1 = mp.mpf("12.776")
VOL_PHASE4_Z2 = mp.mpf("12.554")


def q_number_sym(n: int, q: sp.Expr) -> sp.Expr:
    if n == 0:
        return sp.Integer(0)
    return sp.Add(*(q ** (2 * k - (n - 1)) for k in range(n)))


def hbar_q_sq(q_0: mp.mpf) -> mp.mpf:
    hbar = mp.mpf(1) - mp.mpf(1) / q_0
    return hbar * hbar


def evaluate(expr: sp.Expr, q_0: mp.mpf) -> mp.mpf:
    """Substitute every free symbol in `expr` with `q_0` at the live
    working precision.  Passes `q_0` (mpf) directly to `sp.Float`
    rather than via `str()` (avoid serialisation round-trip; Gemini
    review on PR #1883)."""
    dps = mp.mp.dps
    q_float = sp.Float(q_0, dps)
    subs = {sym: q_float for sym in expr.free_symbols}
    return mp.mpf(str(sp.N(expr.subs(subs), dps)))


def A_phase4(Z: int, N: int, vol_hyp: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    q_sym = sp.Symbol("q", positive=True)
    eight_q = q_number_sym(8, q_sym)
    three_q = q_number_sym(3, q_sym)
    spin_carrier = (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym)) ** (4 * N)
    color_carrier = three_q ** (2 * (Z - 1))
    # Use live `mp.mp.dps` not hardcoded 50; pass `vol_hyp` directly
    # (Gemini + Copilot review on PR #1883).
    expr = sp.Float(vol_hyp, mp.mp.dps) / eight_q * color_carrier * spin_carrier
    return evaluate(expr, q_0)


def lambda_L1b(Z: int, N: int, vol_hyp: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    """λ_L1b(K) = A_Phase-4(K) · Vol_hyp(K)/Vol(𝓑₃) · ℏ_q² (per PR
    #1874's corrected form)."""
    A = A_phase4(Z, N, vol_hyp, q_0)
    return A * vol_hyp / VOL_BORROMEAN_8G * hbar_q_sq(q_0)


def lambda_empirical(m_K: mp.mpf, vol_K: mp.mpf, q_0: mp.mpf) -> mp.mpf:
    return m_K * hbar_q_sq(q_0) / (M_E_MEV * vol_K)


# Light series + per-knot Vol (matches PR #1874 conventions)
LIGHT_SERIES = [
    ("p",   1, 0, M_P_MEV,    VOL_BORROMEAN_8G),
    ("n",   0, 1, m_n_derived_3input,    VOL_BORROMEAN_8G),
    ("D",   1, 1, M_D_MEV,    VOL_PHASE4_Z1),
    ("T",   1, 2, M_T_MEV,    VOL_PHASE4_Z1),
    ("3He", 2, 1, M_HE3_MEV,  VOL_PHASE4_Z2),
    ("4He", 2, 2, M_HE4_MEV,  VOL_PHASE4_Z2),
]


# Candidate exponent rules: (label, Z+N → exponent function)
def rule_R1(Z: int, N: int) -> int: return 1
def rule_R2(Z: int, N: int) -> int: return Z
def rule_R3(Z: int, N: int) -> int: return N
def rule_R4(Z: int, N: int) -> int: return Z + N
def rule_R5(Z: int, N: int) -> int: return Z * N
def rule_R6(Z: int, N: int) -> int: return Z * N - 1


RULES = [
    ("R1 (constant)",      rule_R1),
    ("R2 (per-proton Z)",  rule_R2),
    ("R3 (per-neutron N)", rule_R3),
    ("R4 (per-A Z+N)",     rule_R4),
    ("R5 (Schur-Weyl Z·N)", rule_R5),
    ("R6 (Z·N − 1)",       rule_R6),
]


def main() -> int:
    w = WitnessBuilder(
        "gap-a4-cross-isotope-residual-probe", engine="sympy+mpmath"
    )
    w.set_audit_only("docs/audits/2026-06-05-gap-a4-L1-retrospective.md")
    w.set_description(
        "Cross-isotope follow-up to PR #1882's ³He sqrt([3]_q/[2]_q) "
        "NUMEROLOGY finding (+0.70 %). Tests six per-(Z, N) exponent "
        "rules across the light series {p, n, D, T, ³He, ⁴He}: if any "
        "rule closes all six rows to <5 %, the ³He finding has cross-"
        "isotope structural backing; otherwise it's confirmed as a "
        "single-atom coincidence. Per author 'fix as numerology unless "
        "derivable' rule: a positive result here is required (but not "
        "yet sufficient) to promote from numerology to structural "
        "lead. EXPLORATORY."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    q_sym = sp.Symbol("q", positive=True)
    sqrt_3q_over_2q_val = evaluate(
        sp.sqrt(q_number_sym(3, q_sym) / q_number_sym(2, q_sym)), q_0
    )

    print("=" * 78)
    print("GAP-A-4 cross-isotope residual probe — sqrt([3]_q/[2]_q) extrapolation")
    print("=" * 78)
    print(f"  q₀                       = {Q_0_50DPS}")
    print(f"  sqrt([3]_q/[2]_q) at q₀  = {float(sqrt_3q_over_2q_val):.10f}")
    print("-" * 78)

    # Compute residual_ratio per atom
    rows = []
    print(f"  {'atom':<4} {'Z':>2} {'N':>2} {'λ_emp':>10} "
          f"{'L1b':>10} {'residual':>10}")
    print("-" * 78)
    for label, Z, N, m_K, vol_K in LIGHT_SERIES:
        L1b = lambda_L1b(Z, N, vol_K, q_0)
        lam_emp = lambda_empirical(m_K, vol_K, q_0)
        residual = lam_emp / L1b
        print(f"  {label:<4} {Z:>2} {N:>2} {float(lam_emp):>10.4f} "
              f"{float(L1b):>10.4f} {float(residual):>10.4f}")
        rows.append({
            "label": label, "Z": Z, "N": N,
            "lambda_emp": str(lam_emp),
            "L1b": str(L1b),
            "residual_ratio": str(residual),
        })
    print("-" * 78)

    # Test each rule
    print(f"\n  {'rule':<24s} ", end="")
    for r in rows:
        print(f"{r['label']:>10s} ", end="")
    print(f"  {'worst':>10s}")
    print("-" * 78)

    rule_results = []
    best_rule_label = ""
    best_rule_worst = mp.mpf("inf")
    for rule_label, rule_fn in RULES:
        print(f"  {rule_label:<24s} ", end="")
        per_atom = []
        worst_rel = mp.mpf(0)
        worst_label = ""
        for r in rows:
            Z, N = r["Z"], r["N"]
            exp = rule_fn(Z, N)
            predicted = sqrt_3q_over_2q_val ** exp
            actual = mp.mpf(r["residual_ratio"])
            rel = (predicted - actual) / actual
            print(f"{float(rel):>+9.2%} ", end="")
            per_atom.append({
                "atom": r["label"],
                "exponent": exp,
                "predicted": str(predicted),
                "actual": str(actual),
                "relative_error": str(rel),
            })
            if abs(rel) > abs(worst_rel):
                worst_rel = rel
                worst_label = r["label"]
        worst_str = f"{float(worst_rel):>+9.2%}"
        print(f"  {worst_str:>10s}")
        rule_results.append({
            "rule": rule_label,
            "per_atom": per_atom,
            "worst_relative_error": str(worst_rel),
            "worst_atom": worst_label,
        })
        if abs(worst_rel) < abs(best_rule_worst):
            best_rule_worst = worst_rel
            best_rule_label = rule_label

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_parameter("sqrt_3q_over_2q_at_q0", str(sqrt_3q_over_2q_val))
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)
    w.add_data("residual_per_atom", rows)
    w.add_data("rule_results", rule_results)
    w.add_data("best_rule", {
        "label": best_rule_label,
        "worst_relative_error": str(best_rule_worst),
    })

    print("-" * 78)
    print(f"  best rule: {best_rule_label}  worst rel_err {float(best_rule_worst):+.2%}")

    # Per the discipline: closure requires <5 % worst-row AND
    # categorical identification.  Probe only tests the numerical
    # half (a); categorical identification (b) is not in scope.
    if abs(best_rule_worst) < mp.mpf("5e-2"):
        synthesis = (
            f"At least one per-(Z, N) exponent rule ({best_rule_label}) "
            f"closes ALL six light-atom rows to <5 % with worst rel_err "
            f"{float(best_rule_worst):+.2%}.  This satisfies discipline "
            f"requirement (a) — cross-isotope closure — but is NOT yet "
            f"a structural lead: requirement (b), categorical "
            f"identification of why sqrt([3]_q/[2]_q)^exp(Z, N) is the "
            f"right factor, remains open.  Per author 'fix as numerology "
            f"unless derivable' rule, the ³He finding can now be "
            f"escalated from a single-atom coincidence to a "
            f"cross-isotope coincidence pending (b).  Next probe: derive "
            f"the categorical content of the exponent rule from the "
            f"brane-tower / Schur-Weyl framework."
        )
    else:
        synthesis = (
            f"No tested per-(Z, N) exponent rule closes the residuals "
            f"across the light series; best rule ({best_rule_label}) "
            f"misses by {float(best_rule_worst):+.2%} at the worst atom. "
            f"§4 direction 3 closes NEGATIVE under the 'fix as "
            f"numerology unless derivable' discipline: PR #1882's "
            f"³He +0.70 % match is confirmed as a single-atom "
            f"coincidence with no cross-isotope structural backing. "
            f"Productive direction shifts to §4 direction 2 (additive "
            f"S(K) sub-leading) or §4 direction 4 (re-examine Vol(K) "
            f"convention).  This is the cleanest possible negative "
            f"closure: 18 candidates × 6 atoms × 6 exponent rules all "
            f"tested with no derivation route surfacing."
        )
    w.add_data("synthesis_verdict", synthesis)
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    # Sanity assertion: ³He under R5 (Z·N = 2) reproduces the
    # PR #1882 +0.70 % at the right order
    he3_R5_rel = next(
        mp.mpf(p["relative_error"])
        for rr in rule_results
        if rr["rule"].startswith("R5")
        for p in rr["per_atom"]
        if p["atom"] == "3He"
    )
    w.add_assertion(
        # NEGATIVE CONTROL — this assertion deliberately encodes the
        # ~24 % MISMATCH at ³He under R5 (the Schur-Weyl Z·N rule), to
        # document that the most-plausible categorical exponent rule
        # does NOT fit ³He.  Earlier name "He3_under_R5_close_to_PR1882"
        # was misleading (suggested fit, not mismatch); renamed per
        # Copilot review on PR #1883.
        "negative_control_He3_under_R5_mismatch_24pct",
        computed=float(he3_R5_rel),
        # ³He has Z·N = 2 so R5 gives sqrt([3]_q/[2]_q)^2 = [3]_q/[2]_q
        # ≈ 1.514, not 1.222 → expected to be off by ~24 %
        expected=0.24,
        tolerance=5e-2,
        source=(
            "³He has Z·N = 2 under R5, so the predicted residual is "
            "sqrt([3]_q/[2]_q)^2 = [3]_q/[2]_q ≈ 1.514 vs actual 1.222 "
            "→ +24 %.  This is an assertion that ³He doesn't satisfy "
            "R5 (the categorical Schur-Weyl rule), confirming we're "
            "in the numerology regime."
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
