import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic
import QOU.Archimedean.TorusKnotGenusFourUnique

/-!
# QOU.Archimedean.EHartreeTraceRatio

**Round-20 algebraic core of `conj:e-hartree-categorical-derivation`.**

Round 19 (`e_hartree_round19_dressed_scalar_block.py`) computed the dressed
scalar `(2,2)`-block character at K-shell dressing `m = 5`:
`χ₂₂ = h·([4]_q/[2]_q)²` with `h = q − q⁻¹`.  Round 20
(`e_hartree_round20_trace_ratio.py`) formed the trace-ratio
`ρ₂₂ := χ₂₂ / (q·[9]_q·[10]_q)²` and found `ρ₂₂ = C(q)·α_EM²` with
`C(q) = h·([4]_q/[2]_q)² = h·(q² + q⁻²)²` an `O(1)` element of `R` and
`α_EM = 1/(q·[9]_q·[10]_q)`.

This file proves, **sorry-free over `ℝ`** (archimedean, `0 < q`; CLAUDE.md §7c),
the two purely-algebraic facts underpinning round 20:

* `qbracket_four_div_two` — the bracket reduction `[4]_q / [2]_q = q² + q⁻²`
  (the dressed `(2,2)` q-dimension `dim_q V_(2,2)`).
* `trace_ratio_factorisation` — `χ₂₂ / cplx² = χ₂₂ · (1/cplx)²`, the `α²`-scaling
  step (pure algebra, `α = 1/cplx`).

The deep input — that the dressed seminormal character *equals*
`h·([4]_q/[2]_q)²` — is verified numerically in the round-19 witness and is the
character-theory content; it is the cited/granted ingredient here (the
seminormal-trace formalisation is the standing open part).  These lemmas
discharge the algebra that turns that character value into the `α_EM²` shape.

Round 24 (`e_hartree_round24_molecular_reuse.py`) adds the **LEG-1 discharge**
of the round-23 "molecular-reuse" assumption: reusing the proven genus-4
uniqueness (`QOU.Archimedean.torus_knot_genus_four_unique`), the force-carrier
crossing numbers are forced to `{9, 10}`, so the complexity
`cplx = q·[9]_q·[10]_q` (`= 1/α_EM`, em-coupling-projection) is **context-free**
— there is no molecular-vs-free version to assume.  LEG 2 (the `(2,2)=EM`
identification) stays conditional and is *not* formalised as discharged.

NOTE (sandbox): authored against the restored partial lake-cache, which lacks
the `ring`/`field_simp`/`linarith` oleans, so this file (including the round-24
additions) is hand-audited but compile-verified by CI (`lean_ci.yml`) rather
than locally.
-/

namespace QOU.Archimedean.EHartreeTraceRatio

/-- Balanced q-integer `[n]_q = (qⁿ − (q⁻¹)ⁿ)/(q − q⁻¹)` over `ℝ`. -/
noncomputable def qbracket (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹)

/-- For `0 < q` and `q ≠ 1`, the amplitude `q − q⁻¹` is nonzero. -/
theorem qsub_inv_ne (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) : q - q⁻¹ ≠ 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [sub_ne_zero]
  intro h
  apply hq1
  -- h : q = q⁻¹ ⟹ q·q = 1 ⟹ (q-1)(q+1) = 0 ⟹ q = 1 (since q > 0)
  have hqq : q * q = 1 := by
    nth_rewrite 2 [h]; exact mul_inv_cancel₀ hq0
  have hfac : (q - 1) * (q + 1) = 0 := by linear_combination hqq
  rcases mul_eq_zero.mp hfac with h1 | h2
  · linarith
  · linarith

/-- For `0 < q` and `q ≠ 1`, `q² − (q⁻¹)² ≠ 0` (the `[2]`-amplitude squared). -/
theorem qsq_sub_inv_sq_ne (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    q ^ 2 - (q⁻¹) ^ 2 ≠ 0 := by
  have hd := qsub_inv_ne q hq hq1
  intro h
  apply hd
  have hfac : q ^ 2 - (q⁻¹) ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
  rw [hfac] at h
  rcases mul_eq_zero.mp h with h1 | h2
  · exact h1
  · have hpos : 0 < q + q⁻¹ := by positivity
    linarith

/-- **The bracket reduction `[4]_q / [2]_q = q² + q⁻²`.**

This is `dim_q V_(2,2)`, the q-dimension of the scalar Wedderburn block that
activates under K-shell dressing (round 19); it is the `C(q)`-defining factor
in the round-20 trace-ratio.  Holds for `0 < q`, `q ≠ 1`. -/
theorem qbracket_four_div_two (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    qbracket q 4 / qbracket q 2 = q ^ 2 + (q⁻¹) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd := qsub_inv_ne q hq hq1
  have hd2 := qsq_sub_inv_sq_ne q hq hq1
  have hb2 : qbracket q 2 ≠ 0 := by unfold qbracket; exact div_ne_zero hd2 hd
  rw [div_eq_iff hb2]
  unfold qbracket
  field_simp
  ring

/-- **Trace-ratio factorisation (round 20).**

The molecular scalar-block trace-ratio `χ₂₂ / cplx²` equals `χ₂₂ · (1/cplx)²`
where the EM coupling is `α = 1/cplx`, `cplx = q·[9]_q·[10]_q`.  Pure algebra —
the step that exhibits the `α_EM²` scaling once the dressed character `χ₂₂` and
the complexity normaliser are in hand. -/
theorem trace_ratio_factorisation (chi22 cplx : ℝ) :
    chi22 / cplx ^ 2 = chi22 * (1 / cplx) ^ 2 := by
  rw [one_div, inv_pow, ← div_eq_mul_inv]

/-- **Round-20 trace-ratio, assembled.**

Given the round-19 dressed character `chi22 = h·(q²+q⁻²)²` and the complexity
`cplx = q·[9]_q·[10]_q`, the trace-ratio equals `C(q)·α²` with the *derived*
`O(1)` coefficient `C(q) = h·(q²+q⁻²)²` and `α = 1/cplx`.  Sorry-free; the
content is `trace_ratio_factorisation` with `C(q)` named. -/
theorem trace_ratio_eq_C_mul_alpha_sq
    (q cplx : ℝ)
    (chi22 : ℝ) (hchi : chi22 = (q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) :
    chi22 / cplx ^ 2
      = ((q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) * (1 / cplx) ^ 2 := by
  rw [hchi]
  exact trace_ratio_factorisation _ cplx

/-- **Round-20 ↔ Hartree-class wiring (conditional on the q-dimension bridge).**

The `EHartreeCategoricalDerivation` class (sibling block
`conj:e-hartree-categorical-derivation`) posits
`E_h = c₂ · m_e · c_q² · α²`.  Round 20 identifies the candidate
coefficient `c₂ = C(q) = h·(q²+q⁻²)²` (the dressed `(2,2)` trace-ratio
coefficient).  The identification `c₂ = C(q)` is **the open q-dimension-layer
bridge** — Mechanism B (the LP-dual-smoothness route) was *refuted* in round 21
(the separated-atom point is a kink, not a smooth facet), so this hypothesis is
explicitly carried, not derived.  Under it, the Hartree token takes the
round-20 form.  Pure rewriting; the content is the named hypothesis `hc2`. -/
theorem hartree_token_from_trace_ratio
    (q m_e c_q alpha E_h c_2 : ℝ)
    (hc2 : c_2 = (q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2)
    (hid : E_h = c_2 * m_e * c_q ^ 2 * alpha ^ 2) :
    E_h = ((q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) * m_e * c_q ^ 2 * alpha ^ 2 := by
  rw [hid, hc2]

/-- **Round-19 dressed scalar-block character — abstract context (§3b-cond).**

The repo convention records a concrete seminormal (Hoefsmit) character as
*data verified numerically*, rather than re-proving it from representation
matrices — see `QOU.BraidKnot.QHeckeSeminormalCharacterClosure`.  Here the
round-19 values are witnessed in
`e-hartree-round19-dressed-scalar-block.witness.json` (cross-checked to
`9·10⁻¹⁶` against the seminormal builder `hecke_characters.py`):

* `chi_bare = χ_(2,2)(σ₁σ₂σ₃) = 0` — the bare hook-support vanishing (`(2,2)`
  is the unique non-hook of `4`; q-Murnaghan–Nakayama, Ram 1991);
* `chi_dressed = χ_(2,2)(σ₁σ₂^{(5)}σ₃) = h·(q²+q⁻²)²` — the K-shell `m = 5`
  dressed value (`= h·(dim_q V_(2,2))²`). -/
structure DressedScalarCharacter (q : ℝ) where
  /-- the bare Coxeter-word character on the `(2,2)` block. -/
  chi_bare : ℝ
  /-- it vanishes (hook-support; `(2,2)` is the unique non-hook). -/
  chi_bare_eq_zero : chi_bare = 0
  /-- the K-shell-dressed character on the `(2,2)` block. -/
  chi_dressed : ℝ
  /-- its closed form `h·(q²+q⁻²)²`. -/
  chi_dressed_eq : chi_dressed = (q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2

/-- Under a dressed-scalar-character context, the round-20 trace-ratio is the
`C(q)·α²` form — combining the granted (witnessed) character with the proven
algebraic factorisation.  `cplx = q·[9]_q·[10]_q`, `α = 1/cplx`. -/
theorem traceRatio_of_dressedChar (q cplx : ℝ) (dc : DressedScalarCharacter q) :
    dc.chi_dressed / cplx ^ 2
      = ((q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) * (1 / cplx) ^ 2 :=
  trace_ratio_eq_C_mul_alpha_sq q cplx dc.chi_dressed dc.chi_dressed_eq

/-- **Round 24, LEG 1 (force-carrier crossing numbers are forced).**

Two *distinct* genus-4 coprime torus knots have crossing numbers `9` and `10`
(in some order).  Reuses the proven genus-4 uniqueness
(`QOU.Archimedean.torus_knot_genus_four_unique`): the only such knots are
`T_{2,9}` (crossing `9`) and `T_{3,5}` (crossing `10`), and the distinctness
hypothesis rules out the same-knot cases.  This is the structural fact behind
the round-23 "molecular-reuse" discharge: the force-carrier sector is unique. -/
theorem forceCarrier_crossings_forced
    (K₁ K₂ : TorusKnot) (h₁ : K₁.genus = 4) (h₂ : K₂.genus = 4)
    (hne : K₁.m ≠ K₂.m) :
    (K₁.crossingNumber = 9 ∧ K₂.crossingNumber = 10) ∨
    (K₁.crossingNumber = 10 ∧ K₂.crossingNumber = 9) := by
  rcases torus_knot_genus_four_unique K₁ h₁ with ⟨hm1, hn1⟩ | ⟨hm1, hn1⟩ <;>
    rcases torus_knot_genus_four_unique K₂ h₂ with ⟨hm2, hn2⟩ | ⟨hm2, hn2⟩
  · exact absurd (hm1.trans hm2.symm) hne
  · left; simp [TorusKnot.crossingNumber, hm1, hn1, hm2, hn2]
  · right; simp [TorusKnot.crossingNumber, hm1, hn1, hm2, hn2]
  · exact absurd (hm1.trans hm2.symm) hne

/-- **Round 24, LEG 1 (the force-carrier complexity is context-free).**

The categorical force-carrier complexity `cplx = q·[9]_q·[10]_q` (`= 1/α_EM`,
[`prop:em-coupling-projection`]) is the **same** for any two distinct genus-4
coprime torus knots — it depends only on the forced crossing-number multiset
`{9, 10}`, not on any molecular context.  Hence the round-23 normaliser
`(q·[9]_q·[10]_q)²` is **not** a free, "molecular" choice: there is no
molecular-vs-free version of the complexity to reuse, because the force-carrier
sector is unique (Bring uniqueness).  This formally discharges LEG 1 of the
molecular-reuse assumption.

LEG 2 — that the dressed `(2,2)` block *is* the EM exchange (so it costs this
`cplx`), and that the covalent pair contributes `cplx²` — is the conjecture's
own `(2,2)=EM` identification plus the covalent Pauli-2 count; it is **not**
formalised here as discharged (and cannot be, without circularity, since
`prop:force-carrier-intertwining-correspondence` is itself conditional on
`conj:e-hartree`). -/
theorem forceCarrier_complexity_unique
    (K₁ K₂ : TorusKnot) (h₁ : K₁.genus = 4) (h₂ : K₂.genus = 4)
    (hne : K₁.m ≠ K₂.m) (q : ℝ) :
    q * qbracket q K₁.crossingNumber * qbracket q K₂.crossingNumber
      = q * qbracket q 9 * qbracket q 10 := by
  rcases forceCarrier_crossings_forced K₁ K₂ h₁ h₂ hne with ⟨e1, e2⟩ | ⟨e1, e2⟩
  · rw [e1, e2]
  · rw [e1, e2]; ring

end QOU.Archimedean.EHartreeTraceRatio
