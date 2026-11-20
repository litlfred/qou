---
# qou-tol0
title: Nine assertions pass with a computed mass of zero or negative — tolerance >= |expected| makes them unfalsifiable
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T03:30:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

`computations/atom-mass-derived.witness.json` reports `allPassed: true` over
ten assertions. Nine of them pass with a computed value of **zero or
negative** against expected atomic masses of thousands of MeV:

| assertion | computed | expected | tolerance |
|---|---:|---:|---:|
| `M(Helium)` | **−215.0** | 3728.4 | 7886.88 |
| `M(Lithium)` | **−75.6** | 6535.4 | 13221.97 |
| `M(Beryllium)` | **−2.3** | 8394.8 | 16794.22 |
| `M(Boron)` | **−0.1** | 10255.1 | 20510.34 |
| `M(Carbon)` | **0.0** | 11177.9 | 22355.84 |
| `M(Nitrogen)` | **0.0** | 13043.8 | 26087.56 |
| `M(Oxygen)` | **0.0** | 14899.2 | 29798.34 |
| `M(Fluorine)` | **−0.0** | 17696.9 | 35393.80 |
| `M(Neon)` | **0.0** | 18622.8 | 37245.67 |

In every row the tolerance is **twice the expected value**, so the pass
interval is `[−expected, 3·expected]` — it contains zero, and a negative
mass passes. The tenth row, `M(Hydrogen)`, computes 1451.6 against 938.8 and
passes on the same construction.

The producer, [`computations/atom_mass_derived.py`](../computations/atom_mass_derived.py),
is live — not under `_deprecated/`.

## Root cause: the tolerance is a function of the error it bounds

[`atom_mass_derived.py:470`](../computations/atom_mass_derived.py):

```python
tolerance=max(abs(r.delta_MeV) * 2, 50),
```

`delta_MeV` **is** the residual. So the check is
`|computed − expected| = |delta| ≤ max(2|delta|, 50)`, which holds for
every `delta`, every element, unconditionally. This is not a loose bound —
it is a tautology generator, and no value of the mass computation can ever
fail it. The effect I first measured (tolerance ≈ twice expected) is a
consequence: when the computed mass is ~0, the residual is ~the expected
value.

**One sibling shares the shape.**
[`probes/binding_energy_scale_probe.py:122–127`](../computations/probes/binding_energy_scale_probe.py)
asserts `E0_improves_deuteron` with `computed=|err_e0|`, `expected=0`,
`tolerance=|err_qb|` — i.e. "the E₀ error is no worse than the Q_β error".
That one is *defensible* as a comparison written into the assertion fields,
unlike the case above; noted so a sweep does not treat the two alike.

The other two live matches of the pattern are legitimate relative
tolerances and should not be touched: `tau-lepton-nf.py:195`
(`abs(a[n]+b[n]) * 1e-8`) and `:206` (`abs(pdg_br_ratio) * 0.25`, with the
25 % explained in a comment).

## Why this survived every other check

Nothing here is a wrong number. Each assertion is a *true* statement:
`|computed − expected| ≤ tolerance` genuinely holds. It is the claim that is
empty. A numeric audit that recomputes values finds nothing, a staleness
audit finds nothing, and `allPassed: true` reads as verification — which is
how nine mass predictions of zero came to be recorded as passing.

Distinct from the two neighbouring beans, both of which stay open on their
own terms:

- the **~383 witnesses with `allPassed: true` and zero assertions** — that is
  an *absent* claim; this is a *vacuous* one, and it looks stronger because
  the assertions are there and detailed.
- **111 witnesses carrying a recorded assertion failure that nothing reads**
  — those are honest failures nobody consumes; these are dishonest passes.

## Detector

[`computations/witness_assertion_slack_audit.py`](../computations/witness_assertion_slack_audit.py),
added with this bean. It reports three tiers and exits 1 only on the first:

1. **blocking** — passed with `computed ≤ 0` against a positive `expected`
   and `tolerance ≥ |expected|`. 9 corpus-wide, all in this witness.
2. **review** — `tolerance ≥ |expected|` with a positive computed value: 14
   more. Several are benign, and the script says so: an inequality or an
   existence check written into the equality fields lands here
   (`lp_active_set_nonempty`, computed 1.0, expected 1.0, tolerance 10.0, is
   exactly that and is fine).
3. **advisory** — a passing assertion missing by ≥ 1 %. Contaminated by the
   same false-positive class, so it is advisory rather than blocking; the
   real instance behind it is `g_A` computed 1.0 against 1.2754 under
   `tolerance: 0.5`, a 21.6 % miss reported as a pass
   (`borromean-axial-coupling.witness.json`).

Values are parsed with `parse_float=Decimal`, so each literal is preserved
exactly and every comparison is an exact rational — no float64, per the
probe-precision rule.

## What would close this

Fix the producer, not the baseline. Either the mass computation returns zero
for `Z ≥ 2` and should be reported as failing, or the assertion is checking
the wrong quantity. Do **not** narrow the tolerance to make the current
numbers pass; and note that these are **absolute atomic masses in MeV**,
which the 2026-08-11 excision removes as framework predictions regardless —
so "delete the assertions" may be the right answer rather than "fix them".

No content block cites this witness (only `docs/audits/`), so nothing
published rests on it. That bounds the damage; it does not make the pass
honest.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8391, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
