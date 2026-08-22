---
# qou-ivhc
title: q0_consistency_audit is POLARITY-INVERTED after the proton ruling — it classifies the canonical pin as a stale-q0 bug, and has a --strict CI-gate mode
status: todo
type: task
created_at: 2026-08-22T15:27:20Z
updated_at: 2026-08-22T15:27:20Z
---


Found while tracing `qou-cds3`'s finding that 22 witnesses hold a muon value in a
`proton`-named field. The worst of those was
`computations/audits/q0-consistency-audit.witness.json`; this bean is its cause.

## The inversion

`computations/audits/q0_consistency_audit.py` docstring, verbatim:

> Canonical q₀ is the proton-anchored, habiro-refined value
> **C = 1.10997859555733471…** (`q_parameter.Q`). The stale value is the
> pre-habiro proton solution **A = 1.10997858275138…**, differing from C at the
> 8th sig-fig (~1.2e-8). Scripts that hardcoded A — instead of importing the
> canonical q₀ from `q_parameter` — silently keep computing at the stale
> constant.

Measured today:

```
q_parameter.Q_MP  = 1.10997858275138080759166909561076
Q_50_DIGIT_STR    = 1.10997858275138080759166909561076
```

So **`A` — the value this audit calls stale and flags as a bug — IS
`q_parameter.Q` today.** And `C`, which it calls canonical and attributes to
`q_parameter.Q`, is the hand-typed muon constant (`qou-khac`), itself measured
**8.54e-11 stale** against what `q_muon_at()` now derives.

The docstring's parenthetical *"(`q_parameter.Q`)"* is therefore false on its own
terms: the symbol it names holds the other value.

## Why this is not cosmetic

Three multipliers, in increasing order of consequence:

1. **It classifies correct code as a defect.** A hit on the canonical pin
   assigned to a live constant is classified `production-hardcode — real bug`.
   Every script that correctly hardcodes or reproduces `1.10997858275138…` is
   counted as a migration failure.

2. **It is built to become a CI gate.** From the same docstring: *"Run with
   `--strict` to exit non-zero when any production-hardcode remains (CI gate once
   the backlog is cleared)."* Enabling that gate today would **fail the build for
   using the canonical value**, and the backlog can never clear, because the
   thing it counts is now the correct thing to do.

3. **Its witness asserts the wrong canonical pin, with no way to notice.**
   `q0-consistency-audit.witness.json` carries
   `canonical_proton_q0 = 1.10997859555733471…` — a *muon* value in a field named
   `canonical_proton_q0` — and has **no `computedAt`, no `scriptFile`, no
   `scriptHash`, no `engine`**. Nothing in the provenance machinery can flag it as
   stale, because it records no provenance at all. It is one of only two audits in
   the tree whose witness is written by `out.write_text(json.dumps(...))` directly
   rather than through `WitnessBuilder`.

## Why it went unnoticed — and it is a taxonomy row

The audit was **correct when written**. Before 2026-05-28 the muon-anchored value
*was* the pin (`q_muon_at`'s own docstring: *"This was the pin until 2026-05-28;
now superseded by `q_at()` (m_p anchor)"*), and the 2026-08-15 owner ruling made
the proton pin canonical. The audit's polarity was never revisited.

The general shape, worth adding to
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`: **a detector that encodes
which value is canonical becomes an anti-detector the moment the ruling moves.**
It does not go quiet and it does not fail — it keeps reporting confidently, with
the sign flipped, and its report reads exactly like a real backlog. Every other
row in that taxonomy is a detector that *misses* something; this is one that
*asserts the opposite*.

## Not run, deliberately

`main()` writes the witness unconditionally (`:182`, no dry-run flag), so running
it would regenerate the inverted artefact and refresh its timestamp. The static
evidence above is decisive without it. Whoever fixes this should invert the
polarity **before** the next run, or the run will overwrite the current witness
with an equally wrong one that merely looks fresher.

## What it needs

1. Swap `A` and `C` throughout — canonical is the proton pin, stale is the
   pre-ruling muon value — and re-derive the `tr_M` leaf literals it screens for,
   which are quoted at the old canonical and are presumably inverted too.
2. Read the canonical value from `q_parameter` **at runtime** instead of quoting a
   literal in the docstring and the scan table. The whole defect is that the audit
   hardcodes the thing it exists to stop others hardcoding.
3. Emit through `WitnessBuilder` so the witness carries `computedAt`/`scriptHash`
   and the staleness gates can see it.
4. Do **not** enable `--strict` in CI until 1–3 land.

Related: `qou-cds3` (the 22 mislabelled witnesses, of which this is one),
`qou-khac` (the muon constant this audit calls canonical is itself stale by
8.54e-11).
