---
# qou-oacr
title: 'DOCS STALE: Specht module status tables claim STUB for cores that are proved'
status: todo
type: task
priority: high
created_at: 2026-08-08T09:58:48Z
updated_at: 2026-08-08T09:59:12Z
---


Several Specht modules carry "sorry-free ↔ stubbed map" tables whose **Status**
column is out of date. Verified 2026-08-08 with `#print axioms` and a grep for
the `sorry` tactic (not the word, which appears constantly in these prose
tables).

## The evidence

    grep -E '^\s+sorry\s*$' QOU/BraidKnot/SpechtStandardBasisCore.lean \
                            QOU/BraidKnot/SpechtDominanceCore.lean \
                            QOU/BraidKnot/SpechtTriangularCore.lean
    → no matches

    #print axioms QOU.BraidKnot.SpechtStandardBasis.standardBasis
    #print axioms QOU.BraidKnot.SpechtStandardBasis.standardPolytabloid_span
    #print axioms QOU.BraidKnot.SpechtStandardBasis.specht_finrank_eq_numSYT
    → all three: [propext, Classical.choice, Quot.sound]

So the Garnir straightening / spanning stub and the dominance core are **both
closed**, and have been for some time.

## What still says otherwise

- `SpechtStandardBasis.lean` — `standardPolytabloid_span` row reads
  "**STUB** `sorry` — `-- Ref: [sagan2001]` (Garnir straightening)"; the
  `standardBasis` and `specht_finrank_eq_numSYT` rows read "sorry-free MODULO"
  two cores. A dated ⚠ warning has been prepended to that table (2026-08-08);
  the rows themselves are unchanged, because they still correctly record what
  each declaration *depends on*.
- `SpechtFinrankWired.lean` — its whole rationale paragraph ("sources its
  linear-independence input from the *proved* triangular core rather than the
  opaque brick-2 stub … its **only** remaining sorry is the spanning /
  straightening stub") describes a state that no longer holds. The module is
  still correct and still useful; only the narrative is stale.
- `qou-0xyc` and `sp01` carried the same claim in their "Current status
  (2026-08-05)" sections. Corrected in place when those beans were closed.

## Why it matters more than a typo

These tables are what an agent reads to decide what is open. Bean qou-joo5's
corpus sorry audit lists `specht_finrank_eq_numSYT` among "12 classical
theorems, each a substantial formalization" — a multi-week estimate for
something already proved. Stale status text does not just misinform; it
manufactures phantom work items and hides real ones.

Related: qou-rc7b. There the failure is a *build target* that does not reach
half the tree; here it is *prose* that does not track the code. Both make a
verification artifact look like it is doing a job it is not.

## Todo

- [ ] Rewrite `SpechtFinrankWired.lean`'s rationale to the current state (or
      note that the module is now redundant with `SpechtStandardBasis` and can
      be retired).
- [ ] Rewrite the Status column in `SpechtStandardBasis.lean` rather than just
      warning above it.
- [ ] Re-audit qou-joo5's list against `#print axioms` rather than against
      docstrings; `specht_finrank_eq_numSYT` and `specht_isSimple` are already
      known to be wrong entries.
- [ ] Consider a CI check: for each declaration a status table calls a STUB,
      assert `sorryAx` really is in its axiom set. A table that can go stale
      silently will.
