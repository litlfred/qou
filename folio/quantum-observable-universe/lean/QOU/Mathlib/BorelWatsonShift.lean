/-
  Watson-uniqueness brick 4b-ii (boundary) — the DiffContOnCl shift transport
  (bean el8w tranche 5).

  The ε-reduction (brick 4b-ii boundary, `BorelWatsonBoundary`) reduces Watson
  uniqueness on the open half-plane `{re > 0}` to uniqueness on each shifted
  closed half-plane `{re ≥ ε}` (ε > 0). Each such instance is obtained by
  applying brick 3's `watson_uniqueness_rhp` to the SHIFTED functions
  `w ↦ f(w + ε)` on `{re > 0}`, then translating the conclusion back. That
  requires transporting brick 3's six hypotheses across the translation
  `w ↦ w + ε`.

  This file proves the STRUCTURAL CRUX of that transport, sorry-free: the
  regularity hypothesis `DiffContOnCl` moves across the shift,

      DiffContOnCl f {re > ε}  ⟹  DiffContOnCl (w ↦ f(w+ε)) {re > 0}.

  Both halves — holomorphy on the open half-plane and continuity up to its
  closure — compose through the (entire, hence closure-continuous) affine
  translation, using `closure_setOf_lt_re` to identify the closed half-planes.
  This is a clean, reusable Mathlib-gap lemma; it is the load-bearing piece of
  the shifted `watson_uniqueness_rhp`.

  Remaining for the full shifted instance (honest, mechanical-but-lengthy): the
  same translation applied to the other five hypotheses — the `O(exp(B‖z‖^c))`
  growth (`IsBigO` under the translated `cobounded ⊓ 𝓟` filter), imaginary-axis
  boundedness (becomes boundedness on the vertical line `{re = ε}`), and the
  positive-real-axis stretched-exp decay — then assembly. Scoped in the el8w
  tranche 5 bean; NOT axiomatized.

  Archimedean (ℂ): complex holomorphy and continuity.

  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4b-ii shift
-/

import Mathlib.Analysis.Calculus.DiffContOnCl
import Mathlib.Analysis.Complex.ReImTopology

namespace QOU.Mathlib.Borel

open Set Complex

/-- **The `DiffContOnCl` shift transport (boundary-argument crux).** If `f` is
    holomorphic on `{re > ε}` and continuous up to its closure `{re ≥ ε}`, then
    the shifted `w ↦ f(w + ε)` is holomorphic on `{re > 0}` and continuous up to
    `{re ≥ 0}`. Both properties compose through the entire affine translation
    `w ↦ w + ε` (which maps `{re > 0} → {re > ε}` and `{re ≥ 0} → {re ≥ ε}`);
    the closed half-planes are identified by `closure_setOf_lt_re`. -/
theorem diffContOnCl_comp_add_const {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] {f : ℂ → E} {ε : ℝ}
    (hf : DiffContOnCl ℂ f {z : ℂ | ε < z.re}) :
    DiffContOnCl ℂ (fun w => f (w + (ε : ℂ))) {z : ℂ | 0 < z.re} := by
  have hval : ∀ w : ℂ, (w + (ε : ℂ)).re = w.re + ε := by
    intro w; rw [Complex.add_re, Complex.ofReal_re]
  have ht : Differentiable ℂ (fun w : ℂ => w + (ε : ℂ)) :=
    differentiable_id.add_const _
  refine ⟨?_, ?_⟩
  · -- holomorphy on the open half-plane
    refine DifferentiableOn.comp hf.differentiableOn ht.differentiableOn ?_
    intro w hw
    simp only [mem_setOf_eq, hval] at hw ⊢
    linarith
  · -- continuity up to the closure
    rw [closure_setOf_lt_re]
    have hcont : ContinuousOn f {z : ℂ | ε ≤ z.re} := by
      have := hf.continuousOn
      rwa [closure_setOf_lt_re] at this
    refine hcont.comp ht.continuous.continuousOn ?_
    intro w hw
    simp only [mem_setOf_eq, hval] at hw ⊢
    linarith

end QOU.Mathlib.Borel
