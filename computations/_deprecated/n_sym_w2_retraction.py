#!/usr/bin/env python3
"""W-2 retraction probe — multi-q verification refutes the 62 ppm "closure".

Background.
The earlier W-2 refinement probe (n_sym_b8_refinement_probe.py) found
that

    [3]_q · [4]_q² · [2]_q² · ([4]_q − h³) / 4  =  213.099  (at q = q_0)

matches the W-2 numerical anchor N_sym(q_0) = 213.111807 to 6.2e-5
relative deviation (62 ppm).  This was reported as a "W-2 closure to
62 ppm" in commit 275abb9b6.

The claim is wrong.  Verification at multiple q values shows the
ansatz is point-fit numerology:

  q                   N_sym(q)        ansatz(q)       rel_err
  -----------------------------------------------------------
  0.95 q_0            283.481         197.321         -30.4%
  0.99 q_0            228.531         209.116          -8.5%
  q_0                 213.112         213.099         -0.006%   (point fit)
  1.01 q_0            197.591         217.502         +10.1%
  1.05 q_0            138.674         239.507         +72.7%
  1/q_0               213.112         214.048         +0.44%

Two failures expose the issue:
  1.  N_sym(q) is q ↔ q⁻¹ symmetric (213.112 at both q_0 and 1/q_0)
      because it is built from [n]_q (q-symmetric).  My ansatz
      contains h³ = (q − q⁻¹)³ which flips sign under q → q⁻¹, so
      the ansatz is structurally q-asymmetric.
  2.  Off q_0 the ansatz diverges fast (>30% at 0.95 q_0 and >70% at
      1.05 q_0), confirming the q_0 match is a numerical coincidence,
      not a derivation.

Why the original W-2 framing was misleading.
N_sym(q) ALREADY has an exact closed form by its definition recipe
(n_sym_numerical_anchor.py):

    N_v = 3 · v_weak / m_e        (q-independent)
    N_sym(q) = N_v · [2]_q^3 / ([4]_q^2 · [6]_q^2 · [8]_q^2)

The W-2 task was NOT "find a q-rational that hits 213.11"; it was
"find a Gram-determinant or Goldstone-phase-space ansatz whose
value at q_0 matches N_sym(q_0)" — i.e., find a non-trivial
expression that *numerically equals* the recipe at q_0, suggesting
a structural identity between the EW-Higgs Goldstone phase space
and the nuclear normalisation N_v.

The real open question is: derive N_v itself (currently input
from CODATA G_F) from the categorical pipeline.

Output.
This script writes n-sym-w2-retraction.witness.json recording the
refutation; the q_0-only "62 ppm" is documented but recategorised
as numerology not derivation.

Reference: docs/audits/2026-05-03-next-session-plan-to-1ppb.md W-2.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import mpmath
mpmath.mp.dps = 100

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
N_v_const = 3 * v_weak / m_e


def qint(q, n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** -n) / (q - 1 / q)


def N_sym_recipe(q):
    """N_sym(q) per the n_sym_numerical_anchor.py definition."""
    return N_v_const * qint(q, 2) ** 3 / (
        qint(q, 4) ** 2 * qint(q, 6) ** 2 * qint(q, 8) ** 2
    )


def previous_ansatz(q):
    """The 62-ppm point-fit candidate from n_sym_b8_refinement_probe."""
    h = q - 1 / q
    return qint(q, 3) * qint(q, 4) ** 2 * qint(q, 2) ** 2 * (
        qint(q, 4) - h ** 3
    ) / 4


def q_one_twelfth_ansatz(q):
    """Closed-form alternative: [3]_q · [4]_q^3 · q^(1/12).

    After fixing the operator-precedence bug (commit 3520a4c72) in
    n_sym_b8_refinement_probe.py, this candidate hits N_sym(q_0) at
    8.7 ppm — strictly better than the previous 62 ppm candidate.
    But q^(1/12) is also q-asymmetric (q^(1/12) ≠ q^(-1/12)), and
    the multi-q test below shows the same point-fit signature: 30 %
    off at 0.95 q_0 and 72 % off at 1.05 q_0.  Same retraction
    applies — point-fit numerology, not derivation.
    """
    return qint(q, 3) * qint(q, 4) ** 3 * q ** (mpmath.mpf(1) / 12)


def base_q_symmetric(q):
    """The q-symmetric base [3]_q · [4]_q^3 · [2]_q^2 / 4
    (= previous ansatz minus its q-asymmetric h³ tail)."""
    return qint(q, 3) * qint(q, 4) ** 3 * qint(q, 2) ** 2 / 4


def remainder_R(q):
    """N_sym(q) − base_q_symmetric(q). Both terms q-symmetric, so R is too.
    R measures how far the polynomial base sits from N_sym at each q."""
    return N_sym_recipe(q) - base_q_symmetric(q)


def main() -> int:
    q0 = mpmath.mpf(Q_50_DIGIT_STR)
    print("W-2 retraction probe — multi-q test of the 62-ppm ansatz")
    print(f"  q_0          = {mpmath.nstr(q0, 30)}")
    print(f"  N_v (const)  = {mpmath.nstr(N_v_const, 14)}")
    print(f"  N_sym(q_0)   = {mpmath.nstr(N_sym_recipe(q0), 18)}")
    print()
    print("Multi-q verification of the previous ansatz:")
    print(f"  {'q':>10}  {'N_sym(q)':>20}  {'ansatz(q)':>20}  {'rel_err':>14}")
    print("  " + "-" * 75)
    rows = []
    points = [
        ("0.90 q_0", 0.9 * q0),
        ("0.95 q_0", 0.95 * q0),
        ("0.99 q_0", 0.99 * q0),
        ("q_0",      q0),
        ("1.01 q_0", 1.01 * q0),
        ("1.05 q_0", 1.05 * q0),
        ("1.10 q_0", 1.10 * q0),
        ("1/q_0",    1 / q0),
        ("q_0²",     q0 ** 2),
    ]
    for label, q in points:
        n = N_sym_recipe(q)
        a = previous_ansatz(q)
        a2 = q_one_twelfth_ansatz(q)
        err = float((a - n) / n)
        err2 = float((a2 - n) / n)
        rows.append({
            "q_label": label,
            "q": mpmath.nstr(q, 25),
            "N_sym": mpmath.nstr(n, 18),
            "ansatz": mpmath.nstr(a, 18),
            "rel_err": err,
            "ansatz_q_one_twelfth": mpmath.nstr(a2, 18),
            "rel_err_q_one_twelfth": err2,
        })
        print(f"  {label:>10}  {mpmath.nstr(n, 14):>20}  "
              f"{mpmath.nstr(a, 14):>20}  {err:>+14.4e}")
    print()

    # q ↔ q⁻¹ symmetry check
    rev_err = float(
        (previous_ansatz(1 / q0) - previous_ansatz(q0)) / previous_ansatz(q0)
    )
    rev_err_q12 = float(
        (q_one_twelfth_ansatz(1 / q0) - q_one_twelfth_ansatz(q0))
        / q_one_twelfth_ansatz(q0)
    )
    print(f"q → q⁻¹ asymmetry (h³ ansatz):       {rev_err:+.4e}")
    print(f"q → q⁻¹ asymmetry (q^(1/12) ansatz): {rev_err_q12:+.4e}")
    print(f"  N_sym is q-symmetric (h-free); both ansätze break this symmetry.")
    print()

    # Structural-derivation attempt: R(q) = N_sym(q) − base_q_sym(q)
    # If base_q_sym were close to N_sym then R would be a small q-symmetric
    # correction term, hopefully with a clean closed form.  The data show
    # otherwise.
    print("Structural-derivation attempt — R(q) = N_sym(q) − [3]_q·[4]_q³·[2]_q²/4:")
    print(f"  {'q':>10}  {'R(q)':>16}")
    print("  " + "-" * 30)
    R_pts = []
    for label, q in points:
        Rv = float(remainder_R(q))
        R_pts.append((label, Rv))
        print(f"  {label:>10}  {Rv:>+16.4f}")
    print()
    print("  R(q_0) = -0.46, R(1/q_0) = -0.46 — q-symmetric ✓")
    print("  R(0.99 q_0) = +19, R(1.01 q_0) = -20 — steep slope through q_0")
    print()
    print("Interpretation: N_sym(q) is dominated by 1/[8]_q² (very steep in q),")
    print("while [3]_q·[4]_q³·[2]_q²/4 is a smooth polynomial dominated by [4]_q³.")
    print("These structurally-distinct curves CROSS near q_0 — the 62 ppm match")
    print("is a near-crossing coincidence, not a small correction term.")
    print("R(q) cannot be expressed as a simple q-symmetric closed form.")
    print()
    print("VERDICT: previous ansatz is point-fit numerology.")
    print("  Match at q_0 is a curve-crossing coincidence; the polynomial base")
    print("  and N_sym(q) are structurally different functions of q.")
    print("  Same verdict applies to the q^(1/12) candidate (corrected after")
    print("  the n_sym_b8_refinement_probe operator-precedence bug fix): it")
    print("  hits q_0 at 8.7 ppm but is q-asymmetric and >70% off at 1.05 q_0.")
    print()
    out = {
        "computation": "n-sym-w2-retraction",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Retraction of the 62 ppm 'W-2 closure' claim from "
            "n_sym_b8_refinement_probe.py.  Multi-q verification shows the "
            "previous ansatz "
            "[3]_q·[4]_q²·[2]_q²·([4]_q-h³)/4 is point-fit numerology: q-asymmetric "
            "(h³ flips sign under q→q⁻¹) and 30-70% off at q ≠ q_0.  "
            "Also covers the q^(1/12) candidate revealed after the "
            "operator-precedence bug fix in the b8 refinement probe — at "
            "q_0 it matches N_sym to 8.7 ppm but is also q-asymmetric and "
            "fails the multi-q test the same way.  "
            "N_sym(q) already has an exact closed form by its recipe: "
            "N_sym(q) = N_v · [2]_q³ / ([4]_q² · [6]_q² · [8]_q²) where "
            "N_v = 3·v_weak/m_e is q-independent.  W-2's open question is "
            "whether N_v (currently CODATA G_F input) admits a categorical derivation."
        ),
        "verdict": "all probed ansätze are point-fit numerology; W-2 not closed",
        "N_v_const": mpmath.nstr(N_v_const, 25),
        "N_sym_recipe_form": "N_v · [2]_q^3 / ([4]_q^2 · [6]_q^2 · [8]_q^2)",
        "previous_ansatz_form": "[3]_q · [4]_q^2 · [2]_q^2 · ([4]_q - h^3) / 4",
        "previous_ansatz_q0_match_rel_err": "6.2e-5",
        "previous_ansatz_q_q_inv_asymmetry": rev_err,
        "previous_ansatz_max_off_q0_rel_err": max(abs(r["rel_err"]) for r in rows),
        "q_one_twelfth_ansatz_form": "[3]_q · [4]_q^3 · q^(1/12)",
        "q_one_twelfth_q0_match_rel_err": "8.7e-6",
        "q_one_twelfth_q_q_inv_asymmetry": rev_err_q12,
        "q_one_twelfth_max_off_q0_rel_err": max(
            abs(r["rel_err_q_one_twelfth"]) for r in rows
        ),
        "multi_q_test": rows,
        "open_question": "Derive N_v from categorical pipeline (currently CODATA G_F input)",
    }
    out_path = Path(__file__).parent / "n-sym-w2-retraction.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
