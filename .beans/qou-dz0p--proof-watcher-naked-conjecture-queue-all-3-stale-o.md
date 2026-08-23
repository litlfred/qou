---
# qou-dz0p
title: 'proof-watcher naked-conjecture queue: all 3 stale; one hid a live empty-carrier shadow'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-23T02:19:21Z
updated_at: 2026-08-23T02:20:01Z
---

The proof-integration-watcher queue's **only** three genuinely open items were all
`naked-conjecture`. All three are **stale against the corpus**, and checking them
turned up one live defect the finding text actively pointed away from.

(Filter note: the other three watcher queues are entirely `wontfix`/`resolved`.
`wontfix` is a **closed** disposition — a naive `status not in {done, resolved,
closed}` filter counts all 121 of them as open. Mine did, for one command.)

## All three findings are stale

| block | queue said | on disk |
|---|---|---|
| `mass-endomorphism/conj-rho-k-pair-gen-canonical-form` | ref names `pair_gen_kashaev_limit`, not found | ref names `PairGenCanonical`; sibling declares exactly that, **content-bearing**, docstring says it already *fixed* a prior vacuous field. `pair_gen_kashaev_limit` appears **nowhere** in the corpus |
| `appendix-surreals/casimir-first-q-correction` | `sibling.lean=NO`, decl not found | sibling **exists**; a Lake-tree file declares the real work |
| `gravity-spacetime/lqg-entropy-qdim-partition-pole` | "conjecture has no lean.ref", `sibling.lean=NO` | ref **is** `qou:QOU.GravitySpacetime.LQGEntropyQDimPartitionPole`; sibling **exists** |

All three were fixed after the queue's `source_sha` (`565be78e866d`) and the queue
was never updated. Had I taken the queue's advice at face value —
*"auto-dischargeable by authoring a `class` stub"* — I would have written a
**third** empty carrier on top of two that already exist.

## The live defect: an empty carrier shadowing 14 real declarations

`casimir-first-q-correction.lean` (sibling) is, in full:

```lean
class FigureEightCasimirWeight where
  -- axiomatisation stub
```

Zero fields — a `proof-no-empty-prop-carrier` **critical** under §3b-tax; any
`instance : _ := ⟨⟩` discharges it. Meanwhile
`lean/QOU/AppendixSurreals/FigureEightCasimirWeight.lean` carries **14
declarations**, 12 sorry-free theorems plus a genuinely content-bearing
`class FirstInteractingCasimirCorrection` (`weight : ℝ → ℝ` +
`weight_eq_jones41`), with four conditional theorems.

Because the sibling is resolver **candidate 1** (AGENTS.md §0a), the block's
`lean.ref` resolved to the **empty stub** and every tool following it landed
there. Same pattern removed on #5462.

**The block's own `authorNotes` name the right carrier** — "the carrier
identification is additionally class-axiomatised in the same file
(`FirstInteractingCasimirCorrection`, the §3b-cond pattern)". So the prose knew;
only the machine-readable ref pointed at the stub. And the `.md`'s "exact field
identity" for `J_{4₁}(q) = 1 + (3/4)h² + h⁴/(4(h²+8+4(q+q⁻¹)))` **is** the Lean
`jones41_taylor`, verbatim.

Fixed here: stub deleted, ref repointed. Verified — the Lake-tree file compiles
`lean`-direct **exit 0, 0 sorry, 0 axiom**; QOU validate is 21 issues, i.e. main's
own `1d3988bc31` baseline exactly, with **zero** casimir/appendix-surreals entries.

## Left open, deliberately: the LQG block

`lqg-entropy-qdim-partition-pole.lean` is the same empty-stub shape —

```lean
class LQGEntropyQDimPartitionPole where
  -- axiomatisation stub
```

— but there is **no Lake-tree twin**, so the stub is the only formalisation and
there is nothing to repoint to. Closing it means *writing* a content-bearing
carrier for the horizon-entropy-as-q-dimension-partition-pole conjecture: real
mathematics, not a repoint. Not attempted at 02:30 on an idle pass. It is a
genuine `proof-no-empty-prop-carrier` violation and should be claimed as its own
bean by whoever takes the LQG chapter.

## Queue hygiene

The three entries should be marked resolved (rho-k: already correct; casimir:
fixed here; lqg: re-scoped to the real work). Not edited here — the queue is the
watcher's artifact and rewriting it from outside a watcher run is how it drifted
in the first place.
