import Mathlib.Tactic
import QOU.MassTheory.GammaGammaWordSelection
import QOU.Nuclear.GammaGammaSelectedDeltaVanishes

/-!
# What γγ production says about the up and down strands, and the down-strand self energy

Beans `qou-myts`, `qou-99qc`. Owner, 2026-11-27: *"what does γγ production say for u and d
quarks. track full tower"*. Fork F1 of `docs/audits/2026-11-27-nucleon-down-strand-self-energy.md`:
is the down strand a different strand object from the up strand (up = unknot strand, owner ruling
2026-11-20), so that a flavour self energy `θ_d ≠ θ_u` is possible?

## What is proved

**A. γγ production on every level of the tower (any number of strands).**

* `wordChar_gammaGamma`: let `a` be any invertible scalar and send `σᵢ ↦ a`, `σᵢ⁻¹ ↦ a⁻¹` for
  every `i`. This multiplicative character is `1` on every γγ-produced word, at every `n`.
  It covers both one-dimensional characters of every `H_n(q)` (`a = q`, `a = −q⁻¹`), the
  through-strand coefficient of the Jones decomposition `σ^{±1} = q^{±1}·1 − [2]·e`, and the
  Markov stabilisation factor (`a = z_D/…` is not multiplicative, see C). So **the one scalar that
  tells an up letter (`q`) from a down letter (`q⁻¹`) cancels on every γγ word**: γγ assigns the
  same value to u-type and d-type content and cannot tell them apart.
* `quark_letter_not_gammaGamma`: a single quark letter `σᵢ^{±1}`, up or down, is not γγ-produced
  (odd length), on any strand of any `H_n`.
* `gammaGamma_writhe_ne_nucleon`: γγ words have net orientation `0`; `uud` has `+1`, `udd` `−1`.

**B. The three strands of the γγ core `V³ = (σ₀σ₁⁻¹)³` are indistinguishable by orientation.**

* `core_pure`: the core returns every strand to its own position (a pure braid).
* `core_linking_zero`: all three pairwise linking numbers of its closure are `0` (Borromean).
* `core_strand_writhe_zero`: every strand takes part in signed crossings summing to `0`.
So the core carries no orientation datum on any single strand: it cannot mark one strand as u
(positive orientation, `def:up-quark`) and another as d (negative, `def:down-quark`).

**C. If a flavour sign is put on a strand by hand (outside γγ), the corpus offers two readings.**

* Through-strand reading (Jones/TL basis, `gg_quark_letters_tl`): u ↦ `q`, d ↦ `q⁻¹`, ratio `q²`
  (`through_ratio`). This is the existing `K`-weight cell (`NucleonSplitFullTower`), not new.
* Markov-stabilisation reading (the quark letter is the curl closing its own strand): the
  conditional expectation `E_{n+1→n}` sends `x·σ_n` to `z_D·x` and `x·σ_n⁻¹` to `z̄_D·x`,
  `z̄_D = z_D − (q − q⁻¹) = 1/(q(q²+1))` (`zbarD_eq`), and `z_D = q⁴·z̄_D` (`curl_ratio`).
  The bar involution swaps them (`zD_bar`), so u ↔ d is the bar involution here too.
* `vertex_curls_bar_even`: a γγ vertex read as two stabilisations carries one curl of each sign,
  `z_D·z̄_D = q²/(q²+1)²`, which is bar-even — flavour-blind.
* `curl_split`, `curl_split_eq_twice_through` (in `QOU.Transcendental.Nuclear.NucleonDownQuarkStrandGibbs`):
  the Gibbs map `E·log(τ_d-curl ratio)` gives `4E·log q` for the curl reading, twice the
  through-strand cell `2E·log q`.

## What is NOT claimed

* That either reading in C is the corpus's. Neither is forced: γγ (A, B) does not place a flavour
  sign on any strand, and `def:down-quark` makes the down quark the same unknot as the up quark with
  the opposite crossing orientation, not a different object. Which reading, if any, is an owner call.
* No numerical value enters. Generic `[Field R]` throughout; the `Real.log` statements live
  under `QOU/Transcendental/` (§7c, transcendental boundary).

-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-down-quark-strand.md
-- Ref: [jones1987] https://doi.org/10.2307/1971403 §5 (Markov trace, `tr(xσ_n^{±1})`)
-/

namespace QOU.Nuclear.NucleonDownQuarkStrand

open QOU.Mass.GammaGammaWordSelection

/-! ## A. γγ production, every level of the tower -/

section A

variable {R : Type*} [Field R]

/-- Value of one letter under the character `σᵢ ↦ a`, `σᵢ⁻¹ ↦ a⁻¹` (same `a` for every `i`). -/
def letterChar (a : R) (c : Crossing) : R := if c.pos then a else a⁻¹

/-- The multiplicative extension to words. -/
def wordChar (a : R) (w : Word) : R := (w.map (letterChar a)).prod

theorem wordChar_append (a : R) (u v : Word) :
    wordChar a (u ++ v) = wordChar a u * wordChar a v := by
  simp [wordChar, List.map_append, List.prod_append]

theorem wordChar_vertex (a : R) (ha : a ≠ 0) (i : ℕ) : wordChar a (vertex i) = 1 := by
  simp [wordChar, vertex, letterChar, mul_inv_cancel₀ ha]

/-- **γγ cancels the u/d scalar on every `H_n`.** -/
theorem wordChar_gammaGamma (a : R) (ha : a ≠ 0) {w : Word} (h : GammaGammaWord w) :
    wordChar a w = 1 := by
  induction h with
  | nil => simp [wordChar]
  | cons i _ ih => rw [wordChar_append, wordChar_vertex a ha, ih, one_mul]

/-- An up letter has value `a`, a down letter `a⁻¹`; they differ unless `a² = 1`. -/
theorem up_down_letter_values (a : R) (i : ℕ) :
    wordChar a [⟨i, true⟩] = a ∧ wordChar a [⟨i, false⟩] = a⁻¹ := by
  simp [wordChar, letterChar]

/-- **A single quark letter, up or down, is not γγ-produced**, on any generator. -/
theorem quark_letter_not_gammaGamma (i : ℕ) (b : Bool) : ¬ GammaGammaWord [⟨i, b⟩] :=
  QOU.QBeta.GammaGammaDelta.not_gammaGamma_of_odd_length (by simp)

/-- **Net orientation.** Reading u as orientation `+1` and d as `−1` (`def:up-quark`,
`def:down-quark`), the proton `uud` has net `+1` and the neutron `udd` net `−1`. Every γγ word has
writhe `0` (`writhe_eq_zero`), so no γγ word carries either nucleon's net orientation. -/
theorem gammaGamma_writhe_ne_nucleon {w : Word} (h : GammaGammaWord w) :
    writhe w ≠ (1 + 1 + (-1) : ℤ) ∧ writhe w ≠ (1 + (-1) + (-1) : ℤ) := by
  rw [writhe_eq_zero h]; decide

end A

/-! ## B. Strands of the γγ core -/

section B

/-- Swap the strands at positions `i`, `i+1`. -/
def swapAt (st : List ℕ) (i : ℕ) : List ℕ :=
  (st.set i (st.getD (i + 1) 0)).set (i + 1) (st.getD i 0)

/-- Final strand positions after a word. -/
def finalPos : List ℕ → Word → List ℕ
  | st, [] => st
  | st, c :: w => finalPos (swapAt st c.gen) w

/-- Signed crossings between strands `a` and `b` (the linking number when the braid is pure). -/
def link : List ℕ → Word → ℕ → ℕ → ℤ
  | _, [], _, _ => 0
  | st, c :: w, a, b =>
      (if (st.getD c.gen 0 = a ∧ st.getD (c.gen + 1) 0 = b) ∨
          (st.getD c.gen 0 = b ∧ st.getD (c.gen + 1) 0 = a) then sign c else 0)
        + link (swapAt st c.gen) w a b

/-- Signed crossings in which strand `s` takes part. -/
def involve : List ℕ → Word → ℕ → ℤ
  | _, [], _ => 0
  | st, c :: w, s =>
      (if st.getD c.gen 0 = s ∨ st.getD (c.gen + 1) 0 = s then sign c else 0)
        + involve (swapAt st c.gen) w s

/-- The γγ core `V³ = (σ₀σ₁⁻¹)³`. -/
def core : Word := vertex 0 ++ vertex 0 ++ vertex 0

theorem core_isGammaGamma : GammaGammaWord core := by
  unfold core
  rw [List.append_assoc]
  exact .cons 0 (.cons 0 (.cons 0 .nil))

theorem core_pure : finalPos [0, 1, 2] core = [0, 1, 2] := by decide

theorem core_linking_zero :
    link [0, 1, 2] core 0 1 = 0 ∧ link [0, 1, 2] core 0 2 = 0 ∧
      link [0, 1, 2] core 1 2 = 0 := by decide

theorem core_strand_writhe_zero :
    involve [0, 1, 2] core 0 = 0 ∧ involve [0, 1, 2] core 1 = 0 ∧
      involve [0, 1, 2] core 2 = 0 := by decide

end B

/-! ## C. Two readings of a hand-placed flavour sign -/

section C

variable {R : Type*} [Field R]

/-- Convention-D Markov parameter. -/
def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- Value of the conditional expectation on a negative stabilisation: `σ⁻¹ = σ − (q − q⁻¹)`. -/
def zbarD (q : R) : R := zD q - (q - q⁻¹)

theorem zbarD_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zbarD q = 1 / (q * (q ^ 2 + 1)) := by
  unfold zbarD zD
  field_simp
  ring

theorem curl_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : zD q = q ^ 4 * zbarD q := by
  rw [zbarD_eq q hq hq2]; unfold zD; field_simp

/-- The bar involution `q ↦ q⁻¹` swaps the two curl factors: u ↔ d is bar here. -/
theorem zD_bar (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : zD q⁻¹ = zbarD q := by
  rw [zbarD_eq q hq hq2]; unfold zD
  have : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
  rw [this]; field_simp

/-- A γγ vertex as two stabilisations: one curl of each sign. -/
theorem vertex_curls (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zD q * zbarD q = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  rw [zbarD_eq q hq hq2]; unfold zD; field_simp

/-- …and that product is bar-even (flavour-blind). -/
theorem vertex_curls_bar_even (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ * zbarD q⁻¹ = zD q * zbarD q := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hqi2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    have : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
    rw [this]; exact div_ne_zero hq2 (pow_ne_zero 2 hq)
  rw [vertex_curls q⁻¹ hqi hqi2, vertex_curls q hq hq2]
  have hq2' : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  rw [div_eq_div_iff (pow_ne_zero 2 hqi2) hq2']
  field_simp
  ring

/-- Through-strand reading: u ↦ `q`, d ↦ `q⁻¹`, ratio `q²`. -/
theorem through_ratio (q : R) (hq : q ≠ 0) : q = q ^ 2 * q⁻¹ := by field_simp

end C

end QOU.Nuclear.NucleonDownQuarkStrand
