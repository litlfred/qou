import QOU.AppendixSurreals.BirthdayFaithful

/-!
# Appendix Surreals: Hyperreal & Birthday-Free Surreal Limit-Transfer Instance

This module provides the clean architectural discharge of the sequence-evaluation
and limit-transfer machinery (`SurrealLimitTransfer`) over Mathlib's `Hyperreal`
field `ℝ* = Germ (hyperfilter ℕ) ℝ`, together with the birthday-free carrier
hierarchy `NonstandardOrderedField` and `NonstandardLimitTransfer`.

Specifically:
1. **`NonstandardOrderedField` and `NonstandardLimitTransfer`**:
   Isolates the ordered-field and archimedean-failure (`omegaElem > n`) axioms
   required by sequence evaluation and standard-part limit transfer into a
   birthday-free typeclass `NonstandardOrderedField K`, and defines the corresponding
   sequence-evaluation interface `NonstandardLimitTransfer K`.
2. **Canonical Bridge from `SurrealField` + `SurrealLimitTransfer`**:
   Every `[SurrealField K] [SurrealLimitTransfer K]` canonically induces
   `NonstandardOrderedField K` and `NonstandardLimitTransfer K` without loss of
   algebraic or analytic content.
3. **Genuine Global Instance on Mathlib `Hyperreal` (`ℝ*`)**:
   Mathlib's ultrapower `ℝ*` satisfies `NonstandardOrderedField ℝ*` and
   `NonstandardLimitTransfer ℝ*` globally and unconditionally via `Hyperreal.ofSeq`,
   `hyperrealOfReal`, `Hyperreal.omega`, `Nat.hyperfilter_le_atTop`, and
   `Hyperreal.isSt_of_tendsto`, with no birthday pathology.
4. **Bundled Ring Homomorphism and Limit Algebra via `ℝ*`**:
   Constructs `evalOmegaRingHom : (ℕ → ℝ) →+* ℝ*` (`f ↦ Hyperreal.ofSeq f`),
   proves that it sends the identity sequence `(fun n : ℕ => (n : ℝ))` to
   `Hyperreal.omega`, preserves constants, sums, differences, products, powers, and
   `EventuallyLE`, and yields nonstandard proofs of the real limit laws (sum,
   difference, product, and squeeze theorem) routed through `Hyperreal.IsSt`.
5. **General Bounded-Birthday Obstruction (`BirthdayFaithful`)**:
   Generalizes `flatBirthday_not_faithful` by proving that no `SurrealField K`
   whose `birthday` is bounded above on natural numbers by a finite ordinal
   `(B : ℕ)` can satisfy `BirthdayFaithful K`.
-/

namespace QOU.AppendixSurreals.HyperrealSurrealLimitTransferInstance

open Filter Topology
open scoped Hyperreal Ordinal
open QOU.AppendixSurreals
open QOU.AppendixSurreals.HyperrealTransfer

universe u

-- ============================================================================
-- § 1. Birthday-Free Nonstandard Ordered Field Carrier
-- ============================================================================

/-- A birthday-free ordered field extension of `ℝ` equipped with a distinguished
positive infinite element `omegaElem` exceeding every natural number.
This captures the exact algebraic and order structure of `SurrealField` used by
sequence evaluation (`evalOmega`), standard-part comparison (`IsClose`), and
limit transfer, without imposing Conway ordinal-birthday axioms on ultrapowers. -/
class NonstandardOrderedField (K : Type u)
    extends Field K, LinearOrder K, IsStrictOrderedRing K where
  /-- Canonical ring embedding of the standard reals `ℝ →+* K`. -/
  ofReal : ℝ →+* K
  /-- The real embedding is strictly order-preserving. -/
  ofReal_strictMono : StrictMono ofReal
  /-- Distinguished positive infinite element `ω ∈ K`. -/
  omegaElem : K
  /-- `ω` exceeds every natural number `(n : K)`. -/
  omegaElem_gt_natCast : ∀ n : ℕ, (n : K) < omegaElem

namespace NonstandardOrderedField

variable {K : Type u} [NonstandardOrderedField K]

/-- Order-embedding monotonicity of `ofReal`. -/
theorem ofReal_mono : Monotone (ofReal (K := K)) :=
  ofReal_strictMono.monotone

/-- `ofReal` is injective. -/
theorem ofReal_injective : Function.Injective (ofReal (K := K)) :=
  ofReal_strictMono.injective

/-- `ofReal r ≤ ofReal s ↔ r ≤ s`. -/
@[simp]
theorem ofReal_le_ofReal_iff {r s : ℝ} :
    ofReal (K := K) r ≤ ofReal s ↔ r ≤ s :=
  ofReal_strictMono.le_iff_le

/-- `ofReal r < ofReal s ↔ r < s`. -/
@[simp]
theorem ofReal_lt_ofReal_iff {r s : ℝ} :
    ofReal (K := K) r < ofReal s ↔ r < s :=
  ofReal_strictMono.lt_iff_lt

/-- `ofReal` maps natural casts to natural casts. -/
@[simp]
theorem ofReal_natCast (n : ℕ) : ofReal (K := K) (n : ℝ) = (n : K) :=
  map_natCast ofReal n

/-- The distinguished element `omegaElem` is strictly positive. -/
theorem omegaElem_pos : (0 : K) < omegaElem := by
  simpa using omegaElem_gt_natCast (K := K) 0

/-- Two elements of a `NonstandardOrderedField` are infinitesimally close (`IsCloseNS x y`)
when `|x - y| < ofReal δ` for every positive standard real `δ > 0`. -/
def IsCloseNS (x y : K) : Prop :=
  ∀ δ : ℝ, 0 < δ → |x - y| < ofReal δ

theorem isCloseNS_refl (x : K) : IsCloseNS x x := by
  intro δ hδ
  rw [sub_self, abs_zero]
  have h0 : (0 : K) = ofReal 0 := (map_zero ofReal).symm
  rw [h0]
  exact ofReal_strictMono hδ

theorem isCloseNS_symm {x y : K} (h : IsCloseNS x y) : IsCloseNS y x := by
  intro δ hδ
  rw [abs_sub_comm]
  exact h δ hδ

theorem isCloseNS_trans {x y z : K}
    (hxy : IsCloseNS x y) (hyz : IsCloseNS y z) : IsCloseNS x z := by
  intro δ hδ
  have hδ2 : (0 : ℝ) < δ / 2 := half_pos hδ
  have h1 := hxy (δ / 2) hδ2
  have h2 := hyz (δ / 2) hδ2
  have htri : |x - z| ≤ |x - y| + |y - z| := by
    have : x - z = (x - y) + (y - z) := by ring
    rw [this]
    exact abs_add_le (x - y) (y - z)
  have hsum : |x - y| + |y - z| < ofReal (δ / 2) + ofReal (δ / 2) :=
    add_lt_add h1 h2
  have heq : ofReal (K := K) (δ / 2) + ofReal (δ / 2) = ofReal δ := by
    rw [← map_add, add_halves]
  rw [heq] at hsum
  exact lt_of_le_of_lt htri hsum

/-- Distinct standard reals cannot be infinitesimally close in `K`. -/
theorem ofReal_eq_of_isCloseNS {r s : ℝ}
    (h : IsCloseNS (ofReal (K := K) r) (ofReal s)) : r = s := by
  by_contra hne
  have hpos : (0 : ℝ) < |r - s| := abs_sub_pos.mpr hne
  have hclose := h |r - s| hpos
  have habs : |ofReal (K := K) r - ofReal s| = ofReal |r - s| := by
    rw [← map_sub]
    rcases le_or_gt (r - s) 0 with hle | hgt
    · have hleK : ofReal (K := K) (r - s) ≤ 0 := by
        simpa [map_zero] using ofReal_mono (K := K) hle
      rw [abs_of_nonpos hle, abs_of_nonpos hleK, map_neg]
    · have hgtK : (0 : K) < ofReal (r - s) := by
        simpa [map_zero] using ofReal_strictMono (K := K) hgt
      rw [abs_of_pos hgt, abs_of_pos hgtK]
  rw [habs] at hclose
  exact lt_irrefl _ hclose

/-- Standard-part uniqueness in any `NonstandardOrderedField`. -/
theorem standard_part_unique_ns {x : K} {L₁ L₂ : ℝ}
    (h1 : IsCloseNS x (ofReal L₁)) (h2 : IsCloseNS x (ofReal L₂)) :
    L₁ = L₂ :=
  ofReal_eq_of_isCloseNS (isCloseNS_trans (isCloseNS_symm h1) h2)

end NonstandardOrderedField

-- ============================================================================
-- § 2. Birthday-Free Nonstandard Limit-Transfer Class
-- ============================================================================

/-- Birthday-free sequence-evaluation and standard-part limit-transfer interface
over any `NonstandardOrderedField K`. -/
class NonstandardLimitTransfer (K : Type u) [NonstandardOrderedField K] where
  /-- Evaluate a real sequence `a : ℕ → ℝ` at the infinite index `ω`, producing an element of `K`. -/
  evalOmega : (ℕ → ℝ) → K
  /-- Constant sequences evaluate to their embedded real value. -/
  evalOmega_const : ∀ r : ℝ, evalOmega (fun _ => r) = NonstandardOrderedField.ofReal r
  /-- Additivity of sequence evaluation at `ω`. -/
  evalOmega_add : ∀ a b : ℕ → ℝ, evalOmega (fun n => a n + b n) = evalOmega a + evalOmega b
  /-- Multiplicativity of sequence evaluation at `ω`. -/
  evalOmega_mul : ∀ a b : ℕ → ℝ, evalOmega (fun n => a n * b n) = evalOmega a * evalOmega b
  /-- Order preservation: eventually `a ≤ b` implies `evalOmega a ≤ evalOmega b`. -/
  evalOmega_le_of_eventuallyLE :
    ∀ {a b : ℕ → ℝ}, EventuallyLE a b → evalOmega a ≤ evalOmega b
  /-- Limit transfer: if `a_n → L` in `ℝ`, then `evalOmega a` is infinitesimally close to `ofReal L`. -/
  evalOmega_isClose_of_tendstoReal :
    ∀ {a : ℕ → ℝ} {L : ℝ}, TendstoReal a L →
      NonstandardOrderedField.IsCloseNS (evalOmega a) (NonstandardOrderedField.ofReal L)

namespace NonstandardLimitTransfer

variable {K : Type u} [NonstandardOrderedField K] [NonstandardLimitTransfer K]

/-- Order-comparison transfer in any `NonstandardLimitTransfer` field: if `a_n → L₁`,
`b_n → L₂`, and eventually `a_n ≤ b_n`, then `L₁ ≤ L₂`. -/
theorem tendstoReal_le_of_eventuallyLE_ns (K : Type u)
    [NonstandardOrderedField K] [NonstandardLimitTransfer K]
    {a b : ℕ → ℝ} {L₁ L₂ : ℝ}
    (ha : TendstoReal a L₁) (hb : TendstoReal b L₂)
    (hab : EventuallyLE a b) : L₁ ≤ L₂ := by
  by_contra hlt
  push_neg at hlt
  set δ : ℝ := (L₁ - L₂) / 3
  have hδ : 0 < δ := by
    dsimp [δ]
    linarith
  have hca := (evalOmega_isClose_of_tendstoReal (K := K) ha) δ hδ
  have hcb := (evalOmega_isClose_of_tendstoReal (K := K) hb) δ hδ
  have hle : evalOmega (K := K) a ≤ evalOmega (K := K) b :=
    evalOmega_le_of_eventuallyLE (K := K) hab
  have ha_low :
      NonstandardOrderedField.ofReal (K := K) L₁ - NonstandardOrderedField.ofReal δ <
        evalOmega (K := K) a := by
    have h1 := (abs_lt.mp hca).1
    linarith
  have hb_high :
      evalOmega (K := K) b <
        NonstandardOrderedField.ofReal (K := K) L₂ + NonstandardOrderedField.ofReal δ := by
    have h2 := (abs_lt.mp hcb).2
    linarith
  have hcomb :
      NonstandardOrderedField.ofReal (K := K) (L₁ - δ) <
        NonstandardOrderedField.ofReal (K := K) (L₂ + δ) := by
    rw [map_sub, map_add]
    exact lt_of_lt_of_le ha_low (le_trans hle (le_of_lt hb_high))
  have hreal : L₁ - δ < L₂ + δ :=
    (NonstandardOrderedField.ofReal_lt_ofReal_iff (K := K)).mp hcomb
  dsimp [δ] at hreal
  linarith

end NonstandardLimitTransfer

-- ============================================================================
-- § 3. Canonical Bridge from `SurrealField` + `SurrealLimitTransfer`
-- ============================================================================

/-- Every `SurrealField K` canonically induces a `NonstandardOrderedField K`. -/
def nonstandardOrderedFieldOfSurrealField (K : Type u) [SurrealField K] :
    NonstandardOrderedField K where
  ofReal := SurrealField.ofReal
  ofReal_strictMono := SurrealField.ofReal_strictMono
  omegaElem := SurrealField.omegaSurreal
  omegaElem_gt_natCast := SurrealField.omegaSurreal_gt_natCast

/-- Under `nonstandardOrderedFieldOfSurrealField K`, `IsCloseNS` coincides definitionally
with `QOU.AppendixSurreals.IsClose`. -/
theorem isCloseNS_iff_surrealIsClose {K : Type u} [SurrealField K] (x y : K) :
    @NonstandardOrderedField.IsCloseNS K (nonstandardOrderedFieldOfSurrealField K) x y ↔
      IsClose x y :=
  Iff.rfl

/-- Every `[SurrealField K] [SurrealLimitTransfer K]` canonically induces a
`NonstandardLimitTransfer K`. -/
def nonstandardLimitTransferOfSurrealLimitTransfer (K : Type u)
    [SurrealField K] [SurrealLimitTransfer K] :
    @NonstandardLimitTransfer K (nonstandardOrderedFieldOfSurrealField K) := by
  letI : NonstandardOrderedField K := nonstandardOrderedFieldOfSurrealField K
  exact
    { evalOmega := SurrealLimitTransfer.evalOmega
      evalOmega_const := SurrealLimitTransfer.evalOmega_const
      evalOmega_add := SurrealLimitTransfer.evalOmega_add
      evalOmega_mul := SurrealLimitTransfer.evalOmega_mul
      evalOmega_le_of_eventuallyLE := fun {a b} hab =>
        SurrealLimitTransfer.evalOmega_le_of_eventuallyLE a b hab
      evalOmega_isClose_of_tendstoReal := fun {a L} ha =>
        SurrealLimitTransfer.evalOmega_isClose_of_tendstoReal a L ha }

-- ============================================================================
-- § 4. Genuine Global Instances on Mathlib `Hyperreal` (`ℝ*`)
-- ============================================================================

/-- Mathlib's `Hyperreal` (`ℝ* = Germ (hyperfilter ℕ) ℝ`) is genuinely and globally a
`NonstandardOrderedField`, with no birthday axioms or local instances required. -/
noncomputable instance instNonstandardOrderedFieldHyperreal :
    NonstandardOrderedField ℝ* where
  ofReal := hyperrealOfReal
  ofReal_strictMono := hyperrealOfReal_strictMono
  omegaElem := Hyperreal.omega
  omegaElem_gt_natCast := omega_gt_natCast

/-- In `ℝ*`, `NonstandardOrderedField.ofReal r` is the standard coercion `(r : ℝ*)`. -/
@[simp]
theorem hyperreal_ofReal_apply (r : ℝ) :
    NonstandardOrderedField.ofReal (K := ℝ*) r = (r : ℝ*) :=
  rfl

/-- In `ℝ*`, `NonstandardOrderedField.omegaElem` is `Hyperreal.omega`. -/
@[simp]
theorem hyperreal_omegaElem_eq :
    NonstandardOrderedField.omegaElem (K := ℝ*) = Hyperreal.omega :=
  rfl

/-- Equivalence between `NonstandardOrderedField.IsCloseNS` on `ℝ*` and Mathlib's
`Hyperreal.Infinitesimal (x - y)`. -/
theorem isCloseNS_hyperreal_iff_infinitesimal_sub (x y : ℝ*) :
    NonstandardOrderedField.IsCloseNS x y ↔ Hyperreal.Infinitesimal (x - y) := by
  rw [Hyperreal.infinitesimal_def]
  constructor
  · intro h r hr
    have habs := h r hr
    rw [hyperreal_ofReal_apply, abs_lt] at habs
    exact habs
  · intro h δ hδ
    have hr := h δ hδ
    rw [hyperreal_ofReal_apply, abs_lt]
    exact hr

/-- Equivalence between `IsCloseNS x (ofReal L)` on `ℝ*` and Mathlib's `Hyperreal.IsSt x L`. -/
theorem isCloseNS_hyperreal_ofReal_iff_isSt (x : ℝ*) (L : ℝ) :
    NonstandardOrderedField.IsCloseNS x (NonstandardOrderedField.ofReal L) ↔
      Hyperreal.IsSt x L := by
  change (∀ δ : ℝ, 0 < δ → |x - (L : ℝ*)| < (δ : ℝ*)) ↔ Hyperreal.IsSt x L
  exact Hyperreal.isSt_iff_abs_sub_lt_delta.symm

/-- Bundled ring homomorphism `evalOmegaRingHom : (ℕ → ℝ) →+* ℝ*` sending a real sequence
`f : ℕ → ℝ` to its hyperfilter germ `Hyperreal.ofSeq f ∈ ℝ*`. -/
noncomputable def evalOmegaRingHom : (ℕ → ℝ) →+* ℝ* where
  toFun := Hyperreal.ofSeq
  map_one' := Filter.Germ.coe_one
  map_mul' := fun x y => Filter.Germ.coe_mul x y
  map_zero' := Filter.Germ.coe_zero
  map_add' := fun x y => Filter.Germ.coe_add x y

@[simp]
theorem evalOmegaRingHom_apply (f : ℕ → ℝ) :
    evalOmegaRingHom f = Hyperreal.ofSeq f :=
  rfl

/-- `evalOmegaRingHom` maps constant sequences to their standard real embedding in `ℝ*`. -/
@[simp]
theorem evalOmegaRingHom_const (r : ℝ) :
    evalOmegaRingHom (fun _ : ℕ => r) = (r : ℝ*) :=
  rfl

/-- `evalOmegaRingHom` maps the identity sequence `n ↦ (n : ℝ)` to `Hyperreal.omega`. -/
@[simp]
theorem evalOmegaRingHom_id_eq_omega :
    evalOmegaRingHom (fun n : ℕ => (n : ℝ)) = Hyperreal.omega :=
  rfl

/-- `evalOmegaRingHom` preserves subtraction of sequences. -/
theorem evalOmegaRingHom_sub (a b : ℕ → ℝ) :
    evalOmegaRingHom (fun n => a n - b n) = evalOmegaRingHom a - evalOmegaRingHom b :=
  map_sub evalOmegaRingHom a b

/-- `evalOmegaRingHom` preserves negation of sequences. -/
theorem evalOmegaRingHom_neg (a : ℕ → ℝ) :
    evalOmegaRingHom (fun n => -a n) = -evalOmegaRingHom a :=
  map_neg evalOmegaRingHom a

/-- `evalOmegaRingHom` preserves pointwise natural-number powers of sequences. -/
theorem evalOmegaRingHom_pow (a : ℕ → ℝ) (k : ℕ) :
    evalOmegaRingHom (fun n => a n ^ k) = evalOmegaRingHom a ^ k :=
  map_pow evalOmegaRingHom a k

/-- `evalOmegaRingHom` preserves order on `EventuallyLE` sequences. -/
theorem evalOmegaRingHom_le_of_eventuallyLE {a b : ℕ → ℝ} (h : EventuallyLE a b) :
    evalOmegaRingHom a ≤ evalOmegaRingHom b :=
  ofSeq_le_ofSeq_of_eventuallyLE h

/-- Mathlib's `Hyperreal` (`ℝ*`) is genuinely and globally an instance of
`NonstandardLimitTransfer`, backed by `evalOmegaRingHom` (`Hyperreal.ofSeq`) and
`Hyperreal.isSt_of_tendsto`. -/
noncomputable instance instNonstandardLimitTransferHyperreal :
    NonstandardLimitTransfer ℝ* where
  evalOmega := evalOmegaRingHom
  evalOmega_const := fun _ => rfl
  evalOmega_add := fun a b => map_add evalOmegaRingHom a b
  evalOmega_mul := fun a b => map_mul evalOmegaRingHom a b
  evalOmega_le_of_eventuallyLE := fun hab => ofSeq_le_ofSeq_of_eventuallyLE hab
  evalOmega_isClose_of_tendstoReal := fun {a L} ha => by
    rw [isCloseNS_hyperreal_ofReal_iff_isSt]
    exact isSt_ofSeq_of_tendstoReal ha

-- ============================================================================
-- § 5. Nonstandard Limit Algebra Routed Through `Hyperreal` (`ℝ*`)
-- ============================================================================

/-- If `a_n → L₁` and `b_n → L₂` in `TendstoReal`, then `evalOmegaRingHom (a + b)` has
standard part `L₁ + L₂` in `ℝ*`. -/
theorem isSt_evalOmegaRingHom_add {a b : ℕ → ℝ} {L₁ L₂ : ℝ}
    (ha : TendstoReal a L₁) (hb : TendstoReal b L₂) :
    Hyperreal.IsSt (evalOmegaRingHom (fun n => a n + b n)) (L₁ + L₂) := by
  have h1 : Hyperreal.IsSt (evalOmegaRingHom a) L₁ := isSt_ofSeq_of_tendstoReal ha
  have h2 : Hyperreal.IsSt (evalOmegaRingHom b) L₂ := isSt_ofSeq_of_tendstoReal hb
  change Hyperreal.IsSt (evalOmegaRingHom (a + b)) (L₁ + L₂)
  rw [map_add]
  exact h1.add h2

/-- If `a_n → L₁` and `b_n → L₂` in `TendstoReal`, then `evalOmegaRingHom (a - b)` has
standard part `L₁ - L₂` in `ℝ*`. -/
theorem isSt_evalOmegaRingHom_sub {a b : ℕ → ℝ} {L₁ L₂ : ℝ}
    (ha : TendstoReal a L₁) (hb : TendstoReal b L₂) :
    Hyperreal.IsSt (evalOmegaRingHom (fun n => a n - b n)) (L₁ - L₂) := by
  have h1 : Hyperreal.IsSt (evalOmegaRingHom a) L₁ := isSt_ofSeq_of_tendstoReal ha
  have h2 : Hyperreal.IsSt (evalOmegaRingHom b) L₂ := isSt_ofSeq_of_tendstoReal hb
  change Hyperreal.IsSt (evalOmegaRingHom (a - b)) (L₁ - L₂)
  rw [map_sub]
  exact h1.sub h2

/-- If `a_n → L₁` and `b_n → L₂` in `TendstoReal`, then `evalOmegaRingHom (a * b)` has
standard part `L₁ * L₂` in `ℝ*`. -/
theorem isSt_evalOmegaRingHom_mul {a b : ℕ → ℝ} {L₁ L₂ : ℝ}
    (ha : TendstoReal a L₁) (hb : TendstoReal b L₂) :
    Hyperreal.IsSt (evalOmegaRingHom (fun n => a n * b n)) (L₁ * L₂) := by
  have h1 : Hyperreal.IsSt (evalOmegaRingHom a) L₁ := isSt_ofSeq_of_tendstoReal ha
  have h2 : Hyperreal.IsSt (evalOmegaRingHom b) L₂ := isSt_ofSeq_of_tendstoReal hb
  change Hyperreal.IsSt (evalOmegaRingHom (a * b)) (L₁ * L₂)
  rw [map_mul]
  exact h1.mul h2

/-- Hyperreal squeeze theorem for standard parts: if `a_n → L`, `c_n → L`, and
eventually `a_n ≤ b_n` and `b_n ≤ c_n`, then `evalOmegaRingHom b` has standard part `L`
in `ℝ*` (and hence `st (evalOmegaRingHom b) = L`). -/
theorem isSt_evalOmegaRingHom_of_squeeze {a b c : ℕ → ℝ} {L : ℝ}
    (ha : TendstoReal a L) (hc : TendstoReal c L)
    (hab : EventuallyLE a b) (hbc : EventuallyLE b c) :
    Hyperreal.IsSt (evalOmegaRingHom b) L := by
  have haSt : Hyperreal.IsSt (evalOmegaRingHom a) L := isSt_ofSeq_of_tendstoReal ha
  have hcSt : Hyperreal.IsSt (evalOmegaRingHom c) L := isSt_ofSeq_of_tendstoReal hc
  have hle1 : evalOmegaRingHom a ≤ evalOmegaRingHom b :=
    evalOmegaRingHom_le_of_eventuallyLE hab
  have hle2 : evalOmegaRingHom b ≤ evalOmegaRingHom c :=
    evalOmegaRingHom_le_of_eventuallyLE hbc
  intro δ hδ
  have ⟨ha1, _⟩ := haSt δ hδ
  have ⟨_, hc2⟩ := hcSt δ hδ
  exact ⟨lt_of_lt_of_le ha1 hle1, lt_of_le_of_lt hle2 hc2⟩

/-- Corollary of the hyperreal squeeze theorem: `Hyperreal.st (evalOmegaRingHom b) = L`. -/
theorem st_evalOmegaRingHom_of_squeeze {a b c : ℕ → ℝ} {L : ℝ}
    (ha : TendstoReal a L) (hc : TendstoReal c L)
    (hab : EventuallyLE a b) (hbc : EventuallyLE b c) :
    Hyperreal.st (evalOmegaRingHom b) = L :=
  (isSt_evalOmegaRingHom_of_squeeze ha hc hab hbc).st_eq

-- ============================================================================
-- § 6. General Bounded-Birthday Obstruction (`BirthdayFaithful`)
-- ============================================================================

/-- **General Bounded-Birthday Obstruction**:
No `SurrealField K` whose `birthday` is bounded above on natural numbers by a finite
ordinal `(B : ℕ)` can satisfy `BirthdayFaithful K`.
In particular, any finite-valued or constant birthday assignment (such as `flatBirthday`
with `B = 1`) is rejected by `BirthdayFaithful`. -/
theorem not_birthdayFaithful_of_bounded_nat {K : Type u} [SurrealField K]
    (B : ℕ) (hbound : ∀ n : ℕ, SurrealField.birthday ((n : ℕ) : K) ≤ (B : Ordinal)) :
    ¬ BirthdayFaithful K := by
  intro hFaithful
  have h1 := hFaithful.birthday_natCast (K := K) (B + 1)
  have h2 := hbound (B + 1)
  rw [h1] at h2
  have hlt : (B : Ordinal) < ((B + 1 : ℕ) : Ordinal) :=
    Nat.cast_lt.mpr (Nat.lt_succ_self B)
  exact not_lt_of_ge h2 hlt

/-- Specializing `not_birthdayFaithful_of_bounded_nat` to `B = 1` recovers
`flatBirthday_not_faithful` on `ℝ*`. -/
theorem flatBirthday_not_faithful_via_bounded :
    ¬ @BirthdayFaithful ℝ* surrealFieldHyperreal := by
  letI : SurrealField ℝ* := surrealFieldHyperreal
  apply not_birthdayFaithful_of_bounded_nat (K := ℝ*) 1
  intro n
  change flatBirthday ((n : ℕ) : ℝ*) ≤ ((1 : ℕ) : Ordinal)
  simpa using flatBirthday_le_one ((n : ℕ) : ℝ*)

end QOU.AppendixSurreals.HyperrealSurrealLimitTransferInstance
