import QOU.Hecke.InstanceOnH3A
import QOU.Hecke.MarkovTrace
import QOU.Shared.MarkovTraceClaim

/-!
# `QOU.Hecke.MarkovTraceOnH3A` — a Markov trace at `n = 3`, where two axioms stop being free

`QOU.Hecke.MarkovTraceH2` supplied the first `QOU.Hecke.MarkovTrace` and said
plainly what it did not establish: at `n = 2` two of the five fields are free —
`cyclic` because `H₂(q)` is commutative, and `trace_prod_gen` because
`Generator 2` has a single index so `i.idx < j.idx` is unsatisfiable. It is
therefore not evidence for `n ≥ 3`.

This file is that evidence. At `n = 3` both fields carry content:

* **`cyclic`** is a theorem, not a consequence of commutativity —
  `QOU.Machinery.H3.trM_cyclic`, proved by unfolding the trace sum and the
  nested generator actions and closing with `ring`. `H₃(q)` is not commutative
  (`σ₀σ₁ = e₄ ≠ e₃ = σ₁σ₀`), so `tr(xy) = tr(yx)` is a real symmetry.
* **`trace_prod_gen`** is satisfiable: `Generator 3` carries `idx : Fin 2`, so
  the pair `⟨0⟩ < ⟨1⟩` exists and the field must actually deliver
  `tr(σ₀σ₁) = z²`. It does, because `σ₀σ₁` is normal-form basis vector `e₄` and
  the trace weight there is `z²` (`TRM z h = ![1, z, z, z², z², h·z² + z]`).

## Everything here comes from the tree

The trace, its linearity, its cyclicity and its Markov reduction are
`QOU.Machinery.MarkovTraceOnHecke`'s (`trM`, `trM_add`, `trM_smul`,
`trM_cyclic`, `trM_markov_σ₁`), and `QOU.Machinery.HeckeH3AlgebraInstance`
already wraps them as `QOU.Machinery.MarkovTrace R (H3A R h) (trace z)` — a
*different* class from `QOU.Hecke.MarkovTrace`. What was missing is the bridge
to the `QOU.Hecke` class, which is what every `MarkovTraceContext`-quantified
result in the corpus actually consumes.

## `z` is still a parameter

As at `n = 2`, `markovTraceH3A` is a `def` taking `z`, not an `instance`:
`QOU.Hecke.MarkovTrace` does not index on `z` and constrains it only through
`trace_gen`, so every `z` gives a Markov trace here too. The class cannot
distinguish the conventions — see the discussion on PR #4834, which excludes one
of them by the bar law `bar(z) = z − h`, a condition this class has no field for.

## What is still not established at `n = 4`

`QOU.Machinery.HeckeH4StabilizationRung` has the level-4 trace `trM4` with
`trM4_iota34_stabilizes` and `trM4_markov_σ₂`, but **no cyclicity theorem on the
subscript basis** — which is what `H4A`, and hence
`QOU.Hecke.InstanceOnH4A.instHeckeAlgebraH4A`, is built on.

There is one now, proved **directly on the subscript basis**:
`QOU.Machinery.H4.trM4_cyclic` in `H4Cyclicity`, sorry-free, from the three
generators plus the fact that the trace-central elements form a subalgebra.
`#print axioms` shows `[propext, Classical.choice, Quot.sound]`.

Historical note, since this paragraph has been wrong twice. It first said `n=4`
cyclicity rested on a cited `sorry` (false — stale docstrings). It then said the
only proof was `QOU.Machinery.H4.trM_cyclic` in `MarkovTraceH4Gram`, from
`gram_symm` over a 576-entry closure — true when written, but that chain has
since been **deleted**, and `trM_cyclic` is now a corollary of `trM4_cyclic`
transported across the basis relabelling in `H4BasisBridge`. The change of basis
is still what relates the two 24-word tables; only its direction changed.

The route that avoids both a second Gram closure and the basis change is
`QOU.Machinery.BilinearTrace.gram_symm_of_rep_decomp`: if `trM4` decomposes as a
finite weighted sum of representation traces, each multiplicative on `mulNF₄`,
Gram symmetry follows with no per-pair computation. `HeckeH4Wedderburn.wedderburn₄`
supplies exactly those representations — the five block projections of
`H4A ≃ₐ K × K × M₂ × M₃ × M₃` — so what remains is identifying the Markov
weights. Not attempted here.
-/

namespace QOU.Hecke.MarkovTraceOnH3A

open QOU.Machinery.H3 QOU.Hecke.InstanceOnH3A

universe u

variable (K : Type u) [Field K] (q : K)

/-- The Markov trace on `H₃(q)` at parameter `z`, as an `K`-linear functional. -/
def traceMap (z : K) : H3A K (q - q⁻¹) →ₗ[K] K where
  toFun := fun x => trM z (q - q⁻¹) x.v
  map_add' := fun x y => trM_add z (q - q⁻¹) x.v y.v
  map_smul' := fun c x => trM_smul z (q - q⁻¹) c x.v

@[simp] theorem traceMap_apply (z : K) (x : H3A K (q - q⁻¹)) :
    traceMap K q z x = trM z (q - q⁻¹) x.v := rfl

/-- `tr(1) = 1`. -/
theorem traceMap_one (z : K) : traceMap K q z 1 = 1 := by
  show trM z (q - q⁻¹) (unitNF : Fin 6 → K) = 1
  simp [trM, TRM, unitNF, Fin.sum_univ_six]

/-- `tr(σ₀) = z`. -/
theorem traceMap_s0 (z : K) : traceMap K q z (s0 K q) = z := by
  show trM z (q - q⁻¹) (s0 K q).v = z
  simp [trM, TRM, s0, Fin.sum_univ_six]

/-- `tr(σ₁) = z`. -/
theorem traceMap_s1 (z : K) : traceMap K q z (s1 K q) = z := by
  show trM z (q - q⁻¹) (s1 K q).v = z
  simp [trM, TRM, s1, Fin.sum_univ_six]

/-- **`tr(σ₀σ₁) = z²`** — the field that is vacuous at `n = 2`. `σ₀σ₁` is
normal-form basis vector `e₄`, whose trace weight is `z²`. -/
theorem traceMap_s0_mul_s1 (z : K) :
    traceMap K q z (s0 K q * s1 K q) = z * z := by
  rw [s0_mul_s1]
  show trM z (q - q⁻¹) (![0, 0, 0, 0, 1, 0] : Fin 6 → K) = z * z
  simp [trM, TRM, Fin.sum_univ_six]
  ring

/-- **A Markov trace on `H₃(q)`**, for any Markov parameter `z`.

A `def`, not an `instance`, for the same reason as at `n = 2`: the class does not
index on `z`, so an instance would have to invent one. -/
def markovTraceH3A (z : K) : MarkovTrace 3 q (H3A K (q - q⁻¹)) where
  trace := traceMap K q z
  normalised := traceMap_one K q z
  -- Not commutativity: `H₃(q)` is noncommutative (`σ₀σ₁ = e₄ ≠ e₃ = σ₁σ₀`).
  cyclic := fun x y => trM_cyclic z (q - q⁻¹) x.v y.v
  z_param := z
  trace_gen := by
    intro i
    rcases generator_three_cases i with rfl | rfl
    · simpa using traceMap_s0 K q z
    · simpa using traceMap_s1 K q z
  trace_prod_gen := by
    intro i j hij
    rcases generator_three_cases i with rfl | rfl <;>
      rcases generator_three_cases j with rfl | rfl
    · exact absurd hij (by decide)
    · simpa using traceMap_s0_mul_s1 K q z
    · exact absurd hij (by decide)
    · exact absurd hij (by decide)

/-- **A `MarkovTraceContext` at `n = 3`.**

Contrast `QOU.Hecke.MarkovTraceH2.contextH2`, whose `cyclic` and
`trace_prod_gen` are free. Here both carry content, so a result quantified over
`MarkovTraceContext` is now being tested against a structure where the trace
symmetry is a theorem and the pair-product law is an actual computation. -/
noncomputable def contextH3 : QOU.Shared.MarkovTraceContext where
  R := ℚ
  ringR := inferInstance
  invR := inferInstance
  q := 2
  n := 3
  A := H3A ℚ (2 - 2⁻¹)
  ringA := inferInstance
  algebraA := inferInstance
  heckeInst := instHeckeAlgebraH3A ℚ 2
  markovInst := markovTraceH3A ℚ 2 1

/-- The witness has two generator indices, so `trace_prod_gen` is satisfiable —
the property `contextH2` lacked. -/
theorem contextH3_has_ordered_pair :
    ∃ i j : Generator contextH3.n, i.idx.val < j.idx.val := by
  show ∃ i j : Generator 3, i.idx.val < j.idx.val
  exact ⟨⟨0⟩, ⟨1⟩, by decide⟩

end QOU.Hecke.MarkovTraceOnH3A
