---
# qou-cds3
title: 'S3 (SCIENCE): muon -> proton witness migration — 870 not ~840, and 69 straddle both pins'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-24T13:20:00Z
updated_at: 2026-08-24T02:55:00Z
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

---

## RE-MEASURED 2026-08-23 — still 21 live, and the sibling 563-witness sweep did NOT cover them

The queue file `scratchpad/proton_mislabel.txt` did not survive a container
reset, so the population was re-derived from the artefacts rather than recovered
from the note: **every field anywhere in a witness whose key path contains
`proton` and whose value starts with the muon prefix `1.109978595`**.

```
witnesses with a PROTON-named field holding a MUON value: 21
```

Worth checking explicitly, because it could have been fixed by someone else:
`claude/mass-table-comprehensive-triage` regenerated **563 witnesses** on
2026-08-23 (`qou-fl9i`). **None of these 21 were among them.** The item is live.

A narrower test — top-level `q0Anchor` vs `q0Value` — reports **0 mislabelled**
across 620 proton-labelled witnesses. That is not a contradiction: only 676 of
~2700 witnesses carry those two fields at all, and this defect lives in
producer-specific payload keys (`data.q_proton`, `parameters.q_proton`,
`data.proton_anchor.q0`), not in the anchor stamp. **The anchor-stamp layer is
clean; the payload layer is not** — which is exactly why the migration metric
could not see these.

### Split by whether regeneration moves a published conclusion

| class | n | note |
|---|---|---|
| **qbeta-channel** | **11** | `qbeta_c3_habiro_3rung_crossanchor_rigidity`, `qbeta_c6_c10_crossanchor_falsification`, `qbeta_singularity_cross_anchor_probe`, … — cross-anchor probes whose *result* is a comparison between pins |
| **non-qbeta** | **10** | `h4_form_AB_cross_anchor_stability`, `flavor_split_alpha_*`, `yekutieli_*`, `he4_rho_f_bar_symmetric_audit_probe`, … |

All 21 carry a `scriptFile`; none had to be guessed. All were computed
**2026-06-18 → 2026-07-17**, i.e. before the 2026-08-15 ruling.

### One anomaly, and it ties to `qou-khac`

`habiro-interpolation-wlambda.witness.json` carries
`data.archimedean_F_lambda.proton_q0.q0 = 1.1099785955541805…` — that is **value
B** (the CODATA-2018 evaluation), where the other 20 all carry **value A** (the
frozen canonical muon pin). So this queue is not uniform in *which* muon value it
mislabels. Per the `qou-khac` correction of the same date, B and A are different
objects — B is the live derivation at an older CODATA vintage, A is not
reproducible from any published muon ratio. **Regenerating this one changes a B
to a proton value and destroys the only remaining evidence that it was ever B**,
which is precisely the "hardest to fix after the sweep" hazard this bean warned
about. Do it last, and record the old value in the commit.

### ONE REGENERATED — the inference is now a measurement

The previous section concluded *from reading source* that these need
regeneration, not repair. Verified on `he4_rho_f_bar_symmetric_audit_probe.py`:

```
q_proton  before  1.1099785955573347198997…   (muon)
q_proton  after   1.1099785827513808075916…   (proton)
```

- The probe's **conclusion is unchanged** — *"BAR-SYMMETRIC ρ_F CANDIDATES ALL
  FAIL — best is C1 at +5.87% vs the current production at +5.87%"* — so for this
  one, regeneration is genuinely hygiene.
- The **environment record improved** rather than degraded: `scipy None → 1.17.1`,
  `mpmath 1.3.0 → 1.4.1`, python/numpy unchanged. No environment warning fired.
  (Checked because the `guarded-off-audit` refresh in `qou-i5jy` had to be
  abandoned for the opposite reason.)
- The 28 raw-float64 fields the guard warns about **pre-existed** —
  `candidates[].value_numeric` and friends were already `float` in the committed
  witness. Not introduced here, and not fixed here either.
- Ran in well under 9 minutes.

**20 remain.** Not batched in this session: the container has reset four times
today, and a long serial regeneration would be lost mid-run. Each is now a
one-file job with a known producer, so they can be drained individually and
pushed as they land.

### Still the owner's call, unchanged

The **bulk** muon→proton migration. R2 states an end state, not a sweep. These 21
are a different argument — a field named `proton` holding a muon value is wrong
under either reading — but the 11 qbeta cross-anchor probes are the overlap: a
probe whose *purpose* is to compare two pins may be recording the pins it
actually used, in which case the label is right and the value is right and only
the name reads oddly. **Check that per-probe before regenerating any of the 11.**

---

## ⚠ 2026-08-23 — SEVEN REGENERATIONS RUN AND DELIBERATELY NOT COMMITTED. Regeneration is not hygiene.

Last section I regenerated `he4_rho_f_bar_symmetric_audit_probe`, found its
conclusion unchanged, and wrote that *"for this one, regeneration is genuinely
hygiene."* **That generalised, and the generalisation is wrong.** I then ran the
other seven non-qbeta producers and reverted every one.

### What regenerating actually does

A witness computed in **June 2026** and regenerated in **August** replays *every*
producer change in between — not just the q₀ pin. Two are load-bearing here:

- **`e5dcd8f54`** (2026-08-01) — *"A=3 magnitude r\*≈1.585 is a FREE parameter of
  the Berezinian cross-term"*. A physics change, touching all three probes I
  spot-checked.
- **`bc96793e5`** (**2026-08-23, today**) — a **sibling's** q0-literal migration
  (`claude/q0-literal-transcription-drain`), which edited
  `binding_qgaussian_ell1_ceiling_measurement.py`.

So the mislabel fix **cannot be isolated by regeneration**. Running the producer
applies the pin correction *and* two months of unrelated evolution in one commit.

### Measured, on the seven

| witness | what moved |
|---|---|
| `xq-habiro-element-search-probe` | **all 6 candidates `TIER 1 (cross-anchor proved-candidate)` → `TIER 2 (near-match)`** |
| `binding-qgaussian-ell1-ceiling-measurement` | `muon_anchor.rows[0].classical_ceiling_over_target` 0.516 → 0.566 (**9.7 %**) |
| `flavor-split-alpha-*` | `alpha_true_anchor_drift` 5.8e-8 → 2.4e-4 (**4000×**) |
| `option-e-v9-bar-symmetric-test-probe` | 29 non-pin fields; verdict held |
| `yekutieli-*` | `data.h` moved at 1e-8; verdicts held |

A 9.7 % move is not an 11.5 ppb pin shift, and `muon_anchor.*` fields moving at
all is the tell: these probes' **muon legs** changed too. Every one still reported
*"1 assertions, all passed"* — which is exactly why "assertions passed" is not a
substitute for diffing the payload.

### The one that is a finding in its own right, independent of the pin

`xq-habiro-element-search-probe.witness.json` **as committed advertises six
`TIER 1 (cross-anchor proved-candidate)` results that the current producer does
not reproduce** — it now grades all six `TIER 2 (near-match)`. The committed
artefact is not merely stale in its pin; it is asserting a stronger claim than
today's code supports. That is worth someone's attention on its own terms, and it
was invisible until a regeneration was attempted. **Not resolved here** —
deciding whether June's TIER 1 or August's TIER 2 is correct is `qbeta`/Berezinian
subject matter, not migration hygiene.

### Why the `he4` commit still stands

Re-checked its committed diff field by field: 34 non-pin fields moved, all at the
**ppb level** (`B_pred_MeV` 29.95567724 → 29.95567728, ~1.4e-9 relative) and the
verdict is identical (+5.87 %, all candidates fail). That is the pin correction
propagating and nothing else — the honest outcome of a regeneration whose producer
had not meaningfully changed. Kept.

### Consequence for this bean

The remaining **20** are not a drain queue. Each needs its payload diffed against
the committed witness **before** the regeneration is committed, and any probe
whose conclusion moves needs an owner, not a hygiene commit. That applies to the
non-qbeta ten as much as the qbeta eleven — the split I drew last section was the
wrong axis. The right axis is **"has this producer changed since the witness was
computed?"**, which is a one-line `git log` per file and should be the first
question, not the last.

---

## 2026-08-23 — two cheap proxies for "will regeneration move conclusions", and BOTH are wrong

Last section ended by recommending a one-line `git log` per producer as the first
question. **I tried it, and it does not work.** Then I tried the mechanism the
corpus is actually built on, and that does not work either. Each failure has a
concrete counterexample, so both are recorded rather than just the fix.

### Proxy 1 — `git log --since=<witness date> -- <producer>`. REJECTED.

It reported **0 of 20 producers unchanged**, with `e5dcd8f54` (2026-08-01) as the
sole commit for **14 of them** — which looked like a single reviewable class.

It is not. `e5dcd8f54` is a **28,620-file, 9,957,932-insertion** commit that adds
`uploads/*.pdf` and shows these producers as `new file mode`: a bulk
import/re-baseline of the tree, not a change to any probe. **My own recommendation
from the previous section was measuring repository history, not producer history.**

### Proxy 2 — recorded `scriptHash` vs the current file. BETTER, STILL WRONG.

The designed mechanism (`witness.scriptHash` = sha256 prefix of the producer's
bytes, `witness.py:417`). It separates cleanly:

| | n |
|---|---|
| `scriptHash` **matches** — producer byte-identical since the witness was made | **13** |
| `scriptHash` **differs** — producer genuinely changed | **7** |

`h4-form-AB`, `binding-qgaussian`, both `flavor-split-alpha-*`, and three `qbeta`
cross-anchor probes are the seven that really moved.

**But `xq-habiro-element-search-probe` is in the MATCHES column** — and
regenerating it flipped all six candidates `TIER 1 → TIER 2`. A byte-identical
producer produced a different verdict.

### Why, and it is the interesting part

`scriptHash` covers the **producer file only**. `xq_habiro_element_search_probe.py`
imports `_precision`, `witness_base`, `experimental_constants`, and via
`_path_bridge` the substrate — and the substrate's muon input moved. `qou-khac`
measured it directly this session at dps=60:

```
MASS_RATIO_MU_E_STR   206.7682830  (CODATA 2018)  ->  206.7682827  (CODATA 2022)
q_muon_at()           1.109978595554180…          ->  1.109978595642739…
```

`constants.py:231` now reads `MASS_RATIO_MU_E_STR = _MU_E.value_str  # CODATA 2022`.
(The `git log -S` history for that line is unreadable — it resolves to the same
bulk-import commit — which is *why* the runtime measurement in `qou-khac` was
worth doing.)

So a probe with a muon leg changes output while its own bytes, and therefore its
`scriptHash`, are unchanged.

### Corpus-level consequence — this is a hole in the staleness apparatus itself

`producer_importability_audit`'s own thesis is that *"every existing staleness
mechanism compares a witness against its producer: `witness.scriptHash` vs the
current file hash…"*. **`scriptHash` is blind to dependency drift, and there is a
live instance in this queue.** A witness can be materially stale — asserting
`TIER 1` where the current code says `TIER 2` — with every drift detector green,
because nothing hashes what the producer *imports*.

Same shape as `qou-i5jy`: a check reporting clean over a surface it does not
cover. Recorded here because it is discovered from the migration queue, but it is
not a cds3 defect and is bigger than this bean.

### Settled method for the remaining 20

Neither proxy is sound, so the only reliable test is the one used last section:
**regenerate into a snapshot, diff the payload excluding pin/timestamp/env fields,
and decide per witness.** It costs a producer run each, and that cost is not
avoidable by inspection — which is the useful thing to have established, since
both cheap alternatives look convincing until they are checked.

### NARROWING the "nothing hashes what the producer imports" claim (same day)

Two sibling beans landed on `main` while this was being written, and both bear on
the paragraph above. Checked before leaving the claim standing.

**`qou-jvav`** — *"witness_dependency_drift resolver missed subdirectory upstreams
— 357 of 688 drift records were false."* So the corpus **does** have an
upstream-drift mechanism (`witness_dependency_drift.py`, wired into
`staleness-gates.sh`), and my "nothing hashes what the producer imports" was too
strong. Narrowed to what is actually true, on three measurements of my own:

1. It tracks **declared upstream witnesses** (`upstream_witness_hashes`), not
   Python module imports. A probe importing `qou_substrate.constants` declares no
   upstream witness for it, because there is no witness to declare.
2. Almost nothing declares them anyway: `witness_dependency_coverage_audit`,
   run this session, reports **2 of 2643 witnesses (0.1 %)** carrying
   `upstream_witness_hashes`.
3. So for `xq-habiro-element-search-probe` specifically — `scriptHash` matched,
   no upstream declared, output flipped `TIER 1 → TIER 2`. The gap is real for
   this witness; the general claim was not.

**`qou-a31p`** — *"Witness regeneration flipped 29 assertions PASS→FAIL and every
blocking gate stayed green."* Independently, on commit `a0ee2ac5e` (the 563-witness
sweep), a sibling measured exactly the failure mode this section reasoned toward:
regeneration moves results, and *"assertions all passed"* does not catch it —
because the failed-assertion ratchet is wired **advisory** in
`precision-gates.sh:118`, `blocking = no`. Their measurement is stronger than my
inference: 29 flips, net −27, 136 witnesses / 177 failed assertions against a
baseline of 111.

**Reattributed accordingly.** My contribution here is the narrower one: that the
payload diff is the only sound pre-commit test, with `git log --since` and
`scriptHash` each falsified by a counterexample. The consequence at corpus scale
is `qou-a31p`'s, measured on a real sweep, not mine.

### Merge note — the two conflicted chi witnesses

Merging `origin/main` conflicted on
`chi-at-q0-rust-lossless-helium-4.witness.json` and
`chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json` — the collision `qou-k3wq`
predicted (item C3). Resolved by taking **main's** side: newer (2026-08-23
`a0ee2ac5e` vs my 2026-08-21 `dc30f78a0`), a legitimate producer run, and taking
mine would have reverted a sibling's work. Hand-merging was never an option —
witness numbers may not be edited.

Checked against `qou-a31p` before accepting, since `a0ee2ac5e` is the commit that
flipped 29 assertions: **neither file is named in that bean, and both carry zero
assertions**, so neither can be among the flips. Both are also clean of the
convention-C `z` literal on both sides, so `qou-cdh3`'s property survives the
resolution either way.

---

## 2026-08-23 — THREE MORE COMMITTED, by the settled method. Running total 4 of 21.

Applied the method fixed in the previous section — regenerate into a snapshot,
diff the payload, decide per witness — to the three of last section's seven whose
verdicts had held.

| witness | largest non-pin move | verdict |
|---|---|---|
| `option-e-v9-bar-symmetric-test-probe` | **5.7e-8 percentage points** on `err_vs_target_pct`; `predicted_B_diff_MeV` 4.4e-10 MeV | `data.verdict` **byte-identical** |
| `yekutieli-a2-em-gauge-coupling-h2-probe` | 2.2e-7 relative on `u1_ansatz_h2_weight` | held |
| `yekutieli-per-cell-qlambert-decomposition-probe` | 2.2e-7 relative on `per_cell_hypotheses[5].value` | held |

All three: mislabelled proton-named field **1 → 0**, failed assertions **0 → 0**,
no environment downgrade.

### A methodological correction, because the first pass over-flagged

I screened on **relative** movement against the 11.5 ppb pin shift, and it flagged
`option-e-v9` at 5.9e-6 — 500× the pin — which looked like another
conclusion-mover. It is not. The flagged field is
`candidates[0].err_vs_required_factor_pct`, a **residual near −0.103**: a
6.1e-7-percentage-point change on a near-zero quantity reads as a large *relative*
move and is nothing in absolute terms.

**Relative change is the wrong metric for a field that is itself an error or
residual.** Screening must look at absolute movement in the field's own units, and
at the verdict, before calling anything a regression. Recorded because the same
screen would misfire on every `*_pct`, `*_err*`, `*_residual*` field in the
remaining queue.

The ~2.2e-7 moves on the two `yekutieli` probes are ~19× the pin shift — expected
amplification through the formula, not a separate effect, and both verdicts hold.
Stated rather than rounded to "consistent with the pin".

### Running state of the 21

| | n |
|---|---|
| committed, verdict-preserving | **4** — `he4_rho_f_bar`, `option_e_v9`, `yekutieli_a2`, `yekutieli_per_cell` |
| regenerated, REVERTED — conclusion moves | **4** — `xq_habiro` (TIER 1→2), `binding_qgaussian` (9.7 %), both `flavor_split_alpha_*` (drift 4000×) |
| not yet regenerated | **12** — 11 `qbeta` + `habiro_interpolation_wlambda` |
| excluded by design | **1** — `h4_form_AB_cross_anchor_stability` (*"preserved as-is by design"*) |

`habiro_interpolation_wlambda` still goes last: it is the only one carrying muon
**value B**, and regenerating it destroys the evidence of which muon value it held.

---

## 2026-08-23 — four left the queue without me: the sibling sweep committed the changes I declined

Re-scanning after merging `origin/main`, the queue is **13**, not the 17 that
`21 − 4 committed` predicts. Four are gone, and three of them are **exactly the
ones I regenerated, measured as conclusion-moving, and reverted**:

| witness | fixed by |
|---|---|
| `binding-qgaussian-ell1-ceiling-measurement` | `a0ee2ac5e` |
| `flavor-split-alpha-bond-dilog` | `a0ee2ac5e` |
| `flavor-split-alpha-dilog-expansion` | `a0ee2ac5e` |
| `qbeta-route-alpha-lift-prediction` | `a0ee2ac5e` |

`a0ee2ac5e` is the sibling's **563-witness** sweep (`qou-fl9i`), which reached
this branch through the merge.

### My measurements were exactly right, and that is checkable

The committed versions carry the values I recorded before reverting:

```
flavor-split-alpha-*  alpha_true_anchor_drift  0.00023620856905347091…   (I measured 2.4e-4, was 5.8e-8)
binding-qgaussian     inflation_anchor_drift   0.00000023211456270013…   (I measured 2.3e-7, was 6.9e-11)
```

Independent regeneration, identical numbers to every digit I had. So the
movement is real and reproducible, and reverting did not make it go away — it
landed by another route.

### Was the caution wrong? No, but it was about a different thing

All three still report `allPassed: true, failed: 0`, so **they are not among
`qou-a31p`'s 29 flips** — their assertions tolerate the movement. On correctness,
the sibling's commit is fine and arguably better than my revert: the new values
are computed at the proton pin with current code.

What I was protecting was not correctness but **attribution and visibility** — a
4000× move in a published drift metric should not ride inside a commit whose
stated purpose is fixing a mislabelled field. That concern stands independently
of these three being harmless, and `qou-a31p` exists precisely because the same
563-witness sweep *did* silently break 29 assertions elsewhere while every
blocking gate stayed green.

**Recorded rather than quietly dropped**, because "I declined to commit X and
someone else committed X" is exactly the kind of thing a work-plan should surface
instead of leaving the next reader to wonder why the queue shrank.

---

## 2026-08-23 — the qbeta batch: 6 committed, 4 held back, and the mislabel turns out to be TWO different defects

Ran all 11 remaining qbeta-channel producers. Results split four ways, and the
split corrects this bean's earlier conclusion that *"these need regeneration, not
source repair."* **Two of them need source repair and regeneration cannot touch
them.**

### THE HEADLINE — the mislabel made every cross-anchor probe compare an anchor with ITSELF

`qbeta-c3-habiro-3rung-crossanchor-rigidity`, before regeneration:

```
q_muon   = 1.109978595554180575281594   <- value B (CODATA-2018 muon)
q_proton = 1.109978595557334719899763   <- value A (the FROZEN CANONICAL MUON PIN)
```

Both legs are muon. The probe was measuring the **B↔A separation (3.15e-12)** and
reporting it as the muon↔proton cross-anchor swing. After the fix it is a real
11.5 ppb comparison — and the reported swings grow by three to four orders of
magnitude across the batch:

| probe | swing before | swing after |
|---|---|---|
| `qbeta-c3-habiro-3rung` | −1.52e-10 % | **+6.23e-07 %** |
| `qbeta-c6-c10-falsification` | 5.82e-11 % | **2.38e-07 %** |
| `qbeta-li2q-spectral-combiner` | 1.91e-12 % | **7.79e-09 %** |

**Every qualitative verdict survives** — `RIGID`, `EMPIRICAL — SILVER-ANCHORED`,
`STRUCTURAL REFUTATION CONFIRMED` — because each rests on *swing ≪ empirical*
(−2.88 %, 1 %), and that inequality still holds by orders of magnitude. But those
verdicts were previously supported by a **degenerate comparison**: a probe whose
job is to discriminate two anchors was handed the same anchor twice. The
conclusions are unchanged; the evidence for them is now real. That is the
`AGENTS.md` "never straddle the two layers inside one quantity" rule, caught in
the act.

### The two that regeneration CANNOT fix — a live source defect, not a stale artefact

`qbeta-composite-crossanchor-2factor-sweep` and
`qbeta-cosh-avatar-crossanchor-multicoeff-probe` came back **still mislabelled
(1 → 1)** after a clean run.

Traced: `computations/substrate/q_parameter.py:100-108` resolves the anchor from
`QOU_Q0_ANCHOR`, and **when that is unset it auto-selects by the running
producer's `sys.argv[0]` stem** against `q0_anchor_manifest.json`. Both producers
are in the **`ideal_muon`** layer (110 producers), so `q_at()` *correctly* returns
the muon pin for them — and they write it into a field named **`q_proton`**.

So the defect is the field NAME in the producer source, not the value, and no
number of regenerations will change it. It also explains why this bean's earlier
audit — *"all 20 obtain their pin at runtime via `q_at()`; zero hardcode a muon
literal"* — was true and still missed these: `q_at()` returns a **different value
depending on how the script is invoked**. A `python3 -c` replication of the same
two lines returns the proton pin, because `argv[0]` is then `-c` and the manifest
never matches.

### Committed — 6, mislabel cleared, verdict preserved

`qbeta-c3-habiro-3rung-crossanchor-rigidity`,
`qbeta-li2q-spectral-combiner-crossanchor`, `qbeta-c6-c10-crossanchor-falsification`,
`qbeta-cosh-q-sinh-q-candidate-scan`, `qbeta-delta-tau-m-canonical-explicit-instance`,
`qbeta-signed-vs-abs-tower-diagnostic`. All: mislabelled field 1 → 0, failed
assertions 0 → 0, no environment downgrade. The only textual changes are embedded
swing figures and `engineVersion mpmath 1.3.0 → 1.4.1`.

### Held back — 4

| witness | why |
|---|---|
| `xq-habiro-element-search-probe` | 6 candidates `TIER 1 → TIER 2` |
| `qbeta-jacobi-anger-tower-general` | `allPassed true → false`; one assertion flips |
| `qbeta-composite-crossanchor-2factor-sweep` | ideal-layer naming defect; regeneration is a no-op on it |
| `qbeta-cosh-avatar-crossanchor-multicoeff-probe` | same |

### Blocked — 1, by an upstream data defect

`qbeta_singularity_cross_anchor_probe.py` crashes before writing:

```
mp.mpf(str(v))  ->  ValueError: invalid literal for int() with base 10: ''
```

reading `c_k_extracted_50dps` from `qbeta-decay-sdp-extended-ck.witness.json`
(`:97-103`). A stored value has a malformed exponent, so the producer cannot run
at all. **Its witness is untouched** — nothing was half-written.

### Queue state

4 + 6 = **10 of 21 committed**. 4 held back on conclusion movement, 2 reclassified
as source defects, 1 blocked upstream, 1 excluded by design (`h4_form_AB`),
`habiro_interpolation_wlambda` still last (only carrier of value B), and 3 were
fixed by the sibling sweep.

---

## 2026-08-23 — `habiro_interpolation_wlambda` is the THIRD source defect, settled without running it

This bean has repeatedly said `habiro_interpolation_wlambda` must be regenerated
**last**, because it is the only carrier of muon **value B** and regenerating
destroys the evidence of which muon value it held. Reading it settles the
question without spending the run at all.

Its two q₀ fields, as committed (2026-07-17):

```
data.archimedean_F_lambda.muon_q0.q0    = 1.1099785955573347   <- value A (frozen muon pin)
data.archimedean_F_lambda.proton_q0.q0  = 1.1099785955541805   <- value B (CODATA-2018 muon)
```

**Neither leg is the proton pin.** The probe's "archimedean F_λ at proton vs muon
q₀" comparison is B-versus-A — a 3.15e-12 muon-to-muon gap presented as the
11.5 ppb muon-to-proton one. That is the **third** independent instance of the
degenerate-comparison pattern found today, after the qbeta cross-anchor batch.

### Why regeneration cannot fix it

`habiro_interpolation_wlambda` **is in the `ideal_muon` manifest layer**. Under
that layer `q_parameter` re-derives the q-family from
`computations/q-pinning-50-digit.witness.json`, which holds

```
q0Value = 1.10997859555733471989976322048322     <- value A
```

So for this producer `q_at()` returns **A**, and `q_muon_at()` returns **C**.
A regeneration would rewrite the fields as `proton_q0 = A`, `muon_q0 = C` —
**still two muon values**, with the proton-named field still holding a muon
number. The defect is the field name in source, exactly as for
`qbeta_composite_crossanchor_2factor_sweep` and
`qbeta_cosh_avatar_crossanchor_multicoeff_probe`.

**So it is NOT the value-B evidence problem this bean feared.** Value B survives
in the committed witness and should stay there until the naming is fixed; running
the producer would have destroyed it *and* achieved nothing. Recorded here as the
value of record:

```
habiro-interpolation-wlambda.witness.json
  data.archimedean_F_lambda.proton_q0.q0 = 1.1099785955541805    (value B)
  data.archimedean_F_lambda.muon_q0.q0   = 1.1099785955573347    (value A)
  computedAt 2026-07-17T20:26:41Z   scriptHash 02bbdfe7dd7a
```

### Revised queue arithmetic

The "regenerate" class is smaller and the "source naming defect" class is larger
than this bean assumed:

| class | n |
|---|---|
| committed, verdict-preserving | **10** |
| held back — conclusion moves | 2 (`xq_habiro`, `qbeta_jacobi_anger`) |
| **source naming defect — regeneration is a NO-OP** | **3** (`qbeta_composite_crossanchor`, `qbeta_cosh_avatar`, `habiro_interpolation_wlambda`) |
| blocked by an upstream malformed value | 1 (`qbeta_singularity_cross_anchor`) |
| excluded by design | 1 (`h4_form_AB`) |
| fixed by the sibling sweep | 3 |
| unresolved remainder | 1 |

**Not fixed here.** Renaming `proton_q0` / `q_proton` in an ideal-layer producer
changes a published witness field name, which is a contract change for anything
reading it — and this bean's own §"the last group will be hardest to fix after
the sweep" warns against unilateral moves in this area. The three are now
identified precisely, with the mechanism, which is what the fix needs.

---

## 2026-08-23 — the blocked probe: my "malformed exponent" diagnosis was WRONG

I recorded that `qbeta_singularity_cross_anchor_probe.py` is blocked because *"a
stored value has a malformed exponent"*. **There is no malformed value.**
Verified directly:

```
c_k_extracted_50dps = {'c_2': None, 'c_3': None, … 'c_10': None}    all null
str(None)            = 'None'
'None'.split('e')    = ['Non', '']
mp.mpf(str(None))    -> ValueError: invalid literal for int() with base 10: ''
```

The "empty exponent" is the **letter `e` inside the word `None`**. mpmath splits
the mantissa on `e`, gets `['Non', '']`, and calls `int('')`. The probe's
`mp.mpf(str(v))` turns a JSON `null` into that error.

### The nulls are deliberate, and the probe is a stale consumer

`qbeta_decay_sdp_extended_ck.py:463-466` writes `None` for every unresolved rung:

```python
w.add_data("c_k_extracted_50dps", {
    f"c_{k}": (mp.nstr(v, 50) if resolved[k] else None) for k, v in c_k.items()})
```

Introduced by `e5885ebc0` — *"SDP c_k extractor emitted the residual FLOOR as
data"* (bean `qou-8ofm`). The witness records `last_resolved_rung: null`,
`n_unresolved: 9`, so **all nine rungs are null**. The raw quotients are preserved
under `c_k_unresolved_raw_quotient`, and their successive ratios lock onto
117.409001 = the recorded `one_over_u` — the floor/uᵏ blow-up signature the fix
exists to stop publishing.

So the blockage is **not an upstream data defect**. It is a consumer written
against the pre-`e5885ebc0` format, which coerces a sentinel instead of skipping
it. The fix belongs in the probe (`skip or raise on None`), not in the witness —
and there is no "correct number" to substitute, because the whole point of
`qou-8ofm` was that those numbers were spurious.

### A worse instance of the same shape, found while checking the breadth claim

`computations/deltalambda/binding_weight_markov_pinning_probe.py:125` uses the
same `mp.mpf(str(v))` idiom — but inside:

```python
    try:
        …  return {…: mp.mpf(str(v)) …}, "canonical-module"
    except Exception:
        return dict(Y_LAMBDA_CACHE.get(n, {})), "verified-cache"
```

A `None` here does **not** crash. It raises, is swallowed by the bare
`except Exception`, and the function silently returns a **cached** y_λ table
labelled `"verified-cache"`. That is strictly worse than the crash: the crash
stops and says so; this substitutes different data and calls it verified. Same
family as `qou-i5jy`.

### Breadth NOT established — stated as a bound, not a finding

`grep` counts **687** `.py` files under `computations/` using `mp.mpf(str(`, of
which **495** also mention `witness.json`. **These are file counts, not verified
call sites**, and this campaign's own rule is to verify counts by resolving call
sites rather than by `grep -rl`. They are recorded as an upper bound on where the
idiom *could* meet a `null`, and nothing more. The corpus holds ~6600 `null`s
sitting in dicts whose siblings are numeric strings, so the collision surface is
real — but how much of it is live is unmeasured.

**Consequence for this bean:** `qbeta_singularity_cross_anchor_probe` moves out of
"blocked by upstream data" and into "consumer needs a null guard" — a one-line
source fix in a file this bean does not own, so it is reported rather than made.

---

## CORRECTION 2026-08-23 — my mechanism for the "source defects" was wrong; the count and membership change

I recorded three source-naming defects, all attributed to the `ideal_muon`
manifest auto-select. **The mechanism is narrower than I said, and only two of my
three belong to it.**

The auto-select in `computations/substrate/q_parameter.py:100-108` rebinds
`q_at` / `Q_50_DIGIT_STR` **only inside the `q_parameter` module namespace**
(`:206-217`); `qou_substrate.constants` is left untouched. So manifest membership
is **not sufficient** — the producer must also import through `q_parameter`.
Verified by reading the import lines:

| producer | import route | today's `q_at()` | verdict |
|---|---|---|---|
| `qbeta_composite_crossanchor_2factor_sweep.py:88` | `from q_parameter` | **muon** | source defect ✓ |
| `qbeta_cosh_avatar_crossanchor_multicoeff_probe.py:106` | `from q_parameter` | **muon** | source defect ✓ |
| `qbeta_singularity_cross_anchor_probe.py:92` | `from qou_substrate.constants` | proton | **STALE**, not a source defect |
| `qbeta_jacobi_anger_tower_general.py:87` | `from qou_substrate.constants` | proton | **STALE** |
| `xq_habiro_element_search_probe.py:72` | `from qou_substrate.constants` | proton | **STALE** |

So `xq_habiro`, `qbeta_singularity` and `qbeta_jacobi_anger` are in `ideal_muon`
but bypass the mechanism entirely.

### `habiro_interpolation_wlambda` — right conclusion, wrong reason, and the real reason is worse

I wrote that its `proton_q0` is fed muon *by the manifest*. It is not.
`habiro_interpolation_wlambda.py:372`:

```python
Q0_PROTON = mpf("1.1099785955541805")    # package-layer proton-pinned q₀ (constants.py)
```

A **hardcoded literal**, with a comment asserting it came from `constants.py`. It
did not: that is the *old* `q_muon_at()` closed form (value B). So the file
hardcodes a muon value, names it `Q0_PROTON`, and documents it as the proton pin
— wrong on all three counts, and none of them touched by regeneration.

My conclusion ("regeneration is a no-op, do not run it") **stands and is
reinforced** — a hardcoded literal is even less reachable by re-running than a
manifest lookup would be. But the reason I gave was wrong, and the correct reason
identifies a defect that `q_at()`-based reasoning would never have found.

### An agent inference I checked and did NOT adopt

It was reported that `binding_qgaussian_ell1_ceiling_measurement.py` is a
**latent** instance — its committed witness is correct, but re-running would
introduce the mislabel, since it takes `Q_50_DIGIT_STR` from `q_parameter` (`:69`)
and is in `ideal_muon`.

The mechanism is real in isolation: forcing `sys.argv[0]` to that script's name,
`Q_50_DIGIT_STR` does resolve to the muon pin. **But two actual runs contradict
the prediction** — the sibling sweep `a0ee2ac5e` and my own regeneration both
produced the correct proton value, and the committed witness holds
`proton_anchor.q0 = 1.10997858275138…` with `muon_anchor.q0` at the current value C.
`measure()` records `"q0": str(q)` directly from `mpf(Q_50_DIGIT_STR)` (`:214`,
`:223`), so there is no laundering step between them.

There are **two** `q_parameter.py` in the tree — `computations/substrate/` and
`qou-mass/src/qou_mass/_internal/` — which plausibly explains why an isolated
import resolves differently from the producer's own path setup. **I did not pin
it down**, and I am not recording a latent defect on an inference that direct
evidence contradicts. Noted as an open question about the auto-select's
invocation sensitivity, not as a finding.

### Corrected arithmetic

| class | was | now |
|---|---|---|
| source naming defect (regeneration is a no-op) | 3 | **3**, but different membership: `qbeta_composite`, `qbeta_cosh_avatar` (manifest route) + `habiro_interpolation_wlambda` (hardcoded literal) |
| stale — regeneration fixes | — | `xq_habiro`, `qbeta_singularity`, `qbeta_jacobi_anger`, `h4_form_AB` (the last in `ambiguous`, so auto-select never fires) |

Two of those four stale ones are already held back for *conclusion movement*
(`xq_habiro` TIER 1→2, `qbeta_jacobi_anger` assertion flip), and
`qbeta_singularity` is the null-sentinel consumer. So the reclassification does
not free any of them to be committed — it corrects **why** each is where it is.

---

## ⚠ REGRESSION I INTRODUCED 2026-08-23 — six witnesses now declare an anchor their numbers do not use

Caught while re-running `qbeta_singularity_cross_anchor_probe` on a recovered
checkout. **My own cds3 regenerations added a false `q0Anchor` stamp to six
committed witnesses.**

```
q0Anchor (stamp) : "muon"
q0Value  (stamp) : 1.1099785955573347…      <- value A
data.q_proton    : 1.1099785827513808…      <- the REAL proton pin, computed
data.q_muon      : 1.1099785956427390…      <- value C, computed
```

Neither computed value is the stamped one. Verified `BEFORE` → `AFTER` on each:

| witness | before | after |
|---|---|---|
| `option-e-v9-bar-symmetric-test-probe` | `q0Anchor: None` | `"muon"` / A |
| `qbeta-c6-c10-crossanchor-falsification` | `None` | `"muon"` / A |
| `qbeta-cosh-q-sinh-q-candidate-scan` | `None` | `"muon"` / A |
| `qbeta-signed-vs-abs-tower-diagnostic` | `None` | `"muon"` / A |
| `yekutieli-a2-em-gauge-coupling-h2-probe` | `None` | `"muon"` / A |
| `yekutieli-per-cell-qlambert-decomposition-probe` | `None` | `"muon"` / A |

(committed in `245a6d1d5` and `bd4067648`; `he4_rho_f_bar` is unaffected — still
unstamped.)

### Mechanism

`WitnessBuilder` stamps the anchor from `q0_anchor_manifest.json`: all six
producers are listed `ideal_muon`, so the stamp reads muon and takes value A from
the pinning witness. But all six import `q_at` / `q_muon_at` from
**`qou_substrate.constants`**, which the manifest auto-select never rebinds — so
they compute at the real proton pin. Measured across the layer: of **124**
`ideal_muon` producers, **49** import via `q_parameter` (stamp agrees with
computation) and **11** via `qou_substrate.constants` (stamp cannot agree). Six of
those 11 are the witnesses above.

### Why this is worse than what it replaced

`q0_anchor_consistency_audit.py` checks `q0Anchor` against **`q0Value`** — stamp
against stamp — not against the payload (`_EXPECTED_PREFIX`, `:97`, `:111`). A
`muon` stamp carrying value A **matches**, so all six now classify **`Q0_OK`**.
Before my change they were `Q0_ANCHOR_MISSING`, which the audit documents as
*"pre-backfill; not a failure"* — visibly unstamped.

**So I moved six witnesses from "visibly unstamped" to "confidently mis-declared
and passing a gate."** That is this campaign's own defect shape, authored by me.

### How my verification missed it

My payload diff excluded any key whose name contains `"q0"`, on the reasoning that
pin fields are *expected* to change in a pin migration. The field is called
**`q0Anchor`**. The filter that was supposed to suppress known noise suppressed
the one field that records what the witness claims about its anchor — a blind spot
of exactly the kind `qou-i5jy` catalogues, in the checking code I wrote to avoid it.

### Not reverted, and why — but this needs an owner

The **payload** fix is correct and should stand: those files previously held a
muon value under a proton-named field, and now hold the proton pin. Reverting
would restore a worse defect. What is wrong is the **declaration**, and it cannot
be fixed by editing the witness — the stamp comes from the manifest, and witness
numbers may not be hand-edited. The real repair is one of:

1. remove these 11 producers from `ideal_muon` (they compute at proton — the
   manifest entry is what is false), or
2. switch their imports to `q_parameter` so the manifest actually governs them,
3. and independently: make `q0_anchor_consistency_audit` compare the stamp against
   the **computed payload**, not only against `q0Value`. As written it can only
   ever catch a stamp that contradicts itself.

(3) is the general fix and is the one that would have caught me.

---

## 2026-08-24 — the THIRD seam, and a detector for it

The regression above (six witnesses stamped `muon` while computing at proton)
passed **both** existing anchor checks. Verified by calling them directly:

```
witness                                              classify()        payload_mislabels
option-e-v9-bar-symmetric-test-probe                 Q0_OK             0
qbeta-c6-c10-crossanchor-falsification               Q0_OK             0
qbeta-cosh-q-sinh-q-candidate-scan                   Q0_AUDIT_EXEMPT   0
qbeta-signed-vs-abs-tower-diagnostic                 Q0_OK             0
yekutieli-a2-em-gauge-coupling-h2-probe              Q0_OK             0
yekutieli-per-cell-qlambert-decomposition-probe      Q0_OK             0
```

Because they test different things, and neither is this:

| check | compares | blind to |
|---|---|---|
| `Q0_OK` / `Q0_FLIP` | envelope ↔ envelope (`q0Anchor` vs `q0Value`) | what the payload actually used |
| `payload_mislabels` | field NAME ↔ field VALUE inside `data` | a field whose name and value **agree** |
| **(missing)** | **envelope ↔ payload** | — |

A witness stamped `muon`, whose `q0Value` is the canonical muon pin, and whose
payload holds only proton values in fields correctly named `q_proton`, is
self-consistent on every axis anyone was measuring. That is exactly the shape I
produced.

### `envelope_vs_payload` added

Reports only when the evidence is unambiguous — the other anchor's pin is present
**and** the stamped anchor's is absent. A witness with no q0-shaped payload gives
no evidence either way and is not reported (`zhabiro-phiq-production-crosscheck`
is correctly silent for this reason, despite being a known stamp/compute
contradiction: its payload carries no q0 field at all).

Corpus sweep: **9 mismatches — 8 `muon` stamp / proton payload, 1 the other way.**

| | |
|---|---|
| mine, introduced today | 6 |
| **pre-existing** | **3** — `derivation-chain-audit`, `casimir-macdonald-probe`, and `h4-form-AB-cross-anchor-stability` (**proton** stamp / **muon** payload) |

So the class is real and bidirectional, and it existed before my six. `h4_form_AB`
is the file this bean already excluded from regeneration as *"preserved as-is by
design"* — it turns out to carry the mirror-image defect.

### Diagnostic, not a gate — deliberately

Wired under the existing `--payload-check` flag: printed, never written to the
witness, cannot change the exit code. `Q0_FLIP` remains the only gate. Making
this fatal would fail CI on 9 witnesses including 3 nobody has triaged, which is
the same trap `payload_mislabels` documents for its own 22. Same
visible-not-fatal criterion applied throughout `qou-i5jy`.

**This is the fix that would have caught me**, and it is now in the tree rather
than in a recommendation.

---

## The 3 pre-existing envelope-vs-payload mismatches, diagnosed

The new `envelope_vs_payload` check found 3 beyond my own 6. Each is a different
defect, not three of one kind.

### 1. `computations/probes/casimir-macdonald-probe.witness.json` — the clean twin of mine

```
q0Anchor "muon"   q0Value 1.109978595557334719899763   (muon-A)
parameters.substrate_q = 1.1099785827513808              (PROTON)
```

Same shape as the six I introduced: envelope self-consistent, the one q₀ the
probe actually used is the proton pin. Producer `casimir_macdonald_probe.py`.
Nothing else in the payload is muon.

### 2. `computations/derivation-chain-audit.witness.json` — an audit, and narrower

```
q0Anchor "muon"   q0Value muon-A
data.chain_results[36].target_value   = 1.1099785827513808   (PROTON)
data.chain_results[36].computed_value = 1.1099785827513808   (PROTON)
```

Only **one** chain step out of many carries q₀-shaped values, and both its legs
are proton while the envelope says muon. Producer `derivation_chain_validator.py`.
Milder than (1): the witness is an audit report over many steps, and the envelope
is describing the validator's own anchor rather than each step's. Worth a label,
probably not a regeneration.

### 3. `computations/h4-form-AB-cross-anchor-stability.witness.json` — THREE defects at once

```
q0Anchor "proton"   q0Value 1.109978582751380807591669   (PROTON — envelope correct)
parameters.q_proton = 1.109978595557334719899763          (muon-A)   ← mislabelled
data.q_muon         = 1.109978595554180575281594          (muon-B)
```

- The **envelope is right** and the payload contains **no proton value at all** —
  which is why it trips in the opposite direction from every other hit.
- `parameters.q_proton` holds **muon-A**: the payload mislabel this bean has been
  tracking all along.
- Its two "cross-anchor" legs are **muon-A vs muon-B** — a 3.15e-12 muon-to-muon
  gap presented as the 11.5 ppb muon-to-proton one. **The fourth independent
  instance of the degenerate-comparison pattern**, after the qbeta batch and
  `habiro_interpolation_wlambda`.

This is the file this bean excluded from regeneration because its header says
*"This probe is preserved as-is by design"*. That exclusion still stands — but it
should now be recorded as preserving an artefact whose stability result rests on
comparing an anchor with itself, not as preserving a clean historical datum. Its
`ANCHOR NOTE` was already flagged here for calling the muon value "the CURRENT
canonical proton q0"; the payload matches that note rather than the file's own
docstring, so the note is not merely stale prose — the numbers followed it.

### Disposition

| witness | class | action |
|---|---|---|
| `casimir-macdonald-probe` | same as my 6 | regenerate or re-stamp with the 11 producers |
| `derivation-chain-audit` | audit-level label | label; likely no regeneration |
| `h4-form-AB-cross-anchor-stability` | **preserved artefact, degenerate comparison** | leave; annotate that its stability claim is muon-vs-muon |

None of the three is mine, and none was visible to any check before today.
