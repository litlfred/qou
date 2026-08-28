# The superseded-muon class is 19 actionable, not 260

**Date:** 2026-08-28
**Beans:** `qou-1c4y` (the migration umbrella)
**Branch:** `claude/superseded-muon-triage-2026-08-28`

## Why this measurement exists

[`2026-08-22-q0-migration-worklist-partition.md`](2026-08-22-q0-migration-worklist-partition.md)
established that the corpus carries **two** muon values agreeing to 11 digits —
the live ideal/CAL-2 pin `1.10997859555733471…` and a **superseded** one,
`1.10997859555418057…` — and that the superseded class was the *larger* of the
two. It was recorded as the largest untouched population in the q₀ arc and
recommended as the next work item on that basis.

**That recommendation was inflated, by the same error class the arc kept
correcting.** A population count is not a work count.

## Measured on `main`, 2026-08-28

```
witnesses carrying the superseded value          265
  under _deprecated/                             214   ← 81%, not live work
  live                                            51
    no scriptFile at all (orphan)                 13
    scriptFile names a missing producer            2
    scriptFile names a LIVE producer              36
      self-declaring (deliberate)                 17
      GENUINE candidates                          19
```

**265 → 19.** A 14× over-count of actionable work.

## The 17 deliberate ones declare themselves

They carry the superseded value under a field or a producer name that says so:

| signal | producers |
|---|---|
| `stale_muon_pin_q0` | `mp_dk_decisive_test`, `per_basis_row_invariants_probe`, `qbeta_multi_block_eigenphase_probe`, `qbeta_multi_block_eigenphase_full_eps_probe` |
| `q0_muon_pin` / `q_muon` / `q0_muon` | `c_3_categorical_derivation_attempt`, `probe_mup_dressing_attribution`, `qbeta_chain4_kashiwara_step3_cross_anchor`, `qbeta_chain4_kashiwara_step4_n5`, `qbeta_complex_c3_fibre_probe`, `qbeta_qbessel_crossanchor_smoothness_refutation` |
| subject *is* the pin history | `muon_pin_three_values_probe` (`q0_from_CODATA_2018`), `probe_trace_convention_production_impact` (`S2_q0_current_muon_pinned`) |
| subject *is* literals | `fitted_labelled_canonical_audit`, `hardcoded_q0_literal_families_audit` |

A producer whose subject is the pin history necessarily contains superseded
pins. Re-pinning it would destroy what it measures.

## The 19 genuine candidates

`alpha_em_smatrix_perloop_probe`, `build_six_term_substrate_model_b`,
`chirality_avg_content_chiral`, `compound_binding_via_differences`,
`confinement-operator-selection`, `d_from_scratch`,
`delta_coupling_closed_form_probe`, `derived_masses`, `deuteron_delta_i_audit`,
`garside-irrep-qvalues`, `he4_partition_dominance_audit_probe`,
`implied_h2_coefficient_audit_50dps`,
`lambda_scale_homflypt_skein_recursion_probe`, `neutron_error_diagnostic`,
`q_beta_predicted`, `qbeta_h4_route_a_gate_probe`, `snappy_cusp_seeding`,
`term5_aK_audit`, `universal-ilp`.

These carry the superseded value under a **bare pin key** (`q_0`, `q0`, `q`,
`q_0_50dps`, `q_0_mpf50`) with nothing declaring it deliberate.

**19 is still an upper bound, not a defect count.** Each needs an individual
read — the arc's standing lesson is that a count from a detector is a
hypothesis until one of its members has been opened by hand, and that rule has
already corrected numbers here in both directions (dual-purpose 21 → 3;
contradictions 2 → 11). Two in this list are worth flagging before anyone
starts: `q_beta_predicted` carries `CAL-2_q_0`, and naming CAL-2 identifies
*which calibration*, not *which pin* — the exact conflation
[the partition audit](2026-08-22-q0-migration-worklist-partition.md) retracts.
`confinement-operator-selection` is an LP/SDP witness, so the dual fields
matter to any re-run.

### Method note added 2026-08-28: match on ≤ 18 significant digits, never the full literal

Re-scanning these 19 with an exact match on the recorded 19-char literal
`1.10997859555418057` returns **0 hits on nine of them** — all nine genuinely
carry the value. The superseded pin has two renderings that diverge at the
**19th** significant digit: the *rounded* `…057528…` (107 files: AGENTS.md,
bean `qou-khac`, content `.qa.json`) and the *truncated* `…056776…` (5 files,
incl. `d-from-scratch`, one of the 19). `|d| ~ 7e-19` — three orders below the
3.15e-12 that makes superseded a distinct pin, and below the 1 ppQ L1 target,
so it moves no observable and raises no ruling question. It breaks detectors.

`q0_muon_population_partition.py` was safe by construction (16-digit prefix,
with a comment showing the length was deliberate), so **the 19 stands** — the
re-scan was the wrong instrument, not the triage. The usable window is 14–18
digits: 14 is the shortest that separates superseded from current, 11–13 are
ambiguous between them. The ceiling is now recorded in the script itself.

A second, unrelated blind spot in the same pass: witness stems drop a
producer's `_probe` suffix (`alpha_em_smatrix_perloop_probe` →
`alpha-em-smatrix-perloop.witness.json`), so a stem-equals-producer-name
lookup returns NO FILE for three of the 19. Both failures were mine, in one
sitting, on a list whose own text warns that counts here move when read by
hand. That is the sixth and seventh instance in this arc.

## 🛑 The "13 orphans" were my detector's blind spot, not a provenance gap

An earlier revision of this document called the 13 a provenance gap — *"nothing
can regenerate them and nothing identifies what did"* — and proposed a bean for
them. **That was wrong, and it is the fourth detector correction in this arc.**

The scan keyed on `scriptFile` / `script`. Opening the 13 by hand:

| how provenance is recorded | count | resolves? |
|---|---:|---|
| under `computation`, naming a producer path | 8 | **all 8 exist** — 6 under `docs/audits/scripts/`, which a `computations/`-scoped search cannot see |
| no provenance field, but the witness-name ↔ producer-name convention holds | 5 | **all 5 exist** |
| genuinely unregenerable | **0** | — |

The five that record nothing still resolve by name:
`alpha-k-jones-markov-h4` → `computations/alpha/alpha_k_jones_markov_h4.py`,
`consumer-control-arm-audit` → `computations/audits/consumer_control_arm_audit.py`,
`metallic-q-n4-character-sweep`, `q0-value-drift-audit`,
`two-quark-active-set-mahler-sweep` — the last of which this arc has been
regenerating all along, which should have been the tell.

So the real finding is smaller and different in kind: **13 live witnesses omit
`scriptFile`**, a field-completeness gap in how the schema is used, not a loss
of provenance. Nothing is unrecoverable and no bean is warranted for the
"orphans" as such.

### The pattern is now the finding

Four counts in this arc came from a field-keyed or shape-keyed detector of mine,
and **every one was wrong until a member was opened by hand** — twice too high,
twice too low:

| detector | direction | corrected |
|---|---|---|
| dual-purpose, by substring match | over 7× | 21 → 3 |
| contradictions, file-local scan | under 5.5× | 2 → 11 |
| superseded-muon "work", by population | over 14× | 265 → 19 |
| orphans, by `scriptFile` only | over ∞ | 13 → 0 |

That is not four unlucky scans. A detector encodes one spelling of the thing it
looks for, and the corpus has more spellings than any one scan carries —
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues thirteen for
convention C alone, four of them found *by* detectors written to catch the
previous blind spot. Treat any count in this arc as a hypothesis with an error
bar of several fold until one of its members has been read.

## What this does not say

- It does not say the 19 are wrong. It says they are the only ones that could be.
- It does not authorise a sweep. The first bulk attempt broke `main` for 208
  producers (`qou-m9xp`); constraints 1–4 in AGENTS.md §"q₀ anchor convention"
  rule 4 stand.
- It does not touch the 214 deprecated witnesses. They are correct as recorded
  for retired code.

## The 19 read: all nineteen producers resolve to PROTON today (2026-08-28)

The individual reads this document asked for are done to the point where the
character of the item is settled, and it is not "19 files to adjudicate".

**Anchor resolution.** `computations/substrate/q_parameter.py` (the source, not
the generated `qou-mass/_internal/` mirror — `sync-qou-mass-vendor.py --check`
reports in sync, so the raw `diff` between them is import rewrites only)
resolves the anchor from the running producer's stem:

```python
_stem = _MP(_sys.argv[0]).stem ...
if _stem in _man.get("ideal_muon", []):
    _anchor = "ideal"
```

with the comment stating the rule outright: *"ideal_muon ⇒ muon; anything else
⇒ proton"*. So an **unlisted** stem resolves to proton.

**Measured against `q0_anchor_manifest.json`:**

| bucket | size | of the 19 |
|---|---:|---|
| `ideal_muon` | 45 | **0** |
| `physical_proton` | 665 | 2 |
| `ambiguous` | 18 | 0 |
| unlisted | — | 17 |

**Not one of the nineteen is listed under `ideal_muon`.** None of them asks for
the muon anchor. The two that are listed are listed `physical_proton`. So every
one of the 19 resolves to proton on a run today, and the superseded value in
its committed witness is a **stale output from before that default** — not a
deliberate muon pin, and not a live defect in the producer.

**Two are not bare pins at all** — my "bare pin key" test missed two declarative
field names:

| witness | key carrying the value | also carries proton? |
|---|---|---|
| `chirality-avg-content-chiral` | `/parameters/q0_anchor_note` — a *note about* the anchor | yes |
| `he4-partition-dominance-audit-probe` | `/data/cache_anchor_q_0` — the anchor of a cache it **read** | yes |

The second deserves its own look and not as a pin defect: a `physical_proton`
producer recording a **muon-built cache's** anchor is the shape of the μ₃
Fréchet straddle AGENTS.md documents at 11.54 ppb, where `y_λ` came from a
muon-built cache while `χ_λ` was evaluated at proton. Whether this one straddles
or merely records its provenance honestly is a separate read.

**One is unresolved:** `derived_masses` has no witness carrying the value under
that stem.

**One would move data, not just a parameter:**
`delta-coupling-closed-form-probe` carries the value at twelve `/data/rows[i]/t_value`
entries as well as at `/parameters/q_0`, so a re-run changes tabulated data,
not only a recorded pin.

### What this changes about the work

The item is **not** "read 19 and adjudicate". It is "re-run 17 producers, which
self-correct, and read 2 by hand". Constraint 1 is not at risk: the
anchor-defining `q-pinning-50-digit` is **not** among the 19.

It is still **not** authorised as a sweep here, and this document does not run
one. The bulk migration is `qou-1c4y` under the owner authorisation recorded
2026-08-19, with its four constraints; a producer re-run mutates sibling
witnesses and several producers in this corpus are long-compute or refuse by
design. What has changed is the *expected outcome* of doing it: for these 19,
the run is a re-pin with no adjudication in it.

## `derived_masses` resolved — it is `free-neutron-decay`, and it is the dependency-order case

The one unresolved candidate of the 19. Three corrections, two of them to my own
reading:

1. **It resolves via a top-level `scriptFile`.** `free-neutron-decay.witness.json`
   declares `"scriptFile": "derived_masses.py"` at the **top level**; my scan read
   `witness.scriptFile` and `computation.script` and returned `None`. Eighth
   detector blind spot of the arc, same class as the other seven.
2. **I nearly reported it unregenerable, and that was wrong.**
   `derived_masses.py` is a *library* — its only "write" is a `print(json.dumps(...))`
   — and it *reads* this witness, so the declaration looked circular. But
   `computations/free-neutron-decay.py` **exists**. My consumer scan missed it for
   a mundane reason: a file does not usually contain its own name, so a
   `grep -rln "free-neutron-decay" --include=*.py` never lists the producer. The
   live producer sets `witness["scriptFile"] = Path(__file__).name`, so the
   committed witness simply predates that fix.
3. **It is regenerable and would self-correct — but must NOT be re-run alone.**
   `free-neutron-decay` is unlisted in the manifest, so it resolves proton, exactly
   like the other 17. What makes it different is that **20 Python consumers** read
   this witness and several call it canonical; it supplies `Δ(net)` to the `c_k`
   chain that `qou-cds1` is actively working on #5337 and #5897. This is precisely
   the **dependency-order** blocker the `qou-1c4y` sibling flagged: it *is* the
   upstream. Re-running it moves numbers under live work. Left for the sanctioned
   migration, not taken here.

Its `transition.delta_net = -0.1882906200111204` also turns out to be the
"possible third model" #5897 flagged in `pyhecke` — see
[the Δ-fork addendum](2026-08-28-delta-element-fork-corpus-asymmetry.md), where the
anchor explanation for it is measured and refuted.

## 🛑 Currency + unit correction, 2026-08-28 (post-rebase)

Two corrections to the prefix analysis above, one of staleness and one of
units. Both were caught by the `/prepare-merge` verification on #5892 and by
re-deriving rather than re-reading.

**1. The value this document calls "current" has been demoted.** Main's
`fca08de7d` — *"muon anchor → CODATA 2022 (owner ruling): derive it, stop the
self-certification"* — landed in this branch's history during the rebase and
re-derived the anchor-defining witness. The canonical muon pin is now
`1.10997859564273904…`, **not** `1.10997859555733471…`. So the corpus carries
**three** muon renderings in play, not two: superseded (`…55418057…`), demoted
(`…55733471…`), and canonical (`…5642739…`).

**The headline result is untouched.** 265 → 19, and all nineteen resolving to
the **proton** anchor, is a statement about the proton pin and about manifest
membership. Neither depends on which muon value is current.

**2. The separation threshold was quoted in the wrong unit, and is now
looser.** Re-derived:

| separate superseded from | common prefix | shortest that separates |
|---|---:|---:|
| demoted `…55733471…` | 12 sig digits | **13** |
| canonical `…5642739…` | 10 sig digits | **11** |

The text above says *"14 is the shortest"*. That figure counted **characters
including the decimal point** (`1.109978595554` is 14 characters but 13
digits), so it was right about the boundary and wrong about the unit. Against
the value that is now canonical only **11 significant digits** are needed,
because CODATA-2022 moved the muon anchor at the 11th figure rather than the
13th.

**The 18-digit ceiling is unchanged and still binding.** That limit comes from
the superseded value's own two renderings diverging at their 19th digit — a
fact about the superseded value alone, independent of what the current one is.
So the usable window widens at the bottom but not at the top: **11–18**
significant digits against the canonical pin, 13–18 against the demoted one.
`q0_muon_population_partition.py`'s 16-digit constants sit inside both, so the
count of 19 stands under either reading.

