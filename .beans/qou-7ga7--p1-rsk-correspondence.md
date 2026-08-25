---
# qou-7ga7
title: 'P1: RSK correspondence'
status: scrapped
type: task
priority: high
created_at: 2026-08-08T07:03:46Z
updated_at: 2026-08-08T07:05:01Z
---

The Robinson-Schensted-Knuth correspondence. Absent from Mathlib (0 files).

Needed by `sum_dimSYT_eq_involution` (RSK restricted to involutions gives
Σ_{λ⊢k} f^λ = I(k)), and it is the natural home for the branching and
skew-tableau results.

## Sizing
Multi-week. Row insertion, the bumping algorithm, and the inverse map all
have to be defined and proved mutually inverse.

## Reasons for Scrapping

Duplicate. This work was already tracked, in more detail and further
along, before I filed this — I created it without checking for existing
beans first, which the project guidance explicitly requires.

Canonical trackers:
- `sp00` — EPIC: Specht/S_n formalization program, phase-ordered with
  children sp01–sp09. Already records `specht_submodule_dichotomy` (James
  submodule theorem) as fully sorry-free since 2026-07-05, and carries the
  real critical path: sp01 form_nondegenerate → specht_isSimple;
  sp02 straightening + sp03 triangular-relocation → sp04 finrank=numSYT;
  sp05 pairwise_noniso + sp06 exhausts → sp07; sp09 is the FRT
  hook-length brick.
- `qou-0ap1` — EPIC: Sₙ rep-theory infra build-out (Specht / SYT /
  hook-length / seminormal).
- `qou-v4if` / `qou-n4pv` — the Hadamard chain, already carrying the
  actual proof route for the PI-2 Weierstrass estimate.
- `qou-lbth` — complex-analysis Mathlib gaps.

Nothing here is lost: `qou-joo5` keeps the cross-cutting audit of all 14
sorries and now points at these.
