---
# qou-g5oz
title: 'qbeta_level_k_binding_operator_probe is RED on main since the ordering ruling: both headline findings are grouped-only, and its witness still says allPassed'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T16:04:30Z
updated_at: 2026-10-04T15:23:01Z
parent: qou-9nnz
---

## Measured, both orderings, same probe internals

`binding_block` calls `atom_braid_word_3A(1, 1, ...)`, whose `intra_order`
default flipped from grouped to **borromean** on 2026-09-05 (`qou-hu1f`). The
committed witness is dated **2026-09-03** — two days earlier — and records
`allPassed: true`. Nothing has re-run it since.

Run today on a **clean tree** (verified by stashing my own edits):

    [FAIL] binding_character_is_largest_in_a_tl_kernel_block
    [FAIL] the_only_small_eigenphases_are_in_blind_blocks

Driving both assertions directly under each ordering:

| | grouped | borromean (canonical) |
|---|---|---|
| largest \|chi\| block | (3,2,1) at **-9.597856** | (3,1,1,1) at **2.4581026** |
| that block is TL-kernel | yes | yes |
| assertion (needs \|chi\| > 5) | **True** | **False** |
| small eigenphase blocks | (3,2,1) 0.02525, (2,2,1,1) 0.01955 | **none** |
| assertion | **True** | **False** |

`chi_(6) = 0.0085637314` is IDENTICAL under both — the one-dimensional visible
block is order-invariant, which is the internal check that this comparison is
sound rather than two different computations.

## What actually changes

1. **The magnitude claim.** The largest binding character is still in a
   TL-kernel block, so the qualitative reading survives; but it falls from
   -9.60 to 2.46, under the assertion's own `> 5` bar. The docstring's
   "chi_(3,2,1) = -9.598, the largest of any block" is a grouped-frame number.
2. **The small eigenphases are gone entirely.** Not moved, not reassigned —
   the canonical `Delta_bind` has NO eigenphase below 1 rad in any block. The
   docstring's "The first SMALL eigenphases found anywhere in this arc" and the
   table of (3,2,1) / (2,2,1,1) phases describe an object the corpus no longer
   builds.
3. **The 0.13 % coincidence is retired by this, not merely argued down.** The
   probe already recorded the 0.0448038 vs 0.0447444 agreement as "a target,
   not a finding" and gave a wall-artefact falsification. Under the canonical
   ordering the two phases do not exist, so there is nothing left to coincide.
   That is a stronger retirement than the one the probe argued for itself.

## What is untouched

The construction — `Delta_bind = beta_atom - beta_free` being genuinely
H_6-valued, and the TL dimension arithmetic (720 = 6!, 132 = Catalan(6)) — is
algebra, not a measurement, and does not move. The chain-vs-all-pairs finding
also survives: see below.

## The one part of this file I did change

`chain_word`, used only by the A = 3 ordering-dependence block, built the
grouped word by hand while its docstring called it "`atom_braid_word_3A`'s own
chain" (bean `qou-t29k`). So one file measured A = 2 canonically and A = 3 in
the superseded frame. Switched to `nucleon_word_letters`' default. Measured
first, and the finding is ROBUST:

    grouped    ord_spread = 22.54043935 %   ppn row = 0.2488, -6.581, -28.75
    borromean  ord_spread = 22.69262522 %   ppn row = 0.2488, -3.624, -2.978

Per-block characters move by up to an order of magnitude; the SPREAD across
nucleon orderings does not. The downstream assertion is a threshold
(`ord_spread > 0.1`), which both satisfy. Module docstring literal updated
22.54 % -> 22.69 %.

## Not done, deliberately

Nothing about the two red assertions. They are not a tolerance question and not
mine to resolve: either the headline readings are grouped-frame artefacts and
the docstring's central claims need withdrawing, or the canonical ordering is
wrong for this object. Choosing the frame that restores the result would be
selection against the target. This is the third site in `qou-t29k` whose result
is frame-conditional — after `qou-u8ji` (b_pred) and `qou-y1w0` (multibond) —
and the first that is already RED rather than quietly wrong.

## Environment note

This container was rebuilt with no Python environment; I installed mpmath,
sympy, scipy and clarabel. `mp.eig` returns a different shape under mpmath
1.3.0 than 1.4.1 and this probe CRASHES under 1.3.0 (`TypeError: cannot create
mpf from [mpf(...)]` at line 396). Pinned to 1.4.1, which is what the corpus's
most recent witnesses record. Nothing in the repo pins it.
