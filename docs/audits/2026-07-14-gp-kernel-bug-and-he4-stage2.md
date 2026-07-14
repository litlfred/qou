# Rust GP character kernel returns wrong χ on some plain braid words — found by the A=4 stage-2 leg cross-check; stage 2 rebuilt on the seminormal engine

**Date:** 2026-07-14 · **Branch:** `claude/he4-binding-k-convention-correction-2026-07-13`
(rides PR #3783 per the "related bugs ride on the active PR" rule) · **Bean:** `qou-b2ie` ·
**Probe:** [`he4_binding_k_stage2_probe.py`](../../computations/deltalambda/he4_binding_k_stage2_probe.py)
(+witness) · **Scope:** (a); audit-only; nothing wired.

## The bug (measured, minimal reproducer)

`pyhecke_native.chi_lambdas_via_gp` (the Rust Geck–Pfeiffer exact-Laurent
character path) returns **wrong characters on some plain ±1 braid words**.
Minimal reproducer (delta-debugged from a 91-letter failure):

```
word = [(1,6), (1,7), (-1,9), (1,8), (-1,7)]     # σ₆ σ₇ σ₉⁻¹ σ₈ σ₇⁻¹ at H₁₂
```

On the trivial rep `[12]` every generator acts as `q`, so
χ_[12] = q^{writhe} = **q exactly**. Measured (at the canonical-muon q):

| engine | χ_[12](word) | verdict |
|---|---|---|
| GP exact-Laurent (`chi_lambdas_via_gp`), eval at v=√q | 0.79263478… | **WRONG** (should be 1.10997859…) |
| seminormal mpfr (`chi_lambda_all_partitions_mpfr`) | 1.10997859555733471989… = q | correct to 50 dps |

Higher reps disagree too (e.g. `[11,1]`: GP 5.7575 vs seminormal 7.7213).
The two engines are independent code paths; the trivial-rep value is forced
by writhe alone, so the GP side is unambiguously the broken one.

## How it was caught

The A=4 stage-2 probe evaluates K(⁴He) = T·cp⁻¹ per Wedderburn block through
two independent legs and **cross-checks every block trace**. The first run's
exact(GP)-vs-f64(seminormal) cross-check failed at 2.1e0 worst-case —
*including the d=1 blocks*, where no float accumulation is possible. Hand
computation of the 1-dim block matched the f64 leg, indicting GP; prefix
bisection + greedy delta-debugging on the 91-letter word produced the
5-letter reproducer above.

## Blast radius (checkcorpus)

- **NOT affected:** the certified combiner chain (`chi_at_q0_via_hoefsmit_mpfr`
  → `canonical_tr_m_via_chi_cache`) — seminormal path throughout; the
  presentation-correction probe's certifications (#3783) — every word it
  validated matched the seminormal chain end-to-end (proton/neutron 2.9e-49,
  D/⁴He 1.1e-20), so those specific ≤47-letter words do not trigger the bug.
- **VOID (already voided for the presentation error anyway):** stage-1/1.5
  GP evaluations (#3770/#3775).
- **NEEDS REVALIDATION (word-class not yet certified against seminormal):**
  GP-based chi consumers on longer/structured words — notably
  `derived_chi_catalogue_sweep.py` cells (plain sign-of-c words) and
  `li6_h18_amplification_discriminator_probe.py` (H₁₈). Any GP-derived
  witness should be revalidated per word against the seminormal engine
  until the Rust fix lands. Tracked in bean `qou-b2ie`.
- **Rule of thumb until fixed:** a GP result is trustworthy only with a
  per-word cross-check (trivial-rep writhe check is free: χ_[n] must equal
  q^{writhe} with sign-0 letters contributing [2]_q…; the stage-2 probe
  embeds exactly this pattern).

## Stage 2 (rebuilt on the seminormal engine)

Leg A now computes χ_λ(K) for all 77 blocks via `chi_lambda_all_partitions_mpfr`
(50 dps): sign-encoded word with the certified operator dictionary — σ→+1,
σ⁻¹→−1, averaged (σ−h/2)→0, averaged-inverse = (4/[2]_q²)·(σ−h/2)→0 with a
scalar prefactor per crossing, color-weighted seam = two weighted ±1 branches
(weights ½±δ/4). Leg B (f64 spectra, the A≤3 solver's precision class)
unchanged; every block trace is cross-checked between the legs.

Results: see `he4-binding-k-stage2.witness.json` (leg A dominant channel,
LP duals per the AGENTS.md LP/SDP rule, per-block PSD verdicts, α_gap).
The first (GP-legged) run's channel ranking — dominant λ*(K) = (9,3) — must
be treated as unverified until the seminormal rerun confirms or replaces it.

## Discipline note

The cross-check that caught this was the probe's own leg-agreement assertion
— the witness honestly reported `allPassed: false` rather than shipping the
broken numbers. This is the compute-author cross-check discipline working as
intended: two independent engines per result, assert agreement, refuse to
publish on disagreement.
