import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Order.Filter.AtTopBot.Basic

/-!
# QOU.BraidKnot.terms_2_6_higher_operations — conjecture carrier

Content block
[`conj:terms-2-6-higher-operations`](../../../quantum-observable-universe/mass-theory/terms-2-6-higher-operations.md).

**Conjecture, not a proposition (owner, 2026-11-20, bean `qou-6qbv`).** The
block reads Term 2 of the unified knot-mass formula as the `k → ∞` limit of
the level-`k` Jones–Wenzl traces, and Term 6 as the sum over `ℓ ≥ 2` of the
root-of-unity residues `Res_{q = ζ_ℓ}[Φ_q · tr_{M,ℓ}(T_w)] / (q₀ − ζ_ℓ)`.

## What changed

Until 2026-11-20 this file carried a context class whose fields were
`target_page_term_2 = 1 ∧ hochschild_arity_term_2 = 2` (and the same for
term 6) on free `ℕ` fields, and a `def` that projected them back. Any instance
picked the numbers, so it asserted nothing. It also encoded the Hochschild
higher-operation route, which the block's own author note records as **closed**
(`HH¹(H₃(R, q)) = 0` at generic `q`).

## What is stated now

`Terms26HigherOperations term2 levelTrace term6 residue` is the conjecture
about the four named real quantities: the level traces converge to Term 2, and
the shifted residue series sums to Term 6. It is a `Prop`-valued class with no
instance — the open state. The quantities are parameters, so a witness has to
be about these particular numbers, not ones the instance chooses.

`ℝ` is deliberate (§7c): both readings are limits, which are archimedean.

## What is proved

`term2_eq_of_conj` and `term6_eq_of_conj`: under the conjecture, Term 2 and
Term 6 are *determined* by the level traces and the residues (limits and sums
in `ℝ` are unique). So the conjecture, if true, leaves no freedom in either
term. That is the content a fitted Term 2 or Term 6 would violate.
-/

namespace QOU.BraidKnot

open Filter Topology

/-- **Conjecture (Terms 2 and 6).** `levelTrace k` is the level-`k`
Jones–Wenzl trace contributing to Term 2; `residue ℓ` is the `ℓ`-th
root-of-unity residue term. Term 2 is their `k → ∞` limit and Term 6 is the
sum of the residues over `ℓ ≥ 2`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/terms-2-6-higher-operations
-- Ref: [habiro2004] Habiro, "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
class Terms26HigherOperations (term2 : ℝ) (levelTrace : ℕ → ℝ)
    (term6 : ℝ) (residue : ℕ → ℝ) : Prop where
  /-- Term 2 is the infinite-level Wedderburn limit. -/
  term2_wedderburn_limit : Tendsto levelTrace atTop (𝓝 term2)
  /-- Term 6 is the root-of-unity residue sum over `ℓ ≥ 2`. -/
  term6_residue_sum : HasSum (fun ℓ => residue (ℓ + 2)) term6

/-- Under the conjecture, Term 2 is determined by the level traces. -/
theorem term2_eq_of_conj {t2 t2' t6 t6' : ℝ} {levelTrace residue : ℕ → ℝ}
    (h : Terms26HigherOperations t2 levelTrace t6 residue)
    (h' : Terms26HigherOperations t2' levelTrace t6' residue) : t2 = t2' :=
  tendsto_nhds_unique h.term2_wedderburn_limit h'.term2_wedderburn_limit

/-- Under the conjecture, Term 6 is determined by the residues. -/
theorem term6_eq_of_conj {t2 t2' t6 t6' : ℝ} {levelTrace residue : ℕ → ℝ}
    (h : Terms26HigherOperations t2 levelTrace t6 residue)
    (h' : Terms26HigherOperations t2' levelTrace t6' residue) : t6 = t6' :=
  h.term6_residue_sum.unique h'.term6_residue_sum

/-- The conjecture is not automatic: a divergent level-trace sequence admits no
Term 2 at all, so `Terms26HigherOperations` fails for every candidate value. -/
theorem not_conj_of_divergent {t2 t6 : ℝ} {residue : ℕ → ℝ} :
    ¬ Terms26HigherOperations t2 (fun k => (k : ℝ)) t6 residue := by
  intro h
  exact not_tendsto_nhds_of_tendsto_atTop tendsto_natCast_atTop_atTop t2
    h.term2_wedderburn_limit

end QOU.BraidKnot
