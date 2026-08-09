import QOU.Hecke.FullRank
import QOU.Machinery.MarkovTraceH4

/-!
# `QOU.Hecke.InstanceH4` — `n = 4`, where far-commutativity first has content

`InstanceH2` gave `H₂(q)` (braid and far-commutativity both vacuous — one
generator index). `InstanceH3` gave `H₃(q)`, the first non-vacuous **braid**
relation. This file gives `n = 4`, the first non-vacuous **far-commutativity**:
`Generator n` carries `idx : Fin (n - 1)`, and `Generator.farCommuting` needs two
indices differing by `≥ 2`, so it is unsatisfiable until `n - 1 ≥ 3`.

`n = 4` is therefore the **last level that exercises anything new**. The three
relation shapes are quadratic (n ≥ 2), braid (n ≥ 3), far-commutativity (n ≥ 4);
`n ≥ 5` adds more indices and no new axiom shape.

## Construction: the operator algebra, not a structure-constant table

`QOU.Machinery.MarkovTraceH4` already carries the three generator **right
actions** `mulσ0`, `mulσ1`, `mulσ2` on the 24-element Gröbner normal-form basis
of `H₄(q)` — generated and cross-validated by
`computations/markov/hecke_regular_nf_table.py` — together with `mulNF`, the full
product, and its bilinearity.

The obvious route (put a `Ring` on `Fin 24 → R` with `mulNF`, as `InstanceH3` does
with `H3.mul`) runs straight into the depth-6 `whnf` wall that module's docstring
warns about: `mulNF` composes up to six `mulσ`s, so associativity unfolds to
depth twelve. Measured: `simp` exhausts 4 000 000 heartbeats after seven minutes
without closing a single generator case.

So this file takes the **right regular representation** instead. Each `mulσk` is
an `R`-linear endomorphism of `Fin 24 → R`; the algebra is the subalgebra of
`Module.End R (Fin 24 → R)` they generate. Associativity is then function
composition — free, and never unfolded. What has to be proved is exactly the
Hecke presentation, at depth ≤ 3:

| lemma | depth | relation |
|---|---|---|
| `mulσ_sq0/1/2` | 2 | `σₖ² = 1 + h·σₖ` |
| `mulσ_farcomm02` | 2 | `σ₀σ₂ = σ₂σ₀` — **the point of `n = 4`** |
| `mulσ_braid01`, `mulσ_braid12` | 3 | `σᵢσⱼσᵢ = σⱼσᵢσⱼ` |

All six discharge by `fin_cases` + `simp` + `ring` in about thirteen seconds
total. They are also of independent interest: until now the claim that
`mulσ0/1/2` satisfy the Hecke presentation rested on the Python generator's
cross-validation, not on anything Lean had checked.

## What is proved here, and what is not

Proved: the `HeckeAlgebra R 4 q` instance, all four fields with the braid and
far-commutativity cases carrying real content, plus `not_commutative` — which
already rules out every commutative model, including
`QOU.Hecke.InstanceH2.rankOneModel`.

**Not** proved: `IsHeckeOfFullRank R 4 _`, i.e. that this algebra is free of rank
`24 = 4!`. Linear independence of the 24 word operators is cheap (they send the
identity basis vector to the 24 distinct basis vectors); spanning needs the
72-entry closure table `σₖ · b_j`, which is now pure symbolic rewriting against
the six relations above rather than coordinate expansion. Tracked separately —
see the bean. Until it lands, this instance is a genuine `HeckeAlgebra` whose
dimension has not been pinned, and should be read as exactly that.
-/

namespace QOU.Hecke.InstanceH4

open QOU.Machinery.H4

universe u

variable (R : Type u) [Field R] (q : R)

/-- The Hecke parameter `h = q − q⁻¹` of the §7a convention, which is the `h`
`QOU.Machinery.MarkovTraceH4` leaves as a free ring element. -/
def hp : R := q - q⁻¹

/-! ## The Hecke presentation, verified on the normal-form actions

Depth ≤ 3, `mulσ` expanded on a free vector. Compare the depth-12 unfolding a
`mulNF`-based associativity proof would need. -/

section Relations

variable {R} {q}
variable (h : R)

theorem mulσ_sq0 (v : Fin 24 → R) : mulσ0 h (mulσ0 h v) = v + h • mulσ0 h v := by
  funext i; fin_cases i <;> simp [mulσ0, Pi.add_apply, Pi.smul_apply]

theorem mulσ_sq1 (v : Fin 24 → R) : mulσ1 h (mulσ1 h v) = v + h • mulσ1 h v := by
  funext i; fin_cases i <;> simp [mulσ1, Pi.add_apply, Pi.smul_apply]

theorem mulσ_sq2 (v : Fin 24 → R) : mulσ2 h (mulσ2 h v) = v + h • mulσ2 h v := by
  funext i; fin_cases i <;> simp [mulσ2, Pi.add_apply, Pi.smul_apply]

/-- **Far-commutativity** `σ₀σ₂ = σ₂σ₀`. Indices `0` and `2` differ by `2`, which
is why this relation exists at `n = 4` and at no smaller `n`. -/
theorem mulσ_farcomm02 (v : Fin 24 → R) :
    mulσ0 h (mulσ2 h v) = mulσ2 h (mulσ0 h v) := by
  funext i; fin_cases i <;> simp [mulσ0, mulσ2] <;> ring

theorem mulσ_braid01 (v : Fin 24 → R) :
    mulσ0 h (mulσ1 h (mulσ0 h v)) = mulσ1 h (mulσ0 h (mulσ1 h v)) := by
  funext i; fin_cases i <;> simp [mulσ0, mulσ1] <;> ring

theorem mulσ_braid12 (v : Fin 24 → R) :
    mulσ1 h (mulσ2 h (mulσ1 h v)) = mulσ2 h (mulσ1 h (mulσ2 h v)) := by
  funext i; fin_cases i <;> simp [mulσ1, mulσ2] <;> ring

end Relations

/-! ## The generator actions as endomorphisms -/

/-- `σ₀` acting on the right of the normal-form module, as an `R`-linear map. -/
def L0 : Module.End R (Fin 24 → R) where
  toFun := mulσ0 (hp R q)
  map_add' := mulσ0_add _
  map_smul' := fun c v => mulσ0_smul _ c v

/-- `σ₁` acting on the right. -/
def L1 : Module.End R (Fin 24 → R) where
  toFun := mulσ1 (hp R q)
  map_add' := mulσ1_add _
  map_smul' := fun c v => mulσ1_smul _ c v

/-- `σ₂` acting on the right — the Markov generator. -/
def L2 : Module.End R (Fin 24 → R) where
  toFun := mulσ2 (hp R q)
  map_add' := mulσ2_add _
  map_smul' := fun c v => mulσ2_smul _ c v

@[simp] theorem L0_apply (v : Fin 24 → R) : L0 R q v = mulσ0 (hp R q) v := rfl
@[simp] theorem L1_apply (v : Fin 24 → R) : L1 R q v = mulσ1 (hp R q) v := rfl
@[simp] theorem L2_apply (v : Fin 24 → R) : L2 R q v = mulσ2 (hp R q) v := rfl

/-! ## The relations, transported to `Module.End`

In `Module.End`, `(f * g) v = f (g v)`, so each of these is the corresponding
`mulσ` relation with no further content. -/

theorem L0_sq : L0 R q * L0 R q = (q - q⁻¹) • L0 R q + 1 := by
  refine LinearMap.ext fun v => ?_
  show mulσ0 (hp R q) (mulσ0 (hp R q) v) = (q - q⁻¹) • mulσ0 (hp R q) v + v
  rw [mulσ_sq0]
  simp [hp, add_comm]

theorem L1_sq : L1 R q * L1 R q = (q - q⁻¹) • L1 R q + 1 := by
  refine LinearMap.ext fun v => ?_
  show mulσ1 (hp R q) (mulσ1 (hp R q) v) = (q - q⁻¹) • mulσ1 (hp R q) v + v
  rw [mulσ_sq1]
  simp [hp, add_comm]

theorem L2_sq : L2 R q * L2 R q = (q - q⁻¹) • L2 R q + 1 := by
  refine LinearMap.ext fun v => ?_
  show mulσ2 (hp R q) (mulσ2 (hp R q) v) = (q - q⁻¹) • mulσ2 (hp R q) v + v
  rw [mulσ_sq2]
  simp [hp, add_comm]

theorem L0_L2_comm : L0 R q * L2 R q = L2 R q * L0 R q :=
  LinearMap.ext fun v => mulσ_farcomm02 (hp R q) v

theorem L0_L1_braid : L0 R q * L1 R q * L0 R q = L1 R q * L0 R q * L1 R q := by
  refine LinearMap.ext fun v => ?_
  simp only [Module.End.mul_apply, L0_apply, L1_apply]
  exact mulσ_braid01 (hp R q) v

theorem L1_L2_braid : L1 R q * L2 R q * L1 R q = L2 R q * L1 R q * L2 R q := by
  refine LinearMap.ext fun v => ?_
  simp only [Module.End.mul_apply, L1_apply, L2_apply]
  exact mulσ_braid12 (hp R q) v

/-! ## The algebra -/

/-- **`H₄(q)`, as the operator algebra of the right regular representation** —
the subalgebra of `Module.End R (Fin 24 → R)` generated by the three generator
actions. Its `Ring` and `Algebra` structure is `Module.End`'s, so associativity
is function composition and is never unfolded. -/
def H4Alg : Subalgebra R (Module.End R (Fin 24 → R)) :=
  Algebra.adjoin R {L0 R q, L1 R q, L2 R q}

namespace H4Alg

theorem L0_mem : L0 R q ∈ H4Alg R q := Algebra.subset_adjoin (Or.inl rfl)
theorem L1_mem : L1 R q ∈ H4Alg R q := Algebra.subset_adjoin (Or.inr (Or.inl rfl))
theorem L2_mem : L2 R q ∈ H4Alg R q := Algebra.subset_adjoin (Or.inr (Or.inr rfl))

/-- `σ₁` in the algebra. -/
def g0 : H4Alg R q := ⟨L0 R q, L0_mem R q⟩
/-- `σ₂` in the algebra. -/
def g1 : H4Alg R q := ⟨L1 R q, L1_mem R q⟩
/-- `σ₃` in the algebra. -/
def g2 : H4Alg R q := ⟨L2 R q, L2_mem R q⟩

end H4Alg

open H4Alg

/-- The generator embedding: `Generator 4` carries `idx : Fin 3`. -/
def embed4 : Generator 4 → H4Alg R q := fun i =>
  if i.idx.val = 0 then g0 R q else if i.idx.val = 1 then g1 R q else g2 R q

@[simp] theorem embed4_zero : embed4 R q ⟨0⟩ = g0 R q := rfl
@[simp] theorem embed4_one : embed4 R q ⟨1⟩ = g1 R q := rfl
@[simp] theorem embed4_two : embed4 R q ⟨2⟩ = g2 R q := rfl

/-- Every `Generator 4` is `⟨0⟩`, `⟨1⟩` or `⟨2⟩`. -/
theorem generator_four_cases (i : Generator 4) : i = ⟨0⟩ ∨ i = ⟨1⟩ ∨ i = ⟨2⟩ := by
  obtain ⟨⟨v, hv⟩⟩ := i
  interval_cases v
  · exact Or.inl rfl
  · exact Or.inr (Or.inl rfl)
  · exact Or.inr (Or.inr rfl)

/-- **`H₄(q)` is a Hecke algebra**, with all three relation shapes carrying
content: the quadratic from `mulσ_sqk`, the braid from `mulσ_braid01/12`, and —
for the first time anywhere in the tree — **far-commutativity** from
`mulσ_farcomm02`. -/
instance instHeckeAlgebraH4 : HeckeAlgebra R 4 q (H4Alg R q) where
  embed := embed4 R q
  quadratic := by
    intro i
    rcases generator_four_cases i with rfl | rfl | rfl
    · exact Subtype.ext (L0_sq R q)
    · exact Subtype.ext (L1_sq R q)
    · exact Subtype.ext (L2_sq R q)
  braid := by
    intro i j hij
    rcases generator_four_cases i with rfl | rfl | rfl <;>
      rcases generator_four_cases j with rfl | rfl | rfl
    -- (0,0), (0,2), (1,1), (2,0), (2,2): not adjacent, so vacuous
    · exact absurd hij (by simp [Generator.adjacent])
    · exact Subtype.ext (L0_L1_braid R q)
    · exact absurd hij (by simp [Generator.adjacent])
    · exact Subtype.ext (L0_L1_braid R q).symm
    · exact absurd hij (by simp [Generator.adjacent])
    · exact Subtype.ext (L1_L2_braid R q)
    · exact absurd hij (by simp [Generator.adjacent])
    · exact Subtype.ext (L1_L2_braid R q).symm
    · exact absurd hij (by simp [Generator.adjacent])
  farCommute := by
    intro i j hij
    obtain ⟨hne, hadj⟩ := hij
    rcases generator_four_cases i with rfl | rfl | rfl <;>
      rcases generator_four_cases j with rfl | rfl | rfl
    · exact absurd rfl hne
    · exact absurd (by simp [Generator.adjacent]) hadj
    -- (0,2) and (2,0): the only far-commuting pairs, and the point of `n = 4`
    · exact Subtype.ext (L0_L2_comm R q)
    · exact absurd (by simp [Generator.adjacent]) hadj
    · exact absurd rfl hne
    · exact absurd (by simp [Generator.adjacent]) hadj
    · exact Subtype.ext (L0_L2_comm R q).symm
    · exact absurd (by simp [Generator.adjacent]) hadj
    · exact absurd rfl hne
  spans := by
    have hset : Set.range (embed4 R q)
        = ((↑) : H4Alg R q → Module.End R (Fin 24 → R)) ⁻¹'
            {L0 R q, L1 R q, L2 R q} := by
      ext x
      constructor
      · rintro ⟨i, rfl⟩
        rcases generator_four_cases i with rfl | rfl | rfl
        · exact Or.inl rfl
        · exact Or.inr (Or.inl rfl)
        · exact Or.inr (Or.inr rfl)
      · intro hx
        rcases hx with h | h | h
        · exact ⟨⟨0⟩, Subtype.ext h.symm⟩
        · exact ⟨⟨1⟩, Subtype.ext h.symm⟩
        · exact ⟨⟨2⟩, Subtype.ext h.symm⟩
    rw [hset]
    exact Algebra.adjoin_adjoin_coe_preimage

/-! ## It is not one of the degenerate models

`QOU.Hecke.InstanceH2.rankOneModel` inhabits `HeckeAlgebra ℚ n 1 ℚ` at every `n`;
it and every other small model is **commutative**. This one is not, so it is
excluded on that ground alone — before any rank computation. -/

/-- The identity basis vector of the normal-form module, as a `Matrix.vecCons`
literal so that `mulσ` indexing reduces by the standard `cons_val` simp set. -/
def e0 : Fin 24 → R := ![1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

/-- `σ₁σ₂` sends the identity basis vector to basis position 8. -/
theorem lhs_at_eight : (L0 R q * L1 R q) (e0 R) 8 = 1 := by
  show mulσ0 (hp R q) (mulσ1 (hp R q) (e0 R)) 8 = 1
  simp [mulσ0, mulσ1, e0]

/-- `σ₂σ₁` sends it to position 7 instead, so position 8 is zero. -/
theorem rhs_at_eight : (L1 R q * L0 R q) (e0 R) 8 = 0 := by
  show mulσ1 (hp R q) (mulσ0 (hp R q) (e0 R)) 8 = 0
  simp [mulσ0, mulσ1, e0]

theorem not_commutative : L0 R q * L1 R q ≠ L1 R q * L0 R q := by
  intro hcon
  have h8 := congrFun (LinearMap.congr_fun hcon (e0 R)) 8
  rw [lhs_at_eight, rhs_at_eight] at h8
  exact one_ne_zero h8

/-- Hence the algebra itself is noncommutative — which no rank-1 (indeed no
commutative) model can be. -/
theorem not_commutative_alg : g0 R q * g1 R q ≠ g1 R q * g0 R q := fun hcon =>
  not_commutative R q (congrArg Subtype.val hcon)

/-! ## Open: the rank

`IsHeckeOfFullRank R 4 (H4Alg R q)` — freeness of rank `24 = 4!` — is *not*
established here. The two halves:

* **Independence** of the 24 word operators `W_j` is cheap: `W_j` sends `e0` to
  the `j`-th normal-form basis vector, so a vanishing combination has vanishing
  coefficients.
* **Spanning** needs the `3 × 24` closure table `σₖ · b_j = b_{j'}` (or
  `b_{j'} + h·b_j`). With `mulσ_sq*`, `mulσ_braid*` and `mulσ_farcomm02` proved
  above, each entry is symbolic word reduction — a chain of `rw`s, no coordinate
  expansion — so it is generatable from
  `computations/markov/hecke_regular_nf_table.py`, which already computes the
  reductions.

Until that lands, read `instHeckeAlgebraH4` as what it is: a genuine Hecke
algebra at `n = 4`, noncommutative, whose dimension has not been pinned. -/

end QOU.Hecke.InstanceH4
