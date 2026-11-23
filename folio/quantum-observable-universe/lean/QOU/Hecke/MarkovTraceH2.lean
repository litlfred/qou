import QOU.Hecke.FullRank
import QOU.Hecke.MarkovTrace
import QOU.Shared.MarkovTraceClaim

/-!
# `QOU.Hecke.MarkovTraceH2` — a Markov trace on `H₂(q)`, and a real
`MarkovTraceContext`

Before this file the only inhabitant of `QOU.Shared.MarkovTraceContext` was the
`n = 0` witness, where `Generator 0` is empty and every axiom holds because there
is nothing to check. That is useful for refuting over-general statements and
worth nothing as mathematics: any result quantified over `MarkovTraceContext` was
being tested against a structure with no generators.

This file supplies a witness with content. `H₂(q) = R[X]/(X² − (q − q⁻¹)X − 1)`
is free of rank `2` on the power basis `{1, σ}`
(`QOU.Hecke.InstanceH2` + `QOU.Hecke.instIsHeckeOfFullRankH2`), so the trace is
just "read the two coordinates and weight the second by `z`":

    tr_M(a·1 + b·σ) = a + b·z .

## What each axiom costs

| axiom | why it holds here |
|---|---|
| `trace` is `R`-linear | it is a combination of two `Basis.coord`s |
| `normalised` | `1` is the `0`-th power-basis vector, so its coordinates are `(1, 0)` |
| `cyclic` | **`H₂(q)` is commutative** — `AdjoinRoot` of a commutative ring — so `x*y = y*x` outright |
| `trace_gen` | `σ` is the `1`-st power-basis vector, coordinates `(0, 1)`, so the trace is `z` by construction |
| `trace_prod_gen` | quantifies over `i.idx < j.idx` in `Fin 1` — **vacuous** |

Two of the five are therefore free at `n = 2` (`cyclic` by commutativity,
`trace_prod_gen` by emptiness). That is a real fact about the two-strand algebra,
not a gap: `H₂(q)` is genuinely commutative and genuinely has one generator. It
also means, exactly as `InstanceH2` says of itself, that **this is not evidence
for `n ≥ 3`**, where cyclicity is a theorem with content.

## `z` is a parameter, not a choice made here

The mathematical Markov parameter is `z = 1/(q^{1/2} + q^{-1/2})`, which needs a
square root of `q` in `R`. `QOU.Hecke.MarkovTrace` stores `z` as a class field
and constrains it only through `trace_gen`, so the construction below is stated
for an **arbitrary** `z : R` and does not pretend to pin it. `markovTraceH2` is a
`def` rather than an `instance` for that reason — an instance would have to
invent a value.
-/

namespace QOU.Hecke.MarkovTraceH2

open QOU.Hecke.InstanceH2 Polynomial Module

universe u

variable (R : Type u) [Field R] (q : R)

/-! ## The power basis `{1, σ}` -/

/-- `H₂(q)` on the nose as a rank-2 free module: the `AdjoinRoot` power basis,
reindexed along `heckePoly_natDegree` so the index type is literally `Fin 2`. -/
noncomputable def h2Basis : Basis (Fin 2) R (H2 R q) :=
  ((AdjoinRoot.powerBasis' (heckePoly_monic R q)).basis).reindex
    (finCongr (heckePoly_natDegree R q))

theorem h2Basis_apply (i : Fin 2) :
    h2Basis R q i = AdjoinRoot.root (heckePoly R q) ^ (i : ℕ) := by
  simp only [h2Basis, Module.Basis.reindex_apply, finCongr_symm, finCongr_apply,
    PowerBasis.basis_eq_pow, AdjoinRoot.powerBasis'_gen]
  rfl

/-- The `0`-th basis vector is `1`. -/
theorem h2Basis_zero : h2Basis R q 0 = 1 := by simp [h2Basis_apply]

/-- The `1`-st basis vector is the Hecke generator. -/
theorem h2Basis_one : h2Basis R q 1 = sigma R q := by
  simp [h2Basis_apply, sigma]

/-! ### Coordinates of `1` and `σ`

Stated as their own lemmas because `h2Basis_apply` would otherwise rewrite
`h2Basis R q 0` straight back to `1` and loop. -/

theorem coord_zero_one : (h2Basis R q).coord 0 1 = 1 := by
  conv_lhs => rw [← h2Basis_zero R q]
  simp only [Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_eq_same]

theorem coord_one_one : (h2Basis R q).coord 1 1 = 0 := by
  conv_lhs => rw [← h2Basis_zero R q]
  simp only [Module.Basis.coord_apply, Module.Basis.repr_self]
  exact Finsupp.single_eq_of_ne (by decide)

theorem coord_zero_sigma : (h2Basis R q).coord 0 (sigma R q) = 0 := by
  conv_lhs => rw [← h2Basis_one R q]
  simp only [Module.Basis.coord_apply, Module.Basis.repr_self]
  exact Finsupp.single_eq_of_ne (by decide)

theorem coord_one_sigma : (h2Basis R q).coord 1 (sigma R q) = 1 := by
  conv_lhs => rw [← h2Basis_one R q]
  simp only [Module.Basis.coord_apply, Module.Basis.repr_self, Finsupp.single_eq_same]

/-! ## The trace -/

/-- **The Markov trace on `H₂(q)`**: `tr_M(a·1 + b·σ) = a + b·z`, as an `R`-linear
functional built from the two power-basis coordinates. -/
noncomputable def traceMap (z : R) : H2 R q →ₗ[R] R :=
  (h2Basis R q).coord 0 + z • (h2Basis R q).coord 1

theorem traceMap_apply (z : R) (x : H2 R q) :
    traceMap R q z x = (h2Basis R q).coord 0 x + z * (h2Basis R q).coord 1 x := by
  simp [traceMap]

/-- `tr_M(1) = 1`. -/
theorem traceMap_one (z : R) : traceMap R q z 1 = 1 := by
  rw [traceMap_apply, coord_zero_one, coord_one_one, mul_zero, add_zero]

/-- `tr_M(σ) = z`. -/
theorem traceMap_sigma (z : R) : traceMap R q z (sigma R q) = z := by
  rw [traceMap_apply, coord_zero_sigma, coord_one_sigma, mul_one, zero_add]

/-- **Chain factorisation at `n = 2`** (bean `qou-ltwg`, owner option 3,
2026-11-20). On the genuine rank-two Hecke algebra `H₂(q)`, where `σ² = hσ + 1`
bites at `q ≠ 1`, the Markov trace of one affine letter `a·σ + b` is its vertex
volume `a·z + b`. This is the one-letter case of
`QOU.Hecke.markov_trace_product`, realised on a concrete algebra rather than on
the abstract tower. -/
theorem traceMap_chainLetter (z a b : R) :
    traceMap R q z (a • sigma R q + algebraMap R (H2 R q) b) = a * z + b := by
  rw [map_add, map_smul, traceMap_sigma, Algebra.algebraMap_eq_smul_one, map_smul,
    traceMap_one, smul_eq_mul, smul_eq_mul, mul_one]

/-! ## The instance -/

/-- **A Markov trace on `H₂(q)`**, for any choice of Markov parameter `z`.

A `def` and not an `instance`: `QOU.Hecke.MarkovTrace` does not index on `z`, so
an instance would have to invent a value for it, and the honest statement is that
every `z` gives one. -/
noncomputable def markovTraceH2 (z : R) : MarkovTrace 2 q (H2 R q) where
  trace := traceMap R q z
  normalised := traceMap_one R q z
  -- `H₂(q)` is commutative, so cyclicity is `mul_comm`.
  cyclic := fun x y => by rw [mul_comm]
  z_param := z
  trace_gen := fun _ => traceMap_sigma R q z
  -- `Generator 2` has `idx : Fin 1`, so `i.idx.val < j.idx.val` is never
  -- satisfied — vacuous, exactly as the braid relation is at `n = 2`.
  trace_prod_gen := fun i j hij => by
    exfalso
    have hi := i.idx.isLt
    have hj := j.idx.isLt
    omega

/-- **A `MarkovTraceContext` with content.**

Bundles `ℚ`, the parameter `q = 2`, `n = 2`, the algebra `H₂(2)`, its
`HeckeAlgebra` instance and the Markov trace above with `z = 1`. Contrast the
`n = 0` witness, where `Generator 0` is empty: here the generator exists, the
quadratic relation is genuinely imposed, `spans` genuinely holds, and the trace
genuinely takes the value `z` on the generator. -/
noncomputable def contextH2 : QOU.Shared.MarkovTraceContext where
  R := ℚ
  ringR := inferInstance
  invR := inferInstance
  q := 2
  n := 2
  A := H2 ℚ 2
  ringA := inferInstance
  algebraA := inferInstance
  heckeInst := instHeckeAlgebraH2 ℚ 2
  markovInst := markovTraceH2 ℚ 2 1

/-- **The witness is not the degenerate one.** Its generator set is inhabited;
the `n = 0` witness's is `Generator 0`, which is empty. That is the single fact
separating a `MarkovTraceContext` that carries content from one which discharges
every axiom by having nothing to quantify over. -/
theorem contextH2_generator_nonempty : Nonempty (Generator contextH2.n) := by
  show Nonempty (Generator 2)
  exact ⟨⟨0⟩⟩

/-! ## What this does not establish

`cyclic` and `trace_prod_gen` are free here — the first because `H₂(q)` is
commutative, the second because there is only one generator index. At `n ≥ 3`
neither is free. Noncommutativity is already visible at `n = 3`
(`QOU.Machinery.H3`: `σ₀σ₁ = e₄ ≠ e₃ = σ₁σ₀`) and at `n = 4`
(`QOU.Machinery.H4.mulσ0_mulσ1_ne`), so `cyclic` becomes a theorem rather than a
consequence of commutativity — `QOU.Hecke.MarkovTraceOnH3A.markovTraceH3A` is the
first witness where it does, and where `trace_prod_gen` is satisfiable at all.
Cyclicity at `n = 4` is `QOU.Machinery.H4.trM_cyclic`, sorry-free via the
576-entry `gram_symm` closure, and correspondingly expensive: it is the tree's
build pole.

So this witness makes `MarkovTraceContext`-quantified results non-vacuous. It
does not make them evidence about the general Markov trace. -/

end QOU.Hecke.MarkovTraceH2
