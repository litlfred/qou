---
# qou-4383
title: 'Ordering fingerprint audit: find grouped-era artifacts by VALUE, not by symptom'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T04:29:13Z
updated_at: 2026-09-08T04:28:57Z
---

## The tool

`computations/audits/intra_ordering_value_fingerprint_audit.py` — scans every
committed witness for grouped-era |tr_M| values, matched to **15 significant
digits** against fingerprints computed **live** from `atom_braid_word_3A` under
both orderings at both documented pins (never transcribed, so a re-pin moves
them rather than silently invalidating the scan).

Unlike the three sweeps that missed `compute_tau_M_nucleon_H3`, this keys on the
**answer**, not on a symptom. A 15-digit match to `1.14575969245730087` *is*
that number — the corpus's own coincidence floor puts 9–11 figures at 2.7 %, so
fifteen is not a near miss. That makes the count of *witnesses carrying grouped
values* exact, in a way a symptom count never is.

## Measured — 3548 witnesses scanned

| | count |
|---|---:|
| carry a **grouped**-era value | **89** |
| carry a **borromean** (canonical) value | 15 |
| of the 89: `qou-mass/` duplicates | 6 |
| of the 89: `computations/` originals | 83 |

Age of the 83 originals: **59** from 2026-08 (pre-ruling, expected stale),
**21** from 2026-09, 3 undated.

### The sharp set — 10 computed AFTER the 2026-09-05 ruling

    2026-09-05  derivation-chain-audit                      derivation_chain_validator.py
    2026-09-05  two-row-vs-higher-row-binding-split         two_row_vs_higher_row_binding_split.py
    2026-09-05  the_character_closure_block_..._convention_c_probe
    2026-09-06  atomic-mass-via-rho-k                       atomic_mass_via_rho_k.py
    2026-09-06  qbeta-habiro-pochhammer-convention          (producer field absent)
    2026-09-06  habiro/habiro-exact-qbeta                   habiro_exact_qbeta.py
    2026-09-06  qbeta-bond-factors-derived                  qbeta_bond_factors_derived_probe.py
    2026-09-06  qbeta-mixed-chain-closed-form               qbeta_mixed_chain_closed_form_probe.py
    2026-09-06  atomic-tr-m-helium4                         atomic_tr_m_helium4.py
    2026-09-06  gap-a4-L1-light-series-probe-perknot-rerun

These ran *under* the ruling and still emitted grouped values, so they are live
source behaviour, not merely stale artifacts.

**One is already accounted for.** `atomic-tr-m-helium4` is mine: arm (A), the
disjoint-product route, is deliberately retained and labelled non-canonical
(`qou-hft3`), and it reads the grouped proton leg. Expected, not a finding.

**One is informative.** `gap-a4-L1-light-series-probe-perknot-rerun` was in the
`qou-y2o7` sweep and classified `same` — so it does *not* take its baselines
from `compute_tau_M_nucleon_H3` and reaches grouped values some other way. That
is a second, independent route into the grouped frame, and the reason the
value-keyed scan is worth having.

The other eight want per-site reading. **Not swept.**

## The sharpest actionable finding: `qou-mass/` has forked

All six `qou-mass/src/qou_mass/` hits have a `computations/` twin, and at least
one pair has demonstrably diverged:

    computations/atomic-tr-m-mpfr-50dps.witness.json
        2026-09-06   0.62932842249…  0.47513351767…  0.15196834395…   BORROMEAN
    qou-mass/src/qou_mass/atomic-tr-m-mpfr-50dps.witness.json
        2026-08-29   1.14575978231…  0.98774375682…  0.57517232973…   GROUPED

This is the **second** instance of this defect class — the habiro pair forked
the same way and was synced under `qou-y2o7`. And these are not inert copies:
`qou_mass/_internal/canonical_trm_reference.py` reads
`atomic-tr-m-mpfr-50dps.witness.json`, and `chi_monotone_transfer.py`
references `chi-helium-3-h9-at-q0-50dps.witness.json`. So the `qou_mass`
package is computing against grouped-era references while `computations/` has
moved.

**No producer writes the `qou-mass` copies**, which is exactly why no
symptom-keyed sweep could ever have found them: there is nothing to raise, and
nothing to name `atom_braid_word_3A`.

Not synced here. Whether `qou-mass` is a vendored package with its own cadence
or a mirror that must track `computations/` is a packaging question, and
overwriting six live inputs on a guess is the kind of sweep this arc has
avoided. It needs an owner call — but it is a small, bounded one.

## What a hit does and does not mean

A hit says the **witness payload** is grouped-era. It does not say the producer
is broken: it may be fixed while the artifact was never regenerated (re-run to
tell them apart), or the site may be deliberately historical — three are, and
pass `intra_order="grouped"` on purpose. A non-hit is not a clean bill either: a
witness recording only derived quantities carries no |tr_M| to match.

---

## 2026-09-07 — swept, with the stale-vs-live discriminator applied

Re-ran the audit: **89 → 83 witness files**, 84 → 81 candidates.

### The `qou-mass` fork is closed, and the packaging question is answered

The bean's sharpest finding has resolved under it. `atomic-tr-m-mpfr-50dps` and
`chi-helium-3-h9-at-q0-50dps` are now **identical** across
`qou-mass/src/qou_mass/` and `computations/`, both dated 2026-09-06, both
carrying the same values. A sibling closed it.

The packaging question — *"vendored package with its own cadence, or a mirror
that must track `computations/`?"* — is answerable from evidence rather than an
owner guess, and I measured it rather than leaving it open:

- `docs/audits/2026-05-19-qou-mass-deprecation-audit.md` already names
  `computations/` **"Authoritative originals"** and the `_internal/` tree
  "entirely redundant with computations/".
- That audit is from May and the package has since gone `0.1.0a1` → `1.0.0`, so
  I re-measured today: of the 43 vendored modules that are no longer
  byte-identical, **42 differ only by the folio `_path_bridge` shim** (a
  path-fixup line meaningless inside the package). The sole real difference is
  `__init__.py`, which is package boilerplate.

So it is a mirror, maintained to the line, and `computations/` is authoritative.
The three remaining `qou-mass` hits are **not forks**: each has the *same*
`computedAt` as its twin (2026-08-19 / 08-29 / 08-30), i.e. both sides are
pre-ruling stale. They belong to the "59 from 2026-08, expected stale" bucket,
not to an owner call.

### The eight post-ruling sites, swept

Applied the discriminator the bean named and did not run — *re-run the producer,
re-scan, diff the hit list* — to seven of the eight:

| site | verdict |
|---|---|
| `habiro-exact-qbeta` | **stale artifact** — regenerated, dropped out |
| `two-row-vs-higher-row-binding-split` | **stale artifact** — regenerated, dropped out |
| `the_character_closure_..._convention_c_probe` | **deliberate** — its subject *is* the convention-C table `prop:q-hecke-seminormal-character-closure` publishes; added to the audit's `DELIBERATE` set |
| `derivation-chain-audit` | **live** — still emits grouped after a clean re-run |
| `atomic-mass-via-rho-k` | **live** |
| `qbeta-bond-factors-derived` | **live** |
| `qbeta-mixed-chain-closed-form` | **live** |
| `qbeta-habiro-pochhammer-convention` | not re-run — witness carries no producer field |

### Why the stale ones were stuck: they crashed *after* computing

Three of the seven died on the **last line of `main()`** with

    ModuleNotFoundError: No module named 'qou_substrate'

in the provenance-stamp block. Everything was computed; nothing was written. So
their witnesses were **unregenerable**, which is why they still carried
grouped-era values months after the ruling — not because anyone chose to keep
them.

`computations/_path_bridge` already puts `qou_substrate`
(`tools/qou-substrate/python`) within reach; these three simply never imported
it. Fixed in all three. `two_row_vs_higher_row_binding_split` now exits 0; the
two `qbeta` probes now run to completion and write their witnesses, exiting 1 on
their own honest assertion failures (a closed form that does not reproduce every
atom; two constants extracted rather than derived) — substantive open questions,
not crashes.

**This is the general lesson for the remaining 81.** A stale witness is not
evidence that anyone intended a grouped value; it can simply mean the producer
cannot write. Re-running is cheap and separates the two, and until it is done a
hit count is an upper bound on the real finding count.

### Remaining

- 4 confirmed-live grouped emitters need per-site reading (why do they reach the
  grouped frame?).
- 81 candidates un-swept; the 59 from 2026-08 are pre-ruling and expected stale,
  so re-running is the first move there too, not reading.

---

## 2026-09-07 (later) — the bulk re-run, and a third category

### Result

    grouped-era hits   83 files / 81 candidates  ->  48 files / 46 candidates
    dropped            36
    newly hit           0     (the sweep introduced no regression)

**36 of 81 were purely stale artifacts.** The hypothesis from the morning pass —
that a stale witness is not evidence anyone intended a grouped value — holds for
nearly half the population.

The residual splits by what the producer actually did:

| | |
|---:|---|
| 27 | completed clean and **still** emit grouped |
| 13 | timed out at the 120s budget — verdict unknown, re-running at 900s |
| 4 | exited 1 on their own assertions |
| 2 | no identifiable producer |

### The taxonomy needs a third category

The bean has "stale artifact" vs "live source defect". Many of the 27 are
neither. `witness_value_copy_audit` scrapes witnesses for copied values;
`derivation_chain_validator` classifies every witness it can find;
`atomic_mass_via_rho_k` globs `atomic-tr-m-*.witness.json`; several more are
explicit C-vs-D or three-path *comparisons* that hold both frames on purpose.

These are **downstream reflections**. They carry grouped values because their
inputs do, they resolve when the inputs do, and fixing them at the reflection
would be wrong. Any future count should exclude them, the way `DELIBERATE`
already excludes the deliberate ones — otherwise the number never converges,
because an audit that reports the corpus will always mirror it.

There is also a **dependency order**: re-running a consumer before its inputs is
wasted work. One bulk pass is not a fixed point.

### Seven witnesses flipped green → red, and that is the finding

    probe-9b-manybody-expansion              he4_2body_fraction_matches_ceiling_audit
    colour-weighting-across-mixed-nuclei     reproduces the committed dense arm (x2)
    qbeta-habiro-taylor-investigation        taylor_series_reproduces_delta_tr_at_q0
    skein-proton-canonical                   atlas |tr_M| cross-check vs Layer-1 table
    tr-m-algebraic-q                         algebraic_q0_matches_transfer
    tr-m-atom-via-transfer                   trM_atom_deuteron_matches_canonical_branching
    tr-m-q-hecke-seminormal                  q_hecke_seminormal_closes_gap[p,n]

All seven were computed 2026-08-21..08-31, **before** the ruling, and all seven
fail on a **cross-check against a reference**. They were green only because both
sides were grouped-era. `algebraic_q0_matches_transfer` now reports max
deviation **0.976 against a 1e-9 tolerance** — a whole-value mismatch of exactly
the grouped-vs-borromean magnitude, not drift.

Committed red deliberately: a stale green is a false all-clear, and the honest
state of these seven is red.

### Two source defects found, one fixed

**`stamp_staleness_metadata` never set `scriptFile`** — 948 call sites, and its
own docstring promised seven fields and delivered them all except the one that
says *which script produced the witness*. That is why
`qbeta-habiro-pochhammer-convention` was unattributable and un-re-runnable, and
a sibling had already worked around it locally rather than fixing the helper.
Fixed. Same probe also passed an unrecognised `q0_anchor` token, so its witness
was reported Q0_ANCHOR_UNRECOGNISED and never checked; fixed too.

**Two qbeta probes hardcode grouped-era nucleon traces.** `T_P` /
`MEASURED["t_p"]` = `1.1457596924573008697` matches the grouped proton to
~1e-21 and differs from canonical by **82 %**; the neutron by **108 %** — while
the same probes read *canonical* atom witnesses. Flagged in place with the
measurement, not flipped: `qbeta_delta_vs_deltaTbeta_settled_probe` is
deliberately grouped, so a grouped constant is not automatically a defect, and
`qbeta_bond_factors_derived_probe` is under active edit today (`qou-qqm4`).

### Next

- 13 slow producers re-running at 900s; their verdicts are still unknown.
- A second pass after that, since consumers whose inputs just moved will only
  converge on a re-run.
- Then the residual is small enough to read per-site.

COORDINATION NOTE (2026-09-08, session fervent-noether — not a criticism of this bean's subject, which is unrelated).

Commit 36501d7b01 ('sweep(qou-4383): re-run all 74 candidate producers') TRUNCATED computations/qbeta/qbeta-chain-closed-form.witness.json to **0 bytes** on main. Its own --numstat records the file as pure deletion (0+ 176-) while the commit message asserts 'newly hit 0 (no regression introduced by the sweep)' and lists seven deliberate green->red flips, none of which is this file. It was the only unparseable witness of 3702, and the zero propagated into 24 branches.

NOT THE SWEEP'S FAULT. The producer destroyed its own witness: it ran 'from qou_substrate...' INSIDE a 'with open(path, "w")', and open(...,'w') truncates at open, so the import raising under the sweep's PYTHONPATH wiped the committed file and wrote nothing back. Any producer re-run would have done it. qou_substrate is not on PyPI, so a bare container is the default.

FIXED in PR #7166 (bean qou-oyde): the payload is now built before the file is touched, and the witness is restored (diff vs the last good blob is 4 provenance leaves; no number moved). A re-run can no longer truncate THIS producer.

WHAT THIS BEAN SHOULD KNOW GOING FORWARD: **252 other producers in computations/ still carry the identical template** (measured by AST: an import inside a truncating with-open(w)). Any of them can be zeroed the same way by a sweep that re-runs producers in an environment where an import fails. If this bean runs another producer sweep, diff for 0-byte outputs before committing — 'git diff --numstat | awk $1==0' catches it, and the sweep's own message will not.

Also fixed in #7166: q0_anchor_consistency_audit tallied Q0_PARSE_ERROR but never named the file and could not fail --strict on it, which is why this reached main unseen.

---

## 2026-09-13 — the scan was only ever pointed at witnesses. Pointing it at SOURCE.

`b394e3a3232`. Witness state on entry: **49 grouped files / 48 candidates**
(the bean last recorded 48/46; the drift is sibling landings, not a regression).

### Why source is the sharper surface

This bean's whole argument is *key on the answer, not on the symptom*. That
argument was only ever applied to committed witnesses — and a witness hit is
weak evidence, as this bean already found: 36 of 81 were purely stale and
cleared on a re-run. **A hardcoded constant is the opposite.** It does not
clear on a re-run; it re-emits the grouped value every time. Same method, much
stronger hit.

The bean found two by hand (`T_P` / `MEASURED["t_p"]`). The scan finds **eight**.

### The AST filter is load-bearing, and it retired a list I had just written

A raw substring scan hits 14 files, and the first is `mass_at_3A_proper.py` —
whose docstring quotes *both* values because it EXPLAINS the ruling. Flagging
that flags the documentation of the fix. So the scan reads literals reachable
as **code** and excludes docstrings; comments never enter an AST, so they are
excluded for free. Strings are *not* skipped wholesale — `mp.mpf("1.1457…")`
is how this corpus writes a high-precision constant, and skipping strings would
miss the exact shape.

14 → 9 files. I had drafted a seven-entry `SOURCE_DELIBERATE` list; **six of the
seven turned out prose-only and dropped out on their own.** Pruned to the one
that is real. Six dead entries in a curated set is the rot that teaches the next
reader to trust the list instead of the mechanism.

### Two standing-red audits, one cause, both cleared

    computations/audits/h3_transition_cache_q_key_audit.py
    computations/audits/word_to_mpfr_template_scale_audit.py

carried a **byte-identical** `_PRODUCTION` table of grouped-era (atom, free)
traces as their "production unmoved" gate. Both had failed on all four atoms
since 2026-09-05. Neither audit's actual subject was broken — the cache-key and
dps-key checks, and the template-scale checks, passed throughout. Stale
references guarding against a change already ruled correct: a standing red,
which is a gate someone eventually silences.

Measured, not assumed. Recomputing `tr_m_atom_zn` with `atom_braid_word_3A`
forced to each ordering:

    ordering    D            T             3He          4He
    grouped     0.575172…    0.229310…     0.403767…    0.160974…   <- the baselines
    borromean   0.151968…    0.0291440…    0.0585962…   0.0112374…  <- the code

So the baselines were the old frame and the code is in the new one, not the
reverse. Both audits now exit 0.

> A methodological note for whoever measures this next. My first attempt
> patched `mass_at_3A_proper.atom_braid_word_3A` and got **identical output for
> both orderings** — the consumer does `from mass_at_3A_proper import
> atom_braid_word_3A`, so the patch never took. Identical-under-both is the
> signature of a failed patch, not of an ordering-independent quantity. Patch
> the binding inside the consumer module.

### The sharpest finding, and it is a TRANCHE, not a sweep

`computations/derivation_chain.py` exports `TR_M_AT_Q0` / `TR_M_AT_Q0_50DPS` —
p, n, D — described in its own comment as "the production canonical Markov
trace". **Every entry reproduces to 50 significant digits under `grouped`.**

    key   registry (grouped)                canonical (borromean)          off by
    p     1.14575969245730086968908159577   0.62932840220292191816534575    82 %
    n     0.98774368811580957163402016550   0.47513351715568221250609023   108 %
    D     0.57517224391777187082653534399   0.15196833920423160759266570

**Left unchanged deliberately.** `trm_proton_five_values_census.py` (bean
`qou-soj6`) already settled the policy for this exact constant: *"TR_M_AT_Q0
feeds live producers, so correcting it moves published numbers and is its own
tranche."* Twelve live modules import it (now listed in the flag above the
table): `applied_uniqueness_mass_table`, `audits/canonical_a_k_magnitude_audit`,
`audits/derivation_convention_frame_audit`, the deuteron and neutron
`build_markov_trace_assembly` chains, `build_proton_mass_50dps_chain`,
`build_six_term_substrate_model_b`,
`canonical_derivation_pipeline_compliance`,
`markov/assembly_chain_11_letter_recompute_probe`,
`phase5/phase2_proton_m_e_hecke_diagnostic`, `probes/graded_hecke_energy_probe`,
and the census. Flipping three numbers moves all twelve at once. Overwriting
live inputs on a judgement call is the move this arc declined for the
`qou-mass` fork, and it is the same call here.

**The history is the argument for doing it properly.** This registry has been
corrected once already and went stale again in five days: `qou-soj6` found it
at the convention-C value 1.63315, and the fix landed the *then*-canonical
GROUPED value, which the 2026-09-05 ruling superseded. The failure mode is not
"nobody looked" — it is that **a hardcoded constant does not track a ruling.**
The durable fix is `canonical_trm_reference.tr_m_nucleon()`, which selects by
recorded q0; the tranche should migrate consumers to it rather than re-typing
three better numbers that the next ruling will stale again.

The census's own docstring asserted the grouped pair as canonical — in the
document a reader consults for *"which value is right"*. Corrected in place.
Its finding about the five claimants is untouched; only the label moves.

### Remaining hardcoded: 6

    derivation_chain.py                        pending its tranche (above)
    markov/assembly_chain_11_letter_recompute_probe.py    unread
    probes/path_b_defect_binding_probe.py                 unread
    qbeta/qbeta_bond_factors_derived_probe.py             known to this bean
    qbeta/qbeta_chain_closed_form_probe.py                unread
    qbeta/qbeta_mixed_chain_closed_form_probe.py          known to this bean

Note `qbeta_chain_closed_form_probe.py` is the producer whose witness the
2026-09-08 coordination note records as having been truncated to 0 bytes and
restored in PR #7166 — so read it with that history in hand.

### Truncation guard applied

Per the coordination note (252 producers carry an import inside a truncating
`with open(…, "w")`): checked `git diff --numstat` for 0-added deletions and
scanned the whole tree for 0-byte witnesses. **Both clean.** No producer sweep
was run in this pass — the work was source-side — so the exposure was low, but
the check is cheap and the note asks for it.

### Next in this bean, in my order

1. Read the 4 unread hardcoded sites. Small, bounded, and each is a live
   re-emitter rather than a stale artifact.
2. The `derivation_chain` tranche — owner call, and worth scoping as "migrate
   12 consumers to `canonical_trm_reference`" rather than "edit 3 constants".
3. Only then the remaining witness candidates, in dependency order. The
   downstream-reflection taxonomy the bean asks for is still unbuilt; a first
   pass classified the 48 candidates as 25 computing / 17 reflecting / 4
   neither / 2 no-producer, but that discriminator is not yet validated well
   enough to bake into the count.

## 2026-09-13 (later) — verdicts on all six hardcoded sites

`cc56f213c87`. Read rather than re-run: each is a live re-emitter, so a re-run
tells you nothing a read does not.

| site | verdict |
|---|---|
| `derivation_chain.py` | **tranche** — 12 live consumers, flagged, not flipped |
| `markov/assembly_chain_11_letter_recompute_probe.py` | **failing correctly**, reporting it wrongly — fixed the report; blocked on the tranche |
| `probes/path_b_defect_binding_probe.py` | **grouped in all six atoms**; frame now declared in the witness; not flipped (calibrated model) |
| `qbeta/qbeta_chain_closed_form_probe.py` | **constants stale, result survives** — measured |
| `qbeta/qbeta_bond_factors_derived_probe.py` | already flagged by this bean's earlier pass |
| `qbeta/qbeta_mixed_chain_closed_form_probe.py` | already flagged by this bean's earlier pass |

### The one that was lying about itself

`assembly_chain_11_letter_recompute_probe` printed

> "The recompute on the canonical 11-letter element reproduces the live
> producer witnesses at both pins, to every digit they carry."

**unconditionally** — while four of its own seven assertions were failing. It
recomputes on the canonical element, so it returns borromean
(n: `0.47513351715568221251`); its `LIVE` table holds faithful copies of
committed witnesses that are still grouped (n: `0.98774368811580957163`). The
failure is a *true report that the producers are stale*, which is the job the
old agreement was evidence for. Summary now gated on the result; docstring says
which side is right and that `LIVE` must **not** be "repaired" — editing it
would hide the staleness rather than fix it.

**It is blocked, not fixable in place.** The neutron chain's leaf is hardcoded
against `derivation_chain.TR_M_AT_Q0`, which is behind the tranche. This probe
goes green when that lands and not before — so the tranche has a dependent, and
that is one more argument for scoping it.

### A structural result worth more than the site it came from

`qbeta_chain_closed_form_probe`'s headline is that `tr_M(β_free)` factorises as
`t_p^Z · t_n^N`. I tested whether that survives the ordering ruling, using the
canonical pair against the canonical free traces computed *independently* by
`h3_transition_cache_q_key_audit`:

    atom   t_p^Z · t_n^N (canonical)          rel. to measured free
    2H     0.299015017184640076702160426771   5.4e-32
    3H     0.142072056797304797470498604255   3.9e-31
    3He    0.188178642999488779263479037146   7.1e-31
    4He    0.0894099805019306003820475658199  1.6e-31

Residuals are the precision floor of the 30-digit reference, not drift. **The
factorisation is ordering-independent** — as it must be, since multiplicativity
of the Ocneanu trace is over *disjoint strand ranges* and the nucleon blocks
stay disjoint whichever word sits inside them. Consequence for whoever refreshes
that probe: it is a **small** job — swap two constants and re-measure
`MEAS_ATOM` / `MEAS_FREE_HOMOG`; sections 1–3 need no re-derivation. Left
undone only because the A=4 re-measure is the 33-minute matrix route the file
documents.

### The pattern across all six, stated once

Every one of these was correct when written and went stale on a ruling. `path_b`
records its own history plainly: defect (i) was "convention-C values … while
convention D has been canonical since the owner rulings", fixed 2026-08-31,
grouped-era by 2026-09-05. `derivation_chain` was corrected from 1.63315 and
went stale within five days. **A hardcoded trace does not track a ruling** —
which makes the durable fix a migration to
`canonical_trm_reference.tr_m_nucleon()` (selects by recorded q0, cannot serve
the wrong frame silently), not a better set of typed digits.

That reframes the `derivation_chain` tranche. Scope it as *"migrate 12 consumers
to `canonical_trm_reference`"*, not *"edit 3 constants"* — otherwise the next
ruling re-opens this bean.

### Where the bean stands

- **Source arm: complete.** 8 hardcoded found, 2 fixed outright (the standing-red
  audits), 1 report-defect fixed, 1 frame-declared, 2 already flagged, 1 pinned
  behind its tranche. No unread sites remain.
- **Witness arm: 48 candidates, unchanged this pass** — deliberately, since the
  work was source-side and a producer sweep carries the 0-byte truncation risk
  the coordination note documents.
- **Next**, in my order: (1) scope the `derivation_chain` tranche as a consumer
  migration and put it to the owner; (2) the witness candidates in dependency
  order, which needs the downstream-reflection taxonomy this bean asked for and
  which is still unbuilt — a first pass split the 48 as 25 computing / 17
  reflecting / 4 neither / 2 no-producer, but that discriminator is not
  validated well enough to bake into the count.
