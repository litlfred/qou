---
# qou-ondw
title: Re-pose the LP/SDP and trace compute on TL_n = H_n/rad instead of H_n
status: todo
type: task
priority: high
tags:
    - qbeta
    - hecke
    - compute
    - temperley-lieb
created_at: 2026-08-16T12:54:01Z
updated_at: 2026-08-16T12:54:01Z
---

## Why now

`QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` (PR #5217, sorry-free, all
`n` and all `r`) proves that at convention D the Markov trace annihilates
exactly the `ℓ(λ) ≥ 3` blocks. `MarkovGramDegenerate` proves `det G = 0`. So
the surviving quotient is `TL_n`, of dimension `Catalan(n)`, and the discarded
dimensions are **provably** null — not small, not negligible, null.

Any compute posed on all of `H_n` is therefore doing arithmetic in the kernel.
Re-posing on the quotient is simultaneously **faster and more correct**.

## The size of the prize

| n | `dim H_n = n!` | `dim TL_n = C_n` | ratio |
|---|---|---|---|
| 4 | 24 | 14 | 1.7x |
| 5 | 120 | 42 | 2.9x |
| 6 | 720 | 132 | 5.5x |
| 7 | 5040 | 429 | 11.7x |
| 8 | 40320 | 1430 | 28.2x |

The binding chain runs at `n = 3A`, so A = 2 is n = 6 and A ≈ 2.7 is n = 8 —
exactly the range where the mass/binding compute is currently painful. The
ratio above is on the *dimension*; wherever cost is superlinear in dimension
(Gram assembly, SDP, dense linear algebra) the saving is larger than the table.

## Scope — this bean is the producer-side move

Deliberately NOT owned by `qou-y6h7`. That bean investigated a suspected LP
degeneracy, concluded its own premise was wrong (a `_yc_floor` sentinel, not a
symptom), and explicitly disowned this work:

> *prf:operator-selection-lp is posed at d = n! (2, 6, 24, 120) while the rank
> under D is C_n (2, 5, 14, 42). That claim is corrected in the content and
> proved in MarkovGramDegenerate, but no producer has yet been re-posed on the
> quotient. **That is real work; it just is not what this witness shows.***

This bean is that real work. `qou-y6h7` keeps its two sentinel/guard items.

## Tasks

- [ ] Enumerate the consumers: every producer that builds a basis, Gram matrix,
      or LP/SDP indexed by partitions of `n` or by `n!` braid words. Record
      which run at `n >= 6`, where the cost actually is, and which already
      restrict to two-row `λ` by accident.
- [ ] Decide the representation of the quotient: restrict the partition index
      set to `ℓ(λ) <= 2` (cheap, mechanical, keeps the Wedderburn shape) vs a
      genuine TL diagram basis (larger change, better constants). Prefer the
      former first — provably equivalent, and a small diff.
- [ ] Re-pose `prf:operator-selection-lp` on the quotient. Emit primal AND dual
      per AGENTS.md §LP/SDP duals. Compare `primal_obj` against the `H_n`
      posing: they must agree, since the dropped channels carry weight zero.
      A disagreement is a bug in the re-posing, not a discovery.
- [ ] Remove the `_yc_floor`-style guards that only ever fire on the now-null
      channels; those channels should be *excluded*, not priced at 1e15
      (coordinate with `qou-y6h7`, which owns the sentinel-in-witness item).
- [ ] Benchmark before/after at n = 6 and n = 8 and record the **measured**
      speedup, not the table above.

## Guard — do not over-apply the quotient

The weight vanishing is a statement about `tr_M`. It licenses dropping a block
from a **trace-weighted** sum; it does NOT license dropping it from a dimension
count, from a normalisation sum such as `Σ_λ f^λ y_λ = 1`, or from any
intermediate that is not trace-weighted. Check each call site for what it is
actually summing before deleting an index.

Second guard: the vanishing is proved **at convention D**. Convention C is a
different Markov parameter and the survivor set there is not the same (see the
level-family work, PR #5229). Do not apply this quotient to a C-frame producer.

## Related

- `qou-y6h7` — the disowning bean; owns the sentinel + guard-audit items.
- `qou-8iru` (in-progress) — the D-is-TL identification itself.
- PR #5217 / `docs/audits/2026-08-16-tl-all-n-weight-vanishing.md` — the proof.
- PR #5230 — axiomatises the Wenzl input the proof rests on.
