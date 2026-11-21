import Mathlib.Tactic
import Mathlib.Algebra.DualNumber
import QOU.MassTheory.PairwiseChainLeadingOrder

/-!
# The leading `ℏ_q` coefficient of the trace difference, derived

Bean `qou-pdg9` (successor to `qou-zrx2`). Probe:
`computations/probes/c1_leading_coefficient_derived_probe.py`.

## What this certifies

`PairwiseChainLeadingOrder` carries the six leading coefficients
`c₁ = lim (Δtr − c₀(A))/ℏ_q` of `Δtr = tr_M(W_free) − tr_M(W_atom)` as
**definitions** — Richardson measurements matched to rationals. This file
records the derivation that turns them into values that *follow* from the
braid words, by the same route that derived the classical floor `c₀`
(`ClassicalTraceFloor`):

    d tr_M / dε |₀  =  2^{−n} · Σ_ℓ w_ℓ · 2^{c(σ^{(ℓ)})}          [★]

with `q = 1 + ε`, `w_ℓ = +1` for a `σ` letter, `−1` for `σ⁻¹`, `0` for either
averaged letter, and `σ^{(ℓ)}` the permutation of the word with letter `ℓ`
deleted. Reading the per-letter data collapses it further to

    c₁(Z,N) = (3Z − 2N)·(2^{−A−1} − 2^{−2A}) − 4·(I_pp − I_nn)·2^{−2A}

where `3 = 6/2` and `−2 = −4/2` are the Borromean proton / neutron half
deletion sums `(S_p, S_n)/2` (superseded grouped: `21 = 42/2` and `16 = 32/2`),
and `I_pp = Z−1`, `I_nn = N−1` (truncated at `0`) count the same-species
interfaces of the chain.

## The four steps of [★], and what is formal here

1. **The generator's first-order term is `1 + Y` with `Y` anticommuting with
   `s`.** From `σ² = hσ + 1`, `h = 2ε + O(ε²)`, `s² = 1`. —
   `hecke_first_order_anticommutes` proves the ring identity; `hecke_relation_snd`
   extracts the first-order relation from the Hecke relation in the dual
   numbers `R[ε]/(ε²)`; `h_dual` shows `h = 2ε` there.
2. **`Tr(Y·P) = 0` for every permutation `P`.** A spin-flip symmetry argument on
   `(ℂ²)^{⊗n}`. **Not formalised** — it needs the tensor representation, which
   needs Schur–Weyl, which Mathlib lacks. Stated in the probe.
3. **The `K′` term cancels the normaliser's derivative.** Arithmetic; both are
   `n·2^{c(σ)}`. Folded into [★] as stated.
4. **Each letter's own first-order term is the scalar `1 + d′(0)`,** giving
   `w ∈ {+1, −1, 0, 0}`; the colour weight `δ = O(ε³)` is invisible.
   `letter_weight` records the four values.

What IS proved below, unconditionally: the ring identity of step 1 (in any
ring, and via the dual numbers); that any [★]-shaped sum is a dyadic rational
with denominator dividing `2^n`; that the closed form evaluates to the six
recorded rationals; and — from the actual letter data of the twelve words,
entered as explicit lists — that [★] reproduces every one of them. So the six
definitions in `PairwiseChainLeadingOrder` are now **derived conditional on
steps 2 and 4** (Schur–Weyl plus the trace-invisibility of `Y`), which is
exactly the hypothesis split `ClassicalTraceFloor` uses for `c₀`.

## ⚠ What the closed form does NOT license

It is a statement about the *signed* first-order coefficient of the
**difference** channel at the chain's own letter census. It says nothing
about the log channel, nothing about the scale (`qou-59j5`), and nothing
past first order — the exact `c₂` values are in the witness and are NOT
closed-form here.

-- Ref: [leitner2026] bean qou-pdg9; computations/probes/c1_leading_coefficient_derived_probe.py
-/

namespace QOU.MassTheory

open TrivSqZeroExt

/-! ### 1. First-order structure of a Hecke generator -/

/-- **Step 1, ring form.** If `sX + Xs = s + s`, then `Y := X − 1` anticommutes
with `s`. Holds in any ring, commutative or not — and, as the linter pointed
out, needs no `s² = 1`: that hypothesis is used only to *derive* the relation
(`hecke_relation_snd`), not to read it. -/
theorem hecke_first_order_anticommutes {R : Type*} [Ring R] (s X : R)
    (h : s * X + X * s = s + s) :
    s * (X - 1) = -((X - 1) * s) := by
  have key : s * (X - 1) + (X - 1) * s = 0 := by
    have e : s * (X - 1) + (X - 1) * s = (s * X + X * s) - (s + s) := by noncomm_ring
    rw [e, h, sub_self]
  exact eq_neg_of_add_eq_zero_left key

/-- **Step 1, where the relation comes from.** In the dual numbers `R[ε]/(ε²)`
the Hecke relation `σ² = hσ + 1` for `σ = s + εX` with `h = 2ε` and `s² = 1`
forces exactly `sX + Xs = s + s` on the `ε`-coefficient. -/
theorem hecke_relation_snd {R : Type*} [Ring R] (s X : R)
    (hσ : (inl s + inr X : DualNumber R) * (inl s + inr X)
          = (inr (2 : R) : DualNumber R) * (inl s + inr X) + 1) :
    s * X + X * s = s + s := by
  have h2 := congrArg TrivSqZeroExt.snd hσ
  simp only [snd_mul, snd_add, fst_add, fst_inl, snd_inl, fst_inr, snd_inr,
    snd_one, smul_eq_mul, MulOpposite.smul_eq_mul_unop, MulOpposite.unop_op,
    zero_mul, add_zero, zero_add] at h2
  rw [h2, two_mul]

/-- `h = q − q⁻¹` at `q = 1 + ε` is `2ε` to first order: `(1+ε)(1−ε) = 1` in the
dual numbers, so `q⁻¹ = 1 − ε` and `h = 2ε`. -/
theorem h_dual {R : Type*} [CommRing R] :
    ((1 : DualNumber R) + DualNumber.eps) * (1 - DualNumber.eps) = 1 ∧
    ((1 : DualNumber R) + DualNumber.eps) - (1 - DualNumber.eps) = 2 * DualNumber.eps := by
  constructor
  · have : (DualNumber.eps : DualNumber R) * DualNumber.eps = 0 := DualNumber.eps_mul_eps
    linear_combination (-1 : DualNumber R) * this
  · ring

/-- **Step 4.** The first-order weight `1 + d′(0)` of each letter type, from
`d ∈ {0, −h, −h/2, −h(½ − δ/4)}` with `h′(0) = 2` and `δ = O(ε³)`. -/
def letterWeight : Fin 4 → ℤ
  | 0 => 1      -- σ            d = 0
  | 1 => -1     -- σ⁻¹          d = −h
  | 2 => 0      -- averaged     d = −h/2
  | 3 => 0      -- averaged, colour-weighted   d = −h(½ − δ/4), δ = O(ε³)

theorem letterWeight_values :
    letterWeight 0 = 1 ∧ letterWeight 1 = -1 ∧ letterWeight 2 = 0 ∧ letterWeight 3 = 0 := by
  decide

/-! ### 2. The star sum [★] and its arithmetic -/

/-- `2^{−n} Σ_ℓ w_ℓ 2^{c_ℓ}` over letter data `(w_ℓ, c_ℓ)`. -/
def starSum (n : ℕ) (L : List (ℤ × ℕ)) : ℚ :=
  (L.map fun p => (p.1 : ℚ) * (2 : ℚ) ^ p.2).sum / (2 : ℚ) ^ n

theorem starSum_numerator_int (L : List (ℤ × ℕ)) :
    ∃ m : ℤ, (L.map fun p => (p.1 : ℚ) * (2 : ℚ) ^ p.2).sum = m := by
  induction L with
  | nil => exact ⟨0, by simp⟩
  | cons p L ih =>
    obtain ⟨m, hm⟩ := ih
    refine ⟨p.1 * 2 ^ p.2 + m, ?_⟩
    rw [List.map_cons, List.sum_cons, hm]
    push_cast
    ring

/-- Every [★]-shaped quantity is dyadic with denominator dividing `2^n` — the
same shape as the floor `c₀ = 2^{c−n}`, and the reason every measured `c₁` was
a dyadic rational. -/
theorem starSum_dyadic (n : ℕ) (L : List (ℤ × ℕ)) :
    ∃ m : ℤ, starSum n L * (2 : ℚ) ^ n = m := by
  obtain ⟨m, hm⟩ := starSum_numerator_int L
  refine ⟨m, ?_⟩
  unfold starSum
  rw [div_mul_cancel₀ _ (by positivity), hm]

/-! ### 3. The closed form -/

/-! The closed form itself lives in `PairwiseChainLeadingOrder` as
`c1Closed (a b : ℚ) (Z N : ℕ)`; at the Borromean letter weights it is
`c1Closed 3 (-2)`, and `c1_defs_eq_closed_borromean` there pins it to the six
values. This file used to carry a second, specialised `c1Closed (Z N : ℕ)` — a
**duplicate declaration in the same namespace**, and the weaker of the two — so
it is dropped and everything below uses the parameterised one.

⚠ Note for anyone reading an older revision: the per-nucleon coefficients read
`(21Z + 16N)` until 2026-09-06. Those are the **pre-2026-09-05 (`grouped`) atom
word's**. Owner ruling `qou-hu1f` reordered each nucleon's confinement core and
they became `(3Z − 2N)` — the neutron's changes **sign**. Both are
`(S_p, S_n)/2` for that word's per-nucleon deletion sums, `(42, 32)` grouped and
`(6, −4)` canonical, and `PairwiseChainLeadingOrder.c1_grouped_values_eq_closed`
keeps the superseded column as a check. The interface term `−4(I_pp − I_nn)` is
unchanged, and is unchangeable by an intra-nucleon reordering: interfaces are
single letters outside the nucleon blocks. See
`computations/probes/canonical_c1_closed_form_probe.py` (44 isotopes, both halves
verified separately) and
`docs/audits/2026-09-06-c1-is-stale-on-the-reordered-atom-word.md`. -/

/-- The `pp` and `nn` bonds differ from the `pn` bond only through the
interface term: `c₁(pp) − c₁(pn) = (5·(1/8 − 1/16) − 4/16)` and
`c₁(nn) − c₁(pn) = −5·(1/8 − 1/16) + 4/16`. In particular
`c₁(pp) + c₁(nn) = 2·c₁(pn)` — the interface contributions cancel in the
symmetric combination and the census terms average. -/
theorem c1Closed_bond_symmetry : c1Closed 3 (-2) 2 0 + c1Closed 3 (-2) 0 2 = 2 * c1Closed 3 (-2) 1 1 := by
  norm_num [c1Closed]

/-- At fixed `A`, `c₁` is affine in `Z` with slope `5(2^{−A−1} − 2^{−2A}) − 8·2^{−2A}`
while both species stay present (`1 ≤ Z`, `2 ≤ N`, so that after the move
`N − 1 ≥ 1`): moving one neutron to a proton adds `5` to the census and shifts
`I_pp − I_nn` by `2`. (At `N = 1` the truncated `I_nn` does not move and the
shift is `1`; that boundary case is excluded here.) -/
theorem c1Closed_step (Z N : ℕ) (hZ : 1 ≤ Z) (hN : 2 ≤ N) :
    c1Closed 3 (-2) (Z + 1) (N - 1) - c1Closed 3 (-2) Z N
      = 5 * ((2⁻¹ : ℚ) ^ (Z + N + 1) - (2⁻¹ : ℚ) ^ (2 * (Z + N)))
        - 8 * (2⁻¹ : ℚ) ^ (2 * (Z + N)) := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 2 := ⟨N - 2, by omega⟩
  obtain ⟨z, rfl⟩ : ∃ z, Z = z + 1 := ⟨Z - 1, by omega⟩
  unfold c1Closed
  have e1 : n + 2 - 1 = n + 1 := by omega
  have e2 : z + 1 + 1 - 1 = z + 1 := by omega
  have e3 : n + 1 - 1 = n := by omega
  have e4 : z + 1 - 1 = z := by omega
  simp only [e1, e2, e3, e4]
  push_cast
  ring

/-! ### 4. The twelve words, letter by letter

Each list is the `(w_ℓ, c(σ^{(ℓ)}))` data of the non-averaged letters of one
word, read off the canonical crossings by `atom_canonical_crossings` and a
transposition product with that letter deleted (probe, Part B). Every deleted
`σ` raises the cycle count by one and every deleted `σ⁻¹` lowers it — visible
in the lists as `(1, c+1)` and `(−1, c−1)` against `c_free = 2A`,
`c_atom = A+1`, with the single `nn`-interface `σ⁻¹` the one `(−1, c+1)`. -/

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the pp free word, n = 6: [★] = 3/4. -/
def letters_ppFree : List (ℤ × ℕ) := [(1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3)]
theorem star_ppFree : starSum 6 letters_ppFree = 3 / 4 := by
  simp only [starSum, letters_ppFree, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the pp atom word, n = 6: [★] = 5/8. -/
def letters_ppAtom : List (ℤ × ℕ) := [(1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2), (1, 4), (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2)]
theorem star_ppAtom : starSum 6 letters_ppAtom = 5 / 8 := by
  simp only [starSum, letters_ppAtom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the pn free word, n = 6: [★] = 1/8. -/
def letters_pnFree : List (ℤ × ℕ) := [(1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3)]
theorem star_pnFree : starSum 6 letters_pnFree = 1 / 8 := by
  simp only [starSum, letters_pnFree, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the pn atom word, n = 6: [★] = 1/16. -/
def letters_pnAtom : List (ℤ × ℕ) := [(1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2), (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2)]
theorem star_pnAtom : starSum 6 letters_pnAtom = 1 / 16 := by
  simp only [starSum, letters_pnAtom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the nn free word, n = 6: [★] = -1/2. -/
def letters_nnFree : List (ℤ × ℕ) := [(1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3)]
theorem star_nnFree : starSum 6 letters_nnFree = -1 / 2 := by
  simp only [starSum, letters_nnFree, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the nn atom word, n = 6: [★] = -1/2. -/
def letters_nnAtom : List (ℤ × ℕ) := [(1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2), (-1, 4), (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2)]
theorem star_nnAtom : starSum 6 letters_nnAtom = -1 / 2 := by
  simp only [starSum, letters_nnAtom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the T free word, n = 9: [★] = -1/16. -/
def letters_TFree : List (ℤ × ℕ) := [(1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (1, 5), (1, 5), (1, 5), (1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (-1, 7), (1, 5), (1, 5), (1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (-1, 7), (1, 5), (1, 5)]
theorem star_TFree : starSum 9 letters_TFree = -1 / 16 := by
  simp only [starSum, letters_TFree, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the T atom word, n = 9: [★] = -5/64. -/
def letters_TAtom : List (ℤ × ℕ) := [(1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3), (-1, 5), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3)]
theorem star_TAtom : starSum 9 letters_TAtom = -5 / 64 := by
  simp only [starSum, letters_TAtom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the 3He free word, n = 9: [★] = 1/4. -/
def letters_He3Free : List (ℤ × ℕ) := [(1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (1, 5), (1, 5), (1, 5), (1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (1, 5), (1, 5), (1, 5), (1, 5), (-1, 5), (1, 7), (-1, 5), (1, 5), (-1, 7), (-1, 7), (1, 5), (1, 5)]
theorem star_He3Free : starSum 9 letters_He3Free = 1 / 4 := by
  simp only [starSum, letters_He3Free, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the 3He atom word, n = 9: [★] = 1/8. -/
def letters_He3Atom : List (ℤ × ℕ) := [(1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3), (1, 5), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3), (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3)]
theorem star_He3Atom : starSum 9 letters_He3Atom = 1 / 8 := by
  simp only [starSum, letters_He3Atom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the 4He free word, n = 12: [★] = 1/16. -/
def letters_He4Free : List (ℤ × ℕ) := [(1, 7), (-1, 7), (1, 9), (-1, 7), (1, 7), (-1, 9), (1, 7), (1, 7), (1, 7), (1, 7), (-1, 7), (1, 9), (-1, 7), (1, 7), (-1, 9), (1, 7), (1, 7), (1, 7), (1, 7), (-1, 7), (1, 9), (-1, 7), (1, 7), (-1, 9), (-1, 9), (1, 7), (1, 7), (1, 7), (-1, 7), (1, 9), (-1, 7), (1, 7), (-1, 9), (-1, 9), (1, 7), (1, 7)]
theorem star_He4Free : starSum 12 letters_He4Free = 1 / 16 := by
  simp only [starSum, letters_He4Free, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num

/-- Letter data `(w, c(σ⁽ˡ⁾))` of the 4He atom word, n = 12: [★] = 1/128. -/
def letters_He4Atom : List (ℤ × ℕ) := [(1, 4), (-1, 4), (1, 6), (-1, 4), (1, 4), (-1, 6), (1, 4), (1, 4), (1, 4), (1, 6), (1, 4), (-1, 4), (1, 6), (-1, 4), (1, 4), (-1, 6), (1, 4), (1, 4), (1, 4), (1, 4), (-1, 4), (1, 6), (-1, 4), (1, 4), (-1, 6), (-1, 6), (1, 4), (1, 4), (-1, 6), (1, 4), (-1, 4), (1, 6), (-1, 4), (1, 4), (-1, 6), (-1, 6), (1, 4), (1, 4)]
theorem star_He4Atom : starSum 12 letters_He4Atom = 1 / 128 := by
  simp only [starSum, letters_He4Atom, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]; norm_num


/-- [★] reproduces all six recorded coefficients from the letter data alone:
`c₁ = starSum(free) − starSum(atom)`. -/
theorem c1_from_letters :
    c1_pp = starSum 6 letters_ppFree - starSum 6 letters_ppAtom ∧
    c1_pn = starSum 6 letters_pnFree - starSum 6 letters_pnAtom ∧
    c1_nn = starSum 6 letters_nnFree - starSum 6 letters_nnAtom ∧
    c1_T = starSum 9 letters_TFree - starSum 9 letters_TAtom ∧
    c1_He3 = starSum 9 letters_He3Free - starSum 9 letters_He3Atom ∧
    c1_He4 = starSum 12 letters_He4Free - starSum 12 letters_He4Atom := by
  rw [star_ppFree, star_ppAtom, star_pnFree, star_pnAtom, star_nnFree, star_nnAtom,
    star_TFree, star_TAtom, star_He3Free, star_He3Atom, star_He4Free, star_He4Atom]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [c1_pp, c1_pn, c1_nn, c1_T, c1_He3, c1_He4]

end QOU.MassTheory
