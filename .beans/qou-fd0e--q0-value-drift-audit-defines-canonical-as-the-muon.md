---
# qou-fd0e
title: q0_value_drift_audit defines CANONICAL as the muon pin — a BLOCKING CI gate that cannot see 211 stale witnesses, plus a 13-file inverted ANCHOR NOTE
status: in-progress
type: task
created_at: 2026-08-23T07:56:50Z
updated_at: 2026-08-24T09:40:00Z
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
