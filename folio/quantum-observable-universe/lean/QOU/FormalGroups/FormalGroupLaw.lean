import Mathlib.RingTheory.MvPowerSeries.Substitution

/-!
# Formal group laws (infrastructure)

Mathlib has power series and their substitution (`MvPowerSeries.subst`) but no formal
group laws. This file adds them, in any finite dimension and over any commutative ring,
as the base for the skew-Poisson integration statement
([`thm:skew-poisson-integration`](../../../quantum-observable-universe/models-of-qous/skew-poisson-integration.md),
after [fred2005]).

* `FormalGroupLaw R ι`: a tuple `F = (F_j(X, Y))_{j ∈ ι}` of power series over `R` with zero
  constant terms, `F(X, 0) = X`, `F(0, Y) = Y` and `F(F(X, Y), Z) = F(X, F(Y, Z))`.
  Commutativity is a separate predicate, `IsComm`, so non-commutative laws are included.
* `FormalGroupLaw.map φ`: base change along a ring map `φ : R → S`. For `ℤ_p → 𝔽_p` this is
  reduction modulo `p`. `map_subst` (base change commutes with substitution) is the lemma
  that makes this work; it is not in Mathlib.
* `IsLift φ G H`: `G` reduces to `H` along `φ`.
* Examples: `additive` (commutative, any dimension) and `affine`, the two-dimensional law of
  the affine group `x ↦ (1 + u)x + b`, which is **not** commutative over any nontrivial ring
  (`affine_not_isComm`).

Everything here is sorry-free. Not yet here: formal group homomorphisms, the distribution
algebra `Dist(G)`, the skewed-Poisson structure, and the integration theorem itself.

Building note: this file needs the Mathlib modules `RingTheory.MvPowerSeries.Substitution`
and its import cone (14 modules), which the `lake-cache/qou-v4-24-0` snapshot does not ship.
They build from source with `lean`-direct in about 30 s, but only with `--root=.` and the
Mathlib options `-DautoImplicit=false -DmaxSynthPendingDepth=3`; without `--root` the
auto-generated instance names come out wrong and `PiTopology` fails.

-- Ref: [fred2005]
-/

namespace QOU.FormalGroups

open MvPowerSeries

noncomputable section

variable {R : Type*} [CommRing R] {ι : Type*} [Finite ι]

/-- Substitute two `ι`-tuples `a`, `b` into a series in the variables `Fin 2 × ι`:
`(i, j) ↦ (a, b)ᵢ j`. -/
def subst2 {τ : Type*} (a b : ι → MvPowerSeries τ R) (f : MvPowerSeries (Fin 2 × ι) R) :
    MvPowerSeries τ R :=
  subst (fun p : Fin 2 × ι => (![a, b] : Fin 2 → ι → MvPowerSeries τ R) p.1 p.2) f

/-- The coordinate tuple `(X (k, j))_j` in a series ring with variables `Fin m × ι`. -/
def coords {m : ℕ} (k : Fin m) : ι → MvPowerSeries (Fin m × ι) R := fun j => X (k, j)

/-- Constant coefficient of a tuple is zero. -/
def NoConst {τ : Type*} (a : ι → MvPowerSeries τ R) : Prop := ∀ j, constantCoeff (a j) = 0


section Subst

variable {τ : Type*}

lemma hasSubst2 {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b) :
    HasSubst (fun p : Fin 2 × ι => (![a, b] : Fin 2 → ι → MvPowerSeries τ R) p.1 p.2) :=
  hasSubst_of_constantCoeff_zero (fun p => by
    obtain ⟨k, j⟩ := p; fin_cases k <;> simp [ha j, hb j])

lemma subst2_X {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b)
    (k : Fin 2) (j : ι) :
    subst2 a b (X (k, j)) = (![a, b] : Fin 2 → ι → MvPowerSeries τ R) k j :=
  subst_X (hasSubst2 ha hb) (k, j)

lemma subst2_add {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b)
    (f g : MvPowerSeries (Fin 2 × ι) R) :
    subst2 a b (f + g) = subst2 a b f + subst2 a b g :=
  subst_add (hasSubst2 ha hb) f g

lemma subst2_mul {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b)
    (f g : MvPowerSeries (Fin 2 × ι) R) :
    subst2 a b (f * g) = subst2 a b f * subst2 a b g :=
  subst_mul (hasSubst2 ha hb) f g

lemma constantCoeff_subst2 {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b)
    {f : MvPowerSeries (Fin 2 × ι) R} (hf : constantCoeff f = 0) :
    constantCoeff (subst2 a b f) = 0 := by
  classical
  rw [subst2, constantCoeff_subst (hasSubst2 ha hb)]
  apply finsum_eq_zero_of_forall_eq_zero
  intro d
  by_cases hd : d = 0
  · subst hd; simp [hf]
  · obtain ⟨t, ht⟩ := Finsupp.ne_iff.mp hd
    have h0 : constantCoeff (d.prod fun p e =>
        (![a, b] : Fin 2 → ι → MvPowerSeries τ R) p.1 p.2 ^ e) = 0 := by
      rw [Finsupp.prod, map_prod]
      apply Finset.prod_eq_zero (i := t) (Finsupp.mem_support_iff.mpr ht)
      rw [map_pow]
      have ht' : d t ≠ 0 := ht
      have hc : constantCoeff ((![a, b] : Fin 2 → ι → MvPowerSeries τ R) t.1 t.2) = 0 := by
        obtain ⟨k, j⟩ := t; fin_cases k <;> simp [ha j, hb j]
      rw [hc, zero_pow ht']
    rw [h0, smul_zero]

omit [Finite ι] in
lemma noConst_coords {m : ℕ} (k : Fin m) : NoConst (coords (R := R) (ι := ι) k) :=
  fun j => by simp [coords]

omit [Finite ι] in
lemma noConst_zero : NoConst (0 : ι → MvPowerSeries τ R) := fun j => by simp

lemma noConst_subst2 {a b : ι → MvPowerSeries τ R} (ha : NoConst a) (hb : NoConst b)
    {F : ι → MvPowerSeries (Fin 2 × ι) R} (hF : NoConst F) :
    NoConst (fun i => subst2 a b (F i)) := fun i => constantCoeff_subst2 ha hb (hF i)

/-- Base change commutes with substitution. -/

theorem map_subst {S σ τ : Type*} [CommRing S] (φ : R →+* S) {a : σ → MvPowerSeries τ R} (ha : HasSubst a) (f : MvPowerSeries σ R) :
    map φ (subst a f) = subst (fun s => map φ (a s)) (map φ f) := by
  have ha' : HasSubst (fun s => map φ (a s)) := by
    refine ⟨fun s => ?_, ?_⟩
    · obtain ⟨n, hn⟩ := ha.const_coeff s
      exact ⟨n, by rw [← coeff_zero_eq_constantCoeff_apply, coeff_map, coeff_zero_eq_constantCoeff_apply, ← map_pow, hn, map_zero]⟩
    · intro d
      exact (ha.coeff_zero d).subset fun s hs => by
        simp only [Set.mem_setOf_eq, coeff_map] at hs ⊢
        intro h; exact hs (by rw [h, map_zero])
  ext e
  rw [coeff_map, coeff_subst ha, coeff_subst ha']
  have := (φ.toAddMonoidHom).map_finsum (coeff_subst_finite ha f e)
  simp only [RingHom.toAddMonoidHom_eq_coe, AddMonoidHom.coe_coe] at this
  rw [this]
  refine finsum_congr fun d => ?_
  simp only [smul_eq_mul, map_mul, coeff_map]
  congr 1
  rw [← coeff_map]
  congr 1
  simp only [Finsupp.prod, map_prod, map_pow]

lemma map_subst2 {S : Type*} [CommRing S] (φ : R →+* S) {a b : ι → MvPowerSeries τ R}
    (ha : NoConst a) (hb : NoConst b) (f : MvPowerSeries (Fin 2 × ι) R) :
    map φ (subst2 a b f) =
      subst2 (fun j => map φ (a j)) (fun j => map φ (b j)) (map φ f) := by
  rw [subst2, map_subst φ (hasSubst2 ha hb), subst2]
  congr 1
  funext p; obtain ⟨k, j⟩ := p; fin_cases k <;> rfl

end Subst

variable (R ι) in
/-- An `ι`-dimensional (possibly non-commutative) formal group law over `R`: a tuple
`F = (F_j(X, Y))_{j ∈ ι}` with zero constant terms, `F(X, 0) = X`, `F(0, Y) = Y`, and
`F(F(X, Y), Z) = F(X, F(Y, Z))`. -/
structure FormalGroupLaw where
  F : ι → MvPowerSeries (Fin 2 × ι) R
  noConst : NoConst F
  unit_left : (fun j => subst2 (coords 0) 0 (F j)) = (coords (m := 1) 0 : ι → _)
  unit_right : (fun j => subst2 0 (coords 0) (F j)) = (coords (m := 1) 0 : ι → _)
  assoc : (fun j => subst2 (fun i => subst2 (coords 0) (coords 1) (F i)) (coords 2) (F j)) =
    (fun j => subst2 (coords (m := 3) 0) (fun i => subst2 (coords 1) (coords 2) (F i)) (F j))

namespace FormalGroupLaw

/-- `F` is commutative when `F(X, Y) = F(Y, X)`. -/
def IsComm (G : FormalGroupLaw R ι) : Prop :=
  ∀ j, subst2 (coords 1) (coords 0) (G.F j) = G.F j

/-- Base change along `φ : R → S`; for `φ : ℤ_p → 𝔽_p` this is reduction modulo `p`. -/
def map {S : Type*} [CommRing S] (φ : R →+* S) (G : FormalGroupLaw R ι) :
    FormalGroupLaw S ι where
  F j := MvPowerSeries.map φ (G.F j)
  noConst j := by
    rw [← coeff_zero_eq_constantCoeff_apply, coeff_map, coeff_zero_eq_constantCoeff_apply,
      G.noConst j, map_zero]
  unit_left := by
    funext j
    have := congrArg (MvPowerSeries.map φ) (congrFun G.unit_left j)
    rw [map_subst2 φ (noConst_coords 0) noConst_zero] at this
    simpa [coords] using this
  unit_right := by
    funext j
    have := congrArg (MvPowerSeries.map φ) (congrFun G.unit_right j)
    rw [map_subst2 φ noConst_zero (noConst_coords 0)] at this
    simpa [coords] using this
  assoc := by
    funext j
    have := congrArg (MvPowerSeries.map φ) (congrFun G.assoc j)
    rw [map_subst2 φ (noConst_subst2 (noConst_coords 0) (noConst_coords 1) G.noConst)
        (noConst_coords 2),
      map_subst2 φ (noConst_coords 0)
        (noConst_subst2 (noConst_coords 1) (noConst_coords 2) G.noConst)] at this
    simp only [map_subst2 φ (noConst_coords _) (noConst_coords _)] at this
    simpa [coords] using this

theorem map_isComm {S : Type*} [CommRing S] (φ : R →+* S) {G : FormalGroupLaw R ι}
    (hG : G.IsComm) : (G.map φ).IsComm := by
  intro j
  have := congrArg (MvPowerSeries.map φ) (hG j)
  rw [map_subst2 φ (noConst_coords 1) (noConst_coords 0)] at this
  simpa [map, coords] using this

/-- The additive formal group law `F(X, Y) = X + Y`. -/
def additive : FormalGroupLaw R ι where
  F j := X (0, j) + X (1, j)
  noConst j := by simp
  unit_left := by
    funext j
    rw [subst2_add (noConst_coords 0) noConst_zero, subst2_X (noConst_coords 0) noConst_zero,
      subst2_X (noConst_coords 0) noConst_zero]
    simp [coords]
  unit_right := by
    funext j
    rw [subst2_add noConst_zero (noConst_coords 0), subst2_X noConst_zero (noConst_coords 0),
      subst2_X noConst_zero (noConst_coords 0)]
    simp [coords]
  assoc := by
    have h : ∀ {a b : ι → MvPowerSeries (Fin 3 × ι) R} (ha : NoConst a) (hb : NoConst b) (j : ι),
        subst2 a b (X (0, j) + X (1, j)) = a j + b j := fun ha hb j => by
      rw [subst2_add ha hb, subst2_X ha hb, subst2_X ha hb]; rfl
    funext j
    have hab : NoConst (fun i => (coords (R := R) (ι := ι) (m := 3) 0 i + coords 1 i)) :=
      fun i => by simp [coords]
    have hbc : NoConst (fun i => (coords (R := R) (ι := ι) (m := 3) 1 i + coords 2 i)) :=
      fun i => by simp [coords]
    simp only [h (noConst_coords 0) (noConst_coords 1), h (noConst_coords 1) (noConst_coords 2)]
    rw [h hab (noConst_coords 2), h (noConst_coords 0) hbc, add_assoc]

theorem additive_isComm : (additive (R := R) (ι := ι)).IsComm := by
  intro j
  show subst2 (coords 1) (coords 0) (X (0, j) + X (1, j)) = X (0, j) + X (1, j)
  rw [subst2_add (noConst_coords 1) (noConst_coords 0), subst2_X (noConst_coords 1) (noConst_coords 0),
    subst2_X (noConst_coords 1) (noConst_coords 0)]
  simp [coords, add_comm]

/-- The two-dimensional affine-group law: coordinates `(u, b)` of `x ↦ (1 + u) x + b`,
`F(X, Y) = (X₀ + Y₀ + X₀Y₀, X₁ + Y₁ + X₀Y₁)`. It is not commutative (`affine_not_isComm`). -/
def affineF (j : Fin 2) : MvPowerSeries (Fin 2 × Fin 2) R :=
  ![X (0, 0) + X (1, 0) + X (0, 0) * X (1, 0), X (0, 1) + X (1, 1) + X (0, 0) * X (1, 1)] j

lemma subst2_affineF {τ : Type*} {a b : Fin 2 → MvPowerSeries τ R} (ha : NoConst a)
    (hb : NoConst b) (j : Fin 2) :
    subst2 a b (affineF j) = ![a 0 + b 0 + a 0 * b 0, a 1 + b 1 + a 0 * b 1] j := by
  fin_cases j <;>
  · simp only [affineF, Fin.zero_eta, Fin.mk_one, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.head_cons]
    rw [subst2_add ha hb, subst2_add ha hb, subst2_mul ha hb]
    simp only [subst2_X ha hb]
    rfl

def affine : FormalGroupLaw R (Fin 2) where
  F := affineF
  noConst j := by fin_cases j <;> simp [affineF]
  unit_left := by
    funext j
    rw [subst2_affineF (noConst_coords 0) noConst_zero]
    fin_cases j <;> simp [coords]
  unit_right := by
    funext j
    rw [subst2_affineF noConst_zero (noConst_coords 0)]
    fin_cases j <;> simp [coords]
  assoc := by
    have nab : NoConst (fun i => subst2 (coords (R := R) (m := 3) 0) (coords 1) (affineF i)) :=
      noConst_subst2 (noConst_coords 0) (noConst_coords 1) (fun j => by fin_cases j <;> simp [affineF])
    have nbc : NoConst (fun i => subst2 (coords (R := R) (m := 3) 1) (coords 2) (affineF i)) :=
      noConst_subst2 (noConst_coords 1) (noConst_coords 2) (fun j => by fin_cases j <;> simp [affineF])
    funext j
    rw [subst2_affineF nab (noConst_coords 2), subst2_affineF (noConst_coords 0) nbc]
    simp only [subst2_affineF (noConst_coords _) (noConst_coords _)]
    fin_cases j <;> simp [coords] <;> ring

theorem affine_not_isComm [Nontrivial R] : ¬ (affine (R := R)).IsComm := by
  intro h
  have h1 := congrArg (coeff (Finsupp.single (0, 0) 1 + Finsupp.single (1, 1) 1)) (h 1)
  rw [show (affine (R := R)).F 1 = affineF 1 from rfl,
    subst2_affineF (noConst_coords 1) (noConst_coords 0)] at h1
  classical
  simp [coords] at h1
  rw [show affineF (R := R) 1 = X (0, 1) + X (1, 1) + X (0, 0) * X (1, 1) from rfl,
    map_add, map_add] at h1
  have e1 : (Finsupp.single ((0 : Fin 2), (0 : Fin 2)) 1 + Finsupp.single (1, 1) 1)
      ≠ Finsupp.single (1, 1) 1 := fun h => by
    have := congrArg (fun f => f (0, 0)) h; simp at this
  have e2 : (Finsupp.single ((0 : Fin 2), (0 : Fin 2)) 1 + Finsupp.single (1, 1) 1)
      ≠ Finsupp.single (0, 1) 1 := fun h => by
    have := congrArg (fun f => f (0, 0)) h; simp at this
  have e3 : (Finsupp.single ((0 : Fin 2), (0 : Fin 2)) 1 + Finsupp.single (1, 1) 1)
      ≠ Finsupp.single (1, 0) 1 + Finsupp.single (0, 1) 1 := fun h => by
    have := congrArg (fun f => f (0, 0)) h; simp at this
  set d := (Finsupp.single ((0 : Fin 2), (0 : Fin 2)) 1 + Finsupp.single (1, 1) 1)
  have c1 : coeff d (X (1, 1) : MvPowerSeries (Fin 2 × Fin 2) R) = 0 := by
    rw [coeff_X, if_neg e1]
  have c2 : coeff d (X (0, 1) : MvPowerSeries (Fin 2 × Fin 2) R) = 0 := by
    rw [coeff_X, if_neg e2]
  have hX : ∀ s, (X s : MvPowerSeries (Fin 2 × Fin 2) R) = monomial (Finsupp.single s 1) 1 :=
    fun s => rfl
  have c3 : coeff d (X (1, 0) * X (0, 1) : MvPowerSeries (Fin 2 × Fin 2) R) = 0 := by
    rw [hX, hX, monomial_mul_monomial, coeff_monomial, if_neg e3]
  have c4 : coeff d (X (0, 0) * X (1, 1) : MvPowerSeries (Fin 2 × Fin 2) R) = 1 := by
    rw [hX, hX, monomial_mul_monomial, coeff_monomial, if_pos rfl, mul_one]
  rw [c1, c2, c3, c4] at h1
  simp at h1

/-- `G` reduces to `H` along `φ` (for `φ : ℤ_p → 𝔽_p`: `G ⊗ 𝔽_p ≅ H` with equality of
coordinates). -/
def IsLift {S : Type*} [CommRing S] (φ : R →+* S) (G : FormalGroupLaw R ι)
    (H : FormalGroupLaw S ι) : Prop :=
  (G.map φ).F = H.F

/-- A commutative law reduces to a commutative law. Contrapositive: a non-commutative
reduction can only come from a non-commutative lift. -/
theorem IsLift.isComm {S : Type*} [CommRing S] {φ : R →+* S} {G : FormalGroupLaw R ι}
    {H : FormalGroupLaw S ι} (h : IsLift φ G H) (hG : G.IsComm) : H.IsComm := by
  intro j
  have := map_isComm φ hG j
  simp only [IsLift] at h
  rwa [h] at this

end FormalGroupLaw
end
end QOU.FormalGroups
