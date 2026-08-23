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

### ADDENDUM, same day — the sweep is live, and straddles grow WITH it

Between my first measurement this session and a `main` merge ~1 h later, **232
witness files changed** and the population moved sharply. Both figures are
correct for their tree; verified by counting at each commit
(`git grep -l … 93d4abbf0` → 617, at HEAD → 430).

| | bean 08-15 | 08-21 early | **08-21 HEAD** |
|---|---|---|---|
| total witnesses | 2941 | 2690 | 2694 |
| muon fingerprint | 870 | 617 | **430** |
| proton fingerprint | 588 | 653 | **861** |
| muon-only | 801 | 539 | **332** |
| **both pins** | **69** | **78** | **98** |

The migration is working — muon-only 801 → 332. But **the straddle class grows
with it**: 69 → 78 → 98, i.e. **+20 in the same hour that migrated ~187
witnesses**. That is roughly one new both-pin artefact per nine migrated. It is
consistent with partial migration: a witness that gets its production value moved
to proton while retaining a muon-derived reference now matches both fingerprints.

**Any count here is perishable.** The population moved 30 % in an hour. Quoting a
straddle number without its commit is meaningless; this bean's "69" was accurate
on 2026-08-15 and is now three revisions stale.

### NEW: a straddle class nobody has counted — two MUON pins in one file

The `1.109978595` fingerprint conflates the two muon values `qou-khac` is about.
Splitting it:

| | count |
|---|---|
| stale hand-typed `Q_MUON` (`…55733…`) only | **212** |
| derived `q_muon_at()` (`…55418…`) only | **164** |
| **both muon values in ONE file** | **24** |

Those 24 are an **intra-muon straddle**, and they are invisible to every
muon-vs-proton test — including this bean's, which is why they have never been
counted. `qou-khac` names the two-value problem but scopes it to *3 hand-typed
constants in source*; this is the same defect in the **witness** layer, at 24
files, plus a 212/164 split showing the stale constant is still the **majority**
of muon-bearing witnesses.

Worth doing before the muon→proton sweep finishes: a witness migrated from the
*stale* muon pin inherits a value 3.15e-12 off the one `q_muon_at()` derives, and
once it is relabelled proton nobody can tell which muon value it came from.

### On the structural triage I attempted

I tried to separate deliberate comparisons from straddles by checking whether
both pins sit under a shared JSON parent. **That test does not discriminate** —
calibrating on two cases showed clean comparisons with shared parents:
`peel-anchor-identification` stores `/q0_pins/proton` + `/q0_pins/muon` (its
description: *"no anchor enters it — so both q0 pins can be evaluated from one
expression"*), and `definitive-q0-shift` stores `q0_current` vs
`q0_exact_for_mp`, which is the entire point of the witness. Recorded as a
negative result rather than tuned until it agreed with me.

What would actually discriminate is whether the two pins feed **one computed
quantity** versus sitting in two labelled fields — which needs the producer, not
the artefact. That is the per-file work this bean asks for, and it is not
automatable from the JSON alone.

### ⚠ THE MIGRATION METRIC CANNOT SEE THE WORST CASE — 22 witnesses label a MUON value "proton"

Chasing the 24 intra-muon files turned up something they were a symptom of.

**Measured at HEAD**, over `computations/**/*.witness.json` (excluding
`_deprecated/`), looking at fields whose *name* contains `proton`:

| | count |
|---|---|
| proton-named field holding the real proton pin `1.1099785827513808…` | **63** |
| **proton-named field holding a MUON value** | **22** |

Examples, verbatim:

```
probes/flavor-split-alpha-dilog-expansion   /data/proton_anchor/q0 = 1.1099785955573347…   <- stale MUON
                                            /data/muon_anchor/q0   = 1.1099785955541805…   <- derived muon
                                            /q0Value               = 1.1099785955573347…
qbeta/qbeta-c6-c10-crossanchor-falsification /data/q_proton        = 1.10997859555733471…  <- stale MUON
audits/q0-consistency-audit                  /canonical_proton_q0  = 1.10997859555733471…  <- stale MUON
```

The real proton pin is `1.1099785827513808…`; these are `1.10997859…`. They differ
at the 9th significant digit, so this is not rounding.

**Why this matters more than the straddle count.** This bean measures migration by
**fingerprint** — counting `1.1099785827` as "proton". These 22 witnesses contain
**no proton fingerprint at all**. They are counted as *muon* witnesses awaiting
migration, or as *both*-pin straddles, and in neither case does the metric reveal
that a field literally named `proton` holds a muon number. **The measurement
method is blind to the failure mode it most needs to catch**: right name, wrong
value.

Worse for the sweep: `audits/q0-consistency-audit.witness.json` — the *consistency
audit* — asserts `canonical_proton_q0` = the stale muon constant, and carries
**no `computedAt` and no `scriptHash`**, so nothing flags it as stale.

**Two "cross-anchor" probes are therefore not cross-anchor.**
`qbeta-c6-c10-crossanchor-falsification` and
`qbeta-singularity-cross-anchor-probe` compare `q_proton` against `q_muon` where
`q_proton` holds a muon value — so the "anchor swing" they measure is the
**3.15e-12 gap between the two muon constants** (`qou-khac`), not the ~1.28e-8
muon↔proton separation. Any conclusion drawn from their swing magnitude is scoped
to the wrong comparison. Not re-derived here; flagged.

**Provenance, stated as inference not fact.** Both dated examples were computed in
**June 2026** (`2026-06-29`, `2026-06-22`), before the 2026-08-15 proton ruling. At
a June-era commit the substrate's canonical branch required
`_d["q"].startswith("1.109978595557")` and raised *"not canonical muon"* otherwise
— i.e. **"canonical" then resolved to the muon pin**. So these witnesses recorded
the then-canonical value under a `proton` name. Whether the probes mis-named it in
June or the meaning of "canonical" moved under them, I did not establish, and it
does not change the current state: the field says proton and the value is muon.

**Not fixed here.** Regenerating them is producer work across 22 files and several
of them are `qbeta`-channel probes whose conclusions would move; and hand-editing
a witness value is prohibited outright. The queue is
`scratchpad/proton_mislabel.txt`.

**Bears directly on `qou-khac`**, which scopes the two-muon-value problem to 3
hand-typed source constants. The witness layer carries it at 212 stale-only, 24
both-values, and now 22 mislabelled-as-proton — and the last group will be
*hardest to fix after* the sweep, because once a witness is relabelled there is
nothing left to tell which muon value it came from.

### ANSWERED 2026-08-23 — the mislabelled witnesses are STALE ARTEFACTS, not live producer bugs

The open question on the 22 (20 currently detectable) was whether their producers
*still* emit a muon value into a `proton`-named field. **They do not.** Checked
all 20 named producers — every witness carries a `scriptFile`, so none had to be
guessed:

| how the producer obtains its proton pin | count |
|---|---|
| runtime call / import (`q_at()`, `mpf(str(q_at()))`, `Q_50_DIGIT_STR`, `Q_MP`) | **20** |
| hardcoded muon literal assigned to a proton variable | **0** |

The five that my first pass could not classify resolve the same way on reading —
e.g. `qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py:102` and
`qbeta_c6_c10_crossanchor_falsification.py:153` are both `q_p = mpf(str(q_at()))`.

**Consequence for this bean: these need regeneration, not source repair.** Every
one of them was computed while `q_at()` still returned the muon-anchored value,
and every one would now emit the proton pin unchanged. That is a materially
cheaper item than it looked, and it removes them from the "needs a producer fix"
column entirely.

### But the PROSE did not self-correct, and one file now contradicts itself

`computations/h4_form_AB_cross_anchor_stability.py` is the clearest case. Its code
is correct — `:98` is `q_proton = q_at(DPS)`, resolved at runtime — and its
docstring at `:17` says `q_proton = 1.10997858275…`, also correct. But the ANCHOR
NOTE at the top of the same file (`:1-5`, dated 2026-06-22) says:

> `q0 = 1.10997858275…` occurrences below are the **RETIRED** pre-2026-05-28
> proton anchor … The **CURRENT canonical proton q0 is `q_at()` ≈
> 1.1099785955573347…**

That calls the **muon** value the current canonical proton pin, and declares the
actual canonical value retired — **twelve lines above a docstring that says the
opposite**. It was true when written (`q_at()` did return that value in June) and
the 2026-08-15 ruling reversed it.

This is the same shape as `atomic_tr_m_helium4_canonical.py` in `qou-cds4` and as
`q0_consistency_audit.py` in `qou-ivhc`: **code that resolves a value at runtime
is self-correcting; the prose describing it is not.** Three instances now, in
three different files, all from the same ruling.

The practical hazard is specific: a reader who trusts the ANCHOR NOTE over the
code will "fix" the correct value to the stale one. That is the mechanism by
which a self-correcting producer acquires a real bug.

**Not edited here** — `h4_form_AB_cross_anchor_stability.py`'s header ends
*"This probe is preserved as-is by design"*, so rewriting its banner is a call for
whoever owns that preservation, not a hygiene edit. Recorded with the line numbers
so it is actionable.
