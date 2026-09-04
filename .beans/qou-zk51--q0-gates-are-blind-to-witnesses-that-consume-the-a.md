---
# qou-zk51
title: q0 gates are blind to witnesses that consume the anchor but record only derived numbers
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T08:24:15Z
updated_at: 2026-09-04T08:25:03Z
---


## The gap, measured

The 2026-08-22 muon-anchor re-pin (`fca08de7d2`, owner ruling: A → CODATA
2022) is drained under `qou-3f7a` through two gates. **Both key on a q₀
literal or stamp being PRESENT in the witness:**

- the **anchor-flip** gate reads the `q0Anchor` / `q0Value` pair;
- the **value-drift** gate reads q₀ literals appearing anywhere in the file.

Neither can see a witness that carries **no q₀ field at all** and records only
quantities **derived** from the anchor. That drain audit's summary — *"a pure
re-stamp for group M"* — is correct for the population it scopes and simply
does not describe this one.

The **route** is already detected: `q0_witness_read_dataflow_audit.py` finds
producers inheriting q₀ by *reading* a pinned witness (filesystem, not
imports). What it reports is **straddles**. Nobody had asked the *staleness*
question about the single-pin muon readers it counts.

New detector: [`computations/audits/muon_anchor_reader_invisible_staleness_audit.py`](computations/audits/muon_anchor_reader_invisible_staleness_audit.py)
(6/6), witness `muon-anchor-reader-invisible-staleness.witness.json`.

    producers NAMING the anchor (upper bound)     86
    paired to a witness by scriptFile provenance  65
      ... the same pairing BY FILENAME STEM       31
    witness carries a q0 literal or stamp         51
    carries neither, computed at/after the re-pin 10
    AT RISK: carries neither, predates the re-pin  5

## Why 0.0769 ppb is not a small number downstream

A witness reporting a **ppb-level residual** reports `(v − target)/target`, a
near-cancellation: a relative perturbation of `v` is divided by the residual's
own relative size. Measured on the one confirmed member:

| | |
|---|---|
| q₀, A → C | rel **+0.0769423 ppb** |
| `qbeta-ladder-convention-fee` muon row | 7.336484242 → 7.133936641 ppb, **−2.7608 %** |
| amplification | **3.588e8×** |

Reproduced by evaluating the published ladder at A and at C — to every digit
the witness carries. Its producer reads `derived_50_digit.q` straight out of
the anchor file; its committed witness on `main` had **no `q0Anchor`, no
`q0Value`, and no q₀ literal anywhere**, so neither gate could ever have
flagged it. It was found only because an **unrelated docstring edit** drifted
its `scriptHash`.

## Re-running the at-risk five: TWO causes, not one

2026-09-04 at HEAD, each baselined from `git show origin/main:<w>` (never from
the working tree), volatile keys masked, tree restored by name. **All five
moved.**

**Anchor-class** — the re-pin; own assertions still pass:

- `lambda-scale-derivation-probes-123` — up to **~210 ppb** on
  `delta_lambda_pn` and the strange-baryon λ's (≈2700× the anchor's own shift)
- `qbeta-c3-per-block-categorical-probe` — ~0.60 ppb on χ at q₀ (≈7.8×)
- `fvk-selection` — ~0.079 ppb on `I_F_lower_bound` (≈1×)

**Convention-class** — *not* the anchor; convention C → D reaching the import
cone — and **both record a green a fresh run does not reproduce**:

- `qbeta-symbolic-tbeta-min-l2` — `allPassed` true → **FALSE**; `A_q_symbolic`
  `sqrt(q)`-form → `q**3/(q**2+1)`
- `qbeta-markov-trace-norm-probe` — `allPassed` true → **FALSE**; L2 residue
  `6.85e-14` → `3.48e-9`

Reading all five as anchor drift would misattribute the larger half.

## What is NOT claimed

1. **The two convention-class producers are not asserted broken.** A C-frame
   assertion failing under D is what AGENTS.md and
   `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` predict — the ladder must be
   **re-derived** under D and a z-substitution is not a valid move. The finding
   is a **stale green**, and its remedy is the `qou-cds1` re-derivation.
   **Refreshing these two would commit a red.**
2. **`fvk-selection` is not asserted mis-stamped by intent.** It stamps
   `q0Anchor: independent` with reason *"no q0-dependent field in this
   witness"*, and its numbers move ~1:1 with the anchor. Both cannot be right;
   which is wrong is not settled here.
3. **Nothing refreshed, nothing wired.** Scope-(a); all five restored.

## Two measurement traps this had to survive

- **Stem pairing fails silently, on this very class.**
  `qbeta_ladder_convention_fee_probe.py` emits
  `qbeta-ladder-convention-fee.witness.json` — no `-probe` suffix — so a
  filename-stem match cannot see the one confirmed member of the class being
  measured. 31 vs 65 paired; the "a gate can see it" bucket 21 vs 51. **Pair on
  `scriptFile` provenance, never on the name.**
- **The audit counted itself.** A scanner *names* the anchor filename in order
  to look for it, so a filename scan cannot separate *"consumes the value"*
  from *"greps for the name"* — the reader total read 87 before self was
  excluded, and the other q₀ audits are still in it. Read that figure as an
  **upper bound**. The at-risk bucket is unaffected: every member was confirmed
  to consume the value by re-running it.

## Still open

- Whether `fvk-selection`'s `independent` declaration or its q₀ sensitivity is
  the wrong one.
- Whether the three anchor-class witnesses should be refreshed now or wait for
  the `qou-3f7a` tranche — **not** taken here, because that tranche is another
  session's live work.
- Whether the gate should be extended to key on *producer dataflow* rather than
  on a literal's presence. That is the general fix and it is larger than this
  bean.

Found while closing a loose end in PR #6606 (`qou-99qc`), where I had written
*"it is upstream; I do not assert which upstream."* It was measurable.
