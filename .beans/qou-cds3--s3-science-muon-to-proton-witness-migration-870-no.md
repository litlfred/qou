---
# qou-cds3
title: 'S3 (SCIENCE): muon -> proton witness migration — 870 not ~840, and 69 straddle both pins'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-21T17:05:15Z
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

## RE-MEASURED + TRAP RE-CHECKED 2026-08-21

### The named trap is CLOSED — on both of its premises

This bean's *"specific trap to check at every call site"* says
`wedderburn_jones_markov.y_lambda_at(n, q)` serves the cached **muon-built**
`y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| < 1e-12`, a gate
satisfied trivially when the caller passes `q_parameter.Q` itself, so *"the
ideal-layer cache reaches an experimental-layer caller with no signal."*

Both halves are now false, and the fix was the convention-D excision, not a pin
migration:

**1. The cache is unreachable.** Since 2026-08-09 the function computes directly:

```python
if q_val is not None:
    _y = _y_su_n(n, _mp.mpf(str(q_val)), 2)      # hook-content, at the q PASSED
    return {sh: sp.Float(...) for sh, v in _y.items()}
```

Its own docstring: *"THE THREE C FAST PATHS BELOW ARE NOW DEAD … the D result
returns before any of them is reached. In particular `y-lambda-at-q0.witness.json`
holds C weights and **must NOT be served** — that cache is why the switch has to
happen here rather than only at `markov_z`."*

**2. `q_parameter.Q` is the PROTON pin.** Measured: `Q_MP =
1.10997858275138080759166909561076…` — identical to `Q_50_DIGIT_STR`, the
canonical proton anchor. A caller passing `q_parameter.Q` therefore gets proton,
not muon.

Verified by running it, not by reading it:

```
y_lambda_at(3, Q_MP)  ->  (3,)=0.5054042265…  (2,1)=0.2472978867…  (1,1,1)=0.0
docstring D values    ->   0.5054042           0.2472979            0
convention C would be ->   0.4153958           0.2809296            0.0227449
```

So the ~12 live call sites that pass `q0` — including the production one,
`binding_canonical.py:422` (`from q_parameter import Q_MP as q0`, line 65) — are
**safe from this mechanism**. They recompute at the q they pass. Whether each
passes the *right* q is a separate and *visible* question; the silent-straddle
channel this bean names is gone.

### Counts have moved a lot, and one moved the wrong way

Re-measured with the same fixed-string method over `computations/**/*.witness.json`
(excluding `_deprecated/`):

| | bean, 2026-08-15 | now, 2026-08-21 | Δ |
|---|---|---|---|
| total witnesses | 2941 | **2690** | −251 |
| muon fingerprint | 870 | **617** | −253 |
| proton fingerprint | 588 | **653** | +65 |
| muon-only | 801 | **539** | −262 |
| proton-only | 519 | **575** | +56 |
| **both pins** | **69** | **78** | **+9** |

Migration is clearly progressing — muon-only down 262 — but **the straddle class
grew**, which is the one this bean says to triage first *regardless* of whether
the bulk migration is authorised. Of the 78, **19 were touched since 2026-08-15**
and 59 predate it, so the growth is not purely inherited: partial migration
appears to be creating both-pin artefacts.

### First-cut triage of the 78 — and its limits, stated

Classifying by whether the witness's `computation` name or `description` signals
a deliberate pin comparison (drift / tension / compare / cross-anchor / …):

- **41 deliberate** — e.g. `q0-value-drift-audit`,
  `mu-substrate-tension-audit-100dps`. These *must* carry both pins; flagging them
  would be the false positive.
- **37 candidate straddles** — no such signal.

**This is a first cut, not a verdict, and it has visible false negatives**:
`mu-p-pin-sensitivity-map`, `q0-consistency-audit` (×2) and
`qbeta-meridian-holonomy-anchor-swing` are plainly deliberate and landed in the
"candidate" bucket. I did **not** widen the keyword set to sweep them in — that is
the "widening a regex suppresses a real finding" failure this corpus has already
recorded once. The queue is written to
`scratchpad/ambiguous_straddle.txt`; it needs per-file eyes, not a better regex.

### Unchanged

The bulk migration still lacks its own scoped sign-off (R2 states the end state,
not the sweep), so nothing was migrated. Standing posture holds: new/touched code
uses proton, untouched muon witnesses stay as recorded, never mix within one
quantity, every new witness records its q₀.
