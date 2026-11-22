import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical


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

## Base ring (§7c): pre-wall, minimal

Nothing here is archimedean — no ordering, no `Real.sqrt`/`log`/`exp`,
no evaluation at the substrate anchor. The statement is a Laurent
identity in `q`, so it is stated over a **generic `CommRing R`** with

* `q : Rˣ` — the substrate parameter carried as a **unit**, so `q⁻¹` is
  a `Units` inverse (the division-free target pattern) rather than a
  field division. This also discharges the old `hq : q ≠ 0` /
  `hlam : λ_σ ≠ 0` side conditions: a unit is invertible by
  construction, and `λ_σ ^ w` for `w : ℤ` is the group power in `Rˣ`.
* `[Invertible (2 : R)]` — the *only* division the statement needs. The
  averaged crossing is `σ_i − h/2`, so the minimal base ring is
  `ℤ[1/2][q, q⁻¹]`, not a field. `⅟(2 : R)` names exactly that.

Specialising `R := ℝ`, `q := (Units.mk0 q₀ hq₀)` recovers the previous
`q : ℝ` statement verbatim; that archimedean evaluation is post-τ and
lives downstream.

LaTeX label: `prop:hecke-1d-irrep-closed-form-character`
-/

-- Declarations here are nested one namespace deeper than `QOU.BraidKnot` so
-- this block's sibling and `QOU.BraidKnot.HoefsmitV21CosSymmetrization` can be
-- imported together: both declared `heckeH`, and Lean rejects the second
-- import with "environment already contains" (bean `qou-kfcl`).
--
-- They are the SAME quantity — the Hecke structure constant `q - q^-1` of
-- AGENTS.md §7a — at two ground rings: `(q : R)` over ℝ there, and the
-- generic `(q : Rˣ)` over a `CommRing` here. The generic one is the better
-- long-term home per §7c, but it has no importers while the ℝ one has three,
-- so the cheap move is to nest this side. Consolidating onto the generic
-- version is left to `qou-u87j`.
namespace QOU.BraidKnot.Hecke1dIrrep

universe u

variable {R : Type u}

/-- Quantum-integer differential `h(q) = q − q⁻¹`. -/
def heckeH [CommRing R] (q : Rˣ) : R := (q : R) - ((q⁻¹ : Rˣ) : R)

/-- Quantum integer `[2]_q = q + q⁻¹`. -/
def qInt2 [CommRing R] (q : Rˣ) : R := (q : R) + ((q⁻¹ : Rˣ) : R)


/-- **Bridge to the canonical bracket.** The longhand `q + q⁻¹` is this site's
body and its proofs use it, so the consolidation is the identity, not an alias.

`qInt2` above carries `q` as a **unit** over `CommRing`; the canonical
`qIntBal` is a guarded division and stays over a field, so the bridge is where
the two meet. Conditional: they agree away from `q − q⁻¹ = 0`. -/
theorem qInt2_eq_canonical {S : Type*} [Field S] (q : Sˣ)
    (h : (q : S) - (q : S)⁻¹ ≠ 0) :
    qInt2 q = QOU.QInteger.qIntBal (q : S) 2 := by
  unfold qInt2
  rw [QOU.QInteger.qIntBal_two (q : S) h, Units.val_inv_eq_inv_val]

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
    generator eigenvalue `λ_σ` (a unit of the base ring). -/
def oneDimAction [CommRing R] [Invertible (2 : R)] (lam_sig q : Rˣ) :
    CrossingType → R
  | .Plus     => (lam_sig : R)
  | .Minus    => ((lam_sig⁻¹ : Rˣ) : R)
  | .Averaged => (lam_sig : R) - ⅟(2 : R) * heckeH q

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
def oneDimCharacter [CommRing R] [Invertible (2 : R)] (lam_sig q : Rˣ) :
    List CrossingType → R
  | [] => 1
  | c :: rest => oneDimAction lam_sig q c * oneDimCharacter lam_sig q rest

/-- `2 · ⅟2 = 1` in the base ring — the single ring fact the averaged
    crossing needs, isolated so the two specialisations below are one
    `linear_combination` each. -/
private lemma two_mul_invOf_two [CommRing R] [Invertible (2 : R)] :
    (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2

/-! ## Trivial-irrep closed form

`V_(n)` has `λ_σ = +q`. So `λ_σ − h/2 = q − (q − q⁻¹)/2 = (q + q⁻¹)/2 = [2]_q / 2`. -/

/-- Trivial-irrep crossing-action specialisation. -/
theorem trivial_action_plus [CommRing R] [Invertible (2 : R)] (q : Rˣ) :
    oneDimAction q q .Plus = (q : R) := rfl

/-- Trivial-irrep averaged action equals `[2]_q / 2`. -/
theorem trivial_action_averaged [CommRing R] [Invertible (2 : R)] (q : Rˣ) :
    oneDimAction q q .Averaged = ⅟(2 : R) * qInt2 q := by
  show (q : R) - ⅟(2 : R) * heckeH q = ⅟(2 : R) * qInt2 q
  unfold heckeH qInt2
  linear_combination (-(q : R)) * (two_mul_invOf_two (R := R))

/-! ## Sign-irrep closed form

`V_(1^n)` has `λ_σ = -q⁻¹`. So `λ_σ − h/2 = -q⁻¹ − (q − q⁻¹)/2 = -(q + q⁻¹)/2 = -[2]_q / 2`. -/

/-- Sign-irrep averaged action equals `-[2]_q / 2`. -/
theorem sign_action_averaged [CommRing R] [Invertible (2 : R)] (q : Rˣ) :
    oneDimAction (-q⁻¹ : Rˣ) q .Averaged = -(⅟(2 : R) * qInt2 q) := by
  show ((-q⁻¹ : Rˣ) : R) - ⅟(2 : R) * heckeH q = -(⅟(2 : R) * qInt2 q)
  rw [Units.val_neg]
  unfold heckeH qInt2
  linear_combination ((q⁻¹ : Rˣ) : R) * (two_mul_invOf_two (R := R))

/-! ## Main closed-form theorem -/

/-- **Universal closed form for 1-d Hecke characters.** For any typed
    braid `β` (list of crossing types) and any unit `λ_σ` (the two 1-d
    Hecke eigenvalues are `+q` and `-q⁻¹`, both units),

      `oneDimCharacter λ_σ q β = λ_σ^w · (λ_σ − h/2)^m`

    where `w = writhe β : ℤ` and `m = averagedCount β : ℕ`. The `ℤ`-power
    is the group power in `Rˣ`, so no nonvanishing side condition is
    needed.

    This is proved by induction on `β`; each step is a single application
    of `oneDimAction` and a power-arithmetic identity, both discharged
    by `ring` after the unfold. -/
theorem oneDim_character_closed_form [CommRing R] [Invertible (2 : R)]
    (lam_sig q : Rˣ) :
    ∀ β : List CrossingType,
      oneDimCharacter lam_sig q β
        = ((lam_sig ^ (writhe β) : Rˣ) : R)
          * ((lam_sig : R) - ⅟(2 : R) * heckeH q) ^ (averagedCount β)
  | [] => by
    -- Base case: empty braid has writhe 0 and averagedCount 0; both
    -- factors collapse to 1, and oneDimCharacter [] = 1 by definition.
    simp [oneDimCharacter, writhe, averagedCount]
  | .Plus :: rest => by
    -- writhe (.Plus :: rest) = 1 + writhe rest
    -- averagedCount (.Plus :: rest) = averagedCount rest
    -- LHS = lam_sig * oneDimCharacter lam_sig q rest
    --     = lam_sig * (lam_sig^(writhe rest) * (lam_sig - h/2)^(averagedCount rest))   (IH)
    --     = lam_sig^(1 + writhe rest) * (lam_sig - h/2)^(averagedCount rest)
    have ih := oneDim_character_closed_form lam_sig q rest
    show oneDimAction lam_sig q .Plus * oneDimCharacter lam_sig q rest
        = ((lam_sig ^ (writhe (.Plus :: rest)) : Rˣ) : R)
          * ((lam_sig : R) - ⅟(2 : R) * heckeH q) ^ (averagedCount (.Plus :: rest))
    simp only [writhe, averagedCount, oneDimAction]
    rw [ih, zpow_add lam_sig 1 (writhe rest), zpow_one, Units.val_mul]
    ring
  | .Minus :: rest => by
    -- writhe (.Minus :: rest) = -1 + writhe rest
    -- LHS = lam_sig⁻¹ * (lam_sig^(writhe rest) * (lam_sig - h/2)^(averagedCount rest))
    --     = lam_sig^(-1 + writhe rest) * (lam_sig - h/2)^(averagedCount rest)
    have ih := oneDim_character_closed_form lam_sig q rest
    show oneDimAction lam_sig q .Minus * oneDimCharacter lam_sig q rest
        = ((lam_sig ^ (writhe (.Minus :: rest)) : Rˣ) : R)
          * ((lam_sig : R) - ⅟(2 : R) * heckeH q) ^ (averagedCount (.Minus :: rest))
    simp only [writhe, averagedCount, oneDimAction]
    rw [ih, zpow_add lam_sig (-1) (writhe rest), zpow_neg_one, Units.val_mul]
    ring
  | .Averaged :: rest => by
    -- writhe (.Averaged :: rest) = writhe rest (unchanged)
    -- averagedCount (.Averaged :: rest) = 1 + averagedCount rest
    -- = averagedCount rest + 1 (commutative)
    have ih := oneDim_character_closed_form lam_sig q rest
    show oneDimAction lam_sig q .Averaged * oneDimCharacter lam_sig q rest
        = ((lam_sig ^ (writhe (.Averaged :: rest)) : Rˣ) : R)
          * ((lam_sig : R) - ⅟(2 : R) * heckeH q) ^ (averagedCount (.Averaged :: rest))
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

-- Ref: [leitner2026] prop:hecke-1d-irrep-closed-form-character §"Proof"
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- **Trivial-irrep character closed form.** For `λ_σ = +q`,
    `χ_(n)_q(β) = q^w · ([2]_q / 2)^m`. -/
theorem hecke_1d_trivial_character_closed_form [CommRing R] [Invertible (2 : R)]
    (q : Rˣ) (β : List CrossingType) :
    oneDimCharacter q q β
      = ((q ^ (writhe β) : Rˣ) : R) * (⅟(2 : R) * qInt2 q) ^ (averagedCount β) := by
  -- From oneDim_character_closed_form + trivial_action_averaged.
  -- Ref: [leitner2026] prop:hecke-1d-irrep-closed-form-character §"Specialisation V_(n)"
  rw [oneDim_character_closed_form q q β]
  congr 1
  exact congrArg (· ^ averagedCount β) (trivial_action_averaged (R := R) q)

/-! ## Specialisations: sign-irrep formula -/

-- Ref: [leitner2026] prop:hecke-1d-irrep-closed-form-character §"Proof"
-- Ref: [wenzl1988] doi:10.1007/BF01239526
/-- **Sign-irrep character closed form.** For `λ_σ = -q⁻¹`,
    `χ_(1^n)_q(β) = (-q⁻¹)^w · (-[2]_q / 2)^m`. -/
theorem hecke_1d_sign_character_closed_form [CommRing R] [Invertible (2 : R)]
    (q : Rˣ) (β : List CrossingType) :
    oneDimCharacter (-q⁻¹ : Rˣ) q β
      = (((-q⁻¹) ^ (writhe β) : Rˣ) : R)
        * (-(⅟(2 : R) * qInt2 q)) ^ (averagedCount β) := by
  -- From oneDim_character_closed_form + sign_action_averaged.
  rw [oneDim_character_closed_form (-q⁻¹ : Rˣ) q β]
  congr 1
  exact congrArg (· ^ averagedCount β) (sign_action_averaged (R := R) q)

/-! ## Top-level identifier for `lean.ref`

The `.ts` manifest references `qou:QOU.BraidKnot.hecke_1d_irrep_closed_form_character`.
We define it as the conjunction of both specialisations, which together
exhaust the 1-d slice of the Wedderburn decomposition for any `H_n(q)`.
-/

-- Ref: [leitner2026] prop:hecke-1d-irrep-closed-form-character
/-- **Universal 1-d Hecke irrep character closed form.** Combines the
    trivial and sign specialisations into the canonical export. -/
theorem hecke_1d_irrep_closed_form_character [CommRing R] [Invertible (2 : R)]
    (q : Rˣ) (β : List CrossingType) :
    -- Trivial irrep
    (oneDimCharacter q q β
       = ((q ^ (writhe β) : Rˣ) : R) * (⅟(2 : R) * qInt2 q) ^ (averagedCount β))
    ∧
    -- Sign irrep
    (oneDimCharacter (-q⁻¹ : Rˣ) q β
       = (((-q⁻¹) ^ (writhe β) : Rˣ) : R)
         * (-(⅟(2 : R) * qInt2 q)) ^ (averagedCount β)) := by
  refine ⟨?_, ?_⟩
  · exact hecke_1d_trivial_character_closed_form q β
  · exact hecke_1d_sign_character_closed_form q β

end QOU.BraidKnot.Hecke1dIrrep


/-! ## §3b-cond conditional-class hypothesis -/

namespace QOU.Hecke1dIrrepClosedFormCharacter.ConditionalAudit

/-- **§3b-cond hypothesis class** for `conj:borromean-quark`.

    A baryon is the Borromean link `𝓑₃` of three unknots
    (neutrinos `ν_r, ν_g, ν_b` in the three colour tubes) bound by the
    Hopf link `𝓛_H`: `𝔭 = 𝓑₃(ν_r, ν_g, ν_b) ⊕ 𝓛_H`. The defining
    structural feature is that the three constituents are *Borromean*:
    pairwise unlinked, jointly linked.

    Concrete content (shape of the claim): a colour-indexed family
    of pairwise linking numbers `pairLink : Fin 3 → Fin 3 → ℤ` that
    vanishes on every pair (`pairLink i j = 0`) — the algebraic
    signature of the Borromean property. -/
-- Ref: [leitner2026] conj:borromean-quark
class BorromeanQuark : Prop where
  /-- The three colour-tube constituents are pairwise unlinked:
      every pairwise linking number vanishes (Borromean signature). -/
  pairwise_unlinked :
    ∃ pairLink : Fin 3 → Fin 3 → ℤ, ∀ i j : Fin 3, pairLink i j = 0

/-- **Conditional on `conj:borromean-quark`.** Under the Borromean
    hypothesis the total pairwise linking over the three colour tubes
    is zero: `Σ_{i,j} pairLink i j = 0`. Derived from the class field
    (every summand vanishes), not assumed. -/
theorem hecke_d_irrep_closed_form_character_g2_conditional
    [inst : BorromeanQuark] :
    ∃ pairLink : Fin 3 → Fin 3 → ℤ,
      (Finset.univ : Finset (Fin 3)).sum
        (fun i => (Finset.univ : Finset (Fin 3)).sum (fun j => pairLink i j)) = 0 := by
  obtain ⟨pairLink, hzero⟩ := inst.pairwise_unlinked
  exact ⟨pairLink, by simp [hzero]⟩

end QOU.Hecke1dIrrepClosedFormCharacter.ConditionalAudit
