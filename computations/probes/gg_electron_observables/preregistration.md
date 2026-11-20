# Pre-registration: which observables separate the γγ electron candidates V⁰, V³, V⁶

Bean `qou-a1hh`. Committed before the probe is written or run.

## Question

Under the one γγ rule on three strands (`h2_gg_electron`, results.md), the electron candidates that pass reading 3 on their own are V^k with k ∈ {0, 3, 6}, where V = σ₀σ₁⁻¹. The nucleon is drawn from the same set and the bond is V³. Which power is "the electron" is an owner question. This probe does **not** choose. It measures which mathematical invariants of the three candidates differ, so the owner can rule with those differences in view.

## Candidates

- V⁰: the identity on 3 strands; closure is the 3-component unlink.
- V³: closure is the Borromean rings (expected; checked by SnapPy identify).
- V⁶: closure of (σ₀σ₁⁻¹)⁶; 3 components (V³ is pure).

## Observables (all computed, none fitted, no comparison to measurement)

- O1 Link type: number of components, pairwise linking numbers, SnapPy identification.
- O2 Jones polynomial of the closure (SnapPy, exact Laurent polynomial).
- O3 Chirality: is the closure isotopic to its mirror (Jones symmetric under q ↔ q⁻¹ as a necessary test; SnapPy isometry of exteriors with orientation reversal as the check).
- O4 Hyperbolic volume of the exterior (SnapPy high-precision; 0 / not hyperbolic reported as such).
- O5 Reading-3 level characters of V^k on its own, levels 1..3, convention D, proton pin, 40 dps (existing `h2_gg_atom.level_chars`), and the minimum margin.
- O6 Spectrum of ρ_(2,1)(V^k) at q₀ (eigenvalues, 40 dps).
- O7 Equality with the nucleon: whether the electron word equals the nucleon word for nucleon V³ and V⁶ (trivial combinatorial check, reported so the identification is explicit).

## What counts as a result

A table, one column per candidate, one row per observable. An observable "separates" two candidates if its values differ. No observable is used to pick a candidate; volume, Jones value or any number is not compared with an experimental electron quantity. The ruling card will list each candidate with what it implies (e.g. V⁰ means the electron has no crossings; V³ means electron = nucleon word for nucleon V³).
