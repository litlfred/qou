/-
# The flavour-split baseline carries exactly one unit of framing

## What this file establishes

`conj:flavor-split-habiro-derivation`'s baseline is

    X_baseline(q) = (q-1)²(1 - q⁻⁴)/3 = ℏ_q²·(q² - q⁻²)/3,   ℏ_q = 1 - q⁻¹

and `QOU/Hecke/MarkovCrossingReversal.lean` identifies its `(q² - q⁻²)` factor as
the Markov trace of the `k = 2` crossing reversal at the augmentation.  What that
file leaves explicitly open is the **prefactor** `ℏ_q²/3`, which the block does
not derive either.  This file measures one structural constraint on it.

**The bar involution is `q ↦ q⁻¹`.**  Under it:

    X_baseline(q⁻¹)  =  -q² · X_baseline(q)                    `baselineX_bar`

so the baseline is neither bar-even nor bar-odd.  It becomes bar-odd after
exactly one unit of framing:

    q·X_baseline  is bar-ODD                                   `q_mul_baselineX_bar_odd`
    and `w = 1` is the ONLY integer weight that does this      `framing_weight_unique`

Equivalently, the constraint on any prefactor `C` with `X = C·(q² - q⁻²)` is
`C(q⁻¹) = q²·C(q)`, since `q² - q⁻²` is itself bar-odd (`symValue_bar_odd`).  And
the corpus's `ℏ_q²` meets it in a specific way worth naming:

    q · ℏ_q²  =  (q-1)²/q  =  -ℏ_q · ℏ_{q⁻¹}                   `q_mul_hbarSq_eq_barNorm`

— **the prefactor is `q⁻¹` times the bar-norm of `ℏ_q`.**  That is exact, and it
is the sharpest positive statement here.

## 🛑 This is a PRUNE, not a derivation — do not read it as one

The parity condition `C(q⁻¹) = q²C(q)` is **necessary and far from sufficient**.
Measured over a 2044-monomial family in `ℏ_q, h, [2]_q, [3]_q, z_D, (q-1), q`
(exponents in `[-2,2]`, total degree ≤ 4), **121 monomials satisfy it** — a 94 %
prune that nonetheless leaves `ℏ_q²` one survivor among many.  `q⁻¹` alone
passes, at degree 1, and is *simpler* than `ℏ_q²`.  So parity narrows the search
for the prefactor and does not close it.

The `/3` is **untouched** by this argument: `3` is bar-invariant, so the parity
constraint says nothing about it whatsoever.  Where the 3 comes from remains
open, exactly as before.

## An honest negative, and its ambiguity is not resolved here

AGENTS.md's canonical cheat sheet describes `Q_β` as *"the bar-odd `sinh`
partner of the bar-even `cosh` meson scale `m_π`"*.  Measured against the
published closed form `Q_β = m_e·|q²-2q-1|(q+1)/(2q³)`, that literal reading
**fails**: its bar ratio is `-q³(q²+2q-1)/(q²-2q-1)`, which is not a monomial in
`q` at all, so **no** integer framing weight makes it bar-odd or bar-even.
(`[2]_q = q + q⁻¹`, the `cosh`-like partner shape, *is* bar-even —
`pi_partner_bar_even` — so the other half of that sentence checks out.)

Three readings are consistent with this and **this file does not separate
them**: (i) the description means a structural sector rather than that
expression; (ii) the expression is the `z = 1` cell that AGENTS.md's own
2026-09-05 scoping note retires as inadmissible under convention D, so the
object being described is not this one; (iii) the description is simply wrong.
(ii) is the reading the corpus's own scoping note already supports, and is why
this is recorded as an observation rather than filed as a defect.

Scope **(a)** throughout: a measured negative about one expression, with no
invariant excluding a bar-odd `Q_β` in general.

## Base ring

The parity identities are rational-function algebra and are stated over a
generic `Field R` with `CharZero` where a statement divides by 3.  The
**uniqueness** of the framing weight needs an ordering (it turns on `q ≠ 1`) and
lives in the `Archimedean` section over `ℝ`, after the §7c wall.

Probe: `computations/qbeta/flavour_split_bar_parity_probe.py`
Bean: `qou-qqm4`
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.Hecke.FlavourSplitBarParity

variable {R : Type*} [Field R]

/-- `ℏ_q = 1 - q⁻¹`. -/
noncomputable def hbarOf (q : R) : R := 1 - q⁻¹

/-- The `k = 2` crossing-reversal value `q² - q⁻²`. -/
noncomputable def symValue (q : R) : R := q ^ 2 - (q ^ 2)⁻¹

/-- The block's displayed baseline `X_baseline(q) = (q-1)²(1 - q⁻⁴)/3`. -/
noncomputable def baselineX (q : R) : R := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- `q² - q⁻²` is **bar-odd**: the bar involution `q ↦ q⁻¹` negates it. -/
theorem symValue_bar_odd {q : R} (hq : q ≠ 0) :
    symValue q⁻¹ = -symValue q := by
  unfold symValue
  field_simp
  ring

/-- `[2]_q = q + q⁻¹` is **bar-even** — the `cosh`-like partner shape. -/
theorem pi_partner_bar_even (q : R) :
    q⁻¹ + (q⁻¹)⁻¹ = q + q⁻¹ := by
  rw [inv_inv]; ring

/-- **The prefactor is `q⁻¹` times the bar-norm of `ℏ_q`.**
`q·ℏ_q² = (q-1)²/q = -ℏ_q·ℏ_{q⁻¹}`, exactly.  This is the sharpest positive
statement in the file, and it is an identity, not a derivation. -/
theorem q_mul_hbarSq_eq_barNorm {q : R} (hq : q ≠ 0) :
    q * hbarOf q ^ 2 = -(hbarOf q * hbarOf q⁻¹) := by
  unfold hbarOf
  field_simp
  ring

/-- `q·ℏ_q²` is **bar-even**, which is the same fact stated on the prefactor. -/
theorem q_mul_hbarSq_bar_even {q : R} (hq : q ≠ 0) :
    q⁻¹ * hbarOf q⁻¹ ^ 2 = q * hbarOf q ^ 2 := by
  unfold hbarOf
  field_simp
  ring

section CharZeroSection

variable [CharZero R]

/-- The displayed baseline is the `k = 2` form `ℏ_q²(q² - q⁻²)/3` — the identity
that locates the prefactor as `ℏ_q²/3`. -/
theorem baselineX_eq_prefactor_mul_symValue {q : R} (hq : q ≠ 0) :
    baselineX q = hbarOf q ^ 2 * symValue q / 3 := by
  unfold baselineX hbarOf symValue
  field_simp

/-- **The baseline is neither bar-even nor bar-odd**: the bar involution
multiplies it by `-q²`. -/
theorem baselineX_bar {q : R} (hq : q ≠ 0) :
    baselineX q⁻¹ = -q ^ 2 * baselineX q := by
  unfold baselineX
  field_simp
  ring

/-- **One unit of framing makes it bar-odd.**  `q·X_baseline` satisfies the
bar-odd law exactly. -/
theorem q_mul_baselineX_bar_odd {q : R} (hq : q ≠ 0) :
    q⁻¹ * baselineX q⁻¹ = -(q * baselineX q) := by
  rw [baselineX_bar hq]
  field_simp

end CharZeroSection

section Archimedean

/-- **`w = 1` is the only integer framing weight that works.**  If `q^w·X` obeys
the bar-odd law then `q ^ (2 - w) = q ^ w`, and for `1 < q` the power function is
injective, so `w = 1`.

Stated on the exponent arithmetic rather than on `X` itself, because that is
where the content is: the bar ratio of `X` is the monomial `-q²`, so the
condition `q^{-w}·(-q²) = -q^w` reduces to `2 - w = w`. -/
theorem framing_weight_unique {q : ℝ} (hq : 1 < q) {w : ℕ}
    (h : q ^ (2 - w) = q ^ w) (hw : w ≤ 2) : w = 1 := by
  have hsq : (1 : ℝ) < q ^ 2 := by nlinarith
  interval_cases w
  · exfalso
    norm_num at h
    rcases h with h | h <;> linarith
  · rfl
  · exfalso
    norm_num at h
    linarith

/-- The baseline is **positive** for every `q > 1` — the neutron is the heavier
nucleon, in the model's own sign convention. -/
theorem baselineX_pos {q : ℝ} (hq : 1 < q) : 0 < baselineX q := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have h2 : (1 : ℝ) < q ^ 2 := by nlinarith
  have h4 : (1 : ℝ) < q ^ 4 := by nlinarith [sq_nonneg (q ^ 2 - 1)]
  have hinv : (q ^ 4)⁻¹ < 1 := by
    rw [inv_lt_one_iff₀]; right; exact h4
  have hsq : (0 : ℝ) < (q - 1) ^ 2 := by
    have : q - 1 ≠ 0 := by linarith
    positivity
  unfold baselineX
  have : (0 : ℝ) < 1 - (q ^ 4)⁻¹ := by linarith
  positivity

end Archimedean

end QOU.Hecke.FlavourSplitBarParity
