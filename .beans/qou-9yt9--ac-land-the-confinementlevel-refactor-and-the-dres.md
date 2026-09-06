---
# qou-9yt9
title: 'A+C: land the ConfinementLevel refactor and the DressedParticle shadowing fix'
status: in-progress
type: task
priority: high
created_at: 2026-09-06T09:08:06Z
updated_at: 2026-09-06T09:45:12Z
---

## Landed (A + C)

**A — ConfinementLevel refactor.** `level_canonical` deleted; `valid` is now a
parameter indexed by `BraidDatum` with `level_valid`/`level_min` as proof
fields. `unique` is a one-line theorem, `nonempty` a real `Nat.find`
construction, `level_eq_find` new. **No axioms at all** on all three — not even
`propext`. Registered in the axiom guard, exit 0.

Also repaired `prop:confinement-level-exists`, unplanned: its Lean backing was
the junk record `⟨0,1,0,0⟩`, proving the *type* inhabited rather than that any
braid has a level.

`.md` rewritten: its three stated reasons over-attributed — uniqueness needs
only antisymmetry, and neither monotonicity nor upward-closure does any work in
it. Both kept, correctly scoped.

**C — DressedParticle unshadowed.** The library had already done the refactor
its sibling called "pending" (`shell_on_bare`, `level_preserved` as proof
fields; `dressing_composes` proved from them). Sibling replaced by a witness
extract, matching the pattern `confinement-level-exists.lean` already used.

Axioms 136 → 134, flagged 21 → 19. All touched files lean-direct exit 0;
`check-sidecars` exit 0.

## Two traps recorded

1. **The root `.lake` olean tree precedes the paper's in `LEAN_PATH`**, so a
   `lean-direct-cone.sh` rebuild into the paper tree is INVISIBLE — the stale
   root copy shadows it. Three files reported spurious unknown-identifier errors
   until the paper tree was put first. Root olean 09:08:28 vs source 09:09:25 vs
   paper-tree olean 09:11:28.
2. **`check-sidecars.sh` prints `→ refresh` UNCONDITIONALLY** for every changed
   content-block `.lean` (line 107). It is an advisory reminder, not a staleness
   verdict, and it does not set the failure flag. I misread it as a failure for
   several turns; the discriminator is the `⚠` lines and the exit code.


## NINTH false axiom — `KnotOperatorEnergy.shadowPrice_canonical` (same class, refactored)

`climax-volume-mass/knot-operator-energy-unique.lean`. Plain structure with
`shadowPrice : R` free; the axiom asserted two records agreeing on
`partition` and `q` share it. Refuted by `⟨[],0,0,none⟩` vs `⟨[],0,1,none⟩`.
**Third docstring in this family to name its own defect** — *"requires ... a
structure refactor carrying the LP-canonicity as a proof field."*

Same three-way pattern as #7: false uniqueness axiom **plus** a junk-record
existence witness (`{partition := [1], q := 0, shadowPrice := 0}`), so
`prop:knot-operator-energy-exists` was vacuously backed too.

**Applied the owner's A ruling by analogy** — same defect class, and no library
counterpart exists (unlike #8), so the refactor was the only option that keeps
the claims. One design choice worth naming: the determining data is carried as
a **function** `dualValue : List ℕ → R → R` with `shadowPrice_eq`, NOT as a
relation with a uniqueness field. A structure carrying its own conclusion would
be the self-assuming projection AGENTS.md §3b-cond item 5 forbids; here
uniqueness follows from functionality.

The real content — that the LP dual exists and is unique (Schrijver §7.4) — now
sits explicitly in the `dualValue` parameter a caller supplies, instead of
being smuggled in by a witness that ignored its own indices.

Axioms 134 → 133, flagged 19 → 18. All three blocks lean-direct exit 0,
zero axioms; check-sidecars exit 0.

## The docstring sweep — a useful NEGATIVE

Grepping `"proof field" | "not free data" | "does not enforce"` across
`content/` returns 11 files; excluding Mathlib and the already-fixed ones, only
**one** new instance (this ninth). So this family is **three** — #7, #8, #9 —
not an open-ended class. That is a cheaper and far more specific detector than
the over-quantification rules, because it keys on the author having ALREADY
noticed the defect and written it down.
