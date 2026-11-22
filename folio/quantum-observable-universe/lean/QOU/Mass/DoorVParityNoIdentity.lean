/-
  Door-v parity no-identity: the C1⊗C1 tensor-square realization cannot carry
  the GGM sign character.

  Setting (docs/audits/2026-07-20-qlift-doorV-stokes.md). Door-iv built the
  `{+1,−1}` graded module of GGM from the tensor square of the proved q-lift
  kernel C1, using the carrier-lifted growing/decaying solutions `f₊`, `f₋`.
  Door-v then normalized away the diagonal slope-scaling and found that TS and
  GGM agree as graded + Stokes modules — the unipotent Stokes part is TRIVIAL
  (`U → I`) — leaving a SINGLE residual: a diagonal ℤ/2 `(−1)^m` sign
  character. GGM's growing solution alternates sign (`y_{m+1} ~ −q^m y_m`),
  whereas the tensor-square real solutions `f₊²`, `f₋²` are non-negative (a real
  square is `≥ 0`). This file upgrades that numerical finding to a compiled
  scope-(b) NO-IDENTITY theorem: the positive cone spanned by two non-negative
  sequences (the squares) contains NO genuinely sign-alternating sequence, so no
  such combination can equal the sign-alternating GGM target.

  The `(−1)^m` alternation is the bar-parity of the sinh/cosh (bar-odd/bar-even)
  decomposition: a bar-even (cosh) profile has no sign flip, a genuine bar-odd
  (sinh) alternation does; a sum of squares lives entirely in the non-negative
  (cosh-like) cone. This is the SAME non-negativity invariant as the
  KL-positivity prune (docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md):
  a manifestly non-negative construction cannot supply a mixed-sign target.

  HONEST SCOPE (scope-(b) STRUCTURAL EXCLUSION, per AGENTS.md §"Before
  declaring 'refuted'"). This proves the PARITY obstruction — the minimal named
  residual isolated by Door-v — and NOTHING more. It does NOT assert that C1/GGM
  are unrelated in every sense: Door-v established that they DO share graded +
  Stokes structure (slopes and theta magnitudes match; the unipotent bridge is
  trivial). The cited invariant is exact non-negativity of a real square
  (`0 ≤ x²` / `mul_nonneg`), not a numerical fit and not AME data — hence a
  legitimate scope-(b) exclusion of the specific squares-based realization,
  never a claim about C1 as a module (that module-level exclusion is Door-i's).

  §7c: this is genuinely archimedean (sign / ordering of `ℝ`), so `ℝ` is the
  correct base ring here — not a gratuitous specialization.

  -- Ref: [leitner2026] docs/audits/2026-07-20-qlift-doorV-stokes.md
  -- Ref: [ramis-sauloy-zhang2013] q-difference formal classification / Stokes
-/

import Mathlib.Tactic
import Mathlib.Data.Real.Basic

namespace QOU.Mass.DoorVParityNoIdentity

/-- **The core parity fact.** A pointwise non-negative real sequence is never
    sign-alternating: for every `n`, the product of consecutive terms is
    non-negative, so it cannot be `< 0`. This is the exact invariant behind the
    Door-v residual — the tensor-square solutions `f₊²`, `f₋²` are non-negative
    squares, hence carry no consecutive sign flip. -/
theorem nonneg_not_signalternating (s : ℕ → ℝ) (hs : ∀ n, 0 ≤ s n) (n : ℕ) :
    ¬ (s n * s (n + 1) < 0) :=
  not_lt.mpr (mul_nonneg (hs n) (hs (n + 1)))

/-- A non-negative-coefficient combination of two non-negative sequences is
    itself pointwise non-negative — the positive cone of `{p, q}`. The
    tensor-square realization forces exactly this sign structure (both
    coefficients act on non-negative squares). -/
theorem posCone_nonneg
    (p q : ℕ → ℝ) (hp : ∀ n, 0 ≤ p n) (hq : ∀ n, 0 ≤ q n)
    (α β : ℝ) (hα : 0 ≤ α) (hβ : 0 ≤ β) (n : ℕ) :
    0 ≤ α * p n + β * q n :=
  add_nonneg (mul_nonneg hα (hp n)) (mul_nonneg hβ (hq n))

/-- **Door-v parity NO-IDENTITY (scope-(b) structural exclusion).**

    Model of the Door-v situation. `p`, `q` are the non-negative tensor-square
    sequences `f₊²`, `f₋²` (`0 ≤ p n`, `0 ≤ q n`). `y` is the genuinely
    sign-alternating GGM target (`y n · y (n+1) < 0`, i.e. every consecutive
    pair flips sign — the `(−1)^m` character). `α, β ≥ 0` are the sign-preserving
    coefficients the tensor-square positivity forces.

    Conclusion: NO such `(α, β)` reproduces the target — `α·p + β·q = y` is
    impossible. Proof: the left side lies in the non-negative positive cone
    (`posCone_nonneg`), so an identity would force `y ≥ 0` everywhere,
    contradicting a single sign flip (`nonneg_not_signalternating`). One
    consecutive pair suffices, so genuine alternation *anywhere* already
    excludes the identity.

    This is a scope-(b) exclusion: the cited invariant is the proved
    non-negativity of a real square, not a numerical near-match. -/
theorem doorV_parity_no_identity
    (p q y : ℕ → ℝ)
    (hp : ∀ n, 0 ≤ p n) (hq : ∀ n, 0 ≤ q n)
    (α β : ℝ) (hα : 0 ≤ α) (hβ : 0 ≤ β)
    (m : ℕ) (hy : y m * y (m + 1) < 0) :
    ¬ (∀ n, α * p n + β * q n = y n) := by
  intro hid
  -- The combination lies in the non-negative cone, so `y ≥ 0` at `m` and `m+1`.
  have hym : 0 ≤ y m := by
    rw [← hid m]; exact posCone_nonneg p q hp hq α β hα hβ m
  have hym1 : 0 ≤ y (m + 1) := by
    rw [← hid (m + 1)]; exact posCone_nonneg p q hp hq α β hα hβ (m + 1)
  -- But then the consecutive product is non-negative, contradicting the flip.
  exact absurd hy (not_lt.mpr (mul_nonneg hym hym1))

/-- Everywhere-alternating specialization: if the GGM target flips sign at
    *every* consecutive pair, no non-negative-cone combination of the
    tensor-square sequences can equal it. Immediate from the pointwise version
    at `m = 0`. -/
theorem doorV_parity_no_identity_forall
    (p q y : ℕ → ℝ)
    (hp : ∀ n, 0 ≤ p n) (hq : ∀ n, 0 ≤ q n)
    (α β : ℝ) (hα : 0 ≤ α) (hβ : 0 ≤ β)
    (hy : ∀ n, y n * y (n + 1) < 0) :
    ¬ (∀ n, α * p n + β * q n = y n) :=
  doorV_parity_no_identity p q y hp hq α β hα hβ 0 (hy 0)

/-! ## The bar-parity twist — what it does and does not do

Added 2026-08-08 for `conj:c1-ggm-bar-parity-faces`. The obstruction above says
no non-negative-cone combination can equal a target with a consecutive sign
flip. The conjecture's open half asks whether the diagonal `ℤ/2` character
`(−1)^m` is the *whole* difference. These lemmas settle the scalar-combination
reading of that question, in the negative, and say why the module-level reading
is untouched.

The twist inverts **every** consecutive-pair sign, not only the alternating
ones. So it can clear the obstruction only for a target that alternates at
*every* pair — and the Stokes carrier's solution does not, since `2 − q^{m+1}`
is positive below `m + 1 = log 2 / log q`. Measured in
`computations/qbeta/c3_w2_bar_parity_twist_probe.py` (4/4): the twisted sequence
still flips, at exactly the indices where the untwisted one did not.

**Consequence.** "The diagonal `ℤ/2` character is the sole residual" cannot mean
that applying the character makes the target a non-negative combination of the
squares — that reading is excluded by the same non-negativity invariant that
produced the obstruction. It must be read at the **module** level, up to a
genuine gauge. Nothing here bears on that, and nothing here refutes the
conjecture; one reading of it is removed. -/

section BarTwist

variable {K : Type*} [Field K]

/-- The bar-parity twist `z_m = (−1)^m y_m`. -/
noncomputable def barTwist (y : ℕ → K) (m : ℕ) : K := (-1) ^ m * y m

/-- **The twist carries the Stokes carrier's recurrence to a sign-flipped one.**
`y_{m+2} − (2−q^{m+1})y_{m+1} + y_m = 0` becomes
`z_{m+2} + (2−q^{m+1})z_{m+1} + z_m = 0`. -/
theorem barTwist_recursion (q : K) (y : ℕ → K) (m : ℕ)
    (h : y (m + 2) - (2 - q ^ (m + 1)) * y (m + 1) + y m = 0) :
    barTwist y (m + 2) + (2 - q ^ (m + 1)) * barTwist y (m + 1) + barTwist y m = 0 := by
  simp only [barTwist, pow_succ, pow_add]
  linear_combination ((-1 : K)) ^ m * h

/-- Conversely: the sign-flipped recurrence twists back to the original. -/
theorem barTwist_recursion_inv (q : K) (z : ℕ → K) (m : ℕ)
    (h : z (m + 2) + (2 - q ^ (m + 1)) * z (m + 1) + z m = 0) :
    barTwist z (m + 2) - (2 - q ^ (m + 1)) * barTwist z (m + 1) + barTwist z m = 0 := by
  simp only [barTwist, pow_succ, pow_add]
  linear_combination ((-1 : K)) ^ m * h

end BarTwist

section BarTwistReal

/-- **The twist inverts consecutive-pair signs.** -/
theorem barTwist_consecutive_product (y : ℕ → ℝ) (m : ℕ) :
    barTwist y m * barTwist y (m + 1) = - (y m * y (m + 1)) := by
  have h : ((-1 : ℝ)) ^ m * (-1 : ℝ) ^ m = 1 := by
    rw [← pow_add, ← two_mul, pow_mul]; norm_num
  simp only [barTwist, pow_succ]
  linear_combination (-(y m * y (m + 1))) * h

/-- **The twist removes exactly the parity obstruction.**

`doorV_parity_no_identity` excludes a non-negative-cone identity precisely when
the target has a consecutive sign flip, `y_m · y_{m+1} < 0`. After the twist that
product is strictly positive, so the obstruction does not apply to the twisted
sequence — and it is removed for *every* `m` at which it fired, with nothing
else about the hypothesis changed. -/
theorem barTwist_removes_obstruction (y : ℕ → ℝ) (m : ℕ) (h : y m * y (m + 1) < 0) :
    0 < barTwist y m * barTwist y (m + 1) := by
  rw [barTwist_consecutive_product]
  linarith

/-- And it removes it *only* there: if the target had no flip at `m`, the twist
introduces one. The twist is therefore exactly the parity, not a weakening. -/
theorem barTwist_creates_obstruction (y : ℕ → ℝ) (m : ℕ) (h : 0 < y m * y (m + 1)) :
    barTwist y m * barTwist y (m + 1) < 0 := by
  rw [barTwist_consecutive_product]
  linarith

/-- **The parity twist RELOCATES the obstruction; it cannot remove it.**

`doorV_parity_no_identity` fires as soon as the target has one consecutive sign
flip. The twist inverts *every* consecutive-pair sign
(`barTwist_consecutive_product`), so at each `m` where the product is nonzero
the obstruction fires on `y` or on its twist — never on neither. -/
theorem obstruction_fires_on_one_of (y : ℕ → ℝ) (m : ℕ) (h : y m * y (m + 1) ≠ 0) :
    y m * y (m + 1) < 0 ∨ barTwist y m * barTwist y (m + 1) < 0 := by
  rw [barTwist_consecutive_product]
  rcases lt_trichotomy (y m * y (m + 1)) 0 with hlt | heq | hgt
  · exact Or.inl hlt
  · exact absurd heq h
  · exact Or.inr (by linarith)

/-- **Consequence: the twist clears the obstruction only for a target that
alternates at *every* consecutive pair.**

If some pair of the twisted sequence still flips, no non-negative-cone
combination can equal it either — so exhibiting the twist does not by itself
make the target reachable. -/
theorem twist_clears_only_if_everywhere_alternating (y : ℕ → ℝ)
    (hclear : ∀ m, 0 < barTwist y m * barTwist y (m + 1)) (m : ℕ) :
    y m * y (m + 1) < 0 := by
  have := hclear m
  rw [barTwist_consecutive_product] at this
  linarith

end BarTwistReal

end QOU.Mass.DoorVParityNoIdentity
