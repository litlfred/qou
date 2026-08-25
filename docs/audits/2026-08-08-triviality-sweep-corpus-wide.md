# Corpus-wide triviality sweep — results, and four layers of tooling error

**Date:** 2026-08-08
**Bean:** `qou-z3k1`
**Witness:** [`docs/audits/lean-triviality.json`](lean-triviality.json)
**Tooling:** [litlfred/folio-assistant#69](https://github.com/litlfred/folio-assistant/pull/69)

## Result

| | |
|---|---|
| probed | **802** |
| closed by a cheap tactic | **74 (9%)** |
| skipped | **133** |

Closed by rung: `trivial` 40, `simp` 18, `aesop` 14, `omega` 2.

Skips: `file-does-not-elaborate` 95, `decl-not-found` 34, `no-body` 5.

A closed hit is a **prompt, not a verdict** — content living in a definition
or in the `simp` set is not absence of content. Of the first six read, four
were legitimate.

## The number that mattered was wrong four times

Every headline this sweep produced was, at first, a measurement of our own
tooling rather than of the corpus. Each fix revealed the next layer, and in
each case the wrong number was the one that would have been published.

| pass | what it reported | actual |
|---|---|---|
| 1. LEAN_PATH shadowing | "928 of 938 blocks do not elaborate" | the paper Lake root's 5-olean mathlib stub shadowed the workspace's 6990 |
| 2. one skip message for four causes | all skips read as "file does not elaborate" | `decl-not-found` is *our* bookkeeping, not a broken file |
| 3. sibling-only lookup | 185 `decl-not-found` | 156 (84%) resolved elsewhere in the tree |
| 4. mentions-vs-declares, then last-component matching | 92, then 9 still misreported | namespace-qualified heads (`ConfinementLevel.unique`) |

Final: **34 `decl-not-found`, of which 31 are genuinely absent and 3 are
namespace mismatches** — real findings (below).

The generalisable lesson is procedural, not technical: **check the running
numbers against the prediction early.** Passes 3 and 4 were each caught by
comparing a mid-run count against an expected one (185 vs 29, then 105 vs 29),
not by waiting for the run to finish.

A note on the last one, because it is the reason to prefer suffix-matching over
last-component matching: matching `unique` to `unique` would have made the
probe *silently probe a different theorem* in an unrelated namespace, and report
a confident result about it. Rejecting the mismatch turns a silent wrong answer
into a visible finding.

## Findings

### Vacuous existentials — 12, of which 8 are new

Shape: `∃ x, x = <expr> := ⟨<expr>, rfl⟩` — "there exists a thing equal to this
thing", true for any total function.

**Already in [`2026-08-07-lean-vacuous-existential-audit`](2026-08-07-lean-vacuous-existential-audit.md)** (independent confirmation, no action):
`nuclear_knot_classification`, `knot_factor_spectral_form`, `exists`,
`knot_factor_amphicheiral`.

**New — not in that audit:**

| declaration | file |
|---|---|
| `mass_tower_coefficient_stratification` | `mass-tower-coefficient-stratification.lean` |
| `habiro_integral` | `habiro-precision-ladder-equivalence.lean` |
| `residue_isRingHom_of_residueAtRoot` | `residue-at-root.lean` |
| `hadron_operations_closure` | `hadron-operations-closure.lean` |
| `pauli_factor_wedderburn` | `pauli-factor-wedderburn.lean` |
| `explicit_alpha_k_h3` | `explicit-alpha-k-h3.lean` |
| `optimal_nf_is_standard_basis` | `optimal-normal-form-valley.lean` |
| `cp_violation_spectral_form` | `cp-violation-spectral-form.lean` |

`hadron_operations_closure` is four conjuncts of
`∀ n, ∀ h : Hadron n, ∃ h' : Hadron n, h' = op n h` — closure asserted as
well-typedness. `nuclear_knot_classification` takes `(Z N : ℕ) (hA : Z + N ≥ 4)`,
uses neither, and concludes `∃ K, K = .borromean`.

**Coordinate with that audit's owner before draining.** These extend it.

### Quantified tautologies — 2, now statically caught

```lean
theorem orbit_sum_general (zeta3 : ℝ) : ∀ N : ℕ, 2 ≤ N →
    cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3 := by intro _ _; rfl

theorem closed_form_holds : ∀ n : ℕ, 2 ≤ n →
    imLi3ZetaPredicted (n : ℝ) = imLi3ZetaPredicted (n : ℝ) := by intro _ _; rfl
```

A theorem named *"closed form holds"* asserting a function equals itself. The
reflexive check matched the whole conclusion, so the leading `∀ … →` defeated
it. Fixed; 3 hits corpus-wide, no flood.

### Broken and mismatched `lean.ref` — 34

31 name a declaration that exists nowhere. Three name one that exists in a
**different namespace**, which is the more interesting failure because the block
looks wired:

| block's `lean.ref` | file actually declares |
|---|---|
| `QOU.BraidKnot.AtomKnot.unique` | `ConfinementLevel.unique` |
| `QOU.BraidKnot.KnotOperatorEnergy.unique` | `ConfinementLevel.unique` |
| `QOU.BraidKnot.QBetaCanonicalMarkovWeightsInstance.explicitInstance` | `CanonicalMarkovWeightsH3.explicitInstance` |

### Legit — the documented false-positive mode

`genus_ideal_characterisation` (`Ideal.mk_ker`), `bring_trefoil_cinquefoil_channel`
and `electroweak_triplet_bring_embedding` (concrete `decide`/`omega` on genus
arithmetic), `AlgebraicMassFormula` (`rw; field_simp`), `spectral_sum_finite`.
Content in the definitions, not absent.

## Static coverage after this work

8 of the 74 closed hits are now caught by static detectors — 5 of them by
`proof-no-unused-hypothesis-rfl`, added from this sweep's findings. The
remaining 66 need the elaborating oracle, or new criteria.

Two detector gaps were closed along the way, both found by this sweep rather
than by any gate:

- **`proof-no-unused-hypothesis-rfl`** (new): `rfl` consults no hypothesis, so a
  provable decl whose body reduces to `rfl` while binding an explicit `(h : …)`
  absent from its conclusion proves that conclusion for every value of `h`.
  15 hits.
- **ascribed-literal tautologies**: the reflexive check compared `(0:ℝ)` to `0`
  textually and let every ascribed literal through — 12 numeric claims
  (`colour_sector_count : (3 : ℕ) = 3 := rfl`, `exactly_two_one_dim_irreps`,
  the (3,1) branching multiplicities, `plancherel_via_recipe`) whose content
  lives entirely in the declaration name and the `--` comments.

## Scope

Scope-**(a)** per AGENTS.md §"Before declaring refuted": the *Lean* for the
findings above carries no content. **Not** a claim that the underlying
mathematics is wrong.

No declaration was edited. The honest disposition (prove / state with `sorry` +
`-- Ref:` / demote to `conjecture`, per §1a) is a per-item judgement.

## Reproducing

```sh
for i in 0 1 2; do
  bun run folio-assistant/content/pipeline/lean-triviality-probe.ts \
    --lake-root content/quantum-observable-universe/lean \
    --limit 5000 --shard $i/3 --checkpoint 5 --resume \
    --out /tmp/triv/shard-$i.json &
done; wait
bun run folio-assistant/content/pipeline/lean-triviality-probe.ts \
  --merge /tmp/triv/shard-0.json,/tmp/triv/shard-1.json,/tmp/triv/shard-2.json \
  --out docs/audits/lean-triviality.json
```

~3h at 3-way on 4 cores. Checkpoints every 5 results; `--resume` makes an
interrupted run cost minutes. That mattered — the shards were killed by a
container suspension mid-sweep and resumed from checkpoint with nothing lost.

**Known wart:** `--merge` warns `duplicate skip across shards:
QOU.Eightfold.WeylInvarianceQDeformation`. Two content blocks
(`a2-from-three-strands.ts`, `q-deformation-weight-lattice.ts`) share one
`lean.ref`; the partition is over blocks, the output keyed by declaration.
Benign — the warning is deliberate rather than silently keeping one.
