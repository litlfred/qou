---
# qou-fd0e
title: q0_value_drift_audit defines CANONICAL as the muon pin — a BLOCKING CI gate that cannot see 211 stale witnesses, plus a 13-file inverted ANCHOR NOTE
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T07:56:50Z
updated_at: 2026-09-13T13:47:58Z
---


Systematic sweep for the polarity inversion fixed in `qou-ivhc`: scripts that
still treat the pre-ruling **muon** pin as canonical after the 2026-05-28
supersession and the 2026-08-15 owner ruling made the **proton** pin canonical.

## 1. VERIFIED — `computations/q0_value_drift_audit.py:68`, a BLOCKING gate whose zero point is the muon pin

```python
# Documented anchors. Canonical is the CAL-2 muon pin carried by
# q-pinning-50-digit.witness.json; the proton pin is the physical-
# observations layer (AGENTS.md §q₀ anchor convention).
Q_CANONICAL = mpf("1.10997859555733471989976322048322502665620840878015368660798114614493")
```

All drift is reported as `ppb_vs_canonical` against that. `classify()` returns
**`"canonical"`** for the muon value and demotes the actual canonical pin to a
secondary **`"proton-pin"`** class (`:88-89`).

Its own committed witness:

| class | count |
|---|---|
| `proton-pin` | 1232 |
| `STALE` | 305 |
| **`canonical`** (= muon) | **211** |
| `unknown` | 25 |

**Those 211 muon-carrying witnesses are classed `canonical` and are structurally
unreachable by the `STALE` bucket** — and post-ruling they are exactly the stale
ones. The gate is blind in the single direction the ruling made important.

Wired **blocking** in two places, verified:

```
scripts/precision-gates.sh:76   "q0-value drift ratchet|computations/q0_value_drift_audit.py|--strict|no|yes"
.github/workflows/witness-staleness.yml:320   python3 computations/q0_value_drift_audit.py --strict
```

Unlike `qou-ivhc` this will **not** break the build — the proton pin is explicitly
tolerated as its own class rather than flagged. The defect is the blind spot, not
a false failure, which is why nothing has surfaced it.

## 2. A 13-file replicated `ANCHOR NOTE (2026-06-22)` that inverts both halves

```
# ANCHOR NOTE (2026-06-22): q0 = 1.10997858275… occurrences below are the
# RETIRED pre-2026-05-28 proton anchor (old re-pin #1422) … The CURRENT
# canonical proton q0 is q_at() ≈ 1.1099785955573347…; the muon anchor is
# q_muon_at() ≈ 1.10997859555418…. This probe is preserved as-is by design.
```

It calls the **proton pin "RETIRED"** and the **muon pin "The CURRENT canonical
proton q0"**. Its factual claim is false today: none of the 13 stems are in
`computations/q0_anchor_manifest.json`'s `ideal_muon` (which now holds only three
entries after `_migration_2026_08_19` moved 255 producers out), so `q_at()`
returns `1.10997858275…` for every one of them.

`h4_form_AB_cross_anchor_stability.py` I found independently while working
`qou-cds3` — its code is correct (`:98` `q_proton = q_at(DPS)`) and its docstring
`:17` is correct, so the note contradicts its own file twelve lines down. The
other twelve carry the identical header: `mass_theory_formalize_first_invariants_probe.py`,
`probes/mn_dpn_xq_cross_anchor_probe.py`, `probes/he4_partition_dominance_audit_probe.py`,
`c_3_categorical_derivation_attempt.py`, `qbeta/qbeta_qbessel_crossanchor_smoothness_refutation.py`,
`qbeta/qbeta_c3_complex_habiro_cross_anchor_probe.py`, `qbeta/qbeta_c3_hopf_habiro_profile_probe.py`,
`qbeta/qbeta_c3_complex_singularity_probe.py`, `qbeta/qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py`,
`qbeta/qbeta_hoefsmit_chi_cross_anchor_stability_probe.py`, `qbeta/qbeta_symbolic_tbeta_ck4_8_probe.py`,
`qbeta/qbeta_a1_carrier_reconciliation.py`.

**"This probe is preserved as-is by design" actively instructs future auditors not
to touch it** — which is why a wrong header replicated 13× has survived a ruling.

## 3. Secondary (reported, not individually re-verified)

- **Four producers assert the muon prefix inside a function named
  `load_canonical_q`**: `cross_check_trM_cw_seminormal_leg.py:68`,
  `deltalambda/he4_binding_k_stage2_probe.py:103`,
  `deltalambda/he4_stage2_ranking_seminormal_xcheck.py:56`,
  `deltalambda/he4_binding_k_presentation_correction_probe.py:100`. Each bypasses
  `q_parameter` to read the pinning witness directly. The assert is internally
  consistent; the inversion is the word *canonical*. Only the last states a reason.
- **`tools/pyhecke/tests/test_native.py`** — four tests hardcode `q =
  1.1099785955541805` (muon) and compare against `pyhecke.gram` references built
  at the proton pin, tolerance `1e-14`, while `z(muon) − z(proton) = 1.34e-8`,
  six orders past tolerance. Masked today by `skipif(not bridge.has_native())`.
  Its sibling `test_gram_values.py` was repaired to the proton pin on 2026-08-09
  with a note calling muon "the wrong pin"; this file never got the same pass.
- **Three muon literals annotated as the proton pin**:
  `probes/he_nu_sdp_psd_count_test.py:56`, `substrate/unified_tau_odd_partner_solve.py:53`,
  `option_e_probe1_derive_1plusq_over_2.py:70`.

## Sweep coverage

All 19 `startswith` sites on either prefix; all 19 assert/raise/exit lines
containing a pin literal; all 40 `--strict` scripts touching q0; both CI workflow
gate invocations; all 3 shell gates; every Rust pin constant. A ±4-line context
scan surfaced 173 candidate files (109 muon-only, 45 both-pins, 19 proton-only),
all triaged, ~38 opened in detail. The ~100 muon-only files cleared are plain
stale-pin migration scope (`qou-1c4y`), not inversions.

Correct-polarity sites confirmed and explicitly **not** to be re-flagged:
`substrate/q_parameter.py:113` (the `"not canonical muon"` raise sits inside the
opt-in muon branch), `audits/q0_anchor_consistency_audit.py:97`,
`substrate/witness_constant_staleness.py:70`, `atomic_tr_m_mpfr_50dps.py:110,124`,
`audits/q0_hardcoded_pin_audit.py:64`, `audits/undeclared_muon_pin_flip_risk_audit.py`
(its "canonical muon pin" means canonical *within* the muon family),
`tools/hecke-engine/src/provenance.rs:74`.

## Priority

**#1.** It is a blocking gate, its blind class is 211 witnesses, and the fix is to
re-point `Q_CANONICAL` at the proton pin and re-derive `PROTON_PIN_PPB` — which
**moves what the gate fails on**, so it is a deliberate change, not a hygiene edit.
Not attempted here.

---

## ⚠ CORRECTION 2026-08-23 — "inverted" was the wrong diagnosis, and the real defect is sharper

Challenged on why I recorded this as needing an owner call instead of just fixing
it. Investigating properly shows **both** my framing and my deferral were
under-argued.

### It is NOT polarity-inverted

`q0_value_drift_audit.py` is **two-layer aware by design**. From its own header
table:

| class | meaning (verbatim) |
|---|---|
| `canonical` | matches the CAL-2 muon pin — **the `computations/` layer convention** |
| `proton-pin` | ~11.54 ppb below canonical: the documented physical-observations layer. **Legitimate, not drift.** |

It never flags the proton pin as a defect — it has a named class for it that says
*legitimate*. So this is **not** the `qou-ivhc` failure (a detector calling correct
code a bug). Comparing the two was wrong, and the word `canonical` for a *layer
convention* is what misled me.

### The real defect: the class is calibrated to a layer that no longer exists

`computations/q0_anchor_manifest.json`:

```
ideal_muon      :   3   ['atomic_tr_m_mpfr_50dps', 'cross_check_trM_1ppb', 'q_pinning_50_digit']
physical_proton : 406
_migration_2026_08_19: {'moved': 255, 'kept_ideal_muon': ['q_pinning_50_digit'],
                        'authorisation': 'AGENTS.md q0-anchor-convention rule 4
                                          (owner 2026-08-15, recorded 2026-08-19)'}
```

The owner authorised moving **255 producers** out of the muon layer, leaving
essentially one. The drift audit's `canonical` class still means "the muon layer",
and `canonical` is the one class that can never be `STALE`.

**Measured** against the audit's own committed witness — of the 165 distinct files
carrying the 211 `canonical`-classed fields:

| | count |
|---|---|
| produced by an `ideal_muon` producer (legitimately muon) | **3** |
| produced by something no longer in that layer | **162** |

So 162 witnesses sit in a class defined as "the `computations/` layer convention"
while their producers were moved out of that layer four days ago. That is a real
blind spot — but it is a **stale layer calibration**, not an inverted polarity, and
the distinction changes the fix.

### And the fix is NOT re-pointing `Q_CANONICAL`

That was my own suggested repair and it is wrong: re-pointing the zero would
reclassify all **1232** `proton-pin` entries and destroy the two-layer model the
audit exists to express. The correct fix is to classify **against the producer's
declared layer** — a muon value is legitimate iff its producer is in `ideal_muon`,
stale otherwise. The manifest already exists for exactly this and the audit does
not consult it.

### Why it still needs an owner call — now with the actual reason

Not the vague "it moves what the gate fails on". Specifically:

`--strict` fails on stale values **not already in the baseline**
(`:196 return 1 if (args.strict and new_stale) else 0`). Applying the correct
classification moves ~162 witnesses into `STALE`, none of them in
`q0-drift-baseline.json`, so the gate — wired blocking at
`precision-gates.sh:76` and `witness-staleness.yml:320` — **fails immediately**.

The escape hatch is closed by the audit's own rule: `--rebaseline` is documented
*"use it **only** when draining (the count must go DOWN); it is not a way to
silence a new failure."* Absorbing 162 new stale keys would raise the count, which
that rule forbids.

So the choice is: block CI on 162 pre-existing witnesses, or violate the audit's
stated rebaseline discipline. **Both are owner decisions**, and that is the real
reason to stop here — not the one I gave first.

### Safe partial available

The same pattern used for `--payload-check` on the anchor audit applies: report
the producer-layer mismatch as an opt-in, print-only diagnostic that cannot change
the exit code. That makes the 162 visible and countable without forcing either
horn. Not implemented in this entry; noted as the obvious next step.

---

## `--layer-check` added 2026-08-23 — the blind class is now countable, and my 162 was wrong

Implemented the safe partial: an **opt-in, print-only** producer-layer diagnostic
on `q0_value_drift_audit.py`. It resolves each `canonical`-classed witness to its
`scriptFile` and checks that producer against the manifest's `ideal_muon`.

```
  canonical-classed witness files            : 165
  producer NOT in ideal_muon (blind to STALE): 148
  legitimately muon-layer                    :   3
  UNRESOLVED (not evidence either way)       :  14
```

`148 + 3 + 14 = 165`, and the **3** matches `ideal_muon`'s three entries exactly —
a real self-check, not a coincidence.

Findings are printed, never written to the witness (verified: the artefact is
byte-identical after a `--layer-check` run — this audit writes raw JSON with no
invocation record, unlike the `WitnessBuilder` audits), and the exit code is
untouched: `new_stale` remains the only gate.

### Correcting my own figure: 162 → 148

I reported **162** above. That number lumped **14 unresolved** witnesses in with
the mismatches, because my ad-hoc script counted everything that was not provably
legitimate as a mismatch. The honest split is 148 mismatched, 14 unresolved.

### And I shipped that same defect into the first version of this diagnostic

The first `--layer-check` printed *"legitimately muon-layer: 17"* — computed as
`165 − 148`. But only **3** producers are in `ideal_muon`, so 17 was impossible on
its face. The cause: unresolved witnesses `continue`d out of the loop and were
then counted as legitimate **by subtraction**.

That is exactly the defect this session has been cataloguing — `PROV_AUDIT_EXEMPT`
returning `[]` before checking (`qou-0uqm`), `count_package` returning `-1` and
being read as an improvement (`qou-i5jy`) — reproduced by me, in a tool written to
detect it. The fix is the same one I recommended for those: **three explicit
classes, and never infer a verdict by subtraction.** `UNRESOLVED` is now its own
line, labelled *"not evidence either way"*.

A second latent bug in the same first version: it referenced an undefined `REPO`
on the fallback path. It never fired because the relative paths happened to
resolve against the process cwd, so it would have raised `NameError` only when run
from another directory. Now resolves against `HERE.parent` explicitly.

### The decision this surfaces is unchanged

148 witnesses sit in a class that cannot be `STALE`, and acting on that fails a
blocking gate or breaks the documented `--rebaseline` discipline. Still the
owner's call; the diagnostic makes the number visible without forcing it.

---

## ⚠ UNBLOCKED 2026-08-23 — this bean's premise was an artefact of a lookup bug

Everything below the "real defect" heading rests on one measurement:

```
ideal_muon      :   3   ['atomic_tr_m_mpfr_50dps', 'cross_check_trM_1ppb', 'q_pinning_50_digit']
physical_proton : 406
_migration_2026_08_19: {'moved': 255, ...}
```

**That 3 was a bug, not a migration.** Commit `8b4825920` (2026-08-23 16:58 UTC),
*"fix(q0-manifest): the producer lookup was root-only, so half the corpus was
invisible"*, says it in its own body:

> `_producer_stem` resolved a witness's producer by looking **ONLY** in
> `computations/`. … for every witness under `probes/`, `qbeta/`, `substrate/`
> and the rest it returned None — the witness was **never even read**. …
> **700 LIVE witnesses** had their producer in a subdirectory only … Roughly half
> the corpus.

Current manifest, verified directly and identical on `origin/main`:

| | bean | now |
|---|---|---|
| `ideal_muon` | 3 | **110** |
| `physical_proton` | 406 | **513** |
| `ambiguous` | 1 | **22** |

`_migration_2026_08_19` no longer exists in the manifest at all (grep count 0).
It survives only in this bean and in
`computations/q0_value_drift_audit.py`'s docstring, both of which are now wrong.

This bean was created 07:56 UTC and `--layer-check` added 08:48 UTC; the fix
landed at 16:58 UTC — **after both**. My §"the 3 matches `ideal_muon`'s three
entries exactly — a real self-check, not a coincidence" was a self-check against
the same broken lookup. It agreed because both sides were blind in the same way.

### The blocking dilemma has collapsed

The bean stopped on: *"block CI on 162 pre-existing witnesses, or violate the
audit's stated `--rebaseline` discipline. Both are owner decisions."*

Re-measured against the fixed manifest:

| | bean | now (worktree) | origin/main |
|---|---|---|---|
| canonical-classed witnesses | 165 | **156** | 150 |
| producer NOT in `ideal_muon` | **148** | **66** | 66 |
| legitimately muon-layer | 3 | **76** | 70 |
| UNRESOLVED | 14 | 14 | 14 |

And the 66 split **50 undeclared / 9 `physical_proton` / 7 `ambiguous`**. Fifty of
them are a *declaration* gap — the producer is simply not in the manifest — which
is hygiene needing no ruling and moving nothing into `STALE`. Only ~16 are genuine
layer mismatches, a size an ordinary drain carries.

`q0-drift-baseline.json` holds 329 stale keys against 292 current `STALE`, so
**NEW = 0 and `--strict` exits 0 today.** The CI-failure horn does not exist as
stated.

### Waiting on the CODATA ruling was the wrong dependency

It has **not** landed on `origin/main` (`q_parameter.py` last touched by an
unrelated perf commit; `claude/muon-anchor-codata-2022-2026-08-22` unmerged), and
`q_parameter.py:204` still reads `_MUON_Q_STR = _d["q"]` from the pinning witness
— the self-certification the ruling was meant to remove.

More importantly it is the **wrong axis**: the ruling changes the anchor *value*,
this bean is about layer *membership*. And the derived muon value differs from the
witness pin by **+0.0769 ppb** against a `canonical` tolerance of `1e-6` ppb — so
if it lands it reclassifies **all ~193 currently-canonical fields**, a far larger
event that would sweep these 66 up unresolved rather than settle them.

### Status

**Unblocked.** Not an owner decision any more — the decision it was waiting for was
posed against numbers that no longer exist. Next step is mechanical: re-measure,
replace the 165/148/3/14 block, split the 66 into "declare 50" and "drain ~16",
and correct `q0_value_drift_audit.py:131-148`, whose docstring still tells readers
`ideal_muon` has 3 entries and ~162 witnesses are at stake.

**Not done here** — that is a fresh pass over a bean whose every figure moved, and
it should be done in one piece rather than appended to three layers of superseded
argument.

---

## RE-MEASURED 2026-08-23 — figures reproduced independently, docstring corrected

Every number below was derived here by importing `q0_value_drift_audit` and
calling `scan()` / `layer_mismatches()` directly. **The script was not run**: its
`main()` writes `q0-value-drift-audit.witness.json` unconditionally at `:248`,
before the `--layer-check` branch, so running it to read a diagnostic would have
rewritten a committed artefact.

```
class counts        canonical 193   proton-pin 1309   STALE 292   unknown 25   (1819 fields)

canonical-classed witness files            : 156
producer NOT in ideal_muon (blind to STALE):  66
legitimately muon-layer                    :  76
UNRESOLVED (not evidence either way)       :  14
                                       sum = 156
```

### The 66, split — and this is what dissolves the blocker

| | n | what it is |
|---|---|---|
| **UNDECLARED** in the manifest | **50** (49 distinct stems) | a *declaration* gap — the producer is in no list at all |
| `physical_proton` | 9 | genuine layer mismatch |
| `ambiguous` | 7 | genuine, but the layer is undecided by design |

All 14 UNRESOLVED share one reason: **`no scriptFile`**.

Fifty of the 66 need a manifest entry, not a ruling — declaring a producer moves
nothing into `STALE` and changes no value. The residue needing judgement is
**16**, which an ordinary drain carries.

### The CI horn, checked rather than assumed

```
stale total : 292      baseline : 329      NEW : 0      --strict exit : 0
```

The bean claimed acting here "fails a blocking gate immediately". It does not:
nothing is currently unbaselined. **I got this wrong twice before getting it
right** — first by comparing against the baseline file's top-level keys
(`note`, `count`, `stale_keys`) instead of the `stale_keys` list, which reported
292 NEW and a failing gate. `main()` uses
`key = lambda r: f"{r['file']}::{r['field']}"` against `["stale_keys"]`; matching
that exactly gives 0. Recorded because the wrong reading reproduced the bean's own
alarming figure, which is precisely how a bad number survives.

### Docstring corrected

`computations/q0_value_drift_audit.py:131-148` told every future reader that
`_migration_2026_08_19` moved 255 producers "on owner authorisation, leaving 3",
and that acting would move ~162 witnesses into `STALE` and fail a blocking gate.
Both were artefacts of the root-only lookup. Replaced with the measured figures
and an explicit note of what was wrong, so the correction is legible rather than
silent. **No behaviour change** — the edit is docstring-only, and the function's
three-class return is untouched.

### Still open, and now small

1. Declare the 49 undeclared producer stems in `q0_anchor_manifest.json` — needs
   a decision on *which* layer each belongs to, per producer. Not mechanical, but
   not a gate-blocking ruling either.
2. Drain the 16 real mismatches (9 `physical_proton`, 7 `ambiguous`).
3. The 14 `no scriptFile` witnesses overlap `qou-0uqm`'s 286-witness class and
   should be handled there, not here.

---

## 2026-08-24 — per-producer triage of the undeclared stems, and two reasons not to bulk-declare

### The figures moved again — treat any number here as perishable

| | bean | earlier today | **now** |
|---|---|---|---|
| canonical-classed files | 165 | 156 | **159** |
| mismatch | 148 | 66 | **55** (54 stems) |
| legit | 3 | 76 | **91** |
| unresolved | 14 | 14 | **13** |
| `ideal_muon` / `physical_proton` / `ambiguous` | 3 / 406 / 1 | 110 / 513 / 22 | **124 / 514 / 16** |

Siblings are editing the manifest continuously (`qou-bdkx`; `8529ca4f1`,
`f0ef49648`, `d3959fe96`, `b2cbd495d`). **A fixed count in this bean decays within
hours** — which is itself the lesson from the `ideal_muon == 3` artefact.

### A FOURTH route, which the mechanism note missed

Beyond `q_parameter` (governed) and `qou_substrate.constants` (never governed),
**10 of the 43 undeclared producers read
`computations/q-pinning-50-digit.witness.json` directly** — the muon
anchor-defining file. They are muon unconditionally; the manifest cannot change
their compute. Plus ~24 that hardcode a muon literal or inherit one from a sibling
witness.

**So only ~11 of the 43 are genuinely manifest-governed.** For the other ~32,
declaring them `ideal_muon` changes nothing about what they compute — it only
makes their `q0Anchor` **stamp** truthful (`resolve_q0_anchor`,
`tools/qou-substrate/python/qou_substrate/witness.py:283-325`, whose undeclared
default is `proton` while their values are all muon). That is still worth doing,
but it is a *stamp* fix, not a layer fix, and the bean should say so.

Every one of the 44 witnesses carries **muon-prefix values only**; not one holds a
proton value.

### DO NOT bulk-declare — `markov_peel_atomic_witness` breaks if you do

Verified in source (`computations/markov/markov_peel_atomic_witness.py:153-164`):

> Load the bridge at THIS producer's own q0 layer … **This producer is NOT in
> `q0_anchor_manifest.json`, so `Q_50_DIGIT_STR` resolves to the experimental
> (proton) pin** — while the default bridge witness is the `ideal_muon` one.
> Comparing across that boundary is the straddle AGENTS.md forbids, and it was not
> subtle: `abs_diff_vs_bridge` for the deuteron read **6.73e-04**, which is also
> what kept rejecting this witness in the regeneration wave.

Its absence from the manifest is **load-bearing and documented, with a measured
consequence**. Adding it to `ideal_muon` is a regression, not a fix. Any
bulk-declaration pass over the 43 must exclude it.

### `zhabiro_phiq_production_crosscheck` — a PRE-EXISTING instance of the regression I introduced

```
source :  Q0 = mp.mpf(str(q_at()))          (:68)
          Q0_SRC = "qou_substrate.constants.q_at (proton pin)"   (:69)
witness:  q0Anchor "muon"   q0Value 1.109978595557334719899763   (value A)
```

Computes proton, declares muon. That is **exactly** the defect `qou-cds3` records
me introducing into six witnesses today — and it was already in the corpus before
I touched anything. So the stamp/compute split is **systemic**, not something my
regeneration invented; my six added to an existing population. Re-running this
producer would flip its `q0Value` to the proton pin and expose the contradiction.

### Seven cases that must not be forced

1. `zhabiro_phiq_production_crosscheck` — computes proton, records muon (above).
2. `markov_peel_atomic_witness` — absence is load-bearing (above).
3. `rho_k_h3a_residual_decomposition` — self-documented **proton** compute over a
   **muon**-stamped `tr_M` input, with a muon stamp. A declared straddle.
4. `chirality_topology_binding_probe` — declares `q0Anchor: "independent"` (which
   means q0 is never read) while emitting a `q0` field from a muon literal.
5. `he_nu_sdp_psd_count_test` — source comment claims proton, the literal is the
   muon value. The comment is false; the literal is the evidence.
6. `saddle_offset_zero_location_probe` — its muon literal diverges from canonical
   past ~48 digits (`…878015405145269` vs `…878015368660798114614493`). Harmless
   at the precision it emits, wrong if precision rises.
7. `ame_2020_binding_energies` — never reads q0 at all; its only q0-shaped value is
   the auto-stamp. No manifest bucket is honest here; `q0Anchor: "independent"` is
   the correct vocabulary.

### Revised recommendation for this bean

The earlier "declare 50, drain 16" framing was too clean. Actual shape:

- **~32 stamp-only declarations** — safe, mechanical, no compute changes.
- **~11 genuinely governed** — the real layer decisions.
- **7 contradictions** — each needs reading, not a bucket.
- **1 must stay undeclared** (`markov_peel_atomic_witness`).
- **13 unresolved** (`no scriptFile`) — belong to `qou-0uqm`'s class, not here.


## 2026-08-24 — APPLIED: 32 stamp-only declarations, owner-approved

The triage above was against a 43-stem set that main has since moved out from
under, so the set was **re-derived mechanically** rather than reused. Method:
`q0_value_drift_audit.scan()` -> 288 canonical-classed q0 fields ->
`layer_mismatches()` -> 68 rows, 67 distinct stems -> each stem resolved to
exactly one file and AST-parsed for its q0 import route.

| route | n | declaring it changes… |
|---|---|---|
| hardcoded muon literal | 20 | the stamp only |
| reads `q-pinning-50-digit.witness.json` directly | 17 | the stamp only |
| `qou_substrate.constants` | 2 | the stamp only (never governed) |
| **imports `q_parameter`** | **9** | **what it COMPUTES — not stamp-only** |
| no q0 route found | 19 | unknown — not declared on a guess |

Precedence is deliberately conservative: **any** `q_parameter` import classes the
stem as governed, even when it also reads the pin witness directly. The safe set
under-claims rather than over-claims.

Selected 35; **3 were already declared in another layer and left alone** —
moving a stem between layers is a different decision from declaring an undeclared
one (`lever1_binding_core_characterization`, `murakami_deformed_vc_q0` in
`ambiguous`; `qbeta_c3_complex_habiro_cross_anchor_probe` in `physical_proton`).
**32 added.** That is exactly the "~32 stamp-only" this bean predicted.

    producer NOT in ideal_muon   68 -> 36
    legitimately muon-layer     101 -> 133
    ideal_muon                  120 -> 152
    NEW stale 0, --strict exits 0

### Two exclusions were re-caught independently, by route rather than by list

- `zhabiro_phiq_production_crosscheck` — the route classifier flagged it as
  `constants(ungoverned)` calling `q_at` (proton) while its witness records the
  muon value. This bean had already named it by hand; the mechanical pass found
  it without being told.
- `qbeta_c3_habiro_3rung_crossanchor_rigidity_probe` — calls **both** `q_at` and
  `q_muon_at`, so it is a cross-anchor comparison with no single anchor to
  declare. Same producer whose witness `origin/main` is now stamping `muon` (see
  the merge note in `qou-cds3`). Two independent lines of evidence reached it.

`markov_peel_atomic_witness` stays undeclared — absence is load-bearing, measured
6.73e-04 consequence.

### Still open in this bean

- **9 genuinely governed stems** — each is a real layer decision, not a stamp fix.
- **19 with no q0 route found** — need reading; several are the `gap_a4_T*` family.
- **7 contradictions** — unchanged, each needs reading rather than a bucket.
- **15 UNRESOLVED** (no `scriptFile`) — `qou-0uqm`'s class, not this one's.


## 2026-08-24 — the "no q0 route found" residue: a FIFTH route, and a 17-producer mislabel

Chasing the 19 stems my route triage could not classify. Eight of them are the
`gap_a4_T*` family, and they share a cause.

### A fifth q0 route the mechanism note does not list

Beyond `q_parameter` (governed), `qou_substrate.constants` (never governed),
direct reads of `q-pinning-50-digit.witness.json`, and hardcoded literals, there
is a **shared local constants module**:

    computations/probes/_gap_a4_qsafe.py  ->  Q_0_50DPS

`from _gap_a4_qsafe import Q_0_50DPS`. My triage classified these stems
"none-found" because it looked for the four known routes and a bare literal in
the producer's own source. The pin is one import away. **Same shape as the
sibling's `qou-cq2n`: a value supplied by a shared helper is invisible to a
detector that inspects the caller.**

### The constant was labelled PROTON and holds the MUON pin

    # Substrate parameter (proton-mass-anchored q_0, 50 dps).
    Q_0_50DPS: str = "1.1099785955573347198997632204832250266562084087802"

Measured at `mp.dps = 60`:

    vs the canonical muon pin A : 4.5e-24 ppb   (identical)
    vs the proton pin           : 11.5371 ppb   (exactly the mu-p tension)

The label was false. **17 producers import it**, resolved by AST rather than
`grep -rl`: `gap_a4_T4` through `T18` (incl. `T4_..._perknot_rerun`) and
`borromean_trace_cross_validator`.

This is the second instance of this exact shape in this bean —
`he_nu_sdp_psd_count_test` is already recorded as *"source comment claims proton,
the literal is the muon value"*. One instance is a typo; two, one of them
reaching 17 producers through a module written specifically to de-duplicate, is
a class.

### FIXED: the label. NOT touched: the value.

The comment now states the measured fact and names the open question. The
literal is unchanged. **Whether the muon anchor is what this probe series
INTENDS is not something I can settle** — answering it moves all 17 producers by
11.5 ppb. Evidence that the value is intended: the module calls the decimal
authoritative (*"T4-T8 use this exact 50-dps decimal; T9-T12 extend it without
re-deriving"*), and every one of these witnesses classifies `canonical` (muon) in
the drift audit. Evidence for proton: the comment alone. Owner's call.

### A FOURTH anchor-checking seam, uncovered

Ran all four q0 pin audits — `q0_hardcoded_pin_audit`,
`undeclared_muon_pin_flip_risk_audit`, `hardcoded_q0_literal_families_audit`,
`hardcoded_literal_audit`. **None flags `_gap_a4_qsafe.py`.** Not a scope gap:
`_SCAN_ROOT` covers it. They ratchet on literals that **DIVERGE** from the
canonical pin, and this one **matches it exactly**.

The three seams already known are `Q0_OK`/`Q0_FLIP` (envelope vs envelope),
`payload_mislabels` (field name vs field value), and `envelope_vs_payload`
(envelope vs payload). This is a fourth, and nothing covers it:

  **a literal's LABEL in source versus that literal's VALUE.**

A hardcoded pin that matches canonical perfectly is exactly the case every
existing detector is built to pass over.


## 2026-08-24 — DETECTOR BUILT for the fourth seam: 10 mislabels, both directions

`computations/audits/q0_literal_label_vs_value_audit.py`. Report-only, `--strict`
exits 1. It reads **source**, which is why nothing else could see this: the three
existing seams all read witnesses.

Method: AST-parse every `*.py` outside `_deprecated/`, take each q0-shaped
string/float constant, classify its VALUE by **mpmath distance** to the two pins
(not by prefix, so a 17-digit truncation classifies the same as a 50-digit one),
then read the LABEL from the binding name, the inline comment, and the comment
block immediately above. A context naming BOTH layers is `ambiguous`, not a
defect — a cross-anchor comparison legitimately mentions both, and calling that a
finding is how a detector earns its false positives.

    files containing '1.109'      626      unparseable    0
    q0-shaped literals           667
      label agrees with value    217
      label CONTRADICTS value     10   <- the finding
      no label in context        354   <- UNEXAMINED, not clean
      off-pin (neither layer)     82   <- the other audits' population

**8 labelled proton holding muon; 2 labelled muon holding proton.** The reverse
direction matters — it means this is not a single stale convention but genuine
label drift in both directions.

| file:line | says | holds | ppb from its claim |
|---|---|---|---|
| `deltalambda/a3_magnitude_parity_orthogonal_probe.py:87` | muon | **proton** | −11.5371 |
| `probes/aoperator_a5_crosscheck.py:399` | muon | **proton** | −12.2141 |
| `habiro_interpolation_wlambda.py:372` | proton | **muon** | 11.5343 |
| `probes/brane_tower_full_channel_trace_audit.py:62` | proton | **muon** | 11.5343 |
| `probes/he_nu_sdp_psd_count_test.py:57` | proton | **muon** | 11.5371 |
| `probes/qbeta_habiro_cyclotomic_probe.py:270` | proton | **muon** | 11.5371 |
| `sigma_all_evaluator.py:493` | proton | **muon** | 11.5343 |
| `substrate/unified_tau_odd_partner_solve.py:54` | proton | **muon** | 11.5371 |
| `substrate/z2bn_tau_gauss_manin_sage_probe.py:88` | proton | **muon** | 11.5371 |
| `docs/audits/scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py:39` | proton | **muon** | 11.5343 |

### Validation

- It reproduces `he_nu_sdp_psd_count_test.py:57`, which this bean had already
  found **by hand** — the detector was not tuned to it.
- Two more hand-checked, both correct:
  `unified_tau_odd_partner_solve.py:53` reads *"Canonical substrate q_0
  (proton-pinned, 50 dps)"* over pin A; `a3_magnitude_parity_orthogonal_probe.py:86`
  reads *"at the muon-canonical q₀"* over the proton pin.
- `_gap_a4_qsafe.py` correctly does **not** appear — its label was corrected
  earlier today, so the detector responds to the fix rather than to a hardcoded
  exclusion.

### The mislabel propagated by copy-paste

`unified_tau_odd_partner_solve.py:54` holds the **identical 50-digit string** as
`_gap_a4_qsafe.py` under nearly identical wording — *"(proton-pinned, 50 dps)"*
vs *"(proton-mass-anchored q_0, 50 dps)"*. Same lineage. That is why the class
exists at all, and why fixing one instance does not drain it.

### Not fixed, deliberately

**No literal and no label was changed by this pass.** Whether a mislabelled
constant needs its label corrected or its value corrected is a question about
INTENT, and getting it backwards moves every downstream consumer by 11.5 ppb.
Ten judgement calls, each needing the producer read. The detector makes them
visible and countable; it does not rule on them.

The 354 unlabelled literals are reported as **unexamined, not clean** — that
substitution is the defect `qou-i5jy` exists for.


## 2026-08-29 — label-vs-value drained to zero, after removing two false positives of my own

### First: the detector was over-reporting, 2 of 8

Reading all eight by hand before touching any of them found **two that were not
defects at all**:

- `probes/aoperator_a5_crosscheck.py` holds
  `_PINS = {"muon": "1.109978595", "proton": "1.109978582"}` — a classification
  **lookup table** where both pins appear and both mappings are correct. My
  label-from-nearby-comment read the wrong key off it. Reporting this one meant
  flagging a file's own anchor-consistency machinery as the defect it exists to
  prevent — the surrounding comment even says a hardcoded anchor *"would
  silently become a lie if the classification ever changed"*.
- `sigma_all_evaluator.py` pins its selftest at muon while emitting its witness
  at proton, and says so: *"Pinning both sides here makes the test survive every
  future re-pin … **the two anchors are deliberate**."* My `ambiguous` rule only
  fired when a context named BOTH anchors; this one names only "proton", so a
  documented design was reported as a contradiction.

Two rules added: literals inside a dict **keyed by anchor name** are a table, not
a labelled value (44 literals now correctly excluded, 628 → 584 scanned); and a
context declaring a deliberate two-anchor arrangement is `ambiguous` even when it
names one anchor. **8 → 6**, and the six are the ones verified by hand.

### Then: all six labels corrected

| file:line | said | holds |
|---|---|---|
| `deltalambda/a3_magnitude_parity_orthogonal_probe.py:87` | "muon-canonical" | **proton** |
| `probes/he_nu_sdp_psd_count_test.py:57` | "proton-pinned" | **muon** A |
| `probes/qbeta_habiro_cyclotomic_probe.py:270` | "at proton q₀" | **muon** A |
| `substrate/unified_tau_odd_partner_solve.py:54` | "proton-pinned" | **muon** A |
| `substrate/z2bn_tau_gauss_manin_sage_probe.py:88` | "proton-pinned" | **muon** A |
| `docs/audits/scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py:39` | "proton-anchored re-pin" | **muon** B |

Each comment now states the measured fact, the ppb distance from what it had
claimed, and that **whether that layer is INTENDED remains open** — the label is
corrected, the intent is not ruled on.

**No value was changed, and that is checked rather than asserted**: every q0
literal in all six files is byte-identical to `HEAD`, compared as extracted sets.
Two assignments moved to their own line so an inline comment could become a
block; the literals themselves are untouched.

    label CONTRADICTS value   6 -> 0
    label agrees with value   205 -> 211

### Recorded, not fixed

Two of the six (`he_nu_sdp_psd_count_test`,
`keystone_wrt_schurweyl_plancherel_4count_probe`) hold their q0 as a **float64
literal**, which the corpus's no-float64 directive forbids. Changing that changes
the compute, so each carries a note instead. Separate work.

`unified_tau_odd_partner_solve.py:54` holds the **identical 50-digit string**
that `_gap_a4_qsafe.py` carried under near-identical wording, which is the
copy-paste lineage already recorded here. Main has since fixed `_gap_a4_qsafe`
structurally by resolving through `q_parameter`; this one is still a literal.


## 2026-08-30 — the 277 "unexamined" literals are now EXAMINED, and they are clean

The label-vs-value audit reported 277 q0 literals with no anchor label in
context, counted as *"UNEXAMINED, not clean"*. That is the honest way to report
them, but it is not an answer. A literal with no comment is not thereby wrong —
so the question is whether anything in that bucket contradicts something
checkable. It does have a check available: the producer's own **manifest
declaration**.

New mode: `--cross-manifest`.

    204  producer undeclared (nothing to contradict)
     58  fallback / sentinel (another audit's population)
     11  agrees with declaration (proton)
      2  declared ambiguous
      2  CONTRADICTS its manifest declaration

**Both survivors are already known** — `lever1_trB_geometric_target` and
`lever1_trB_quantum_integer_form`, two of the durable seven in `qou-cds3`. So
the largest unexamined pocket in this audit contains **zero new defects**. That
is a negative result and it is worth having: it was the biggest thing either
audit could not speak to.

### It reported 14 before I looked at any of them

The first cut of this cross-check found **14** contradictions. Hand-checking two
killed it, and the two failed for *different* reasons — which is why one spot
check would not have been enough:

- `atomic_tr_m_mpfr_50dps.py:124` — the literal sits in
  `if not q.startswith("1.10997858275"): raise SystemExit(...)`. It is a
  **prefix being compared against**, not a value in use. That script checks that
  `q_parameter` resolved to the pin it asked for; reporting it would flag a
  correctness check as the defect it exists to catch.
- `alpha_k_four_strand_singlet_selection.py:82` — the literal is in an
  **`except` fallback**: `try: Q0 = q_at()` / `except: Q0 = "<muon>"`. The
  operative q0 is the resolved one. Cross-layer fallbacks already have a
  detector — `q0_cross_layer_fallback_scan`, which names
  `rt_c23_singlet_sign_core` and `rt_identity_chain_consolidation` in its own
  output, two of my "findings". Reporting them here would have inflated this
  audit with another audit's population and called it new.

Excluding both shapes by AST: **14 → 2**. The exclusion is a printed bucket (58),
not a silent drop.

Third time this session that a first cut of a detector of mine over-reported,
and the same shape each time: **the literal was in the file, but it was not the
thing the file computes with.**


## 2026-08-30 — PINNING CONVENTION CONFORMANCE, measured

Established what the current convention actually IS before checking anything
against it:

    proton layer  q_parameter.Q_MP / Q_50_DIGIT_STR  ->  1.10997858275138080759...
    muon layer    q-pinning-50-digit.witness.json
                  derived_50_digit.q                 ->  1.10997859564273904668...
                  and that witness stamps itself `q0Anchor: muon`

So **the muon pin is C**. `deltalambda/he4_binding_k_presentation_correction_probe.py:95`
encodes the conformant idiom and asserts it:

    q = d["derived_50_digit"]["q"]
    assert q.startswith("1.109978595642"), q

Note its docstring's warning, which matters for anyone copying it: *"q_parameter
is anchor-adaptive and would resolve PROTON in this non-manifest process"* — so
`q_parameter` is NOT a muon source for an undeclared producer.

### The corpus is largely NOT conformant

Scanned every `*.py` outside `_deprecated/`, AST-parsed, comment-only literals
excluded, classified by distance to each vintage:

    283 literals in 238 files   A (muon, SUPERSEDED)
    214 literals in 183 files   proton (CURRENT)
     43 literals in  36 files   off-pin / other
     11 literals in  11 files   C (muon, CURRENT)

**A outnumbers C by 26 to 1.** Anything hardcoding A is not "the muon pin" any
more; it is last week's muon pin.

**NOT bulk-edited, deliberately.** That population is `qou-0hnz`'s and main is
actively draining it — `2caa0ad00 migrate(qou-1c4y): 12 frozen muon literals
resolved at the source` landed on 2026-08-29. Editing 238 files here would
collide with an in-flight campaign and move values across the corpus. Recorded
as a measurement for whoever owns it.

### Fixed the one I own

`probes/rho_binding_constancy_probe.py` was mine, from earlier this session, and
it was non-conformant in a way I had explicitly deferred — I fixed its float64
and left the vintage, writing "re-pinning is a convention decision". Under the
current convention that deferral was the wrong call: a hardcoded A is stale by
construction.

Re-fixed by **resolving rather than re-hardcoding at a newer vintage**, which is
the only version that does not go stale again:

    q0 before  1.109978595557334719899763   (A)
    q0 after   1.109978595642739046681795   (C, read from the pinning witness)
    raw float64 fields  0        verdicts  identical

The general rule this settles, and the reason it is worth a bean entry: **the
conformant fix for a pin literal is not "update it to the current value", it is
"stop having a literal".** Updating A to C would have been non-conformant again
at the next re-pin.


## 2026-08-30 — pulled main's migration in; it does NOT drain the A-literals

Merged `origin/main` (225 commits) to bring the in-flight migration onto this
branch — `qou-aj91` and `qou-1c4y` are actively migrating producers. One
conflict, `alpha-5-lp-dual-crystal.witness.json`: mine was the mpf-kernel
regeneration at muon/C, main's was `aea2728dc migrate(qou-aj91):
alpha_5_lp_dual_crystal to proton`. Took main's — it carries the migration.

**The A-literal population did not go down. It went UP.**

    before merge   283 literals in 238 files
    after merge    285 literals in 239 files

Those migrations move a producer's ANCHOR — declaring it, or repointing it at
`q_parameter` — which is a different axis from a hardcoded literal in the
source. Pulling the migration in was correct and it does not, by itself, address
this population.

### And a blanket migration would be WRONG, which the count hides

Split the 285 by whether migrating them is even the right action:

    215 literals in 189 files   PRODUCER consuming a hardcoded A   <- the target
     39 literals in  31 files   fallback / sentinel / comparison
     17 literals in  17 files   docs/audits scripts
     13 literals in   5 files   TEST fixture (asserts the pin)
      1 literal  in   1 file    the substrate package (DEFINES the pin)

`tools/qou-substrate/python/qou_substrate/constants.py` and
`tools/qou-substrate/tests/test_q0_anchor.py` are the first hits by file order,
and they are exactly the files that MUST keep an A literal — one defines the
pin, the others assert it. A 239-file sweep would rewrite the definition and
then rewrite the tests that guard it, and the tests would still pass.

**The real scope is 189 producers, not 239 files.** Every one is a value-moving
change needing a witness regeneration, which is why `qou-aj91` is doing them one
at a time with a regen per producer rather than in a sweep. That is the correct
shape for the work; the contribution here is the denominator and the exclusions.


## 2026-08-30 — the 189-producer migration: worklist built, agents dispatched, 20 triaged

Built the worklist mechanically: AST-parsed every `*.py` outside `_deprecated/`,
kept literals that FULL-match a q0 decimal (an earlier prefix-only regex crashed
on a string that starts `1.109` and contains non-ASCII), excluded comment-only,
except-fallback and `startswith` sentinel occurrences, and excluded the substrate
package, its tests and `docs/`. **Exactly 189 producers**, matching the earlier
independent count.

### The breakdown changes the design

    169  UNDECLARED in q0_anchor_manifest.json
     14  declared proton
      5  declared ambiguous
      1  declared muon

**169 of 189 have no manifest answer.** So this is not "resolve to what the
manifest says" — for 89% of the population the manifest says nothing, and
choosing wrong moves physics by 11.5 ppb. It is 169 judgements about intent.

Dispatched four READ-ONLY agents over the 169, one per batch, classifying each
into CROSS-ANCHOR / MUON-INTENT / PROTON-INTENT / UNCLEAR with cited evidence and
a confidence. Read-only deliberately: agents sharing this checkout must not run
producers (never two at once) and must not race the git index — a previous agent
already caused one index race here.

### The 20 declared, triaged by hand — and the heuristic already failed twice

Counting cross-anchor markers (`cross.anchor`, `both anchors`, `q_proton`,
`anchors =`):

    HANDS OFF, cross-anchor (markers 5-32):
      c_3_categorical_derivation_attempt (15)
      qbeta_c3_complex_habiro_cross_anchor_probe (32)
      qbeta_c3_complex_singularity_probe (11)
      qbeta_chain4_kashiwara_step3_cross_anchor (29)
      qbeta_chain4_kashiwara_step4_n5 (9)
      qbeta_hoefsmit_chi_cross_anchor_stability_probe (22)
      qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe (21)
      qbeta_qbessel_crossanchor_smoothness_refutation (10)
      qbeta_ck_basis_constrained_pslq (5)
      qbeta_ck_qholonomic_recurrence_test (17)

**Half of the declared set is cross-anchor**, where the A literal is the muon arm
of a deliberate comparison. Migrating any of them destroys one arm.

**The marker count has two known false negatives, both caught by hand:**

- `sigma_all_evaluator` scores **1**, and I verified earlier this session that
  its comment reads *"Pinning both sides here makes the test survive every future
  re-pin … the two anchors are deliberate."* It is cross-anchor.
- `mu_p_pin_sensitivity_map` scores **0**, and it is a **mu-p pin sensitivity
  map** — cross-anchor by construction, from its name alone.

So the marker heuristic is a screen, not a verdict — the same "keyed on how it is
SPELLED, not what it DOES" failure this campaign keeps hitting, this time in my
own triage. **No migration was performed on the strength of it.** The agents were
told to be skeptical for exactly this reason, and their verdicts need the same
treatment when they land.


## 2026-08-30 — agent triage of the 169, and a defect that BLOCKS the migration

Three of four batches returned (127 of 169; batch 3 still running).

    CROSS-ANCHOR (hands off)   57
    MUON-INTENT                27
    PROTON-INTENT               7
    UNCLEAR                    36

**45% is CROSS-ANCHOR.** Nearly half the population holds pin A as the *muon arm
of a deliberate two-anchor comparison* — `Q = {"muon": …, "proton": …}`,
`dq = Q_PROTON - Q_MUON`, per-anchor result tables. Migrating any of them
destroys one side of the experiment. Two files say so in their own headers:
*"its cross-anchor comparison is the point, so it must NOT be migrated."*

**Only 7 are PROTON-INTENT** — the case a naive "A is superseded, move it"
sweep would have assumed for all 189.

### The blocker: the manifest generator cannot see the current muon pin

`computations/gen_q0_anchor_manifest.py:26` classified by

    MUON   = "1.109978595557"     <- pin A
    PROTON = "1.10997858275"

A and C diverge at the **10th** significant figure, so **C does not match**.
Verified directly: `C.startswith("1.109978595557")` is `False`.

The consequence is not cosmetic. A producer correctly migrated to the CURRENT
muon pin matches neither prefix, falls into the generator's *"neither: no q0
field — omit"* branch, drops out of the manifest entirely, and is then defaulted
to **proton** by `resolve_q0_anchor`. **Migrating a producer to the current muon
pin silently re-declared it proton.** The tooling punished conformance, and it
would have silently mis-declared all 27 MUON-INTENT producers the moment they
were migrated.

Fixed: the generator now matches all three muon vintages (A, A', C) and says why
in-line. Verified all three classify muon; C did not before.

**Batch 1 flagged the same A-only blind spot in
`audits/q0_witness_read_dataflow_audit.py:121` and
`q0_cross_layer_fallback_scan.py:47`**, with only `witness_regen_classify.py:155`
and `q0_muon_population_partition.py:49` handling C. Those are not fixed here.

### My worklist has false positives — the agents found five classes

1. **Detector prefixes counted as pins.** `q0_anchor_payload_recovery.py:86`
   `MUON_PREFIX = "1.10997859555"` is a 13-char *pattern*, not a q0. Verified.
2. **A' counted as A.** `1.1099785955541805` is a distinct vintage sitting
   **0.0028 ppb** from A — inside my 0.01 ppb tolerance, so it was absorbed.
3. **Garbled A.** `he4_binding_k_averaged_interface_probe.py:67` is
   `…5573347117485…` where A is `…5573347198997…` — diverges at digit 18.
   Verified by eye against the canonical string.
4. **Dead assignments and unreachable defaults.** `a4_interface_kl_subpath_
   closure.py:27` is never referenced; several `.get("q0", A)` defaults never
   fire because the upstream witness supplies proton.
5. **Comment-only occurrences** in files whose operative pin is something else.

### And one the detector CANNOT see

`qbeta/qbeta_h4_route_a_gate_probe.py:171` carries A as
`sp.Rational(11099785955573347, 10000000000000000)`. A decimal-literal scan is
blind to it, and it is the only *operative* A-vintage value in that file while
both decimal occurrences are dead. There may be more of these.


## 2026-08-30 — ALL FOUR BATCHES IN. 169 triaged, and the migration is mostly NOT one

    CROSS-ANCHOR (hands off)   76   45%
    UNCLEAR                    44   26%
    MUON-INTENT                39   23%
    PROTON-INTENT              10    6%
                              ----
                              169

**Only 10 of 169 are proton-intent** — the verdict a naive "A is superseded,
move it to the current pin" sweep would have applied to all 189. It would have
been wrong 94% of the time.

**76 hold pin A as the muon arm of a deliberate two-anchor comparison** —
`Q = {"muon": …, "proton": …}`, `dq = Q_PROTON - Q_MUON`, per-anchor result
tables, straddle tests. Several say so in their own headers: *"its cross-anchor
comparison is the point, so it must NOT be migrated."* A sweep would have
silently deleted one arm of each experiment and left them still producing
numbers.

### The muon layer is squeezed from BOTH sides by single-vintage blindness

Two tools, each hardcoding a different single muon vintage, in opposite
directions:

    gen_q0_anchor_manifest.py:26   MUON = "1.109978595557"      <- pin A only
    qou_substrate/witness.py:278   ("muon", "1.10997859564")    <- pin C only

Verified both. Consequences:

- a producer at the **current** pin C matched neither prefix in the generator,
  was omitted from the manifest, and defaulted to **proton**. (Fixed here.)
- a producer at pin **A** matches neither prefix in the resolver, so
  `_q0_anchor_from_payload` returns `None` and `resolve_q0_anchor` falls to its
  documented default — **proton**. (NOT fixed: changing the substrate resolver
  restamps witnesses corpus-wide and is not a unilateral call.)

**Therefore: `q0Anchor: "proton"` on an UNDECLARED, A-carrying producer is a
runtime default, not a measurement.** Three of four agents reached this
independently and discarded those stamps as evidence. `witness.py:393` says so
in its own comment. Anyone — including me — who has read such a stamp as intent
was reading the absence of a manifest entry.

The corpus visibly straddles because of it:
`he-nu-sdp-saturation-obstruction.witness.json` carries `q0: "1.1099785955573347"`
(pin A) next to `q0Anchor: "proton"`.

### Evidence coverage is thin, and the agents said so

40 of 42 producers in one batch have **no `q0Anchor`/`q0Value` at all** on their
witness. Verdicts rest on source text and upstream-witness inheritance, not on
recorded anchors. That is a limit of the evidence, not a hedge.

### My worklist's false-positive classes, now complete

1. **Detector prefixes** (13-14 chars) counted as pins — they are pattern
   matchers. Verified.
2. **Vintage conflation**: my 0.01 ppb tolerance absorbed A' (`…5955541805`),
   which is 0.0028 ppb from A. At least 8 files across batches carry B/A', not A.
3. **Garbled A**: `…5573347117485…` vs A's `…5573347198997…`, diverging at
   digit 18. Verified.
4. **Dead assignments** and `.get("q0", A)` defaults that never fire because the
   upstream supplies proton.
5. **Comment-only** occurrences whose operative pin is something else.
6. **Invisible to a decimal scan entirely**:
   `qbeta_h4_route_a_gate_probe.py:171` holds A as
   `sp.Rational(11099785955573347, 10**16)` — the only operative A-value there,
   while both decimal occurrences are dead.

### What the migration actually is

Not 189 edits. It is **10 proton-intent** producers (mechanical), **39
muon-intent** (safe only now that the generator recognises C), **44 unclear**
needing a ruling — two of which say in their own comments that the intent
question is open and cite this bean — and **76 that must not be touched at all**.


## 2026-08-30 — RULING REQUEST written for the 44 UNCLEAR

`docs/coordination/2026-08-30-a-literal-unclear-ruling-request.md`.

The 44 are not one question. They split three ways, and only two of the three
need the owner:

- **~20 have no anchor language at all** — a bare literal feeding real
  arithmetic, no comment, no second pin, no declaring witness. These cluster
  into families (`lever1_*`, `he_nu_sdp_*`, the `mmu_gap_a4_*` scratch scripts,
  the τ-binding probes), and **one answer per family would settle most of the
  group**. That is the ask.
- **2 have the question written into their own source**, both from this
  campaign: `he_nu_sdp_psd_count_test.py:56-59` and
  `substrate/unified_tau_odd_partner_solve.py:53-57` each say *"whether muon is
  INTENDED is open (bean qou-fd0e)"*, having had a false label corrected to
  match their value. They need a yes/no, not analysis.
- **~22 are anchor-immaterial** and need no ruling at all — dead assignments
  (`a4_option_e_color_tube_closure.py:23`, `a4_interface_kl_subpath_closure.py:27`
  assign `Q0_STR` and never read it — deletion, not migration); both sides of a
  comparison sharing the pin so it cancels; a matplotlib tick label; a
  precision-loss test fixture; assertions at 6 significant figures against an
  11.5 ppb gap. Documenting them is the whole fix.

The document states plainly why these cannot be decided mechanically: all 44 are
undeclared, so the manifest is silent; and the `q0Anchor` stamp is worthless
here because `resolve_q0_anchor` defaults undeclared stems to `proton` while
`_Q0_PREFIXES` recognises muon only as pin C — so **every one of the 44 reports
`proton` by construction**, whatever it computes. In one batch, 40 of 42
producers' witnesses carry no `q0Anchor`/`q0Value` at all.

It also records what happens if nobody rules: nothing breaks, but the 44 stay
pinned to a vintage the corpus has left, invisible to the manifest, each
reporting proton while holding a muon-family value — and the next pin audit
re-derives this same list from scratch.

## 2026-08-30 — seven detectors were blind to the LIVE muon pin (fixed)

Measured by feeding all four pin values to each detector: every one of them
recognised the two SUPERSEDED muon vintages (A, A') and classified vintage C —
**the pin actually in use** — as not-muon (`None`, `''`, or `AMBIGUOUS`).

    tr_m_wenzl_bridge_mpfr.anchor_of_q0        q0_producer_pin_classifier
    q0_anchor_payload_recovery                 q0_witness_read_dataflow_audit
    q0_cross_layer_fallback_scan               chi_dual_path_xref_audit
    stamp_joint_tower_witness

Each was spelled with an A/A'-only prefix (`1.10997859555` or longer), written
when the corpus had two vintages; C leaves both at the 10th digit. Widened to
`1.109978595`, the prefix all three share — proton diverges a digit earlier at
`1.109978582`, so it stays unambiguous. `witness_regen_classify.py` and
`consumer_control_arm_audit.py` already used this width and never had the bug.

**100 witnesses** carry vintage C and no superseded vintage, so no detector
could see them at all — including every `-muon` chi-cache sibling,
`canonical-tr-m-via-chi-cache-muon` and `muon-pin-stored-vs-live`.

Two sites needed more than a widening:
- `q0_anchor_payload_recovery`: `_SUPERSEDED_MUON` had to widen WITH the
  prefix. The label names the CURRENT value, so when C became the pin, A
  joined A' as superseded; widening the prefix alone would have proposed
  `q0Anchor: "muon"` for A-valued payloads, which the consistency audit reads
  as flips — the exact 74-flip defect guard 1 exists to prevent.
- `tr_m_wenzl_bridge_mpfr` is the COMPUTE path. `anchor_of_q0 -> None` for
  today's muon pin sent callers down the off-anchor branch, bypassing the
  muon cache and the straddle guard; and since that guard reads the TABLE's
  declared pin, the muon y_lambda cache could not have been regenerated at
  the live pin at all without raising. Latent only because it is still at A.

NOT touched: `tools/qou-substrate/witness.py:278` has the MIRROR bug (muon
recognised ONLY as C, so A/A' are unlabelled). It STAMPS; changing it
restamps corpus-wide and is not a unilateral call.

## 2026-08-30 — did the convention-C sweeps flip witnesses proton -> A?

Raised by the `option_b_h3_h4_bratteli` review, which found `.work/convention-c-
regen*.jsonl` logging that producer's witness moving
`lambda_A_at_q0  2.53277965639939149205… -> 2.53277966367467598266…`
under `kind: "q0_refresh"`. Confirmed independently: evaluating
`lambda_A(q) = (3q^2+4+3q^-2)/4` at 60 dps gives the "before" as **exactly**
lambda_A(proton) to all 50 digits and the "after" as **exactly** lambda_A(pin A).
So that witness held proton values until a sweep re-ran the producer against
its hardcoded pin-A literal and overwrote them, logged as a benign refresh.

Scope, measured across all eight regen logs: 2890 `q0_refresh` field deltas
over **44 witnesses / 43 producers**, median relative move **1.154e-08** — the
11.54 ppb mu-p tension. 25 of those witnesses still hold the sweep's output.

**The class does NOT generalise.** Cross-tabbing sweep-output witnesses against
producers holding a pin-A literal, evaluated at `9faabdc38` (before this
session's migrations): **exactly 1 — bratteli itself**, now migrated. Today the
count is 0. The mechanism is benign in general because the sweep re-ran each
producer and each landed on whatever pin its OWN source resolved to; only a
producer with a hardcoded pin-A literal could be moved away from proton.

BOUND ON THIS RESULT: it covers only the 44 witnesses these sweeps logged with
`q0_refresh` deltas. Most of the 189-producer A-literal population's witnesses
do not appear in these logs, so this bounds the SWEEP-INDUCED variant, not the
campaign.


---

## 2026-09-13 post-merge: the gate is RED on 4 NEW, and all four look like FALSE POSITIVES

Measured on the merged tree (218 commits from main). `stale total: 206,
baseline: 329, NEW: 4` — so the backlog is draining well, but four new entries
block. Read individually, none is a stale copy of q₀.

### Three of the four are fields DELIBERATELY at a retired pin

```
probes/the_gram_block_publishes_a_D_eigenvalue_no_pin_produces_probe.witness.json
    data.D_spectrum_at_retired.q0          (-0.0798 ppb)
probes/two_blocks_publish_the_two_sides_of_one_identity_at_different_pins_probe.witness.json
    data.figures_at_retired.q0             (-0.0798 ppb)
    data.figures_at_frozen_A.q0            (-0.0769 ppb)
```

The field names say it: `..._at_retired`, `..._at_frozen_A`. The second probe's
own description says what it is for:

> That block publishes the right side at the PROTON pin and says so; this block
> publishes the left side at a MUON pin, so the two sides of a proved identity
> are published as numbers differing by 7.94e-8 relative.

**The probe exists to document that these pins differ.** Flagging its
comparison figures as drift is a false positive by construction, and "fix by
RE-RUNNING THE PRODUCER" — which is what the gate prints — would destroy the
measurement.

**This audit has no exemption mechanism at all.** `q0_anchor_consistency_audit`
has one (`AUDIT_SUFFIXES` → `Q0_AUDIT_EXEMPT`, 92 witnesses); this one has
nothing. Deciding what marks a field as deliberately-off-pin is a convention
call, so it is recorded here rather than invented. A field-name convention is
already latent in the corpus (`_at_retired`, `_at_frozen_*`) if that is the
route wanted.

### The fourth is under `_deprecated/`, which every other audit skips

```
computations/_deprecated/alpha-high-precision.witness.json  q_0  (-0.0769 ppb)
```

`scan()` is a bare `HERE.rglob("*.witness.json")` with **no directory
filtering**. Every other audit in this repo carries
`SKIP_DIRS = ("_deprecated", "__pycache__", "node_modules", ".git")`.
Measured: **190 of the 2909 scanned rows (6.5 %) are under `_deprecated/`**.
You cannot re-run a deprecated producer, so those findings have no fix.

**Not changed here, deliberately.** Adding the skip would drop 190 rows from
scan, and they are currently *in the baseline* — so they would drain **by
exclusion rather than by fix**, silently, in a ratchet whose whole value is
that its count only falls when something is repaired. That is the same trap the
y_lambda check-D ratchet fell into today (7 "drained" entries, all of them
files main had deleted). If the skip is adopted, the baseline should be
regenerated in the same change with the reason stated, so the drop is not read
as progress.

### Net

The gate blocks on four findings, none of which is a defect in the sense the
gate exists to catch. Worth fixing before the noise trains readers to skip it —
`scripts/precision-gates.sh`'s own header says a gate red on arrival gets
skipped.
