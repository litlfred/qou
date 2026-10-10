---
# qou-7tim
title: 'P4: Specht standard basis (specht_finrank_eq_numSYT)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T07:04:14Z
updated_at: 2026-08-08T07:05:02Z
blocked_by:
    - qou-uf0p
---

`QOU/BraidKnot/Specht.lean:309` — dim_k S^μ = #SYT(μ). The standard
polytabloids {e_t : t ∈ SYT(μ)} form a k-basis. Sagan Thm 2.5.2.

Blocked on P2: the statement is *about* `numSYT`, so that side needs to
be developed first.

Mathlib has no Specht module theory at all — this builds from scratch on
the file's own `SpechtSubmodule` / `Mtab` scaffolding.

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
