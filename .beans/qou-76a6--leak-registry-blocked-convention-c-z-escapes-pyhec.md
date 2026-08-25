---
# qou-76a6
title: 'LEAK: registry-blocked convention-C z escapes pyhecke into 25 production sites'
status: scrapped
type: task
priority: normal
created_at: 2026-08-10T03:43:41Z
updated_at: 2026-08-15T12:51:56Z
---


## What

`docs/coordination/trace-convention-registry.json` → `blocked_migrations` records
one deliberate exception to the convention-D excision:

    file:   tools/pyhecke/python/pyhecke/gram.py
    symbol: z
    stays:  C
    reason: G_INV = np.linalg.inv(G) runs at module import, and under D the
            Markov–Gram form on the H_3(q) NF basis is SINGULAR. numpy raises
            nothing — it returns entries up to 7.6e15 with ||G G_INV − I|| = 1.64.

That exception is sound only while the symbol stays inside its module. It does not:

    computations/substrate/hecke_core.py:61
        from pyhecke.gram import (z, W_SYM, W_STD, W_ALT, ...)

`hecke_core` is the shared substrate module. Production computations then do
`from hecke_core import z as Z_MARKOV` and use it as *the* Markov parameter.
Measured by `scripts/convention-c-producer-audit.py` (`scan_reexports`):

| | |
|---|---|
| modules re-exporting the blocked symbol | 12 |
| further consumers importing it from those | 13 |
| **production sites receiving convention C** | **25** |

Confirmed live, not inferred:

    >>> from hecke_core import z
    0.4993203341836945          # z_C
    z_D = 0.61268803714646525160

## Why every gate missed it

`is_c_form` shape-matches `1/(sqrt-ish + …)`. There is no arithmetic here — only
an import — so the AST audit reported **0 actionable sites** while the substrate
module handed convention C to every caller that asked for `z`. The registry's
containment was a statement about one file; nothing checked the file kept it.

## The blocker is now solved in principle

The registry's stated reason is that the Gram is singular under D. That is
exactly `MarkovGramDegenerate.wedderburnGram_det_eq_zero_of_dead` — `det G = ∏ y_λ`,
and `y_λ = 0` for every `ℓ(λ) ≥ 3` under D (7 of 11 dead at n = 6). It is not a
numerical accident to be worked around; it is the theorem.

The repair is named: `wedderburnGram_restrict_live_det_ne_zero` — restrict to the
live channels, which is `H_n/rad ≅ TL_n`, where the Gram *is* invertible. In
compute that is `computations/live_channels.py` (`live_channels`, `assert_all_live`).

So `pyhecke.gram` can move to D by inverting the live-channel restriction instead
of the full Wedderburn Gram. That was not available when the block was recorded.

## Next

1. Migrate `pyhecke.gram` to D with `G_INV` over live channels only.
2. Re-run the 25 sites' witnesses.
3. Remove the `blocked_migrations` row — and with it the leak.

Detector: `scripts/convention-c-producer-audit.py` (selftest 23/23, includes a
fixture asserting pyhecke's own modules are not reported as leaking).

---

## RETRACTED — the leak was never live (2026-08-15)

**The central claim of this bean is false.** It said 25 production sites
receive convention C through `hecke_core`'s re-export of `pyhecke.gram.z`.
They receive **D**. `gram.py:175` is `z = q0 ** 3 / (q0 ** 2 + 1)`, migrated
2026-08-15 under bean `qou-w8zz`, with `G` inverted on the quotient `H_3/rad`.

I measured it and reported it live:

    >>> from hecke_core import z
    0.4993203341836945

That was real — but it was run against a **five-day-stale checkout**, before
the migration landed. On current main the same import returns
`0.6126880371464652`. The 25 re-export sites are real and still exist; what
was wrong is what they carry.

### How the mistake was made

`scan_reexports` derives its verdict from the registry's `blocked_migrations`
row, and that row still said `stays: C` after the code moved. So the detector
faithfully reported a state that had ended. **A detector that trusts a record
inherits the record's staleness** — the same class of defect this whole
excision has been unpicking, arriving inside the tool built to find it.

The bean's closing claim, that "the blocker is now solved in principle" by
`wedderburnGram_restrict_live_det_ne_zero`, was right about the mathematics
and late on the facts: it had already been solved in practice.

### What survives

The structural point stands — the registry's containment was a statement about
one file, and nothing checked the file kept it. That is now enforced rather
than asserted:

- `_defines_convention_d(src, sym)` verifies the premise before any leak is
  derived from a row, and prints `REGISTRY STALE` when the file disagrees.
- classification is registry-derived, not path-prefix, which surfaced three
  genuine unexplained C sites the blanket had been hiding.

Continued as **`qou-2ixd`** (R9 red on main; registry corrected; the three
sites). Closing this one as retracted rather than deleting it — the failure
mode is worth keeping.
