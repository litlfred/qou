# Pre-registration — H₂ with a mirror γγ electron

Follows `gg_symmetry/results.md` (97f60b25270): V̄ = σ₀⁻¹σ₁ passes alone for the same powers as V (3, 6, 9) but
has different level-2 characters. Owner ruling 2026-11-15: each particle passes alone. Question: does H₂ still
bind, and by which bond, when the electron is a mirror word?

Grid: nucleon P ∈ {V³, V⁶}; electron E ∈ {V̄³, V̄⁶, V⁹, V̄⁹}; atom-2 order ∈ {pe, ep}; bond K ∈ {none, V, V², V³}
at sites 4, 5. Same harness as h2_gg_electron (reading 3 at every level 1..12, convention D, proton q₀, mpmath).
Check M0: the V⁹ electron is handled by the same code path as the V^k electrons of h2_gg_electron.

Outcome (i): with mirror electrons the passing bonds are exactly {none, V³@4, V³@5}, as for Vᵏ electrons → the
mirror label does not change chemistry. Outcome (ii): the set differs → report it. Nothing selected or wired.
