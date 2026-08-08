# `wall-side-correct` — the 33 that need a human, not a note

Date: 2026-08-07. Measured with `scripts/check-wall-side.ts --sweep`
(the real `checkWallSide`, called the way `qa-sweep` calls it: through
each block's referring manifest).

## Why this list exists

After the Gap 1 retraction it is true that **every** `wall-side-correct`
finding *can* be cleared by adding a §7c note to the referring block's
`authorNotes`. It does not follow that every one *should* be.

The criterion exists to make the author state, deliberately, which side
of the substrate→archimedean wall a file belongs on. Bulk-generating an
acknowledgement for all 121 failing blocks would clear the count while
answering that question for nobody — and would paper over precisely the
case §7c was written to catch. That is audit-dodging in the sense of
AGENTS.md §1a, even though no individual note would be false.

So the 121 were classified by the evidence actually present in the Lean:

| class | count | evidence | disposition |
|---|---|---|---|
| STRONG | 23 | `Real.sqrt` / `Real.pi` / `Real.exp` / `Real.log` / `Complex.*` / integrals | acknowledged — `ℝ` is *forced*, and each note cites the construct found in that file |
| MED | 65 | ordering (`0 <`, `≤`), `abs`, `linarith`/`positivity` only | **not** acknowledged in this pass — `ℝ` is defensible but a `[LinearOrderedField R]` restatement is often possible; needs a per-file call |
| WEAK | 33 | bare `ℝ`, **no archimedean construct at all** | **review queue — listed below** |

22 of the 23 STRONG were acknowledged (one, `brane-tower-q-laplacian-decay`,
matched the class regex only inside a comment and was left alone).
Sweep went **1067/1188 → 1089/1188**.

## The WEAK 33 — candidate genuine §7c violations

These carry `ℝ` with no `Real.*`, no ordering, no `abs`, no analysis —
**the same signature as `hoefsmit-binding-amplitude`**, which on
inspection turned out to be the one genuine gratuitous-`ℝ` violation in
the whole 18-candidate shortlist and was regenericised to
`{R : Type*} [Field R]`.

Absence of an archimedean token is evidence, not proof (the earlier
17-file read found the heuristic false-positives often — via typeclasses,
imported `M → ℝ` structures, or the *meaning* of a quantity). But this is
where a real violation is most likely to be hiding, so each needs a read,
and **none should be given an acknowledgement without one**.

```
braids-and-knots/meson-em-sinh-closed-form.lean
lean/QOU/Interactions/confinementUniversality.lean
lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean
lean/QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean
lean/QOU/AlgebraicSubstrate/collatz_contact_boundary.lean
quantum-observable-universes/fermion-boson-decomposition.lean
quantum-observable-universes/q-heat-equation.lean
lean/QOU/QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean
mass-theory/derived-mass-formula-light-isotopes.lean
lean/QOU/BraidsKnots/skein_mass_from_linking.lean
lean/QOU/BraidKnot/confined_knot_binding.lean
mass-theory/q-beta-radius-of-convergence-gate.lean
lean/QOU/BraidsAndKnots/qmn_recursive_memoized.lean
lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean
mass-theory/mass-volume-factorization.lean
mass-theory/mass-endomorphism-tower.lean
mass-theory/macdonald-hook-telescope.lean
lean/QOU/ParticleInteractions/mass_categorical_descent.lean
lean/QOU/FeynmanPathIntegrals/markov_identification.lean
mass-theory/demazure-fiber-markov-trace.lean
lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean
lean/QOU/AppendixSurreals/DiophantineBirthday.lean
lean/QOU/LiftingDescent/tm_transient_localisation.lean
lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean
lean/QOU/TopologicalMass/cat_descended_is_base_mass.lean
lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean
lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean
lean/QOU/Archimedean/BorelZagierQouVolumes.lean
lean/QOU/Archimedean/SingleVolumeIrrationality.lean
nuclear-interactions/cpt-d6-d7-d8-closure.lean
lean/QOU/ParticleInteractions/positron_correction.lean
lean/QOU/Interactions/nucleon_ordering_factorization.lean
lean/QOU/Molecular/ch4_lp_dual_binding.lean
```

Two of these sit under `QOU/Archimedean/` — worth reading first, since a
bare `ℝ` in a directory that *declares* the archimedean side but carries
no archimedean construct is either a mis-filed module or a genuinely
algebraic statement in the wrong tree.

Several cluster by subsystem (`TopologicalMass/cat_*`,
`LiftingDescent/tm_*`, the two `lp_dual_binding` blocks), so a single
read likely settles three or four at a time.

## Reproduce

```bash
bun run scripts/check-wall-side.ts --sweep content/quantum-observable-universe
```

Requires the `folio-assistant` clone
(`scripts/setup-folio-assistant.sh`), since the checker lives there.
