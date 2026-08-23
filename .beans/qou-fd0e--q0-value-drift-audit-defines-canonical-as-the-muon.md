---
# qou-fd0e
title: q0_value_drift_audit defines CANONICAL as the muon pin — a BLOCKING CI gate that cannot see 211 stale witnesses, plus a 13-file inverted ANCHOR NOTE
status: todo
type: task
created_at: 2026-08-23T07:56:50Z
updated_at: 2026-08-23T07:56:50Z
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
