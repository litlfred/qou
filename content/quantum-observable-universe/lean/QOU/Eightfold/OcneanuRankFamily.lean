import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
# QOU.Eightfold.OcneanuRankFamily — convention D is the rank-2 member of a
one-parameter family, and the rank is recoverable from the Markov parameter

Bean `qou-j3w6` (the condition-5 decision), epic `qou-8lxd`.  Companion to
`QOU.QuantumObservableUniverse.VolumeFormDegree`, which is the same `N` on the
categorical side.

## The question this answers

Does the corpus's canonical Markov parameter `z = q³/(q²+1)` (convention D,
owner ruling 2026-08-15 R1) correspond to a *rank*, and if the rank is left free
is there a natural member at every `N`?

**Yes to both, and the two are the same `N` as the volume-form degree.**
[`computations/y_lambda_su_n.py`](../../../../../computations/y_lambda_su_n.py)
already carries the `N`-parametrised weights — the principal specialisation
`s_λ(1, q, …, q^{N-1})` by hook-content — and every call site in the corpus
passes `N = 2`.  Evaluating the Markov parameter `z = tr_M(σ) = y_{(2)}·q −
y_{(1,1)}·q⁻¹` on those weights gives, symbolically and exactly,

  `z_N  =  (q − q⁻¹) · q^{2N} / (q^{2N} − 1)`

which is `markovParam` below.  Verified exact in `sympy` for `N = 1 … 6` against
that producer; `z_2 = q³/(q²+1)` on the nose, and numerically
`z_2(q₀) = 0.6126880371464652516` against the trace-convention registry's
`REG_ZD = 0.61268803714646524`.

## The three facts, and why each matters

**(1) `z_2` IS convention D** (`markovParam_two`).  So the production trace is
an `SU(N)` quantum-group trace, at `N = 2`.  The corpus's canonical Markov
parameter is not a free normalisation choice that happened to land somewhere —
it is a *rank commitment*.

**(2) The rank is recoverable from the parameter** (`markovParam_strictAnti`,
`markovParam_injective`).  For `1 < q` the family is strictly decreasing in `N`,
hence injective, so `z` determines `N`.  This is what makes (1) a commitment
rather than a coincidence: no other rank produces `q³/(q²+1)`.  It is also the
Lean form of what
[`ocneanu_N_lockin_probe.py`](../../../../../computations/ocneanu_N_lockin_probe.py)
measures numerically — the mass channel cannot be *retuned* to `N = 3`, because
moving `N` moves `z`, and `z` is the trace the mass pipeline already evaluates.
Flavour therefore needs a **second trace on the same `H_n(q)`**, not a modified
first one; `QOU.Braiding.HnMarkovTrace.MarkovTraceTower` already types the
Markov parameter as a free class field, so two instances are typeable today.

**(3) The whole family sits between two limits** (`markovParam_gt_hecke`,
`markovParam_one`).  `z_1 = q` is the `gl(1)` corner where only the fully
symmetric block survives; `z_N` decreases strictly to `q − q⁻¹`, the coefficient
of the Hecke relation itself `σ² = (q − q⁻¹)σ + 1`, which is the `N → ∞`
(uncapped, full-Hecke) value and is never attained.  Every rank-`N` trace is
`(q − q⁻¹)` plus the strictly positive excess `(q − q⁻¹)/(q^{2N} − 1)`
(`markovParam_sub_hecke`), and that excess is exactly the row cap.

## The row cap, and its identity with the volume-form degree

`RowCapObstruction.lean` proves `dim V_{(1^3)} = C(N,3)` vanishes iff `N < 3`,
i.e. `Λ³` of a rank-`N` object needs `N ≥ 3`.  Here the same cap arrives as
arithmetic, from the hook-content numerator: a partition with more than `N` rows
has a cell at position `(N+1, 1)`, whose content is `1 − (N+1) = −N`, so the
numerator picks up the balanced quantum integer `[N + (−N)]_q = [0]_q = 0` and
the whole weight dies (`cap_content`, `qIntBalanced_zero`, `rowCapFactor_eq_zero`).
Measured on the producer at `n = 4`: `N = 1` survives only `(4)`, `N = 2` only
`ℓ(λ) ≤ 2`, `N = 3` only `ℓ(λ) ≤ 3`, `N = 4` everything.

**That cap is the volume form.**  The last partition surviving at rank `N` is
the single column `(1^N)`, which is `Λ^N` of the fundamental — the determinant,
`Λ^N W ≅ 𝟙`; the first to die is `(1^{N+1})`, i.e. `Λ^{N+1}W = 0`.  So the `N`
of `VolumeFormDegree.rank_eq_of_volumeForm` and the `N` of this trace are one
number, approached from the categorical and the trace side respectively.  In
particular **condition 5 of `def:quantum-observable-universe` (`Λ²V ≅ 𝟙`) and
convention D (`z = q³/(q²+1)`) are the same commitment**, stated twice.

## What is proved here, and what is not

**Proved, sorry-free:** every statement about `markovParam` and the row-cap
arithmetic below — the closed form's specialisations, strict antitonicity and
injectivity in `N`, the two-sided bracket, and the content computation that
makes the cap automatic.

**Not proved, and asserted nowhere below:**

* that `markovParam N` **is** the Markov parameter of the `SU(N)` trace.  That is
  the hook-content principal-specialisation identity, verified symbolically in
  `sympy` against the corpus producer for `N = 1 … 6` and cited here; Mathlib has
  no hook-content or principal-specialisation API to state it against.  Every
  declaration below is about the closed form, and none upgrades to a claim about
  Hecke weights.
* that a rank-3 trace **exists** on the substrate's `H_n(q)` as a second
  structure compatible with axioms 1–4.  Nothing here constructs one.  This file
  says what its parameter would have to be — `z_3 = q⁵/(q⁴+q²+1)`,
  `≈ 0.4493048091` at `q₀` (`markovParam_three`) — which is a *specification*,
  not a construction.
* anything about which rank the axioms supply.  That is bean `qou-j3w6`.

Base ring: `ℝ`, and the archimedean specialisation is genuine rather than
gratuitous (§7c) — the ordering `1 < q` is used essentially, both for
`q^{2N} ≠ 1` and for the strict monotonicity that carries the whole injectivity
argument.
-/

namespace QOU.Eightfold.OcneanuRankFamily

/-- The Markov parameter of the rank-`N` Ocneanu / Wenzl trace, as a closed form
in the substrate modulus.

`z_N = (q − q⁻¹) · q^{2N} / (q^{2N} − 1)`.  See the module docstring for its
provenance: it is the value of `tr_M(σ)` on the hook-content weights of
`computations/y_lambda_su_n.py`, verified symbolically for `N = 1 … 6`. -/
noncomputable def markovParam (N : ℕ) (q : ℝ) : ℝ :=
  (q - q⁻¹) * q ^ (2 * N) / (q ^ (2 * N) - 1)

/-- The Hecke coefficient `q − q⁻¹` — the `N → ∞` value of the family, and the
coefficient in `σ² = (q − q⁻¹)σ + 1`. -/
noncomputable def heckeCoeff (q : ℝ) : ℝ := q - q⁻¹

section Positivity

variable {q : ℝ} (hq : 1 < q)

include hq

theorem q_pos : 0 < q := lt_trans zero_lt_one hq

theorem q_ne_zero : q ≠ 0 := ne_of_gt (q_pos hq)

/-- `1 < q^{2N}` for `N ≥ 1` — what makes the denominator non-zero. -/
theorem one_lt_pow_two_mul {N : ℕ} (hN : 1 ≤ N) : 1 < q ^ (2 * N) :=
  one_lt_pow₀ hq (by omega)

theorem denom_pos {N : ℕ} (hN : 1 ≤ N) : 0 < q ^ (2 * N) - 1 :=
  sub_pos.mpr (one_lt_pow_two_mul hq hN)

theorem heckeCoeff_pos : 0 < heckeCoeff q := by
  have h0 : 0 < q := q_pos hq
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  simpa [heckeCoeff] using sub_pos.mpr (lt_trans this hq)

end Positivity

section Identities

variable {q : ℝ} (hq : 1 < q)

include hq

/-- **`z_1 = q`** — the `gl(1)` corner, where only the fully symmetric block
survives.  (`N = 1` keeps exactly the partitions with one row.) -/
theorem markovParam_one : markovParam 1 q = q := by
  have h0 : q ≠ 0 := q_ne_zero hq
  have hd : q ^ (2 * 1) - 1 ≠ 0 := ne_of_gt (denom_pos hq le_rfl)
  simp only [markovParam]
  rw [div_eq_iff hd]
  field_simp

/-- **`z_2 = q³/(q²+1)` — this is convention D**, the corpus's canonical Markov
parameter (owner ruling 2026-08-15 R1).  So the production trace is the rank-2
member of the family, and `def:quantum-observable-universe`'s condition 5
`Λ²V ≅ 𝟙` is the same commitment read categorically. -/
theorem markovParam_two : markovParam 2 q = q ^ 3 / (q ^ 2 + 1) := by
  have h0 : q ≠ 0 := q_ne_zero hq
  have hd : q ^ (2 * 2) - 1 ≠ 0 := ne_of_gt (denom_pos hq (by omega))
  have hs : q ^ 2 + 1 ≠ 0 := by positivity
  simp only [markovParam]
  rw [div_eq_div_iff hd hs]
  field_simp
  ring

/-- **`z_3 = q⁵/(q⁴+q²+1)`** — the value a flavour `SU(3)` trace on the same
`H_n(q)` would have to carry.  `≈ 0.4493048091` at the substrate `q₀`.  A
specification, not a construction: nothing here builds such a trace. -/
theorem markovParam_three : markovParam 3 q = q ^ 5 / (q ^ 4 + q ^ 2 + 1) := by
  have h0 : q ≠ 0 := q_ne_zero hq
  have hd : q ^ (2 * 3) - 1 ≠ 0 := ne_of_gt (denom_pos hq (by omega))
  have hs : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  simp only [markovParam]
  rw [div_eq_div_iff hd hs]
  field_simp
  ring

/-- **The excess over the Hecke coefficient is exactly the row cap.**
`z_N − (q − q⁻¹) = (q − q⁻¹)/(q^{2N} − 1)`, strictly positive and strictly
decreasing — so an uncapped (`N → ∞`) trace would sit at `q − q⁻¹` and every
finite rank sits strictly above it. -/
theorem markovParam_sub_hecke {N : ℕ} (hN : 1 ≤ N) :
    markovParam N q - heckeCoeff q = heckeCoeff q / (q ^ (2 * N) - 1) := by
  have hd : q ^ (2 * N) - 1 ≠ 0 := ne_of_gt (denom_pos hq hN)
  simp only [markovParam, heckeCoeff]
  field_simp
  ring

/-- Every member of the family lies strictly above the Hecke coefficient. -/
theorem markovParam_gt_hecke {N : ℕ} (hN : 1 ≤ N) : heckeCoeff q < markovParam N q := by
  have hd : 0 < q ^ (2 * N) - 1 := denom_pos hq hN
  have hh : 0 < heckeCoeff q := heckeCoeff_pos hq
  have := markovParam_sub_hecke hq hN
  nlinarith [div_pos hh hd, this]

end Identities

section Monotonicity

variable {q : ℝ} (hq : 1 < q)

include hq

/-- **The family is strictly decreasing in the rank.**  Together with
`markovParam_injective` this is what makes convention D a *rank commitment*:
`z` determines `N`, so the mass channel's trace cannot be silently retuned to a
different rank. -/
theorem markovParam_strictAnti {M N : ℕ} (hM : 1 ≤ M) (hMN : M < N) :
    markovParam N q < markovParam M q := by
  have hN : 1 ≤ N := le_trans hM (le_of_lt hMN)
  have hdM : 0 < q ^ (2 * M) - 1 := denom_pos hq hM
  have hdN : 0 < q ^ (2 * N) - 1 := denom_pos hq hN
  have hh : 0 < heckeCoeff q := heckeCoeff_pos hq
  have hlt : q ^ (2 * M) < q ^ (2 * N) :=
    pow_lt_pow_right₀ hq (by omega)
  have hstep : heckeCoeff q / (q ^ (2 * N) - 1) < heckeCoeff q / (q ^ (2 * M) - 1) :=
    div_lt_div_of_pos_left hh hdM (by linarith)
  have eM := markovParam_sub_hecke hq hM
  have eN := markovParam_sub_hecke hq hN
  linarith

/-- **The rank is recoverable from the Markov parameter.** -/
theorem markovParam_injective {M N : ℕ} (hM : 1 ≤ M) (hN : 1 ≤ N)
    (h : markovParam M q = markovParam N q) : M = N := by
  rcases lt_trichotomy M N with hlt | heq | hgt
  · exact absurd h (markovParam_strictAnti hq hM hlt).ne'
  · exact heq
  · exact absurd h (markovParam_strictAnti hq hN hgt).ne

/-- **No rank other than 2 gives convention D.**  The corollary that matters for
the corpus: `z = q³/(q²+1)` pins `N = 2`. -/
theorem conventionD_forces_rank_two {N : ℕ} (hN : 1 ≤ N)
    (h : markovParam N q = q ^ 3 / (q ^ 2 + 1)) : N = 2 :=
  markovParam_injective hq hN (by omega) (h.trans (markovParam_two hq).symm)

end Monotonicity

section RowCap

/-- The content of the cell in row `i`, column `j` of a Young diagram
(1-indexed), as an integer: `j − i`. -/
def content (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- The balanced quantum integer `[m]_q = (q^m − q^{−m})/(q − q⁻¹)`, at integer
`m`.  This is the factor the hook-content numerator contributes per cell, with
`m = N + content`. -/
noncomputable def qIntBalanced (m : ℤ) (q : ℝ) : ℝ :=
  (q ^ m - q ^ (-m)) / (q - q⁻¹)

@[simp] theorem qIntBalanced_zero (q : ℝ) : qIntBalanced 0 q = 0 := by
  simp [qIntBalanced]

/-- **The cap cell.**  A partition with more than `N` rows has a cell at
`(N+1, 1)`, and its content is `−N`. -/
theorem cap_content (N : ℕ) : content (N + 1) 1 = -(N : ℤ) := by
  simp [content]

/-- **The row cap is automatic, not imposed.**  At that cell the numerator factor
is `[N + content]_q = [N − N]_q = [0]_q = 0`, so the whole hook-content weight
vanishes.  This is `RowCapObstruction.weyl_dim_alt_eq_zero_iff` arriving as
arithmetic rather than as a dimension count. -/
theorem rowCapFactor_eq_zero (N : ℕ) (q : ℝ) :
    qIntBalanced ((N : ℤ) + content (N + 1) 1) q = 0 := by
  rw [cap_content]
  simp

/-- The cap is sharp: at a cell of row `i ≤ N` in column 1 the factor is
`[N + 1 − i]_q`, whose index is strictly positive, so nothing above the cap is
killed by this mechanism. -/
theorem belowCap_index_pos {N i : ℕ} (hiN : i ≤ N) :
    0 < (N : ℤ) + content i 1 := by
  simp only [content]
  omega

end RowCap

end QOU.Eightfold.OcneanuRankFamily
