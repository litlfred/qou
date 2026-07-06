# Keystone geometric leg — formalize-first status + owner-gate (2026-06-19)

**Branch:** `claude/serene-cerf-j4d339` (PR #2500). Owner-directed item 3 of "1 2 3".
**Discipline:** corpus-grep "before declaring open" (STRICT) + critical-distance +
**no fabrication** (the construction is owner-gated; this doc records status, it
does **not** attempt a derivation).

## Corpus-grep: the geometric leg is genuinely OPEN (checklist run 2026-06-19)

1. `docs/audits/` — the geometric realization is recorded **open** in
   [`keystone-arena-is-full-hecke-not-su3.md`](2026-06-16-keystone-arena-is-full-hecke-not-su3.md),
   [`keystone-index-necessary-conditions.md`](2026-06-16-keystone-index-necessary-conditions.md),
   [`keystone-wu-manifold-reeb-obstruction.md`](2026-06-16-keystone-wu-manifold-reeb-obstruction.md).
2. `content/` — Reeb hits are substrate-contact / adelic-Reeb / the **refuted**
   Reeb-eigenvalue resonance; none realizes the full-Hecke Markov trace.
3. `computations/` — Reeb scripts are the refuted eigenvalue/phase probes
   (`reeb_rotation_pn_test.py`, `option_e_canonical_reeb_*`), not an index compute.
4. Coordination ledger [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
   marks it **"⛔ differential geometry (owner-gated)."**

All four paths agree: **open**. This session's items 1–2 do **not** close it.

## The corrected open object (single sentence)

> Does the **full-Hecke principal-specialization trace** `s_λ(1,q,q²,…)`
> (infinite-variable, intrinsically `p(3A)`-dimensional) admit *any* geometric
> realization whose `S¹`-equivariant index reproduces the canonical Markov
> weights — and a finite-dimensional (finite-`N` colour) Sasakian is **ruled out**?

## What items 1–2 tightened (this session)

- **Item 1 gives C6 ("full support") quantitative teeth.** The colour-`ℂ^N`-missed
  Wedderburn-block count is **unbounded + monotone in `A`**
  ([`ColourArenaBlockCount.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ColourArenaBlockCount.lean),
  sorry-free) ⇒ no finite-`N` arena captures the trace for all `A`. The index must
  carry **all `p(3A)`** blocks — a finite-dimensional Sasakian is ruled out
  *quantitatively*, not just by the single `3.4%` @⁴He data point.
- **Item 2 confirms C6 has no vanishing sectors from the combiner side.** Every
  block is reached
  ([`CombinerBranchingCompleteness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/CombinerBranchingCompleteness.lean),
  `exists_subpartition_of_size`).

So the necessary conditions are sharper, but the **construction** is untouched.

## The seven necessary conditions a valid index must satisfy

Unchanged from [`keystone-index-necessary-conditions.md`](2026-06-16-keystone-index-necessary-conditions.md)
(C1–C7); the two actionable levers remain **C2** (the chirality involution
`T₁↔T₂` is forced by exact `W_λ=W_{λ'}`) and **C4** (the index computes block
*dimensions* `d_q²`, not eigenvalues — retro-explains the refuted Reeb-eigenvalue
resonance). **C6** now additionally rules out *finite-dimensional* Sasakians.

## Owner-gate (no fabrication)

The construction is **research-grade infinite-dimensional differential geometry**
and is **owner-gated**: the coordination ledger declined substrate/geometric
subgoal-2 on 2026-05-08, and CLAUDE.md fences attempting it "without owner
reversal." Per the canonical-derivation / critical-distance discipline, this
session does **not** fabricate a construction — doing so would be exactly the
unfalsifiable correspondence-chain the Habiro lead already refused. The honest
terminus: the open object is now **correctly aimed and maximally pruned**; the DG
build itself awaits an explicit owner go/no-go.
