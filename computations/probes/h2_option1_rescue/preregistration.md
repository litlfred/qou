# Pre-registration: can a non-γγ letter rescue H₂ with the trefoil electron? (owner option 1)

Owner card 2026-11-15 "Which halves of the rule are hadron-specific?" → **"Measure option 1 first"**.
Option 1: the γγ construction (G) applies only to hadronic words; confinement positivity (S, reading 3
at every level, convention D, proton pin) applies to every word, atoms included.
Bean `qou-a1hh`, PR #7741. Written and pushed **before** any computation below.

## Fixed inputs (not varied)

- Nucleon block p = V³ (V = σ₀σ₁⁻¹), the γγ nucleon of `h2_gg_atom`.
- Electron e = σ₀³σ₁ on its own three strands (`kct.ELECTRONS["trefoil_s0s0s0s1"]`).
- Reading 3 exactly as in `h2_gg_atom` (`level_chars`, levels from m = 1; TOL as there).
- mpmath at the dps the reused base code sets (40); convention D; proton pin via `cf.Q`.

## Why only letters on strands 1–6 can matter at level 6 (derived, `h2_gg_atom/results.md`)

Level 6 sees atom 1 only through E_{12→6}. Atom 2's letters act on strands 7–12 and contribute a
positive scalar. A single letter σ₅^{±1} across the junction cut contributes the Markov factor
z_D or z_D − (q − q⁻¹), both positive at q₀, so it cannot change the sign either.
**Prediction J1 (check, not a search):** the bare trefoil word plus one junction letter σ₅⁻¹ keeps
(3,3)/(6) at level 6 equal to −0.31373335326276292589 to 1e-18.

## Family searched

Stage 1 (hydrogen atom, 6 strands): H_a = p · σ₂^a · e for a ∈ {−3, −2, −1, 0, 1, 2, 3}.
σ₂ is the only letter joining the proton strands (0–2) to the electron strands (3–5); a = −1 is the
corpus p–e letter (`kct.sinv(2)`). a = 0 is the control, with a predicted fail at level 6.
Record every level 1–6 character.

Stage 2 (full H₂, 12 strands): for every a that passes stage 1 at every level, build
H₂ = H_a ⊗ shift(H_a or its "ep" mirror, 6). Test it bare and with bond K ∈ {V, V², V³} at s ∈ {4, 5},
as in `h2_gg_atom`. Record levels 1–12.

## Outcomes, fixed now

- **(i)** Some a passes stage 1 and some H₂ cell passes every level. Then option 1 has an admissible
  H₂ in this family. Report **every** passing (a, orientation, bond), and do not pick one; choosing
  among them is not this probe's job.
- **(ii)** Some a passes stage 1 but no H₂ cell passes every level. Report the failing levels.
- **(iii)** No a passes stage 1. Then option 1 has no hydrogen atom in this family (scope (a):
  one p–e letter power, fixed V³ and σ₀³σ₁).

Trace ratios are reported, never used to select (ruling B). Nothing fitted, selected against data,
or wired to a dashboard.
