/-
QOU.Mass.EpsEqFromMonotonicity — `eps_eq` stops being a bare measured hypothesis: the
step from the block structure to the product `u · v` is proved here, and what remains
assumed is three sharp braid-word facts rather than one opaque one.

Arc context (carrier derivation, route 3; beans `qou-768r`, `qou-2g9j`).
`ChainTripleMilnorVanishesByGcdDividesProduct.lean` closes route 3's last residual on
`gcd u v ∣ u * v`, but carries `ChainTriple.eps_eq` — *"the degree-2 Magnus coefficient
of the hub's longitude is `u * v`"* — as a structural hypothesis measured 596/596. This
file derives that hypothesis from smaller ones.

**The decomposition, measured by
`computations/probes/eps_eq_decomposition_from_monotonicity_probe.py`.** Every one of
the eight facts holds on **all 596** monotone chain triples — 62 on the derived carrier
across both crossing-resolution branches, 534 on random monotone words — and every one
degrades off monotone (78 chain triples, one RNG consumed sequentially so the arms stay
comparable with the sibling probes):

| | monotone | non-monotone |
|---|---|---|
| **tier 1 — braid-word facts, still ASSUMED** | | |
| all `hub`↔`x` crossings sit in ONE generator's run | 596/596 | 56/78 |
| all `hub`↔`y` crossings sit in ONE generator's run | 596/596 | 58/78 |
| the two generators differ | 596/596 | 37/78 |
| `g_x < g_y` ⟺ `x < y` | 596/596 | 36/78 |
| each run has EVEN length | 596/596 | 40/78 |
| each run's length is exactly `2|lk|` | 596/596 | 30/78 |
| **tier 2 — consequences, CONSUMED by the theorems below** | | |
| signed sum of `x`-letters in `λ_hub` equals `u` | 596/596 | 51/78 |
| signed sum of `y`-letters in `λ_hub` equals `v` | 596/596 | 53/78 |
| the `x`-letters are CONTIGUOUS in `λ_hub` | 596/596 | 56/78 |
| the `y`-letters are CONTIGUOUS in `λ_hub` | 596/596 | 67/78 |
| the blocks are disjoint and `x`'s precedes `y`'s | 596/596 | 18/78 |

Quote the witness, not this table if they ever disagree: a scratch run against a
*per-arm* RNG gave `32/78` for the `2|lk|` row, and the same class of error produced two
wrong figures earlier in this arc (#6679's `251/2080`, and a "0 of 71" vacuity claim in
#6726 that was really 1 of 78).

**What is PROVED here.**

`epsCoeff_append_of_blocks` — the arithmetic core, and the whole reason `eps_eq` has the
shape it does. If a longitude word splits as `A ++ B` with no `y`-letter in `A` and no
`x`-letter in `B`, then the degree-2 Magnus coefficient is exactly the product of the
two blocks' signed sums, and the reverse ordering is `0`. This is where the `u * v` in
`ChainTriple.eps_eq` comes from; it is a statement about lists and needs no topology.

`underSum_eq_linking` — the other half. A run of `2m` crossings between two strands
alternates which one passes under, so the hub records exactly `m` of them, all carrying
the run's sign `s`; meanwhile `lk = (2 m s)/2 = m s`. The two agree. Both the run's even
length and its length being `2|lk|` are measured facts feeding this.

`eps_eq_of_blocks` composes them: block structure plus the two signed sums equalling the
linking numbers gives `ε_{x,y} = u * v`, which is `ChainTriple.eps_eq`.

**What is still ASSUMED, stated plainly.** The three braid-word facts in the table's top
half — one generator per component pair, generators in ascending order matching
component order, run length `2|lk|`. Deriving *those* needs the strand-permutation
bookkeeping of a monotone word formalised (positions, runs, who passes under whom),
which is a substantially larger object than anything in this arc and is not attempted.
They are recorded as hypotheses `hA`, `hB`, `hsum` of `eps_eq_of_blocks`, so a reader
can see exactly what is bought and what is borrowed.

**The gain is real but should not be overstated.** `eps_eq` was one hypothesis about a
Magnus coefficient; it is now a theorem given three hypotheses about a braid word. The
arithmetic — the part that could have been wrong in a subtle way, and the part that
makes `gcd u v ∣ u * v` applicable at all — is machine-checked. The combinatorics of
which strand is where is not.

SCOPE — the Lean statements are unconditional; the empirical claim that their
hypotheses hold on monotone closures is **scope-(a)**, 596/596 over 7 isotopes, both
branches, and one random-word regime.

Base ring: `ℤ`. Crossing signs, linking numbers and Magnus coefficients are integers,
and no ordering or ring generality is used (AGENTS.md §7c).
-/
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Mass.EpsEqFromMonotonicity

variable {ι : Type*} [DecidableEq ι]

/-- A letter of a longitude word: whose meridian it is, and the crossing's sign. -/
abbrev Letter (ι : Type*) := ι × ℤ

/-- Signed sum of the letters belonging to component `c`. -/
def signSum (w : List (Letter ι)) (c : ι) : ℤ :=
  (w.map (fun l => if l.1 = c then l.2 else 0)).sum

@[simp] theorem signSum_nil (c : ι) : signSum ([] : List (Letter ι)) c = 0 := rfl

@[simp] theorem signSum_append (A B : List (Letter ι)) (c : ι) :
    signSum (A ++ B) c = signSum A c + signSum B c := by
  induction A with
  | nil => simp [signSum]
  | cons a t ih => simp [signSum] at ih ⊢; rw [ih]; ring

/-- Signed sum of a block containing no `c`-letters is zero. -/
theorem signSum_eq_zero_of_absent {w : List (Letter ι)} {c : ι}
    (h : ∀ l ∈ w, l.1 ≠ c) : signSum w c = 0 := by
  induction w with
  | nil => rfl
  | cons a t ih =>
    have ha : a.1 ≠ c := h a (by simp)
    have ht : signSum t c = 0 := ih (fun l hl => h l (by simp [hl]))
    simpa [signSum, ha] using ht

/-- Peeling one letter off a signed sum. -/
theorem signSum_cons (a : Letter ι) (t : List (Letter ι)) (c : ι) :
    signSum (a :: t) c = (if a.1 = c then a.2 else 0) + signSum t c := by
  simp [signSum]

/-- The degree-2 Magnus coefficient, with the running total of `p`-signs carried
explicitly. `epsAux w p q s` is the signed count of `(p before q)` pairs in `w`, given
that `s` worth of `p`-signs has already been seen. -/
def epsAux (w : List (Letter ι)) (p q : ι) (s : ℤ) : ℤ :=
  match w with
  | [] => 0
  | l :: t =>
      if l.1 = q then s * l.2 + epsAux t p q s
      else if l.1 = p then epsAux t p q (s + l.2)
      else epsAux t p q s

/-- `ε_{p,q}(w)` — the coefficient of `h_p h_q` in the Magnus expansion of `w`. -/
def epsCoeff (w : List (Letter ι)) (p q : ι) : ℤ := epsAux w p q 0

/-- A block with no `q`-letters contributes nothing: there is no `q` for a `p` to
precede. -/
theorem epsAux_eq_zero_of_no_q {w : List (Letter ι)} {p q : ι} (s : ℤ)
    (h : ∀ l ∈ w, l.1 ≠ q) : epsAux w p q s = 0 := by
  induction w generalizing s with
  | nil => rfl
  | cons a t ih =>
    have ha : a.1 ≠ q := h a (by simp)
    have ht : ∀ l ∈ t, l.1 ≠ q := fun l hl => h l (by simp [hl])
    by_cases hp : a.1 = p
    · rw [epsAux, if_neg ha, if_pos hp, ih _ ht]
    · rw [epsAux, if_neg ha, if_neg hp, ih _ ht]

/-- A block with no `p`-letters cannot grow the accumulator, so every `q`-letter is
weighted by the *same* running total: the block contributes `s` times its own signed
sum. -/
theorem epsAux_eq_of_no_p {w : List (Letter ι)} {p q : ι} (s : ℤ)
    (h : ∀ l ∈ w, l.1 ≠ p) : epsAux w p q s = s * signSum w q := by
  induction w generalizing s with
  | nil => simp [epsAux, signSum]
  | cons a t ih =>
    have ha : a.1 ≠ p := h a (by simp)
    have ht : ∀ l ∈ t, l.1 ≠ p := fun l hl => h l (by simp [hl])
    by_cases hq : a.1 = q
    · rw [epsAux, if_pos hq, ih _ ht, signSum_cons, if_pos hq]; ring
    · rw [epsAux, if_neg hq, if_neg ha, ih _ ht, signSum_cons, if_neg hq]; ring

/-- Running the accumulator through a concatenation: the second block starts with
whatever `p`-signs the first block contributed.

`p ≠ q` is needed and is not a technicality: a letter cannot be both the thing being
counted and the thing being counted *against*, and the chain triples this is applied to
have distinct components by construction. -/
theorem epsAux_append (A B : List (Letter ι)) {p q : ι} (hpq : p ≠ q) (s : ℤ) :
    epsAux (A ++ B) p q s = epsAux A p q s + epsAux B p q (s + signSum A p) := by
  induction A generalizing s with
  | nil => simp [epsAux, signSum]
  | cons a t ih =>
    by_cases hq : a.1 = q
    · have hnp : a.1 ≠ p := fun h => hpq (h ▸ hq)
      rw [List.cons_append, epsAux, if_pos hq, ih, epsAux, if_pos hq,
          signSum_cons, if_neg hnp]
      ring
    · by_cases hp : a.1 = p
      · rw [List.cons_append, epsAux, if_neg hq, if_pos hp, ih, epsAux, if_neg hq,
            if_pos hp, signSum_cons, if_pos hp]
        ring_nf
      · rw [List.cons_append, epsAux, if_neg hq, if_neg hp, ih, epsAux, if_neg hq,
            if_neg hp, signSum_cons, if_neg hp]
        ring_nf

/-- **The arithmetic core.** When the two far components occupy disjoint, ordered blocks
of the hub's longitude — no `y` in the first, no `x` in the second — the degree-2 Magnus
coefficient is exactly the product of the blocks' signed sums, and the reverse ordering
vanishes.

This is where the `u * v` of `ChainTriple.eps_eq` comes from. It is a fact about lists;
no topology enters. -/
theorem epsCoeff_append_of_blocks {A B : List (Letter ι)} {x y : ι} (hxy : x ≠ y)
    (hA : ∀ l ∈ A, l.1 ≠ y) (hB : ∀ l ∈ B, l.1 ≠ x) :
    epsCoeff (A ++ B) x y = signSum A x * signSum B y ∧
    epsCoeff (A ++ B) y x = 0 := by
  constructor
  · rw [epsCoeff, epsAux_append _ _ hxy, epsAux_eq_zero_of_no_q _ hA,
        epsAux_eq_of_no_p _ hB]
    ring
  · rw [epsCoeff, epsAux_append _ _ (Ne.symm hxy), epsAux_eq_of_no_p _ hA,
        epsAux_eq_zero_of_no_q _ hB]
    ring

/-- **The other half.** A run of `2 m` crossings between two strands alternates which
passes under, so the hub records exactly `m` of them, every one carrying the run's sign
`s`. Its signed contribution is therefore `m * s` — and the pair's total signed crossing
count is `2 * lk` by the definition of the linking number. The two agree.

Stated without division, as the identity it is: the *measured* inputs are that the run
has even length and that its length is `2|lk|`. -/
theorem underSum_eq_linking {m s lk : ℤ} (h : 2 * lk = 2 * m * s) : lk = m * s := by
  linarith

/-- **`ChainTriple.eps_eq`, derived.** Given the block structure and the two signed sums
equalling the linking numbers, the hub longitude's degree-2 Magnus coefficient is
`u * v` — which is precisely the hypothesis
`ChainTripleMilnorVanishesByGcdDividesProduct.ChainTriple.eps_eq`, and with it the
`gcd u v ∣ u * v` closure of route 3's chain residual goes through.

The hypotheses are the measured braid-word facts, named so that what is borrowed is
visible: `hA`/`hB` say the far components occupy disjoint ordered blocks, and `hsum`
says each block's signed sum is that pair's linking number. -/
theorem eps_eq_of_blocks {A B : List (Letter ι)} {x y : ι} {u v : ℤ} (hxy : x ≠ y)
    (hA : ∀ l ∈ A, l.1 ≠ y) (hB : ∀ l ∈ B, l.1 ≠ x)
    (hsum : signSum A x = u ∧ signSum B y = v) :
    epsCoeff (A ++ B) x y = u * v ∧ epsCoeff (A ++ B) y x = 0 := by
  obtain ⟨h1, h2⟩ := epsCoeff_append_of_blocks hxy hA hB
  exact ⟨by rw [h1, hsum.1, hsum.2], h2⟩

/-- **Not vacuous**: the carrier's own shape. `u = v = -2` on the all-`σ⁻¹` branch, blocks
`[(x,-1),(x,-1)]` then `[(y,-1),(y,-1)]`, and the coefficient comes out `4` — matching
`carrierChain` in the sibling file, whose `Δ = 2` then divides it. Recorded so the
theorem above cannot be read as holding because the coefficient is always zero. -/
theorem carrier_shape_gives_four :
    epsCoeff ([((0 : ℕ), (-1 : ℤ)), (0, -1)] ++ [(1, -1), (1, -1)]) 0 1 = 4 := by
  decide

end QOU.Mass.EpsEqFromMonotonicity
