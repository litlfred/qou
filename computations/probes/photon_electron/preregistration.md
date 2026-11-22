# Pre-registration — one-photon interaction with γγ electron candidates

Owner 2026-11-15: "Choosing the electron needs a different observable — what is simple photon interaction?"
In the γγ grammar a photon pair is V = σ₀σ₁⁻¹, so one photon is one crossing letter σ_g^{±1}.

Candidates (all pass reading 3 alone): E ∈ {V³, V̄³, V⁶, V̄⁶, V⁹, V̄⁹} (V̄ = σ₀⁻¹σ₁). V⁰ is included as a control.
Interactions on 3 strands, g ∈ {0,1}, ε = ±1:
- absorb:  E·σ_g^ε
- emit:    σ_g^ε·E
- Compton: σ_g^ε·E·σ_g^{−ε}
Measured: reading 3 at levels 1..3 for each, and the photon response R_g(E) = χ(E·σ_g) − χ(E·σ_g⁻¹) at each level.

Derived before computing:
- Full level 3: σ − σ⁻¹ = h, so R_g = h·χ(E) at level 3; it carries no information beyond χ(E).
- Level 2 with g = 0 (σ₀ ∈ H₂): R_0 at level 2 = h × the level-2 restriction of E, which `gg_symmetry` found differs
  between Vᵏ and V̄ᵏ. So a photon on the first strand pair should separate an electron from its mirror.
- Compton: conjugation keeps the level-3 characters; the level-2 values may move.
Check P0: R at level 3 equals h·χ(E) to 1e-30.
Outcome (i): some interaction separates candidates that H₂ could not (report which). Outcome (ii): nothing separates them.
This is an observable, not a selection rule; nothing is selected or wired. Bean qou-a1hh, PR #7741.
