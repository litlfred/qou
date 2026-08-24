---
# qou-cds3
title: 'S3 (SCIENCE): muon -> proton witness migration — 870 not ~840, and 69 straddle both pins'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-24T05:10:00Z
---

Parent: `qou-cdx1`. Related: `qou-1c4y` (the tracked migration), `tnjb`
(completed, a *dashboard* defect — do not confuse the two).

## Measured 2026-08-15 (fixed-string, `computations/**/*.witness.json`)

| | count |
|---|---|
| total witnesses | **2941** |
| muon fingerprint `1.109978595` | **870** |
| proton fingerprint `1.1099785827` | **588** |
| **both** | **69** |
| muon-only | **801** |
| proton-only | 519 |

**AGENTS.md's "~840" is low, not stale-high.** The measured figure is 870
(801 muon-only). AGENTS.md was right to flag the number as needing
re-measurement; the error runs the opposite way from what "stale" suggests.

## Do the 69 both-pin witnesses FIRST — they are a defect either way

A witness quoting both pins is either a deliberate comparison or a **layer
straddle**, which AGENTS.md names STRICT: *"Never straddle the two layers inside
one quantity."* The worked precedent is the μ₃ Fréchet probe, which took `y_λ`
from the muon-built cache while evaluating `χ_λ` at the proton `q₀` — an
11.54 ppb separation, ~1e-7 on the result. Triaging these 69 is worth doing
**regardless** of whether the bulk migration is authorised.

## The specific trap to check at every call site

`wedderburn_jones_markov.y_lambda_at(n, q)` returns the cached **muon-built**
`y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| < 1e-12` — a gate
satisfied **trivially** when the caller passes `q_parameter.Q` itself. The
ideal-layer cache reaches an experimental-layer caller with **no signal**. For
experimental-anchor compute call
`schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)` instead.

## Scope question for the owner

**R2's wording does not obviously authorise the bulk rewrite.** The 2026-08-07
directive explicitly did *not*, and R2 states the end state rather than the
sweep. Recommendation in the ruling audit: treat the bulk migration as still
needing its own scoped sign-off; do the 69-witness straddle triage now.

Standing posture until then: new/touched code uses proton; untouched muon
witnesses stay as recorded; never mix within one quantity; every new witness
records its q₀.

---

## 2026-08-23 — `qbeta_singularity_cross_anchor_probe` unblocked and committed (11 of 21), and the real defect was not the one I fixed first

Two corrections to my own account, then the fix.

### 1. It is no longer blocked, because main moved

I recorded this probe as blocked by an upstream all-null `c_k_extracted_50dps`.
A merge from main brought `6e586861b` — *"only c_2 and c_3 are supported; my own
guard was off by one"* — so the witness now reads

```
c_2: -1.017217328566724951324066253      c_3: -2.021615577060006120530024970
c_4..c_10: null        last_resolved_rung: 3   n_unresolved: 7
```

With two rungs resolved the probe no longer crashes at all.

### 2. My first guard was the wrong guard

I added `raise SystemExit` when the resolved set is **empty**. That fires on the
old state and not the current one — and the current one is worse. The probe ran
to completion, printed `VERDICT: FIBRE_LEVEL_CONFIRMED`, and wrote
`allPassed: true` **over a c_k table with zero rows**.

Why: section (a) consumes `k >= 6` only (`if k < 6: continue`), and 6..10 are
exactly the nulled rungs. So the resolved set is non-empty (c_2, c_3) while the
consumed range is entirely absent. A guard keyed to "is anything resolved" cannot
see that. The verdict itself comes from section (b), the `u_subst` location test,
which uses **no `c_k` at all** — which is why the probe looks healthy.

### The fix — keyed to the range actually consumed

`load_ck_from_witness` now returns `(resolved, nulled)` and skips sentinels;
`main()` reports the coverage of the range it consumes and refuses to let an
empty (a) read as a passed (a):

```
  rungs k>=6 available: NONE   nulled upstream: [6, 7, 8, 9, 10]
  *** SECTION (a) EVALUATED NOTHING. … The VERDICT printed later comes from
      section (b) alone, which uses no c_k at all -- do not read it as
      confirming (a).
```

and the witness carries it, so the artefact cannot be misread either:

```json
"ck_section_a_coverage": {"min_k_consumed": 6, "rungs_available": [],
  "rungs_nulled_upstream": [6,7,8,9,10], "section_a_evaluated": false}
```

`allPassed: true` is still true of what ran; it is now impossible to read as
covering what did not.

### Committed as a cds3 item

Mislabelled proton-named field **1 → 0** (`data.q_proton` is now
`1.10997858275138…`), failed assertions 0 → 0, verdict byte-identical,
environment **upgraded** (`scipy None → 1.17.1`, `mpmath 1.3.0 → 1.4.1`) not
downgraded. Consistent with the agent finding that this producer imports
`q_at` from `qou_substrate.constants` and therefore resolves proton regardless of
its `ideal_muon` listing — i.e. genuinely stale, and regeneration is the right
fix for it.

**Running total: 11 of 21 committed.**
