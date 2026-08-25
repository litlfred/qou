---
# qou-cds3
title: 'S3 (SCIENCE): muon -> proton witness migration — 870 not ~840, and 69 straddle both pins'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-25T08:22:10Z
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


## Re-measured 2026-08-25 — 105 both-pin, not 69, and ZERO unpaired straddles

The 69 above is from 2026-08-15; the corpus has grown. Re-measured on main
`2c53783e3d3` over `computations/**/*.witness.json`:

    both-pin witnesses                              105
      DELIBERATE — every site names its own layer    30
      DELIBERATE — computed-at sites layer-PAIRED    19
      ABOUT — audits reporting the pins as data       8
      residue needing a human read                   48
      UNPAIRED computed-at straddles                  0

**The bucket that would be the real defect class is EMPTY.** A witness carrying
both pins is overwhelmingly a deliberate comparison: `/data/muon_anchor/q0`
beside `/data/proton_anchor/q0`, or `/anchors[1]/q` beside `/anchors[0]/q`.
The bean's framing -- "a defect either way" -- does not survive measurement.

**My first classifier said 19 straddles and was wrong.** It required EVERY
mention of a pin to name its layer, so a plain `q0Value` provenance stamp --
which names nothing -- kicked 19 genuine paired comparisons into the straddle
bucket. Testing for PAIRING (is each muon computed-at site matched by a proton
sibling, by name or by index?) absorbed all 19. Five iterations of the
classifier plateaued at ~48 residue, which is the signal that the rest needs
reading rather than more regex.

## TWO confirmed, and they are NOT the same defect

Both are stamped `proton` while their `parameters.q_0_50dps` is muon-family.
Cross-confirmed from an independent direction: both also appear in the
stamp-vs-payload scan recorded on `qou-khac`.

  he3-brane-tower-structural-gap    q_0_50dps = 1.1099785955573347...  = A
      the CANONICAL muon anchor. A plain mis-stamp; the honest label is `muon`.

  he3-tower-charge-asymmetry        q_0_50dps = 1.1099785955541805...  = B
      the CODATA-2018-derived value, which is NEITHER anchor. Same class as
      `meson_mass_from_hecke` (PR #5742), whose honest label is `ambiguous`
      plus a reason naming the value.

Neither is fixed here -- each needs its producer read, which is separate work.

## The bean's "specific trap" note is STALE — do not act on it

The section above tells the reader to check every `y_lambda_at(n, q)` call site
because it "returns the cached muon-built witness". **That was corrected on
2026-08-23** (beans `qou-c1ya` / `qou-vu19`, and AGENTS.md carries the
correction): the live `y_lambda_at` is five statements, reads no witness, and
its whole call cone is cache-free. The gate and the cache load moved into
`_y_lambda_at_convention_C_HISTORICAL`, which is dead code.

Measured cost of following the stale wording: promoting `y_lambda_at` to a
muon identifier reclassified **56 producers** from `proton` to `BOTH`, hiding
56 clean files behind an association the code no longer has.
