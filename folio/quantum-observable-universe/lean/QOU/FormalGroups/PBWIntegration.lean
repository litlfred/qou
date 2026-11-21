/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import UGB.GrobnerShirshov.SplayIntegration
import QOU.FormalGroups.SplayPoisson

/-!
# Thm. 3.7 of arXiv:math/0602138: the PBW basis of `U = T / J` for a splay

`UGB.GrobnerShirshov.BlockSplay.Model.integrationBasis` (in the `ugb` package) proves
the PBW half of Thm. 3.7 for any *model*: an algebra `A` with a surjection
`q : MA G k → A` whose kernel is the same-block ideal, and a Poisson bracket whose
values on letters are the corrections `π(a, b)` of a strongly filtered block-splay
system. This file supplies the model for the splay algebra itself.

Setting. Each `Aᵢ` is a commutative `R`-algebra with a basis `bᵢ` indexed by
`Option (Lᵢ)`, with `bᵢ none = 1` (for `Aᵢ = Dist(Hᵢ)`: the divided-power basis
`δx^J`, `J` a multi-index, with `J = 0` the unit). The letters are `G = Σ i, Lᵢ`.

* `letter`, `qT`: the letter `⟨i, x⟩` goes to `ιᵢ (bᵢ x)` in the splay algebra
  `T = ∐ Aᵢ`, and `qT : MA G R → T` is the induced algebra map.
* `qT_surjective`: the letters generate `T`.
* `qT_ker`: **the free product is presented by the multiplication tables**: if
  `qT X = 0` then `X` lies in the same-block ideal. The proof maps `T` back to
  the free algebra modulo the same-block relations, using the universal property
  of the free product; no normal-form argument for `T` is needed.
* `model`: the block-splay model on `T`, with bracket a splay Poisson structure.
* `integrationBasis`: the ordered monomials are an `R`-basis of
  `U = IntegrationQuotient π`.

Hypotheses on the block-splay data `F` (each is the paper's input, written in the
basis): the block of `⟨i, x⟩` is `i`; the block product `μ` is the structure
constants of `Aᵢ` in `bᵢ`; and each correction `π(a, b)` is a preimage of the bracket
of the two letters. The *strong filtration* of Thm. 3.7 is the field `F.π_wt`: those
preimages are lighter than `a b`. Constructing such an `F` from a strongly filtered
`π` (choosing the preimages, the weights and the admissible order) is the next step
and is not done here.

No `sorry`, no axiom beyond Lean's three.
-/

set_option linter.unusedSectionVars false

namespace QOU.FormalGroups.PBW

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond UGB.GrobnerShirshov.Quadratic
  UGB.GrobnerShirshov.BlockSplay LinearAlgebra

noncomputable section

variable {R : Type*} [CommRing R] {I : Type*} [DecidableEq I]
  {A : I → Type*} [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
  {L : I → Type*} [∀ i, DecidableEq (L i)]
  (b : ∀ i, Module.Basis (Option (L i)) R (A i))

/-- The image of the letter `⟨i, x⟩` in the splay algebra: `ιᵢ (bᵢ x)`. -/
def letter (g : Σ i, L i) : SplayAlgebra R A :=
  FreeProduct.ι R A g.1 (b g.1 (some g.2))

/-- The algebra map `MA G R → T` sending each letter to its image. -/
def qT : MA (Σ i, L i) R →ₐ[R] SplayAlgebra R A :=
  MonoidAlgebra.lift R (FreeMonoid (Σ i, L i)) _ (FreeMonoid.lift (letter b))

theorem qT_ofW_single (g : Σ i, L i) : qT b (ofW [g]) = letter b g := by
  simp [qT, ofW, MonoidAlgebra.lift_single]

/-- The word of a basis index: the empty word for the unit, a letter otherwise. -/
def wordOf (i : I) : Option (L i) → MA (Σ i, L i) R
  | none => 1
  | some x => ofW [⟨i, x⟩]

variable {b}

theorem qT_wordOf (hb1 : ∀ i, b i none = 1) (i : I) (o : Option (L i)) :
    qT b (wordOf i o) = FreeProduct.ι R A i (b i o) := by
  cases o with
  | none => rw [wordOf, map_one, hb1, map_one]
  | some x => rw [wordOf, qT_ofW_single]; rfl

/-- **The letters generate the splay algebra.** -/
theorem qT_surjective (hb1 : ∀ i, b i none = 1) : Function.Surjective (qT b) := by
  set S := (qT b).range
  have hι : ∀ i (a : A i), FreeProduct.ι R A i a ∈ S := by
    intro i a
    rw [← (b i).linearCombination_repr a, Finsupp.linearCombination_apply, map_finsuppSum]
    refine Subalgebra.sum_mem _ fun o _ => ?_
    dsimp only
    rw [map_smul]
    exact Subalgebra.smul_mem _ ((AlgHom.mem_range _).2 ⟨_, qT_wordOf hb1 i o⟩) _
  let θ : SplayAlgebra R A →ₐ[R] S :=
    FreeProduct.lift R A fun {i} => (FreeProduct.ι R A i).codRestrict S (hι i)
  have hθ : S.val.comp θ = AlgHom.id R _ := by
    rw [FreeProduct.lift_unique R A (maps := fun {i} => FreeProduct.ι R A i) (S.val.comp θ)
      (fun i => by
        ext a
        rw [AlgHom.comp_apply, AlgHom.comp_apply, ← AlgHom.comp_apply θ, FreeProduct.lift_comp_ι]
        rfl),
      FreeProduct.lift_unique R A (maps := fun {i} => FreeProduct.ι R A i) (AlgHom.id R _)
      (fun i => by ext a; simp)]
  intro x
  have := (θ x).2
  rwa [show (θ x : SplayAlgebra R A) = x from AlgHom.congr_fun hθ x] at this

variable {ord : AdmissibleOrder (Σ i, L i)} [LinearOrder I] [Nontrivial R]
  {F : FilteredData (Σ i, L i) R ord I}

/-- The same-block presentation, as a quotient ring. -/
local notation "P" => RingQuot (QRel F.same)

/-- The basis maps `Aᵢ → P`: the unit to `1`, `bᵢ x` to the class of the letter. -/
def ψLin (b : ∀ i, Module.Basis (Option (L i)) R (A i))
    (F : FilteredData (Σ i, L i) R ord I) (i : I) : A i →ₗ[R] RingQuot (QRel F.same) :=
  (b i).constr R fun o => RingQuot.mkAlgHom R (QRel F.same) (wordOf i o)

variable (hb1 : ∀ i, b i none = 1) (hblk : ∀ g, F.blk g = g.1)
  (hμ : ∀ i (x y : L i), F.μ ⟨i, x⟩ ⟨i, y⟩ =
    ((b i).repr (b i (some x) * b i (some y))).sum fun o c => c • wordOf i o)

include hb1 in
theorem ψLin_one (i : I) : ψLin b F i 1 = 1 := by
  rw [← hb1 i, ψLin, Module.Basis.constr_basis, wordOf, map_one]

include hb1 hblk hμ in
theorem ψLin_mul (i : I) (x y : A i) :
    ψLin b F i (x * y) = ψLin b F i x * ψLin b F i y := by
  set f := ψLin b F i
  have key : ((LinearMap.mul R (A i)).compr₂ f) =
      (LinearMap.mul R P).compl₁₂ f f := by
    refine (b i).ext fun u => (b i).ext fun v => ?_
    simp only [LinearMap.compr₂_apply, LinearMap.mul_apply', LinearMap.compl₁₂_apply]
    rcases u with _ | u
    · rw [hb1, one_mul, ψLin_one hb1, one_mul]
    rcases v with _ | v
    · rw [hb1, mul_one, ψLin_one hb1, mul_one]
    have hpair : (⟨i, u⟩, ⟨i, v⟩) ∈ F.same.pairs := by
      show F.blk ⟨i, u⟩ = F.blk ⟨i, v⟩
      rw [hblk, hblk]
    have hrel := RingQuot.mkAlgHom_rel R (QRel.of (d := F.same) ⟨_, hpair⟩)
    simp only [f, ψLin, Module.Basis.constr_basis, wordOf]
    rw [← map_mul (RingQuot.mkAlgHom R (QRel F.same)), ← ofW_append]
    change RingQuot.mkAlgHom R (QRel F.same) (ofW [⟨i, u⟩, ⟨i, v⟩]) =
      RingQuot.mkAlgHom R (QRel F.same) (F.μ ⟨i, u⟩ ⟨i, v⟩) at hrel
    change _ = RingQuot.mkAlgHom R (QRel F.same) (ofW [⟨i, u⟩, ⟨i, v⟩])
    rw [hrel, hμ, Module.Basis.constr_apply, map_finsuppSum]
    simp only [map_smul]
    rfl
  exact LinearMap.congr_fun₂ key x y

/-- The algebra maps `Aᵢ → P`. -/
def ψᵢ (i : I) : A i →ₐ[R] RingQuot (QRel F.same) :=
  AlgHom.ofLinearMap (ψLin b F i) (ψLin_one hb1 i) (ψLin_mul hb1 hblk hμ i)

/-- The map `T → P` out of the free product. -/
def ψ : SplayAlgebra R A →ₐ[R] RingQuot (QRel F.same) :=
  FreeProduct.lift R A fun {i} => ψᵢ hb1 hblk hμ i

include hb1 hblk hμ in
theorem ψ_comp_qT : (ψ hb1 hblk hμ).comp (qT b) = RingQuot.mkAlgHom R (QRel F.same) := by
  refine MA_algHom_ext fun g => ?_
  rw [AlgHom.comp_apply, qT_ofW_single, letter, ψ,
    ← AlgHom.comp_apply (FreeProduct.lift R A _), FreeProduct.lift_comp_ι]
  simp [ψᵢ, ψLin, Module.Basis.constr_basis, wordOf]

include hb1 hblk hμ in
/-- **The free product is presented by the block multiplication tables.** -/
theorem qT_ker (X : MA (Σ i, L i) R) (h : qT b X = 0) : InId F.same.sys X := by
  apply F.same.inId_of_mk_eq_zero
  rw [← ψ_comp_qT hb1 hblk hμ, AlgHom.comp_apply, h, map_zero]

include hb1 hblk hμ in
/-- The block products are realised in the splay algebra. -/
theorem qT_μ (a c : Σ i, L i) (h : F.blk a = F.blk c) :
    qT b (F.μ a c) = qT b (ofW [a]) * qT b (ofW [c]) := by
  obtain ⟨i, x⟩ := a
  obtain ⟨j, y⟩ := c
  rw [hblk, hblk] at h
  dsimp only at h
  subst h
  rw [hμ, map_finsuppSum, qT_ofW_single, qT_ofW_single, letter, letter]
  dsimp only
  rw [← map_mul (FreeProduct.ι R A i)]
  conv_rhs => rw [← (b i).linearCombination_repr (b i (some x) * b i (some y)),
    Finsupp.linearCombination_apply, map_finsuppSum]
  simp only [map_smul, qT_wordOf hb1]

variable (π : SplayPoisson R A)
  (hπ : ∀ a c, F.blk c < F.blk a →
    qT b (F.π a c) = π.toPoissonStructure.bracket (letter b a) (letter b c))

/-- **The block-splay model on the splay algebra**, with bracket the splay Poisson
    structure `π`. -/
def model : Model F (SplayAlgebra R A) where
  q := qT b
  ker := qT_ker hb1 hblk hμ
  qμ := qT_μ hb1 hblk hμ
  br := π.toPoissonStructure.bracket
  skew := π.toPoissonStructure.skew
  leib x y z := by rw [π.toPoissonStructure.leibniz_right, add_comm]
  jacobi := π.toPoissonStructure.jacobi
  qπ a c h := by rw [qT_ofW_single, qT_ofW_single]; exact hπ a c h
  same a c h := by
    obtain ⟨i, x⟩ := a
    obtain ⟨j, y⟩ := c
    rw [hblk, hblk] at h
    dsimp only at h
    subst h
    rw [qT_ofW_single, qT_ofW_single]
    exact SplayPoisson.bracket_ι_ι R A π i _ _

omit [LinearOrder I] [Nontrivial R] in
/-- The quotient by `IntRel` is the integration quotient of `SplayPoisson.lean`. -/
def intEquiv {T : Type*} [Ring T] [Algebra R T] (ρ : PoissonStructure R T) :
    RingQuot (IntRel ρ.bracket) ≃ₐ[R] IntegrationQuotient ρ :=
  AlgEquiv.ofAlgHom
    (RingQuot.liftAlgHom R ⟨integrationMk ρ, by
      rintro _ _ ⟨x, y⟩; exact RingQuot.mkAlgHom_rel R (IntegrationRel.of x y)⟩)
    (RingQuot.liftAlgHom R ⟨RingQuot.mkAlgHom R _, by
      rintro _ _ ⟨x, y⟩; exact RingQuot.mkAlgHom_rel R (IntRel.of x y)⟩)
    (by apply RingQuot.ringQuot_ext'; ext x; simp [integrationMk])
    (by apply RingQuot.ringQuot_ext'; ext x; simp [integrationMk])

include hb1 hblk hμ hπ in
/-- **Thm. 3.7 of arXiv:math/0602138, PBW half, for the splay.** The images of the
    ordered monomials are an `R`-basis of `U = T / J`, `J = (fg − gf − π(f, g))`. -/
theorem integrationBasis [DecidableEq R] :
    ∃ B : Module.Basis {m : Monomial (Σ i, L i) // NormalFormMonomial ord F.quad.sys m} R
        (IntegrationQuotient π.toPoissonStructure),
      ∀ m, B m = integrationMk _ (qT b (ofW m.val)) := by
  obtain ⟨B, hB⟩ := (model hb1 hblk hμ π hπ).integrationBasis (qT_surjective hb1)
  refine ⟨B.map (intEquiv π.toPoissonStructure).toLinearEquiv, fun m => ?_⟩
  rw [Module.Basis.map_apply, hB]
  simp [intEquiv, model]

end

end QOU.FormalGroups.PBW
