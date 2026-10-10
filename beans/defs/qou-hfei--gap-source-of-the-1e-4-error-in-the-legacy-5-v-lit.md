---
# qou-hfei
title: 'GAP: source of the ~1e-4 error in the legacy 5₂ V literals'
status: scrapped
type: task
priority: normal
created_at: 2026-08-03T14:28:58Z
updated_at: 2026-08-14T21:01:52Z
---


## What is open

Where the ~1e-4 error in the two legacy 5₂ literals came from.

| | extraction convention | legacy literal | rel |
|---|---|---|---|
| σ₁ | 1.37919430966108 | 1.3790860299 | 7.85e-5 |
| σ₃ | −2.75838861932215 | −2.7580990292 | 1.05e-4 |

## Settled — do not re-litigate

**The convention is IDENTIFIED.** Both literals match the extraction convention
`V_eff = V_GGM + π²/2` to ~4 digits. This supersedes two earlier verdicts — the
2026-07-26 "matches neither published convention" and the 2026-08-01 "Im V₁
doesn't match" — **both of which tested only ONE literal**. Testing σ₃ as well
changed the answer. Do not reopen the "which convention" question.

> **Corrected 2026-08-14 (see the closing note below).** The earlier gloss
> "the formula was right; the evaluation was sloppy" is **withdrawn**: the
> 2026-08-14 narrowing probe shows *no* degradation of this formula reproduces
> the legacy pair. The literals agree with the convention to ~4 sig figs but
> are a **different computation**, not a sloppy evaluation of this one. The
> convention-identification above stands; only the "sloppy eval" mechanism was
> wrong.

**The pair is internally inconsistent** by 7.3e-5 against the exact relation
`V₃ = −2·Re V₁ − 3π²/2`, so the two were computed *independently*; neither was
derived from the other.

## Refuted as the source (scope-(a), direct test)

- **Li₂ series truncation** — converges σ₃ to the *true* extraction value and
  never to the legacy one (residual stalls at 2.9e-4 for N ≥ 9); and cannot
  produce σ₁ at all, since `|y₁| = 1.52 > 1` and the series diverges there.
- **Root imprecision** — the map is insensitive: a 3-decimal root already
  reproduces the extraction value to 1e-8. Inverting for the root that *would*
  give legacy σ₃ yields `0.4351928`, cubic residual `9.2e-3` — not a root of
  the cubic at all.

Scope-(a): these two are excluded by direct test; the space of error sources
is **not** exhausted.

## Status / priority

Bounded to a 4-digit evaluation slip in a correct formula, not a different
formula, object, or knot. **Low priority** — the values are no longer used
(`fivetwo_saddle_values.py` computes them; `V₃` follows from `V₁`), so this is
forensics, not a blocker. Close as `wontfix` if it stays cold.

## Refs

- probe: `computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`
- ledger: `docs/coordination/1ppq-qbeta.md`, 2026-08-02 row
- PRs #4454, #4624


---
**2026-08-14 — five more sources refuted; closing `wontfix` (scrapped).**

Probe `computations/probes/qbeta_5two_legacy_provenance_narrowing_probe.py`
(self-contained mpmath, EXIT 0) refutes five more error sources by direct test:
H1 truncated π (converges to the TRUE value, min |err| vs legacy 2.81e-4),
H2 rounded root (map insensitive, confirms bean), H3 perturbed cubic coeffs
(nearest legacy repro off by 8.3e-3), H4 additive shift (implied shifts are
`0.49999·π²` and `0.50003·π²` — independently off `π²/2`, not a common
constant), H5 low working precision (even dps=6 converges to TRUE, never legacy).

DECISIVE: **no degradation of the current formula reproduces the legacy pair.**
Every perturbation lands on / converges to the TRUE extraction value, ≥ ~6e-5
from legacy. So the legacy pair is not a sloppy eval of THIS formula — it is a
DIFFERENT computation agreeing to ~4 sig figs (consistent with the pair being
internally inconsistent by 7.3e-5 against `V₃ = −2·Re V₁ − 3π²/2`). This mildly
CORRECTS the bean's prior "formula right, evaluation sloppy" framing.

Cold forensics, no downstream consumer (values unused; V₃ follows from V₁ via
the proved sum rule). Seven refuted sources total; the remaining space
(the actual different-source computation) is unbounded and buys nothing.
Closing `wontfix` per this bean's own guidance. Audit:
`docs/audits/2026-08-14-hfei-5two-legacy-provenance-narrowing.md`.
