import Mathlib.Tactic
import Mathlib.Algebra.Order.Archimedean.Basic
import QOU.Core.CutLimit

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

## Algebraic form (2026-11-27, bean `qou-e1uf`, epic `qou-dk7p`)

Owner ruling 2026-11-27: transcendental and analytic statements live behind
`QOU/Transcendental/`. The majorant is now carried in its **squared** form,
`v_n² · (n − 3) ≤ 1`, which for `v_n ≥ 0` and `n ≥ 4` is equivalent to
`v_n ≤ 1/√(n − 3)` and uses no square root. The conclusion is
`QOU.Core.CutLimit.ConvergesTo`, a located cut, over any Archimedean ordered
field. No `Real.sqrt`, no filter, no topology. The `ℝ`/`Real.sqrt`/`Tendsto`
form of the same statement is `QOU.Transcendental.QPlancherelSqrtBridge`.

## Cross-references

  - [folio/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md]
  - [folio/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean] (`HasQPlancherelCLT`)
-/

namespace QOU.Observations

open QOU.Core.CutLimit

/-- **Inputs** for the q-Plancherel asymptotic skeleton, over an Archimedean
    ordered field `K`. The variance majorant is an *assumption* (its
    `1/√(n − 3)` form is unsourced, see the module docstring), carried
    squared: `char_variance n ^ 2 * (n − 3) ≤ 1`. The theorem
    `QPlancherelAsymptoticSkeleton` **derives** the vanishing of the
    fluctuations from it, rather than re-emitting it. -/
class QPlancherelAsymptoticSkeletonContext (K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  /-- Variance of the character fluctuations `χ_λ − 𝔼_q[χ]` at strand
      count `n`, measured under the pushforward measure `μ_n^{(q)}`. -/
  char_variance : ℕ → K
  /-- The variance is non-negative (it is a variance). -/
  variance_nonneg : ∀ n : ℕ, 0 ≤ char_variance n
  /-- **Assumed majorant**, squared: `char_variance n ≤ 1/√(n − 3)` written
      without the root. An ASSUMPTION of the context, not a cited theorem;
      see the module docstring. -/
  variance_majorant_sq : ∀ n : ℕ, 4 ≤ n →
    char_variance n ^ 2 * ((n : K) - 3) ≤ 1

/-- **q-Plancherel asymptotic skeleton — fluctuation vanishing**
    ([`prop:q-plancherel-asymptotic-skeleton`]).

    The character fluctuations vanish in the large-`n` limit: the sequence
    `char_variance` converges to `0` as a located cut.

    **Derived** from the squared majorant and non-negativity, using only the
    Archimedean property of `K`: for `ε > 0` pick `N ≥ 4` with
    `ε² (N − 3) > 1`; then `v_n ≥ ε` for some `n ≥ N` would give
    `v_n² (n − 3) ≥ ε² (n − 3) > 1`. -/
-- Ref: [feray-meliot2012] https://doi.org/10.1007/s00440-010-0331-6
-- Ref: [leitner2026] quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md
theorem QPlancherelAsymptoticSkeleton {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] [Archimedean K]
    [ctx : QPlancherelAsymptoticSkeletonContext K] :
    ConvergesTo ctx.char_variance 0 := by
  apply convergesTo_of_tendstoEps
  intro ε hε
  obtain ⟨M, hM⟩ := exists_nat_gt (1 / ε ^ 2)
  refine ⟨M + 4, fun n hn => ?_⟩
  have hv := ctx.variance_nonneg n
  have hsq := ctx.variance_majorant_sq n (by omega)
  rw [sub_zero, abs_of_nonneg hv]
  by_contra hge
  push_neg at hge
  have hε2 : 0 < ε ^ 2 := by positivity
  have hn : (M : K) + 4 ≤ n := by exact_mod_cast hn
  have h1 : 1 < ε ^ 2 * ((n : K) - 3) := by
    have : 1 / ε ^ 2 < (n : K) - 3 := by linarith
    rw [div_lt_iff₀ hε2] at this
    linarith
  have h2 : ε ^ 2 ≤ ctx.char_variance n ^ 2 := by
    exact pow_le_pow_left₀ hε.le hge 2
  have h3 : ε ^ 2 * ((n : K) - 3) ≤ ctx.char_variance n ^ 2 * ((n : K) - 3) :=
    mul_le_mul_of_nonneg_right h2 (by linarith)
  linarith

end QOU.Observations
