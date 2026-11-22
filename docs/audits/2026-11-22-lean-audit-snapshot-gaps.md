# Lean audit snapshots, 2026-11-21: what the regeneration found

Three whole-corpus Lean snapshots were regenerated on `main` after #8917
(PRs #8933, #8934, #8937). This document records the two findings that needed
reading rather than counting: the theorems the tactic ladder no longer closes,
and the content blocks whose `lean.ref` does not resolve. Each open gap has a
bean (table at the end).

## 1. Snapshots and how they were produced

| snapshot | producer | before | after |
|---|---|---|---|
| `docs/audits/lean-triviality.json` | `lean-triviality-probe.ts` at platform pin `82b389982`, 120 s per rung, 3 shards | 2026-08-08: 802 probed, 74 closed, 133 skipped (95 did not elaborate) | 921 probed, 54 closed, 169 skipped (0 did not elaborate) |
| `computations/audits/lean-ref-resolution-audit.witness.json` | `lean_ref_resolution_audit.py` | 2026-06-02: 1006 of 1026 resolve | 1302 of 1327 resolve; 1317 of 1328 after PR #8977 |
| `docs/audits/lean-atlas-deps.json` | `lean-atlas-ingest.ts --scan`, cache deleted first | 2026-08-07: 485 edges | 1317 declarations, 605 edges |

The platform CLI at this pin no longer has `--shard` / `--checkpoint` /
`--resume` / `--merge`, so the triviality sweep ran through a local driver that
mirrors the CLI loop and adds only sharding and checkpoints. `--scan` merges
into the existing cache, so the atlas cache must be deleted before a rebuild,
or stale names survive. The Lean resolver must be preloaded
(`configureLeanPackages(LEAN_PACKAGES)`), or the scan finds 903 declarations
instead of 1317.

## 2. Theorems the ladder closed in August and does not close now (12)

The ladder is a vacuity detector: a theorem it closes with `trivial`, `simp`,
`aesop` or `omega` says too little. Losing a closure is good when the statement
gained content. Each August statement was read from the last commit before
2026-08-08 on GitHub and compared with `main`.

**Vacuous in August, contentful now (6).**

| declaration | August statement | now |
|---|---|---|
| `QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe` | `(1 : ℝ) = 1 := ctx.holds` | `∃ i, ctx.d i * ctx.y i ≠ 0` |
| `QOU.BraidKnot.nuclear_knot_classification` | `∃ K, K = .borromean` | `classifyByMassNumber (Z + N) = .borromean` for `Z + N ≥ 4` |
| `QOU.BraidsAndKnots.explicit_alpha_k_h3` | four constants exhibited by `rfl` | the four traces derived from the Hecke relation, cyclicity and the Markov property |
| `QOU.OptimalNF.optimal_nf_is_standard_basis` | `∃ c, ∀ i, c i = markovVolume i q` | length, valley bound, non-absorbability and maximality of the standard basis |
| `QOU.TopologicalMass.cat_transient_localises_blowup` | the decomposition was a hypothesis | the decomposition is proved to exist from a support hypothesis |
| `QOU.BraidKnot.LevelSufficiency` | a `rfl` theorem | survives only as a module name |

**Generalised (2).** `QOU.Torsion.AlgebraicMassFormula` moved from `[Field R]`
with `≠ 0` to `[CommRing R]` with a unit. `QOU.BraidKnot.knot_factor_amphicheiral`
gained an explicit off-block normalisation hypothesis.

**Same statement, ladder now misses it (2).**

- `QOU.BraidKnot.pauli_factor_wedderburn`: the proof needs the field
  `W.sym_nonzero`, which `simp` does not pick up. Not vacuous.
- `QOU.BraidKnot.mass_tower_coefficient_stratification`: `stratumDepth term ≤ 4`,
  proved by `cases term <;> decide`. **This is still trivial content.** The
  ladder misses it only because plain `simp` does not unfold `stratumDepth`. It
  was already one of the vacuous declarations in bean `qou-z3k1`; the new
  snapshot hides it, so the snapshot's closed count is not a vacuity count.

**Gone (2).** `QOU.WedderburnMass.unified_curvature_rank_mass` is renamed or
removed. `QOU.Archimedean.UpstreamAdditions.complexLiTwo` is now a `def`.

## 3. Content blocks whose `lean.ref` does not resolve

The audit reported 25. PR #8977 resolves 14:

- **3 audit false alarms.** The audit's declaration keywords did not include
  `inductive` or `opaque` (`Interactions.SectorTaxonomy.Sector`,
  `Torsion.LinkingOperation`, `Archimedean.weierstrassProjection`). Fixed.
- **11 repointed** to the declaration in the same file that carries the
  block's statement. Three of these are weaker than their block:
  - `lem:descent` → `QOU.descent_surjective` is a predicate. Nothing in
    `descent-lemma.lean` proves the lemma.
  - `conj:reidemeister-mass-invariance` → `identity_preserved_by_shell_transition`
    is one line from `axiom bareMass_R1_invariant`. The file carries six axioms.
  - `prop:schur-weyl-mass-decomposition` → class `SchurWeylMassDecomposition`,
    which the same file inhabits with an empty instance (`emptyDecomposition`).

**Unresolved after the first repoint (11).** Four more were fixed in the same PR (`qou-g7nn`), leaving 7 (1321 of 1328 resolve). In ten, the named declaration was deleted, mostly
self-assuming projections removed by the vacuity drain (the modules' own
comments say so). The module survives.

| ref | what the module declares now | group |
|---|---|---|
| `QOU.Observations.centered_hecke_variance_positive` | `centeredVariance_pos` and its closed form | obvious successor |
| `QOU.BraidKnot.confined_knot_binding` | `confined_knot_extremal_cancellation`, `confined_knot_weighted_cancellation` | obvious successor (one of two) |
| `QOU.QBeta.FiveTwoDTSpectrumSplit` (a module name) | `dt_spectrum_two_element`, … | obvious successor |
| `QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition` | a structure **field** of that name | audit does not count fields |
| `QOU.OneDim.TLIsXXZChain` (a module name) | `xxzAnisotropy_eq`, `tlLoop_add_heckeH`, … | successor unclear |
| `QOU.BraidKnot.QHeckeSeminormalCharacterClosure.character_closure_holds` | only the context structure | projection removed; needs a real theorem |
| `QOU.BraidKnot.Cl3Zeta5PslqIndependence.pslq_independence` | only the context structure | projection removed; needs a real theorem |
| `QOU.BraidKnot.graded_trace_residue_split` | the `GradedTraceResidueSplit` structure | projection removed; needs a real theorem |
| `QOU.BraidKnot.phi_q_tower_algebraic_stratification` | only the structure | projection removed; needs a real theorem |
| `QOU.Observations.AlgebraicGnsEmbedding.markov_gns_embedding` | class `HasMarkovGnsEmbedding` | projection removed; needs a real theorem |

The eleventh, `QOU.word_no_closedChainAt`, is declared in another block's
sibling, `quantum-observable-universes/braiding-induced-ordering.lean`. The
resolver searches a block's own sibling and the lake root, not other blocks'
siblings.

## 4. Triviality probe: `decl-not-found` rose from 33 to 156

In August, 95 files did not elaborate, and those blocks were skipped before the
probe looked for their declaration. With the olean cache restored, every file
elaborates. The probe reads only the block's sibling `.lean`, so a block whose
ref points into the library (most of the 156) is reported `decl-not-found`.
This is a limit of the probe, not 123 new defects. The two audits disagree by
design (the ref audit resolves 1317 of 1328), and the 156 have not been
triaged one by one.

## 5. Gaps and their beans

| gap | bean |
|---|---|
| the epic for this list | `qou-uwyf` |
| repoint the 4 refs with an obvious successor; count structure fields | `qou-g7nn` (done in PR #8977: `centeredVariance_pos`, `confined_knot_weighted_cancellation`, `dtPair52_grading`; audit now counts fields) |
| the 5 removed self-assuming projections: state and prove a real theorem, or demote the block | `qou-02q4` |
| `TLIsXXZChain` successor | `qou-mhzl` |
| `word_no_closedChainAt`: give the block its own declaration, or let the resolver follow cross-block siblings | `qou-4nlc` |
| `lem:descent` has no Lean proof | `qou-nfn4` |
| Reidemeister block rests on six axioms | `qou-5o9n` |
| `SchurWeylMassDecomposition` inhabited by an empty instance | `qou-xksw` |
| triage the 156 `decl-not-found` skips | `qou-y1qu` |
| ladder misses `cases … <;> decide`; `mass_tower_coefficient_stratification` | appended to `qou-z3k1` |
