import QOU.Mass.HeckeMonodromy
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Linear
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Tactic.CategoryTheory.Monoidal.Basic

/-!
# Braid relations on `V^{⊗n}` for every `n`, from a braided monoidal category

Bridge A, step A4 of `docs/audits/2026-11-15-derivation-chain-audit.md` (project copy:
`derivation-chain-audit-2026-11-15.md`, §2 and §8 step 8). The step-2 class
`QOU.Mass.HeckeMonodromy` asks for the Hecke quadratic, the braid relation and far commutation on
every generator of a tower. This file derives the last two **categorically**, for every number of
strands, with no holonomy computation.

## The construction

In a monoidal category `C` with an object `V`, put `V^{⊗0} = 𝟙`, `V^{⊗(n+1)} = V^{⊗n} ⊗ V`
(`tpow`). For any endomorphism `f` of `V ⊗ V`, let `strand f n i` act by `f` on the factors
`i, i+1` of `V^{⊗n}` and by the identity elsewhere (`strand`; the identity when `i + 1 ≥ n`).

## What is proved (sorry-free, no hypotheses beyond those stated)

* `strand_far` — far commutation `σ_i σ_j = σ_j σ_i` for `i + 2 ≤ j`, for **any** `f`
  (interchange law and associator naturality).
* `strand_braid` — the braid relation `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}` for every `n`,
  for any `f` satisfying the three-strand relation `IsYB f`. The general case is the three-strand
  case whiskered by `V^{⊗i}` and conjugated by a structural isomorphism (`whisker_last_two`,
  `last_pair_succ`; both are coherence, closed by Mathlib's `monoidal` tactic).
* `isYB_braiding` — in a braided category, `f = β_{V,V}` satisfies `IsYB`. This is Mathlib's
  `BraidedCategory.yang_baxter`, i.e. the hexagon axioms.
* `strand_quad` — in a `K`-linear monoidal category, if `f² = h f + 1` then every `σ_i`
  (`i + 1 < n`) satisfies the same quadratic.
* `isYB_smul` — a scalar multiple of a solution is a solution, so the rescaled braiding of the
  Drinfeld category `D_ℏ` (`QOU.KZ.Drinfeld.hecke_DH`) also qualifies.

## Drinfeld–Kohno as a hypothesis (`BraidedMonodromy`)

The Drinfeld–Kohno theorem says that the monodromy functor of the KZ connection is braided
monoidal: the KZ monodromy generators on `V^{⊗n}` are the images of the categorical braid
generators. The class `BraidedMonodromy` states exactly that for a Markov-trace tower `T` over a
commutative ring `R`, with a ring map `φ : R → K` to the scalars of the category: there are ring
maps `ρ_n : End(V^{⊗n}) → A`, semilinear along `φ`, with `ρ_n(σ_i) = T.g i`. It is a
**hypothesis**; no instance is claimed for the framework's substrate connection (bean `qou-d0qq`).

`heckeMonodromy_of_braided` assembles the step-2 class `HeckeMonodromy` from

1. `BraidedMonodromy` (Drinfeld–Kohno), and
2. the two-strand Hecke quadratic for `f` (in the KZ model this is
   `QOU.Mass.KohnoTwoPoint.kzExchange_quad`; in `D_ℏ` it is `QOU.KZ.Drinfeld.hecke_DH`),

plus a shadow map `ε` lying over `q ↦ 1`, which is passed separately.

**A category at one fixed coupling cannot supply the shadow.** `subsingleton_of_fixed_coupling`:
if the monodromy factors through a `K`-linear category with `K` a field and `φ(q) ≠ 1`, then every
shadow ring is zero. The `q = 1` shadow needs the coupling to vary, i.e. a tower over a ring such as
`ℤ[q, q⁻¹]` whose monodromy is not pinned to one value of `q`. So this file supplies the Hecke
quadratic, the braid relation and far commutation from Drinfeld–Kohno; the shadow is a statement
about the family, and stays open here.

Base ring §7c: generic `Field K` for the category's scalars, generic `CommRing R` for the tower,
generic `Ring A`; the category is arbitrary. Nothing analytic.

-- Ref: [kassel1995] Kassel, *Quantum Groups*, Thm XIII.1.3 (braided category ⇒ braid group action)
-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — KZ monodromy and the R-matrix
-- Ref: [drinfeld1990] Drinfeld, Leningrad Math. J. 1 (1990) — quasi-Hopf algebras and KZ
-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §5
-/

namespace QOU.Mass.BraidedStrands

open CategoryTheory MonoidalCategory

section Monoidal

variable {C : Type*} [Category C] [MonoidalCategory C] (V : C)

/-- `V^{⊗n}`, nested to the left: `V^{⊗0} = 𝟙`, `V^{⊗(n+1)} = V^{⊗n} ⊗ V`. -/
def tpow : ℕ → C
  | 0 => 𝟙_ C
  | n + 1 => tpow n ⊗ V

/-- `f` acting on the last two factors of `(X ⊗ V) ⊗ V`. -/
def lastPair (f : V ⊗ V ⟶ V ⊗ V) (X : C) : (X ⊗ V) ⊗ V ⟶ (X ⊗ V) ⊗ V :=
  (α_ X V V).hom ≫ X ◁ f ≫ (α_ X V V).inv

/-- `f` acting on the factors `i, i+1` of `V^{⊗n}` (the identity if `i + 1 ≥ n`). -/
def strand (f : V ⊗ V ⟶ V ⊗ V) : (n : ℕ) → ℕ → (tpow V n ⟶ tpow V n)
  | 0, _ => 𝟙 _
  | 1, _ => 𝟙 _
  | n + 2, i => if i = n then lastPair V f (tpow V n) else strand f (n + 1) i ▷ V

variable {V}

theorem strand_last (f : V ⊗ V ⟶ V ⊗ V) (n : ℕ) :
    strand V f (n + 2) n = lastPair V f (tpow V n) := by
  simp [strand]

theorem strand_of_ne (f : V ⊗ V ⟶ V ⊗ V) {n i : ℕ} (h : i ≠ n) :
    strand V f (n + 2) i = strand V f (n + 1) i ▷ V := by
  simp [strand, h]

/-- The three-strand braid relation for `f` on `(V ⊗ V) ⊗ V`:
`(f ⊗ 1)(1 ⊗ f)(f ⊗ 1) = (1 ⊗ f)(f ⊗ 1)(1 ⊗ f)`. -/
def IsYB (f : V ⊗ V ⟶ V ⊗ V) : Prop :=
  f ▷ V ≫ lastPair V f V ≫ f ▷ V = lastPair V f V ≫ f ▷ V ≫ lastPair V f V

/-- The structural isomorphism `((W ⊗ V) ⊗ V) ⊗ V ≅ W ⊗ ((V ⊗ V) ⊗ V)`. -/
def shiftIso (W : C) : ((W ⊗ V) ⊗ V) ⊗ V ≅ W ⊗ ((V ⊗ V) ⊗ V) :=
  whiskerRightIso (α_ W V V) V ≪≫ α_ W (V ⊗ V) V

/-- The second-to-last pair is `W ◁ (f ▷ V)`, up to the structural isomorphism (coherence). -/
theorem whisker_last_two (f : V ⊗ V ⟶ V ⊗ V) (W : C) :
    lastPair V f W ▷ V = (shiftIso W).hom ≫ W ◁ (f ▷ V) ≫ (shiftIso W).inv := by
  simp only [lastPair, shiftIso, Iso.trans_hom, Iso.trans_inv, whiskerRightIso_hom,
    whiskerRightIso_inv, Category.assoc]
  monoidal

/-- The last pair is `W ◁ lastPair f V`, up to the structural isomorphism (coherence). -/
theorem last_pair_succ (f : V ⊗ V ⟶ V ⊗ V) (W : C) :
    lastPair V f (W ⊗ V) = (shiftIso W).hom ≫ W ◁ lastPair V f V ≫ (shiftIso W).inv := by
  simp only [lastPair, shiftIso, Iso.trans_hom, Iso.trans_inv, whiskerRightIso_hom,
    whiskerRightIso_inv, Category.assoc]
  monoidal

omit [MonoidalCategory C] in
/-- Conjugating by an isomorphism respects composition. -/
private theorem conj3 {X Y : C} (e : X ≅ Y) (a b c : Y ⟶ Y) :
    (e.hom ≫ a ≫ e.inv) ≫ (e.hom ≫ b ≫ e.inv) ≫ (e.hom ≫ c ≫ e.inv) =
      e.hom ≫ (a ≫ b ≫ c) ≫ e.inv := by
  simp [Category.assoc]

/-- **The braid relation on `V^{⊗n}`, for every `n`.** If `f` satisfies the three-strand
relation, then `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}` on `V^{⊗n}` whenever `i + 2 < n`. -/
theorem strand_braid (f : V ⊗ V ⟶ V ⊗ V) (hf : IsYB f) :
    ∀ (n i : ℕ), i + 2 < n →
      strand V f n i ≫ strand V f n (i + 1) ≫ strand V f n i =
        strand V f n (i + 1) ≫ strand V f n i ≫ strand V f n (i + 1)
  | 0, _, h => absurd h (by omega)
  | 1, _, h => absurd h (by omega)
  | n + 2, i, h => by
    by_cases hi : i + 1 = n
    · -- the Yang–Baxter case: positions `n − 1, n` of `((W ⊗ V) ⊗ V) ⊗ V`, `W = V^{⊗(n-1)}`
      subst hi
      have e1 : strand V f (i + 1 + 2) (i + 1) = lastPair V f (tpow V i ⊗ V) :=
        strand_last f (i + 1)
      have e2 : strand V f (i + 1 + 2) i = lastPair V f (tpow V i) ▷ V := by
        rw [strand_of_ne f (by omega : i ≠ i + 1)]
        exact congrArg (· ▷ V) (strand_last f i)
      rw [e1, e2, whisker_last_two, last_pair_succ, conj3, conj3,
        ← MonoidalCategory.whiskerLeft_comp, ← MonoidalCategory.whiskerLeft_comp,
        ← MonoidalCategory.whiskerLeft_comp, ← MonoidalCategory.whiskerLeft_comp, hf]
    · -- both crossings are whiskered: induct
      have hi1 : i + 1 ≠ n := hi
      have hi0 : i ≠ n := by omega
      rw [strand_of_ne f hi0, strand_of_ne f hi1, ← comp_whiskerRight, ← comp_whiskerRight,
        ← comp_whiskerRight, ← comp_whiskerRight, strand_braid f hf (n + 1) i (by omega)]

/-- **Far commutation on `V^{⊗n}`, for any `f`.** `σ_i σ_j = σ_j σ_i` whenever `i + 2 ≤ j` and
`j + 1 < n`. -/
theorem strand_far (f : V ⊗ V ⟶ V ⊗ V) :
    ∀ (n i j : ℕ), i + 2 ≤ j → j + 1 < n →
      strand V f n i ≫ strand V f n j = strand V f n j ≫ strand V f n i
  | 0, _, _, _, _ => by simp [strand]
  | 1, _, _, _, _ => by simp [strand]
  | n + 2, i, j, hij, hjn => by
    by_cases hj : j = n
    · subst hj
      by_cases hsmall : i + 1 < j
      · -- `σ_i = (g ▷ V) ▷ V` with `g = σ_i` on `V^{⊗j}`; `σ_j` acts on the last two factors
        obtain ⟨l, rfl⟩ : ∃ l, j = l + 1 := ⟨j - 1, by omega⟩
        have e : strand V f (l + 1 + 2) i = (strand V f (l + 1) i ▷ V) ▷ V := by
          rw [strand_of_ne f (by omega : i ≠ l + 1)]
          congr 1
          exact strand_of_ne f (by omega : i ≠ l)
        rw [e, strand_last, lastPair]
        simp only [← Category.assoc]
        rw [associator_naturality_left]
        simp only [Category.assoc]
        rw [← whisker_exchange_assoc]
        congr 1
        congr 1
        rw [← associator_inv_naturality_left]
      · -- `i + 1 ≥ j ≥ i + 2` is impossible
        omega
    · have hi : i ≠ n := by omega
      rw [strand_of_ne f hi, strand_of_ne f hj, ← comp_whiskerRight, ← comp_whiskerRight,
        strand_far f (n + 1) i j hij (by omega)]

end Monoidal

section Braided

variable {C : Type*} [Category C] [MonoidalCategory C] [BraidedCategory C] (V : C)

/-- **Yang–Baxter from the hexagons.** The braiding `β_{V,V}` satisfies the three-strand
relation; this is Mathlib's `BraidedCategory.yang_baxter` rearranged. -/
theorem isYB_braiding : IsYB (β_ V V).hom := by
  have h := BraidedCategory.yang_baxter V V V
  unfold IsYB lastPair
  rw [← cancel_epi (α_ V V V).inv, ← cancel_mono (α_ V V V).hom]
  simp only [Category.assoc, Iso.inv_hom_id, Iso.inv_hom_id_assoc, Category.comp_id] at h ⊢
  exact h

/-- In a braided category the braid generators on `V^{⊗n}` satisfy the braid relation for every
`n`, with no holonomy computation. -/
theorem braid_relation (n i : ℕ) (h : i + 2 < n) :
    strand V (β_ V V).hom n i ≫ strand V (β_ V V).hom n (i + 1) ≫ strand V (β_ V V).hom n i =
      strand V (β_ V V).hom n (i + 1) ≫ strand V (β_ V V).hom n i ≫
        strand V (β_ V V).hom n (i + 1) :=
  strand_braid (β_ V V).hom (isYB_braiding V) n i h

end Braided

section Linear

variable {K : Type*} [Field K]
variable {C : Type*} [Category C] [MonoidalCategory C] [Preadditive C] [Linear K C]
  [MonoidalPreadditive C] [MonoidalLinear K C] {V : C}

/-- A scalar multiple of a solution of the three-strand relation is a solution. -/
theorem isYB_smul {f : V ⊗ V ⟶ V ⊗ V} (hf : IsYB f) (s : K) : IsYB (s • f) := by
  unfold IsYB lastPair at hf ⊢
  simp only [MonoidalLinear.smul_whiskerRight, MonoidalLinear.whiskerLeft_smul,
    Linear.smul_comp, Linear.comp_smul, smul_smul]
  rw [hf]

/-- The quadratic `f² = h f + 1` is inherited by `X ◁ f`, conjugated by an isomorphism. -/
private theorem quad_conj {X Y Z : C} (e : X ≅ Y ⊗ Z) {f : Z ⟶ Z} {h : K}
    (hf : f ≫ f = h • f + 𝟙 Z) :
    (e.hom ≫ Y ◁ f ≫ e.inv) ≫ (e.hom ≫ Y ◁ f ≫ e.inv) =
      h • (e.hom ≫ Y ◁ f ≫ e.inv) + 𝟙 X := by
  simp only [Category.assoc, Iso.inv_hom_id_assoc]
  rw [← MonoidalCategory.whiskerLeft_comp_assoc, hf, MonoidalPreadditive.whiskerLeft_add,
    MonoidalLinear.whiskerLeft_smul, MonoidalCategory.whiskerLeft_id, Preadditive.add_comp,
    Preadditive.comp_add, Linear.smul_comp, Linear.comp_smul, Category.id_comp, Iso.hom_inv_id]

/-- **The Hecke quadratic on every strand.** If `f² = h f + 1` on `V ⊗ V`, then every `σ_i`
with `i + 1 < n` satisfies the same quadratic on `V^{⊗n}`. -/
theorem strand_quad {f : V ⊗ V ⟶ V ⊗ V} {h : K} (hf : f ≫ f = h • f + 𝟙 (V ⊗ V)) :
    ∀ (n i : ℕ), i + 1 < n →
      strand V f n i ≫ strand V f n i = h • strand V f n i + 𝟙 (tpow V n)
  | 0, _, hi => absurd hi (by omega)
  | 1, _, hi => absurd hi (by omega)
  | n + 2, i, hi => by
    by_cases hin : i = n
    · subst hin
      rw [strand_last]
      exact quad_conj (α_ (tpow V i) V V) hf
    · rw [strand_of_ne f hin, ← comp_whiskerRight, strand_quad hf (n + 1) i (by omega),
        MonoidalPreadditive.add_whiskerRight, MonoidalLinear.smul_whiskerRight,
        MonoidalCategory.id_whiskerRight]
      rfl

end Linear

/-! ### Drinfeld–Kohno as a hypothesis, and the conditional step-2 instance -/

section Assembly

open QOU.MathlibExt.OcneanuTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable {K : Type*} [Field K]
variable {C : Type*} [Category C] [MonoidalCategory C] [Preadditive C] [Linear K C]

/-- **Drinfeld–Kohno, as a hypothesis on a tower.** The generators of the Markov-trace tower `T`
(over `R`) are the images of the categorical braid generators `σ_i = strand f n i` under ring maps
`ρ_n : End(V^{⊗n}) → A` that are semilinear along `φ : R → K`. For the KZ connection this is the
content of the Drinfeld–Kohno theorem (the monodromy functor is braided monoidal, so the KZ
monodromy of `σ_i` is the braiding acting on strands `i, i+1`). Nothing here asserts it for the
framework's own connection (bean `qou-d0qq`). -/
class BraidedMonodromy (T : MarkovTrace R A) (φ : R →+* K) (V : C) (f : V ⊗ V ⟶ V ⊗ V) :
    Prop where
  /-- The monodromy maps, one per strand count. -/
  exists_rep : ∃ ρ : ∀ n, End (tpow V n) →+* A,
    (∀ n (r : R) (x : End (tpow V n)), ρ n (φ r • x) = r • ρ n x) ∧
    ∀ n i, i + 1 < n → ρ n (strand V f n i) = T.g i

variable [MonoidalPreadditive C] [MonoidalLinear K C]

/-- **Step 2 assembled from Drinfeld–Kohno and the two-strand Hecke quadratic.** If the tower's
generators are the images of `σ_i = strand f n i` (`BraidedMonodromy`), `f` satisfies the
three-strand relation (`IsYB`; automatic for a braiding, `isYB_braiding`) and the two-strand
quadratic `f² = (φ q − φ q⁻¹) f + 1`, then the tower satisfies the Hecke quadratic, the braid
relation and far commutation. The shadow `ε` lying over `q ↦ 1` is a hypothesis; see
`subsingleton_of_fixed_coupling` for why it cannot come from the category at fixed coupling. -/
theorem heckeMonodromy_of_braided (T : MarkovTrace R A) (q : Rˣ) (φ : R →+* K) {B : Type*}
    [Ring B] (ε : A →+* B) (V : C) (f : V ⊗ V ⟶ V ⊗ V) [hDK : BraidedMonodromy T φ V f]
    (hYB : IsYB f) (hquad : f ≫ f = (φ q - φ ↑q⁻¹) • f + 𝟙 (V ⊗ V))
    (shadow_at_one : ε (algebraMap R A q) = 1) :
    HeckeMonodromy T q ε := by
  obtain ⟨ρ, hsmul, hρ⟩ := hDK.exists_rep
  refine ⟨fun i => ?_, fun i => ?_, fun i j hij => ?_, shadow_at_one⟩
  · -- Hecke quadratic: on `V^{⊗(i+2)}`
    have h := strand_quad hquad (i + 2) i (by omega)
    have h' := congrArg (ρ (i + 2)) h
    rw [← hρ (i + 2) i (by omega)]
    rw [← End.mul_def] at h'
    rw [← map_sub, map_mul, map_add, hsmul] at h'
    have h1 : (ρ (i + 2)) (𝟙 (tpow V (i + 2))) = 1 := map_one (ρ (i + 2))
    rw [h1] at h'
    exact h'
  · -- braid relation: on `V^{⊗(i+3)}`
    have h := strand_braid f hYB (i + 3) i (by omega)
    have h' := congrArg (ρ (i + 3)) h
    simp only [← End.mul_def, map_mul] at h'
    rw [← hρ (i + 3) i (by omega), ← hρ (i + 3) (i + 1) (by omega)]
    exact h'
  · -- far commutation: on `V^{⊗(j+2)}`
    have h := strand_far f (j + 2) i j hij (by omega)
    have h' := congrArg (ρ (j + 2)) h
    simp only [← End.mul_def, map_mul] at h'
    rw [← hρ (j + 2) i (by omega), ← hρ (j + 2) j (by omega)]
    exact h'.symm

omit [MonoidalPreadditive C] [MonoidalLinear K C] in
/-- **A category at fixed coupling cannot carry the `q = 1` shadow.** If the tower's monodromy
factors through a `K`-linear category (`BraidedMonodromy`, `K` a field) and `φ(q) ≠ 1`, then a
shadow `ε` lying over `q ↦ 1` has zero target. Reason: `q` acts on the tower through the scalar
`φ(q)` of `End(𝟙)`, and `ε ∘ ρ` sends the unit `φ(q) − 1` of that field to `0`. The shadow needs
`q` to vary, which a single fixed-coupling category does not provide. -/
theorem subsingleton_of_fixed_coupling (T : MarkovTrace R A) (q : Rˣ) (φ : R →+* K) {B : Type*}
    [Ring B] (ε : A →+* B) (V : C) (f : V ⊗ V ⟶ V ⊗ V) [hDK : BraidedMonodromy T φ V f]
    [HeckeMonodromy T q ε] (hq : φ q ≠ 1) : Subsingleton B := by
  obtain ⟨ρ, hsmul, -⟩ := hDK.exists_rep
  have hA : algebraMap R A q = ρ 0 (φ q • (1 : End (tpow V 0))) := by
    rw [hsmul, map_one, Algebra.algebraMap_eq_smul_one]
  have h1 : ε (ρ 0 ((φ q - 1) • (1 : End (tpow V 0)))) = 0 := by
    rw [sub_smul, one_smul, map_sub, map_sub, ← hA, HeckeMonodromy.shadow_at_one (T := T),
      map_one, map_one, sub_self]
  have hu : IsUnit ((φ q - 1) • (1 : End (tpow V 0))) := by
    rw [Algebra.smul_def, mul_one]
    exact (isUnit_iff_ne_zero.mpr (sub_ne_zero.mpr hq)).map _
  have hu' := (hu.map (ρ 0)).map ε
  rw [h1] at hu'
  exact subsingleton_of_zero_eq_one (isUnit_zero_iff.mp hu')

end Assembly

end QOU.Mass.BraidedStrands
