/-
CableShiftFourfold.lean — the cable-shift law on a one-dimensional channel is
exactly multiplicative by four, for EVERY word, positive or not.

THE QUESTION.  Measurement gives `α_shift(C(K)) ≤ 4·α_shift(K)` for the
2-parallel cable, with equality iff the braid word is positive and a one-sided
deviation otherwise.  An earlier pass answered "what is the law for a
non-positive word?" by scanning candidate closed forms in the word's length,
writhe, strand count and `α_shift` — that was a FIT, and it is retracted.  What
follows is the derivation that replaces it.

THE DERIVATION, in two steps, both here.

  1. `writhe_cable` — the 2-parallel substitution `σᵢ ↦ s_{2i} s_{2i−1}
     s_{2i+1} s_{2i}` writes four letters of the SAME sign per letter (an
     inverse reverses the block and negates each, which is the same list of
     four expressions once the signs are pushed through — see `cableBlock`).
     Hence `writhe(C(w)) = 4·writhe(w)`, with no positivity hypothesis.

  2. A one-dimensional channel sees ONLY the writhe — `charOf_eq_zpow` in
     `QOU.BraidKnot.AlphaShiftOneDimChannel`.

Composing them gives `val_charOf_cable`: on the all-row `(n)` and all-column
`(1ⁿ)` channels the valuation scales by exactly four, for every word.  So the
deficit `4·α(K) − α(C(K))` **cannot come from a one-dimensional channel at
all**; it can only arise when the maximizing `λ` is intermediate, where the
character is a sum over standard-tableau paths and no factor of four need
survive.

**The law is therefore a statement about WHICH channel attains the maximum,
not about the word's letters** — which is why no closed form in the counts
exists.  Positivity mattered only because it keeps the maximum on the column
channel.

WHAT IS NOT PROVED, and it is a derived limitation rather than a gap.  Nothing
here bounds the multi-dimensional case, and nothing here claims the deficit is
nonzero — that the deficit is REAL is a measurement
(`computations/meson/cable_shift_where_the_deficit_lives_probe.py`, 5 words
with a nonzero deficit, every one of them with a multi-dimensional maximizer,
and 7 words with a one-dimensional maximizer at both ends, every one of them
with deficit zero).  This file proves the half that forces the deficit OUT of
the one-dimensional channels; the probe locates where it went.

No `ℝ`, no ordering, nothing archimedean (AGENTS.md §7c); and no calibration
input — `α_shift` is a fibre-level valuation in the formal `q` and consumes
none of CAL-1/2/3.

@module QOU.BraidKnot.CableShiftFourfold
-/

import QOU.BraidKnot.AlphaShiftOneDimChannel

set_option autoImplicit false

namespace QOU.BraidKnot

variable {G : Type*} [CommGroup G]

/-- The four letters the 2-parallel substitution writes for one letter `g`.

For `g = i > 0` this is `σ_{2i} σ_{2i−1} σ_{2i+1} σ_{2i}`, the standard
2-parallel image.  For `g = −i < 0` the image is the block reversed with every
letter inverted, `σ_{2i}⁻¹ σ_{2i+1}⁻¹ σ_{2i−1}⁻¹ σ_{2i}⁻¹` — which is the SAME
list of expressions in `g`, since `−(2i+1) = 2g − 1` and `−(2i−1) = 2g + 1`.
That coincidence is why the sign bookkeeping below needs no case split on the
letter's own sign beyond `g ≠ 0`. -/
def cableBlock (g : Int) : Word := [2 * g, 2 * g - 1, 2 * g + 1, 2 * g]

/-- The 2-parallel cable of a braid word. -/
def cable : Word → Word
  | [] => []
  | g :: rest => cableBlock g ++ cable rest

/-- Every letter of a positive letter's block is positive. -/
theorem writhe_cableBlock_pos {g : Int} (hg : 0 < g) : writhe (cableBlock g) = 4 := by
  have h1 : (0 : Int) < 2 * g := by omega
  have h2 : (0 : Int) < 2 * g - 1 := by omega
  have h2' : (1 : Int) < 2 * g := by omega
  have h3 : (0 : Int) < 2 * g + 1 := by omega
  simp [cableBlock, writhe, h1, h2', h3]

/-- Every letter of an inverse letter's block is negative. -/
theorem writhe_cableBlock_neg {g : Int} (hg : g < 0) : writhe (cableBlock g) = -4 := by
  have h1 : ¬ ((0 : Int) < 2 * g) := by omega
  have h2 : ¬ ((0 : Int) < 2 * g - 1) := by omega
  have h2' : ¬ ((1 : Int) < 2 * g) := by omega
  have h3 : ¬ ((0 : Int) < 2 * g + 1) := by omega
  simp [cableBlock, writhe, h1, h2', h3]

/-- One letter contributes exactly four letters of its own sign. -/
theorem writhe_cableBlock {g : Int} (hg : g ≠ 0) :
    writhe (cableBlock g) = 4 * (if 0 < g then (1 : Int) else -1) := by
  rcases lt_trichotomy g 0 with h | h | h
  · rw [if_neg (by omega), writhe_cableBlock_neg h]; norm_num
  · exact absurd h hg
  · rw [if_pos h, writhe_cableBlock_pos h]; norm_num

/-- **(P1) The writhe quadruples**, for every word — positive, negative or
mixed.  The only hypothesis is that the letters are genuine braid generators
(`g ≠ 0`); the substitution never mixes signs within a block. -/
theorem writhe_cable : ∀ w : Word, (∀ g ∈ w, g ≠ 0) → writhe (cable w) = 4 * writhe w := by
  intro w
  induction w with
  | nil => intro _; simp [cable, writhe]
  | cons g rest ih =>
      intro hw
      have hg : g ≠ 0 := hw g (by simp)
      have hrest : ∀ x ∈ rest, x ≠ 0 := fun x hx => hw x (by simp [hx])
      show writhe (cableBlock g ++ cable rest)
           = 4 * ((if 0 < g then (1 : Int) else -1) + writhe rest)
      rw [writhe_conj, writhe_cableBlock hg, ih hrest, mul_add]

/-- The cable of a word has four times its length: the substitution is
length-multiplying by the same factor it multiplies the writhe by. -/
theorem length_cable (w : Word) : (cable w).length = 4 * w.length := by
  induction w with
  | nil => simp [cable]
  | cons g rest ih =>
      show (cableBlock g ++ cable rest).length = 4 * (rest.length + 1)
      rw [List.length_append, ih]
      simp [cableBlock]
      omega

/-- **The character on a one-dimensional channel is a fourth power.**  Since
such a channel sees only the writhe (`charOf_eq_zpow`) and the writhe
quadruples, cabling raises the character to the fourth — with no positivity
hypothesis anywhere. -/
theorem charOf_cable (s : G) {w : Word} (hw : ∀ g ∈ w, g ≠ 0) :
    charOf s (cable w) = (charOf s w) ^ (4 : Int) := by
  have h : (4 : Int) * writhe w = writhe w * 4 := by ring
  rw [charOf_eq_zpow, charOf_eq_zpow, writhe_cable w hw, h, zpow_mul]

/-- **(P2) The cable-shift law on a one-dimensional channel: exactly ×4, for
every word.**  This is the derived statement that answers "what is the law for
a non-positive word?" — the law is the same one, because a one-dimensional
channel cannot tell a non-positive word from a positive one except through its
writhe. -/
theorem val_charOf_cable (val : G → Int) (hmul : ∀ a b : G, val (a * b) = val a + val b)
    (hone : val 1 = 0) (s : G) {w : Word} (hw : ∀ g ∈ w, g ≠ 0) :
    val (charOf s (cable w)) = 4 * val (charOf s w) := by
  rw [val_charOf val hmul hone, val_charOf val hmul hone, writhe_cable w hw, mul_assoc]

/-- **(P3, the half that is provable here) The deficit vanishes on a
one-dimensional channel.**  `4·α − α(cable)` is identically zero there, so a
nonzero deficit forces the maximizing partition to be intermediate.  Which
partition actually attains the maximum is a measurement, not a theorem — see
the module docstring. -/
theorem cable_deficit_zero_on_oneDim (val : G → Int)
    (hmul : ∀ a b : G, val (a * b) = val a + val b) (hone : val 1 = 0)
    (s : G) {w : Word} (hw : ∀ g ∈ w, g ≠ 0) :
    4 * val (charOf s w) - val (charOf s (cable w)) = 0 := by
  rw [val_charOf_cable val hmul hone s hw]
  ring

/-- **Non-vacuity I.**  A genuinely non-positive word — `σ₁σ₁σ₂⁻¹`, which
contains an inverse letter — still quadruples.  Without this the ×4 law above
could be read as a positive-word statement carrying an unused hypothesis. -/
theorem writhe_cable_nonpositive_witness :
    writhe (cable [(1 : Int), 1, -2]) = 4 ∧ writhe [(1 : Int), 1, -2] = 1 := by
  constructor <;> decide

/-- The witness word really is non-positive. -/
theorem nonpositive_witness_has_inverse_letter :
    ∃ g ∈ ([(1 : Int), 1, -2] : Word), g < 0 := by decide

/-- **Non-vacuity II.**  The `g ≠ 0` hypothesis is load-bearing, not
decorative: a degenerate zero letter produces a block with MIXED signs
(`[0, -1, 1, 0]`), and the ×4 law fails on it.  Recorded so that a later reader
does not drop the hypothesis as noise. -/
theorem writhe_cable_fails_on_zero_letter :
    writhe (cable [(0 : Int)]) ≠ 4 * writhe [(0 : Int)] := by decide


/-! ### What the law actually rides on: multiplicativity, not cyclicity

A sibling session raised this on PR #5863 and it is a real sharpening, verified
here rather than taken on trust.  The framing above says "a one-dimensional
channel sees only the writhe".  True, but it names the channel rather than the
property.  Two properties are in play and only one of them does the work:

  * **Cyclicity** (`χ(xy) = χ(yx)`) is shared — every character is a class
    function, the multi-dimensional `χ^λ` included.  So cyclicity cannot be what
    separates the channels.
  * **Multiplicativity** (`χ(xy) = χ(x)·χ(y)`) is what a one-dimensional channel
    has and a higher-dimensional one does not: a trace of a product is not a
    product of traces once the dimension exceeds one.

So the migration the deficit measures is from a **multiplicative** readout to a
merely **cyclic** one.  That is why the writhe stops controlling the valuation:
the writhe is exactly what a homomorphism can see, and once the maximizer is a
sum over standard-tableau paths there is no homomorphism left for the factor of
four to ride on.

`fourfold_of_multiplicative` makes the dependence explicit — ANY readout that is
multiplicative on concatenation and sends each letter to `s^{±1}` quadruples,
whatever channel it came from.  `sqWritheReadout` is the converse guard: a
readout that is cyclic but NOT multiplicative, on which the law fails outright
(it scales by sixteen, not four).  Without that guard the theorem above could be
read as though cyclicity sufficed.
-/

/-- The character is multiplicative on concatenation — an algebra map into a
commutative target.  This is the property, stated on its own. -/
theorem charOf_append (s : G) (v w : Word) :
    charOf s (v ++ w) = charOf s v * charOf s w := by
  induction v with
  | nil => simp [charOf]
  | cons g rest ih =>
      show (if 0 < g then s else s⁻¹) * charOf s (rest ++ w)
           = ((if 0 < g then s else s⁻¹) * charOf s rest) * charOf s w
      rw [ih, mul_assoc]

/-- Cabling a word of genuine braid letters produces genuine braid letters:
every entry of `cableBlock g` is nonzero when `g` is, since `2g` is even and
nonzero while `2g ± 1` are odd. -/
theorem cable_letters_ne_zero :
    ∀ w : Word, (∀ g ∈ w, g ≠ 0) → ∀ x ∈ cable w, x ≠ 0 := by
  intro w
  induction w with
  | nil => intro _ x hx; simp [cable] at hx
  | cons g rest ih =>
      intro hw x hx
      have hg : g ≠ 0 := hw g (by simp)
      have hrest : ∀ y ∈ rest, y ≠ 0 := fun y hy => hw y (by simp [hy])
      rcases List.mem_append.mp hx with h | h
      · simp only [cableBlock, List.mem_cons, List.not_mem_nil, or_false] at h
        rcases h with h | h | h | h <;> omega
      · exact ih hrest x h

/-- A multiplicative readout is determined by its values on single letters, so
it agrees with `charOf`. -/
theorem eq_charOf_of_multiplicative
    (f : Word → G) (hmul : ∀ v w : Word, f (v ++ w) = f v * f w) (hnil : f [] = 1)
    (s : G) (hlet : ∀ g : Int, g ≠ 0 → f [g] = if 0 < g then s else s⁻¹) :
    ∀ w : Word, (∀ g ∈ w, g ≠ 0) → f w = charOf s w := by
  intro w
  induction w with
  | nil => intro _; simpa [charOf] using hnil
  | cons g rest ih =>
      intro hw
      have hg : g ≠ 0 := hw g (by simp)
      have hrest : ∀ x ∈ rest, x ≠ 0 := fun x hx => hw x (by simp [hx])
      show f ([g] ++ rest) = charOf s (g :: rest)
      rw [hmul, hlet g hg, ih hrest]
      rfl

/-- **The property the law rides on.**  Any readout that is multiplicative on
concatenation and sends each letter to `s^{±1}` quadruples under cabling — the
channel it came from is irrelevant.  The hypothesis is MULTIPLICATIVITY; see
`sqWritheReadout_not_fourfold` for why cyclicity would not do. -/
theorem fourfold_of_multiplicative
    (f : Word → G) (hmul : ∀ v w : Word, f (v ++ w) = f v * f w) (hnil : f [] = 1)
    (s : G) (hlet : ∀ g : Int, g ≠ 0 → f [g] = if 0 < g then s else s⁻¹)
    {w : Word} (hw : ∀ g ∈ w, g ≠ 0) :
    f (cable w) = (f w) ^ (4 : Int) := by
  rw [eq_charOf_of_multiplicative f hmul hnil s hlet (cable w)
        (cable_letters_ne_zero w hw),
      eq_charOf_of_multiplicative f hmul hnil s hlet w hw]
  exact charOf_cable s hw

/-- A readout built from the SQUARE of the writhe.  It is cyclic — the writhe is
invariant under cyclic permutation, hence so is its square — but it is not
multiplicative. -/
def sqWritheReadout (s : G) (w : Word) : G := s ^ (writhe w * writhe w)

/-- `sqWritheReadout` is cyclic: it takes the same value on `v ++ w` and
`w ++ v`.  So it has the property every character shares. -/
theorem sqWritheReadout_cyclic (s : G) (v w : Word) :
    sqWritheReadout s (v ++ w) = sqWritheReadout s (w ++ v) := by
  simp only [sqWritheReadout, writhe_conj]
  ring_nf

/-- **The converse guard.**  Cyclicity is not enough: this cyclic readout scales
by SIXTEEN under cabling, not four, for any word of nonzero writhe.  So
`fourfold_of_multiplicative`'s hypothesis is load-bearing — the law is about
multiplicativity, and a merely-cyclic readout (which is what every
higher-dimensional character is) breaks it. -/
theorem sqWritheReadout_not_fourfold
    {w : Word} (hw : ∀ g ∈ w, g ≠ 0) (hW : writhe w ≠ 0) :
    writhe (cable w) * writhe (cable w) ≠ 4 * (writhe w * writhe w) := by
  rw [writhe_cable w hw]
  have : writhe w * writhe w > 0 := by
    rcases lt_trichotomy (writhe w) 0 with h | h | h
    · nlinarith
    · exact absurd h hW
    · nlinarith
  nlinarith

/-- Subtracting four times the word writhe from the cabled word writhe cancels to zero (`qou-f1rs`). -/
theorem writhe_cable_sub_eq_zero (w : Word) (hw : ∀ g ∈ w, g ≠ 0) :
    writhe (cable w) - 4 * writhe w = 0 := by
  rw [writhe_cable w hw, sub_self]

end QOU.BraidKnot
