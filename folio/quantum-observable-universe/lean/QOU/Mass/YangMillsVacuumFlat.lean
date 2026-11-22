import Mathlib.Tactic
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Bridge A, step A1 — the gauge vacuum is flat (Bogomolny, algebraically)

Audit `qou-derivation-chain/derivation-chain-audit-2026-11-15.md`, §2 and §8 step 8.
The Lagrangian's gauge part is the Yang–Mills density `tr(F ∧ ⋆F)`; the remark
`rem:instanton-on-shell` states the Bogomolny decomposition
`‖F‖² = c₂ + 2‖F⁻‖²` and `prop:categorical-self-duality` concludes "critical points are
instantons". This file proves the decomposition and isolates exactly what "on-shell" buys.

## Setting

`V` is the space of curvature values (`Ω² ⊗ ad`), a module over a field `K` with `2 ≠ 0`,
carrying

* a symmetric bilinear pairing `B` (the `tr(X ∧ ⋆Y)` / `L²` pairing), and
* a Hodge involution `⋆` (`⋆⋆ = 1`) that is a `B`-isometry.

`action F = B F F` is the Yang–Mills action `S = ∫ tr(F ∧ ⋆F)`, and `charge F = B F (⋆F)` is
the topological term `c₂ = ∫ tr(F ∧ F)`. `F⁺ = ½(F + ⋆F)`, `F⁻ = ½(F − ⋆F)`.

## What is proved

**Algebraic part (§1, any field with `2 ≠ 0`, no order, no analysis).**
`F = F⁺ + F⁻`, `⋆F^± = ±F^±`, `B(F⁺, F⁻) = 0`, and the two Bogomolny identities

* `action F = charge F + 2·B(F⁻, F⁻)` (`bogomolny_minus`; this is `rem:instanton-on-shell`);
* `action F = −charge F + 2·B(F⁺, F⁺)` (`bogomolny_plus`).

**Positivity (§2, isolated).** The only non-algebraic input is that `B` is positive definite:
`0 ≤ B x x`, and `B x x = 0 → x = 0`. Over a manifold this is the statement that the `L²` norm
is a norm, which is where analysis lives; here it is a single hypothesis `PosDef B`, and every
theorem that uses it says so. With it:

* `action_eq_zero_iff` — `tr(F ∧ ⋆F) = 0 ↔ F = 0`;
* `flat_iff_instanton_and_charge_zero` — `F = 0 ↔ (F⁻ = 0 ∧ c₂ = 0)`;
* `flat_iff_isMinimum` — `F = 0 ↔ F minimises the action`.

**What "on-shell ⇒ flat" really says.** It is *false* as stated:
`instanton_not_flat` gives a self-dual, non-zero `F` (charge `≠ 0`). The correct statement is
that the **vacuum** — the absolute minimum, equivalently instanton with `c₂ = 0` — is flat.
So Bridge A's first step reads: *the gauge part is in its vacuum ⇔ `∇` is flat*, and the
extra datum beyond the Euler–Lagrange equation is the vanishing of the topological charge.
The corpus's `categorical-self-duality-proof.md` argues from *minimising*, which is what the
theorem here uses; its statement says *critical point*, which is weaker (non-minimal
Yang–Mills critical points exist).

**Matrix instance (§3).** For matrix-valued curvature over an ordered field,
`B X Y = tr(Xᵀ Y)` is positive definite (`traceForm_posDef`), so §2 applies to `tr(Fᵀ F)`.
For an anti-Hermitian gauge algebra the physical pairing is `−tr(F F)`, which is this one
because `Fᵀ = −F` there.

Base ring §7c: generic `Field K` for §1; `[LinearOrder K] [IsStrictOrderedRing K]` only in
§2–§3, where positivity is the content. No `ℝ`, no `ℂ`.

-- Ref: [leitner2026] quantum-observable-universes/instanton-on-shell.md
-- Ref: [leitner2026] quantum-observable-universes/categorical-self-duality-proof.md
-- Ref: [donaldson1990] Donaldson–Kronheimer, The Geometry of Four-Manifolds, §2.1.
-/

namespace QOU.Mass.YangMillsVacuumFlat

open LinearMap (BilinForm)

variable {K : Type*} [Field K] {V : Type*} [AddCommGroup V] [Module K V]

/-- A Hodge pairing: a symmetric bilinear form and an involutive isometry `⋆`. -/
structure HodgePairing (K V : Type*) [Field K] [AddCommGroup V] [Module K V] where
  /-- The pairing `B(X, Y) = ∫ tr(X ∧ ⋆Y)`. -/
  B : BilinForm K V
  /-- The Hodge star on curvature values. -/
  star : V →ₗ[K] V
  B_symm : ∀ x y, B x y = B y x
  star_star : ∀ x, star (star x) = x
  B_star : ∀ x y, B (star x) (star y) = B x y

namespace HodgePairing

variable (H : HodgePairing K V)

/-- Yang–Mills action `S(F) = B(F, F)`. -/
def action (F : V) : K := H.B F F

/-- Topological charge `c₂(F) = B(F, ⋆F)`. -/
def charge (F : V) : K := H.B F (H.star F)

/-- Self-dual part `F⁺ = ½(F + ⋆F)`. -/
def plus (F : V) : V := (2 : K)⁻¹ • (F + H.star F)

/-- Anti-self-dual part `F⁻ = ½(F − ⋆F)`. -/
def minus (F : V) : V := (2 : K)⁻¹ • (F - H.star F)

/-- `F` is an instanton (self-dual): `F⁻ = 0`. -/
def IsInstanton (F : V) : Prop := H.minus F = 0

/-! ## §1 Algebra (any field with `2 ≠ 0`) -/

variable (h2 : (2 : K) ≠ 0)
include h2

theorem plus_add_minus (F : V) : H.plus F + H.minus F = F := by
  unfold plus minus
  rw [← smul_add]
  have : F + H.star F + (F - H.star F) = (2 : K) • F := by rw [two_smul]; abel
  rw [this, smul_smul, inv_mul_cancel₀ h2, one_smul]

omit h2 in
theorem star_plus (F : V) : H.star (H.plus F) = H.plus F := by
  unfold plus
  rw [map_smul, map_add, H.star_star, add_comm]

omit h2 in
theorem star_minus (F : V) : H.star (H.minus F) = -H.minus F := by
  unfold minus
  rw [map_smul, map_sub, H.star_star, ← smul_neg, neg_sub]

/-- `F⁺ ⊥ F⁻`. -/
theorem B_plus_minus (F : V) : H.B (H.plus F) (H.minus F) = 0 := by
  have h := H.B_star (H.plus F) (H.minus F)
  rw [H.star_plus, H.star_minus, map_neg] at h
  -- h : -B F⁺ F⁻ = B F⁺ F⁻
  have h' : (2 : K) * H.B (H.plus F) (H.minus F) = 0 := by linear_combination -h
  exact (mul_eq_zero.mp h').resolve_left h2

theorem B_minus_plus (F : V) : H.B (H.minus F) (H.plus F) = 0 := by
  rw [H.B_symm]; exact H.B_plus_minus h2 F

/-- `S(F) = ‖F⁺‖² + ‖F⁻‖²`. -/
theorem action_eq (F : V) :
    H.action F = H.B (H.plus F) (H.plus F) + H.B (H.minus F) (H.minus F) := by
  unfold action
  conv_lhs => rw [← H.plus_add_minus h2 F]
  simp only [map_add, LinearMap.add_apply, H.B_plus_minus h2, H.B_minus_plus h2]
  ring

/-- `c₂(F) = ‖F⁺‖² − ‖F⁻‖²`. -/
theorem charge_eq (F : V) :
    H.charge F = H.B (H.plus F) (H.plus F) - H.B (H.minus F) (H.minus F) := by
  unfold charge
  conv_lhs => rw [← H.plus_add_minus h2 F]
  simp only [map_add, H.star_plus, H.star_minus, map_neg, LinearMap.add_apply,
    H.B_plus_minus h2, H.B_minus_plus h2]
  ring

/-- **Bogomolny, `rem:instanton-on-shell`.** `S(F) = c₂(F) + 2‖F⁻‖²`. -/
theorem bogomolny_minus (F : V) :
    H.action F = H.charge F + 2 * H.B (H.minus F) (H.minus F) := by
  rw [H.action_eq h2, H.charge_eq h2]; ring

/-- **Bogomolny, other sign.** `S(F) = −c₂(F) + 2‖F⁺‖²`. -/
theorem bogomolny_plus (F : V) :
    H.action F = -H.charge F + 2 * H.B (H.plus F) (H.plus F) := by
  rw [H.action_eq h2, H.charge_eq h2]; ring

/-- On an instanton the action is the topological charge: `S = c₂`. -/
theorem action_eq_charge_of_isInstanton {F : V} (hF : H.IsInstanton F) :
    H.action F = H.charge F := by
  rw [H.bogomolny_minus h2, show H.minus F = 0 from hF]
  simp

/-! ## §2 Positivity — the one isolated analytic input

`PosDef B` is the statement that the `L²` pairing is a norm. Everything else is algebra. -/

omit h2

/-- Positive definiteness of a bilinear form over an ordered field. -/
def PosDef [LinearOrder K] (B : BilinForm K V) : Prop :=
  ∀ x, 0 ≤ B x x ∧ (B x x = 0 → x = 0)

variable [LinearOrder K] [IsStrictOrderedRing K]

omit [IsStrictOrderedRing K] in
theorem action_nonneg (hB : PosDef H.B) (F : V) : 0 ≤ H.action F := (hB F).1

omit [IsStrictOrderedRing K] in
/-- **`tr(F ∧ ⋆F) = 0 ↔ F = 0`.** -/
theorem action_eq_zero_iff (hB : PosDef H.B) (F : V) : H.action F = 0 ↔ F = 0 := by
  refine ⟨(hB F).2, ?_⟩
  rintro rfl
  simp [action]

/-- `|c₂| ≤ S`: the Bogomolny bound. -/
theorem abs_charge_le_action (hB : PosDef H.B) (F : V) : |H.charge F| ≤ H.action F := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  have hp := (hB (H.plus F)).1
  have hm := (hB (H.minus F)).1
  rw [abs_le, H.action_eq h2, H.charge_eq h2]
  constructor <;> linarith

/-- **Flat ⇔ instanton with vanishing charge.** -/
theorem flat_iff_instanton_and_charge_zero (hB : PosDef H.B) (F : V) :
    F = 0 ↔ (H.IsInstanton F ∧ H.charge F = 0) := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  constructor
  · rintro rfl
    refine ⟨?_, ?_⟩
    · simp [IsInstanton, minus]
    · simp [charge]
  · rintro ⟨hI, hc⟩
    rw [← H.action_eq_zero_iff hB, H.action_eq_charge_of_isInstanton h2 hI, hc]

omit [IsStrictOrderedRing K] in
/-- **Flat ⇔ vacuum.** `F = 0` iff `F` minimises the action over all curvature values. -/
theorem flat_iff_isMinimum (hB : PosDef H.B) (F : V) :
    F = 0 ↔ ∀ G, H.action F ≤ H.action G := by
  constructor
  · rintro rfl G
    simpa [action] using H.action_nonneg hB G
  · intro h
    have h0 := h 0
    simp only [action, map_zero] at h0
    exact (H.action_eq_zero_iff hB F).1 (le_antisymm h0 (H.action_nonneg hB F))

end HodgePairing

/-! ### "On-shell ⇒ flat" is false without the charge condition

With `V = K`, `⋆ = id` and `B = multiplication`, every `F` is self-dual, and `F = 1` is a
non-flat instanton of charge `1`. So the Euler–Lagrange (instanton) condition alone does not
give flatness; the vacuum does. -/

/-- The one-dimensional Hodge pairing with `⋆ = id`. -/
def trivialPairing (K : Type*) [Field K] : HodgePairing K K where
  B := LinearMap.mul K K
  star := LinearMap.id
  B_symm := fun x y => mul_comm x y
  star_star := fun _ => rfl
  B_star := fun _ _ => rfl

theorem instanton_not_flat (K : Type*) [Field K] :
    (trivialPairing K).IsInstanton 1 ∧ (1 : K) ≠ 0 ∧ (trivialPairing K).charge 1 = 1 := by
  refine ⟨?_, one_ne_zero, ?_⟩
  · simp [HodgePairing.IsInstanton, HodgePairing.minus, trivialPairing]
  · simp [HodgePairing.charge, trivialPairing]

/-! ## §3 Matrix instance: `tr(Xᵀ Y)` is positive definite -/

section Matrix

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The trace pairing `B(X, Y) = tr(Xᵀ Y)` on `n × n` matrices. -/
def traceForm : BilinForm K (Matrix n n K) :=
  LinearMap.mk₂ K (fun X Y => (Xᵀ * Y).trace)
    (fun X X' Y => by simp [Matrix.transpose_add, Matrix.add_mul, Matrix.trace_add])
    (fun c X Y => by simp [Matrix.transpose_smul, Matrix.trace_smul])
    (fun X Y Y' => by simp [Matrix.mul_add, Matrix.trace_add])
    (fun c X Y => by simp [Matrix.trace_smul])

theorem traceForm_apply_self (X : Matrix n n K) :
    traceForm X X = ∑ i, ∑ j, X j i * X j i := by
  simp [traceForm, Matrix.trace, Matrix.mul_apply, Matrix.diag]

variable [LinearOrder K] [IsStrictOrderedRing K]

theorem traceForm_posDef : HodgePairing.PosDef (traceForm (K := K) (n := n)) := by
  intro X
  rw [traceForm_apply_self]
  refine ⟨Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => mul_self_nonneg _, ?_⟩
  intro h
  ext j i
  have hi := (Finset.sum_eq_zero_iff_of_nonneg
    (fun i _ => Finset.sum_nonneg fun j _ => mul_self_nonneg (X j i))).1 h i (Finset.mem_univ _)
  have hj := (Finset.sum_eq_zero_iff_of_nonneg
    (fun j _ => mul_self_nonneg (X j i))).1 hi j (Finset.mem_univ _)
  simpa using mul_self_eq_zero.1 hj

end Matrix

end QOU.Mass.YangMillsVacuumFlat
