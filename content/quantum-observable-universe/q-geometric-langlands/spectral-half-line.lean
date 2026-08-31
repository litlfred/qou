import QOU.AlgebraicSubstrate.LocalQZetaFunction
import QOU.AlgebraicSubstrate.ReebSpectrum
import QOU.AlgebraicSubstrate.WeilZeta
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv

/-!
# QOU.AlgebraicSubstrate.spectral_half_line

Corollary: the spectral coordinate mapping translates the Hasse–Weil
bound into Re(ρᵢ) = 1/2 for all fundamental Reeb modes.

## Proof strategy for `abs_cpow_ofReal_eq_rpow_re`

For real q > 0 and complex ρ:

  (↑q)^ρ  = exp(ρ · log(↑q))          [cpow definition, ↑q ≠ 0]
  |exp(z)| = exp(Re(z))                [Complex.norm_exp]
  (log ↑q).re = Real.log |↑q| = log q  [log_re + abs_ofReal + abs_of_pos]
  (log ↑q).im = arg(↑q) = 0            [log_im + arg_ofReal_of_nonneg]

  Hence: |(↑q)^ρ| = exp(Re(ρ)·log q - Im(ρ)·0)
                   = exp(Re(ρ)·log q)
                   = q^{Re(ρ)}           [rpow_def_of_pos]

LaTeX label: `cor:spectral-half-line`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

set_option autoImplicit false


open Complex Real

namespace QOU.AlgebraicSubstrate

/-- For real q > 0 and complex ρ, |q^ρ| = q^{Re(ρ)}.

    The proof uses the chain:
    `|(↑q)^ρ| = |exp(ρ · log(↑q))| = exp(Re(ρ · log(↑q)))`.
    For positive real q, `log(↑q) = log(q) + 0·i`, so
    `Re(ρ · log(↑q)) = Re(ρ) · log(q)` and
    `exp(Re(ρ) · log(q)) = q^{Re(ρ)}` by definition of `rpow`. -/
theorem abs_cpow_ofReal_eq_rpow_re (q : ℝ) (hq : 0 < q) (ρ : ℂ) :
    ‖(q : ℂ) ^ ρ‖ = q ^ ρ.re :=
  Complex.norm_cpow_eq_rpow_re_of_pos hq ρ

theorem abs_rpow_eq_rpow_re (q : ℝ) (hq : q > 1) (ρ : ℂ) :
    ‖(q : ℂ) ^ ρ‖ = q ^ ρ.re :=
  abs_cpow_ofReal_eq_rpow_re q (by linarith) ρ

/-- **Spectral half-line**: all fundamental Reeb modes lie on the
    critical line Re(ρ) = 1/2.

    Given the spectral coordinate mapping αᵢ = q^{ρᵢ}, the
    Hasse–Weil bound |αᵢ| = q^{1/2} forces Re(ρᵢ) = 1/2.

    **Proof**: By `abs_rpow_eq_rpow_re`, |q^{ρᵢ}| = q^{Re(ρᵢ)}.
    Combined with |αᵢ| = q^{1/2}, we get q^{Re(ρᵢ)} = q^{1/2}.
    Since q > 1, the function q^(·) is strictly monotone, giving
    Re(ρᵢ) = 1/2. -/
theorem spectral_half_line
    (Z : LocalQZetaFunction)
    (hq : Z.q > 1)
    (ρ : Fin 8 → ℂ)
    (spectral_coord : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i))
    (hw : ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ)) :
    ∀ i, (ρ i).re = 1 / 2 := by
  intro i
  have h1 := hw i
  rw [spectral_coord i, abs_rpow_eq_rpow_re Z.q hq (ρ i)] at h1
  -- h1 : Z.q ^ (ρ i).re = Z.q ^ (1 / 2 : ℝ)
  -- Since q > 1 (hence q ≠ 1), rpow q is injective in the exponent
  -- q^a = q^b with q > 1 forces a = b: take logs and cancel log q ≠ 0.
  -- (There is no exponent-injectivity lemma for real `rpow` in this Mathlib;
  --  `rpow_left_injective` exists only for ℝ≥0 / ℝ≥0∞ and is injectivity in
  --  the BASE, not the exponent.)
  have hq0 : (0 : ℝ) < Z.q := by linarith
  have hlog : Real.log Z.q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have hl := congrArg Real.log h1
  rw [Real.log_rpow hq0, Real.log_rpow hq0] at hl
  exact mul_right_cancel₀ hlog hl

/-! ## The spectral coordinate map

`spectral_half_line` takes `spectral_coord` as a hypothesis. Two facts about
that hypothesis are provable here and are worth separating from what is not
(bean `qou-qspc`).

**What is proved below.** Such a map always *exists* — `ρ := log α / log q` on
the principal branch, using only `α ≠ 0`, which `LocalQZetaFunction` carries —
and, more usefully, `Re(ρ)` is *independent of the branch*: any two exponents
with the same `q`-power share a real part. So the conclusion `Re(ρᵢ) = 1/2` is
well-posed even though the map `α ↦ ρ` is not, being determined only modulo
`2πi / log q`.

**What is NOT proved, and is the open part.** Nothing here identifies these `ρᵢ`
with the spectrum of the Reeb derivation `ξ_q`. `spectral_coord` in
`spectral_half_line` is doing double duty: it asserts a coordinate relation
(supplied below) *and* that the exponents are Reeb eigenvalues (not supplied
anywhere in the corpus). Existence does not close that gap — it isolates it. -/

/-- A spectral coordinate map always exists: on the principal branch,
    `ρ := log α / log q` satisfies `α = q^ρ`.

    Uses only `q > 1` and `αᵢ ≠ 0`, the latter being a field of
    `LocalQZetaFunction`. This supplies the *coordinate relation* of
    `spectral_half_line`'s `spectral_coord` hypothesis, and nothing more —
    see the section docstring. -/
theorem exists_spectral_coord (Z : LocalQZetaFunction) (hq : Z.q > 1) :
    ∃ ρ : Fin 8 → ℂ, ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i) := by
  have hq0 : (0 : ℝ) < Z.q := by linarith
  have hlog : Real.log Z.q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have hqC : (Z.q : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt hq0)
  refine ⟨fun i => Complex.log (Z.eigenvalues i) / (Real.log Z.q : ℂ), fun i => ?_⟩
  have hlogC : (Real.log Z.q : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hlog
  show Z.eigenvalues i = (Z.q : ℂ) ^ (Complex.log (Z.eigenvalues i) / (Real.log Z.q : ℂ))
  rw [Complex.cpow_def_of_ne_zero hqC, ← Complex.ofReal_log (le_of_lt hq0), mul_comm,
      div_mul_cancel₀ _ hlogC, Complex.exp_log (Z.eigenvalues_ne_zero i)]

/-- **The real part is branch-independent.** `α = q^ρ` pins `ρ` only modulo
    `2πi / log q`, but every such `ρ` has the same real part — so
    `Re(ρᵢ) = 1/2` is a well-posed conclusion despite the map `α ↦ ρ` not being
    well-defined. -/
theorem spectral_coord_re_unique
    (q : ℝ) (hq : q > 1) (α : ℂ) (ρ ρ' : ℂ)
    (h : (q : ℂ) ^ ρ = α) (h' : (q : ℂ) ^ ρ' = α) :
    ρ.re = ρ'.re := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlog : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have e : q ^ ρ.re = q ^ ρ'.re := by
    rw [← abs_cpow_ofReal_eq_rpow_re q hq0 ρ, ← abs_cpow_ofReal_eq_rpow_re q hq0 ρ',
        h, h']
  have hl := congrArg Real.log e
  rw [Real.log_rpow hq0, Real.log_rpow hq0] at hl
  exact mul_right_cancel₀ hlog hl

/-- The real part produced by the principal branch, in closed form:
    `Re(ρ) = log ‖α‖ / log q`. Combined with `spectral_coord_re_unique` this is
    *the* real part of any spectral coordinate for `α`. -/
theorem spectral_coord_re_eq
    (q : ℝ) (hq : q > 1) (α : ℂ) (ρ : ℂ) (h : (q : ℂ) ^ ρ = α) :
    ρ.re = Real.log ‖α‖ / Real.log q := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlog : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have e : q ^ ρ.re = ‖α‖ := by rw [← abs_cpow_ofReal_eq_rpow_re q hq0 ρ, h]
  have hl := congrArg Real.log e
  rw [Real.log_rpow hq0] at hl
  rw [eq_div_iff hlog]
  exact hl

/-! ## Why the line is `Re = 1/2` — the functional equation's fixed locus

`spectral_half_line` derives `Re(ρ) = 1/2` from `|α| = q^{1/2}`, but nothing so
far says why *that* line rather than any other vertical one. The reason is a
symmetry, and it is provable here.

The functional equation pairs `α` with `q/α`. When `|α|² = q` — the Hasse–Weil
conclusion — that partner is exactly the **complex conjugate**: `q/α = ᾱ`. So
the Frobenius eigenvalues are Weil numbers on the circle of radius `√q`, closed
under conjugation, and in the spectral coordinate `α = q^ρ` the pairing
`α ↦ q/α` becomes `ρ ↦ 1 − ρ`. Its fixed locus under conjugation is
`Re(ρ) = 1/2`.

That is the classical picture, and stating it in the framework's own terms
answers a question the arc otherwise leaves open: the critical line is not a
fitted constant, it is where the functional equation's involution acts
trivially on real parts. -/

/-- **The pairing acts as `ρ ↦ 1 − ρ` on the spectral coordinate.** If
    `α = q^ρ` and `q/α = q^σ`, then `σ = 1 − ρ` — provided `q > 1`, so that the
    exponent is determined by its value up to the usual period.

    Stated on real parts, which is where it is unambiguous:
    `Re σ = 1 − Re ρ`. -/
theorem partner_re_eq_one_sub
    (q : ℝ) (hq : q > 1) (ρ σ : ℂ)
    (h : (q : ℂ) ^ σ = (q : ℂ) / (q : ℂ) ^ ρ) :
    σ.re = 1 - ρ.re := by
  have hq0 : (0 : ℝ) < q := by linarith
  have hlog : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  have hpow : ((q : ℂ) ^ ρ) ≠ 0 := by
    simpa using Complex.cpow_ne_zero_iff.mpr
      (Or.inl (Complex.ofReal_ne_zero.mpr (ne_of_gt hq0)))
  -- take norms: q^{Re σ} = q / q^{Re ρ} = q^{1 - Re ρ}
  have hn := congrArg (fun z : ℂ => ‖z‖) h
  simp only [norm_div, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hq0,
    abs_cpow_ofReal_eq_rpow_re q hq0] at hn
  -- hn : q ^ σ.re = q / q ^ ρ.re
  have hrw : q / q ^ ρ.re = q ^ (1 - ρ.re) := by
    rw [Real.rpow_sub hq0, Real.rpow_one]
  rw [hrw] at hn
  have hl := congrArg Real.log hn
  rw [Real.log_rpow hq0, Real.log_rpow hq0] at hl
  exact mul_right_cancel₀ hlog hl

/-- **The critical line is the fixed locus.** For `q > 1`, a spectral exponent
    has real part `1/2` exactly when it is fixed by the functional equation's
    involution `ρ ↦ 1 − ρ` on real parts.

    So `Re(ρ) = 1/2` is not a fitted constant: it is the unique vertical line on
    which `α ↦ q/α` acts trivially. -/
theorem critical_line_iff_fixed (ρ : ℂ) :
    ρ.re = 1 / 2 ↔ ρ.re = 1 - ρ.re := by
  constructor <;> intro h <;> linarith

/-- **Assembled.** Under the Hasse–Weil bound, every eigenvalue's spectral
    exponent is fixed by the functional-equation involution — the content of
    `spectral_half_line`, restated as the symmetry statement it is. -/
theorem spectral_half_line_is_fixed_locus
    (Z : LocalQZetaFunction) (hq : Z.q > 1) (ρ : Fin 8 → ℂ)
    (spectral_coord : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (ρ i))
    (hw : ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1 / 2 : ℝ)) :
    ∀ i, (ρ i).re = 1 - (ρ i).re := fun i =>
  (critical_line_iff_fixed (ρ i)).mp (spectral_half_line Z hq ρ spectral_coord hw i)

/-! ## The Reeb spectrum on the critical line

`spectral_half_line` concludes `Re(ρᵢ) = 1/2` for *any* exponents with
`αᵢ = q^{ρᵢ}`, and `exists_spectral_coord` shows such exponents always exist —
so on its own it is a statement about arbitrary complex numbers, not about the
Reeb derivation. `QOU.AlgebraicSubstrate.ReebSpectrum` supplies the missing
object and `HasReebSpectralCoords` the missing identification, as a named
hypothesis with no instance (bean `qou-qspc`).

With both, the arc's intended statement is available and is a theorem: **the
Reeb spectrum lies on the critical line**, conditional on the identification and
on the Hasse–Weil bound. The conditionality is visible in the type, which is the
point — the identification is unproved, and nothing here pretends otherwise. -/

/-- **The Reeb spectrum lies on the critical line.**

    This is what `cor:spectral-half-line` was always meant to say. What it said
    before was the same conclusion about unnamed exponents; the `ρ` here are the
    eigenvalues of an actual operator, carried by `R`.

    **The magnitude is now derived, not assumed.** This statement used to carry
    `(hw : ∀ i, ‖Z.eigenvalues i‖ = Z.q ^ (1/2))` as a hypothesis — the very fact
    `hasse_weil_bound` proves from `IsWeilZeta`, one file away, which this file
    could not reach because content-block siblings cannot import one another
    (§0a). Lifting the class into `QOU.AlgebraicSubstrate.WeilZeta` removed the
    duplication: `[IsWeilZeta Z]` replaces `hw`, and the Hasse–Weil bound is
    imported rather than re-assumed.

    So the result is now conditional on exactly two things, and it is worth being
    precise about their different standings:

    - `[IsWeilZeta Z]` — the two classical Weil inputs (functional equation,
      Castelnuovo–Severi). Cited results, and `weilZetaExample` witnesses that
      they are jointly satisfiable.
    - `[HasReebSpectralCoords Z R]` — the identification of the Frobenius
      exponents with the Reeb spectrum. **This is the open one** (bean
      `qou-qspc`); no instance exists, and `hasReebSpectralCoords_satisfiable`
      below shows only that the hypothesis is consistent, not that `ξ_q` meets
      it. -/
theorem reeb_spectrum_on_critical_line
    (Z : LocalQZetaFunction) (hq : Z.q > 1) [IsWeilZeta Z]
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R] :
    ∀ i, (R.spec i).re = 1 / 2 :=
  spectral_half_line Z hq R.spec HasReebSpectralCoords.coords
    (hasse_weil_bound Z)

/-- The same, as the symmetry statement: each Reeb eigenvalue is fixed by the
    functional equation's involution on real parts. -/
theorem reeb_spectrum_fixed_by_involution
    (Z : LocalQZetaFunction) (hq : Z.q > 1) [IsWeilZeta Z]
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R] :
    ∀ i, (R.spec i).re = 1 - (R.spec i).re := fun i =>
  (critical_line_iff_fixed (R.spec i)).mp
    (reeb_spectrum_on_critical_line Z hq R i)


/-! ## Is the hypothesis satisfiable?

`reeb_spectrum_on_critical_line` is conditional on `HasReebSpectralCoords`. A
conditional theorem is worthless if its hypothesis is unsatisfiable — that is
exactly the defect the `False`-proving axioms in `hasse-weil-bound.lean` had, and
the reason they were removed. `reebSpectrumExample` does **not** settle it: that
witness has every `spec i = 1`, which would force `αᵢ = q` for all `i`, false for
any `Z` with distinct eigenvalues.

So it is proved below, and the proof is a construction: diagonalise. -/

/-- The diagonal operator on `Fin 8 → ℂ` with entries `ρ`. -/
def diagOp (ρ : Fin 8 → ℂ) : (Fin 8 → ℂ) →ₗ[ℂ] (Fin 8 → ℂ) where
  toFun v := fun i => ρ i * v i
  map_add' := by intro x y; funext i; simp [mul_add]
  map_smul' := by intro c x; funext i; simp [Pi.smul_apply]; ring

/-- **The identification is a consistent hypothesis.** For every `Z` with `q > 1`
    there is a `ReebSpectrum` satisfying `HasReebSpectralCoords Z`.

    Hence `reeb_spectrum_on_critical_line` is not vacuously true: its hypothesis
    can be met.

    **What this does not establish**, and the distinction is the whole point:
    satisfiability says *some* operator has the Frobenius exponents as its
    spectrum — here a diagonal operator built from them, which is no more than
    bookkeeping. The arc's claim is that the framework's Reeb derivation `ξ_q` is
    such an operator. That is a statement about a *particular* operator and is
    untouched by this. What the result buys is the elimination of one way the arc
    could have been empty, and a sharper location for the open part: everything
    now rests on the choice of operator, nothing on the shape of the hypothesis. -/
theorem hasReebSpectralCoords_satisfiable (Z : LocalQZetaFunction) (hq : Z.q > 1) :
    ∃ R : ReebSpectrum (Fin 8 → ℂ), HasReebSpectralCoords Z R := by
  obtain ⟨ρ, hρ⟩ := exists_spectral_coord Z hq
  refine ⟨{ op := diagOp ρ
            mode := fun i => Pi.single i 1
            spec := ρ
            mode_ne_zero := ?_
            is_eigen := ?_ }, ⟨hρ⟩⟩
  · intro i hi
    have h1 := congrFun hi i
    simp at h1
  · intro i
    funext j
    by_cases hji : j = i
    · subst hji; simp [diagOp]
    · simp [diagOp, Pi.single_eq_of_ne hji]

/-! ## What the functional equation ALONE forces on the Reeb spectrum

`reeb_spectrum_on_critical_line` is the arc's target, and it consumes both Weil
inputs: the functional equation *and* Castelnuovo–Severi, the latter through
`hasse_weil_bound`. Castelnuovo–Severi is the deep one.

The two results below use **only the functional equation**, and say so in their
types — they take the permutation as an explicit argument rather than reaching
for `[IsWeilZeta Z]`, so a reader can see at a glance which half of the Weil
input is doing the work. That matters for a reason beyond tidiness: it isolates
a *cheap necessary condition* on the identification.

The identification `HasReebSpectralCoords` is open (`qou-qspc`). Anyone
proposing that the framework's `ξ_q` satisfies it now has something to check
that does not require establishing the Hasse–Weil bound first, and
`reeb_spectrum_sum_re` reduces that check to **one real number**. -/

/-- **The functional equation reflects the Reeb spectrum in the critical line.**

    Given the Weil pairing `α_{σ i} = q / αᵢ` as a permutation `σ`, the
    identification transports it to `Re ρ_{σ i} = 1 − Re ρᵢ`. So the multiset of
    real parts is symmetric about `1/2`.

    This is strictly weaker than `reeb_spectrum_on_critical_line`, and
    deliberately so: symmetry about the line is not the same as lying on it. A
    spectrum with real parts `{0.3, 0.7}` satisfies this and violates the
    critical line. Castelnuovo–Severi is what collapses the symmetry onto the
    fixed locus; `critical_line_iff_fixed` names that locus. -/
theorem reeb_spectrum_reflected_by_functional_equation
    (Z : LocalQZetaFunction) (hq : Z.q > 1)
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R]
    (σ : Equiv.Perm (Fin 8))
    (hσ : ∀ i, Z.eigenvalues (σ i) = (Z.q : ℂ) / Z.eigenvalues i) :
    ∀ i, (R.spec (σ i)).re = 1 - (R.spec i).re := by
  intro i
  refine partner_re_eq_one_sub Z.q hq (R.spec i) (R.spec (σ i)) ?_
  rw [← HasReebSpectralCoords.coords (Z := Z) (R := R) (σ i),
      ← HasReebSpectralCoords.coords (Z := Z) (R := R) i]
  exact hσ i

/-- **The Reeb spectrum has trace equal to the genus.** `∑ᵢ Re ρᵢ = 4`.

    Bring's curve has genus `g = 4`, and `LocalQZetaFunction` carries `2g = 8`
    eigenvalues — the `Fin 8` throughout this file. So the statement is
    `∑ Re ρᵢ = g`, and it is forced by the functional equation alone.

    **Why this is the useful form.** It follows from
    `reeb_spectrum_on_critical_line` too (eight halves make four), but that route
    needs Castelnuovo–Severi. Here the hypothesis is only the pairing, and the
    conclusion is a *single real number* computable from any candidate operator
    without diagonalising it in the complex plane: the trace of the Reeb
    derivation on the eight fundamental modes, real part, must be `4`.

    So it is a falsification test for `qou-qspc`'s open identification. If the
    framework's `ξ_q` has `∑ᵢ Re ρᵢ ≠ 4` on its eight modes, then no `IsWeilZeta`
    datum can satisfy `HasReebSpectralCoords` with that operator, and the
    identification is refuted — without ever touching the deep Weil input.

    It is of course only necessary, not sufficient: `{0.3, 0.7}` sums correctly
    and sits off the line. Scope-(a): passing this test is evidence, not a
    proof. -/
theorem reeb_spectrum_sum_re
    (Z : LocalQZetaFunction) (hq : Z.q > 1)
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R]
    (σ : Equiv.Perm (Fin 8))
    (hσ : ∀ i, Z.eigenvalues (σ i) = (Z.q : ℂ) / Z.eigenvalues i) :
    ∑ i, (R.spec i).re = 4 := by
  have hrefl := reeb_spectrum_reflected_by_functional_equation Z hq R σ hσ
  have hperm : ∑ i, (R.spec (σ i)).re = ∑ i, (R.spec i).re :=
    Equiv.sum_comp σ (fun i => (R.spec i).re)
  have key : ∑ i, (R.spec i).re = ∑ i : Fin 8, (1 - (R.spec i).re) := by
    rw [← hperm]
    exact Finset.sum_congr rfl (fun i _ => hrefl i)
  rw [Finset.sum_sub_distrib] at key
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul,
    Nat.cast_ofNat, mul_one] at key
  linarith

/-- The same two facts packaged for a datum that carries `[IsWeilZeta Z]`, which
    supplies the permutation. Convenience only — the content is above, and the
    explicit-`σ` forms are the ones that record which hypothesis was used. -/
theorem reeb_spectrum_sum_re_of_isWeilZeta
    (Z : LocalQZetaFunction) (hq : Z.q > 1) [IsWeilZeta Z]
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R] :
    ∑ i, (R.spec i).re = 4 := by
  obtain ⟨σ, hσ⟩ := IsWeilZeta.functional_equation (Z := Z)
  exact reeb_spectrum_sum_re Z hq R σ hσ

/-- **The whole chain is jointly satisfiable, and the trace really is 4.**

    `reeb_spectrum_sum_re` is conditional on three things at once — a Weil datum,
    a Reeb spectrum, and the identification between them. Each is separately
    known to be inhabited, which is *not* the same as their being jointly
    inhabited, and a theorem conditional on an unsatisfiable conjunction proves
    nothing.

    Here they are met together, on `weilZetaExample` (`q = 4`, every `αᵢ = 2`).
    That datum is supersingular: `|αᵢ| = 2 = √q`, so every spectral exponent is
    `log 2 / log 4 = 1/2` and the eight of them sum to `4`. The conclusion is
    therefore exhibited on a concrete case, not merely derived. -/
theorem reeb_spectrum_sum_re_witness :
    ∃ R : ReebSpectrum (Fin 8 → ℂ),
      ∃ _ : HasReebSpectralCoords weilZetaExample R,
        ∑ i, (R.spec i).re = 4 := by
  have hq : weilZetaExample.q > 1 := by norm_num [weilZetaExample]
  obtain ⟨R, hR⟩ := hasReebSpectralCoords_satisfiable weilZetaExample hq
  refine ⟨R, hR, ?_⟩
  haveI := hR
  exact reeb_spectrum_sum_re_of_isWeilZeta weilZetaExample hq R

/-- **The Weil pairing is an involution on the eigenvalues.** Applying
    `α ↦ q/α` twice returns `αᵢ`.

    Stated on the eigenvalues rather than on the permutation, because that is
    the form that is unconditionally true: `σ² = id` as a permutation needs the
    `αᵢ` to be *distinct* (a repeated eigenvalue lets `σ` permute its indices
    without moving any value), whereas `α_{σ²i} = αᵢ` holds always. The weaker
    statement is the honest one and is all the fixed-point result below uses. -/
theorem eigenvalue_functional_equation_involutive
    (Z : LocalQZetaFunction)
    (σ : Equiv.Perm (Fin 8))
    (hσ : ∀ i, Z.eigenvalues (σ i) = (Z.q : ℂ) / Z.eigenvalues i)
    (i : Fin 8) :
    Z.eigenvalues (σ (σ i)) = Z.eigenvalues i := by
  have hq : (Z.q : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt Z.q_pos)
  have hi : Z.eigenvalues i ≠ 0 := Z.eigenvalues_ne_zero i
  rw [hσ (σ i), hσ i]
  field_simp

/-- **A fixed point of the pairing lies ON the critical line — from the
    functional equation alone.**

    If the Weil involution fixes index `i`, then `Re ρᵢ = 1/2` exactly, with **no
    Castelnuovo–Severi input**. `reeb_spectrum_on_critical_line` gets the same
    conclusion for *every* `i`, but pays the deep Weil bound for it; this gets it
    for the fixed indices for free.

    Why that is worth stating separately. `critical_line_iff_fixed` already
    observes that `Re ρ = 1/2` is *equivalent* to being fixed by `ρ ↦ 1 − ρ`, but
    that is an identity about real numbers — it holds for any `ρ` whatsoever and
    says nothing about this spectrum. Here the fixed-ness is supplied by the
    Weil pairing itself, so the critical line stops being a value the spectrum is
    observed to have and becomes **the fixed locus of a symmetry the functional
    equation forces on it**.

    Concretely a fixed index means `αᵢ = q/αᵢ`, i.e. `αᵢ² = q` — the
    supersingular shape, `αᵢ = ±√q`. `weilZetaExample` is exactly this case at
    every index, which is why its permutation is `Equiv.refl`. -/
theorem reeb_spectrum_fixed_point_on_critical_line
    (Z : LocalQZetaFunction) (hq : Z.q > 1)
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R]
    (σ : Equiv.Perm (Fin 8))
    (hσ : ∀ i, Z.eigenvalues (σ i) = (Z.q : ℂ) / Z.eigenvalues i)
    (i : Fin 8) (hfix : σ i = i) :
    (R.spec i).re = 1 / 2 := by
  have h := reeb_spectrum_reflected_by_functional_equation Z hq R σ hσ i
  rw [hfix] at h
  linarith

/-- The eigenvalue form of the same fact: a fixed index has `αᵢ² = q`. Needs no
    Reeb spectrum and no identification — it is a statement about `Z` alone. -/
theorem eigenvalue_sq_eq_q_of_fixed
    (Z : LocalQZetaFunction)
    (σ : Equiv.Perm (Fin 8))
    (hσ : ∀ i, Z.eigenvalues (σ i) = (Z.q : ℂ) / Z.eigenvalues i)
    (i : Fin 8) (hfix : σ i = i) :
    Z.eigenvalues i ^ 2 = (Z.q : ℂ) := by
  have hi : Z.eigenvalues i ≠ 0 := Z.eigenvalues_ne_zero i
  have h := hσ i
  rw [hfix] at h
  field_simp at h
  linear_combination h

/-! ## Periodicity — the framework's OWN Reeb axiom, against the critical line

Everything above constrains the spectrum using Weil inputs only. The framework
carries an independent constraint on `ξ_q` that has never been set against them:
`QOU.AlgebraicSubstrate.CategoricalReebDerivation` has a field

    reeb_periodic : (reeb : End obj) ^ period = 1

so the Reeb derivation is **periodic**. Combining that with the critical line
pins the spectrum to two points, and the pinning is sharply falsifiable.

The periodicity is carried below as an explicit hypothesis on `R.op` rather than
imported from `CategoricalReebDerivation`: that structure's `reeb` is an
endomorphism of a monoidal-category object, and identifying it with a `ℂ`-linear
operator on an 8-dimensional space is precisely `qou-qspc`'s open problem. What
is proved here is the *consequence* of periodicity, available to any candidate
operator that has it. -/

/-- An eigenvector stays one under iteration: `op^n (modeᵢ) = specᵢ^n • modeᵢ`. -/
theorem reeb_spectrum_pow_apply
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H) (i : Fin 8) :
    ∀ n : ℕ, (R.op ^ n) (R.mode i) = (R.spec i) ^ n • R.mode i := by
  intro n
  induction n with
  | zero => simp
  | succ k ih =>
    -- `(f * g) v = f (g v)` is definitional for linear maps, so no lemma here.
    have hstep : (R.op ^ (k + 1)) (R.mode i) = (R.op ^ k) (R.op (R.mode i)) := by
      rw [pow_succ]; rfl
    rw [hstep, R.is_eigen i, map_smul, ih, smul_smul]
    congr 1
    ring

/-- **A periodic Reeb operator has root-of-unity eigenvalues.** If
    `op^Ω = id` then `specᵢ^Ω = 1`.

    This is where `mode_ne_zero` earns its place in the structure: without it the
    zero vector would satisfy the eigenvalue equation for every scalar and
    nothing could be concluded. -/
theorem reeb_spectrum_periodic_eigenvalue
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    (Ω : ℕ) (hper : R.op ^ Ω = LinearMap.id) (i : Fin 8) :
    (R.spec i) ^ Ω = 1 := by
  have h := reeb_spectrum_pow_apply R i Ω
  rw [hper] at h
  simp only [LinearMap.id_coe, id_eq] at h
  -- h : R.mode i = specᵢ^Ω • R.mode i
  have hz : ((R.spec i) ^ Ω - 1) • R.mode i = 0 := by
    rw [sub_smul, one_smul, ← h]; simp
  rcases smul_eq_zero.mp hz with hc | hm
  · linear_combination hc
  · exact absurd hm (R.mode_ne_zero i)

/-- Root-of-unity eigenvalues have modulus one (for a positive period). -/
theorem reeb_spectrum_norm_one_of_periodic
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    (Ω : ℕ) (hΩ : Ω ≠ 0) (hper : R.op ^ Ω = LinearMap.id) (i : Fin 8) :
    ‖R.spec i‖ = 1 :=
  Complex.norm_eq_one_of_pow_eq_one (reeb_spectrum_periodic_eigenvalue R Ω hper i) hΩ

/-- **The pinning.** A periodic Reeb operator whose spectrum realises the
    Frobenius exponents of a Weil datum has
    `Re ρᵢ = 1/2` *and* `(Im ρᵢ)² = 3/4` — that is, every `ρᵢ` is one of the two
    primitive sixth roots of unity `1/2 ± i√3/2`.

    **This is a sharply falsifiable consequence, and it is the point.** The two
    constraints are independent in origin — the real part comes from the Weil
    bound, the modulus from the framework's own `reeb_periodic` field — and
    together they leave the eight eigenvalues only **two** possible values. A
    genus-4 curve whose Frobenius eigenvalues are not all
    `q^{1/2 ± i√3/2}` therefore **refutes the conjunction**: either `ξ_q` is not
    the operator whose spectrum these are, or it is not periodic.

    Note this does not contradict Hasse–Weil, which it entails:
    `‖q^{ρᵢ}‖ = q^{Re ρᵢ} = √q` for either value.

    A corollary worth stating in words rather than Lean: since
    `1/2 ± i√3/2` are primitive **sixth** roots of unity, `specᵢ^Ω = 1` forces
    `6 ∣ Ω`. So the framework's Reeb period cannot be any natural number — the
    identification requires it to be a multiple of six. -/
theorem reeb_spectrum_pinned_by_periodicity
    (Z : LocalQZetaFunction) (hq : Z.q > 1) [IsWeilZeta Z]
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [HasReebSpectralCoords Z R]
    (Ω : ℕ) (hΩ : Ω ≠ 0) (hper : R.op ^ Ω = LinearMap.id) (i : Fin 8) :
    (R.spec i).re = 1 / 2 ∧ (R.spec i).im ^ 2 = 3 / 4 := by
  have hre : (R.spec i).re = 1 / 2 := reeb_spectrum_on_critical_line Z hq R i
  refine ⟨hre, ?_⟩
  have hn : ‖R.spec i‖ = 1 := reeb_spectrum_norm_one_of_periodic R Ω hΩ hper i
  have hsq : (R.spec i).re ^ 2 + (R.spec i).im ^ 2 = 1 := by
    have h1 : Complex.normSq (R.spec i) = 1 := by
      rw [← Complex.sq_norm, hn]; norm_num
    simpa [Complex.normSq_apply, sq] using h1
  rw [hre] at hsq
  linarith

end QOU.AlgebraicSubstrate
