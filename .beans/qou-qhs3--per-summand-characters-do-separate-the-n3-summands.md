---
# qou-qhs3
title: Per-summand characters DO separate the n=3 summands — chi^lambda exists for general n
status: completed
type: task
priority: normal
created_at: 2026-09-04T02:33:10Z
updated_at: 2026-09-04T02:43:57Z
---

## The framing this bean corrects is my own, and the corpus-grep caught it

Closing #6547 I said the per-summand character values for general `n` were
"the upstream gap" and "the real open item", and deliberately did NOT open a
bean for it on the grounds that it was a known upstream absence.

**That was wrong, and the six-path checklist is what found it.** The
general-`n`, general-`λ` character machinery is live in the corpus:

- `tools/hecke-engine/src/seminormal.rs` — `chi_lambda_braid(shape, word, q)`
  and `chi_lambdas_braid`, Hoefsmit seminormal form, general `n`, general `λ`.
- `tools/hecke-engine/src/seminormal_mpfr.rs` — the MPFR variants.
- `tools/hecke-engine/src/geck_pfeiffer.rs` — the `T_β = Σ c_w(q) T_w`
  canonical-basis expansion.
- `tools/hecke-engine/src/bin/hecke_canonical_chi.rs` — a CLI computing
  `χ^λ(β)` for every `λ ⊢ n`.
- **All of it reachable from Python right now**: `pyhecke_native 0.9.0` is
  installed and exports `chi_lambdas_braid_mpfr` among ~20 chi entry points.

So "not in this file" (true, about the Lean) got reported as "upstream and
open" (false, about the corpus). Same error class as PRs #1515 / #1532 /
#1543 in AGENTS.md, committed by the agent who had just spent two PRs on
statements that claimed more than they encoded.

## What the compute then answered, immediately

#6547 proved `jones_channels_not_separating`: the two *named Jones values* of
`descartes_n3_both_detected` coincide at `q* ≈ 0.7795446638`, a `q` the
Descartes condition permits, so that pair cannot distinguish the two `n = 3`
summands.

The obvious follow-up question — do the **characters** separate where that
pair fails? — needed no new machinery. Measured with
`chi_lambdas_braid_mpfr` at 50 dps, shapes `[3]` and `[2,1]` (the `≤ 2`-row
partitions of 3):

| word | `χ^[3]` | `χ^[2,1]` | separates |
|---|---|---|---|
| identity | 1 | 2 | yes (dims) |
| `σ₁` | 0.77954466382093496888 | −0.50325547119442657056 | yes |
| `σ₁³` (trefoil) | 0.47372140546618934285 | −1.6372239486199317447 | yes |
| `σ₁σ₂` | 0.60768988289169451699 | −1 | yes |
| `σ₁σ₂⁻¹` | 1 | −1.2532660692871243117 | yes |

all at `q = q*`, the exact point where the Jones pair fails.

**And the closed forms are trivial**, verified against the native path at 8
sample q to < 1e-45:

    χ^[3](σ₁)   = q
    χ^[2,1](σ₁) = q − q⁻¹
    difference  = q⁻¹        — never zero

So **the single generator `σ₁` separates the two `n = 3` summands at every
`q ∉ {0, 1}`**, which includes every Descartes `q`.

`jones_channels_not_separating` is therefore a fact about the *particular
pair of Jones values that theorem named*, not about the framework's ability
to separate summands. That is a much narrower negative than it reads as, and
it now has its positive counterpart.

## Recorded while measuring

`chi_lambdas_braid_mpfr` returns `['NaN', 'NaN']` at exactly `q = 1` — the
seminormal form has a pole there. Harmless for this arc (Descartes requires
`q ≠ 1`) but it is a silent NaN, not a raised error, so a caller that does
not exclude `q = 1` gets NaN propagated into a witness.

## Scope

- Probe under `computations/` with a witness, mpmath end-to-end.
- Lean: the two characters and the `σ₁` separation, in the Descartes file
  beside `jones_channels_not_separating`, so the negative and its resolution
  sit together.
- NOT in scope: wiring `trSummand` to the actual Hoefsmit values in Lean.
  That needs the seminormal construction formalised and is a real piece of
  work, not a rename.
