import QOU.QuantumObservableUniverses.QIntegralTransforms


/-!
# QOU.CategoricalFourier.exists — existence of the categorical Fourier transform

`𝓕` exists via **Wick rotation** of the Laplace transform `𝓛`: setting
`project_j f := L.transform f (s j)` for a family of (imaginary) spectral
parameters `s : Irreps → R_q`, the Fourier monoidal property
(`convolution ↦ pointwise product on each irreducible`) is **inherited from**
`L.monoidal_mul`.  The witness genuinely uses the input `f` — it is not the
input-ignoring constant-`id` projection.

LaTeX: `\label{prop:categorical-fourier-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-fourier-transform-exists
- [kassel1995] Quantum Groups, §IV
-/

namespace QOU

noncomputable section
abbrev R_q := Archimedean.R_q

/-- **Existence of the categorical Fourier transform.**

    For any categorical Laplace transform `L` on `A` and any family of
    spectral parameters `s : Irreps → R_q`, there exists a
    `CategoricalFourier A Irreps` whose projections are the Wick-rotated
    Laplace transforms `project_j f = L.transform f (s j)`.

    This replaces the earlier `Nonempty (CategoricalFourier A Irreps)` proved
    by the input-ignoring witness `project := fun _ _ => id` (whose monoidal
    law held vacuously because both sides collapsed to `id`): the existential
    now pins the projections to the genuine Wick rotation of `L`, and the
    Fourier monoidal law is *derived* from `L.monoidal_mul` rather than holding
    vacuously — realising [`def:categorical-fourier`]'s
    `F[f](ξ) = L[f](iξ)`. -/
-- Ref: [kassel1995]
theorem CategoricalFourier.exists
    {A : Type*} {Irreps : Type*}
    (L : CategoricalLaplace A) (s : Irreps → R_q) :
    ∃ F : CategoricalFourier A Irreps,
      ∀ (j : Irreps) (f : A → A), F.project j f = L.transform f (s j) :=
  ⟨{ project := fun j f => L.transform f (s j)
     monoidal := fun j f g q_conv => L.monoidal_mul f g (s j) q_conv },
   fun _ _ => rfl⟩

end

end QOU
