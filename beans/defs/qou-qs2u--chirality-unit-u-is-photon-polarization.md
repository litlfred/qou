---
# qou-qs2u
title: 'Test: chirality unit u in S^2 is the photon polarization point [v1:v2]'
status: todo
type: task
priority: normal
tags:
    - quark-state
created_at: 2026-11-15T08:00:00Z
updated_at: 2026-11-15T08:00:00Z
parent: qou-qs0e
---

Stream 3 (#7818, #7820) proved u must be a pure unit quaternion (a point of S^2) and that neither S5 nor the Reeb triad fixes it.
Breit-Wheeler (`mass-theory/breit-wheeler-vertex.md:3-14`) identifies the fibre P^1(C) = S^2 coordinates [v1:v2] with the two polarizations.
Test whether u transforms as [v1:v2] under that identification, i.e. chirality is a state variable inherited through gamma gamma, not a constant.
Tension to address: `prop:confinement-universality` (conditional, class ConfinementUniversalityConjecture) says the nucleon NF is independent of the photon colour content.

## 2026-11-15: first pass, PR #7825 (draft)

`QOU/StandardModel/ChiralityPolarizationHopf.lean`: lean-direct exit 0 (`-DautoImplicit=false -s 65536`), no `sorryAx` in `#print axioms`.

**Proved (generic CommRing):**
- The Hopf map `p ↦ p i p̄` is constant on Reeb fibres (right ℂ-multiplication) and equivariant under left multiplication. So the S² of admissible `u` is ℙ¹(ℂ) as `reeb-bundle.md` reads it (the Hopf base, with the Reeb field as fibre).
- The `Γ_u = −1` eigenspace is exactly one polarization line (`hopf_eigen_line`, `hopf_eq_ray`). Choosing `u` is choosing which polarization line is left-handed.
- A Hermitian-orthogonal photon pair has antipodal Hopf images, so it fixes Γ up to the global flip, and swapping the photons is the flip (`orth_pair_chirality`, `orth_pair_swap_is_flip`).
- Linear polarizations `[v₁:v₂]` with real coordinates fill the i–k great circle. Circular polarizations map to `∓2j`.
- Conditional on ConfinementUniversalityConjecture: a `u` that is a function of the photon coefficients cannot be read off the nucleon NF. Confinement hides it; it does not contradict it.

**Still open (scope a):**
1. That BW "perpendicular" (σ₀ vs σ₁) means Hermitian orthogonality.
2. A map `(φ₀, φ₁, φ₀₁) ↦ p`. None exists in the corpus, so "inherited through γγ" is established on the cone side only.
3. The confinement class quantifies over real φ only, so it covers only the linear circle. Circular states are outside its scope as stated.

The bean stays `todo` (rule 13a).
