---
# qou-a9li
title: 'EM-linking crossing-number MINIMISATION crux (from qou-0hdx): Freedman-He''s asymptotic crossing number is MINIMISED over homotopies, so the computed ACN=1.643 is an UPPER bound and minimisation moves it FURTHER from the required 3.99-4.79 — UNLESS the minimisation is constrained to the complement of the third Borromean component, where Brunnian-ness could hold it up. Unconstrained the pair is an unlink (min 0). Resolving which minimisation is physically correct decides whether the per-pair crossing-number route is dead or alive'
status: completed
type: task
priority: normal
created_at: 2026-08-01T21:25:43Z
updated_at: 2026-09-02T21:41:57Z
---

## BODY BACKFILLED 2026-09-02 — this bean was `completed` with no body for a month

Closed 2026-08-01T21:47:37Z carrying its answer nowhere. Recording it here, because
a `completed` bean whose conclusion exists only in an audit doc is exactly what
corpus-grep path 6 warns about — and it cost a session to rediscover.

**The crux as posed is malformed, and the underlying question resolves against (a).**

The bean asks whether the Freedman–He minimisation for a Borromean **PAIR** is
unconstrained (pair is an unlink, inf = 0, route dead) or constrained to the
complement of the third component (Brunnian-ness holds it up).

There is **no pair minimisation**. Verified against the primary source
`library/arxiv-0808.1533v1/sections/sec-001-energy-bound.md:203-216` (Komendarczyk
eq. 43, p. 26): the invariant in the link bound is `ac(L_k, L)` — one component
against the whole link, summed over the `n` components. No `ac(L_i, L_j)` occurs in
Komendarczyk or Khesin. Khesin's Rmk 3.5 gloss about "two given space curves" is the
two-curve warm-up, not the invariant used in the bound.

The (a)-vs-(b) intuition nonetheless resolves **against (a)**: eq. (43)'s own text
bounds `ac(L_k, L)` below by "a smallest genus among surfaces in
`R^3 \ {L_1 ∪ … ∪ L̂_k ∪ … ∪ L_n}` with a single boundary component" — a genuine
complement constraint, so Brunnian-ness does hold the value up. But via a
**single-component genus in the complement**, not via a constrained pair homotopy.

So `ACN = 1.643` is the wrong object with the wrong sum, and the correctly indexed
answer is `1 <= ac(L_k, L) <= 3.285` per component, `3 <= sum_k <= 9.856`
(`computations/em-linking-fh-link-bound-correction.witness.json`). The `genus >= 1`
step is the correcting agent's inference from `mubar_123 = 1 != 0`; neither source
computes it.

Parent bean `qou-0hdx` is **scrapped** (2026-09-02) — full record and the second,
independent correction (there is no `Vol^{-1/3}` factor in the link bound) are in
its body.
