import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.Algebra.Prod
import Mathlib.Logic.Function.Basic
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.RingTheory.SimpleRing.Matrix
import Mathlib.RingTheory.HopfAlgebra.Basic
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Algebra.Star.Subalgebra

/-!
# QOU.DescentLemma — Descent preserves the quantum observable universe

**Lemma** ([`lem:descent`](descent-lemma.md)).

The restriction morphism `rₙ : Aₙ → A_{n-1}` yields a Frobenius–Hopf object
such that `(C, A_{n-1}, τ)` is again a QOU. The induced descent homomorphism
`𝔡ₙ : End_C(Aₙ) → End_C(A_{n-1})` is a **surjective algebra homomorphism**,
and it **intertwines the `G_q`-actions** across levels `n` and `n − 1`.

## 2026-09-03 — the conclusion was a field, and the encoding was weaker in
## three separate ways

`structure DescentLemma` carried `endAlgN`, `endAlgPrev` and `descentMap` as
data plus `surjective : Function.Surjective descentMap` — the lemma's
conclusion verbatim — and `descent_surjective` returned that field. AGENTS.md
§3b-cond item 5: with the map chosen by whoever builds the structure, "the
descent map is surjective" reduces to "the surjective map I supplied is
surjective".

A bundled *definition* whose fields are its own axioms would be the accessor
idiom and not a defect. This is not that: the block is a **lemma**
(`label: "lem:descent"`), and its content is that the actual restriction
morphism *yields* such a datum. Nothing here constructs one, so the assertion
was empty rather than merely unproved.

**And the encoding said less than the `.md` in three ways**, none of them
noted in the file:

1. **`→ₗ[R]`, not an algebra map.** The `.md` says *surjective **algebra**
   homomorphism*; a `LinearMap` drops multiplicativity entirely. Corrected
   here to `→ₐ[R]`.
2. **The `G_q`-intertwining is absent.** The `.md`'s second sentence about
   `𝔡ₙ` has no counterpart at all.
3. **The QOU-preservation claim is absent.** That `(C, A_{n-1}, τ)` is again
   a quantum observable universe — the first thing the lemma asserts — is
   nowhere in the Lean.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`descent_surjective` is now a **`Prop`-valued definition over a
caller-supplied algebra homomorphism**. A caller with an actual `𝔡ₙ` takes it
as a hypothesis, and it constrains them because the map is theirs.

`descentSurjective_comp` **derives** the tower statement: descent through two
levels is surjective when each step is. That is what makes the lemma worth
having for a tower `{Aₙ}_{n ≥ 0}` rather than for one pair of levels, and it
is the one consequence available without constructing `End_C(Aₙ)`.

`not_descentSurjective_diagonal` refutes the claim at a concrete algebra map
— the diagonal `ℤ →ₐ[ℤ] ℤ × ℤ`, whose image misses `(1, 0)` — so a `sorry`
over it would read as "true, not yet proved" about something false.

## What is still unencoded

Everything the lemma is about: the brane tower `{Aₙ}`, the restriction
morphism `rₙ`, the Frobenius–Hopf structure, `End_C(Aₙ)`, the `G_q`-actions
and the intertwining, and the archimedean realisation as a surjective
`*`-homomorphism of section algebras. The two algebras and the map are
caller-supplied.

## 2026-11-22 — the descent map, proved where it holds and refuted where it does not

Bean `qou-nfn4`. The proof block (`descent-lemma-proof.md`, Step 4) builds the
descent map from the unit section `ℓ : A_{n-1} → A_n` and the counit
restriction `r : A_n → A_{n-1}`, with `r ∘ ℓ = id` (Step 1: `A_{n-1}` is a
direct summand). The map it then means is the **compression**
`𝔡(φ) = r ∘ φ ∘ ℓ`. Over that datum the section below proves, with no
hypothesis beyond `r ∘ ℓ = id`:

1. `descentCompression_surjective`: compression `End(A_n) → End(A_{n-1})` is a
   surjective **linear** map (lift `φ` to `ℓ ∘ φ ∘ r`).
2. `descentHom_surjective`: on the subalgebra `blockEnd ℓ r` of endomorphisms
   commuting with the idempotent `e = ℓ ∘ r` (the block-diagonal ones),
   compression is a surjective **algebra** homomorphism.

It also proves that the `.md`'s wording, *a surjective algebra homomorphism on
all of `End(A_n)`*, does not follow and is false in the cases one can check:

3. `descentCompression_not_multiplicative`: on `ℤ × ℤ → ℤ` with `ℓ = inl`,
   `r = fst`, the swap `φ` has `𝔡(φ²) = 1` and `𝔡(φ)² = 0`. Step 4's
   "`r_n` preserves multiplication" is a statement about `r_n` on `A_n`; it
   does not make `φ ↦ r ∘ φ ∘ ℓ` multiplicative on `End(A_n)`.
4. `not_surjective_matrix_algHom`: over a field, no algebra map from
   `k × k` matrices onto `j × j` matrices is surjective when `0 < j < k`
   (matrix algebras are simple, so the map would be injective and the
   dimensions `k²`, `j²` would agree). So whenever `End_C(A_n)` is a full
   matrix algebra of size larger than `End_C(A_{n-1})`, **no** surjective
   algebra homomorphism between them exists, by any construction.

Step 4's surjectivity argument ("`ℓ_n` is injective, so its adjoint `r_n` is
surjective") proves that `r_n : A_n → A_{n-1}` is onto; it is a different map
from `𝔡_n`, and items 3 and 4 show the gap is real. What survives is item 2:
the descent homomorphism is an algebra map on the block-diagonal subalgebra.
Whether `End_C` in the category `C` is that subalgebra is not decided here.

Intertwining (added the same day): `descentCompression_intertwines`,
`descentCompression_conj` and `descentHom_sandwich` prove that descent
commutes with every action of the form `φ ↦ Σᵢ ρ(uᵢ) φ ρ(vᵢ)` (group
conjugation, Hopf adjoint action) once `r` and `ℓ` are equivariant. The
equivariance of `r_n`, `ℓ_n` is a hypothesis here; Step 5 derives it from
`r_n` being a Hopf morphism, which is not encoded.

Second addition the same day. `adEnd_hom`, `hopf_r_equivariant`,
`hopf_l_equivariant` and `descentCompression_hopf_intertwines` derive the
equivariance of `r_n`, `ℓ_n` for the Hopf adjoint action from their being
Hopf morphisms (algebra maps with `(f ⊗ f) ∘ Δ = Δ ∘ f` and `f ∘ S = S ∘ f`).
`archDescentHom` and `archDescentHom_surjective` prove the archimedean
statement in a Hilbert-space model: with `ℓ` an isometry and `r = ℓ†`, descent
is a surjective `*`-algebra homomorphism from the operators commuting with
`ℓ ℓ†` onto all bounded operators on the lower level. `descentHom_tower_surjective`
applies the result at every level of a tower.

Still unencoded: the jet object `J¹(A)` and the categorical claim that
restriction yields a Frobenius–Hopf object with `(C, A_{n-1}, τ)` again a QOU
(proof Steps 1–3); the identification of `Γ(J¹ S_n, SU_{q_n}(2))` with the
Hilbert-space operator algebra above (the functor `τ`).

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- **Surjectivity of a descent homomorphism** ([`lem:descent`]), as a
proposition over a caller-supplied algebra map.

`𝔡ₙ : End_C(Aₙ) →ₐ[R] End_C(A_{n-1})` is surjective.

**Named, not asserted.** An algebra homomorphism rather than a linear one,
matching the `.md`; see the module docstring for the two claims of the lemma
that remain unencoded. -/
-- Ref: [leitner2026] §3 Lifting and Descent
def descent_surjective {R A B : Type*} [CommSemiring R] [Semiring A] [Semiring B]
    [Algebra R A] [Algebra R B] (descentMap : A →ₐ[R] B) : Prop :=
  Function.Surjective descentMap

/-- **Descent through the tower, derived.**

If each one-step descent is surjective then so is their composite, so
surjectivity propagates from level `n` down to any lower level of the brane
tower `{Aₙ}_{n ≥ 0}`.

This is why the lemma is stated for a tower rather than a single pair, and it
is the one consequence obtainable without constructing `End_C(Aₙ)`. -/
-- Ref: [leitner2026] §3 Lifting and Descent
theorem descentSurjective_comp {R A B C : Type*} [CommSemiring R]
    [Semiring A] [Semiring B] [Semiring C]
    [Algebra R A] [Algebra R B] [Algebra R C]
    {f : A →ₐ[R] B} {g : B →ₐ[R] C}
    (hf : descent_surjective f) (hg : descent_surjective g) :
    descent_surjective (g.comp f) :=
  hg.comp hf

/-- **The claim is refutable at a concrete algebra map**, which is why it is
named rather than carried as a `sorry`.

The diagonal `ℤ →ₐ[ℤ] ℤ × ℤ` is an algebra homomorphism whose image misses
`(1, 0)`: a preimage would have to equal `1` in the first coordinate and `0`
in the second. -/
theorem not_descentSurjective_diagonal :
    ¬ descent_surjective (Algebra.ofId ℤ (ℤ × ℤ)) := by
  intro h
  obtain ⟨r, hr⟩ := h (1, 0)
  have h1 : r = 1 := congrArg Prod.fst hr
  have h2 : r = 0 := congrArg Prod.snd hr
  omega

section Compression

variable {R M N : Type*} [CommRing R] [AddCommGroup M] [Module R M]
  [AddCommGroup N] [Module R N]

/-- **Compression along a split pair** `ℓ : N → M`, `r : M → N`:
`𝔡(φ) = r ∘ φ ∘ ℓ`. With `ℓ` the unit section and `r` the counit
restriction this is the descent map of `lem:descent`. It is linear; it is not
multiplicative (`descentCompression_not_multiplicative`). -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 4
def descentCompression (ℓ : N →ₗ[R] M) (r : M →ₗ[R] N) :
    Module.End R M →ₗ[R] Module.End R N where
  toFun φ := r ∘ₗ φ ∘ₗ ℓ
  map_add' φ ψ := by ext x; simp
  map_smul' c φ := by ext x; simp

@[simp] lemma descentCompression_apply (ℓ : N →ₗ[R] M) (r : M →ₗ[R] N)
    (φ : Module.End R M) : descentCompression ℓ r φ = r ∘ₗ φ ∘ₗ ℓ := rfl

/-- **Descent is surjective as a linear map**, given only `r ∘ ℓ = id`:
`φ` is the compression of `ℓ ∘ φ ∘ r`. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 4
theorem descentCompression_surjective {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    (hrl : r ∘ₗ ℓ = LinearMap.id) :
    Function.Surjective (descentCompression ℓ r) := by
  intro φ
  refine ⟨ℓ ∘ₗ φ ∘ₗ r, ?_⟩
  ext x
  have h : ∀ y, r (ℓ y) = y := fun y => LinearMap.congr_fun hrl y
  simp [h]

/-- **The block-diagonal endomorphisms**: those commuting with the idempotent
`e = ℓ ∘ r`. They form a subalgebra of `End(M)`, and it is on this subalgebra
that descent is an algebra map. -/
def blockEnd (ℓ : N →ₗ[R] M) (r : M →ₗ[R] N) : Subalgebra R (Module.End R M) where
  carrier := {φ | (ℓ ∘ₗ r) * φ = φ * (ℓ ∘ₗ r)}
  mul_mem' {φ ψ} hφ hψ := by
    simp only [Set.mem_setOf_eq] at *
    rw [← mul_assoc, hφ, mul_assoc, hψ, mul_assoc]
  add_mem' {φ ψ} hφ hψ := by
    simp only [Set.mem_setOf_eq] at *
    rw [mul_add, add_mul, hφ, hψ]
  algebraMap_mem' c := by
    simp only [Set.mem_setOf_eq, Algebra.commutes]

lemma mem_blockEnd {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N} {φ : Module.End R M} :
    φ ∈ blockEnd ℓ r ↔ (ℓ ∘ₗ r) * φ = φ * (ℓ ∘ₗ r) := Iff.rfl

/-- **The descent homomorphism** on block-diagonal endomorphisms, an `R`-algebra
map. Multiplicativity: `r φ ψ ℓ = r φ (ℓ r) ψ ℓ` because `φ` commutes with
`ℓ ∘ r` and `r ∘ ℓ = id`. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 4
def descentHom {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N} (hrl : r ∘ₗ ℓ = LinearMap.id) :
    blockEnd ℓ r →ₐ[R] Module.End R N where
  toFun φ := r ∘ₗ (φ : Module.End R M) ∘ₗ ℓ
  map_one' := by simpa using hrl
  map_mul' φ ψ := by
    have hφ := (mem_blockEnd.mp φ.2)
    have h : ∀ y, r (ℓ y) = y := fun y => LinearMap.congr_fun hrl y
    ext x
    have := LinearMap.congr_fun hφ ((ψ : Module.End R M) (ℓ x))
    simp only [Module.End.mul_apply, LinearMap.comp_apply] at this ⊢
    simp only [Subalgebra.coe_mul, Module.End.mul_apply]
    rw [← this, h]
  map_zero' := by ext x; simp
  map_add' φ ψ := by ext x; simp
  commutes' c := by
    ext x
    have h : ∀ y, r (ℓ y) = y := fun y => LinearMap.congr_fun hrl y
    simp [Algebra.algebraMap_eq_smul_one, h]

/-- **`lem:descent`, in the form that holds**: descent is a surjective algebra
homomorphism from the block-diagonal subalgebra of `End(M)` onto `End(N)`,
for any split pair `r ∘ ℓ = id`. The lift `ℓ ∘ φ ∘ r` is block-diagonal. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 4
theorem descentHom_surjective {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    (hrl : r ∘ₗ ℓ = LinearMap.id) : Function.Surjective (descentHom hrl) := by
  intro φ
  have h : ∀ y, r (ℓ y) = y := fun y => LinearMap.congr_fun hrl y
  refine ⟨⟨ℓ ∘ₗ φ ∘ₗ r, ?_⟩, ?_⟩
  · rw [mem_blockEnd]; ext x; simp [h]
  · ext x; simp [descentHom, h]

/-- **Compression is not multiplicative on all of `End(M)`.** `M = ℤ × ℤ`,
`N = ℤ`, `ℓ = inl`, `r = fst`, `φ` the swap: `𝔡(φ * φ) = 𝔡(1) = 1` but
`𝔡(φ) = 0`. So the `.md`'s "surjective algebra homomorphism" on the whole
of `End(A_n)` is not what Step 4 proves. -/
theorem descentCompression_not_multiplicative :
    let ℓ : ℤ →ₗ[ℤ] ℤ × ℤ := LinearMap.inl ℤ ℤ ℤ
    let r : ℤ × ℤ →ₗ[ℤ] ℤ := LinearMap.fst ℤ ℤ ℤ
    let φ : Module.End ℤ (ℤ × ℤ) := (LinearEquiv.prodComm ℤ ℤ ℤ).toLinearMap
    r ∘ₗ ℓ = LinearMap.id ∧
      descentCompression ℓ r (φ * φ) ≠ descentCompression ℓ r φ * descentCompression ℓ r φ := by
  intro ℓ r φ
  refine ⟨by ext; simp [ℓ, r], fun h => ?_⟩
  have := LinearMap.congr_fun h 1
  simp [ℓ, r, φ] at this

/-! ### Intertwining the `G_q`-actions (`lem:descent`, proof Step 5)

An action on each level is a map `ρ : H → End(M)`, `ρ' : H → End(N)`, and the
split pair is **equivariant** when `r ∘ ρ h = ρ' h ∘ r` and
`ρ h ∘ ℓ = ℓ ∘ ρ' h`. The induced action on endomorphisms is a finite sum of
sandwiches `φ ↦ Σᵢ ρ(uᵢ) φ ρ(vᵢ)`: one term `ρ(g) φ ρ(g⁻¹)` for a group, and
`Σ ρ(h₍₁₎) φ ρ(S h₍₂₎)` for the adjoint action of a Hopf algebra (any
presentation of `Δ h`). Descent commutes with every such operator, so it
intertwines the actions on `End(M)` and `End(N)`. Nothing about `H` is used
beyond the two equivariance equations. -/

/-- **Descent commutes with one sandwich.** -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem descentCompression_sandwich {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    {a b : Module.End R M} {a' b' : Module.End R N}
    (ha : r ∘ₗ a = a' ∘ₗ r) (hb : b ∘ₗ ℓ = ℓ ∘ₗ b') (φ : Module.End R M) :
    descentCompression ℓ r (a * φ * b) = a' * descentCompression ℓ r φ * b' := by
  ext x
  have h1 := LinearMap.congr_fun hb x
  have h2 := LinearMap.congr_fun ha (φ (ℓ (b' x)))
  simp only [LinearMap.comp_apply] at h1 h2
  simp [Module.End.mul_apply, h1, h2]

/-- **Descent intertwines any finite-sum action** `φ ↦ Σᵢ ρ(uᵢ) φ ρ(vᵢ)` built
from an equivariant pair of actions. Covers group conjugation and the Hopf
adjoint action. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem descentCompression_intertwines {H ι : Type*} {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    {ρ : H → Module.End R M} {ρ' : H → Module.End R N}
    (hr : ∀ h, r ∘ₗ ρ h = ρ' h ∘ₗ r) (hl : ∀ h, ρ h ∘ₗ ℓ = ℓ ∘ₗ ρ' h)
    (s : Finset ι) (u v : ι → H) (φ : Module.End R M) :
    descentCompression ℓ r (∑ i ∈ s, ρ (u i) * φ * ρ (v i)) =
      ∑ i ∈ s, ρ' (u i) * descentCompression ℓ r φ * ρ' (v i) := by
  rw [map_sum]
  exact Finset.sum_congr rfl fun i _ => descentCompression_sandwich (hr _) (hl _) φ

/-- **Group case**: for representations `ρ : G →* End(M)`, `ρ' : G →* End(N)`
with `r`, `ℓ` equivariant, descent commutes with conjugation. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem descentCompression_conj {G : Type*} [Group G] {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    {ρ : G →* Module.End R M} {ρ' : G →* Module.End R N}
    (hr : ∀ g, r ∘ₗ ρ g = ρ' g ∘ₗ r) (hl : ∀ g, ρ g ∘ₗ ℓ = ℓ ∘ₗ ρ' g)
    (g : G) (φ : Module.End R M) :
    descentCompression ℓ r (ρ g * φ * ρ g⁻¹) =
      ρ' g * descentCompression ℓ r φ * ρ' g⁻¹ :=
  descentCompression_sandwich (hr g) (hl g⁻¹) φ

/-- **Equivariant actions preserve the block-diagonal subalgebra**: `ρ h`
commutes with `e = ℓ ∘ r`, so a sandwich of a block-diagonal `φ` by `ρ`-values
stays block-diagonal. Hence the action restricts to `blockEnd ℓ r` and the
descent homomorphism `descentHom` is itself equivariant. -/
theorem rho_mem_blockEnd {H : Type*} {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    {ρ : H → Module.End R M} {ρ' : H → Module.End R N}
    (hr : ∀ h, r ∘ₗ ρ h = ρ' h ∘ₗ r) (hl : ∀ h, ρ h ∘ₗ ℓ = ℓ ∘ₗ ρ' h) (h : H) :
    ρ h ∈ blockEnd ℓ r := by
  rw [mem_blockEnd]
  ext x
  have h1 := LinearMap.congr_fun (hr h) x
  have h2 := LinearMap.congr_fun (hl h) (r x)
  simp only [LinearMap.comp_apply] at h1 h2
  simp [Module.End.mul_apply, h1, h2]

/-- **`descentHom` is equivariant** for an equivariant pair of actions. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem descentHom_sandwich {H : Type*} {ℓ : N →ₗ[R] M} {r : M →ₗ[R] N}
    (hrl : r ∘ₗ ℓ = LinearMap.id)
    {ρ : H → Module.End R M} {ρ' : H → Module.End R N}
    (hr : ∀ h, r ∘ₗ ρ h = ρ' h ∘ₗ r) (hl : ∀ h, ρ h ∘ₗ ℓ = ℓ ∘ₗ ρ' h)
    (a b : H) (φ : blockEnd ℓ r) :
    descentHom hrl (⟨ρ a, rho_mem_blockEnd hr hl a⟩ * φ * ⟨ρ b, rho_mem_blockEnd hr hl b⟩) =
      ρ' a * descentHom hrl φ * ρ' b :=
  descentCompression_sandwich (hr a) (hl b) (φ : Module.End R M)

/-- **Along the brane tower.** For any tower of levels with ascent `ℓₙ` and
descent `rₙ` satisfying `rₙ ∘ ℓₙ = id` (the data of
`def:recursive-brane-tower`), descent at every level is a surjective algebra
homomorphism on the block-diagonal subalgebra. -/
-- Ref: [leitner2026] §3 Lifting and Descent
theorem descentHom_tower_surjective {R : Type*} [CommRing R] (level : ℕ → Type*)
    [∀ n, AddCommGroup (level n)] [∀ n, Module R (level n)]
    (ascent : ∀ n, level n →ₗ[R] level (n + 1)) (descent : ∀ n, level (n + 1) →ₗ[R] level n)
    (retraction : ∀ n, descent n ∘ₗ ascent n = LinearMap.id) (n : ℕ) :
    Function.Surjective (descentHom (retraction n)) :=
  descentHom_surjective (retraction n)

end Compression

/-! ### The Hopf adjoint action, and equivariance of `r_n`, `ℓ_n` (proof Step 5)

`adEnd h` is `a ↦ Σ h₍₁₎ a S(h₍₂₎)`. A Hopf morphism, an algebra map `f` with
`(f ⊗ f) ∘ Δ = Δ ∘ f` and `f ∘ S = S ∘ f`, intertwines it: `f ∘ ad_h = ad_{f h} ∘ f`
(`adEnd_hom`). With `r` and `ℓ` both Hopf morphisms and `r ∘ ℓ = id`, the algebra
`A_{n-1}` acts on `A_n` through `ℓ` and on itself, `r` and `ℓ` are equivariant
(`hopf_r_equivariant`, `hopf_l_equivariant`), and descent intertwines the induced
actions on endomorphisms (`descentCompression_hopf_intertwines`). -/

section HopfAction
open TensorProduct
variable {R A B : Type*} [CommRing R] [Ring A] [Ring B] [HopfAlgebra R A] [HopfAlgebra R B]

/-- core of the adjoint action on a tensor -/
def adCore (a : A) (t : A ⊗[R] A) : A :=
  LinearMap.mul' R A (TensorProduct.map (LinearMap.mulRight R a) (HopfAlgebra.antipode R) t)

lemma adCore_add_left (a b : A) (t : A ⊗[R] A) : adCore (R := R) (a + b) t = adCore a t + adCore b t := by
  induction t using TensorProduct.induction_on with
  | zero => simp [adCore]
  | tmul x y => simp [adCore, mul_add, add_mul]
  | add s t hs ht => simp only [adCore, map_add] at *; rw [hs, ht]; abel

lemma adCore_smul_left (c : R) (a : A) (t : A ⊗[R] A) : adCore (R := R) (c • a) t = c • adCore a t := by
  induction t using TensorProduct.induction_on with
  | zero => simp [adCore]
  | tmul x y => simp [adCore]
  | add s t hs ht => simp only [adCore, map_add] at *; rw [hs, ht, smul_add]

/-- The adjoint action `ad_h a = Σ h₍₁₎ a S(h₍₂₎)`, linear in `a`. -/
def adEnd (h : A) : Module.End R A where
  toFun a := adCore a (Coalgebra.comul (R := R) h)
  map_add' a b := adCore_add_left a b _
  map_smul' c a := adCore_smul_left c a _

lemma adCore_hom (f : A →ₐ[R] B)
    (hS : f.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ f.toLinearMap)
    (a : A) (t : A ⊗[R] A) :
    f (adCore a t) = adCore (f a) (TensorProduct.map f.toLinearMap f.toLinearMap t) := by
  induction t using TensorProduct.induction_on with
  | zero => simp [adCore]
  | tmul x y =>
    have := LinearMap.congr_fun hS y
    simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply] at this
    simp [adCore, this]
  | add s t hs ht => simp only [adCore, map_add] at *; rw [hs, ht]

theorem adEnd_hom (f : A →ₐ[R] B)
    (hΔ : TensorProduct.map f.toLinearMap f.toLinearMap ∘ₗ Coalgebra.comul (R := R)
      = Coalgebra.comul (R := R) ∘ₗ f.toLinearMap)
    (hS : f.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ f.toLinearMap)
    (h : A) : f.toLinearMap ∘ₗ adEnd h = adEnd (f h) ∘ₗ f.toLinearMap := by
  ext a
  have := LinearMap.congr_fun hΔ h
  simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply] at this
  simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply, adEnd, LinearMap.coe_mk, AddHom.coe_mk]
  rw [adCore_hom f hS, this]

/-- `r` is equivariant for the action of `A_{n-1}` through `ℓ`. -/
theorem hopf_r_equivariant (r : A →ₐ[R] B) (ℓ : B →ₐ[R] A)
    (hrl : r.toLinearMap ∘ₗ ℓ.toLinearMap = LinearMap.id)
    (hΔ : TensorProduct.map r.toLinearMap r.toLinearMap ∘ₗ Coalgebra.comul (R := R)
      = Coalgebra.comul (R := R) ∘ₗ r.toLinearMap)
    (hS : r.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ r.toLinearMap)
    (x : B) : r.toLinearMap ∘ₗ adEnd (ℓ x) = adEnd x ∘ₗ r.toLinearMap := by
  rw [adEnd_hom r hΔ hS]
  have : r (ℓ x) = x := LinearMap.congr_fun hrl x
  rw [this]

/-- `ℓ` is equivariant for the same action. -/
theorem hopf_l_equivariant (ℓ : B →ₐ[R] A)
    (hΔ : TensorProduct.map ℓ.toLinearMap ℓ.toLinearMap ∘ₗ Coalgebra.comul (R := R)
      = Coalgebra.comul (R := R) ∘ₗ ℓ.toLinearMap)
    (hS : ℓ.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ ℓ.toLinearMap)
    (x : B) : adEnd (ℓ x) ∘ₗ ℓ.toLinearMap = ℓ.toLinearMap ∘ₗ adEnd x :=
  (adEnd_hom ℓ hΔ hS x).symm

/-- **Descent intertwines the Hopf actions**, derived from `r`, `ℓ` being Hopf
morphisms with `r ∘ ℓ = id`. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem descentCompression_hopf_intertwines {ι : Type*} (r : A →ₐ[R] B) (ℓ : B →ₐ[R] A)
    (hrl : r.toLinearMap ∘ₗ ℓ.toLinearMap = LinearMap.id)
    (hΔr : TensorProduct.map r.toLinearMap r.toLinearMap ∘ₗ Coalgebra.comul (R := R)
      = Coalgebra.comul (R := R) ∘ₗ r.toLinearMap)
    (hSr : r.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ r.toLinearMap)
    (hΔl : TensorProduct.map ℓ.toLinearMap ℓ.toLinearMap ∘ₗ Coalgebra.comul (R := R)
      = Coalgebra.comul (R := R) ∘ₗ ℓ.toLinearMap)
    (hSl : ℓ.toLinearMap ∘ₗ HopfAlgebra.antipode R = HopfAlgebra.antipode R ∘ₗ ℓ.toLinearMap)
    (s : Finset ι) (u v : ι → B) (φ : Module.End R A) :
    descentCompression ℓ.toLinearMap r.toLinearMap
        (∑ i ∈ s, adEnd (ℓ (u i)) * φ * adEnd (ℓ (v i))) =
      ∑ i ∈ s, adEnd (u i) * descentCompression ℓ.toLinearMap r.toLinearMap φ * adEnd (v i) :=
  descentCompression_intertwines (ρ := fun x => adEnd (ℓ x)) (ρ' := adEnd)
    (hopf_r_equivariant r ℓ hrl hΔr hSr) (hopf_l_equivariant ℓ hΔl hSl) s u v φ

end HopfAction

/-! ### The archimedean realisation: a surjective `*`-homomorphism

At the archimedean wall the levels are Hilbert spaces `E` (level `n`) and `F`
(level `n − 1`), the section `ℓ : F → E` is an isometry (`ℓ† ℓ = id`) and the
restriction is its adjoint `r = ℓ†`. Then `𝔡(φ) = ℓ† φ ℓ` commutes with the
adjoint (`archDescent_star`), the operators commuting with the projection
`e = ℓ ℓ†` form a `*`-subalgebra (`archBlockEnd`), and descent is a surjective
`*`-algebra homomorphism from it onto all bounded operators on `F`
(`archDescentHom`, `archDescentHom_surjective`). -/

section Archimedean
open ContinuousLinearMap
variable {𝕜 E F : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F]

noncomputable def archDescent (ℓ : F →L[𝕜] E) (φ : E →L[𝕜] E) : F →L[𝕜] F := adjoint ℓ ∘L φ ∘L ℓ

theorem archDescent_star (ℓ : F →L[𝕜] E) (φ : E →L[𝕜] E) :
    archDescent ℓ (star φ) = star (archDescent ℓ φ) := by
  simp only [archDescent, star_eq_adjoint, adjoint_comp, adjoint_adjoint, comp_assoc]

theorem archDescent_surjective {ℓ : F →L[𝕜] E} (hiso : adjoint ℓ ∘L ℓ = ContinuousLinearMap.id 𝕜 F) :
    Function.Surjective (archDescent ℓ) := by
  intro ψ
  refine ⟨ℓ ∘L ψ ∘L adjoint ℓ, ?_⟩
  simp only [archDescent, ← comp_assoc, hiso]
  simp only [comp_assoc, hiso, ContinuousLinearMap.comp_id, ContinuousLinearMap.id_comp]

def archBlockEnd (ℓ : F →L[𝕜] E) : StarSubalgebra 𝕜 (E →L[𝕜] E) where
  carrier := {φ | (ℓ ∘L adjoint ℓ) * φ = φ * (ℓ ∘L adjoint ℓ)}
  mul_mem' {φ ψ} hφ hψ := by
    simp only [Set.mem_setOf_eq] at *
    rw [← mul_assoc, hφ, mul_assoc, hψ, mul_assoc]
  add_mem' {φ ψ} hφ hψ := by
    simp only [Set.mem_setOf_eq] at *
    rw [mul_add, add_mul, hφ, hψ]
  algebraMap_mem' c := by simp only [Set.mem_setOf_eq, Algebra.commutes]
  star_mem' {φ} hφ := by
    simp only [Set.mem_setOf_eq] at *
    have he : star (ℓ ∘L adjoint ℓ) = ℓ ∘L adjoint ℓ := by
      simp [star_eq_adjoint, adjoint_comp]
    have := congrArg star hφ
    rw [star_mul, star_mul, he] at this
    exact this.symm

noncomputable def archDescentHom {ℓ : F →L[𝕜] E} (hiso : adjoint ℓ ∘L ℓ = ContinuousLinearMap.id 𝕜 F) :
    archBlockEnd ℓ →⋆ₐ[𝕜] (F →L[𝕜] F) where
  toFun φ := archDescent ℓ φ
  map_one' := by simpa [archDescent] using hiso
  map_mul' φ ψ := by
    have hφ : (ℓ ∘L adjoint ℓ) * (φ : E →L[𝕜] E) = φ * (ℓ ∘L adjoint ℓ) := φ.2
    ext x
    have := congrArg (fun T : E →L[𝕜] E => adjoint ℓ (T ((ψ : E →L[𝕜] E) (ℓ x)))) hφ
    have h : ∀ y, adjoint ℓ (ℓ y) = y := fun y => by
      simpa using congrArg (fun T : F →L[𝕜] F => T y) hiso
    simp only [mul_apply, comp_apply, h] at this
    simp only [archDescent, MulMemClass.coe_mul, mul_apply, comp_apply]
    exact this
  map_zero' := by ext; simp [archDescent]
  map_add' φ ψ := by ext; simp [archDescent]
  commutes' c := by
    have h : ∀ y, adjoint ℓ (ℓ y) = y := fun y => by
      simpa using congrArg (fun T : F →L[𝕜] F => T y) hiso
    ext x; simp [archDescent, Algebra.algebraMap_eq_smul_one, h]
  map_star' φ := archDescent_star ℓ φ

theorem archDescentHom_surjective {ℓ : F →L[𝕜] E} (hiso : adjoint ℓ ∘L ℓ = ContinuousLinearMap.id 𝕜 F) :
    Function.Surjective (archDescentHom hiso) := by
  intro ψ
  have h : ∀ y, adjoint ℓ (ℓ y) = y := fun y => by
    simpa using congrArg (fun T : F →L[𝕜] F => T y) hiso
  refine ⟨⟨ℓ ∘L ψ ∘L adjoint ℓ, ?_⟩, ?_⟩
  · show (ℓ ∘L adjoint ℓ) * _ = _ * (ℓ ∘L adjoint ℓ)
    ext x; simp [h]
  · ext x; simp [archDescentHom, archDescent, h]

/-- **Archimedean equivariance**: if `ℓ` intertwines `a` with `a'` and `a†`
with `a'†` (e.g. unitaries of a compact group action), descent commutes with
conjugation. -/
-- Ref: [leitner2026] §3 Lifting and Descent, descent-lemma-proof Step 5
theorem archDescent_sandwich (ℓ : F →L[𝕜] E) {a b : E →L[𝕜] E} {a' b' : F →L[𝕜] F}
    (ha : star a ∘L ℓ = ℓ ∘L star a') (hb : b ∘L ℓ = ℓ ∘L b') (φ : E →L[𝕜] E) :
    archDescent ℓ (a * φ * b) = a' * archDescent ℓ φ * b' := by
  have ha' : adjoint ℓ ∘L a = a' ∘L adjoint ℓ := by
    have := congrArg adjoint ha
    simpa [star_eq_adjoint, adjoint_comp] using this
  simp only [archDescent, mul_def, ← comp_assoc, ha']
  simp only [comp_assoc, hb]

end Archimedean

/-- **No surjective algebra map shrinks a full matrix algebra.** Over a field,
for `0 < j < k` no `K`-algebra homomorphism `M_k(K) → M_j(K)` is surjective:
`M_k(K)` is simple, so the map is injective, hence a linear isomorphism, and
`k² = j²` fails. Whenever `End_C(A_n)` and `End_C(A_{n-1})` are full matrix
algebras with the first strictly larger, the `.md`'s statement is false. -/
theorem not_surjective_matrix_algHom {K : Type*} [Field K] {k j : ℕ}
    (hj : 0 < j) (hjk : j < k)
    (f : Matrix (Fin k) (Fin k) K →ₐ[K] Matrix (Fin j) (Fin j) K) :
    ¬ Function.Surjective f := by
  intro hs
  haveI : Nonempty (Fin j) := ⟨⟨0, hj⟩⟩
  haveI : Nonempty (Fin k) := ⟨⟨0, by omega⟩⟩
  have hinj : Function.Injective f := (f.toRingHom).injective
  have e := LinearEquiv.ofBijective f.toLinearMap ⟨hinj, hs⟩
  have := e.finrank_eq
  simp [Module.finrank_matrix] at this
  nlinarith
end QOU
