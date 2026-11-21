import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.Topology.Algebra.InfiniteSum.Basic


/-!
# QOU.AlgebraicSubstrate.explicit_formula

The explicit formula: a spectral–geometric trace identity equating
the q-Chebyshev function (geometric side) to a sum over Reeb
eigenvalues (spectral side).

The proof decomposes into:
1. A Mellin-transform identity relating ψ_q to Z(B, t)
2. The partial-fraction decomposition of Z(B, t)⁻¹ via the eigenvalues
3. Contour integration (residue sum) producing the spectral terms

LaTeX: `\label{conj:explicit-formula}`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- A Reeb eigenvalue ρ in the spectrum of the Reeb derivation ξ_q.

**Widened to `ℂ` on 2026-08-29 (bean `qou-qspc`).** The field was `ℝ`, with the
docstring *"the eigenvalue ρ ∈ ℂ (represented here as ℝ for the real part)"* —
and `spectralSide` then used that real part *as the exponent*. That is not a
simplification, it is a different sum. In the classical explicit formula
`X^ρ = X^{1/2}·e^{iγ log X}` for `ρ = ½ + iγ`: the oscillation **is** the
imaginary part. Substituting `Re ρ` leaves `X^{1/2}`, which is monotone, so the
formalised spectral side could not oscillate while the `.md` promised that "each
eigenvalue `ρ` contributes a wave of amplitude `X^ρ/[ρ]_q`".

It also disagreed with the sibling `cor:spectral-half-line`, which quantifies
over `ρ : Fin 8 → ℂ` and concludes `Re(ρ) = 1/2` — a conclusion that would say
every eigenvalue *equals* ½ against a real spectrum. -/
structure ReebEigenvalue where
  /-- The eigenvalue ρ ∈ ℂ. -/
  val : ℂ

/-- The q-integer [ρ]_q = (q^ρ - q^{-ρ}) / (q - q^{-1}).

**Deliberately not consolidated onto `QOU.QInteger.qIntBal`** (`qou-qint`
census).  The index is a Reeb eigenvalue `ρ : ℝ` and the powers are `rpow`, so
this is the continuous-index bracket; the canonical `qIntBal` (ℕ) and
`qIntBalZ` (ℤ) are both discrete.  Distinct from the `JonesMarkovWenzl` case,
which merely *looked* continuous — there the `rpow`s were at half-integer
multiples of a `ℕ` index and did reduce to `qIntBal` at `q^{1/2}`.  Here `ρ`
ranges over a genuine spectrum, so no such reduction exists. -/
noncomputable def qInteger (q : ℝ) (_hq : 1 < q) (ρ : ℂ) : ℂ :=
  ((q : ℂ) ^ ρ - (q : ℂ) ^ (-ρ)) / ((q : ℂ) - (q : ℂ)⁻¹)

/-- The real-index q-integer, kept because its positivity is a genuine proved
    fact (`qIntegerReal_pos`) that the complex bracket cannot state. -/
noncomputable def qIntegerReal (q : ℝ) (_hq : 1 < q) (ρ : ℝ) : ℝ :=
  (q ^ ρ - q ^ (-ρ)) / (q - q⁻¹)

/-- The two brackets agree on a real index: `[ρ]_q` computed over `ℂ` at
    `(ρ : ℂ)` is the coercion of the real one. Keeps the widening honest —
    nothing about the real-index case changed. -/
theorem qInteger_ofReal (q : ℝ) (hq : 1 < q) (ρ : ℝ) :
    qInteger q hq (ρ : ℂ) = ((qIntegerReal q hq ρ : ℝ) : ℂ) := by
  have hq0 : (0 : ℝ) ≤ q := by linarith
  unfold qInteger qIntegerReal
  push_cast [← Complex.ofReal_cpow hq0]
  norm_num [Complex.ofReal_cpow hq0]

/-- The widening is not cosmetic: the type now admits an eigenvalue off the real
    axis, which is exactly what the oscillatory term needs and what the previous
    `val : ℝ` could not express. With `ρ = ½ + iγ` the classical term is
    `X^ρ = X^{1/2}·e^{iγ log X}`; at `γ = 0` it degenerates to the monotone
    `X^{1/2}` that the old spectral side computed for every eigenvalue. -/
theorem exists_offAxis_reebEigenvalue :
    ∃ ρ : ReebEigenvalue, ρ.val.im ≠ 0 :=
  ⟨⟨⟨1 / 2, 1⟩⟩, by norm_num⟩

/-- The q-logarithm ln_q(x) = ln(x) / ln(q). Well-defined for `q > 1`
    (so `Real.log q ≠ 0`); the positivity hypothesis is carried by the
    consumers rather than baked into the definition. -/
noncomputable def qLog (q : ℝ) (x : ℝ) : ℝ :=
  Real.log x / Real.log q

/-- The spectral side of the explicit formula: the oscillatory sum
    over Reeb eigenvalues plus constant and tail terms. -/
noncomputable def spectralSide
    (q : ℝ) (hq : 1 < q) (spectrum : List ReebEigenvalue)
    (Omega_q : ℝ) (X : ℝ) : ℂ :=
  (X : ℂ) - (spectrum.map fun ρ => (X : ℂ) ^ ρ.val / qInteger q hq ρ.val).sum
    - ((qLog q (2 * Real.pi * Omega_q) : ℝ) : ℂ)
    - (1 / 2) * ((qLog q (1 - X ^ (-2 : ℝ)) : ℝ) : ℂ)

/-- For q > 1, the q-integer [n]_q is positive for positive n. -/
theorem qIntegerReal_pos (q : ℝ) (hq : 1 < q) (ρ : ℝ) (hρ : 0 < ρ) :
    0 < qIntegerReal q hq ρ := by
  unfold qIntegerReal
  apply div_pos
  · -- q^ρ > q^{-ρ} when q > 1 and ρ > 0
    have hq_pos : (0 : ℝ) < q := by linarith
    exact sub_pos.mpr (Real.rpow_lt_rpow_of_exponent_lt hq (by linarith : -ρ < ρ))
  · -- q - q⁻¹ > 0 when q > 1
    have hq_pos : (0 : ℝ) < q := by linarith
    have : q⁻¹ < 1 := by rw [inv_lt_one₀ hq_pos]; exact hq
    linarith

/-! ### The `q → 1` limit of `qLog` — a refuted axiom (bean `qou-qexf`)

Until 2026-08-29 this file carried

```lean
axiom qLog_tendsto_log_axiom (x : ℝ) (hx : 0 < x) :
    Filter.Tendsto (fun q => qLog q x) (nhdsWithin 1 (Set.Ioi 1)) (nhds (Real.log x))
```

captioned *"External theorem (L'Hôpital, renormalised q-log limit)"*. **It proves
`False`**, and the reason is visible from the definition directly above: `qLog q x
= log x / log q`, and `log q → 0⁺` as `q → 1⁺`, so for `x ≠ 1` the quotient
diverges — it does not converge to `log x`.

The word *renormalised* in that caption was doing real work and pointing at the
right fact, which is `qLog_mul_log` below: the product `qLog q x · log q` is
*identically* `log x`, with no limit taken. What tends to `log x` as `q → 1` is
the Tsallis q-logarithm `(x^{1-q} − 1)/(1 − q)`, a different function; if the
framework needs that limiting behaviour it needs that definition, not this one.

Both facts are now theorems rather than a false assumption. -/

/-- **The exact renormalisation identity.** For `q > 1`, `qLog q x · log q = log x`
    — no limit involved. This is what the withdrawn axiom's "renormalised" caption
    was gesturing at, and unlike the limit claim it is true. -/
theorem qLog_mul_log (q : ℝ) (hq : 1 < q) (x : ℝ) :
    qLog q x * Real.log q = Real.log x := by
  have hne : Real.log q ≠ 0 := ne_of_gt (Real.log_pos hq)
  rw [qLog, div_mul_cancel₀ _ hne]

/-- **Refutation of the withdrawn axiom.** `qLog q x` does *not* tend to `log x`
    as `q → 1⁺`. Reported as a proved negative per Strict Lean Discipline §10
    rather than left as a docstring caveat.

    The witness is `x = 2`: if the limit held, multiplying by `log q → 0` would
    force `log 2 = 0`, since `qLog q 2 · log q` is identically `log 2`. -/
theorem not_qLog_tendsto_log :
    ¬ (∀ x : ℝ, 0 < x →
        Filter.Tendsto (fun q => qLog q x)
          (nhdsWithin 1 (Set.Ioi 1)) (nhds (Real.log x))) := by
  intro h
  have h1 := h 2 (by norm_num)
  have hc : Filter.Tendsto Real.log (nhdsWithin (1:ℝ) (Set.Ioi 1)) (nhds 0) := by
    have hl := (Real.continuousAt_log (by norm_num : (1:ℝ) ≠ 0)).tendsto
    rw [Real.log_one] at hl
    exact hl.mono_left nhdsWithin_le_nhds
  have hp := h1.mul hc
  have heq : (fun q => qLog q 2 * Real.log q) =ᶠ[nhdsWithin (1:ℝ) (Set.Ioi 1)]
      (fun _ => Real.log 2) := by
    filter_upwards [self_mem_nhdsWithin] with q hq
    exact qLog_mul_log q hq 2
  have huniq : Real.log 2 * 0 = Real.log 2 :=
    tendsto_nhds_unique (Filter.Tendsto.congr' heq hp) tendsto_const_nhds
  rw [mul_zero] at huniq
  exact absurd huniq.symm (ne_of_gt (Real.log_pos (by norm_num)))

/-- A maximal ideal of the coordinate ring in the geometric (ℝ)
    realisation: it carries a real norm N(𝔪) (residue-field
    cardinality) and a flag marking fundamental defects. The Laurent
    `R_q` form lives in the sibling `q-von-mangoldt-function`; here we
    work over ℝ for the analytic explicit-formula side. -/
structure MaxIdeal where
  /-- The norm N(𝔪) — cardinality of the residue field. -/
  norm : ℝ
  /-- Whether this ideal corresponds to a fundamental defect. -/
  isFundamental : Bool

/-- The q-von Mangoldt weight of a maximal ideal: for a fundamental
    defect with norm N(𝔪), `(N(𝔪)^ℏ_q − 1)/ℏ_q`; otherwise `0`. -/
noncomputable def QVonMangoldtFunction (hbar_q : ℝ) (_hbar_pos : 0 < hbar_q)
    (m : MaxIdeal) : ℝ :=
  if m.isFundamental then (m.norm ^ hbar_q - 1) / hbar_q else 0

open Classical in
/-- The q-Chebyshev function ψ_q(X): the sum of the q-von Mangoldt
    weights over all maximal ideals with norm `N(𝔪) ≤ X`. The norm
    cutoff `N(𝔪) ≤ X` is a real comparison, decided classically. -/
noncomputable def QChebyshevFunction
    (hbar_q : ℝ) (hbar_pos : 0 < hbar_q)
    (ideals : List MaxIdeal) (X : ℝ) : ℝ :=
  (ideals.map
    (fun m => if m.norm ≤ X then QVonMangoldtFunction hbar_q hbar_pos m else 0)).sum

/-! ### The explicit formula — a refuted axiom, restated as a conjecture (bean `qou-qexf`)

Until 2026-08-29 this file carried `explicit_formula_axiom`, quantified over
`ideals` and `spectrum` **independently**, and `theorem explicit_formula` was its
projection. **It proves `False`**, by the same shape as the two Hasse–Weil axioms
(`qou-hwax`): an identity asserted for every pair of unrelated data. The
geometric side is determined by `ideals`, the spectral side by `spectrum`, and
nothing tied them together — so the empty datum with `Ω_q = 1/(2π)` gives `0` on
the left and `2 + (positive)` on the right. Machine-checked;
`not_qExplicitFormula_empty` below is that counterexample, kept as a theorem so
the universal form cannot be reinstated by accident.

The identity is stated instead for a single `QZetaDatum` — the ideals and the
Reeb spectrum of *one* geometry — as a §3b conjecture class with **no instance**.
**And no instance can exist**: `not_qExplicitFormula` proves the class
uninhabitable for every datum, so `explicit_formula` below is a conditional whose
hypothesis nothing satisfies — see that theorem for why this refutes the
finite-`List` formalisation and not the mathematics.

**On the citation.** The withdrawn axiom was captioned *"External theorem (Rosen
2002 Ch 5 Thm 5.12; Weil 1948; Reshetikhin–Turaev 1991)"*. Rosen Thm 5.12 is the
explicit formula for the zeta function of a curve over `𝔽_q`; the identity here
is its **q-deformation**, and `[ρ]_q`, `ln_q` and the `Ω_q` term are the
framework's own constructions, appearing in none of the three works. The
citation is withdrawn and replaced by `[leitner2026]`, per the disposition
`qou-rhax` required for the same defect. -/

/-- The data of one q-zeta geometry: its parameters, its maximal ideals, and its
    Reeb spectrum. Bundling them is the point — the explicit formula relates the
    two lists *of the same geometry*, and quantifying over them separately is
    what made the withdrawn axiom false. -/
structure QZetaDatum where
  /-- The deformation parameter. -/
  q : ℝ
  /-- `q > 1`. -/
  hq : 1 < q
  /-- The infinitesimal `ℏ_q`. -/
  hbar_q : ℝ
  /-- `ℏ_q > 0`. -/
  hbar_pos : 0 < hbar_q
  /-- The maximal ideals (the geometric side). -/
  ideals : List MaxIdeal
  /-- The Reeb spectrum (the spectral side). -/
  spectrum : List ReebEigenvalue
  /-- The constant `Ω_q`. -/
  Omega_q : ℝ
  /-- `Ω_q > 0`. -/
  Omega_pos : 0 < Omega_q

/-- **Conjecture (q-explicit formula).** For the datum `D`, the q-Chebyshev
    function equals the spectral expansion:

    `ψ_q(X) = X − Σ_{ρ ∈ Spec(ξ_q)} X^ρ/[ρ]_q − ln_q(2πΩ_q) − ½ ln_q(1 − X^{−2})`

    The intended proof route is a Mellin-transform identity relating `ψ_q` to the
    local zeta function `Z(B, t)`, then contour integration of `−Z'/Z`, each pole
    at `α_i = q^{ρ_i}` contributing `X^{ρ_i}/[ρ_i]_q`. That route is not carried
    out anywhere in the corpus.

    **No instance is provided — that is the honest open state** (§3b). Note that
    the class is *not* satisfiable for every datum: `not_qExplicitFormula_empty`
    exhibits one it fails on, so any future instance must come with the side
    conditions that make `ideals` and `spectrum` the two faces of one geometry. -/
-- Ref: [leitner2026] Ch. 8 §explicit-formula
class QExplicitFormula (D : QZetaDatum) : Prop where
  /-- The identity, at every `X > 1`. -/
  formula : ∀ X : ℝ, 1 < X →
    ((QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X : ℝ) : ℂ) =
      spectralSide D.q D.hq D.spectrum D.Omega_q X

/-- The explicit formula holds for a datum satisfying the conjecture. Conditional
    on `[QExplicitFormula D]` (§3b-cond) — the hypothesis is visible in the type
    rather than assumed globally. -/
theorem explicit_formula (D : QZetaDatum) [QExplicitFormula D] (X : ℝ) (hX : 1 < X) :
    ((QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X : ℝ) : ℂ) =
      spectralSide D.q D.hq D.spectrum D.Omega_q X :=
  QExplicitFormula.formula X hX

/-- **The counterexample that refutes the universal form.** With no ideals, no
    spectrum, and `Ω_q = 1/(2π)`, the geometric side is `0` while the spectral
    side is `2 − ½·ln_q(3/4) > 0`. Kept as a theorem so the withdrawn axiom
    cannot be reinstated without tripping over it. -/
theorem not_qExplicitFormula_empty :
    ¬ QExplicitFormula ⟨2, by norm_num, 1, by norm_num, [], [],
        1 / (2 * Real.pi), by positivity⟩ := by
  intro hinst
  have h := hinst.formula 2 (by norm_num)
  rw [QChebyshevFunction, spectralSide] at h
  simp only [List.map_nil, List.sum_nil] at h
  have h1 : 2 * Real.pi * (1 / (2 * Real.pi)) = 1 := by
    have := Real.pi_pos; field_simp
  rw [h1] at h
  have h2 : qLog 2 1 = 0 := by simp [qLog]
  rw [h2] at h
  have h3 : (2:ℝ) ^ (-2 : ℝ) = 1/4 := by
    rw [show (-2:ℝ) = ((-2 : ℤ) : ℝ) by norm_num, Real.rpow_intCast]; norm_num
  rw [h3] at h
  have hlog34 : Real.log (1 - 1/4 : ℝ) < 0 := by
    rw [show (1 - 1/4 : ℝ) = 3/4 by norm_num]
    exact Real.log_neg (by norm_num) (by norm_num)
  have hq34 : qLog 2 (1 - 1/4 : ℝ) < 0 :=
    div_neg_of_neg_of_pos hlog34 (Real.log_pos (by norm_num))
  -- the identity is now an equation in ℂ, but every term is a real coercion,
  -- so injectivity of `Complex.ofReal` returns it to ℝ.
  have hre := congrArg Complex.re h
  simp at hre
  nlinarith [hre, hq34]

/-! ### The class is uninhabitable for an empty spectrum — and why (bean `qou-qexu`)

`not_qExplicitFormula_empty` above refutes **one** datum. That is weaker than it
looks, and the gap matters: a class refuted on one instance may still be
satisfiable on another, and a conditional theorem over it is only worthless if
**no** instance exists. So the satisfiability question has to be asked
separately — the lesson recorded on this branch as *"exhibit a witness of the
thing the conditional theorems actually depend on"*, here applied in the
negative direction.

Asked, the answer is that the identity fails for **every** datum with an empty
spectrum, whatever its ideals, `Ω_q` and `q`. The mechanism:

* `ψ_q(X)` is a sum over a **finite** `List MaxIdeal` whose terms are switched on
  and off by `N(𝔪) ≤ X`, never grown — so it is bounded uniformly in `X`, by the
  total of the weights' magnitudes.
* `−½·ln_q(1 − X^{−2})` **diverges to `+∞` as `X → 1⁺`**, since `1 − X^{−2} → 0⁺`
  and `log q > 0`.

A bounded function cannot equal an unbounded one, so no such datum satisfies the
class.

**This is a defect in the formalisation, not in the mathematics**, and the
diagnosis is worth stating precisely because it says what a repair must do. The
classical explicit formula carries the *same* `−½ log(1 − x^{−2})` term, and it
is true — because there the spectral sum runs over **infinitely many** zeros and
is only conditionally convergent. That term is itself the closed form of the
trivial-zero series, and its blow-up near `x = 1` is cancelled by the divergence
of the non-trivial-zero sum. Pairing it against a **finite** `List` cannot
reproduce that cancellation.

So a faithful carrier needs the spectral side to be an infinite sum with a
specified summation order, not a `List`. Until it has one, `explicit_formula` is
a conditional whose hypothesis nothing can satisfy in the empty-spectrum case,
and the general case is `qou-qexu`. -/

/-- `ψ_q` is bounded uniformly in `X`: a finite sum whose terms are switched on
    and off, never grown. -/
theorem qChebyshev_abs_le (hbar : ℝ) (hpos : 0 < hbar)
    (ideals : List MaxIdeal) (X : ℝ) :
    |QChebyshevFunction hbar hpos ideals X|
      ≤ (ideals.map fun m => |QVonMangoldtFunction hbar hpos m|).sum := by
  unfold QChebyshevFunction
  induction ideals with
  | nil => simp
  | cons a t ih =>
    simp only [List.map_cons, List.sum_cons]
    have hstep : |if a.norm ≤ X then QVonMangoldtFunction hbar hpos a else 0|
        ≤ |QVonMangoldtFunction hbar hpos a| := by
      by_cases h : a.norm ≤ X <;> simp [h]
    calc |(if a.norm ≤ X then QVonMangoldtFunction hbar hpos a else 0)
            + (t.map fun m => if m.norm ≤ X then QVonMangoldtFunction hbar hpos m else 0).sum|
        ≤ |if a.norm ≤ X then QVonMangoldtFunction hbar hpos a else 0|
            + |(t.map fun m => if m.norm ≤ X then QVonMangoldtFunction hbar hpos m else 0).sum| :=
          abs_add_le _ _
      _ ≤ |QVonMangoldtFunction hbar hpos a|
            + (t.map fun m => |QVonMangoldtFunction hbar hpos m|).sum := by linarith

/-- The trivial-zero tail term is **unbounded** as `X → 1⁺`: for every bound `B`
    there is an `X > 1` on which it exceeds `B`.

    Constructed rather than obtained as a limit: `X := 1/√(1−ε)` gives
    `1 − X^{−2} = ε` exactly, so choosing `ε ≤ q^{−2B}` makes the term at least
    `B`. Taking `ε ≤ 1/2` as well keeps `X ≤ √2`, which is what lets the
    *bounded* side of the identity be bounded by a constant. -/
theorem tail_term_unbounded (q : ℝ) (hq : 1 < q) (B : ℝ) :
    ∃ X : ℝ, 1 < X ∧ X ≤ Real.sqrt 2 ∧ B ≤ -(1 / 2) * qLog q (1 - X ^ (-2 : ℝ)) := by
  have hlogq : 0 < Real.log q := Real.log_pos hq
  set ε : ℝ := min (1 / 2) (q ^ (-(2 * B))) with hε
  have hqpos : (0:ℝ) < q := lt_trans one_pos hq
  have hεpos : 0 < ε := lt_min (by norm_num) (Real.rpow_pos_of_pos hqpos _)
  have hεhalf : ε ≤ 1 / 2 := min_le_left _ _
  have hone : (0:ℝ) < 1 - ε := by linarith
  set y : ℝ := Real.sqrt (1 - ε) with hy
  have hypos : 0 < y := Real.sqrt_pos.mpr hone
  have hysq : y ^ 2 = 1 - ε := Real.sq_sqrt hone.le
  refine ⟨1 / y, ?_, ?_, ?_⟩
  · -- 1 < 1/y  because y < 1
    have hylt : y < 1 := by nlinarith [hysq, hypos]
    rw [lt_div_iff₀ hypos]; linarith
  · -- 1/y ≤ √2  because y ≥ 1/√2, i.e. y² ≥ 1/2
    have h2 : (1:ℝ)/2 ≤ y ^ 2 := by rw [hysq]; linarith
    have hs2 : Real.sqrt 2 > 0 := Real.sqrt_pos.mpr (by norm_num)
    rw [div_le_iff₀ hypos]
    nlinarith [h2, hypos, Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num), hs2]
  · -- the bound itself
    have hx2 : (1 / y) ^ (-2 : ℝ) = 1 - ε := by
      rw [show (-2:ℝ) = -(2:ℕ) by norm_num,
        Real.rpow_neg (by positivity), Real.rpow_natCast, div_pow, one_pow, hysq,
        one_div, inv_inv]
    rw [hx2, show (1:ℝ) - (1 - ε) = ε by ring, qLog]
    have hle : ε ≤ q ^ (-(2 * B)) := min_le_right _ _
    have hlog : Real.log ε ≤ -(2 * B) * Real.log q := by
      calc Real.log ε ≤ Real.log (q ^ (-(2 * B))) := Real.log_le_log hεpos hle
        _ = -(2 * B) * Real.log q := Real.log_rpow hqpos _
    have hdiv : Real.log ε / Real.log q ≤ -(2 * B) := by
      rw [div_le_iff₀ hlogq]; linarith [hlog]
    linarith [hdiv]

/-- **The class is uninhabitable for an empty spectrum.** For *every* datum with
    `spectrum = []` — any ideals, any `Ω_q`, any `q > 1` — the identity fails.

    Strictly stronger than `not_qExplicitFormula_empty`, which refutes one datum.
    A class refuted on one instance may still be satisfiable on another; this
    says no empty-spectrum datum satisfies it at all, so over that whole family
    `explicit_formula` is a conditional whose hypothesis nothing meets.

    The proof is the bounded-vs-unbounded argument: `qChebyshev_abs_le` bounds
    the geometric side by a constant of the datum, `tail_term_unbounded` puts the
    tail term above that constant at some `X ∈ (1, √2]`, and `X ≤ √2 < 2` keeps
    the remaining terms small enough that the two cannot meet.

    **Subsumed by `not_qExplicitFormula`**, which drops the `spectrum = []`
    hypothesis entirely. Kept because its proof is this argument without the
    spectral-sum bound, which is where the idea is easiest to read. -/
theorem not_qExplicitFormula_of_nil_spectrum (D : QZetaDatum) (hs : D.spectrum = []) :
    ¬ QExplicitFormula D := by
  intro hinst
  set M : ℝ := (D.ideals.map fun m => |QVonMangoldtFunction D.hbar_q D.hbar_pos m|).sum with hM
  set c : ℝ := qLog D.q (2 * Real.pi * D.Omega_q) with hc
  obtain ⟨X, hX1, hX2, hXb⟩ := tail_term_unbounded D.q D.hq (M + |c| + 2)
  have h := hinst.formula X hX1
  rw [spectralSide, hs] at h
  simp only [List.map_nil, List.sum_nil, sub_zero] at h
  -- every term is a real coercion, so the identity returns to ℝ by injectivity
  have hre : QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X
      = X - qLog D.q (2 * Real.pi * D.Omega_q)
        - (1 / 2) * qLog D.q (1 - X ^ (-2 : ℝ)) := by
    have hc2 : ((QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X : ℝ) : ℂ)
        = ((X - qLog D.q (2 * Real.pi * D.Omega_q)
            - (1 / 2) * qLog D.q (1 - X ^ (-2 : ℝ)) : ℝ) : ℂ) := by
      rw [h]; push_cast; ring
    exact_mod_cast hc2
  -- the geometric side is bounded by M
  have hbdd : |QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X| ≤ M :=
    qChebyshev_abs_le _ _ _ _
  have hXlt2 : X < 2 := by
    have : Real.sqrt 2 < 2 := by
      nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num),
        Real.sqrt_nonneg 2]
    linarith
  have habs := abs_le.mp hbdd
  linarith [hXb, habs.2, hX1, le_abs_self c]

/-! ### The general case: uninhabitable for ANY finite spectrum (bean `qou-qexu`)

`not_qExplicitFormula_of_nil_spectrum` covers the empty spectrum. The same
argument covers a **nonempty finite** one, because on `X ∈ (1, √2]` the spectral
sum is a finite sum of terms whose norms are bounded by a constant of the datum:
`‖(X:ℂ)^ρ‖ = X^{Re ρ}`, and `X ≤ √2` caps that.

The bounding constant is deliberately crude — `√2 ^ |Re ρ|` per term, which
dominates `X ^ Re ρ` for every `X ∈ (1, √2]` whatever the sign of `Re ρ`. It does
not need to be sharp; it only needs to be independent of `X`, because the whole
argument is bounded-versus-unbounded.

Note `[ρ]_q = 0` is not an obstacle and must not be assumed away: at `ρ = 0` the
bracket vanishes, and Lean's `x / 0 = 0` makes that term `0`, which the bound
covers. A proof assuming `[ρ]_q ≠ 0` would be both unnecessary and false. -/

/-- Each spectral term is bounded on `(1, √2]` by a constant of the eigenvalue,
    independent of `X`. Crude by design — only `X`-independence matters. -/
theorem spectral_term_norm_le (q : ℝ) (hq : 1 < q) (ρ : ReebEigenvalue)
    (X : ℝ) (hX1 : 1 < X) (hX2 : X ≤ Real.sqrt 2) :
    ‖(X : ℂ) ^ ρ.val / qInteger q hq ρ.val‖
      ≤ Real.sqrt 2 ^ |ρ.val.re| / ‖qInteger q hq ρ.val‖ := by
  have hX0 : (0:ℝ) < X := lt_trans one_pos hX1
  have hs2 : (1:ℝ) ≤ Real.sqrt 2 := by
    nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num), Real.sqrt_nonneg 2]
  -- the numerator bound, whatever the sign of Re ρ
  have hnum : X ^ ρ.val.re ≤ Real.sqrt 2 ^ |ρ.val.re| := by
    rcases le_or_gt 0 ρ.val.re with hs | hs
    · calc X ^ ρ.val.re ≤ Real.sqrt 2 ^ ρ.val.re := Real.rpow_le_rpow hX0.le hX2 hs
        _ = Real.sqrt 2 ^ |ρ.val.re| := by rw [abs_of_nonneg hs]
    · have h1 : X ^ ρ.val.re ≤ 1 := Real.rpow_le_one_of_one_le_of_nonpos hX1.le hs.le
      have h2 : (1:ℝ) ≤ Real.sqrt 2 ^ |ρ.val.re| := Real.one_le_rpow hs2 (abs_nonneg _)
      linarith
  rw [norm_div, Complex.norm_cpow_eq_rpow_re_of_pos hX0]
  gcongr

/-- The whole spectral sum is bounded on `(1, √2]` by a constant of the datum. -/
theorem spectralSum_norm_le (q : ℝ) (hq : 1 < q) (spectrum : List ReebEigenvalue)
    (X : ℝ) (hX1 : 1 < X) (hX2 : X ≤ Real.sqrt 2) :
    ‖(spectrum.map fun ρ => (X : ℂ) ^ ρ.val / qInteger q hq ρ.val).sum‖
      ≤ (spectrum.map fun ρ =>
          Real.sqrt 2 ^ |ρ.val.re| / ‖qInteger q hq ρ.val‖).sum := by
  induction spectrum with
  | nil => simp
  | cons a t ih =>
    simp only [List.map_cons, List.sum_cons]
    calc ‖(X : ℂ) ^ a.val / qInteger q hq a.val
            + (t.map fun ρ => (X : ℂ) ^ ρ.val / qInteger q hq ρ.val).sum‖
        ≤ ‖(X : ℂ) ^ a.val / qInteger q hq a.val‖
            + ‖(t.map fun ρ => (X : ℂ) ^ ρ.val / qInteger q hq ρ.val).sum‖ :=
          norm_add_le _ _
      _ ≤ Real.sqrt 2 ^ |a.val.re| / ‖qInteger q hq a.val‖
            + (t.map fun ρ => Real.sqrt 2 ^ |ρ.val.re| / ‖qInteger q hq ρ.val‖).sum := by
          have := spectral_term_norm_le q hq a X hX1 hX2
          linarith

/-- **`QExplicitFormula` is uninhabitable — for every datum, no exceptions.**

    The finite-`List` formalisation of the q-explicit formula is satisfied by no
    `QZetaDatum` whatsoever: any ideals, any spectrum, any `Ω_q`, any `q > 1`.

    Bounded versus unbounded, as in the empty-spectrum case: `ψ_q` is bounded by
    `qChebyshev_abs_le`, the spectral sum by `spectralSum_norm_le`, and the tail
    term exceeds their total somewhere in `(1, √2]` by `tail_term_unbounded`.

    **This refutes the formalisation, not the mathematics** — see the section note
    above `not_qExplicitFormula_of_nil_spectrum`. The classical explicit formula
    carries the same `−½log(1−x^{−2})` term and is true, because its spectral sum
    is infinite and only conditionally convergent; that term is the closed form of
    the trivial-zero series and its blow-up at `x = 1` is cancelled by the
    divergence of the non-trivial-zero sum. **A finite `List` cannot do that**, and
    this theorem is the precise statement of why. A faithful carrier needs the
    spectral side to be an infinite sum with a specified summation order. -/
theorem not_qExplicitFormula (D : QZetaDatum) : ¬ QExplicitFormula D := by
  intro hinst
  set M : ℝ := (D.ideals.map fun m => |QVonMangoldtFunction D.hbar_q D.hbar_pos m|).sum with hM
  set S : ℝ := (D.spectrum.map fun ρ =>
    Real.sqrt 2 ^ |ρ.val.re| / ‖qInteger D.q D.hq ρ.val‖).sum with hS
  set c : ℝ := qLog D.q (2 * Real.pi * D.Omega_q) with hc
  obtain ⟨X, hX1, hX2, hXb⟩ := tail_term_unbounded D.q D.hq (M + S + |c| + 2)
  have h := hinst.formula X hX1
  rw [spectralSide] at h
  -- real part of the identity, with the spectral sum kept as a complex term
  set T : ℂ := (D.spectrum.map fun ρ => (X : ℂ) ^ ρ.val / qInteger D.q D.hq ρ.val).sum with hT
  have hTb : ‖T‖ ≤ S := spectralSum_norm_le D.q D.hq D.spectrum X hX1 hX2
  have hre : QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X
      = X - T.re - c - (1 / 2) * qLog D.q (1 - X ^ (-2 : ℝ)) := by
    have := congrArg Complex.re h
    simpa [hT, hc, Complex.sub_re, Complex.ofReal_re, Complex.mul_re, Complex.ofReal_im]
      using this
  have hbdd := abs_le.mp (qChebyshev_abs_le D.hbar_q D.hbar_pos D.ideals X)
  have hTre : |T.re| ≤ S := le_trans (Complex.abs_re_le_norm T) hTb
  have hTre' := abs_le.mp hTre
  linarith [hXb, hbdd.2, hX1, le_abs_self c, hTre'.1, hTre'.2]

/-! ### Toward a faithful carrier: an ordered infinite spectrum (bean `qou-qexu`)

`not_qExplicitFormula` names the repair: the spectral side must be an **infinite**
sum with a **specified summation order**, read as the limit of its ordered
partial sums. `QExplicitFormulaSeq` below is that carrier, with the spectrum an
`ℕ`-indexed sequence and the identity asserted as convergence of the partial
spectral sides. **No instance is provided — the honest open state (§3b).**

What *is* proved is a necessary condition any instance must meet, and it is the
precise form of the classical cancellation mechanism. On `X ∈ (1, √2]` the
ordered partial spectral sums must be **unbounded** (`partialSpectral_unbounded`):
the tail term `−½·ln_q(1 − X^{−2})` blows up as `X → 1⁺` while `ψ_q` stays
bounded, so the spectral sum has to blow up with it. A uniformly bounded ordered
spectrum is therefore excluded (`not_qExplicitFormulaSeq_of_bounded`), and in
particular any spectrum dominated by the summable majorant
`√2^{|Re ρ_n|}/‖[ρ_n]_q‖` is excluded (`not_qExplicitFormulaSeq_of_summable`).
So an instance, if one exists, needs a spectrum whose sum converges for each
fixed `X > 1` but **not uniformly** near `X = 1` — conditional, order-dependent
convergence is forced, not merely permitted. This constrains the carrier; it
does not decide whether it is inhabited. -/

/-- A q-zeta datum whose Reeb spectrum is an ordered sequence rather than a
    finite list. The order is part of the data: the identity below is a limit of
    partial sums taken in this order. -/
structure QZetaDatumSeq where
  /-- The deformation parameter. -/
  q : ℝ
  /-- `q > 1`. -/
  hq : 1 < q
  /-- The infinitesimal `ℏ_q`. -/
  hbar_q : ℝ
  /-- `ℏ_q > 0`. -/
  hbar_pos : 0 < hbar_q
  /-- The maximal ideals (the geometric side). -/
  ideals : List MaxIdeal
  /-- The Reeb spectrum, in its summation order. -/
  spectrum : ℕ → ReebEigenvalue
  /-- The constant `Ω_q`. -/
  Omega_q : ℝ
  /-- `Ω_q > 0`. -/
  Omega_pos : 0 < Omega_q

/-- The `N`-th ordered partial spectral side: the finite spectral side of the
    first `N` eigenvalues, in the datum's order. -/
noncomputable def QZetaDatumSeq.partialSide (D : QZetaDatumSeq) (N : ℕ) (X : ℝ) : ℂ :=
  spectralSide D.q D.hq ((List.range N).map D.spectrum) D.Omega_q X

/-- The `N`-th ordered partial spectral sum `Σ_{n<N} X^{ρ_n}/[ρ_n]_q`. -/
noncomputable def QZetaDatumSeq.partialSum (D : QZetaDatumSeq) (N : ℕ) (X : ℝ) : ℂ :=
  (((List.range N).map D.spectrum).map
    fun ρ => (X : ℂ) ^ ρ.val / qInteger D.q D.hq ρ.val).sum

/-- **Conjecture (q-explicit formula, ordered-infinite-spectrum carrier).** For
    every `X > 1` the ordered partial spectral sides converge to `ψ_q(X)`.

    No instance is provided. Unlike `QExplicitFormula`, this class is not refuted
    by any theorem in this file; what is proved is the necessary condition
    `partialSpectral_unbounded`. -/
-- Ref: [leitner2026] Ch. 8 §explicit-formula
class QExplicitFormulaSeq (D : QZetaDatumSeq) : Prop where
  /-- The identity, as a limit of ordered partial sums, at every `X > 1`. -/
  formula : ∀ X : ℝ, 1 < X →
    Filter.Tendsto (fun N => D.partialSide N X) Filter.atTop
      (nhds ((QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X : ℝ) : ℂ))

/-- **Necessary condition.** If the ordered-spectrum explicit formula holds for
    `D`, then the ordered partial spectral sums are unbounded on `(1, √2]`: for
    every `C` there are `X ∈ (1, √2]` and `N` with `‖Σ_{n<N} X^{ρ_n}/[ρ_n]_q‖ > C`.

    Conditional on `[QExplicitFormulaSeq D]` (§3b-cond). The proof is the
    bounded-versus-unbounded argument of `not_qExplicitFormula`, run against the
    limit: if every partial sum were bounded by `C`, the real part of every
    partial side would exceed `ψ_q`'s bound at the `X` supplied by
    `tail_term_unbounded`, and so would the limit. -/
theorem partialSpectral_unbounded (D : QZetaDatumSeq) [hinst : QExplicitFormulaSeq D]
    (C : ℝ) : ∃ X : ℝ, 1 < X ∧ X ≤ Real.sqrt 2 ∧ ∃ N : ℕ, C < ‖D.partialSum N X‖ := by
  by_contra hcon
  push_neg at hcon
  set M : ℝ := (D.ideals.map fun m => |QVonMangoldtFunction D.hbar_q D.hbar_pos m|).sum
    with hM
  set c : ℝ := qLog D.q (2 * Real.pi * D.Omega_q) with hc
  obtain ⟨X, hX1, hX2, hXb⟩ := tail_term_unbounded D.q D.hq (M + C + |c| + 2)
  have hlim := (Complex.continuous_re.tendsto _).comp (hinst.formula X hX1)
  have hbdd := abs_le.mp (qChebyshev_abs_le D.hbar_q D.hbar_pos D.ideals X)
  -- every partial side has real part at least `M + 1`
  have hlow : ∀ N : ℕ, M + 1 ≤ (D.partialSide N X).re := by
    intro N
    have hTb : ‖D.partialSum N X‖ ≤ C := hcon X hX1 hX2 N
    have hTre := abs_le.mp (le_trans (Complex.abs_re_le_norm (D.partialSum N X)) hTb)
    have hre : (D.partialSide N X).re
        = X - (D.partialSum N X).re - c - (1 / 2) * qLog D.q (1 - X ^ (-2 : ℝ)) := by
      simp [QZetaDatumSeq.partialSide, QZetaDatumSeq.partialSum, spectralSide, hc,
        Complex.sub_re, Complex.ofReal_re, Complex.mul_re, Complex.ofReal_im]
    rw [hre]
    linarith [hXb, hX1, le_abs_self c, hTre.1]
  have hge : M + 1 ≤ (((QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X : ℝ) : ℂ)).re :=
    ge_of_tendsto hlim (Filter.Eventually.of_forall hlow)
  rw [Complex.ofReal_re] at hge
  linarith [hbdd.2]

/-- A datum whose ordered partial spectral sums are uniformly bounded on
    `(1, √2]` satisfies no ordered-spectrum explicit formula. -/
theorem not_qExplicitFormulaSeq_of_bounded (D : QZetaDatumSeq) (C : ℝ)
    (hC : ∀ X : ℝ, 1 < X → X ≤ Real.sqrt 2 → ∀ N : ℕ, ‖D.partialSum N X‖ ≤ C) :
    ¬ QExplicitFormulaSeq D := by
  intro hinst
  obtain ⟨X, hX1, hX2, N, hN⟩ := partialSpectral_unbounded D C
  linarith [hC X hX1 hX2 N]

/-- **Absolute summability of the majorant is excluded.** If
    `Σ_n √2^{|Re ρ_n|}/‖[ρ_n]_q‖` converges, `D` satisfies no ordered-spectrum
    explicit formula. So an instance needs genuinely conditional convergence
    near `X = 1`, matching the classical mechanism. -/
theorem not_qExplicitFormulaSeq_of_summable (D : QZetaDatumSeq)
    (hs : Summable fun n => Real.sqrt 2 ^ |(D.spectrum n).val.re|
      / ‖qInteger D.q D.hq (D.spectrum n).val‖) :
    ¬ QExplicitFormulaSeq D := by
  set a : ℕ → ℝ := fun n => Real.sqrt 2 ^ |(D.spectrum n).val.re|
      / ‖qInteger D.q D.hq (D.spectrum n).val‖ with ha
  have hnn : ∀ n, 0 ≤ a n := fun n => by
    simp only [ha]; exact div_nonneg (Real.rpow_nonneg (Real.sqrt_nonneg 2) _) (norm_nonneg _)
  refine not_qExplicitFormulaSeq_of_bounded D (∑' n, a n) ?_
  intro X hX1 hX2 N
  have h1 := spectralSum_norm_le D.q D.hq ((List.range N).map D.spectrum) X hX1 hX2
  have h2 : (((List.range N).map D.spectrum).map fun ρ =>
        Real.sqrt 2 ^ |ρ.val.re| / ‖qInteger D.q D.hq ρ.val‖).sum
      = ∑ n ∈ Finset.range N, a n := by
    clear h1
    induction N with
    | zero => simp
    | succ k ih =>
      rw [List.range_succ, List.map_append, List.map_append, List.sum_append, ih,
        Finset.sum_range_succ]
      simp [ha]
  have h3 : ∑ n ∈ Finset.range N, a n ≤ ∑' n, a n :=
    hs.sum_le_tsum _ (fun n _ => hnn n)
  calc ‖D.partialSum N X‖ ≤ _ := h1
    _ = ∑ n ∈ Finset.range N, a n := h2
    _ ≤ ∑' n, a n := h3

end QOU.AlgebraicSubstrate
