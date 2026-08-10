# The 61 blocked edges are three problems, not one

Generated 2026-08-10. Bean: `cnd4`. PR #4921.

Two defects on this branch each produced correct `uses[]` edges that were
held rather than declared, because declaring them would add a forward
reference — a block depending on something stated later. This audit
measures what the held set actually consists of, and what would fix each
part. **The answer is not "61 decisions". It is three groups with three
different fixes, and only one of them needs the author.**

## The set

| origin | edges | what it is |
|---|---|---|
| `cnd4` | 19 | §3b-cond rule 4: an `.md` banner says "conditional on `conj:X`" but the manifest does not declare it |
| `prn1` corroborated scan | 37 | pruned edges the source's own prose still names |
| `prn1` tranche 1 | 5 | restored, went red on the sweep, reverted |
| **total** | **61** | |

The 5 are already reverted and not re-litigated below; the live measurement
covers the 56.

## The split that matters

A forward reference is checked by two different criteria, and only one of
them is wired:

| | edges | criterion | state |
|---|---|---|---|
| **same-chapter** | 39 | `detangler-no-forward-ref` | **live** — this is what turned three blocks red |
| **cross-chapter** | 17 | `detangler-no-xchapter-fwd` | **unwired stub** — `return { result: "n/a" }`, TODO since written |

`qa-checkers-extended.ts:1359` is the stub. Its sibling
`checkDetanglerArchimedeanWall` is a stub too. So cross-chapter forward
references are currently **unmeasured corpus-wide**, not merely unenforced
here.

**This is not a licence.** That the checker is off makes those 17 invisible,
not acceptable. Declaring a forward reference because nothing is watching is
the same move as copying an `interprets` label into `uses[]` to make a
checker see it — gaming the gate rather than recording a dependency.

## Group 1 — 35 edges: fixed by reordering, no editorial decision

Restricting each chapter's block graph to its intra-chapter edges **and
adding every held edge**, then testing for cycles:

| chapter | blocks | intra edges | result |
|---|---|---|---|
| `mass-theory` | 753 | 802 | **acyclic** |
| `predicted-spectra` | 295 | 269 | **acyclic** |
| `fluid-dynamics` | 96 | 123 | 2 cycles (3 blocks) |
| `appendix-surreals` | 98 | 99 | 2 cycles (4 blocks) |

An acyclic dependency graph **always** admits an ordering with zero forward
references — that is what a topological sort is. So for every held edge not
caught in a cycle, the edge is not the problem and never was: the block
order is. Reordering makes them all backward at once, and would take a bite
out of the paper's existing forward-reference count as a side effect.

This also explains why the per-block "just move it" test looked worse than
it is. Moving one target often exposes one of *its* dependencies:

```
conj:critical-exponent  -> blocked by conj:regularity-breakdown
conj:q-aubin-lions      -> blocked by conj:ns-counterexample
conj:ns-counterexample  -> blocked by prop:universality
```

Those are not four obstructions. They are one chain, and a topological sort
moves the whole chain in a single pass. Only 6 targets are free to move
individually (12 edges); the other 23 need the chain moved with them.

## Group 2 — 4 edges: genuinely circular, and only the author can resolve them

Four held edges do not merely point forward. They close a **cycle**:

```
prop:discrete-vortex-spectrum -> rem:vortex-intensity-modes
                              -> rem:planck-reynolds
                              -> prop:discrete-vortex-spectrum

rem:vortex-intensity-modes    -> rem:planck-reynolds
                              -> rem:vortex-intensity-modes

conj:archimedean-stpart       -> conj:classical-limit-stpart
                              -> conj:archimedean-stpart

conj:p-vs-np-qou              -> rem:p-vs-np-surreal-bound
                              -> conj:p-vs-np-qou
```

**No ordering fixes a cycle.** Reordering is a relabelling; a cycle is
invariant under it. Each of these says two blocks each depend on the other,
which cannot both be true as stated. One edge in each pair is wrong, or the
two blocks are really one block, or one of them is stating a consequence as
a premise.

Verified against three states, because a cycle I introduced would be my bug
to fix rather than a finding to report:

| | `fluid-dynamics` | `appendix-surreals` |
|---|---|---|
| `origin/main` | 0 cycles | 0 cycles |
| this branch as committed | 0 cycles | 0 cycles |
| **if the held edges landed** | **2 cycles** | **2 cycles** |

So the branch is clean, and these four are a reason the edges were right to
hold — the sweep that caught them caught something real.

`conj:p-vs-np-qou` is worth singling out because tranche 2 edited it. The
three edges added there (`def:reeb-epsilon`, `lem:surreal-squeeze`,
`prop:surreal-rate-calculus`) are **not** in the cycle. The cycle would come
from a held edge, and the `.md` supports reading the dependency the other
way: line 24 is *"See [Surreal bound for P vs NP] for the squeeze-inequality
statement **implied by** this conjecture"* — the bound depends on the
conjecture, not the reverse.

## Group 3 — 17 edges: cross-chapter, ungated, and a bigger question

These are not reachable by reordering blocks within a chapter; they would
need a block moved **between** chapters, or a chapter moved. That is an
editorial act of a different size, and the gate that would measure it does
not run.

The largest gaps sit here — `conj:magic-numbers-bring` at 1008 positions,
`rem:building-block-knots` at 1022, `thm:knot-mass-formula-unified` at 1119.
A `mass-theory` proposition declaring itself conditional on a conjecture
stated 1008 blocks later in `observations` is a real structural claim about
the paper, not a bookkeeping nit.

## Recommendation

1. **Group 1 (35) — produce the topological reorder as a reviewable diff.**
   Mechanical to compute, but it changes reading order, so it is proposed
   and not applied. Sequencing note: land the reorder *first*, then declare
   the edges, so no intermediate commit is red.
2. **Group 2 (4) — author call, one question each.** Which direction is
   real? Cheap to answer, impossible to compute.
3. **Group 3 (17) — hold.** Do not declare against an unwired checker.
4. **Wire `detangler-no-xchapter-fwd`** (separate bean). Until it runs,
   nobody knows the corpus-wide cross-chapter figure, and Group 3 cannot be
   prioritised against anything.
