#!/usr/bin/env python3
"""alpha_em_r2_quillen_curvature_probe.py — R2 premise attack: is the α_EM
per-loop normalization 1/(8π) a Quillen determinant-line CURVATURE coefficient
over the Bring family?

Bean qou-jkcx. DERIVATION-ONLY; owner ruling stands (2026-07-19: R2 is NOT
Lean/derived-proved; 1/(8π) stays a phase-4 identification; NOTHING wires
regardless of outcome). Scope-(a), audit-only, NO FIT.

DISTINCT ANGLE vs the active B2 sibling cluster (a2ee67bd MatrixSchurCommutant,
1a83135b Hodge normalization, 58c3d52f equivariance ⇒ τ(Markov)∝Hodge): the
siblings attack the IDENTIFICATION "loop weight = Hodge Gram" algebraically;
this probe attacks the NORMALIZATION 1/(8π) geometrically, as a curvature
coefficient of the determinant line bundle over the Bring Jacobian family
(the §5 proposal of docs/audits/2026-07-25-quillen-anomaly-classification.md,
executed).

TARGET-OBJECT STATEMENT (Task 1, precise). R2's surviving open content after
the 2026-07-19 decomposition is (i) R2-core — "the loop expansion weighs
proper time by the standard Schwinger measure with unit normalization, one
per-mode unit on the doubled pair" — plus (ii) the B2 τ-identification. The
working coefficient is ½·a₀ = 1/(8π) with a₀ = 1/(4π) the 2D heat-kernel
unit (derived, #3909). MISMATCH FINDING (recorded up front): R2-core's object
is a PROPER-TIME MEASURE normalization, not per se a determinant-line point
value or curvature. The bridge that makes a Quillen attack meaningful anyway:
Bismut–Freed compute Quillen curvature from the SAME heat-kernel index
density (AGMV Sect. 4, below Eq. (4.18)), so if 1/(8π) is derivable
geometrically it must appear as a curvature coefficient (rational × 1/π) of
a determinant line over the framework's own family. Candidate identities are
therefore of the form:

    1/(8π)  =?  [curvature coefficient of det line L over family F,
                 extracted against the scale-invariant reference form,
                 normalized by a framework-forced count]

with every ingredient named per candidate:
  * family F = the Bring Jacobian isogeny family Jac(Bring) ≅ E_{5τ}³ × E_τ
    (complex torus; τ_B = τ₀·M_RR, spec(M_RR) = {5,5,5,1} ⇒ factor
    multiplicities (3,1) — BN12/BDH22 data, verified exactly in
    tau_dictionary_fricke_spin_probe.py), one-parameter base τ ∈ ℍ through
    the Bring point τ₀ = −1/2 + 0.186676i, fibres (5τ,5τ,5τ,τ);
  * operator = ∂̄ per elliptic fibre (equivalently the scalar Laplacian via
    the verified det'Δ(E_τ) = (Im τ)²|η|⁴), and for the spin-content
    candidates the AGMV family D: Lⁿ → L^{n+2} with obstruction weight
    3(n+1)²−1 (AGMV Eq. (4.25)–(4.32)); spin structure: the S₅-invariant
    characteristic is the EVEN/Szegő one (A6, forced — unique fixed point of
    S₅ on the 256 characteristics), and per AGMV (below Eq. (4.32)) S_L and
    U_WP make NO reference to the characteristic, so the forced spin
    structure is curvature-coefficient-blind — it cannot carry the 1/8;
  * measure = coefficient extraction against ω_hyp = dx∧dy/y² (both the
    Quillen curvature form and ω_hyp are invariant under τ ↦ 5τ, verified
    exactly, so the extraction is well-defined along the family), or AGMV's
    WP normalization ⟨,⟩_WP with the (4.31) coefficient −[3(n+1)²−1]/(64π).

BUILDING BLOCK (exact, from the merged classification probe + AGMV (4.18)):
∂τ∂τ̄ log det'Δ(E_τ) = −1/(2 (Im τ)²), so the curvature 2-form of the
genus-1 determinant line in AGMV's normalization (i/2π)∂∂̄ log‖σ‖² is

    c₁(L_τ) = (i/2π)·(−1/(2y²))·dτ∧dτ̄ = −(1/(2π))·ω_hyp        (exact),

i.e. coefficient −1/(2π) per elliptic factor.

CANDIDATES (Task 2; all exact rational × 1/π, compared to 1/(8π) with
rational arithmetic, no tolerance):
  T0   baseline: 1/(π·b₁), b₁ = 8            — the PR #1552 phase-4
       identification; = 1/(8π) TRIVIALLY (the tautology floor; whether a
       curvature integral DERIVES the shape is the whole question).
  Q-A  product line, unit multiplicities (1,1,1,1): |Σ c₁|/ω_hyp = 4/(2π)
       = 2/π                                  — MISS (16× target).
  Q-A5 isogeny-degree weights (5,5,5,1): 16/(2π) = 8/π — MISS (64×).
  Q-B  per-real-cohomology-mode: (2/π)/b₁ = 1/(4π) = a₀ EXACTLY — MISS by
       exactly 2 (= the known ½ residual, #3925): the Quillen route
       independently reproduces the heat-kernel unit a₀ from forced legs
       only. Structural corroboration, not closure.
  Q-C  per-mode on the complexified doubled pair: (2/π)/(2·b₁) = 1/(8π)
       — MATCH, but the divisor 16 = dim_ℝ(H¹(M,ℝ)⊗ℂ) is exactly the
       "per-mode unit on the doubled pair" premise, i.e. R2-core itself.
  Q-D  Belavin–Knizhnik WP coefficient, scalar content n=0 per factor:
       Σᵢ[3(nᵢ+1)²−1] = 4·2 = 8 ⇒ 8/(64π) = 1/(8π) — MATCH, but n=0 is
       unforced (and 4·2 = 2g = b₁, so the weight sum is the b₁ count in
       disguise) + the /(64π) is AGMV's WP normalization convention.
  Q-E  the framework's actual photon content (spin 1) over the 4 factors:
       n=2 ⇒ Σ = 4·26 = 104 ⇒ 13/(8π) (MISS ×13); n=1 ⇒ Σ = 4·11 = 44 ⇒
       11/(16π) (MISS ×11/2).
  P1   prune (formalize-first): 3(n+1)²−1 = 8 has NO integer solution
       ((n+1)² = 3), so no single AGMV spin weight can equal 8; only sums
       can, and the only structurally-suggested sum landing on 8 is the
       scalar one already flagged as the b₁ count in disguise.

VERDICT (Task 3, tautology audit in the audit doc): shape-compatible,
selection-dependent — NOT derived. Every exact match requires exactly one
unforced discrete choice, and each such choice is a restatement of R2's
known open content. NOTHING WIRES.

Exit 0 ⟺ all assertions pass. Witness:
alpha-em-r2-quillen-curvature-probe.witness.json (audit-only).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp  # noqa: E402
from mpmath import mp, mpc, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Consistency with the committed gate/classification lineage.
from tau_dictionary_hauptmodul_validator import dedekind_eta  # noqa: E402


TARGET = 1 / (8 * sp.pi)          # the phase-4 per-loop weight (magnitude)
B1 = 8                            # b₁ = 2g = dim H¹(Bring, ℝ) — proved (#2114/#3834/#3896)
GENUS = 4                         # Bring genus — 4 elliptic isogeny factors
A0 = 1 / (4 * sp.pi)              # heat-kernel unit a₀ (derived, #3909)


def spin_weight(n: int) -> int:
    """AGMV obstruction weight 3(n+1)² − 1 for D: Lⁿ → L^{n+2} (Eq. 4.25/4.32)."""
    return 3 * (n + 1) ** 2 - 1


# ── Block 1: the genus-1 curvature-form coefficient, exact (sympy) ─────────

def curvature_form_coefficient() -> sp.Expr:
    """c₁(L_τ) = (i/2π)·∂τ∂τ̄ log det'Δ · dτ∧dτ̄ expressed against ω_hyp.

    (i) Re-verify ∂τ∂τ̄ log[(Im τ)²|η|⁴] = −1/(2y²): the |η|⁴ part is
        ∂∂̄-flat (|holomorphic|², η ≠ 0 on ℍ), the metric part is the
        quarter-Laplacian of 2·log y.
    (ii) Convert the AGMV (4.18) normalization (i/2π)∂∂̄ log‖σ‖² to a real
        2-form: dτ∧dτ̄ = −2i·dx∧dy, so
        c₁ = (i/2π)·(−1/(2y²))·(−2i)·dx∧dy = −(1/(2π))·(dx∧dy)/y².
    Returns the exact coefficient against ω_hyp = dx∧dy/y².
    """
    x, y = sp.symbols("x y", real=True, positive=True)

    # (i) metric part: quarter-Laplacian of 2 log y equals −1/(2y²) exactly.
    metric = 2 * sp.log(y)
    quarter_lap = sp.Rational(1, 4) * (sp.diff(metric, x, 2) + sp.diff(metric, y, 2))
    assert sp.simplify(quarter_lap - (-1 / (2 * y ** 2))) == 0

    # |holomorphic|² flatness in independent (u, v):
    u, v = sp.symbols("u v")
    f, g = sp.Function("f"), sp.Function("g")
    assert sp.simplify(sp.diff(2 * sp.log(f(u)) + 2 * sp.log(g(v)), u, v)) == 0

    # (ii) dτ∧dτ̄ = (dx + i dy)∧(dx − i dy) = −2i dx∧dy (wedge coefficient):
    wedge_coeff = sp.expand((1) * (-sp.I) - (sp.I) * (1))   # dx∧dy coefficient
    assert wedge_coeff == -2 * sp.I

    coeff = sp.simplify(sp.I / (2 * sp.pi) * sp.Rational(-1, 2) * wedge_coeff)
    assert coeff == -1 / (2 * sp.pi), f"curvature coefficient: {coeff}"
    return coeff


def hyperbolic_form_scale_invariance() -> None:
    """ω_hyp = dx∧dy/y² is invariant under τ ↦ 5τ (x,y) ↦ (5x,5y): the
    pullback Jacobian 25 cancels (5y)² / y² = 25 exactly. So per-factor
    curvature coefficients pull back to the (5τ,5τ,5τ,τ) fibres unchanged
    and the multiplicity bookkeeping is clean."""
    y = sp.symbols("y", positive=True)
    jacobian = sp.Integer(5) * sp.Integer(5)          # d(5x)∧d(5y) = 25 dx∧dy
    pullback = sp.simplify(jacobian / (5 * y) ** 2 * y ** 2)
    assert pullback == 1, f"omega_hyp not scale-invariant: {pullback}"


# ── Block 2: candidate table, exact rational arithmetic ────────────────────

def build_candidates(kappa: sp.Expr) -> list[dict]:
    """kappa = per-factor curvature coefficient magnitude = 1/(2π)."""
    cands: list[dict] = []

    def add(key: str, value: sp.Expr, family: str, operator: str,
            measure: str, forced: str, unforced: str) -> None:
        ratio = sp.simplify(value / TARGET)
        assert ratio.is_Rational, f"{key}: ratio not rational: {ratio}"
        cands.append({
            "key": key,
            "value_exact": str(value),
            "value_times_pi": str(sp.simplify(value * sp.pi)),
            "ratio_to_1_over_8pi": str(ratio),
            "match": bool(ratio == 1),
            "family": family,
            "operator": operator,
            "measure": measure,
            "forced_ingredients": forced,
            "unforced_ingredients": unforced,
        })

    fam = ("Jac(Bring) ≅ E_{5τ}³ × E_τ, base τ ∈ ℍ through τ₀; "
           "multiplicities (3,1) from spec(M_RR) = {5,5,5,1}")
    op = "∂̄ per elliptic fibre (scalar det'Δ(E_τ) = (Im τ)²|η|⁴)"

    # T0 — the tautology floor (phase-4 identification, PR #1552).
    add("T0_baseline_reciprocal_count", 1 / (sp.pi * B1),
        "none (no family)", "none (no operator)",
        "none — the identification 1/(8π) = 1/(π·b₁) itself",
        "b₁ = 8 proved (#2114/#3834/#3896)",
        "the reciprocal-in-b₁ FORM is the phase-4 identification — "
        "definitionally the thing to be derived, so this row is the "
        "tautology floor, not a candidate")

    # Q-A — product determinant line, unit multiplicities.
    add("QA_product_line_unit_mult", 4 * kappa, fam, op,
        "coefficient against ω_hyp (scale-invariant, verified)",
        "4 factors (g = 4); per-factor −1/(2π) (this probe + AGMV 4.18)",
        "none — and it MISSES by 16")

    # Q-A5 — isogeny-degree weights.
    add("QA5_isogeny_degree_weights", 16 * kappa, fam, op,
        "coefficient against ω_hyp, factors weighted (5,5,5,1)",
        "weights (5,5,5,1) = spec(M_RR)",
        "weighting-by-isogeny-degree is itself a choice — and it MISSES by 64")

    # Q-B — democratic per-real-mode.
    qb = sp.simplify(4 * kappa / B1)
    add("QB_per_real_mode", qb, fam, op,
        "coefficient against ω_hyp ÷ b₁ (per real H¹ mode)",
        "4 factors; per-factor −1/(2π); b₁ = 8 proved",
        "the 'divide by the count' step is the reciprocal-form "
        "identification (phase-4) — BUT the output is a₀ = 1/(4π) "
        "EXACTLY (asserted), reproducing the derived heat-kernel unit "
        "from the Quillen side; residual vs target is exactly 2 — the "
        "known ½ (#3925)")
    assert qb == A0, f"per-real-mode coefficient is not a₀: {qb}"

    # Q-C — per-mode on the complexified doubled pair.
    add("QC_per_mode_doubled_pair", sp.simplify(4 * kappa / (2 * B1)), fam, op,
        "coefficient against ω_hyp ÷ 16, 16 = dim_ℝ(H¹(M,ℝ)⊗ℂ) = "
        "dim_ℝ(H^{1,0} ⊕ H^{0,1} as real space)",
        "4 factors; per-factor −1/(2π); b₁ = 8; H¹⊗ℂ = H^{1,0}⊕H^{0,1} "
        "(Hodge, proved doubling #3920)",
        "counting per REAL dimension of the COMPLEXIFIED pair space is "
        "exactly the R2-core premise ('one per-mode unit on the doubled "
        "pair') — selected because it lands on 1/(8π); no independent "
        "framework fact forces this count over Q-B's")

    # Q-D — Belavin–Knizhnik WP coefficient, scalar operator content.
    w_scalar = sum(spin_weight(0) for _ in range(GENUS))
    assert w_scalar == 8
    add("QD_BK_WP_scalar_content", sp.Rational(w_scalar, 64) / sp.pi,
        fam, "AGMV family D: L⁰ → L², weight 3(0+1)²−1 = 2 per factor",
        "AGMV (4.31) WP normalization: δδ̄W = −Σ[3(nᵢ+1)²−1]/(64π)·⟨δg,δg⟩_WP",
        "4 factors (g = 4); the weight formula (AGMV 4.25/4.32)",
        "(i) n = 0 scalar content is unforced — the framework's photon "
        "lives on real 1-forms (spin 1 ⇒ n = 2 or 1, both MISS, Q-E); "
        "(ii) Σ = 4·2 = 2g = b₁, so the weight sum is the b₁ count in "
        "disguise; (iii) the /(64π) is AGMV's WP normalization convention "
        "— the exact landing inherits a convention choice")

    # Q-E — the photon-appropriate spin content.
    add("QE1_photon_spin1_n2", sp.Rational(4 * spin_weight(2), 64) / sp.pi,
        fam, "AGMV family n = 2 (pair of spin ±1), weight 26 per factor",
        "AGMV (4.31) WP normalization", "weight formula", "none — MISSES")
    add("QE2_photon_n1", sp.Rational(4 * spin_weight(1), 64) / sp.pi,
        fam, "AGMV family n = 1, weight 11 per factor",
        "AGMV (4.31) WP normalization", "weight formula", "none — MISSES")

    return cands


def prune_no_single_spin_weight_is_8() -> None:
    """Formalize-first prune: 3(n+1)² − 1 = 8 ⇒ (n+1)² = 3 has no integer
    solution — no single AGMV spin weight equals 8; only sums can."""
    n = sp.symbols("n", integer=True)
    sols = sp.solve(sp.Eq(3 * (n + 1) ** 2 - 1, 8), n)
    assert sols == [], f"unexpected integer solutions: {sols}"
    # And the integer solutions of (n+1)^2 = 3 over ℚ are irrational:
    assert not any(sp.sqrt(3).is_rational for _ in [0])


# ── Block 3: numeric tie to the Bring point (mpmath) ───────────────────────

def numeric_curvature_at_bring() -> dict:
    """Finite-difference quarter-Laplacian of log[(Im τ)²|η|⁴] at τ₀ vs
    −1/(2y²) — ties the exact coefficient to the actual Bring point."""
    tau0 = mpc(mpf("-0.5"), mpf("0.186676"))   # BDH22 corrected Bring modulus
    x0, y0 = mp.re(tau0), mp.im(tau0)

    def F(x, y):
        return 2 * mp.log(y) + 4 * mp.log(abs(dedekind_eta(mpc(x, y))))

    with mp.workdps(mp.dps + 40):
        fxx = mp.diff(lambda x: F(x, y0), x0, 2)
        fyy = mp.diff(lambda y: F(x0, y), y0, 2)
        computed = (fxx + fyy) / 4
        expected = -1 / (2 * y0 ** 2)
        rel = abs(computed - expected) / abs(expected)
    assert rel < mpf("1e-10"), f"numeric curvature at tau0: rel {rel}"
    return {
        "tau0": mp.nstr(tau0, 12),
        "quarter_laplacian": mp.nstr(computed, 20),
        "expected": mp.nstr(expected, 20),
        "rel_dev": mp.nstr(rel, 5),
    }


def main() -> None:
    set_compute_dps()
    wb = WitnessBuilder("alpha-em-r2-quillen-curvature-probe",
                        engine="sympy+mpmath")

    # Block 1 — building block.
    kappa_signed = curvature_form_coefficient()
    kappa = -kappa_signed                       # magnitude 1/(2π); sign recorded
    hyperbolic_form_scale_invariance()
    print(f"Block 1: c₁(L_τ) = ({kappa_signed})·ω_hyp exactly; "
          f"ω_hyp scale-invariant under τ↦5τ.")
    wb.add_assertion(
        "genus1_curvature_form_coefficient",
        computed=str(kappa_signed), expected="-1/(2*pi)",
        source="c₁ = (i/2π)∂∂̄ log det'Δ(E_τ)·dτ∧dτ̄ = −(1/2π)·ω_hyp: "
               "AGMV Eq. (4.18) normalization × the exact mixed derivative "
               "−1/(2y²) (sympy exact; dτ∧dτ̄ = −2i dx∧dy); sign NEGATIVE "
               "(recorded: the working loop insertion is also negative, "
               "[2]_q(1−h²α))",
    )
    wb.add_assertion(
        "omega_hyp_scale_invariant_under_5tau",
        computed="1", expected="1",
        source="pullback of dx∧dy/y² under (x,y)↦(5x,5y): Jacobian 25 "
               "cancels (5y)²/y² — multiplicity bookkeeping over the "
               "(5τ,5τ,5τ,τ) fibres is exact",
    )

    # Block 2 — candidates.
    cands = build_candidates(kappa)
    print(f"\n{'key':36s} {'value':12s} {'ratio':>8s}  match")
    for c in cands:
        print(f"{c['key']:36s} {c['value_exact']:12s} "
              f"{c['ratio_to_1_over_8pi']:>8s}  {c['match']}")
    matches = [c["key"] for c in cands if c["match"]]
    misses = [c["key"] for c in cands if not c["match"]]
    # Exactly the tautology floor + the two selection-dependent matches:
    assert set(matches) == {"T0_baseline_reciprocal_count",
                            "QC_per_mode_doubled_pair",
                            "QD_BK_WP_scalar_content"}, matches
    wb.add_assertion(
        "exact_matches_are_selection_dependent_only",
        computed=",".join(sorted(matches)),
        expected="QC_per_mode_doubled_pair,QD_BK_WP_scalar_content,"
                 "T0_baseline_reciprocal_count",
        source="rational-exact comparison of every candidate against "
               "1/(8π): the ONLY exact matches are the tautology floor T0 "
               "and the two candidates each requiring one unforced discrete "
               "choice (Q-C: the doubled-pair per-mode count = R2-core "
               "premise; Q-D: scalar operator content whose weight sum "
               "4·2 = 2g = b₁ is the count in disguise, under AGMV's WP "
               "convention). Every forced-ingredients-only candidate "
               "MISSES: Q-A by 16, Q-A5 by 64, Q-B by 2, Q-E by 13 and "
               "11/2.",
    )
    wb.add_assertion(
        "per_real_mode_reproduces_a0_exactly",
        computed=str(sp.simplify(4 * kappa / B1)), expected="1/(4*pi)",
        source="Q-B: total curvature coefficient 4/(2π) ÷ b₁ = 1/(4π) = a₀ "
               "EXACTLY — the Quillen/Bismut–Freed route independently "
               "reproduces the derived heat-kernel unit (#3909); the "
               "residual vs 1/(8π) is exactly 2, i.e. the known open ½ "
               "(#3925) relocated, not closed",
    )
    prune_no_single_spin_weight_is_8()
    wb.add_assertion(
        "no_single_agmv_spin_weight_equals_8",
        computed="[]", expected="[]",
        source="3(n+1)²−1 = 8 ⇒ (n+1)² = 3: no integer solution (sympy "
               "solve over ℤ) — no single AGMV spin weight is 8; only sums "
               "reach 8, and the structurally-suggested one (4 scalar "
               "factors) is 2g = b₁ in disguise",
    )

    # Block 3 — numeric tie to the Bring point.
    num = numeric_curvature_at_bring()
    print(f"\nBlock 3: quarter-Laplacian at τ₀ = {num['quarter_laplacian']} "
          f"vs {num['expected']} (rel dev {num['rel_dev']})")
    wb.add_assertion(
        "curvature_numeric_at_bring_tau0",
        computed=num["quarter_laplacian"], expected=num["expected"],
        tolerance=1e-10,
        source="mpmath finite-difference quarter-Laplacian of "
               "log[(Im τ)²|η|⁴] at the Bring τ₀ = −0.5 + 0.186676i",
    )

    # Witness.
    wb.set_description(
        "α_EM R2 Quillen-curvature attack (bean qou-jkcx; DERIVATION-ONLY; "
        "owner ruling 2026-07-19 stands: R2 NOT proved, 1/(8π) stays "
        "phase-4, NOTHING wires). Executes the §5 proposal of the "
        "2026-07-25 Quillen classification: test whether 1/(8π) is a "
        "determinant-line CURVATURE coefficient over the Bring Jacobian "
        "family Jac(Bring) ≅ E_{5τ}³ × E_τ. Building block (exact): "
        "c₁(L_τ) = −(1/2π)·ω_hyp per elliptic factor (AGMV 4.18 × the "
        "verified −1/(2y²)); ω_hyp scale-invariant under τ↦5τ so the "
        "(3,1) multiplicities pull back cleanly. Candidate table (exact "
        "rational × 1/π, no tolerance): unit-multiplicity product 2/π "
        "(MISS ×16); isogeny-weights (5,5,5,1) 8/π (MISS ×64); "
        "per-real-mode (÷b₁=8) = 1/(4π) = a₀ EXACTLY (MISS ×2 — the "
        "Quillen route independently reproduces the derived heat-kernel "
        "unit; the residual 2 is the known open ½, #3925); per-mode on "
        "the complexified doubled pair (÷16) = 1/(8π) MATCH but the "
        "divisor is the R2-core premise itself; Belavin–Knizhnik WP "
        "coefficient with scalar content 8/(64π) = 1/(8π) MATCH but n=0 "
        "is unforced (photon spin-1 content gives 13/(8π) or 11/(16π), "
        "both MISS) and Σ = 4·2 = 2g = b₁ is the count in disguise under "
        "AGMV's WP convention. Prune: no integer n has 3(n+1)²−1 = 8. "
        "The forced even/Szegő characteristic (A6) is curvature-"
        "coefficient-blind (AGMV: S_L, U_WP reference no characteristic) "
        "— it cannot carry the 1/8. VERDICT: shape-compatible, "
        "selection-dependent — NOT derived; every exact match needs "
        "exactly one unforced choice restating R2's known open content. "
        "MISMATCH FINDING: R2-core's object is a Schwinger proper-time "
        "measure normalization, not a determinant-line quantity; the "
        "curvature attack can reproduce a₀ and relocate the ½, not "
        "derive it. Scope-(a); NO FIT; audit-only; nothing wired."
    )
    wb.set_audit_only(
        "docs/audits/2026-07-25-alpha-em-r2-quillen-curvature-attack.md")
    wb.add_data("target_object_statement", {
        "R2_core": "the loop expansion weighs proper time by the standard "
                   "Schwinger measure with unit normalization — one "
                   "per-mode unit on the doubled pair (OPEN; owner ruling "
                   "2026-07-19)",
        "working_coefficient": "½·a₀ = 1/(8π), a₀ = 1/(4π) heat-kernel "
                               "(derived #3909)",
        "mismatch_finding": "R2-core's object is a proper-time MEASURE "
                            "normalization, not a determinant-line point "
                            "value or curvature; the Bismut–Freed bridge "
                            "(same heat-kernel index density) is what "
                            "makes the curvature framing meaningful as a "
                            "shape test only",
    })
    wb.add_data("candidates", cands)
    wb.add_data("numeric_bring_tie", num)
    wb.add_data("agmv_reference", {
        "citation": "L. Alvarez-Gaume, G. Moore, C. Vafa, 'Theta "
                    "Functions, Modular Invariance, and Strings', Commun. "
                    "Math. Phys. 106, 1-40 (1986)",
        "upload": "library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf",
        "equations_used": {
            "(4.18)": "curvature of the determinant line = (i/2π)∂∂̄ "
                      "log‖σ‖² (Bismut–Freed)",
            "(4.25)/(4.27)": "conformal-anomaly weight [3(n+1)²−1]/(24π) "
                             "Liouville / [3(n+1)²−1]/(192π) momentum form",
            "(4.31)": "δδ̄W = −[3(n+1)²−1]/(64π)·⟨δg,δg⟩_WP",
            "below (4.32)": "total obstruction ∝ Σᵢ[3(nᵢ+1)²−1]; S_L and "
                            "U_WP make no reference to the spin structure",
        },
    })
    wb.save()
    print("\nwitness saved; all assertions passed.")


if __name__ == "__main__":
    main()
