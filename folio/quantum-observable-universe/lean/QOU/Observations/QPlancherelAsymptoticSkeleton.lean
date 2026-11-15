import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.Observations.QPlancherelAsymptoticSkeleton

**Proposition** ([`prop:q-plancherel-asymptotic-skeleton`](../../../quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md)).

The `q`-Plancherel measure `M_{n,q}` pushes forward to measures on the
`q`-deformed Thoma simplex. The `q = 1` weak limit (clause 1) and the
generic-`q` asymptotics (clause 2) are literature; the operator-algebra
realisation of the generic-`q` limit (clause 3) is conjectural.

**The weight was corrected on 2026-09-05** (bean `qou-j7ef`). This module
previously said the manuscript pushed forward the Wedderburn weight
`w̃_λ^{(n)} = dim_q²(λ)/[n]_q!` and called clause 2 *established* for it.
It is not: the cited asymptotics are proved for `M_{n,q}`, which differs
from `dim_q²/[n]_q!` by a factor of 978 on some `λ` at `n = 12` at the
substrate — not by a normalisation, so no rescaling moves the citation
across. The manuscript block now states the proposition over `M_{n,q}`
itself, which the corpus already holds as the Molien / fake-degree weight
(`MolienFakeDegreeGeneralN.molienSum`) under the substitution `Q = q²`;
that identification is exact and is verified in exact rational arithmetic
in `computations/probes/molien_feray_meliot_bridge_probe.py`.

**The `1/√(n − 3)` majorant below is UNSOURCED, and the field is named
accordingly.** It was attributed to Féray–Méliot; that expression does
not occur anywhere in their `q`-Plancherel paper, whose fluctuation
result is a central limit theorem at scale `√n`. The theorem proved here
is unaffected — it is a squeeze, valid for *any* non-negative sequence
dominated by a majorant tending to `0`, whoever supplies it — but the
hypothesis is carried as an assumption of the context class and must not
be read as a cited theorem until someone sources it.

## Disposition (derived, not projected)

The previous encoding returned `ctx.constant_eq_one ▸ ctx.char_variance_bound`
— i.e. it re-emitted the class field that **is** the variance-bound
conclusion (after substituting `C = 1`); no derivation.

Here the class carries the genuine **input**: the majorant
`char_variance n ≤ 1/√(n − 3)` — an ASSUMPTION, not a cited theorem; it
was described here as "an established external theorem, cited
[`feray2010`]" and neither half survived checking (see above) — together
with non-negativity of the variance. The theorem
then **derives** the actual asymptotic content the manuscript needs — the
character fluctuations **vanish in the large-`n` limit**,
`char_variance n → 0` — by squeezing between `0` and the majorant
`1/√(n − 3) → 0`. This vanishing is precisely what makes the pushforward
measures concentrate (the measure-theoretic half of the convergence in
clauses 1–2); it is a *consequence* of the hypothesis, not a restatement
of a field. That the hypothesis is unsourced weakens what the module can
be cited FOR; it does not weaken the derivation, which needs only that
the majorant tends to `0`.

The full measure-valued statement (existence of `Ω_q`, the pushforward
maps `ι_n`, weak convergence, and the conjectural operator-algebra
realisation 3a/3b) is not formalised here — those are the open
literature/conjectural parts of the manuscript, honestly left unencoded
rather than smuggled into a `True`/projection field.

## Cross-references

  - [folio/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md]
  - [folio/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean] (`HasQPlancherelCLT`)
-/

namespace QOU.Observations

open Filter Topology

/-- **Inputs** for the q-Plancherel asymptotic skeleton. The variance
    majorant is an *assumption* (its `1/√(n − 3)` form is unsourced — see
    the module docstring); the theorem `QPlancherelAsymptoticSkeleton`
    **derives** the asymptotic vanishing of the fluctuations from it,
    rather than re-emitting it. -/
class QPlancherelAsymptoticSkeletonContext where
  /-- Variance of the character fluctuations `χ_λ − 𝔼_q[χ]` at strand
      count `n`, measured under the pushforward measure `μ_n^{(q)}`. -/
  char_variance : ℕ → ℝ
  /-- The variance is non-negative (it is a variance). -/
  variance_nonneg : ∀ n : ℕ, 0 ≤ char_variance n
  /-- **Assumed majorant**: the character fluctuations have variance
      `O(1/√(n − 3))`. This is an ASSUMPTION of the context, not a cited
      theorem — see the module docstring: the `1/√(n − 3)` form does not
      occur in Féray–Méliot, and no source for it has been identified.
      Renamed from `feray_meliot_bound` on 2026-09-05 so the name stops
      asserting a provenance the corpus cannot produce. -/
  variance_majorant : ∀ n : ℕ, 4 ≤ n →
    char_variance n ≤ 1 / Real.sqrt ((n : ℝ) - 3)

/-- **q-Plancherel asymptotic skeleton — fluctuation vanishing**
    ([`prop:q-plancherel-asymptotic-skeleton`]).

    The character fluctuations vanish in the large-`n` limit:
    `char_variance n → 0`.

    **Derived** by squeezing the assumed majorant `1/√(n − 3)` (which
    itself tends to `0`, proved here via `Real.sqrt` continuity at `0`)
    against the non-negative variance. This is the measure-concentration
    content the manuscript's clauses 1–2 rest on — a consequence of the
    hypothesis, not a projection of it. The squeeze needs only that the
    majorant tends to `0`; it does not depend on where the majorant came
    from, which is why the unsourced provenance does not touch the
    theorem. -/
-- Ref: [feray-meliot2012] https://doi.org/10.1007/s00440-010-0331-6
-- Ref: [leitner2026] quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md
theorem QPlancherelAsymptoticSkeleton [ctx : QPlancherelAsymptoticSkeletonContext] :
    Tendsto (fun n : ℕ => ctx.char_variance n) atTop (𝓝 0) := by
  -- The assumed majorant `1/√(n − 3)` tends to `0`.
  have hden : Tendsto (fun n : ℕ => (n : ℝ) - 3) atTop atTop := by
    simpa using tendsto_atTop_add_const_right atTop (-3 : ℝ) tendsto_natCast_atTop_atTop
  have hinv : Tendsto (fun n : ℕ => ((n : ℝ) - 3)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp hden
  have hmaj : Tendsto (fun n : ℕ => 1 / Real.sqrt ((n : ℝ) - 3)) atTop (𝓝 0) := by
    have h := (Real.continuous_sqrt.tendsto (0 : ℝ)).comp hinv
    rw [Real.sqrt_zero] at h
    refine h.congr (fun n => ?_)
    simp only [Function.comp_apply, Real.sqrt_inv, one_div]
  -- Squeeze `0 ≤ char_variance n ≤ 1/√(n − 3)`.
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hmaj
    (Eventually.of_forall (fun n => ctx.variance_nonneg n)) ?_
  filter_upwards [eventually_ge_atTop 4] with n hn
  exact ctx.variance_majorant n hn

end QOU.Observations
