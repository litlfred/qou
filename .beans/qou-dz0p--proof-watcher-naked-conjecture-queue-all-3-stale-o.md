---
# qou-dz0p
title: 'proof-watcher naked-conjecture queue: all 3 stale; one hid a live empty-carrier shadow'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-23T02:19:21Z
updated_at: 2026-08-23T02:34:28Z
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


## LQG carrier: WRITTEN (the item left open above is now closed)

`lqg-entropy-qdim-partition-pole.lean` no longer holds the empty stub. It now
carries a §3b-cond axiomatisation, sorry-free, 13 declarations, `lean`-direct
**exit 0**.

**Structure — the class carries HYPOTHESES, the theorems DERIVE the conjecture.**

    Z1 qdim casimir s = ∑' n, qdim n * exp(-s * casimir n)      -- the actual sum

    class LQGEntropyQDimPartitionPole (qdim casimir : ℕ → ℝ) (lo hi : ℝ) : Prop
      lo_lt_hi, Z1_continuous, Z1_strictAnti, Z1_super (1 < Z1 lo), Z1_sub (Z1 hi < 1)

    theorem exists_unique_critical : ∃! s, s ∈ Icc lo hi ∧ Z1 s = 1

The class does **not** state the pole. `exists_critical` derives it by IVT;
`critical_unique` by injectivity of a strictly antitone function. That is
§3b-cond item 5 satisfied — the carrier holds analytic inputs, the theorem
concludes. Claim (3) is covered by `immirzi sStar = sStar / 2π` with
`immirzi_pos` and `immirzi_eq_iff`.

**A flaw caught before it landed.** The first draft hardcoded the window to
`[0,1]`. It compiled cleanly — and silently excluded the conjecture's own
expected answer: the standard Immirzi value `γ ≈ 0.237` gives
`s⋆ = 2πγ ≈ 1.49 > 1`. A carrier that compiles while ruling out the physical
solution is worse than no carrier. `lo`/`hi` are now class **parameters**, so an
instance must state its own window.

**Satisfiability witness included, and it is not decoration.** An *unsatisfiable*
carrier is as dangerous as a vacuous one — it makes every `[C] → …` downstream
vacuously true. `witness_pole` instantiates the class on
`qdim = (2,0,0,…)`, `casimir ≡ 1`, where `Z₁(s) = 2e^{-s}`, crossing 1 inside
`[0,1]` because `2 < e`. Labelled as a satisfiability check, **not** as the LQG
data — the established pattern from `MotivicGaloisCharacterTrivial.lean`. The
conjecture's real content — that the actual `q`-dimension data satisfies these
hypotheses — remains open with no instance.

Verified: `lean`-direct exit 0, 0 sorry, 0 axiom; QOU validate 21 issues = main's
own `1d3988bc31` baseline exactly, with zero gravity-spacetime / lqg / casimir
entries. No repoint needed — the block's existing ref already names this class.
