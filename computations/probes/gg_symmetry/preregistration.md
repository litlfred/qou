# Pre-registration — symmetries of the γγ family Vᵏ on 3 strands

Owner ruling 2026-11-15: each particle must pass reading 3 on its own strands. Candidate electrons left:
V⁰, V³, V⁶ (V = σ₀σ₁⁻¹). Question: can charge conjugation or handedness pick one out, i.e. does any of
the four word symmetries change the Wedderburn characters of Vᵏ?

Symmetries tested, for k = 1..9:
- inverse  Vᵏ ↦ V⁻ᵏ          (V⁻¹ = σ₁σ₀⁻¹)
- mirror   σᵢ ↦ σᵢ⁻¹          (V ↦ σ₀⁻¹σ₁)
- reverse  word reversed       (V ↦ σ₁⁻¹σ₀), strand orientation reversed
- swap     σ₀ ↔ σ₁             (V ↦ σ₁σ₀⁻¹)

Prediction, derived before computing (not fitted): all four images are conjugate to Vᵏ in B₃.
V⁻¹ = σ₁σ₀⁻¹ is the swap of V, and swap is conjugation by the half twist Δ; the mirror σ₀⁻¹σ₁ is a cyclic
rotation of V⁻¹; the reverse σ₁⁻¹σ₀ is a cyclic rotation of V. So every character χ_λ at levels 1–3 should be
unchanged, and every symmetry image should pass reading 3 alone exactly when Vᵏ does.

Check S0: χ at levels 1–3 of the four images equals that of Vᵏ to 1e-30 (mpmath 40 dps, convention D, proton q₀).
Outcome (i): equal for every k and symmetry → the 3-strand γγ grammar carries no charge or handedness label;
the electron cannot be told from the proton by these symmetries. Outcome (ii): some differ → report which.
Nothing is selected or wired. Bean qou-a1hh.
