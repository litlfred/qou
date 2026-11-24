/-
# The decay fibre from bar-parity, WITHOUT the two-row cap

Companion to `QOU.QBeta.DecayBlockCarrier`, which proved

    tr(Δ_S)(z) = g(z) · χ^(3)(Δ_S),    g(z) = (2qz − q² + 1)/(q² + 1)

with `χ^(3)(Δ_S)` a fixed rational function of `q`. This file computes how each
factor behaves under the fibre bar involution `q ↦ q⁻¹` and draws the iff.

## Why it matters

The admissible set `{q, z_D}` comes from the two-row cap `y_(1³) = 0`
(`QOU.QBeta.AdmissibleRoots`). That cap is the MASS channel's forcing; that the
DECAY channel must satisfy it is settled by the 2026-08-15 owner ruling, and the
trace-convention registry preserves the prior analysis explicitly — *"its finding
that neither convention was DERIVED for this channel stands"*. So an exclusion
resting only on the cap rests on a decision.

The results here rest on neither. They exclude `z = 1` and `z_C` from bar-parity
alone.

## The premise, stated rather than smuggled

Turning the iff below into an exclusion needs *"the decay trace must have
definite bar-parity"*. That is corpus-standard (`fig8Trace_im_odd`,
`ZBarParity`) and is **not** proved here. The theorems themselves are
unconditional facts about `Δ_S`.

## The limit

The full-bar family is `z_D + (any bar-even function)` and contains `z = q` as
well, so bar-parity NARROWS the fibre to full-bar — it does not pin a unique
`z`. `barSum_full_bar_of_full_bar` records exactly that.

Base ring: generic `[Field R]` per AGENTS.md §7c. The bar involution is modelled
by evaluating at `q⁻¹`, so no ordering and nothing archimedean is needed.

-- Ref: [leitner2026] bean `qou-cds1`; probe
--      computations/qbeta/qbeta_decay_fibre_bar_parity_derivation_probe.py
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.DecayFibreBarParity

-- `CharZero` because `chi3S` divides by 2 and the iff below divides by `2q`.
variable {R : Type*} [Field R] [CharZero R]

/-- `h = q − q⁻¹`. -/
def hq (q : R) : R := q - q⁻¹

/-- The decay carrier scalar `g(z) = y_(3)(z) − y_(1³)(z)`, from
`DecayBlockCarrier`. -/
def g (q z : R) : R := (2 * q * z - q ^ 2 + 1) / (q ^ 2 + 1)

/-- `χ^(3)(Δ_S) = h²/2 − h·q`, from `DecayBlockCarrier.chi3_deltaS`. -/
def chi3S (q : R) : R := hq q ^ 2 / 2 - hq q * q

/-- The full-bar condition on the Markov parameter: `bar(z) = z − h`. -/
def FullBar (q z zbar : R) : Prop := zbar = z - hq q

section
variable {q : R} (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)

include hq0

/-- **The fixed character is bar-ODD.** `χ^(3)(Δ_S)` at `q⁻¹` is its negative. -/
theorem chi3S_bar_odd : chi3S q⁻¹ = -chi3S q := by
  unfold chi3S hq
  field_simp
  ring

include hq2 in
/-- **`g` at the bar point, over the SAME denominator.** `g(q⁻¹, w)` has
denominator `q⁻²+1`; clearing it to `q²+1` first is what lets every identity
below close by `ring`. Without this, `field_simp` strands a `(1+q²)⁻¹` inside a
sum where `ring` cannot reach it. -/
theorem g_at_inv (w : R) : g q⁻¹ w = (2 * q * w - 1 + q ^ 2) / (q ^ 2 + 1) := by
  unfold g
  have hden : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro hc
    have hq2ne : q ^ 2 ≠ 0 := pow_ne_zero 2 hq0
    field_simp at hc
    exact hq2 (by linear_combination hc)
  rw [div_eq_div_iff hden hq2]
  field_simp
  ring

include hq2 in
/-- **The bar-defect of the carrier scalar, cleared of denominators.** -/
theorem g_bar_defect_mul (z zbar : R) :
    (g q⁻¹ zbar - g q z) * (q ^ 2 + 1) = 2 * q * (zbar - (z - hq q)) := by
  rw [g_at_inv hq0 hq2]
  unfold g hq
  field_simp
  ring

include hq2 in
/-- **The carrier scalar is bar-EVEN exactly on the full-bar condition.**
`g` at `(q⁻¹, zbar)` equals `g(q, z)` iff `zbar = z − h`.

From `g_bar_defect_mul`: the cleared defect is `2q·(zbar − (z−h))`, which
vanishes exactly when `zbar = z − h`, given `q ≠ 0` and `2 ≠ 0`. No ordering is
used anywhere — an earlier attempt reached for `nlinarith` and then `linarith`,
both of which need an ORDERED field and are simply unavailable over a generic
one. -/
theorem g_bar_even_iff_fullBar (z zbar : R) :
    g q⁻¹ zbar = g q z ↔ FullBar q z zbar := by
  have h2 : (2 : R) ≠ 0 := by norm_num
  constructor
  · intro hEq
    have hdef := g_bar_defect_mul hq0 hq2 z zbar
    rw [hEq, sub_self, zero_mul] at hdef
    rcases mul_eq_zero.mp hdef.symm with hc | hd
    · exact absurd hc (mul_ne_zero h2 hq0)
    · unfold FullBar; linear_combination hd
  · intro hEq
    unfold FullBar at hEq
    subst hEq
    have hdef := g_bar_defect_mul hq0 hq2 z (z - hq q)
    rw [sub_self, mul_zero] at hdef
    rcases mul_eq_zero.mp hdef with hz | hden
    · exact sub_eq_zero.mp hz
    · exact absurd hden hq2

end

section
variable {q : R} (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)

include hq0 hq2

/-- **THE FIBRE CONSTRAINT.** When `z` satisfies the full-bar condition, the
decay trace `g(z)·χ^(3)(Δ_S)` is bar-ODD.

This is the half that does the work: it holds with no appeal to `y_(1³) = 0`,
so it is independent of the two-row cap and hence of the owner ruling that
imported the cap into this channel. -/
theorem decayTrace_bar_odd_of_fullBar (z zbar : R) (hfb : FullBar q z zbar) :
    g q⁻¹ zbar * chi3S q⁻¹ = -(g q z * chi3S q) := by
  rw [(g_bar_even_iff_fullBar hq0 hq2 z zbar).mpr hfb, chi3S_bar_odd hq0]
  ring

end

section
variable {q : R} (hq0 : q ≠ 0)

include hq0

/-- **`z = 1` is NOT full-bar** (for `h ≠ 0`, i.e. away from `q = 1`). The
coordinate-sum point is bar-EVEN — `bar(1) = 1` — and bar-even is a DIFFERENT
condition from full-bar. This is the second, cap-free exclusion. -/
theorem one_not_fullBar (hh : hq q ≠ 0) : ¬ FullBar q (1 : R) 1 := by
  unfold FullBar
  intro hEq
  exact hh (by linear_combination hEq)

/-- **A bar-EVEN parameter is never full-bar** away from `q = 1`. `z_C` is
bar-even, which is why the C-frame ladder cannot carry a bar-odd decay trace —
the content of `decayLadder_zC_threeRow_ne_zero`, seen from the parity side. -/
theorem barEven_not_fullBar (z : R) (hh : hq q ≠ 0) : ¬ FullBar q z z := by
  unfold FullBar
  intro hEq
  exact hh (by linear_combination hEq)

end

/-- **The full-bar family is affine over the bar-even functions**, so bar-parity
narrows the fibre without pinning a unique `z`. If `z` is full-bar and `f` is
bar-even, then `z + f` is full-bar too. `z = q` and `z_D` are both in the
family. -/
theorem fullBar_add_barEven {q z zbar f : R} (h : FullBar q z zbar) :
    FullBar q (z + f) (zbar + f) := by
  unfold FullBar at h ⊢
  rw [h]; ring


/-! ### What actually pins `z_D`, and what bar-parity does NOT do

Three conditions are in play and they do different jobs. Keeping them apart is
the point of this section, because conflating them is how "bar-parity closes the
gap" would get written down, and that is false.

* **the two-row cap** `y_(1³) = 0` — narrows to `{q, z_D}` (`AdmissibleRoots`).
  For the DECAY channel this is a RULING, not a derivation.
* **faithfulness** `y_(2,1) ≠ 0` — the corpus's own `hfaith` hypothesis.
  `y_(2,1)(q) = 0` exactly, so the augmentation is the trivial-block-only trace
  and is not faithful. Within the admissible pair this picks `z_D`.
* **full-bar** — derived above. Excludes `z_C` and the CONSTANT `z ≡ 1`.

**The limitation, stated so it cannot be quoted away.** `fullBar_add_barEven`
plus the fact that every constant is bar-even means `z_D + c` is full-bar for
ANY constant `c`. So a full-bar parameter can take ANY value at the substrate
pin, and bar-parity therefore constrains the FUNCTIONAL FORM of `z(q)`, not its
value. `one_not_fullBar` excludes `z ≡ 1` as a choice of parameter; it does NOT
exclude the required VALUE (`z_required ≈ 0.99850`), which a full-bar function
could attain.

Consequently the narrowing to `{q, z_D}` — and hence the exclusion of what the
data wants — still rests on the cap, which for this channel is the ruling. -/

/-- The `(2,1)` Ocneanu weight, as a function of `q` and the Markov parameter. -/
def y21 (q z : R) : R :=
  q * (q - z) * (q * z + 1) / ((q ^ 2 - q + 1) * (q ^ 2 + q + 1))

/-- **The augmentation is NOT faithful:** `y_(2,1)(q) = 0` exactly. This is what
picks `z_D` out of the admissible pair `{q, z_D}` — and it is structural, being
the corpus's own `hfaith` hypothesis, rather than a further ruling. -/
theorem y21_at_augmentation (q : R) : y21 q q = 0 := by
  unfold y21
  rw [sub_self]
  simp

/-- **Every constant is bar-even**, hence `z_D + c` is full-bar whenever `z_D`
is. Together with `fullBar_add_barEven` this is the precise sense in which
bar-parity cannot constrain the value at a point. -/
theorem fullBar_add_const {q z zbar : R} (c : R) (h : FullBar q z zbar) :
    FullBar q (z + c) (zbar + c) := fullBar_add_barEven h


/-! ### Why the cap had to be a ruling: the decay channel is BLIND to it

`DecayBlockCarrier` proved `tr(Δ_S)(z) = (y_(3) − y_(1³)) · χ^(3)(Δ_S)`. The
decay pairing therefore depends on the block weights ONLY through the difference
`y_(3) − y_(1³)`. Together with normalisation that is two constraints on three
unknowns, so a one-parameter family of normalised weight triples produces the
SAME Q-value — and the family sweeps every value of `y_(1³)`.

So the two-row cap `y_(1³) = 0` is not merely un-derived for this channel: it is
**undeterminable by it**. No decay measurement, at any precision, can establish
or refute it. It selects one member of a family the channel cannot tell apart.

That is why it arrived as a ruling, and it says where a derivation would have to
come from: another channel, or a structural argument — never from Q_β itself. -/

/-- **The decay channel cannot determine the three-row weight.** For ANY
prescribed value `t` of `y_(1³)`, there is a normalised weight triple whose
decay pairing is the given `g`. The cap picks one member of this family; the
data cannot. -/
theorem threeRow_undetermined_by_decay (g t : R) :
    ∃ y3 y21 y111 : R,
      y3 - y111 = g ∧ y3 + 2 * y21 + y111 = 1 ∧ y111 = t := by
  refine ⟨g + t, (1 - g - 2 * t) / 2, t, by ring, ?_, rfl⟩
  have h2 : (2 : R) ≠ 0 := by norm_num
  field_simp
  ring

/-- **The `y_(1³) = 0` member of that family**, exhibited: the cap is a choice
of representative, not a consequence. -/
theorem cap_member_of_family (g : R) :
    (g : R) - 0 = g ∧ g + 2 * ((1 - g) / 2) + 0 = 1 := by
  refine ⟨by ring, ?_⟩
  have h2 : (2 : R) ≠ 0 := by norm_num
  field_simp
  ring

end QOU.QBeta.DecayFibreBarParity
