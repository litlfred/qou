# The h4 Form A/B frozen record, and why a docstring was not enough

**Bean:** `qou-tean` · **Date:** 2026-08-24

`computations/h4-form-AB-cross-anchor-stability.witness.json` is a
deliberately frozen probe result. Until today its only protection was a
sentence in a header comment:

> This probe is **preserved as-is by design**.

Nothing enforced that. Any agent running the producer — a sweep, an audit, a
`--candidates` pass — silently overwrote the frozen numbers, and `git add -A`
committed the result. That very nearly happened during the `qou-bdkx` triage,
and in the same session it *did* happen to a different witness (reverted in
`a93d01c250`).

This document is the third of three mechanisms now standing between the frozen
record and the next tool that walks the tree, and it is the one that cannot be
defeated by a tool at all: **the numbers are written down here, in prose.**

## The frozen values, and what a re-run replaces them with

| field | committed (frozen) | fresh run |
|---|---|---|
| `Form_A_ppb_proton` | 4753.80226522 | **207.114326709** |
| `Form_B_ppb_proton` | 4753.80454962 | **207.116611119** |
| `Form_A_ppb_muon` | 4752.63138326 | 4992.62545608 |
| `data.q_muon` | 1.109978595554180575281594 | 1.109978595642739046681795 |

`evaluate_form` confirms `Form_A_ppb_proton` is what the docstring means — the
ppb residual of Form A at `q_proton` — so this is like-for-like, not a
relabelling.

## Neither number matches the producer's own claim

The docstring states:

> Form A: f = 1 + (1 − π²/80)·h⁴ → **0.003 ppb** at q_proton
> Form B: f = 1 + (7/8)·h⁴ + (G/(8π))·h⁶ → **0.0008 ppb** at q_proton

4753 and 207 are both roughly five orders of magnitude away from those.

**This is not a claim that the docstring was ever wrong.** The residual depends
on `alpha_em`, `m_e`, `m_mu` and `m_p` from the CODATA registry, and those have
moved. The likeliest reading is that 0.003 ppb was true at the inputs of its
day and every input has since drifted.

What *is* certain, and what nothing in the file said before this document:
**the documented sub-ppb closure is not reproducible today.** Anyone citing
this probe for the Form A/B discrimination needs to know that.

## The three mechanisms

1. **This document.** Prose in `docs/audits/`, which no regeneration harness
   writes to. Even if every other guard is removed, the numbers survive here.
2. **`"preserved": true` in the witness, enforced in `WitnessBuilder.save()`.**
   The guard lives at the single point every producer's output passes through,
   not per-producer, so it protects any witness that opts in — not just this
   one. A blocked run **raises**; it does not silently succeed, because a
   producer that thinks it wrote and did not is the same class of lie in the
   other direction. Escape hatch: `QOU_ALLOW_OVERWRITE_PRESERVED=1`, and an
   overwrite must re-declare the freeze or the next run loses it.
3. **`--force` on the producer.** The local, discoverable half — so the escape
   hatch is visible from the script you are actually running rather than only
   from an env var you would have to already know exists.

## Still open: the header is inverted

The producer's header reads:

```
canonical proton q0 is q_at() ≈ 1.1099785955573347…
```

Measured today, `q_at()` = `1.10997858275138…` and `q_muon_at()` =
`1.10997859564274…`. **The value the header attributes to the proton accessor
is the frozen muon literal.** Same inversion class as `qou-q0inv`, in a
file-level comment rather than an audit.

This is left unfixed here — it was offered as a separate item and not taken up,
so it stays recorded rather than silently changed. It is one line, and it is
actively misleading about which accessor returns what.
