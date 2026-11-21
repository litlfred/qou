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

## Four-term chiral photon arm (added 2026-11-20; the record above is unchanged)

Owner ruling (bean `qou-99qc`, 2026-11-18, confirmed 2026-11-20): `def:photon` is
γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹. The rows above treat one photon as a single crossing σ_g^±1,
which under the ruling is a **term** of one photon, not a photon. The producer now also runs the full
photon (`four_term_arm`, witness key `four_term_photon_arm`). Characters are linear in the element
(new check P1, worst 1.1e-41), so the four per-term characters are recorded and any φ can be read
off them. The photon is **evaluated** only at the corpus-derived weights, the eigenvalue pair
γ₊ = γ(0,0,qh), γ₋ = γ(0,0,−q⁻¹h) of `borromean-two-photon-factorisation` (V³ = γ₊γ₋). No φ is
fitted. Proton q₀, 40 dps as before.

| | single crossing (record) | four-term photon at γ₊ / γ₋ |
|---|---|---|
| absorb passes reading 3 | only σ₁⁺, for all seven words | **all seven words, both γ₊ and γ₋** |
| response R | χ(E·σ₀) − χ(E·σ₀⁻¹) | χ(E·γ₊) − χ(E·γ₋) = (q+q⁻¹)h·χ(E·V) |

ΔR = R(1,1) − R(2) at level 2, and the same with the V⁰ value subtracted (V⁰ is no longer 0, because
the photon's own V term responds on the empty word):

| E | V⁰ | V³ | V⁶ | V⁹ | V̄³ | V̄⁶ | V̄⁹ |
|---|---|---|---|---|---|---|---|
| ΔR single crossing (record) | 0 | +0.00352 | +0.00620 | +0.00803 | −0.00433 | −0.00946 | −0.01534 |
| ΔR four-term pair | −0.34122 | −0.36351 | −0.38534 | −0.40656 | −0.36485 | −0.38799 | −0.41052 |
| minus V⁰ | 0 | −0.02230 | −0.04412 | −0.06534 | −0.02363 | −0.04677 | −0.06931 |

**What moves (scope a).** The outcome-(i) finding was that a one-photon response splits Vᵏ (+) from V̄ᵏ (−).
With the four-term photon at the corpus weights that split **does not survive**. Every word responds
with the same sign, and the word and its mirror differ only in size (V̄ᵏ slightly larger). The sign
split was a property of the single-crossing term σ₀, not of the photon. The pass/fail degeneracy also changes.
The single crossing passed only σ₁⁺, and the full photon at γ±
passes on all seven words, so reading 3 still cannot separate them. The φ₀/φ₁ chiral part has no
corpus-derived weight. Its per-term characters are in the witness, but choosing a value would be a fit.
