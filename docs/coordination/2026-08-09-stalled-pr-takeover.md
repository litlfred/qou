# Stalled-PR takeover — measured inventory (2026-08-09)

Owner instruction: *"take over stalled agent PRs"*. This file is the
measured starting point, so the takeover survives the session that opened it.

## Headline

**41 open PRs. All 41 merge cleanly into `main` — zero conflicts.** They are
stale, not broken. Every one is small: the largest contributes 7,071 lines,
the median well under 500.

> **Measurement caveat, stated because it bit me.** A first pass reported
> every PR as "67 commits behind, clean". That was an artifact: an earlier
> `git fetch --depth=1` had left the clone **shallow**, so `origin/main` held
> only 67 commits and every count was meaningless. Re-measured after
> `git fetch --unshallow`. Likewise, PR size must be the **three-dot** diff
> (`git diff origin/main...<branch>` = the branch's own contribution); the
> two-dot diff is dominated by main's progress and reports ~22,000 files for
> a four-file PR.

## Why they look worse than they are

The repo merges with **rebase** (AGENTS §8), so a merged PR's commits get new
SHAs on `main` and the originals stay distinct objects. Ancestry-based
"ahead" counts therefore inflate wildly — a branch can read 20,000 commits
ahead while contributing 27 lines. Judge these PRs by three-dot diff size and
merge cleanliness, never by ahead/behind.

## Inventory (three-dot: what each PR actually contributes)

Regenerate with:

```bash
git diff --shortstat origin/main...origin/<branch>
```

| PR | files | lines | branch |
|---|---|---|---|
| 4582 | 1 | 13 | charm-knot-production-reconcile |
| 3808 | 3 | 27 | mass-binding-errors |
| 4514 | 4 | 49 | burnside-bridge2-reindex |
| 4682 | 1 | 65 | quantum-observable-formalization |
| 2503 | 1 | 100 | keystone-dg-construction |
| 4589 | 3 | 151 | neutrino-mass-mechanism |
| 3805 | 2 | 166 | alien-calculus-surreal-integration |
| 4557 | 7 | 184 | bwse-rt-bwhecke-program |
| 4451 | 8 | 187 | copilot/build-pdf-of-main |
| 4562 | 2 | 205 | electroweak-even-tower |
| 4579 | 1 | 229 | continuant-reverse-divisibility |
| 4564 | 1 | 274 | su3-stabilizer-action |
| 4561 | 4 | 276 | hypercharge-twist-derivation |
| 4435 | 1 | 277 | qcollatz-three-odd |
| 4548 | 7 | 287 | burnside-encoding-bridges |
| 4515 | 3 | 297 | c3-exact-volume-boost |
| 4617 | 4 | 323 | deltalambda-submodularity-parallel |
| 4568 | 1 | 343 | pr-3683-pickup |
| 4685 | 10 | 377 | close-numsyt-hlf-bridge |
| 4597 | 3 | 378 | hypercharge-second-invariant |
| 4596 | 5 | 396 | theta-qcd-framing-phase |
| 4346 | 3 | 402 | z-c-k-f-map-keystone |
| 4409 | 3 | 447 | lean-cache-release-infra |
| 4618 | 4 | 487 | weak-isospin-t3-grading |
| 3807 | 13 | 524 | canonical-derivation-c-k |
| 4718 | 9 | 537 | agent-pr-4690-stall (tests) |
| 4608 | 4 | 554 | jpsi-boundstate-mass |
| 4584 | 9 | 607 | complex-mass-constituent-scaffold |
| 4614 | 5 | 614 | meson-fluxtube-operation |
| 4656 | 6 | 640 | stokes-multipliers |
| 4588 | 5 | 643 | 5two-habiro-tail-bar-odd |
| 4594 | 5 | 773 | charm-mass-projection |
| 4571 | 9 | 824 | whitehead-c-sigma-torsion |
| 4591 | 3 | 926 | tau-mass-complex-volume |
| 4532 | 15 | 1292 | whitehead-vc-squeeze-bricks |
| 4684 | 4 | 1574 | binding-mass-derivation-gaps |
| 4600 | 43 | 2204 | agent-task-662242 (beans) |
| 4133 | 110 | 3519 | mass-theory-binding-prolongation-kernel |
| 4766 | 20 | 4558 | binding-channel-convention-exposure |
| 4673 | 40 | 5641 | convention-systematic-audit |
| 4565 | 82 | 7071 | generation-bridge |

## Clusters

1. **Infra** — 4718, 4409, 4451, 4568
2. **Lean / Mathlib bridges** — 4685, 4548, 4514, 4532, 4571, 4579, 4435
3. **Convention / trace / binding** — 4766, 4673, 4617
4. **Standard-Model gap probes** — 4561, 4562, 4564, 4565, 4582, 4584, 4589, 4591, 4594, 4596, 4597, 4608, 4614, 4618
5. **c_k / Stokes / Habiro + old keystone** — 2503, 3805, 3807, 3808, 4133, 4346, 4515, 4588, 4656

## Dispensed so far

| PR | action | outcome |
|---|---|---|
| **4834** | opened | convention-D ruling, Lean, `qou-w2d7`, registry — see its description |
| **4766** | coordinated | its `N_eff ≈ 2.5995` exclusion of C upgraded to a theorem for **every** `N` (`zC_not_fibre_family` + `zRank_eq_qpow_div_qInt`); correction posted that binding is not settled on C |
| **4718** | reviewed + measured | fix is real (**+12 tests, −2 collection errors**, A/B on current main with numpy present) but the *"59 of 86 test files"* headline **does not reproduce**; the figure is also in the shipped `conftest.py` docstring. Offered to take it over and correct both claims. |

## Verification posture for this takeover

CI auto-triggers are disabled repo-wide (AGENTS), so each PR needs its own
agent-run evidence before merge, and **merging needs the owner's explicit
per-PR go** (AGENTS §7). "Merges clean" in the table above is a statement
about `git merge-tree`, not a claim that any PR is correct.

Two traps worth carrying into the remaining work, both hit in the first hour:

- **Running the test suite mutates the tree.** `pytest computations/`
  regenerated four `*.witness.json` files as a side effect. Check
  `git status` after any collection run and revert what you did not intend.
- **Headline claims in stale PR descriptions have drifted.** 4718's was
  written 544 commits ago. Re-measure before repeating a number in a merge
  rationale.
