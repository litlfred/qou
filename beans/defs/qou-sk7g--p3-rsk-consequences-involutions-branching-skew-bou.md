---
# qou-sk7g
title: 'P3: RSK consequences — involutions, branching, skew bound'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T07:03:46Z
updated_at: 2026-08-08T07:05:02Z
blocked_by:
    - qou-7ga7
---

Three sorries in `QOU/BraidKnot/YoungTableauStandard.lean`, all discharged
once RSK exists:

- `sum_dimSYT_eq_involution` (117) — Σ_{λ⊢k} f^λ = I(k). Sagan §3.1.
- `branching_two_one` (125) — branching rule at μ=(2,1). Sagan Thm 3.10.2.
- `skew_le_straight` (133) — skew SYT inject into straight. Sagan §4.

Blocked on P1.

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
