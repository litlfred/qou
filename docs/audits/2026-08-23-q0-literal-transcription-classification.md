# Hardcoded-q₀ literals: the 72 sites are 37 defects

**Date:** 2026-08-23 · **PR:** #5535 · **Branch:** `claude/q0-literal-transcription-drain-2026-08-23`

Owner instruction: *"resolve the 71. do it proper."*

`computations/audits/hardcoded_q0_literal_families_audit.py` reported **72**
divergent hardcoded-q₀ literals against a baseline of 71. This document records
the classification that had to come first, the thirteen sites migrated, and
three findings the classification surfaced that are larger than the thing it was
looking for.

§2 corrects this document's own first deferral argument, which conflated
*transcribing* the new value with *reading* the anchor. That correction is what
turned up eight sites that were never blocked at all.

Machine-checkable artifacts:

- Ledger — [`computations/audits/q0-literal-classification.json`](../../computations/audits/q0-literal-classification.json)
- Validator — [`computations/audits/q0_literal_classification_audit.py`](../../computations/audits/q0_literal_classification_audit.py)

## 1. Why the classification is the job

The families audit counts **sites**, and says so itself:

> This count is SITES, not defects. … The predecessor CODATA sweep made exactly
> this mistake and had to correct itself: its "code that computes a wrong
> number" bullet was **wrong for 87 % of its own count**. Do not quote 65 as a
> defect count. The split is the next step.

The split, on the 72 sites as found:

| class | meaning | count |
|---|---|---:|
| **(a)** | **code that computes** — the literal feeds arithmetic, or is published as a q₀ into a witness | **50** |
| (b) | deliberate classifier constant | 10 |
| (c) | documentation / docstring / comment | 2 |
| (d) | test fixture | 10 |

**22 of 72 were never defects.** After this PR's migrations the live set is **61**
sites / **37** class-(a) — 32 cost-deferred, 5 correctness-deferred.

The code-vs-documentation half of the split was made mechanically — `tokenize`
for comments, `ast` for module/class/function docstrings — rather than by eye.
That is what put `hardcoded_q0_literal_families_audit.py` itself and
`flavor_split_alpha_dilog_expansion_probe.py` in class (c): both appear in the
char-13 family *because they document the superseded value on purpose*. The
semantic half — is this constant load-bearing? — cannot be mechanised and is
recorded per row with a reason.

### Class (b) is load-bearing *because* it is superseded

The instruction was explicit that migrating one breaks the detector, and the
ten rows bear that out:

- `q0_muon_population_partition.py::MUON_OLD` — the script exists to separate
  the `MUON_CURRENT` population from the `MUON_OLD` one. Re-pinning it collapses
  the two populations it was written to split.
- `Q0_STALE_MUON_PIN` in `mp_dk_decisive_test`, `per_basis_row_invariants_probe`
  and the two `qbeta_multi_block_eigenphase` probes — one leg of a drift test.
- `regenerate_y_lambda_{jones_markov,orphans}_conventionD` — the anchor is held
  fixed **by documented design**: *"moving the convention and the anchor in one
  commit would make the diff unreadable and conflate two independent axes."*
  Re-pinning here silently does the thing that section refuses to do.
- `muon_pin_three_values_probe` (B *is* its subject), `q0_provenance_audit`
  (its reference string), `c_3_categorical_derivation_attempt` (reproduces the
  historical cross-anchor c₃ pair).

The validator records these under `never_migrate_class_b`.

## 2. Why the remaining defects are not fixed here — the reason, corrected

Owner ruling, 2026-08-22, landing in **#5500**: *"2022 CODATA better than 2018.
A → CODATA 2022."*

```
A  1.10997859555733471989…   the anchor the families audit measures against — being replaced
B  1.10997859555418057528…   Vol(4₁)/206.7682830, CODATA 2018 — the 66-site char-13 family
C  1.10997859564273904668…   q_muon_at(), live over the NIST ratio — the destination
```

**The first version of this section gave one blanket reason — "blocked on
#5500" — and it was wrong.** That argument works against *transcribing C*. It
does not work against *reading the anchor*, which is what the migration is: a
site that calls `_q0_value_for_anchor` is pinned to nothing and follows the
anchor before and after the ruling. This document's own next sentence said as
much. Corrected under review; recorded rather than quietly rewritten, because
the distinction is the whole substance of the deferral.

Re-measured — by scanning for `WitnessBuilder` / `json.dump` / `.save(`, not by
family label — the 45 split three ways:

| why deferred | count | the argument |
|---|---:|---|
| **migratable now** | **10 → 8 migrated** | emits **no witness**, so reading the anchor costs no regeneration at all |
| cost-deferred | 32 | emits a witness: reading the anchor regenerates it B→A now, and #5500 regenerates it A→C — **twice**, and each regeneration is a place an unexplained number slips through, which §4 measured happening three times |
| correctness-deferred | 5 | reading the anchor does **not** close the defect |

**Category (3) was not empty**, and the eight in it are migrated in this PR —
see §3.1. Two of the ten turned out on a second reading to carry a matched-pair
constraint and moved to correctness-deferred; see §3.2.

The five correctness cases:

- `gap_a3_overshoot_robustness_check` — the file states it: *"Q0 and TRM below
  are a **MATCHED PAIR** from that one run; changing either alone makes them
  inconsistent, which is why neither has been corrected in place."*
- `gap_a3_deuteron_A_D_overshoot` — same shape, `TRM_BETA_D` frozen at the same
  #2626 run.
- the two `he4_binding_k_*` probes — `y_λ` read from a **B**-built witness, so
  pointing `Q0` at the anchor makes the straddle exact-A-vs-B rather than
  closing it.
- `probe_inter_knot_decoupling` — computes nothing; every value in its witness
  is a transcription of an earlier run.

For all five, cost is *not* the obstacle — two of them emit no witness at all.

## 3. Migrated (13)

### 3.1 Print-only, zero cost (8)

Eight sites emit **no witness**, so reading the anchor costs no regeneration —
the deferral argument never applied to them. All eight moved from the B literal
to `_q0_value_for_anchor("muon")`:

```
gap_a3_cross_atom_overshoot_probe.py            qbeta/qbeta_counit_vs_trace_fork_probe.py
gap_a3_deuteron_plambda_flat_baseline_probe.py  qbeta/qbeta_d_frame_two_row_cap_prune_probe.py
qbeta/qbeta_bar_odd_sinh_partner_check_probe.py qbeta/qbeta_phase_bar_parity_completeness_probe.py
qbeta/qbeta_ck_coordinate_magnifier_probe.py    qbeta/qbeta_sinh_partner_object_identification_probe.py
```

All eight re-run at **exit 0**; the six `qbeta` probes still print `ASSERTIONS
PASS`; `git status` after the runs lists **no witness file**, which is the
measurement that category (3) is real rather than assumed.

Only the **muon** leg moved. The proton literals in the `qbeta` `ANCHORS` dicts
are not divergent, and at 61 characters against the anchor witness's 51,
pointing them at `_q0_value_for_anchor("proton")` would *lose* precision — a
separate question, out of scope here.

### 3.2 Two were migrated and reverted

`gap_a3_overshoot_robustness_check` and `gap_a3_deuteron_A_D_overshoot` are
print-only and were migrated with the other eight. Reading the first one's
comment block reverted both:

> Q0 and TRM below are a **MATCHED PAIR** from that one run; changing either
> alone makes them inconsistent, which is why neither has been "corrected" in
> place.

Moving `Q0` alone would leave a `tr_M` computed at the old pin beside a `q₀`
read from the anchor — creating exactly the straddle this ledger exists to
catch. Reclassified `a-correctness-deferred`. The witness-emission scan cannot
see a constraint like this; only reading the file can.

### 3.3 Read the anchor (3)

Each transcribed the **anchor** value A and got A itself wrong:

| file | wrong from | witness |
|---|---:|---|
| `probe_qbeta_form.py` | digit 18 | none (print-only) |
| `deltalambda/mu3_anchor_consistency_probe.py` | digit 52 | withheld — see §4.1 |
| `q0_anchor_gate_test.py` | digit 52 | none (print-only); re-run PASSes 3/3 |

`probe_qbeta_form`'s literal matches **no pin in the corpus** — not A, not B,
not C, not proton. It tracks A for 17 digits and then goes its own way.

`q0_anchor_gate_test` is class **(a), not (d)**, and the distinction matters:
its literal is an *input anchor* at which `y_λ` is evaluated, not a pinned
expected value, so reading it cannot make the test tautological — the
assertions compare cache against live. A test *about* crossing calibration
layers that transcribes the anchor it tests cannot follow a re-pin, which is
the exact defect it exists to catch. Its proton leg already read
(`q_parameter.Q_MP`); the muon leg is now symmetric with it.

### 3.4 Raise, do not guess (2)

`binding_qgaussian_ell1_ceiling_measurement.py` and
`flavor_split_alpha_bond_dilog_probe.py` each carried

```python
    except Exception:
        return mpf("1.1099785955541810")
```

under `q_muon_at()` — a silent fallback that fires only when the substrate
import fails, and then answers with a retired pin. `q_muon_at()` today returns
**C**, so the two branches of one function returned different numbers.

The fix is not new: `flavor_split_alpha_dilog_expansion_probe.py` removed the
identical fallback under bean `qou-khac`, replacing it with a `RuntimeError`
naming the reason. Both sites now follow it verbatim. The change is
**value-neutral on the normal path**, so no re-run is owed for the fix itself.

Both files therefore move from class (a) to class (c): the literal survives only
in the docstring recording what was removed — which is why the precedent probe
was class (c) in the first place.

## 4. Findings

### 4.1 Two probes' "anchor-stable" conclusions were measured between two *muon* values

Trial re-runs of the two fallback probes (reverted, not committed) moved their
headline anchor-drift figures by three to four orders of magnitude:

| probe | committed | fresh run | factor |
|---|---|---|---:|
| `flavor-split-alpha-bond-dilog` | `alpha_true_anchor_drift` 5.8e-8 | 2.4e-4 | ~4000× |
| `binding-qgaussian-ell1-ceiling` | `inflation_anchor_drift` 6.9e-11 | 2.3e-7 | ~3350× |

The cause is visible in the diff. Each probe evaluates at two anchors:
`analyze(mpf(Q_50_DIGIT_STR), "proton_q0")` and `analyze(_muon_q0(), "muon_q0")`.
In the committed witnesses (2026-06-29) the leg labelled **`proton_q0` carries
the value A** — because `q_parameter.Q_50_DIGIT_STR` was muon-valued when they
ran. It is the proton pin now.

So the committed "Anchor-stable" claim was measured **between A and B, two muon
values 2.8e-12 apart**, not between the proton and muon pins 11.5 ppb apart.
`A_bond_sensitivity` moves 0.1324 → 0.1029 (22 %) between the two readings.

**Not committed, deliberately.** The move is main-side drift under a
2026-06-29 witness, not a consequence of a docstring-and-`except` edit, and the
fresh run also **drops `q0Anchor` and `q0Value`** — a provenance regression the
`q0-anchor-consistency-audit` reads. Landing it inside a literal-migration
commit would launder an unexplained 22 % change under an unrelated diff.

### 4.2 The `mu3` re-run's 22 % move reproduces with the ORIGINAL literal

`mu3_anchor_consistency_probe` shows the same shape and was checked rather than
assumed. Re-running it after the migration moves `d2` 0.4225 → 0.3278 (22 %) and
drives `rel_shift_vs_mixed` to exactly `0.0` — which a change at digit 52
cannot possibly do.

Re-running the **unmodified** file (stashed the edit, ran, diffed) produced
**the same numbers**. The move is main-side drift in the `y_λ` / χ caches since
2026-08-07; the migration is not its cause. Witness withheld on the same
grounds as §4.1.

This is the check the instruction asked for — *"if one does, that is a real
finding — report it, do not absorb it"* — and it is the reason three witness
regenerations were reverted rather than committed.

### 4.3 Two audits on `main` classify A and B with opposite polarity

- `hardcoded_q0_literal_families_audit` measures divergence against
  `_q0_value_for_anchor("muon")` = **A**, so the B family is "divergent".
- `q0_provenance_audit::Q_MUON_50` is **B**, and its committed test
  `test_q0_provenance_audit.py` asserts
  `verdict("1.1099785955573347…") == "stale"` — i.e. **the current anchor A is
  asserted stale by a committed test**.

`q0_provenance_audit`'s reference comment claims *"DERIVED not typed:
`q_muon_at(60)` … reproduces exactly this"*. It returns **C**. That comment is
already false on `main` and gets more so when #5500 lands.

Recorded, not patched — #5500 is the resolution, and both `Q_MUON_50` and the
nine test fixtures are classified (b)/(d) and left alone.

### 4.4 Smaller, but live

- **`gap_a3_overshoot_robustness_check` carries an in-source instruction not to
  change its literal**, justified as *"a 17-digit truncation of `q_muon_at()`,
  which derives … from today's constants"*. True under CODATA 2018; expired.
  Classified **(a)**, not (b) — the rationale that would have made it deliberate
  no longer holds, and the comment needs correcting when #5500 lands.
- **Two mislabels.** `habiro_interpolation_wlambda.py` binds muon-B as
  `Q0_PROTON` and comments it *"package-layer proton-pinned q₀
  (constants.py)"*; `probes/brane_tower_full_channel_trace_audit.py` comments
  the same value *"q₀ (proton-pinned, 50 dps)"* and cites
  `zhabiro_physical_z_pin.py` as its source — so the mislabel is inherited, not
  local. Both compute at a muon value while reporting a proton one.
- **The two `he4_binding_k_*` probes already straddle two muon values.** Their
  χ is evaluated at a near-A literal while `y_λ` is read from
  `wenzl-y-lambda-h12.witness.json`, whose recorded `parameters.q0` is **B**.
  Pointing `Q0` at the anchor would make the straddle exact-A-vs-B rather than
  close it; the correct fix reads the consumed witness's own q₀. Left
  `a-blocked` for that reason, not for the ratchet's.
- **`probe_inter_knot_decoupling` publishes its literal** as
  `w.add_data("q_0_50dps", …)` while computing nothing — every value in that
  witness is a transcription of an earlier run. Re-pinning only the q₀ label
  would make the witness self-inconsistent with the `tau_M` values beside it.

## 5. Ratchet

`BASELINE_DIVERGENT` 71 → **61**, in two steps: 72 → 69 (the char-52 family gone entirely, char-18 2 → 1) and 69 → 61 (the eight print-only sites). The baseline comment now says what the 61 are and why each is deferred, so the next reader does not mistake it for a defect backlog.

## 6. Verification

CI is `workflow_dispatch`-only, so zero check runs is expected; the agent's own
verification is the gate.

- `scripts/precision-gates.sh --changed` → **All blocking precision gates
  green.** No baseline was widened; nothing was rebaselined.
- `q0_literal_classification_audit.py --strict` → exit 0, 4/4 assertions.
- `hardcoded_q0_literal_families_audit.py --self-test` → ratchet fires at 68,
  holds at 69.
- `hardcoded_q0_literal_families_audit.py` → `allPassed: true` (was `false`).
- `q0_anchor_gate_test.py` → PASS 3/3 after migration.
- `probe_qbeta_form.py` → exit 0 after migration.
- All 8 print-only migrations → exit 0; the six `qbeta` probes still print
  `ASSERTIONS PASS`; `git status` after the runs lists no witness file.
- No `invocation.argv` drift committed; `q0-anchor-consistency-audit` was
  regenerated once for its one substantive move (`Q0_INDEPENDENT` 36 → 37, the
  new witness) and thereafter reverted by the gate as drift-only.

Not touched: `computations/q-pinning-50-digit.witness.json` (AGENTS.md STRICT
rule 1; #5500 owns it).

## 7. What is left

37 class-(a) rows: **32 cost-deferred** (each emits a witness, so reading the
anchor regenerates it twice) and **5 correctness-deferred** (reading the anchor
does not close the defect). The cost-deferred set is one coherent follow-up
owned by the A→C migration, bean `qou-c4kv`; the correctness five are
independent of it and need their frozen companions recomputed, not a re-pin. The ledger validator fails on an unclassified live site, so a new
transcription cannot land unnoticed, and fails on an orphan row, so the ledger
drains with the corpus rather than rotting beside it.
