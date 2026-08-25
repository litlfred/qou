---
# qou-uf0p
title: 'P2: Frame-Robinson-Thrall hook-length formula (numSYT_mul_hookProduct)'
status: scrapped
type: task
priority: high
created_at: 2026-08-08T07:03:45Z
updated_at: 2026-08-08T07:05:00Z
---

`numSYT_mul_hookProduct (μ : YoungDiagram) : numSYT μ * hookProduct μ = (μ.card).factorial`
in `QOU/BraidKnot/StandardYoungTableau.lean:149`.

Stated multiplicatively so it lives over ℕ (no division). The file calls
this "the genuine formalisation target of this brick".

**Load-bearing.** Five other sorries reference `numSYT`; this is the
entry point that unblocks the most, and unlike the Specht work it needs
no representation theory to exist first.

Mathlib at the pinned rev has NOTHING to build on: 0 files matching
hook_length, numStandardYoungTableaux, or RSK.

## Known proof routes
- **Greene–Nijenhuis–Wilf hook walk** (probabilistic). Shortest on paper,
  but needs a probability argument over tableaux.
- **Novelli–Pak–Stoyanovskii** (bijective). Most self-contained; builds an
  explicit bijection. Probably the best fit for Lean.
- **Induction via the branching rule.** Circular here — branching is
  itself one of the deferred sorries.

## Sizing
Multi-week. A plausible Mathlib contribution in its own right.

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
