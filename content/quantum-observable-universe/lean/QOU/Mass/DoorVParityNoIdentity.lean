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

  -- Ref: [manuscript] docs/audits/2026-07-20-qlift-doorV-stokes.md
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

end QOU.Mass.DoorVParityNoIdentity
