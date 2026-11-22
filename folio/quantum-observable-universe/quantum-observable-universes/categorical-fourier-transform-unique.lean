import QOU.Basic
import QOU.QuantumObservableUniverses.QIntegralTransforms


/-!
# QOU.CategoricalFourier.unique — uniqueness of the categorical Fourier transform

𝓕 is unique by Wick rotation of 𝓛 + Peter-Weyl uniqueness.

LaTeX: `\label{prop:categorical-fourier-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CategoricalFourier A Irreps)`, which is
**false** in general: `project` is a free data field, so distinct
instances exist whenever `(A → A)` admits two distinct self-maps
compatible with the `monoidal` law.

This file now imports the relocated `CategoricalFourier` structure
(`QOU.QuantumObservableUniverses.QIntegralTransforms`) and proves —
with no axiom:

1. **Extensionality** (`CategoricalFourier.unique`): the projection
   family determines the structure (`monoidal` is propositional).
2. **Degeneracy** (`CategoricalFourier.project_const`): because
   `monoidal` quantifies over *all* convolutions `q_conv`,
   `project j` is constant in its function argument — a structure
   defect (the law should fix one convolution).  Pinning `q_conv`
   as a field is the open structure refactor.

## References

- [leitner2026] §2-quantum-observable-universes/categorical-fourier-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

namespace QOU

/-- **Uniqueness of the categorical Fourier transform (proved
    extensionality).**

    Two `CategoricalFourier A Irreps` instances with the same
    projection family are equal: `monoidal` is propositional.  This
    replaces a false `Subsingleton (CategoricalFourier A Irreps)`
    axiom with the extensionality the structure genuinely supports. -/
-- Ref: [kassel1995] Quantum Groups, §IV
theorem CategoricalFourier.unique (A : Type*) (Irreps : Type*)
    (F₁ F₂ : CategoricalFourier A Irreps)
    (hproj : F₁.project = F₂.project) : F₁ = F₂ := by
  cases F₁
  cases F₂
  subst hproj
  rfl

/-- **Degeneracy of the current `monoidal` law (proved).**

    Because `monoidal` quantifies over *all* convolutions `q_conv`,
    the projection `project j` is constant in its function argument.
    Recorded as a proved lemma so the structure defect is visible; the
    fix (pin `q_conv` as a field) is the open refactor. -/
-- Ref: [kassel1995] Quantum Groups, §IV
theorem CategoricalFourier.project_const {A Irreps : Type*}
    (F : CategoricalFourier A Irreps) (j : Irreps) (f g : A → A) :
    F.project j f = F.project j g := by
  have h₁ := F.monoidal j g g (fun _ _ => f)
  have h₂ := F.monoidal j g g (fun _ _ => g)
  rw [h₁, ← h₂]

end QOU
