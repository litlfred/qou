---
# qou-iph3
title: 'habiro-frobenius probe: deprecated input, hidden failing test, half-integer full trace'
status: todo
type: task
priority: normal
created_at: 2026-08-22T22:55:17Z
updated_at: 2026-08-22T22:55:56Z
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
