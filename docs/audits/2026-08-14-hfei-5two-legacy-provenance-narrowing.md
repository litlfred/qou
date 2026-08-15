# qou-hfei — the ~1e-4 error in the legacy 5₂ V literals: five more sources refuted; it is not a degraded eval of the current formula

**Date:** 2026-08-14
**Bean:** `qou-hfei`
**Probe:** [`computations/probes/qbeta_5two_legacy_provenance_narrowing_probe.py`](../../computations/probes/qbeta_5two_legacy_provenance_narrowing_probe.py) (self-contained, EXIT 0)
**Predecessor:** [`computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`](../../computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py) + bean history

## Question

Where did the ~1e-4 error in the two long-unexplained corpus literals come from?

| | extraction (true) | legacy | Δ |
|---|---|---|---|
| σ₁ (Im V₁ slot) | 1.37919430966108 | 1.3790860299 | −1.08e-4 |
| σ₃ (V₃) | −2.75838861932215 | −2.7580990292 | +2.90e-4 |

Extraction convention: `σ = Re(3·Li₂(y) + (log y + b·πi)²) + π²/2`, `y` a root of `y³−2y²+3y−1`, with `σ₁ = ext(y₁, b=−1)`, `σ₃ = ext(y₃, b=+1)`. Prior work refuted two sources (Li₂-series truncation; root imprecision).

## Five more sources refuted (scope-(a), direct test)

| # | hypothesis | result |
|---|---|---|
| H1 | truncated π (3–10 digits) | converges to the **true** value; min |err| vs legacy 2.81e-4 |
| H2 | root rounded to 3–8 dp | map insensitive; no effect (confirms bean) — 2.89e-4 |
| H3 | perturbed/typo'd cubic coefficients (±1 sweep) | nearest legacy repro off by **8.3e-3** |
| H4 | clean rational-π² additive shift | implied shifts are `0.49999·π²` (σ₁) and `0.50003·π²` (σ₃) — **independently** off `π²/2`, not a common constant |
| H5 | low mpmath working precision | even **dps=6** converges to the **true** value, never legacy |

## Decisive finding

**No degradation of the current formula — π precision, root rounding, cubic coefficients, additive shift, or working precision — reproduces the legacy pair.** Every perturbation lands on (or converges to) the *true* extraction value, staying ≥ ~6e-5 from the legacy numbers.

This **sharpens and mildly corrects** the bean's prior "the formula was right; the evaluation was sloppy" framing. A sloppy evaluation of *this* formula does not produce the legacy values. The legacy pair is consistent only with a **different computation** (a different normalization/source that happens to agree to ~4 significant figures), not a degraded evaluation of the current one. That the two legacy values are *internally inconsistent* by 7.3e-5 against the exact relation `V₃ = −2·Re(V₁) − 3π²/2` (they were computed independently) fits this reading.

## Verdict — `wontfix`

The source of the legacy values remains **unidentified**, and the search is now well-bounded (seven refuted sources total). But this is cold forensics with **no downstream consumer**: the values are unused in production, and `V₃` follows from `V₁` via the proved sum rule. Per the bean's own guidance ("close as `wontfix` if it stays cold"), this axis should be closed `wontfix` rather than worked further — the remaining space (locating the actual different-source computation) is unbounded and buys nothing.

## Discipline

Exploratory forensics. No fit, no production wiring, no witness overwrite (the predecessor probe's witness drift was reverted). The narrowing probe is self-contained (mpmath only) and asserts its refutations.
