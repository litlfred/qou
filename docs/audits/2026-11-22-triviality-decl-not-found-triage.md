# Triviality probe: the 156 `decl-not-found` skips, triaged

Bean `qou-y1qu` (epic `qou-uwyf`). Follows §4 of
`2026-11-22-lean-audit-snapshot-gaps.md` (added by PR #8977, not yet on `main` when this record merged).
The probe fix is litlfred/folio-assistant-sci#213 (issue #212).

## 1. Result

The 2026-11-21 snapshot (`docs/audits/lean-triviality.json`) skipped 156
declarations as `decl-not-found`. Each was classified statically, with the
lexer and namespace logic of the fixed probe, against the tree at PR #8977's head
(`642d84bd0`), whose ref repoints the counts below assume. Per-declaration rows:
[`2026-11-22-triviality-decl-not-found-triage.json`](2026-11-22-triviality-decl-not-found-triage.json).

| cause | count | what it is |
|---|---|---|
| declared in the block's own `.lean`, under a qualified spelling | 55 | a probe defect. `theorem AtomKnot.exists` inside `namespace QOU.BraidKnot` is `QOU.BraidKnot.AtomKnot.exists`, but the probe compared only the last component of the ref against the spelled name. |
| declared in exactly one library file, by its fully qualified name | 77 | a probe defect. The block's `.lean` is a sibling that imports the library; the probe read only that file. |
| no file declares the ref by its qualified name | 24 | ref defects. Listed in §3. |

So 132 of the 156 were limits of the probe, not defects in the corpus. The
fixed probe finds all 132.

## 2. A third gap found on the way: blocks dropped before the loop

The probe's CLI never configured the folio's Lean packages. Without them,
`walkBlocks` cannot resolve a `lean.ref` that points into the library, so a
block with no sibling `.lean` is dropped before the probe loop sees it. It is
neither probed nor counted as skipped. Measured on this tree: 1094 blocks with
a provable file reach a declaration when the packages are configured, 697
when they are not, so a bare CLI run leaves out 397. The 2026-11-21 snapshot
was not affected, because its local driver preloaded the packages. The CLI
now loads `schemas/lean-packages.ts` (folio-assistant-sci#213, second
commit).

## 3. Refs the probe cannot resolve

**Current refs, not the snapshot's.** Run over every block on this tree with
its current `lean.ref` (after the repoints in PR #8977), 14 blocks name no
declaration the fixed probe can find:

| block | ref | covered by |
|---|---|---|
| `prop:substrate-massive-regime` | `QOU.OneDim.TLIsXXZChain` (a module) | `qou-mhzl` |
| `prop:algebraic-gns-embedding` | `…AlgebraicGnsEmbedding.markov_gns_embedding` | `qou-02q4` |
| `prop:cl3-zeta5-pslq-independence` | `…Cl3Zeta5PslqIndependence.pslq_independence` | `qou-02q4` |
| `prop:q-hecke-seminormal-character-closure` | `…QHeckeSeminormalCharacterClosure.character_closure_holds` | `qou-02q4` |
| `conj:gs-spectral-decomposition-existence` | `…GBResidueSpectralSum.spectral_decomposition` (a structure field) | `qou-g7nn` (the ref audit counts fields; the probe has no body to splice) |
| `def:braid-group` | `QOU.BraidGroup` | new: `qou-5n04` |
| `prop:q-jacobiator` | `QOU.q_jacobiator` (declared as `QOU.Elaboration.q_jacobiator`) | new: `qou-5n04` |
| `thm:qu-to-qou` | `QOU.Torsion.YekutieliTriple.qu_to_qou` (the sibling's `qu_to_qou` is in `namespace QOU`) | new: `qou-5n04` |
| `def:brane-boundary` | `QOU.Torsion.Descent.BraneBoundary` | new: `qou-5n04` |
| `def:yekutieli-triple` | `QOU.LiftingDescent.CosimplicialCrossedGroupoid.YekutieliTriple` | new: `qou-5n04` |
| `def:hecke-mass-element` | `QOU.Torsion.HeckeMassElement` (a module) | new: `qou-5n04` |
| `def:two-row-stratum` | `QOU.BraidKnot.TwoRowStratum` (a module) | new: `qou-5n04` |
| `prop:confinement-sdp` | `QOU.ParticleInteractions.ConfinementSDP` (declared as `QOU.Interactions.ConfinementSDP`) | new: `qou-5n04` |
| `cor:mass-identity-C` | `QOU.MassIdentityC` (declared as `QOU.Torsion.MassIdentityC`) | new: `qou-5n04` |

The nine marked new are refs whose qualified name matches no declaration,
though a declaration with the same short name, or a module of that name,
exists. The ref-resolution audit counts these as resolving, because it
matches module paths and short names. The triviality probe does not guess
past a namespace: probing a same-named declaration in another namespace would
measure a different goal. Repointing them is a per-block choice and is not
done here.

The snapshot's own refs leave 24 unresolved rather than 14; the difference is
refs PR #8977 repointed, plus three UGB blocks whose declarations live in the
UGB folio's lake root, which a qou run does not index.

## 4. The `cases <;> decide` gap (`qou-z3k1`)

`QOU.BraidKnot.mass_tower_coefficient_stratification` states
`stratumDepth term ≤ 4` and is proved by `cases term <;> decide`. `decide`
cannot close it, because `term` is a free variable, and `simp` does not unfold
`stratumDepth`. The probe now has a last rung, `cases-decide`: case analysis on
one explicit or implicit binder, then `decide` on each case. It is last so
every older rung keeps its `steps` number across snapshots. A declaration with
no binder records the rung as inapplicable, not as a loss. Any closure is a
real Lean proof, so the rung can only add closures.

## 5. Verification

- Static classification: the bun scripts used are summarised above; counts
  measured on PR #8977's head (`642d84bd0`), 2026-11-22.
- `bun test pipeline/lean-triviality-probe.test.ts` (folio-assistant-sci):
  with Lean 4.24.0 on `PATH`, 28 pass, 0 fail, 0 skip (after the
  `not-a-proof` commit; 27 before it).
- The Lean-backed run (the controls, and a re-probe of the 156 plus
  `mass_tower_coefficient_stratification` on the restored olean cache) is
  in §6.

## 6. Lean-backed re-probe

Run 2026-11-22, 09:46 to 09:57 UTC, with Lean 4.24.0 from
`scripts/lean-toolchain-cache-restore.sh` and the olean cache from
`scripts/lean-cache-restore.sh` (3697 Mathlib and 3465 QOU oleans,
`cat/folio-assistant-sci/lake-cache/qou-v4-24-0`). No `lake` was run.

- **Probe controls**: `bun test pipeline/lean-triviality-probe.test.ts` with
  Lean on `PATH`: 27 pass, 0 fail, 0 skip. That includes the new
  `casesDecideClosesTableCheck` control.
- **Re-probe** of the 156 snapshot skips plus
  `mass_tower_coefficient_stratification` (157), each through
  `probeDeclaration` at 120 s per rung, with the file found the way the fixed
  CLI finds it: 56 in their own `.lean`, 77 in the lake root, 24 unresolved
  (§3). None was skipped: no `baseline-fails`, `baseline-timeout` or
  `no-body`.

| outcome | count |
|---|---|
| closed | 7 |
| open | 126 |
| unresolved ref | 24 |

The seven closed, by rung:

| declaration | rung (step) | file |
|---|---|---|
| `QOU.MassIdentity.exists` | `trivial` (1) | own |
| `QOU.Archimedean.genus_maximal_descent` | `omega` (5) | lake root |
| `QOU.Archimedean.torus_knot_shell_binding` | `aesop` (6) | lake root |
| `QOU.CategoricalAction.unique` | `aesop` (6) | own |
| `QOU.HyperellipticQuintic.minimal_z5_classification` | `aesop` (6) | lake root |
| `QOU.MassIdentity.unique` | `aesop` (6) | own |
| `QOU.BraidKnot.mass_tower_coefficient_stratification` | `cases-decide` (7) | own |

So the new rung recovers `mass_tower_coefficient_stratification` (`qou-z3k1`),
and six more declarations close that the snapshot never measured. A closure is
a prompt to read the statement, not a verdict that it is vacuous (see the
probe's own header); these seven have not been read here.

No rung timed out. `aesop` was unavailable on four declarations whose files
import neither Aesop nor Mathlib; all four stay open, so for them "open" was
measured against a six-rung ladder. `cases-decide` was inapplicable (no named
binder) on 35.

**Caveat: many of the 126 open are not theorems.** Of the 133 found, 86 are
theorems (7 closed, 79 open); the other 47 are structures (21), defs (18),
classes (6) and abbrevs (2). The probe filtered a *file* by whether it holds a
theorem, not the *declaration* by its kind, so it spliced tactics into these
too, and their "open" means nothing. Fixed for types in
folio-assistant-sci#213 (fourth commit): a ref naming a `structure`, `class`
or `inductive` (27 here) is now skipped as `not-a-proof`. `def`, `abbrev` and
`instance` are still probed, because a Prop-valued `def` is the self-assuming
shape the probe exists for; the 18 defs and 2 abbrevs above are left as they
are. Bean `qou-2a55`.

The probe runs plain `lean`, not `lake build` with `-DautoImplicit=false`, as
it always has; that is unchanged here.
