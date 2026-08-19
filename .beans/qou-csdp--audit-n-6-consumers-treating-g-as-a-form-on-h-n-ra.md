---
# qou-csdp
title: Audit n >= 6 consumers treating G as a form on H_n rather than TL_n
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:39:30Z
updated_at: 2026-08-16T11:39:30Z
---

Related: `qou-cds2` (S2 — the Gram singularity), `qou-8iru` (the TL
identification), `qou-o3ta` / `qou-y6h7` / `qou-m7py` (all **n = 3** only).
Sibling to the all-n vanishing lemma tracked as `qou-smtg` step 2.

## The measurement

Under convention D (`z_D = q³/(q²+1)`) the Markov–Gram form on `H_n(q)` has
radical the Temperley–Lieb ideal, so `dim H_n/rad = Catalan(n)` and the
annihilated dimension is `n! − Catalan(n)`:

| n | dim `H_n` = n! | Catalan(n) | null dim | **null fraction** |
|---|---|---|---|---|
| 3 | 6    | 5   | 1   | 16.7 % |
| 4 | 24   | 14  | 10  | 41.7 % |
| 5 | 120  | 42  | 78  | 65.0 % |
| 6 | 720  | 132 | **588** | **81.7 %** |

At n = 6, **81.7 % of `H_6` is annihilated.** The four corank points
`1 / 10 / 78 / 588` are exact (PR #5207, merge `05a3178ab9`); n = 6 was the
discriminator named in PR #5187.

## Why this is a correctness question, not an efficiency note

The extra 588 dimensions are **null, not slow.** A consumer that treats `G`
as a form on `H_n` is not doing more arithmetic than necessary — it is
pairing against directions on which the form is identically zero. Any
quantity it derives from those directions is meaningless rather than
imprecise, and nothing in numpy or the Rust engine raises: the same failure
mode `qou-cds2` measured at n = 3 (`det 3.998e-17`, `cond 4.9e16`,
`‖G·G_INV − I‖ = 1.64`, **numpy silent**) gets worse monotonically in n.

Every existing bean on this form is **n = 3**: `qou-cds2` is the `gram.py`
6×6 singularity, `qou-m7py` the Rust `TR_M[5]` coupling, `qou-y6h7` the LP
sentinel. None of them looks at the high-n regime, where the fraction is the
problem rather than the single null direction.

## Status — this is a GUARD, not a live repair

**S2 surveyed the existing consumers and found none arithmetic-dependent on
the annihilated subspace.** So no defect is being asserted here, and none
should be inferred: the bean exists so that the *next* thing built at n ≥ 6
does not silently pair against 588 null directions.

## Priority: normal, deliberately not high

Argued rather than assumed, since the number invites "high":

- **For normal.** No live defect. The corpus is currently clean by S2's
  survey, and a high-priority slot spent on a guard displaces work on
  something actually broken.
- **For high.** The blast radius if missed is total — a wrong answer, not a
  noisy one — and it grows with n.

Resolved to **normal** because "no live defect" is a measured finding, not an
assumption. **Escalate to high the moment any consumer at n ≥ 6 lands**, or
if a re-survey contradicts S2's.

## What to do

1. Re-run the consumer survey rather than trusting S2's (per the repo's
   "measured, not maintained" discipline) — enumerate everything that pairs
   through `G` at any n, not just the `pyhecke.gram` re-exporters catalogued
   in `qou-cdh2`.
2. For each, decide explicitly: does it need the form on `H_n`, or on
   `H_n/rad = TL_n`? Record the answer at the call site; "it happened to be
   fine at n = 3" is not an answer for n = 6.
3. Prefer routing new work through the quotient (`gram_quotient_inverse`)
   from the start, so the question does not recur per consumer.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI
(the binary is not shipped in cloud sandboxes; `scripts/install-beans.sh`
is the fix). Measurements: PR #5207 / merge `05a3178ab9`; PR #5187's
weight table; `qou-8iru`'s n = 2..7 sweep (worst residual 1.34e-51).
