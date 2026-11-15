---
# qou-jhym
title: 'PI: Weierstrass factors -> canonical product -> Hadamard factorization'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T07:04:15Z
updated_at: 2026-08-08T07:05:04Z
---

Three sorries in `QOU/Mathlib/HadamardFactorization.lean`, a single chain,
INDEPENDENT of the tableau work (P1-P5) — can proceed in parallel.

- `norm_one_sub_weierstrassFactor_le` (131) — ‖1 − Eₚ(z)‖ ≤ ‖z‖^{p+1} for
  ‖z‖ ≤ 1. The convergence-critical estimate. File: "Not elementary."
  Follows from Eₚ(z) = 1 − Σ_{k>p} a_k z^k with a_k ≥ 0, Σ a_k = 1.
- `multipliable_canonicalProduct` (141) — needs the above plus the
  log-summability criterion for infinite products.
- `hadamard_factorization` (161) — Hadamard's theorem itself.

Mathlib has 0 files matching Hadamard or weierstrassFactor. Do them in
order; the first is the smallest and unblocks the second.

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
