---
# qou-q5pf
title: 'Second laundering surface: pasted decimal literals in high-dps files (153 candidate files, defect rate UNMEASURED)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T20:22:55Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## Where this came from

Raised by the author of #6457 on #6489, from a real instance in their own
branch: `mp.mpf(str(mp.mpf("4.18598136329")))` for `E_0` in a 50-dps file,
where `E_0` is derivable as `m_e/(q_0(q_0-1))` off `codata_constants`. Their
point: a drain that greps for `q_parameter import Q` cannot see a pasted
constant, so it is a **second surface** to the `LAUNDERED` tier drained in
`qou-b7cf`.

## Measured extent — CANDIDATES, not defects

AST scan of `computations/**/*.py` (excluding `_deprecated`) for
`mp.mpf("<decimal>")` whose significant-digit count is at least 8 below the
working `mp.mp.dps` the file sets:

    files: 153   sites: 309

**The defect rate in that population is UNMEASURED, and the discriminator is
not mechanical.** A pasted literal is legitimate when the quantity is an
*experimental input* that genuinely has that many digits, and is a defect
when the quantity is *computable* and was pasted instead of derived. Sampled:

| site | verdict |
|---|---|
| `mpf("137.035999177")` in a 60-dps file | **legitimate** — CODATA alpha^-1, exactly 12 digits of input datum |
| `mpf("206.7682830")` in an 80-dps file | **legitimate** — CODATA m_mu/m_e |
| `mpf("1.109978595557334719899...")` (48 digits) | **legitimate** — a recorded q_0 |
| `mpf("7.327722906465")` in a **110-dps** file | **legitimate, and it is the trap** — `borromean_volume_100dps.py:132` pastes the ATLAS literature value at exactly its published precision, on purpose, to test whether a 1.85e-6 gap is a precision artefact. Deriving it would destroy the comparison. |

I picked the Borromean one out as the clearest suspect on shape alone — 13
digits in a 110-dps file — and it is a false positive. That is the same
lesson as class (b) in `qou-b7cf`: **measure the instance before calling the
shape a defect.**

## What a real drain would need

Not a grep. Per site: is the quantity computable from something already in
scope? That is a triage judgement, so the honest unit of work is a sampled
audit that estimates the defect rate first, and only then a drain scoped to
whatever that rate justifies. 309 sites at an unknown rate is not a sweep to
launch blind.

## Related

- `qou-b7cf` — the `LAUNDERED` tier (35 sites, drained).
- The upstream-refill problem #6457 names in the same comment: their fresh
  instance landed **while** `qou-b7cf` was reaching zero and was outside its
  file list. A drain that reaches zero on a moving `main` has not closed the
  class; only re-running the detector shows the live count.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8388, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
