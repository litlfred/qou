---
# qou-iph3
title: 'habiro-frobenius probe: deprecated input, hidden failing test, half-integer full trace'
status: todo
type: task
priority: normal
created_at: 2026-08-22T22:55:17Z
updated_at: 2026-08-22T22:59:28Z
---

Split out of the `qou-lwyo` scoping pass (2026-08-22), which carries the full
measurement. Three independent defects in
`computations/probes/habiro_frobenius_probe.py` and its witness — none blocks
`qou-lwyo`'s Lean instance, all three affect what the block
`def:qou-motivic-galois-instance` can claim, whose `.ts` says
`computation.status: "verified"`.

**1. Input is a `_deprecated/` witness.** Resolves to
`computations/_deprecated/habiro-coefficients-atomic-fast.witness.json`. Live
per-atom witnesses exist for all five atoms, plus a live aggregate at
`computations/habiro/habiro-coefficients-atomic.witness.json`.

Not a mechanical repoint — the deprecated file is **deeper**: proton 10 vs 9,
deuteron 14 vs 13, tritium 19 vs 16, ³He 20 vs 16, neutron 9 vs 9. Fewer
coefficients ⇒ the Pochhammer mechanism (`2p ≤ n_coeffs`) covers fewer primes.
Which generation is canonical is an author call.

**2. The witness headline omits the test that fails.**
`summary.step2_all_atoms_compatible: true` is the numerator-only test. The same
script computes `step2_full_trace_passed` — **False at 45/45** (5 atoms × 9
primes) — and the top-level `summary` never surfaces it. Reading `summary` alone
gives the opposite impression to the per-prime data.

Fix: surface `step2_full_trace_compatible` in the top-level summary alongside the
numerator result, so the witness reports both tests it runs.

**3. The full-trace failure is a uniform factor of 2 — probe it before reading it
as a refutation.** Proton: `frob_full` missing at p=3 (`denominator vanishes mod
Phi_{2p}`); at the remaining eight primes the full Galois trace is a
**half-odd-integer** — −4/3, −1/4, then 1/2, −5/2, 3/2, −7/2, 5/2, −9/2 at
p = 7,11,13,17,19,23. So past the Pochhammer range, `2·Tr(full)` is an odd
integer, uniformly. That is the shape of a missing normalisation, not of a broken
claim, and it is the one lead in this area with a visible pattern.

Per the "(a)/(b) scope" discipline: `step2_full_trace_compatible: false` is a
**scope-(a)** negative — this normalisation of the full trace, as computed, is not
integral. It is **not** a structural exclusion of full-trace compatibility, and
nothing in the corpus should cite it as one.


## CORRECTION (same session, 2026-08-22) — "uniform factor of 2" is WRONG

Defect 3 above says the full-trace failure is *"a uniform factor of 2 — `2·Tr(full)`
is an odd integer, uniformly"*. **That is false.** I measured the **proton only**
and generalised to all five atoms without checking. Measured denominators of
`Tr(full)`, all 5 atoms × 9 primes:

| atom | p=2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|---|---|
| proton | 3 | — | 4 | 2 | 2 | 2 | 2 | 2 | 2 |
| neutron | 3 | — | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| deuteron | 30 | — | — | 16 | 32 | 32 | 16 | 8 | 32 |
| tritium | 90720 | — | — | — | 32 | 128 | 64 | 64 | 128 |
| ³He | 90720 | — | — | — | 64 | 16 | 128 | 64 | 128 |

Denominator 2 occurs for the **proton alone**, and only at p ≥ 7. The neutron is
uniformly 4; the composites run 8 → 128 and grow with A.

A second thing I assumed and did not check: I reasoned that
`Tr(num)/Tr(full)` recovers `denom`, having verified it at p=2 (−16 / (−4/3) = 12).
It does not — the Galois trace is not multiplicative, and `denom` is not
Galois-invariant, so that quotient is meaningless wherever the orbit is bigger.
It came out non-integral at most primes, which is the symptom of the assumption
being wrong rather than of anything in the data.

## What the corrected measurement actually shows — a better lead than the wrong one

**Away from p = 2, the obstruction is exactly 2-adic.** For every atom and every
p ∈ {5,7,11,13,17,19,23} the denominator of `Tr(full)` is a **power of 2**:
`Tr(full) ∈ ℤ[1/2]`, with `v₂` running 1..7 and increasing with A.

**Every non-2-power denominator in the whole 45-cell table sits at p = 2**:
3 (proton, neutron), 30 (deuteron), 90720 (tritium, ³He). p = 3 has no `frob_full`
at all (`denominator vanishes mod Phi_{2p}`).

So `step2_full_trace_passed` fails for a *structured* reason — non-integrality is
2-adic away from the prime 2, and only at p = 2 do odd primes enter the
denominator. That is a sharper and more suggestive shape than the one I wrote
first, and it is the actual lead. It remains a **scope-(a)** negative: this
normalisation of the full trace is not integral. Nothing here excludes full-trace
compatibility structurally.
