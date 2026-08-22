---
# qou-tol0
title: 'Nine assertions pass with a computed mass of zero or negative — tolerance >= |expected| makes them unfalsifiable'
status: todo
type: task
priority: normal
created_at: 2026-08-22T03:30:00Z
updated_at: 2026-08-22T03:30:00Z
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
