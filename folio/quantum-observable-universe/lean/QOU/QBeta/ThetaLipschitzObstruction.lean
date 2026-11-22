/-
  ϑ_K cannot be Lipschitz-in-q₀ with a moderate constant (bean `qou-8vt2`).
  The `dc₃/dq` obstruction, transferred to ϑ.

  THE TRANSFER.  `conj:binding-qbeta-complex-volume` sets
  `S_leak(q₀) := c₃(q₀) + Vol(4₁)` (tabulated in `QOU.QBeta.SLeakZeroCrossing`),
  and the T5 channel reads `S = A_ω·κ·(ln²q₀ − ϑ²)`.  Composing, **ϑ_K is an
  affine reparametrisation of c₃** — "derive ϑ_K" and "derive c₃" are one
  question.

  NOTE THE OFFSET IS INERT HERE.  `S_leak` is a DEFINITION, not a derived
  decomposition: calling `−Vol(4₁)` the bar-even part of c₃ would need a
  derivation nobody has (AGENTS.md §"Defined residual ≠ derived
  decomposition"; the identification is disputed — see
  `docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`
  §RETRACTED).  Nothing below rests on it.  The bound uses only the DIFFERENCE
  `|S₁ − S₂|`, in which the additive constant cancels identically:

      |S₁ − S₂| = |(c₃(p) + V) − (c₃(μ) + V)| = |c₃(p) − c₃(μ)|

  Checked across `V ∈ {Vol(4₁), 2 + 1/36, 63/31, 0, 1000}` — all give
  `0.04914234`, the `0.049` used below.  So the forced `K ∈ [10⁷, 1.1×10⁷]` is a
  fact about c₃'s anchor-to-anchor variation ALONE, and the obstruction holds
  whether or not `−Vol(4₁)` is c₃'s bar-even part.

  AND THE CANCELLATION ARTIFACT DOES NOT REACH IT.  `S_leak` is separately known
  to be a ~98% cancellation, which amplifies c₃'s anchor swing by ~209× — the
  RELATIVE swing goes `2.4325% → 507.51%`.  That amplification is arithmetic,
  not structure, so it would be a bad thing to rest an argument on.  This file
  does not: the bound is stated in the ABSOLUTE difference `|S₁ − S₂|`, which is
  `0.04914234` for `S_leak` and for bare c₃ alike — the ~209× lives in the
  denominator of a relative measure that never appears here.  The `0.049` below
  IS c₃'s real 2.4325% swing.

  That matters because the c₃ arc already carries a structural obstruction the ϑ
  arc never had.  The ck-dk canonical registry records c₃ as
  **"EMPIRICAL — near-match, REFUTED as real-q fibre element"**, with
  `dc₃/dq ≈ 3.84×10⁶` — "impossible for smooth real `f`", which killed the real-q
  c₃ family.  Via the affine relation, the same obstruction lands on ϑ.

  WHAT THIS FILE PROVES.  A Lipschitz bound in the forward direction — a ϑ that
  is `K`-Lipschitz across the anchor interval BOUNDS how much `S` can move:

      |S₁ − S₂| ≤ A·κ·( |L₁ − L₂| + K·|Δq|·(|ϑ₁| + |ϑ₂|) )

  Read contrapositively, a large measured `|S₁ − S₂|` over a tiny `|Δq|` forces a
  large `K`.  Stated this way it needs no division and no hypothesis that ϑ is
  differentiable — only Lipschitz, which every smooth geometric quantity is.

  THE NUMBERS IT EXCLUDES (measured; not inputs to any theorem here).  The two
  anchors are the muon and proton PINS of the same substrate, `1.28e-8` apart
  (11.54 ppb).  Across that interval `S` moves by `4.9e-2`.  So

      dϑ/dq ≈ −2.5×10⁷ (muon)      −7.3×10⁶ (proton)

  against `d(ln q₀)/dq = 0.90` — O(1) — for a smooth geometric quantity.  Seven
  orders of magnitude.  The Lipschitz form below brackets it sharply: every
  `K ≤ 10⁷` is excluded and `K = 1.1×10⁷` clears, so the forced constant sits in
  `[10⁷, 1.1×10⁷]`.

  WHY IT IS WORTH A FILE.  This is a filter ORTHOGONAL to the scale filter that
  did most of the pruning so far.  The scale filter is about MAGNITUDE (ϑ is
  `O(ln q₀) ≈ 0.1`, so `O(1)–O(5)` readings were excludable before measuring).
  This one is about the DERIVATIVE, and it excludes candidates the scale filter
  passes: any ϑ of the right size that also varies smoothly in q₀ is dead,
  whatever its value.  Apply it up front, like the scale filter.

  HONESTY BOUNDARY.

  * The `dc₃/dq` obstruction is NOT new — it is the corpus's, from the real-q c₃
    falsification.  What is new here is the TRANSFER to ϑ, which the ϑ arc did
    not have because the two arcs were running on separate trails.
  * `dS/dq` is a FINITE DIFFERENCE between two pins, not a derivative.  If `c₃`
    is not a function of `q₀` at all — which is the live reading, per AGENTS.md's
    fibre-vs-observable distinction — then the "derivative" is not one.  The
    exclusion survives that reading intact: no Lipschitz function of `q₀` with a
    moderate constant can move that far over 11.54 ppb, whether or not the
    underlying object is a function of `q₀`.
  * Recomputing `dS/dq` from the tabulated anchor values gives `3.84e6`; the
    registry quoted `≈ 4.6e6`.  **RECONCILED 2026-08-29 (bean `qou-kt8o`): this
    file was right and the registry was stale.**  `4.6e6` is what the secant
    gives when the muon `c₃` is the pre-#1422 **superseded** `-2.0097`; the live
    value is `-2.01986031` at the CODATA-2022 pin (`-2.02020024` at the
    superseded CODATA-2018 one), which yields `3.84e6` — exactly the number computed
    here.  `ck-dk-canonical-registry.md` §3 absorbed the correction on
    2026-08-25 (PR #5765) and its JSON twin on 2026-08-29.  The caution above
    was well placed: the disagreement was real, not a rounding artifact, and the
    conclusion is indeed insensitive to it.
> **🛑 CONVENTION-C SCOPE (added 2026-08-31).** The `c₃` values quoted here —
> `−2.01986031` (muon, CODATA-2022 pin) and `−2.06934258` (proton) — are
> **C-frame extractions**.
> Owner ruling 2026-08-09 excised convention C at the `z` level (production uses
> `z_D = q³/(q²+1)`), but the `c_k` **ladder** has not been re-derived under D:
> bean `qou-cds1` states it "must be re-derived, not re-evaluated", and the
> `c₃ ≈ −974` obtained by feeding `z_D` to the current extractor is a
> sensitivity measurement, **not** a proposed value. So every value-level `c₃`
> fact below is C-conditional and moves if `qou-cds1` lands.
>
> **No theorem in this file depends on it** — the values appear in this
> docstring only, verified by AST scan in
> `computations/deltalambda/wlambda_binding_c_frame_conditionality_audit.py`.
  * Nothing here proposes a ϑ or derives `A_ω`.

  Scope (a): what is excluded is the class of Lipschitz-with-moderate-constant
  ϑ candidates, not ϑ itself.

  Archimedean (ℝ): absolute values and ordering — §7c.

  -- Ref: [leitner2026] bean qou-8vt2; docs/coordination/ck-dk-canonical-registry.md §c_3
  -- Ref: [leitner2026] docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md
-/

import Mathlib.Tactic

namespace QOU.QBeta.ThetaLipschitzObstruction

/-- **A Lipschitz ϑ bounds the S-variation.**

If the channel `S = A·κ·(L − ϑ²)` holds at two substrate points, and ϑ is
`K`-Lipschitz between them, then `S` cannot move further than the bound.

No division, no differentiability: Lipschitz is all that is assumed, and every
smooth geometric quantity is Lipschitz on a compact interval. -/
theorem s_variation_le_of_lipschitz
    {A κ L₁ L₂ S₁ S₂ ϑ₁ ϑ₂ Δq K : ℝ}
    (hAκ : 0 ≤ A * κ)
    (h₁ : S₁ = A * κ * (L₁ - ϑ₁ ^ 2))
    (h₂ : S₂ = A * κ * (L₂ - ϑ₂ ^ 2))
    (hlip : |ϑ₁ - ϑ₂| ≤ K * |Δq|) :
    |S₁ - S₂| ≤ A * κ * (|L₁ - L₂| + K * |Δq| * (|ϑ₁| + |ϑ₂|)) := by
  have hsq : |ϑ₁ ^ 2 - ϑ₂ ^ 2| ≤ K * |Δq| * (|ϑ₁| + |ϑ₂|) := by
    have hfac : ϑ₁ ^ 2 - ϑ₂ ^ 2 = (ϑ₁ - ϑ₂) * (ϑ₁ + ϑ₂) := by ring
    rw [hfac, abs_mul]
    have h1 : |ϑ₁ + ϑ₂| ≤ |ϑ₁| + |ϑ₂| := by
      rcases abs_cases (ϑ₁ + ϑ₂) with ⟨e, _⟩ | ⟨e, _⟩ <;>
        rcases abs_cases ϑ₁ with ⟨a, _⟩ | ⟨a, _⟩ <;>
          rcases abs_cases ϑ₂ with ⟨b, _⟩ | ⟨b, _⟩ <;> linarith
    have h2 : (0:ℝ) ≤ |ϑ₁ - ϑ₂| := abs_nonneg _
    have h3 : (0:ℝ) ≤ |ϑ₁| + |ϑ₂| := by positivity
    calc |ϑ₁ - ϑ₂| * |ϑ₁ + ϑ₂| ≤ |ϑ₁ - ϑ₂| * (|ϑ₁| + |ϑ₂|) := by
          exact mul_le_mul_of_nonneg_left h1 h2
      _ ≤ (K * |Δq|) * (|ϑ₁| + |ϑ₂|) := mul_le_mul_of_nonneg_right hlip h3
  have hS : S₁ - S₂ = A * κ * ((L₁ - L₂) - (ϑ₁ ^ 2 - ϑ₂ ^ 2)) := by
    rw [h₁, h₂]; ring
  rw [hS, abs_mul, abs_of_nonneg hAκ]
  have htri : |(L₁ - L₂) - (ϑ₁ ^ 2 - ϑ₂ ^ 2)| ≤ |L₁ - L₂| + |ϑ₁ ^ 2 - ϑ₂ ^ 2| := by
    rcases abs_cases ((L₁ - L₂) - (ϑ₁ ^ 2 - ϑ₂ ^ 2)) with ⟨e, _⟩ | ⟨e, _⟩ <;>
      rcases abs_cases (L₁ - L₂) with ⟨a, _⟩ | ⟨a, _⟩ <;>
        rcases abs_cases (ϑ₁ ^ 2 - ϑ₂ ^ 2) with ⟨b, _⟩ | ⟨b, _⟩ <;> linarith
  have : |(L₁ - L₂) - (ϑ₁ ^ 2 - ϑ₂ ^ 2)| ≤ |L₁ - L₂| + K * |Δq| * (|ϑ₁| + |ϑ₂|) := by
    linarith
  exact mul_le_mul_of_nonneg_left this hAκ

/-- **The exclusion, contrapositive.**  If the measured S-variation EXCEEDS the
Lipschitz bound, no such `K` works — the candidate ϑ is excluded.

This is the form to apply as an up-front filter: compute the bound for the
candidate's Lipschitz constant, compare against the measured `|S₁ − S₂|`, and
discard on failure without ever evaluating the candidate's value. -/
theorem not_lipschitz_of_s_variation_gt
    {A κ L₁ L₂ S₁ S₂ ϑ₁ ϑ₂ Δq K : ℝ}
    (hAκ : 0 ≤ A * κ)
    (h₁ : S₁ = A * κ * (L₁ - ϑ₁ ^ 2))
    (h₂ : S₂ = A * κ * (L₂ - ϑ₂ ^ 2))
    (hbig : A * κ * (|L₁ - L₂| + K * |Δq| * (|ϑ₁| + |ϑ₂|)) < |S₁ - S₂|) :
    ¬ (|ϑ₁ - ϑ₂| ≤ K * |Δq|) :=
  fun hlip => absurd (s_variation_le_of_lipschitz hAκ h₁ h₂ hlip) (not_le.mpr hbig)

/-- **The Lipschitz constant is bounded below.**  Rearranged division-free:
given the measured variation, any valid `K` satisfies this.  With
`|Δq| ≈ 1.3e-8` and `|S₁ − S₂| ≈ 4.9e-2` it is what forces `K ~ 10⁷`. -/
theorem lipschitz_constant_ge
    {A κ L₁ L₂ S₁ S₂ ϑ₁ ϑ₂ Δq K : ℝ}
    (hAκ : 0 ≤ A * κ)
    (h₁ : S₁ = A * κ * (L₁ - ϑ₁ ^ 2))
    (h₂ : S₂ = A * κ * (L₂ - ϑ₂ ^ 2))
    (hlip : |ϑ₁ - ϑ₂| ≤ K * |Δq|) :
    |S₁ - S₂| - A * κ * |L₁ - L₂| ≤ A * κ * (K * (|Δq| * (|ϑ₁| + |ϑ₂|))) := by
  have hb := s_variation_le_of_lipschitz hAκ h₁ h₂ hlip
  nlinarith [hb]

/-! ## The numeric bite, at the measured anchor values

Rounded-outward inputs, so each inequality is a genuine bound on the real case:
`A·κ = 3·√3/4 ≈ 1.2990381`, `|ΔL| ≤ 1e-8`, `|Δq| = 1.3e-8` (the 11.54 ppb pin
separation), `|ϑ₁| + |ϑ₂| ≤ 0.27`, and the measured `|S₁ − S₂| = 0.049`.

These are `norm_num` facts about the BOUND, not about ϑ — no ϑ value is asserted. -/

/-- `K = 10³` is excluded: the bound is `4.6e-6`, four orders below the measured
`0.049`. -/
theorem bound_excludes_K_1e3 :
    (1.2990381 : ℝ) * (0.00000001 + 1000 * 0.000000013 * 0.27) < 0.049 := by norm_num

/-- `K = 10⁶` is still excluded — the bound reaches only `4.6e-3`. -/
theorem bound_excludes_K_1e6 :
    (1.2990381 : ℝ) * (0.00000001 + 1000000 * 0.000000013 * 0.27) < 0.049 := by norm_num

/-- **`K = 10⁷` is STILL excluded** (bound `4.56e-2` vs measured `4.9e-2`).

Worth stating: a first draft of this file asserted the opposite, guessing `10⁷`
would clear.  It does not — the threshold is `≈ 1.07e7`, and the guess was wrong
by that factor. -/
theorem bound_excludes_K_1e7 :
    (1.2990381 : ℝ) * (0.00000001 + 10000000 * 0.000000013 * 0.27) < 0.049 := by norm_num

/-- `K = 1.1 × 10⁷` finally clears the bound, so the exclusion is sharp: the
forced Lipschitz constant lies between `10⁷` and `1.1 × 10⁷`.  Recorded so the
result is a bracket, not a one-sided "at least". -/
theorem bound_clears_K_1p1e7 :
    ¬ ((1.2990381 : ℝ) * (0.00000001 + 11000000 * 0.000000013 * 0.27) < 0.049) := by
  norm_num

end QOU.QBeta.ThetaLipschitzObstruction
