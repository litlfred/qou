/-
Copyright (c) 2026 litlfred. All rights reserved.

# Closing a prose-only step: a scaling that stabilises the branch locus has finite order

Three W1 tranches (bean `qou-d8de`) reach the same conclusion through the same
**unformalised** step, and each says so in its own header:

* `QOU.Mass.DilationBranchLocusRigidity` (#6769) — *"The geometric step is stated here in
  prose and is not formalised: an automorphism `σ : Σ → Σ` covering `z ↦ l·z` … carries
  ramification points to ramification points and therefore permutes the finite branch
  locus `B`."*
* `QOU.Mass.PalindromicInvolutionLift` (#7185) — the same, plus *"the finiteness of
  `Stab(B)`, whose elementary proof is stated above … but which would need Möbius
  machinery Mathlib does not carry in usable form."*
* `QOU.Mass.QGaugeSpectralRigidity` (#7208) — the covering/gauge dictionary, likewise
  cited rather than proved.

The step splits into two halves that are not equally hard, and the corpus has been
carrying them as one:

1. **"an automorphism covering `z ↦ l·z` permutes `B`"** — genuinely geometric, about
   coverings and ramification. Still prose. Not touched here.
2. **"a map permuting a finite set of nonzero points has finite order"** — not geometric
   at all. It is pigeonhole, and for the case the corpus actually uses — `l` acting by
   *scaling* — it needs no Möbius machinery whatever.

This file proves half 2, in the generality the three tranches use it.

## What is proved

`exists_pow_eq_one_of_stabilizes` — if a finite set `S` of a field contains no zero and
is mapped into itself by `r ↦ l·r`, then `l^n = 1` for some `1 ≤ n ≤ S.card`.

The proof is three lines of content: `l^k·r ∈ S` for every `k` by induction, so the
`S.card + 1` values `l^0·r, …, l^{S.card}·r` land in a set of size `S.card`, so two
coincide, and cancelling the (nonzero) common factor leaves `l^n = 1`.

Note the hypothesis is *maps into*, not *permutes* — the weaker one, which is what a
covering argument actually hands you before you know injectivity. Finiteness upgrades it.

`not_stabilizes_of_one_lt_real` and `not_stabilizes_of_one_lt_complex` then give the
form the substrate needs: a real `l > 1` — the W1 shift is `l = q₀²` with
`q₀ ≈ 1.10998` — stabilises **no** finite set of nonzero points, in `ℝ` or in `ℂ`. The
branch locus `B` of the colour curve qualifies: it has six elements and `D(0) = 16 ≠ 0`,
so `0 ∉ B`.

## What this does NOT close

Half 1 above. The geometric step — that an automorphism of `Σ` covering a base map
permutes the branch locus — is still prose in all three tranches, and this file does not
address it. What changes is that the prose chain is now **one link long instead of two**:
everything downstream of "permutes `B`" is machine-checked.

Nor does this give `Stab(B) ↪ S₆` for a general Möbius map; it gives the scaling case,
which is the case every W1 tranche to date has needed. The general statement still rests
on the three-point rigidity of a Möbius map, argued in prose and measured exactly in
`w1_palindromic_involution_lifts_probe.py` T9a.

§7c: generic `[Field K]` for the core; `ℝ` and `ℂ` only in the two archimedean
corollaries, where an order comparison is genuinely required. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-08-w1-palindromic-involution-lifts-and-is-elliptic.md
-/
import Mathlib.Tactic
import Mathlib.Data.Complex.Basic

namespace QOU.Mass.BranchLocusFiniteOrder

variable {K : Type*} [Field K]

/-- Every `l`-orbit point of a member of `S` stays in `S`, by induction on the exponent.
Only `maps into` is assumed — not that `r ↦ l·r` is a bijection of `S`. -/
theorem pow_smul_mem (S : Finset K) (l : K) (hmap : ∀ r ∈ S, l * r ∈ S)
    {r : K} (hr : r ∈ S) : ∀ k : ℕ, l ^ k * r ∈ S := by
  intro k
  induction k with
  | zero => simpa using hr
  | succ k ih =>
      have h := hmap _ ih
      have hrw : l ^ (k + 1) * r = l * (l ^ k * r) := by ring
      rwa [hrw]

/-- **The pigeonhole step.** If a finite set `S` of a field contains no zero and is
mapped into itself by multiplication by `l`, then `l` has finite multiplicative order,
bounded by `S.card`.

This is the half of the W1 tranches' prose step that is not geometric. The `S.card + 1`
orbit points `l^0·r, …, l^{S.card}·r` all lie in `S`, which has `S.card` elements, so two
coincide; the common factor `l^i·r` is nonzero, so cancelling it gives `l^n = 1`. -/
theorem exists_pow_eq_one_of_stabilizes (S : Finset K) (hS : (0 : K) ∉ S) (l : K)
    (hmap : ∀ r ∈ S, l * r ∈ S) {r : K} (hr : r ∈ S) :
    ∃ n : ℕ, 0 < n ∧ n ≤ S.card ∧ l ^ n = 1 := by
  have hl0 : l ≠ 0 := by
    rintro rfl
    exact hS (by simpa using hmap r hr)
  have hr0 : r ≠ 0 := by rintro rfl; exact hS hr
  -- the orbit map lands in `S`, and its domain is one larger
  have hmaps : ∀ k ∈ Finset.range (S.card + 1), l ^ k * r ∈ S :=
    fun k _ => pow_smul_mem S l hmap hr k
  have hcard : S.card < (Finset.range (S.card + 1)).card := by
    simp
  obtain ⟨i, hi, j, hj, hij, heq⟩ :=
    Finset.exists_ne_map_eq_of_card_lt_of_maps_to hcard hmaps
  -- cancel the nonzero common factor `l^i * r`
  have key : ∀ a b : ℕ, 0 < b → l ^ a * r = l ^ (a + b) * r → l ^ b = 1 := by
    intro a b _ h
    have hne : l ^ a * r ≠ 0 := mul_ne_zero (pow_ne_zero _ hl0) hr0
    rw [pow_add] at h
    have hz : l ^ a * r * (l ^ b - 1) = 0 := by linear_combination -h
    rcases mul_eq_zero.mp hz with hz' | hz'
    · exact absurd hz' hne
    · linear_combination hz'
  simp only [Finset.mem_range] at hi hj
  rcases lt_or_gt_of_ne hij with hlt | hlt
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_lt hlt
    refine ⟨k + 1, Nat.succ_pos k, ?_, key i (k + 1) (Nat.succ_pos k) ?_⟩
    · omega
    · have hassoc : i + (k + 1) = j := by omega
      rw [hassoc]; exact heq
  · obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_lt hlt
    refine ⟨k + 1, Nat.succ_pos k, ?_, key j (k + 1) (Nat.succ_pos k) ?_⟩
    · omega
    · have hassoc : j + (k + 1) = i := by omega
      rw [hassoc]; exact heq.symm

/-- A real `l > 1` has no finite multiplicative order: `l^n > 1` for every `n ≥ 1`. -/
theorem one_lt_pow_of_one_lt {l : ℝ} (hl : 1 < l) : ∀ n : ℕ, 0 < n → 1 < l ^ n := by
  intro n hn
  induction n with
  | zero => omega
  | succ k ih =>
      rcases Nat.eq_zero_or_pos k with hk | hk
      · subst hk; simpa using hl
      · have hik := ih hk
        rw [pow_succ]
        nlinarith

/-- **The substrate form, over `ℝ`.** A real scaling `l > 1` stabilises no nonempty
finite set of nonzero reals. The W1 shift is `l = q₀²` with `q₀ ≈ 1.10998 > 1`. -/
theorem not_stabilizes_of_one_lt_real (S : Finset ℝ) (hS : (0 : ℝ) ∉ S)
    (hne : S.Nonempty) {l : ℝ} (hl : 1 < l) : ¬ (∀ r ∈ S, l * r ∈ S) := by
  intro hmap
  obtain ⟨r, hr⟩ := hne
  obtain ⟨n, hn, _, hpow⟩ := exists_pow_eq_one_of_stabilizes S hS l hmap hr
  have hgt := one_lt_pow_of_one_lt hl n hn
  rw [hpow] at hgt
  exact lt_irrefl 1 hgt

/-- **The substrate form, over `ℂ`** — which is where the branch locus actually lives,
since the six roots of the branch sextic `D` are complex. A real `l > 1`, viewed in `ℂ`,
stabilises no nonempty finite set of nonzero complex numbers.

Applied to `B = {D = 0}`: `D(0) = 16 ≠ 0` so `0 ∉ B`, `B` is nonempty, and `l = q₀² > 1`.
So **no dilation by the substrate shift can permute the branch locus** — which is the
conclusion #6769 and #7185 reach through the prose step, now machine-checked from
"permutes `B`" onward. -/
theorem not_stabilizes_of_one_lt_complex (S : Finset ℂ) (hS : (0 : ℂ) ∉ S)
    (hne : S.Nonempty) {l : ℝ} (hl : 1 < l) : ¬ (∀ r ∈ S, (l : ℂ) * r ∈ S) := by
  intro hmap
  obtain ⟨r, hr⟩ := hne
  obtain ⟨n, hn, _, hpow⟩ := exists_pow_eq_one_of_stabilizes S hS (l : ℂ) hmap hr
  -- `(l : ℂ)^n = 1` pushes back to `l^n = 1` in `ℝ` by injectivity of the coercion
  have hreal : (l : ℝ) ^ n = 1 := by
    have : ((l ^ n : ℝ) : ℂ) = ((1 : ℝ) : ℂ) := by push_cast; simpa using hpow
    exact_mod_cast this
  have hgt := one_lt_pow_of_one_lt hl n hn
  rw [hreal] at hgt
  exact lt_irrefl 1 hgt

end QOU.Mass.BranchLocusFiniteOrder
