import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
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

/-- A Reeb eigenvalue ρ in the spectrum of the Reeb derivation ξ_q. -/
structure ReebEigenvalue where
  /-- The eigenvalue ρ ∈ ℂ (represented here as ℝ for the real part). -/
  val : ℝ

/-- The q-integer [ρ]_q = (q^ρ - q^{-ρ}) / (q - q^{-1}).

**Deliberately not consolidated onto `QOU.QInteger.qIntBal`** (`qou-qint`
census).  The index is a Reeb eigenvalue `ρ : ℝ` and the powers are `rpow`, so
this is the continuous-index bracket; the canonical `qIntBal` (ℕ) and
`qIntBalZ` (ℤ) are both discrete.  Distinct from the `JonesMarkovWenzl` case,
which merely *looked* continuous — there the `rpow`s were at half-integer
multiples of a `ℕ` index and did reduce to `qIntBal` at `q^{1/2}`.  Here `ρ`
ranges over a genuine spectrum, so no such reduction exists. -/
noncomputable def qInteger (q : ℝ) (hq : 1 < q) (ρ : ℝ) : ℝ :=
  (q ^ ρ - q ^ (-ρ)) / (q - q⁻¹)

/-- The q-logarithm ln_q(x) = ln(x) / ln(q). Well-defined for `q > 1`
    (so `Real.log q ≠ 0`); the positivity hypothesis is carried by the
    consumers rather than baked into the definition. -/
noncomputable def qLog (q : ℝ) (x : ℝ) : ℝ :=
  Real.log x / Real.log q

/-- The spectral side of the explicit formula: the oscillatory sum
    over Reeb eigenvalues plus constant and tail terms. -/
noncomputable def spectralSide
    (q : ℝ) (hq : 1 < q) (spectrum : List ReebEigenvalue)
    (Omega_q : ℝ) (X : ℝ) : ℝ :=
  X - (spectrum.map fun ρ => X ^ ρ.val / qInteger q hq ρ.val).sum
    - qLog q (2 * Real.pi * Omega_q)
    - (1 / 2) * qLog q (1 - X ^ (-2 : ℝ))

/-- For q > 1, the q-integer [n]_q is positive for positive n. -/
theorem qInteger_pos (q : ℝ) (hq : 1 < q) (ρ : ℝ) (hρ : 0 < ρ) :
    0 < qInteger q hq ρ := by
  unfold qInteger
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

**On the citation.** The withdrawn axiom was captioned *"External theorem (Rosen
2002 Ch 5 Thm 5.12; Weil 1948; Reshetikhin–Turaev 1991)"*. Rosen Thm 5.12 is the
explicit formula for the zeta function of a curve over `𝔽_q`; the identity here
is its **q-deformation**, and `[ρ]_q`, `ln_q` and the `Ω_q` term are the
framework's own constructions, appearing in none of the three works. The
citation is withdrawn and replaced by `[manuscript]`, per the disposition
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
-- Ref: [manuscript] Ch. 8 §explicit-formula
class QExplicitFormula (D : QZetaDatum) : Prop where
  /-- The identity, at every `X > 1`. -/
  formula : ∀ X : ℝ, 1 < X →
    QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X =
      spectralSide D.q D.hq D.spectrum D.Omega_q X

/-- The explicit formula holds for a datum satisfying the conjecture. Conditional
    on `[QExplicitFormula D]` (§3b-cond) — the hypothesis is visible in the type
    rather than assumed globally. -/
theorem explicit_formula (D : QZetaDatum) [QExplicitFormula D] (X : ℝ) (hX : 1 < X) :
    QChebyshevFunction D.hbar_q D.hbar_pos D.ideals X =
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
  nlinarith [h, hq34]

end QOU.AlgebraicSubstrate
