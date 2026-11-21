# Pre-registration: H₂ with a γγ electron (owner, 2026-11-15: "Yes, test a γγ electron")

Committed before any number in this directory was computed. Bean `qou-a1hh`, PR #7741. Follows
`../h2_gg_atom/` (decision C): with nucleon V³ or V⁶, H₂ bound with the T_w0 electron (bond V³) and
failed at level 6 with the trefoil electron. Neither corpus electron is a γγ word. The owner chose
to extend the one rule to the electron.

## Structural statements, made before computing

- On its three strands a γγ electron is V^k (only vertex: V = σ₀σ₁⁻¹; grammar has no inverses).
- So nucleon and electron differ only by their power of V. If k equals the nucleon's m they are
  the same word; nothing in the γγ grammar on three strands distinguishes them.
- On H₃ alone V^k passes reading 3 at every level exactly when V^k did as a nucleon
  (`h2_gg_atom`: k ∈ {3, 6} pass among 3…7); k = 0 (no electron letters) passes trivially.

## Enumeration (nothing outside it)

- Nucleon V^m, m ∈ {3, 6} (the decision-C survivors).
- Electron V^k, **k ∈ {0, 1, …, 7}**. k = 0 is included as the degenerate control (no electron
  crossings); it is reported but cannot count as an electron.
- Cells as in `h2_gg_atom`: 12 strands, atom = nucleon (3 strands) + electron (3 strands), atom 2 in
  order pe or ep, no p–e letter, no junction letter, bond K ∈ {none, V, V², V³} at s ∈ {4, 5}.
- 2 × 8 × 2 × 7 = 224 rows. Code: `h2_gg_atom_probe.h2_rows` unchanged; the electron is supplied
  through `kct.ELECTRONS`.

## Test

Reading 3 at every level m = 1…12, convention D, proton pin, mpmath 40 dps. Trace ratio reported,
not used to select (ruling B).

## Calibration

- E0: the electron hook reproduces the `h2-gg-atom` rows for nucleon V³ with the T_w0 electron.
- E1: χ_(3) = 1 on H₃ for every V^k.

## Outcomes, per (m, k), k ≥ 1

- (i) bound: bare H₂ word passes every level and some K ≠ none passes every level.
- (ii) blocked: bare word fails some level.
- (iii) no γγ bond: bare word passes, no K ≠ none passes.

Reported for every (m, k). Nothing is chosen by the result. If (i) holds for several k, which k is
"the electron" is an owner question, not something this probe selects.
