# The blocked edges are four problems, not one

Generated 2026-08-10, re-measured after rebasing onto `main` (+53 commits).
Bean: `cnd4`. PR #4921.

Two defects on this branch each produced correct-looking `uses[]` edges that
were held rather than declared, because declaring them would add a forward
reference — a block depending on something stated later. This audit measures
what the held set consists of and what would fix each part.

**Headline: it is not one decision, and most of it is not the author's.**
The largest single category turns out to be edges that should never be
declared at all — for a reason that has nothing to do with ordering.

## Re-measure after the rebase

| | before rebase | after |
|---|---|---|
| blocked forward edges | 56 | **50** |
| same-chapter (gated) | 39 | **33** |
| cross-chapter (stub) | 17 | 17 |

Six edges stopped pointing forward on their own when `main`'s 53 commits
landed. Any figure quoted from the pre-rebase pass is stale; this one
supersedes it.

## The four groups

| group | edges | resolution | needs the author? |
|---|---|---|---|
| **1. Overview-source** | 8 | **reject the edge** | no |
| **2. Reorder** | 22 | 11 block moves | no (diff needs review) |
| **3. Cross-chapter** | 17 | hold | no |
| **4. Circular** | 3 legs → **1** real | editorial | **yes, one question** |

### Group 1 — 8 edges whose source is a chapter overview

Every one of these has its source in **§0**, the chapter's overview section,
and every source is a `remark`:

| source (§0) | pulls in |
|---|---|
| `rem:q-metric-contact-deformation` | `def:ns-obstruction`, `prop:core-levi-form`, `rem:hyperbolic-overlap-saturation`, `rem:townsend-biot-savart-strain`, `thm:q-ns-wellposedness` |
| `rem:planck-reynolds` | `prop:discrete-vortex-spectrum`, `rem:vortex-intensity-modes` |
| `rem:hecke-charge-mass-duality` | `def:vertex-operator` |

A chapter overview that surveys what is coming **names** later results; it
does not **depend** on them. The minimal-move computation exposed this by
reductio: to satisfy these edges it proposed moving `def:ns-obstruction`
from §4 to before position 9 — i.e. relocating a definition to sit ahead of
the chapter introduction that previews it. When the fix is absurd, the
constraint is wrong.

These are **corroborated** — the prose does name the targets — and still
wrong. That is exactly the caveat the corroboration audit carried:

> Corroboration is evidence for a **reading**, never a licence to populate:
> relatedness is not dependency.

This is the first concrete instance of that caveat biting, and it is the
largest single category in the held set. `rem:q-metric-contact-deformation`
was 5/6 corroborated — high on the priority list by fraction — and all five
of its held edges are rejected here.

### Group 2 — 22 edges fixed by 11 block moves

With Group 1 removed and the cycle legs set aside, the remainder is a
genuine ordering problem. `mass-theory` (753 blocks) and `predicted-spectra`
are acyclic; an acyclic graph always admits a zero-forward-reference
ordering. The minimal move set:

| chapter | edges | moves |
|---|---|---|
| `fluid-dynamics` | 12 | 4 |
| `mass-theory` | 8 | 5 |
| `appendix-surreals` | 1 | 1 |
| `predicted-spectra` | 1 | 1 |
| **total** | **22** | **11** |

The `fluid-dynamics` case is the clearest and accounts for over half:

```
conj:critical-exponent      §6 -> §4
conj:ns-counterexample      §6 -> §4
conj:q-aubin-lions          §6 -> §4
conj:regularity-breakdown   §6 -> §4
```

Four **conjectures** sit in §6 ("NS obstruction tower, specialisations, and
observable MTC") while propositions in §4 ("Global regularity for `q > 1`")
and §5 ("NS obstruction: statement and observability") declare themselves
conditional on them. A conditional result should follow the conjecture it is
conditional on, so the conjectures move up. Moving the whole of §6 would be
wrong — the tower genuinely builds on the statement; only the conjectural
inputs belong earlier.

This also corrects the per-block "just move it" reading from the first pass.
`critical-exponent` blocked by `regularity-breakdown`, `q-aubin-lions` by
`ns-counterexample` is **one chain**, not separate obstructions; the four
move together.

### Group 3 — 17 cross-chapter, and a checker that does not run

`detangler-no-xchapter-fwd` is an **unwired stub**
(`qa-checkers-extended.ts:1359`, `return { result: "n/a" }`; its sibling
`checkDetanglerArchimedeanWall` likewise). Cross-chapter forward references
are **unmeasured corpus-wide**.

That makes these 17 invisible, **not** acceptable. Declaring a forward
reference because nothing is watching is the same move as copying an
`interprets` label into `uses[]` so a checker sees it. Held.

### Group 4 — three cycle legs, one real question

No ordering fixes a cycle: reordering is a relabelling and a cycle is
invariant under it. Five surfaced initially; four dissolve without the
author:

| cycle | resolution |
|---|---|
| `prop:discrete-vortex-spectrum` ↔ `rem:vortex-intensity-modes` ↔ `rem:planck-reynolds` | dissolved — its legs are Group-1 overview edges |
| `rem:vortex-intensity-modes` ↔ `rem:planck-reynolds` | same |
| `conj:p-vs-np-qou` ↔ `rem:p-vs-np-surreal-bound` | dissolved — the `.md` says which way it runs |
| `conj:p-vs-np-qou` → `rem:p-vs-np-surreal-bound` → `rem:millennium-unification` → back | same leg |
| **`conj:archimedean-stpart` ↔ `conj:classical-limit-stpart`** | **open — author** |

For the p-vs-np pair, `p-vs-np-conjecture.md` line 24 reads *"See [Surreal
bound for P vs NP] for the squeeze-inequality statement **implied by** this
conjecture"*. The bound depends on the conjecture; the held edge is
backwards, and dropping it kills both cycles.

The remaining one is a genuine mutual dependency between two conjectures,
one leg already committed and one held. It needs a reading, not a
computation.

Verified the branch causes none of these: **0 cycles on `main`, 0 as
committed**; they appear only if held edges land.

## Recommendation

1. **Reject Group 1 (8).** Overview sections preview; they do not depend.
   Worth a general rule: a `uses[]` edge whose source is a §0 overview block
   is suspect by construction.
2. **Apply Group 2 (22 edges / 11 moves) as a reviewable diff.** Reorder
   lands first, then the edges, so no intermediate commit is red.
3. **Hold Group 3 (17)** until the cross-chapter checker runs.
4. **One question (Group 4):** which of `conj:archimedean-stpart` /
   `conj:classical-limit-stpart` depends on the other?
5. **Wire `detangler-no-xchapter-fwd`** — separate bean. Until it runs,
   Group 3 cannot be prioritised against anything.
