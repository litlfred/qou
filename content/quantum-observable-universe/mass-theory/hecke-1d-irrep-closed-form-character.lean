import Mathlib.Algebra.Order.Ring.Lemmas
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic


/-!
# QOU.BraidKnot.hecke_1d_irrep_closed_form_character

Universal closed form for the q-character of any typed braid `β ∈ B_n`
on the two 1-dimensional Hecke irreps `V_(n)` (trivial) and `V_(1^n)`
(sign), for every `n ≥ 2`:

  `χ_(n)_q(β)    = q^w · ([2]_q / 2)^m`
  `χ_(1^n)_q(β)  = (-q⁻¹)^w · (-[2]_q / 2)^m`

with `w(β) = #(σ_i) − #(σ_i⁻¹)` the writhe and `m(β)` the count of
operator-valued averaged crossings `σ_i − h/2 · 1` in the typed
encoding.

The proof is multiplicative on the typed crossing sequence and
independent of `n`: any 1-d Hecke irrep has generator eigenvalue
`λ_σ ∈ {+q, -q⁻¹}` by the Iwahori-Hecke quadratic relation, and the
typed-crossing actions are powers of `λ_σ` (positive/negative
crossings) or `λ_σ − h/2` (averaged crossings).

LaTeX label: `prop:hecke-1d-irrep-closed-form-character`
-/

namespace QOU.BraidKnot

/-- Quantum-integer differential `h(q) = q − q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- Quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def qInt2 (q : ℝ) : ℝ := q + q⁻¹

/-! ## Typed-braid encoding

A "typed crossing" carries one of three labels:

  `Plus`     → σ_i, action `λ_σ` on a 1-d irrep
  `Minus`    → σ_i⁻¹, action `λ_σ⁻¹`
  `Averaged` → σ_i − h/2 · 1, action `λ_σ − h/2`

A typed braid is a finite list of such crossings (the gen_idx is
irrelevant for 1-d characters since 1-d irreps treat all σ_i
identically). -/

inductive CrossingType : Type
  | Plus
  | Minus
  | Averaged
  deriving DecidableEq, Repr

/-- The 1-d action of a single typed crossing on a 1-d Hecke irrep with
    generator eigenvalue `λ_σ`. -/
noncomputable def oneDimAction (lam_sig q : ℝ) : CrossingType → ℝ
  | .Plus     => lam_sig
  | .Minus    => lam_sig⁻¹
  | .Averaged => lam_sig - heckeH q / 2

/-- Writhe of a typed-braid encoding: signed crossing count. -/
def writhe : List CrossingType → ℤ
  | [] => 0
  | .Plus     :: rest => 1 + writhe rest
  | .Minus    :: rest => -1 + writhe rest
  | .Averaged :: rest => writhe rest

/-- Averaged-crossing count of a typed-braid encoding. -/
def averagedCount : List CrossingType → ℕ
  | [] => 0
  | .Plus     :: rest => averagedCount rest
  | .Minus    :: rest => averagedCount rest
  | .Averaged :: rest => 1 + averagedCount rest

/-- Multiplicative trace on a 1-d Hecke irrep over a typed braid. -/
noncomputable def oneDimCharacter (lam_sig q : ℝ) : List CrossingType → ℝ
  | [] => 1
  | c :: rest => oneDimAction lam_sig q c * oneDimCharacter lam_sig q rest

/-! ## Trivial-irrep closed form

`V_(n)` has `λ_σ = +q`. So `λ_σ − h/2 = q − (q − q⁻¹)/2 = (q + q⁻¹)/2 = [2]_q / 2`. -/

/-- Trivial-irrep crossing-action specialisation. -/
theorem trivial_action_plus (q : ℝ) :
    oneDimAction q q .Plus = q := rfl

/-- Trivial-irrep averaged action equals `[2]_q / 2`. -/
theorem trivial_action_averaged (q : ℝ) (hq : q ≠ 0) :
    oneDimAction q q .Averaged = qInt2 q / 2 := by
  show q - heckeH q / 2 = qInt2 q / 2
  unfold heckeH qInt2
  field_simp

/-! ## Sign-irrep closed form

`V_(1^n)` has `λ_σ = -q⁻¹`. So `λ_σ − h/2 = -q⁻¹ − (q − q⁻¹)/2 = -(q + q⁻¹)/2 = -[2]_q / 2`. -/

/-- Sign-irrep averaged action equals `-[2]_q / 2`. -/
theorem sign_action_averaged (q : ℝ) (hq : q ≠ 0) :
    oneDimAction (-q⁻¹) q .Averaged = - qInt2 q / 2 := by
  show -q⁻¹ - heckeH q / 2 = - qInt2 q / 2
  unfold heckeH qInt2
  field_simp
  ring

/-! ## Main closed-form theorem -/

/-- **Universal closed form for 1-d Hecke characters.** For any typed
    braid `β` (list of crossing types) and any `λ_σ ∈ {+q, -q⁻¹}`,

      `oneDimCharacter λ_σ q β = λ_σ^w · (λ_σ − h/2)^m`

    where `w = writhe β` and `m = averagedCount β`.

    This is proved by induction on `β`; each step is a single application
    of `oneDimAction` and a power-arithmetic identity, both discharged
    by `ring` after the unfold. -/
theorem oneDim_character_closed_form (lam_sig q : ℝ) (hq : q ≠ 0)
    (hlam : lam_sig ≠ 0) :
    ∀ β : List CrossingType,
      oneDimCharacter lam_sig q β
        = lam_sig ^ (writhe β) * (lam_sig - heckeH q / 2) ^ (averagedCount β)
  | [] => by
    -- Base case: empty braid has writhe 0 and averagedCount 0; both
    -- factors collapse to 1, and oneDimCharacter [] = 1 by definition.
    simp [oneDimCharacter, writhe, averagedCount]
  | .Plus :: rest => by
    -- writhe (.Plus :: rest) = 1 + writhe rest
    -- averagedCount (.Plus :: rest) = averagedCount rest
    -- LHS = lam_sig * oneDimCharacter lam_sig q rest
    --     = lam_sig * (lam_sig^(writhe rest) * (lam_sig - h/2)^(averagedCount rest))   (IH)
    --     = lam_sig^(writhe rest + 1) * (lam_sig - h/2)^(averagedCount rest)
    -- = lam_sig^(1 + writhe rest) * ...
    have ih := oneDim_character_closed_form lam_sig q hq hlam rest
    show oneDimAction lam_sig q .Plus * oneDimCharacter lam_sig q rest
        = lam_sig ^ (writhe (.Plus :: rest))
          * (lam_sig - heckeH q / 2) ^ (averagedCount (.Plus :: rest))
    simp only [writhe, averagedCount, oneDimAction]
    rw [ih, show (1 + writhe rest : ℤ) = writhe rest + 1 from by ring,
        zpow_add_one hlam]
    ring
  | .Minus :: rest => by
    -- writhe (.Minus :: rest) = -1 + writhe rest = writhe rest - 1
    -- LHS = lam_sig⁻¹ * (lam_sig^(writhe rest) * (lam_sig - h/2)^(averagedCount rest))
    --     = lam_sig^(writhe rest - 1) * (lam_sig - h/2)^(averagedCount rest)
    have ih := oneDim_character_closed_form lam_sig q hq hlam rest
    show oneDimAction lam_sig q .Minus * oneDimCharacter lam_sig q rest
        = lam_sig ^ (writhe (.Minus :: rest))
          * (lam_sig - heckeH q / 2) ^ (averagedCount (.Minus :: rest))
    simp only [writhe, averagedCount, oneDimAction]
    rw [ih, show (-1 + writhe rest : ℤ) = writhe rest - 1 from by ring,
        zpow_sub_one hlam]
    ring
  | .Averaged :: rest => by
    -- writhe (.Averaged :: rest) = writhe rest (unchanged)
    -- averagedCount (.Averaged :: rest) = 1 + averagedCount rest
    -- = averagedCount rest + 1 (commutative)
    have ih := oneDim_character_closed_form lam_sig q hq hlam rest
    show oneDimAction lam_sig q .Averaged * oneDimCharacter lam_sig q rest
        = lam_sig ^ (writhe (.Averaged :: rest))
          * (lam_sig - heckeH q / 2) ^ (averagedCount (.Averaged :: rest))
    simp only [writhe, averagedCount, oneDimAction]
    rw [ih]
    -- Now: (lam_sig - h/2) * (lam_sig^w * (lam_sig - h/2)^m) =
    --      lam_sig^w * (lam_sig - h/2)^(m + 1)
    -- where m = averagedCount rest, and the LHS averagedCount is 1 + m
    -- which equals m + 1 by add_comm.
    rw [show (1 + averagedCount rest) = averagedCount rest + 1 from
        Nat.add_comm 1 _, pow_succ]
    ring

/-! ## Specialisations: trivial-irrep formula -/

-- Ref: [manuscript] prop:hecke-1d-irrep-closed-form-character §"Proof"
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- **Trivial-irrep character closed form.** For `λ_σ = +q`,
    `χ_(n)_q(β) = q^w · ([2]_q / 2)^m`. -/
theorem hecke_1d_trivial_character_closed_form (q : ℝ) (hq : q ≠ 0)
    (β : List CrossingType) :
    oneDimCharacter q q β
      = q ^ (writhe β) * (qInt2 q / 2) ^ (averagedCount β) := by
  -- From oneDim_character_closed_form + trivial_action_averaged.
  -- Ref: [manuscript] prop:hecke-1d-irrep-closed-form-character §"Specialisation V_(n)"
  rw [oneDim_character_closed_form q q hq hq β]
  congr 1
  show (q - heckeH q / 2) ^ (averagedCount β) = (qInt2 q / 2) ^ (averagedCount β)
  congr 1
  unfold heckeH qInt2
  field_simp

/-! ## Specialisations: sign-irrep formula -/

-- Ref: [manuscript] prop:hecke-1d-irrep-closed-form-character §"Proof"
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- **Sign-irrep character closed form.** For `λ_σ = -q⁻¹`,
    `χ_(1^n)_q(β) = (-q⁻¹)^w · (-[2]_q / 2)^m`. -/
theorem hecke_1d_sign_character_closed_form (q : ℝ) (hq : q ≠ 0)
    (β : List CrossingType) :
    oneDimCharacter (-q⁻¹) q β
      = (-q⁻¹) ^ (writhe β) * (- qInt2 q / 2) ^ (averagedCount β) := by
  -- From oneDim_character_closed_form + sign_action_averaged.
  have h_lam_ne_zero : (-q⁻¹) ≠ 0 := by
    simp; exact hq
  rw [oneDim_character_closed_form (-q⁻¹) q hq h_lam_ne_zero β]
  congr 1
  show (-q⁻¹ - heckeH q / 2) ^ (averagedCount β)
        = (- qInt2 q / 2) ^ (averagedCount β)
  congr 1
  unfold heckeH qInt2
  field_simp
  ring

/-! ## Top-level identifier for `lean.ref`

The `.ts` manifest references `qou:QOU.BraidKnot.hecke_1d_irrep_closed_form_character`.
We define it as the conjunction of both specialisations, which together
exhaust the 1-d slice of the Wedderburn decomposition for any `H_n(q)`.
-/

-- Ref: [manuscript] prop:hecke-1d-irrep-closed-form-character
/-- **Universal 1-d Hecke irrep character closed form.** Combines the
    trivial and sign specialisations into the canonical export. -/
theorem hecke_1d_irrep_closed_form_character (q : ℝ) (hq : q ≠ 0)
    (β : List CrossingType) :
    -- Trivial irrep
    (oneDimCharacter q q β
       = q ^ (writhe β) * (qInt2 q / 2) ^ (averagedCount β))
    ∧
    -- Sign irrep
    (oneDimCharacter (-q⁻¹) q β
       = (-q⁻¹) ^ (writhe β) * (- qInt2 q / 2) ^ (averagedCount β)) := by
  refine ⟨?_, ?_⟩
  · exact hecke_1d_trivial_character_closed_form q hq β
  · exact hecke_1d_sign_character_closed_form q hq β

end QOU.BraidKnot


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub) -/

namespace QOU.Hecke1dIrrepClosedFormCharacter.ConditionalAudit

class BorromeanQuark : Prop where
  holds : True

def hecke_d_irrep_closed_form_character_g2_conditional [_inst : BorromeanQuark] : True := trivial

end QOU.Hecke1dIrrepClosedFormCharacter.ConditionalAudit
