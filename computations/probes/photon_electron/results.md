# One photon on γγ electron candidates — results

Pre-registration `preregistration.md` (4ba00ecab5b). Producer `photon_electron_probe.py`, witness
`photon-electron.witness.json`. Check P0 PASS (level-3 response = h·χ(E), worst 1.1e-41).

## Outcome (i): a one-photon response separates Vᵏ from its mirror; pass/fail does not

- **Pass/fail is identical for all seven words** (V⁰ control included): absorb and emit pass only for σ₁ (positive);
  every Compton conjugation σ_g^ε E σ_g^{−ε} passes. So reading 3 cannot tell the candidates apart here either.
- **The level-2 photon response does.** R₀ = χ(E·σ₀) − χ(E·σ₀⁻¹) at level 2, and ΔR = R₀(1,1) − R₀(2):

| E | V⁰ | V³ | V⁶ | V⁹ | V̄³ | V̄⁶ | V̄⁹ |
|---|---|---|---|---|---|---|---|
| ΔR | 0 | +0.00352 | +0.00620 | +0.00803 | −0.00433 | −0.00946 | −0.01534 |

  The sign is + for every Vᵏ, − for every V̄ᵏ, and 0 for the empty word. The size grows with k and is not
  symmetric between a word and its mirror.

## What this means (scope a)

A single photon on the first strand pair reads a sign that splits the γγ family into Vᵏ, V̄ᵏ and the neutral V⁰.
That sign behaves like a charge sign, but calling it charge is an interpretation, not a result. It is read relative to
the strand order of the tower (level 2), the same place the order test found dependence. Nothing is selected or wired.
