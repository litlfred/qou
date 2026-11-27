# H14 result: whole-word (KL-basis) signs reproduce Lusztig's folded descent (2026-11-21)

Pre-registration: `h14_preregistration.md`. Script and output: `h14_kl_folding_probe.py`, `.out.txt` (exact integer arithmetic, runs in under a second).

The KL bases were computed independently: S₆ with equal parameters (720 elements; all coefficients nonnegative, as KL positivity requires), and the fixed group W ≅ B₃ (48 elements) with τ = s₃, b₁ = s₂s₄, b₂ = s₁s₅.

| criterion | L = (1, 2, 2) (Lusztig) | control L = (1, 1, 1) |
|---|---|---|
| 1. folded p_{y,x} ≡ ambient p̃_{y,x} mod 2, coefficientwise, all 847 pairs y ≤ x in W | **pass** | fail |
| 1. abs(folded) ≤ ambient, coefficientwise | **pass** | fail |
| 2. positions where folded ≠ ambient | 188 (90 negative, 98 nonnegative but smaller) | — |
| 3. control discriminates | **pass** | |

## What this shows

- Lusztig's §16.6 relation holds on this folding exactly as predicted: each folded KL coefficient is the trace of an involution on a space whose dimension is the ambient coefficient. The equal-parameter folding fails the same test, so the weights (1, 2, 2) are not a free choice.
- **The sign lives on whole words.** At 188 coefficient positions the twisted trace differs from the plain one, 90 of them by turning negative. That is why H13's per-crossing sign could not work: no sign per generator produces a negative coefficient in a positive KL basis.
- **The strand-level descent model:** expand the ambient (six-strand) element in the S₆ KL basis, drop swapped pairs x ≠ ι(x), and send c̃_x ↦ c_x for x ∈ W with these signs. By §16.7 this sends each doubled letter to the folded generator with eigenvalues {q², −q⁻²}, i.e. reading B (bulk q², wall q; D(q₀) = 0.94911520554914481986 on V³).
- The ruled "summed" trace keeps the ambient coefficients and the swapped pairs. It is the untwisted functional and does not factor through H(B₃; q², q).

## Limits

- Criterion 1 is a necessary consequence of Lusztig's theorem, checked numerically on one folding. It is not a proof, and the signs at the 188 positions are read off by comparison, not constructed from the φ_x.
- Conditional, as before, on `conj:type-b-folding-cpt` and the shared λ. D is a trace ratio, not a mass; no CODATA comparison.
