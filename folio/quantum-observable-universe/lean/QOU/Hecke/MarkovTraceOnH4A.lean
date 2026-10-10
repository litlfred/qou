import QOU.Hecke.InstanceOnH4A
import QOU.Hecke.MarkovTrace
import QOU.Machinery.H4BasisBridge
import QOU.Shared.MarkovTraceClaim

/-!
# `QOU.Hecke.MarkovTraceOnH4A` — the Markov trace at `n = 4`, the top of the ladder

`QOU.Hecke.MarkovTraceH2` gave the first `QOU.Hecke.MarkovTrace`, at `n = 2`,
and said plainly that two of its five fields were free there. `MarkovTraceOnH3A`
gave `n = 3`, where `cyclic` and `trace_prod_gen` both carry content. This file
gives `n = 4`, which is where the ladder stops mattering: `Generator n` carries
`idx : Fin (n - 1)`, so `n = 4` is the last level at which a class field
(`HeckeAlgebra.farCommute`) becomes satisfiable for the first time. Every field
of both classes now has content on one and the same carrier.

## What had to be proved first

`cyclic` was the whole obstruction, and it is not free at `n = 4`: `H₄(q)` is
noncommutative, and `trM4` had **no cyclicity theorem on the subscript basis** —
which is exactly the basis `H4A`, and hence
`QOU.Hecke.InstanceOnH4A.instHeckeAlgebraH4A`, is built on. The ASCII basis had
one (`QOU.Machinery.H4.trM_cyclic`, sorry-free via the 576-entry `gram_symm`
closure) but the two are different tables.

`QOU.Machinery.H4Bridge.trM4_cyclic` closes it, by transport rather than by a
second Gram closure: the two bases are one basis relabelled, the relabelling
carries products to products (`phi_mulNF`) and `trM` to `trM4` (`trM4_phi`), so
cyclicity comes across. Bean qou-x64l.

## Where the trace values come from

`H4A`'s basis vectors are `e₄ j`, so `trM4 z h (b j).v` is the single weight
`TRM4 z h j` — no sum to evaluate. The generators are basis vectors
(`s0 = b 1`, `s1 = b 2`, `s2 = b 6`, all weight `z`), and each of the three
ordered generator products is again a basis vector, reached by one step of the
word tree `InstanceOnH4A.b_tree_*`:

| product | basis vector | why | weight |
|---|---|---|---|
| `σ₀σ₁` | `b 4` | `b_tree_4` | `z²` |
| `σ₁σ₂` | `b 7` | `b_tree_7` | `z²` |
| `σ₀σ₂` | `b 8` | `farcomm02` then `b_tree_8` | `z²` |

The third is the one `n = 3` cannot ask: it is the far-commuting pair, and
reaching its basis vector needs the relation, not just the tree.

## `z` is still a parameter

As at `n = 2` and `n = 3`, `markovTraceH4A` is a `def` taking `z`, not an
`instance`: `QOU.Hecke.MarkovTrace` does not index on `z` and constrains it only
through `trace_gen`, so every `z` gives a Markov trace here too. Excluding the
wrong convention needs the bar law `bar(z) = z − h`, which this class has no
field for — see PR #4834.
-/

namespace QOU.Hecke.MarkovTraceOnH4A

open QOU.Machinery.H4 QOU.Machinery.H4Bridge QOU.Hecke.InstanceOnH4A

universe u

variable (K : Type u) [Field K] (q : K)

/-! ## The trace on basis vectors

`e₄ j` is `Pi.single j 1`, so the 24-term sum collapses to one weight. Nothing
here expands `TRM4`. -/

theorem trM4_e₄ (z h : K) (j : Fin 24) : trM4 z h (e₄ (R := K) j) = TRM4 z h j := by
  simp [trM4, e₄, Pi.single_apply, Finset.sum_ite_eq']

theorem trM4_b (z : K) (j : Fin 24) :
    trM4 z (q - q⁻¹) (b K q j).v = TRM4 z (q - q⁻¹) j :=
  trM4_e₄ K z (q - q⁻¹) j

/-! ## The trace as a linear functional -/

/-- The Markov trace on `H₄(q)` at parameter `z`, as a `K`-linear functional. -/
def traceMap (z : K) : H4A K (q - q⁻¹) →ₗ[K] K where
  toFun := fun x => trM4 z (q - q⁻¹) x.v
  map_add' := fun x y => trM4_add z (q - q⁻¹) x.v y.v
  map_smul' := fun c x => trM4_smul z (q - q⁻¹) c x.v

@[simp] theorem traceMap_apply (z : K) (x : H4A K (q - q⁻¹)) :
    traceMap K q z x = trM4 z (q - q⁻¹) x.v := rfl

/-- `tr(1) = 1`. The unit is basis vector `b 0` (`InstanceOnH4A.b_zero`), whose
weight is `TRM4 … 0 = 1`. -/
theorem traceMap_one (z : K) : traceMap K q z 1 = 1 := by
  rw [← b_zero K q, traceMap_apply, trM4_b]
  simp [TRM4]

theorem traceMap_s0 (z : K) : traceMap K q z (s0 K q) = z := by
  show trM4 z (q - q⁻¹) (b K q 1).v = z
  rw [trM4_b]; simp [TRM4]

theorem traceMap_s1 (z : K) : traceMap K q z (s1 K q) = z := by
  show trM4 z (q - q⁻¹) (b K q 2).v = z
  rw [trM4_b]; simp [TRM4]

theorem traceMap_s2 (z : K) : traceMap K q z (s2 K q) = z := by
  show trM4 z (q - q⁻¹) (b K q 6).v = z
  rw [trM4_b]; simp [TRM4]

/-! ## The three ordered generator products -/

/-- `tr(σ₀σ₁) = z²`. -/
theorem traceMap_s0_mul_s1 (z : K) :
    traceMap K q z (s0 K q * s1 K q) = z * z := by
  show traceMap K q z (b K q 1 * s1 K q) = z * z
  rw [b_tree_4 K q, traceMap_apply, trM4_b]
  simp [TRM4]; ring

/-- `tr(σ₁σ₂) = z²`. -/
theorem traceMap_s1_mul_s2 (z : K) :
    traceMap K q z (s1 K q * s2 K q) = z * z := by
  show traceMap K q z (b K q 2 * s2 K q) = z * z
  rw [b_tree_7 K q, traceMap_apply, trM4_b]
  simp [TRM4]; ring

/-- **`tr(σ₀σ₂) = z²`** — the far-commuting pair, which does not exist below
`n = 4`. Reaching its basis vector needs `farcomm02`: the word tree gives
`σ₂σ₀ = b 8`, and the relation is what identifies that with `σ₀σ₂`. -/
theorem traceMap_s0_mul_s2 (z : K) :
    traceMap K q z (s0 K q * s2 K q) = z * z := by
  rw [farcomm02 K q]
  show traceMap K q z (b K q 6 * s0 K q) = z * z
  rw [b_tree_8 K q, traceMap_apply, trM4_b]
  simp [TRM4]; ring

/-! ## The Markov trace -/

/-- **A Markov trace on `H₄(q)`**, for any Markov parameter `z`.

Every field carries content. `cyclic` is `QOU.Machinery.H4.trM4_cyclic` — a
theorem, not a consequence of commutativity, since `H₄(q)` is noncommutative —
and `trace_prod_gen` must deliver all three ordered pairs, including the
far-commuting one.

Previously this was `H4Bridge.trM4_cyclic`, which transported the ASCII
`trM_cyclic` across the basis relabelling and so depended on `gram_symm`'s 576
computed entries. `H4.trM4_cyclic` proves the same statement directly from the
three generators, so that dependency — and the Gram chain behind it — is gone.
Note the argument order differs: `(z, h, …)` here, against the bridge's
`(h, z, …)`. -/
def markovTraceH4A (z : K) : MarkovTrace 4 q (H4A K (q - q⁻¹)) where
  trace := traceMap K q z
  normalised := traceMap_one K q z
  cyclic := fun x y => QOU.Machinery.H4.trM4_cyclic z (q - q⁻¹) x.v y.v
  z_param := z
  trace_gen := by
    intro i
    rcases generator_four_cases i with rfl | rfl | rfl
    · simpa using traceMap_s0 K q z
    · simpa using traceMap_s1 K q z
    · simpa using traceMap_s2 K q z
  trace_prod_gen := by
    intro i j hij
    rcases generator_four_cases i with rfl | rfl | rfl <;>
      rcases generator_four_cases j with rfl | rfl | rfl
    · exact absurd hij (by decide)
    · simpa using traceMap_s0_mul_s1 K q z
    · simpa using traceMap_s0_mul_s2 K q z
    · exact absurd hij (by decide)
    · exact absurd hij (by decide)
    · simpa using traceMap_s1_mul_s2 K q z
    · exact absurd hij (by decide)
    · exact absurd hij (by decide)
    · exact absurd hij (by decide)

/-- **A `MarkovTraceContext` at `n = 4`.**

`contextH2`'s `cyclic` and `trace_prod_gen` are free; `contextH3`'s carry
content but cannot reach a far-commuting pair. This one does both, on a carrier
that also carries `wedderburn₄` and `IsHeckeOfFullRank K 4`. -/
noncomputable def contextH4 : QOU.Shared.MarkovTraceContext where
  R := ℚ
  ringR := inferInstance
  invR := inferInstance
  q := 2
  n := 4
  A := H4A ℚ (2 - 2⁻¹)
  ringA := inferInstance
  algebraA := inferInstance
  heckeInst := instHeckeAlgebraH4A ℚ 2
  markovInst := markovTraceH4A ℚ 2 1

/-- The witness has a far-commuting pair of generator indices — the property
`contextH3` cannot have, since `Generator 3` has only two indices and they are
adjacent. -/
theorem contextH4_has_far_commuting_pair :
    ∃ i j : Generator contextH4.n, i.idx.val + 1 < j.idx.val := by
  show ∃ i j : Generator 4, i.idx.val + 1 < j.idx.val
  exact ⟨⟨0⟩, ⟨2⟩, by decide⟩

end QOU.Hecke.MarkovTraceOnH4A
