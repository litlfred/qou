# Lean tooling beans, 2026-11-21: sweep false-green, LWC-2 leftovers, never-built modules, pyhecke-native provisioning

Thread "Fix Lean tooling beans" (split from "Turn the Lean build green on main", issue #8817).
Main at `313bff6b2` unless stated. Beans: `qou-tpdg`, `qou-4r5y`, `qou-8jjo`, `qou-dgkf`.

## 1. `qou-tpdg`: the library sweep's false green (fixed on this branch)

**Claim.** `scripts/lean-library-sweep.py` could print `0 RED` and exit 0 while
modules it was asked to judge were never compiled.  Measured 2026-09-13 in the
bean: `--only-exact QOU.Mass.ProductionChainBondProduct` printed
`0 RED ... 6 skipped (dependency red)` with the named target itself skipped,
behind two `signal 11` deaths.  The single label `skipped (dependency red)`
also called "red" a cascade whose roots were all UNVERIFIED.

**Change.**
- Each skipped module's roots are traced transitively.  It is `SKIPPED`
  only if a root is RED; otherwise `BLOCKED` (not judged).
- A `--only-exact` target that was not compiled ok is named on a `TARGET` line.
- Last line is `VERDICT: GREEN | RED | INCOMPLETE (exit N)`.
- Exit status: 0 green, 1 RED, **8** incomplete (no RED, but some module
  TIMEOUT / UNVERIFIED / BLOCKED).  8 ORs cleanly with the 1 / 2 / 4 that
  `lean-progressive-reseed.py` already uses.
- `skills/local/prepare-merge-auto.md`: quote the `VERDICT:` line; exit 8 is
  not a green.

**Evidence.** No Lean toolchain in this container, so the check used a fake
`lean` on a 7-module throwaway package (one segfaulting root, one erroring
root, one clean leaf):

```
--all:                 1 ok, 1 RED, 0 TIMEOUT + 1 UNVERIFIED + 3 BLOCKED (NOT judged), 1 skipped behind RED
                       VERDICT: RED  (exit 1)
--only-exact QOU.T:    0 ok, 0 RED, 0 TIMEOUT + 1 UNVERIFIED + 2 BLOCKED (NOT judged), 0 skipped behind RED
                       TARGET QOU.T was NOT verified ok (not judged)
                       VERDICT: INCOMPLETE -- 3 of 3 module(s) not judged; this is NOT a green  (exit 8)
all clean:             7 ok ... VERDICT: GREEN -- all 7 module(s) compiled  (exit 0)
```

Before the change the second run would have exited 0.  Not run against real
Lean here; the next sweep on a Lean-equipped container is the live check.

**Blast radius.** Callers that read the exit code: `lean-progressive-reseed.py`
(ORs it, so an incomplete chunk now makes the reseed exit non-zero, which is
the point).  No script parses the old `skipped (dependency red)` text.

## 2. `qou-4r5y`: LWC-2 namespace-strip leftovers (audit, no edits)

`22728b8801` stripped a leading `Prefix.` from **539** declarations in 143
files.  Classified against current main by
[`2026-11-21-lwc2-namespace-strip-audit.py`](2026-11-21-lwc2-namespace-strip-audit.py):

| class | count | meaning |
|---|---|---|
| prefix restored since | 309 | the old full name is declared again |
| strip was correct | 5 | prefix equals the enclosing namespace (true duplicate) |
| renamed (prefix ≠ enclosing namespace) | 213 | full name changed; dot-notation on the type is gone |
| declaration no longer found | 12 | removed or moved since |

**Compile breaks: none left.** The whole-library sweep of 2026-11-21 at
`2ae54ab401` (issue #8817) judged 3435 QOU modules with no source error
outside the library root's `unitJ` clash, which is not an LWC-2 casualty.
Every renamed declaration's callers therefore compile.

**What is left is name drift in references that no compiler checks.** 26 old
names are still mentioned somewhere and are declared nowhere in the repo
(comments, docstrings, coordination docs, skill docs, probe docstrings and
witness `description` text).  No content-block `lean.ref` is among them.

- `CFinite.recurrence_step` -> now `recurrence_step` in QOU/QBeta/RationalCoeffRecurrence.lean (13 ref): computations/qbeta/qbeta-bar-even-kernel-invariant-probe.witness.json:13, computations/qbeta/qbeta_bar_even_kernel_invariant_probe.py:245, computations/qbeta/qbeta_bar_even_kernel_invariant_probe.py:287, computations/qbeta/qbeta_ck_recurrence_on_corrected_crosscheck.py:16
- `Cell.content_plus_transpose_content_eq_zero` -> now `content_plus_transpose_content_eq_zero` in QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean (2 ref): folio/quantum-observable-universe/appendix-formalisation-notes/type-b-folded-crystal-combinatorics-table-data.md:7, folio/quantum-observable-universe/lean/QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean:87
- `ConfinementLevel.exists` -> now `exists` in QOU/BraidKnot/ConfinementLevel.lean (1 ref): docs/coordination/2026-11-20-session-review.json:8063
- `ElementDatum.deviation_uniform` -> now `deviation_uniform` in QOU/AtomicMass.lean (1 ref): folio/quantum-observable-universe/lean/scripts/gen_atomic_mass.py:166
- `H2.one_mul_sigma` -> now `one_mul_sigma` in QOU/Mathlib/HeckeAlgebra.lean (1 ref): computations/audits/field-typeclass-audit.witness.json:595
- `H2.sigma_mul_one` -> now `sigma_mul_one` in QOU/Mathlib/HeckeAlgebra.lean (1 ref): computations/audits/field-typeclass-audit.witness.json:605
- `H2.sigma_sq_eq` -> now `sigma_sq_eq` in QOU/Mathlib/HeckeAlgebra.lean (1 ref): computations/audits/field-typeclass-audit.witness.json:615
- `InSymmetricIdempotent.refl` -> now `refl` in QOU/Mathlib/SymmetricIdempotent.lean (1 ref): folio/quantum-observable-universe/lean/QOU/Mathlib/SymmetricIdempotent.lean:61
- `IsSU2.mul` -> now `mul` in QOU/QuaternionicElectroweak.lean (1 ref): folio/quantum-observable-universe/lean/QOU/QuaternionicElectroweak.lean:17
- `IsSU2.one` -> now `one` in QOU/QuaternionicElectroweak.lean (1 ref): folio/quantum-observable-universe/lean/QOU/QuaternionicElectroweak.lean:17
- `IsSigmaUnitary.crossFactor` -> now `crossFactor` in QOU/QBeta/FaddeevModularDouble.lean (2 ref): computations/qbeta/qbeta-fmap-phi-b-channel-separation.witness.json:37, computations/qbeta/qbeta_fmap_phi_b_channel_separation_probe.py:186
- `List.sum_insertionSort_eq` -> now `sum_insertionSort_eq` in QOU/MathlibExt.lean (1 ref): skills/local/lean-mathlibext-curator.md:111
- `Matrix.PosSemidef.eigenvalues_pos_filter_eq_ne_zero_filter` -> now `PosSemidef.eigenvalues_pos_filter_eq_ne_zero_filter` in QOU/MathlibExt/SDPRankEquality.lean (3 ref): docs/coordination/2026-05-30-sdp-uniqueness-status.md:29, folio/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean:91, folio/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean:175
- `Matrix.PosSemidef.rank_via_eigenvalues` -> now `PosSemidef.rank_via_eigenvalues` in QOU/MathlibExt/SDPRankEquality.lean (3 ref): docs/coordination/2026-05-30-sdp-uniqueness-status.md:14, docs/coordination/2026-05-30-sdp-uniqueness-status.md:45, folio/quantum-observable-universe/lean/QOU/MathlibExt/SDPRankEquality.lean:95
- `Matrix.frobeniusInner_symm` -> now `frobeniusInner_symm` in QOU/MathlibExt/FrobeniusInnerProduct.lean (1 ref): folio/quantum-observable-universe/lean/QOU/MathlibExt/FrobeniusInnerProduct.lean:19
- `PartitionOf5.binding_magnitude_eq_dim` -> now `binding_magnitude_eq_dim` in QOU/BraidsAndKnots/S5SO3FiberAction.lean (1 ref): docs/coordination/option-e.md:179
- `PartitionOf5.deltaSign_mixed` -> now `deltaSign_mixed` in QOU/BraidsAndKnots/S5SO3FiberAction.lean (7 ref): AGENTS.md:3106, computations/kl_betti_cell_dependence_probe.py:9, computations/probes/deltalambda-cyclotomic-sign-map.witness.json:89, computations/probes/deltalambda_cyclotomic_sign_map_probe.py:9
- `PartitionOf5.dtEuler_eq_deltaLambda` -> now `dtEuler_eq_deltaLambda` in QOU/BraidsAndKnots/DeltaLambdaDTIndex.lean (1 ref): folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndexGeneralN.lean:150
- `PartitionOf5.electron_block` -> now `electron_block` in QOU/BraidsAndKnots/S5SO3FiberAction.lean (1 ref): folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean:659
- `PartitionWithCells.self_transpose_content_sum_zero` -> now `self_transpose_content_sum_zero` in QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean (1 ref): folio/quantum-observable-universe/appendix-formalisation-notes/type-b-folded-crystal-combinatorics-table-data.md:12
- `PentagonClosure.solution_periodic` -> now `solution_periodic` in QOU/QBeta/CyclicDilogPentagon.lean (1 ref): folio/quantum-observable-universe/lean/QOU/QBeta/CyclicDilogPentagon.lean:30
- `Real.q_half_denom` -> now `q_half_denom` in QOU/MathlibExt.lean (4 ref): skills/local/lean-mathlibext-curator.md:40, skills/local/lean-substrate-numerics.md:40, skills/local/lean-substrate-numerics.md:76, skills/local/lean-substrate-numerics.md:122
- `SDPSlaterUniqueness.ofActiveEmptyAndCostPosDef` -> now `ofActiveEmptyAndCostPosDef` in QOU/MathlibExt/SDPRealUniqueness.lean (1 ref): folio/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean:477
- `SDPSlaterUniqueness.ofDualSlackPosDef` -> now `ofDualSlackPosDef` in QOU/MathlibExt/SDPRealUniqueness.lean (1 ref): folio/quantum-observable-universe/lean/QOU/MathlibExt/SDPRealUniqueness.lean:476
- `TauAssignmentData.bar_kills_nilpotent` -> now `bar_kills_nilpotent` in QOU/Machinery/HeckeMonodromyWeightFiltration.lean (1 ref): folio/quantum-observable-universe/lean/QOU/Machinery/HeckeMonodromyWeightFiltration.lean:25
- `ZetaFamily.conj_fixed_of_bar_fixed` -> now `conj_fixed_of_bar_fixed` in QOU/Machinery/HabiroZetaFamily.lean (1 ref): folio/quantum-observable-universe/lean/QOU/Machinery/HabiroZetaFamily.lean:21


**Options (owner call; the default is to leave them).**
1. Update the 26 references to the current names.  Exemption 2 of the
   ask-before-changing rule arguably covers it (the Lean declaration decides
   the name), but four are witness `.json` files, which should be fixed at the
   producer, not by hand.
2. Restore the type prefix on the 213 renamed declarations.  Larger, touches
   about 100 Lean files, and brings dot-notation back; nothing currently needs it.
3. Leave as is and close the bean.  Nothing breaks; the drift is prose.

My recommendation (judgement): option 1 for the 22 non-witness references, and
close the bean.

## 3. `qou-8jjo`: never-built modules (triage)

The bean's title figure (1089 never built) is container state, as its own
2026-09-14 entry says.  The corpus-level answer is current as of today: the
2026-11-21 whole-library run at `2ae54ab401` judged 3435 QOU modules, all
green after the `unitJ` fix and the 66 gap oleans.

**Delta since that run** (`git diff --name-status 2ae54ab401 origin/main`,
QOU / UGB / Fred2005 library paths): **104** files, 55 added and 49 modified,
about 6 hours later.  Those are the modules whose compile status is unknown
right now.  UGB and Fred2005 were not in the 2026-11-21 run at all.

What would close the bean (from its own text): a delta sweep keyed off a
last-swept commit recorded somewhere durable, so no agent has to remember it.
Proposal, not built: the sweep writes `{commit, verdict, judged, date}` to a
small tracked file when it ends GREEN under `--all`, and `--since-last-green`
seeds the run with `git diff` from that commit.  That changes the shared gate,
so it waits for the owner.

## 4. `qou-dgkf`: pyhecke-native wheel provisioning (owner decision)

**State has moved since the bean was filed (2026-08-07).** Options 2 and 4 of
the bean already exist on main: `scripts/build-pyhecke-native.sh` builds and
installs the wheel and checks the trace convention, and `.claude/settings.json`
runs it in the background at SessionStart.

Measured in this container today: `./scripts/build-pyhecke-native.sh` exit 0,
**2 m 36 s** wall (5 m 31 s CPU), wheel `pyhecke_native-0.9.0-cp313-cp313-manylinux_2_35_x86_64.whl`,
convention gate `markov_z(q0)` matches the registry to 0.  The Clarabel fork
fetch from github.com succeeded through the proxy.

So the remaining cost is ~2.5 min per fresh container, plus a race: a probe
launched in the first ~3 minutes still sees `ModuleNotFoundError`.  The wheel is
not abi3 (`pyo3` has no `abi3-py3x` feature), so a cached wheel is tied to one
CPython minor version (this container: 3.13; the bean's was 3.11).

Options are in the thread's decision card.
