import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Field.Basic

/-!
# A single universal binding scale has a minimax floor

**The question (bean `qou-of4i`).** The derived binding law is
`B = E₀ · L`, where `L = ln(tr_free / tr_atom)` is a pure number fixed by the
braid word and the Markov trace, and `E₀` is one energy scale shared by every
nucleus (`computations/binding_log_free_energy.py`). Locus (a) of the
deuteron overshoot asks whether `E₀` is the wrong scale for the
nucleon–nucleon interface.

In this law the internal nucleon traces cancel in the ratio
(`QOU.QBeta.InterfaceScalar.binding_indep_of_free_trace`), so `E₀` multiplies
the interface terms only. Changing it is therefore a change for every
nucleus at once. Each nucleus `A` has a *required* scale
`r_A = B_obs(A) / L_A`, the value at which the law would reproduce it.

**What is proved here.** If two nuclei need different scales `r₁ < r₂`, then
no single scale `E` brings both within relative error
`t = (r₂ − r₁)/(r₁ + r₂)`. The bound is attained at the harmonic mean
`2 r₁ r₂ / (r₁ + r₂)`, so it is sharp.

This is a statement about the *form* `B = E · L` with one shared `E`. It says
nothing about which `L` is right. It is the order-field core of the
"A-scaling refutes any rescaling" argument of
`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
§4, with the threshold computed rather than read off a table.

The measured instantiation (on the single-crossing interface letters, which
the 2026-11-15 γγ ruling marks as superseded, so the numbers are a record and
not a current result) lives in
`computations/probes/deuteron_overshoot_loci/RESULTS.md`.

Generic over a linearly ordered field (AGENTS.md §7c): nothing archimedean is
used.
-/

namespace QOU.Nuclear.UniversalScaleMinimax

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The two relative-error bounds meet at the harmonic mean: with
`t = (r₂ − r₁)/(r₁ + r₂)`, `r₁·(1 + t) = r₂·(1 − t)`. -/
theorem upper_eq_lower (r₁ r₂ : R) (hs : r₁ + r₂ ≠ 0) :
    r₁ * (1 + (r₂ - r₁) / (r₁ + r₂)) = r₂ * (1 - (r₂ - r₁) / (r₁ + r₂)) := by
  field_simp
  ring

/-- **No universal scale fits two nuclei with different required scales
better than `t = (r₂ − r₁)/(r₁ + r₂)` in relative error.**

`|E − r_i| < t · r_i` is "`E` reproduces nucleus `i` to relative error below
`t`". Both cannot hold. -/
theorem no_scale_within_minimax (r₁ r₂ E : R) (h₁ : 0 < r₁) (h₁₂ : r₁ < r₂) :
    ¬ (|E - r₁| < (r₂ - r₁) / (r₁ + r₂) * r₁ ∧
        |E - r₂| < (r₂ - r₁) / (r₁ + r₂) * r₂) := by
  rintro ⟨ha, hb⟩
  have hs : (0 : R) < r₁ + r₂ := by linarith
  have hmeet := upper_eq_lower r₁ r₂ (ne_of_gt hs)
  have hup : E < r₁ * (1 + (r₂ - r₁) / (r₁ + r₂)) := by
    have := (abs_lt.mp ha).2
    nlinarith
  have hlo : r₂ * (1 - (r₂ - r₁) / (r₁ + r₂)) < E := by
    have := (abs_lt.mp hb).1
    nlinarith
  linarith

/-- **The bound is sharp:** the harmonic mean `2 r₁ r₂/(r₁ + r₂)` sits at
relative error exactly `t` from both. Stated for nucleus 1; nucleus 2 is
symmetric. -/
theorem harmonic_mean_attains (r₁ r₂ : R) (h₁ : 0 < r₁) (h₁₂ : r₁ < r₂) :
    2 * r₁ * r₂ / (r₁ + r₂) - r₁ = (r₂ - r₁) / (r₁ + r₂) * r₁ := by
  have hs : r₁ + r₂ ≠ 0 := by linarith
  field_simp
  ring

/-- **Lowering a shared scale to fix an over-bound nucleus worsens every
under-bound one.** If nucleus 1 is over-bound at `E` (`B₁ < E·L₁`) and
nucleus 2 under-bound (`E·L₂ < B₂`), then any smaller scale `E' < E`
strictly increases nucleus 2's deficit. -/
theorem lowering_scale_widens_deficit (E E' L₂ B₂ : R) (hL : 0 < L₂)
    (hunder : E * L₂ < B₂) (hE : E' < E) :
    0 < B₂ - E * L₂ ∧ B₂ - E * L₂ < B₂ - E' * L₂ := by
  constructor
  · linarith
  · nlinarith

end QOU.Nuclear.UniversalScaleMinimax
