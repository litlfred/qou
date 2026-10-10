---
# qou-jt65
title: 'P5: Specht simplicity and classification'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T07:04:14Z
updated_at: 2026-08-08T07:05:03Z
blocked_by:
    - qou-7tim
---

Three sorries, all downstream of the standard basis:

- `specht_isSimple` (Specht.lean:320) — S^μ simple over char-0 field.
- `spechtIso_imp_dom_both` (SpechtClassification.lean:449)
- `specht_exhausts_irreducibles` (SpechtClassification.lean:485)

Together these are the classification of irreducible S_n representations.
Blocked on P4.

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
