import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.Data.Fintype.Perm
import QOU.BraidKnot.RegularRepTrace
import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.BraidKnot.RegularRepBlockTrace — side 2 (Wedderburn block trace) of Identity (B)

[`RegularRepTrace`](RegularRepTrace.lean) discharged **side 1** of the Identity-(B) trace equation:
`tr_reg(C₂) = n!·binom(n,2)` over any `CommRing R`, ℂ-free. This file discharges **side 2** —
`tr_reg(C₂) = Σ_λ dim(λ)²·ω_λ` — as a **rigorous conditional result** (§3b-cond), the only
unproved input being a single hypothesis bundle that Mathlib does not yet provide.

## The Mathlib gap, isolated

Side 2 needs the **Wedderburn block decomposition** of `R[S_n]` together with the **Jucys–Murphy
eigenvalue theorem** (the central `C₂ = Σ_k X_k²` acts on the `λ`-isotypic block by the scalar
`ω_λ = Σ_{c∈λ} c(c)²`). Equivalently — and this is all the trace computation actually uses — the
endomorphism `mulLeft C₂` is **diagonalisable with the block spectral decomposition**
`mulLeft C₂ = Σ_λ ω_λ · π_λ`, where `π_λ` projects onto the `λ`-isotypic block (R-dimension
`dim(λ)²`) and `Σ_λ π_λ = id`.

The *existence* of a block decomposition is **semisimplicity**, which **is** in the pinned Mathlib
(`Mathlib.RepresentationTheory.Maschke`: `R[G]` is semisimple when `|G|` is invertible in `R`).
What is **not** in Mathlib is the **S_n-specific Okounkov–Vershik layer** pinning down *which*
blocks and *which* scalars: the partition ↔ irreducible classification, `dim(λ) = #SYT(λ)`, and the
JM-eigenvalue = contents theorem. That identification — not semisimplicity — is the irreducible
content of the hypothesis below. (`Mathlib.RepresentationTheory.*` is merely missing from this
sandbox's partial olean cache; it builds from the pinned commit, so the gap is genuinely the
Okounkov–Vershik mathematics, not a toolchain artifact.)

`SnWedderburnSpectralData` bundles exactly that hypothesis. Everything downstream of it is **fully
proved** in pure linear algebra (trace is linear; trace of a projection is the rank of its range,
`LinearMap.IsProj.trace`; `finrank (R[S_n]) = n!`), so the theorems are honest conditional results:
*if* the spectral decomposition exists, *then* the conclusions hold — verified by Lean modulo the
single named structural input.

## What is derived (non-degenerate — the conclusions are produced, not assumed)

- `blockTrace_eq`  — `tr_reg(C₂) = Σ_λ ω_λ·dim(λ)²` (**side 2**). The quadratic `dim(λ)²` is
  *produced* by `IsProj.trace` (= `finrank` of the rank-`dim(λ)²` block), not carried as a field.
- `sumSq_dim_eq`  — `Σ_λ dim(λ)² = n!` (the **RSK sum-of-squares**, the "dim side" the gate note
  flagged as needing HLF/RSK). Produced from completeness `Σ π_λ = id` and `tr(id) = finrank = n!`.
- `identityB_conditional` — `Σ_λ dim(λ)²·ω_λ = n!·binom(n,2)`: **Identity (B)** itself, obtained by
  equating side 2 (`blockTrace_eq`) with side 1 (`RegularRepTrace.trace_centralC2_…`).

To read `ω_λ` as the content-square sum `Σ_{c∈λ} c(c)²` (so `identityB_conditional` becomes the
literal Plancherel content-square mean of the keystone) is the residual JM-eigenvalue identification;
the sibling `IdentityIContentDecomposition.idB_verified_le12` confirms the same equality
numerically for all partitions of `n ≤ 12`.

Base ring: `Field R`. Side 2 is genuinely a field phenomenon — semisimplicity / Wedderburn fails
over a general `CommRing` — so `Field` is the weakest typeclass that admits the construction (§7c);
the eigenvalues/contents are integers, hence live in any field. (Side 1 stays `CommRing`-generic and
is reused here by specialisation.)

## References
- [leitner2026] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (B)"
- [vershik2005] Vershik–Okounkov, "A new approach to the representation theory of the symmetric
  groups II" (JM elements; eigenvalues = contents) https://doi.org/10.1007/s10958-005-0421-7
-/

open scoped BigOperators

namespace QOU.BraidKnot.RegularRepBlockTrace

open RegularRepTrace (centralC2)

/-- **The isolated Mathlib gap for side 2.** A Wedderburn / Jucys–Murphy *block spectral
decomposition* of `mulLeft C₂` on the regular representation `R[S_n]`: a finite family of
projections `proj i` onto blocks `p i` of R-dimension `d i ^ 2` (the `λ`-isotypic components,
`dim(λ)²`), the central element acting as the scalar `ω i` on block `i`
(`mulLeft C₂ = Σ_i ω_i · proj_i`), and the blocks exhausting the space (`Σ_i proj_i = id`).

This bundles precisely the **S_n Okounkov–Vershik content not in Mathlib** (the partition ↔
irreducible classification, `dim(λ) = #SYT(λ)`, and JM eigenvalues = contents) that pins the blocks
and scalars; the *existence* of such a decomposition is semisimplicity (`RepresentationTheory.Maschke`,
which is in Mathlib). Every theorem below is proved outright *given* such a datum. -/
structure SnWedderburnSpectralData (R : Type*) [Field R] (n : ℕ) where
  /-- Index of the irreducible blocks (the partitions of `n`). -/
  Idx : Type
  [fintypeIdx : Fintype Idx]
  /-- `d i = dim(λ_i)`, the dimension of the `i`-th irreducible. -/
  d : Idx → ℕ
  /-- `ω i` = the scalar by which `C₂` acts on block `i` (the JM eigenvalue `Σ_{c∈λ_i} c(c)²`). -/
  ω : Idx → R
  /-- The `i`-th isotypic block (R-dimension `d i ^ 2`). -/
  p : Idx → Submodule R (MonoidAlgebra R (Equiv.Perm (Fin n)))
  /-- The projection onto block `i`. -/
  proj : Idx → Module.End R (MonoidAlgebra R (Equiv.Perm (Fin n)))
  /-- `proj i` is the projection onto `p i`. -/
  isProj : ∀ i, LinearMap.IsProj (p i) (proj i)
  /-- The `i`-th isotypic block has R-dimension `dim(λ_i)²`. -/
  rank : ∀ i, Module.finrank R (p i) = d i ^ 2
  /-- **Block spectral decomposition**: `C₂` acts as the scalar `ω i` on block `i`. -/
  decomp : LinearMap.mulLeft R (centralC2 (R := R) n) = ∑ i, ω i • proj i
  /-- The blocks exhaust the regular representation. -/
  complete : ∑ i, proj i = LinearMap.id

attribute [instance] SnWedderburnSpectralData.fintypeIdx

variable {R : Type*} [Field R] {n : ℕ}

/-- **Side 2 of the Identity-(B) trace equation.** Given a Wedderburn/JM block spectral
decomposition, the trace of `mulLeft C₂` on the regular representation is `Σ_i ω_i · dim(λ_i)²`.
The `dim(λ_i)²` weighting is *produced* by `LinearMap.IsProj.trace` (the trace of the block
projection equals the rank `d i ^ 2` of its range), not assumed. -/
theorem blockTrace_eq (W : SnWedderburnSpectralData R n) :
    LinearMap.trace R (MonoidAlgebra R (Equiv.Perm (Fin n)))
        (LinearMap.mulLeft R (centralC2 (R := R) n))
      = ∑ i, W.ω i * (W.d i : R) ^ 2 := by
  rw [W.decomp, map_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [map_smul, (W.isProj i).trace, W.rank i, smul_eq_mul]
  push_cast
  ring

/-- **RSK sum-of-squares, conditional.** `Σ_i dim(λ_i)² = n!` — the "dimension side" the
`Δ_λ`-gate note flagged as needing HLF/RSK. Produced from completeness `Σ_i proj_i = id`,
`tr(id) = finrank = |S_n| = n!`, and `tr(proj_i) = dim(λ_i)²`. -/
theorem sumSq_dim_eq (W : SnWedderburnSpectralData R n) :
    ∑ i, (W.d i : R) ^ 2 = (n.factorial : R) := by
  have hM : Module.finrank R (MonoidAlgebra R (Equiv.Perm (Fin n))) = n.factorial := by
    unfold MonoidAlgebra
    rw [Module.finrank_finsupp_self, Fintype.card_perm, Fintype.card_fin]
  have h := congrArg (LinearMap.trace R (MonoidAlgebra R (Equiv.Perm (Fin n)))) W.complete
  rw [map_sum, LinearMap.trace_id, hM] at h
  rw [← h]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [(W.isProj i).trace, W.rank i]
  push_cast
  ring

/-- **Identity (B), conditional on the Wedderburn/JM block spectral decomposition.**
`Σ_i dim(λ_i)²·ω_i = n!·binom(n,2)`, obtained by equating **side 2** (`blockTrace_eq`) with
**side 1** (`RegularRepTrace.trace_centralC2_eq_factorial_mul_choose_two`, proved unconditionally
over any `CommRing`). Reading `ω_i = Σ_{c∈λ_i} c(c)²` (the JM eigenvalue) makes this the literal
Plancherel content-square mean carried by the keystone. -/
theorem identityB_conditional (W : SnWedderburnSpectralData R n) :
    ∑ i, W.ω i * (W.d i : R) ^ 2 = (n.factorial : R) * (n.choose 2 : R) := by
  rw [← blockTrace_eq W]
  exact RegularRepTrace.trace_centralC2_eq_factorial_mul_choose_two n

open QOU.BraidKnot.IdentityI (dimHLF sumSqContents) in
/-- **Identity (B) in literal content form, conditional (Layer 2).** Reading off each block `i` as a
partition `κ i` whose dimension is the Frame–Robinson–Thrall hook-length value `dimHLF (κ i)` and
whose Jucys–Murphy eigenvalue is the content-square sum `sumSqContents (κ i) = Σ_{c∈κ i} c(c)²`
(the two identifications that the assumed Wedderburn/JM bundle supplies), `identityB_conditional`
becomes the **literal Plancherel content-square mean**
`Σ_i dim(κ i)²·(Σ_{c∈κ i} c²) = n!·binom(n,2)`. This is the **general-`n`** counterpart of the
sibling's bounded check `IdentityI.idB_verified_le12` (`n ≤ 12`): the same per-partition summand
`dimHLF² · sumSqContents` (cf. `IdentityI.identityB_lhs`), now an identity for all `n` modulo the
single Wedderburn/JM hypothesis. -/
theorem identityB_content_form (W : SnWedderburnSpectralData R n)
    (κ : W.Idx → List ℕ)
    (hd : ∀ i, W.d i = dimHLF (κ i))
    (hω : ∀ i, W.ω i = (sumSqContents (κ i) : R)) :
    ∑ i, (dimHLF (κ i) : R) ^ 2 * (sumSqContents (κ i) : R)
      = (n.factorial : R) * (n.choose 2 : R) := by
  rw [← identityB_conditional W]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [hω i, hd i]
  ring

/-! ## Non-vacuity — the hypothesis bundle is satisfiable

The conditional results above are vacuous if `SnWedderburnSpectralData` cannot be instantiated, so we
exhibit the degenerate `n = 0` witness. `R[S_0] ≅ R` is one-dimensional; the single (empty) partition
has `dim = 1`, and `C₂ = 0` (an empty `Fin 0` sum) so its eigenvalue is `ω = 0` and the lone block is
the whole space. This sorry-free instance certifies that the structure is consistent / not
over-constrained. (Non-degenerate instances, `n ≥ 2`, require the actual Wedderburn block
decomposition — the isolated Mathlib gap this file is conditional on.) -/
noncomputable def spectralData_zero : SnWedderburnSpectralData R 0 where
  Idx := Unit
  d := fun _ => 1
  ω := fun _ => 0
  p := fun _ => ⊤
  proj := fun _ => LinearMap.id
  isProj := fun _ => ⟨fun _ => Submodule.mem_top, fun _ _ => rfl⟩
  rank := fun _ => by
    have h1 : Module.finrank R (MonoidAlgebra R (Equiv.Perm (Fin 0))) = 1 := by
      unfold MonoidAlgebra
      rw [Module.finrank_finsupp_self, Fintype.card_perm, Fintype.card_fin, Nat.factorial_zero]
    rw [finrank_top, h1, one_pow]
  decomp := by
    rw [show centralC2 (R := R) 0 = 0 from by simp [centralC2], LinearMap.mulLeft_zero_eq_zero]
    simp
  complete := by simp

end QOU.BraidKnot.RegularRepBlockTrace
