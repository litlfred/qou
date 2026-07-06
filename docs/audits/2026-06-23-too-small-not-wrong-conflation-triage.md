# "Too small / not-dominant / unwired" ≠ "WRONG" — a conflation triage

**Date:** 2026-06-23
**Branch:** `claude/nice-dirac-ywun65`
**Status:** epistemology audit (owner-prompted); no content/compute change; durable record.

## The owner's point

> "[q-Bessel quadratic-action] 20–80× too small → does that mean it's wrong? if
> Lean-proved and part of categorical action why not wired up? even if not
> closing the large gap, does not mean wrong. are there other situations like
> this?"

Correct. Three verdicts that the audit prose frequently blurs must be kept apart:

| Verdict | Meaning | Charity applies? |
|---|---|---|
| **WRONG** | the identity/mechanism is mathematically false (sign error, failed cross-check, hidden fit) | No — legitimately dead |
| **SUBDOMINANT-but-REAL** | the math holds (often Lean-proved), the magnitude just isn't the dominant term | **Yes — not wrong** |
| **UNWIRED-but-REAL** | proved + part of the categorical action, but no compute consumes it | **Yes — not wrong** |

**Discriminator** (from the triage below): *refuted by a forced / out-of-sample
check, or a disguised fit* ⇒ really WRONG. *"Refuted" = too small under forced
weights / not the dominant term / no consumer script* ⇒ real-but-subdominant-or-
unwired.

## The worked case — q-Bessel quadratic-action binding correction

Squarely **SUBDOMINANT-but-REAL**, and the corpus already self-corrected toward
the owner's reading: [`2026-06-20-qbessel-reeb-flow-radial-argument.md`](2026-06-20-qbessel-reeb-flow-radial-argument.md)
records it **forced** (parameter-free), **surviving** (`δ ≠ 0`, doesn't cancel),
**scale-open** (~25× small *at a crude classical first pass* — uniform weights,
classical `q→1` Bessel — NOT the forced `y_λ χ_λ`-weighted q-deformed version).
PR #2538 declared the direction "CLOSED"; that audit calls it **"premature"** and
reopened it. The Lean machinery (`QCasoratianAbel`, `QBesselContiguityRecurrence`,
`QLommelOrderRecurrence`) is sorry-free: *"the machinery stands; the physics claim
does not"* ([`2026-06-20-binding-gate-stocktake-post-qbk2.md`](2026-06-20-binding-gate-stocktake-post-qbk2.md)).
The **skeleton** (the contiguity recurrences) is now wired —
[`computations/qbeta/qbessel_jackson_contiguity.py`](../../computations/qbeta/qbessel_jackson_contiguity.py),
the pure UNWIRED-but-REAL case (sorry-free, costs nothing in discipline, just
hadn't been plumbed). The *binding application* stays exploratory until forced AND
on-scale (wiring a tuned-prefactor correction would be a CAL-4 fit).

## Triage of other cases (judged on the math, not the label)

| # | Object | Lean-proved? | Verdict-language | TRUE bucket |
|---|--------|--------------|------------------|-------------|
| 1 | **Δ_λ = sgn(w₀^{S_λ'})·dim** | YES (sign rule sorry-free) | "proved **but wrong magnitude**"; functional "refuted" | **SUBDOMINANT/sign-REAL** — sign proved/closed; only one *magnitude reading* refuted (see the a-function re-scoping, 2026-06-23) |
| 2 | **q-Bessel quadratic-action (qbk2)** | YES (machinery) | "REFUTED"; "20–80× too small" | **SUBDOMINANT-REAL** — owner's example |
| 3 | **silver-ratio / Q_A pole** (`SilverAnchorGrounding.lean`, `b²=7/8` derived) | YES | "pattern BREAKS at c_8"; pole "GENUINE but SUBDOMINANT" | **SUBDOMINANT-REAL** (corpus relabels it itself); `qbeta-c8-c10-silver-rationals.ts` has **no `computation`** ⇒ also UNWIRED |
| 4 | **Δtr_M bar-decomposition** (`BarSymmetricBarAntiSymmetricIdentities.lean`) | YES | "structural observation … nothing wired" | **UNWIRED-REAL** — load-bearing constraint, never plumbed |
| 5 | **W/Z Weinberg angle = cosh(5η₀)/cosh(7η₀)** | YES (conditional, §3b-cond) | block kind `conjecture`; "Open" | **UNWIRED-REAL** — proved conditional; +1.1% is the open part |
| 6 | **content/twist eigenbasis L1–L3** (`θ_λ=q^{2c}` proved) | partial | "exact-symbolic … Nothing wired" | **UNWIRED-REAL** — worth the Lean follow-up |
| 7 | **proton-mass near-identity** (0.24 ppm, 0 free params; 3 ingredients proved) | partial | "near-identity … needs categorical proof"; "12 = empirical near-match" | **UNWIRED-REAL** — not refuted; the integers await derivation |
| 8 | **α_EM Habiro `[2]_q·(1−h²α)`** (PR #1511, Taylor-exact) | YES | "NEAR-MATCH 4.18 ppm" | **UNWIRED/partly-wired-REAL** — element derived; residual ppm open |
| — | **c_3 as a UNIVERSAL real-q fibre element** | no (c_2=−1 is) | "FALSIFIED" | **WRONG** — `dc₃/dq ≈ 4.6×10⁶` impossible for smooth real `f` (forced cross-anchor) |
| — | **Φ_q (Faddeev) as the archimedean face** | — | "REFUTED-DIAGNOSTIC" | **WRONG** as production face — real-q saddle is `li2q` (in production) |
| — | **q-factorial per-knot ratio** (PR #1383) | — | "RETRACTED … backhanded fitting" | **WRONG** — disguised multi-parameter fit (implied 12.7 vs actual 0.67) |
| — | **ν_SDP per-block-PSD reading** | — | "sharpened-negative" | **WRONG** — fails out-of-sample anchor (T at H₅: 1≠2) |

## Synthesis

- **At least 8 items carry refutation-flavored language over a Lean-proved-and-real
  core** (rows 1–8). The cleanest "owner is right to flag" cases: **#1 (Δ_λ sign),
  #2 (qbk2), #3 (silver pole)** — subdominant-but-real; **#4 (Δtr_M bar-decomp)** —
  unwired-but-real.
- **The genuinely-dead set is fairly discriminable:** each fails a **forced /
  out-of-sample test** or hides a **fit** (c_3-universal, Φ_q-as-face, q-factorial,
  ν_SDP). Charity does **not** rescue these — be fair both ways.
- **Root cause:** the corpus has a clean 3-tier rubric (`PROVED / NEAR-MATCH /
  REFUTED`, `ck-dk-canonical-registry.md` §1: "machinery-proved ≠ values-derived"),
  but saga prose collapses NEAR-MATCH and the subdominant sub-case into
  REFUTED-flavored language. Where the rubric is applied (silver pole, c_3
  registry) the bucketing is clean; where it isn't (binding-magnitude prose) the
  conflation creeps in.
- **Cheap remediation:** the UNWIRED-but-REAL sorry-free skeletons (silver pole
  c_8–c_10, Δtr_M bar-decomp, content-twist L1/L3) can be wired as honest small
  corrections / verifications at no discipline cost — exactly as the Jackson
  contiguity was here — without touching the (legitimately gated) binding-scale
  applications.
