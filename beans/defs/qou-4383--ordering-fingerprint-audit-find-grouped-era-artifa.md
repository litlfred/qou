---
# qou-4383
title: 'Ordering fingerprint audit: find grouped-era artifacts by VALUE, not by symptom'
status: todo
pr: 8352
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T04:29:13Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
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

## 2026-09-13 (later still) — scoping the tranche found the migration target was itself grouped

`52b154af6e1`, `2ffefa65ef9`.

### I was wrong about the fix, in three commits, and here is the correction

I recommended `canonical_trm_reference.tr_m_nucleon()` as the durable
alternative to a hardcoded trace — in this bean, in `derivation_chain.py`'s flag,
and in two commit messages — on the stated grounds that it *"selects by recorded
q0 and cannot silently serve the wrong frame"*.

The first half is true. **The second was false as deployed.** Measured: the
module was returning the GROUPED values for all five atoms. It selects by
**pin** and has no notion of the intra-nucleon ordering at all, so it guards a
cross-pin read while being blind to precisely the frame this bean is about.

**Why nobody saw it, which is the durable lesson.** The CANONICAL-pin witness
was the stale one (`atomic-tr-m-mpfr-50dps-proton.witness.json`, proton pin,
**2026-08-19**) and the RETIRED-pin witness was the fresh one (muon,
2026-09-07). Any check of the form *"is the recent artifact canonical?"* passes.
The file that matters is the other one.

### One producer re-run unblocked the target

    QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py \
        --anchor proton

(A bare `--anchor proton` is refused with exactly that line — the producer binds
its pin at import, before argparse, and says so. Good guard; it wrote nothing on
the refusal.) Checked for the truncating open-with-import template first per the
coordination note — absent from this producer. Diff 61+/49-, a normal
regeneration.

The module now serves canonical on all five atoms, and the producer's own
**independent** bridge-vs-peel cross-check agrees to **4.3e-51**. The witness has
moved from the audit's grouped list to its borromean one.

### Mirror synced, on this bean's own evidence

`qou-mass/src/qou_mass/` held the same file at 2026-08-19 and three live package
modules read it. This bean already answered the packaging question by
measurement — mirror, `computations/` authoritative, 42 of 43 non-identical
modules differing only by the `_path_bridge` shim — and a sibling has synced two
such pairs. Verified before copying that the mirror was **structurally identical**
to the pre-regeneration `computations/` copy (all keys equal, `results`
identical), so this is a mirror restore rather than a judgement about values.

### Two new beans, both found on the way

- **`qou-72f8`** — the `qou_mass` copy of `canonical_trm_reference` resolves its
  data against `_internal/`, which holds **0** witness files against **25** one
  level up. So `tr_m_nucleon` **always raises** in the shipped package, and
  `_internal/markov_weights_symbolic.py` imports it. The error prints
  `inspected []`; that empty list is the tell — a path bug wearing a provenance
  error's clothing, which is likely why it survived.
- **`qou-y4gi`** — the `computations/` copy validates the pin and **not** the
  ordering. Regenerating its input fixed today's values; it did not fix the gap,
  and the corpus already shows this recurring (`TR_M_AT_Q0` corrected then stale
  in five days; `path_b` the same two-step). Proposed fix: stamp
  `intra_ordering_frame` at the producer and require it on load, with
  absent-or-wrong raising — an undeclared frame must not default to canonical,
  since every pre-ruling witness is undeclared.

### Where the tranche now stands

`derivation_chain.TR_M_AT_Q0` is **unchanged** and still grouped; the twelve
consumers still hardcode it. What changed is that **the migration target is now
correct**, which it was not when the tranche was first scoped. Order of work:

1. `qou-y4gi` — the ordering assertion, so the target cannot stale again
   silently. Do this BEFORE migrating; migrating twelve consumers onto a loader
   that can serve the wrong frame just relocates the problem.
2. Migrate the twelve, diffing what moves at each.
3. `qou-72f8` in parallel if the package matters.

And a dependent worth remembering: `assembly_chain_11_letter_recompute_probe`
is red until step 2 reaches the neutron chain's leaf.

## 2026-09-13 — the TR_M_AT_Q0 tranche: migration half COMPLETE

`eecf2369cca`, `ff7b290798d`, `3d7d7a89f6e`, `7d0bc81993b`.

### The inventory was smaller than "twelve consumers"

Of the twelve modules that *mention* the registry: **six** genuinely import it,
**one keeps its own separate copy**, **one AUDITS it by AST**
(`derivation_convention_frame_audit` — migrating that would break what it
measures), and the rest name it only in prose.

| module | outcome |
|---|---|
| `audits/canonical_a_k_magnitude_audit` | own copy, **two** rulings behind, migrated; also fixed a crashing data path |
| `build_markov_trace_assembly_neutron_chain` | migrated, target → 0.4751335171556822 |
| `build_markov_trace_assembly_deuteron_chain` | migrated, target → 0.1519683392042316 |
| `applied_uniqueness_mass_table` | migrated; was MIXING frames; frame check added, now gated red |
| `build_proton_mass_50dps_chain` | migrated; documentary step, mass unmoved (verified) |
| `phase5/phase2_proton_m_e_hecke_diagnostic` | migrated; **ratios move 45–74 %** |
| `build_six_term_substrate_model_b` | **not migrated — already dead** (`qou-imkb`) |
| `audits/derivation_convention_frame_audit` | **must not migrate** — it audits the registry |

### What actually moved

Only `phase2_proton_m_e_hecke_diagnostic` moved numbers:

    atom      categorical_ratio_to_m_e_Hecke
    proton    1.870053963830540526  ->  1.027159604966268874   (-45 %)
    neutron   1.612147827654885259  ->  0.775490116256505033   (-52 %)
    deuteron  0.938768523368891780  ->  0.248035427477920604   (-74 %)

and they gained precision, 16 digits → 60, because the values now come from the
50-dps witness rather than float literals. The proton mass chain is
**byte-identical** — verified by baselining before the edit, not assumed.

### Three findings the migration produced that the migration was not looking for

1. **Δ_I(deuteron) = b_pn, exactly.** In the canonical frame,
   tr_M(atom)/tr_M(free) = `0.508229789376738962577995797656`, which is
   `qbeta_bond_factors_derived_probe.MEASURED["b_pn"]` to all 20 digits it
   carries. Invisible in the old frame (Δ_I was 0.19047 there). Second link to
   `qou-qqm4` today, after b_pp = markov_z. **The migration made an independent
   identity appear** — the best evidence available that it is right.
2. **`applied_uniqueness_mass_table` was mixing frames**, and migrating it
   changed no number, because the authority there is the assembly CHAIN file
   and not the registry. What the migration bought was a frame-consistency
   check that makes the disagreement visible. It fires on exactly one atom.
3. **The orphan** — `markov-trace-assembly-proton.derivation.json` has no live
   builder while both siblings do, so the cluster is now mixed-frame at 82 %.
   Un-deprecating the old builder does **not** fix it: that builder assumes a
   6-crossing all-positive-σ word and yields ~2.12258, the fifth claimant in
   `trm_proton_five_values_census`. Beaned as `qou-nhkv` with the real work
   (write a live builder against the canonical 11-letter element — the
   recompute probe already has the value and the method).

### Two deliberate reds, and why they are opposite calls

- `applied_uniqueness_mass_table.all_chains_in_the_canonical_intra_ordering_frame`
  — **expected 0, measured 1, RED.** An artifact is genuinely in the wrong
  frame. Locking the measurement would teach the next reader that a
  mixed-frame mass table is acceptable.
- Earlier today, `magnus_omega2_weight_family_robustness_probe` had its
  assertion **re-framed to lock the measurement**. Opposite call, and rightly:
  there the assertion encoded a hypothesis that reality had disproved, so a
  permanent red carried no signal. The test is whether the red names something
  someone can fix.

I also left `canonical_a_k_magnitude_audit`'s
`deuteron_true_delta_I_differs_from_fallback_and_a_k` red rather than touch it:
it misses its band by 0.0082 and the miss is a tolerance artifact, but widening
a tolerance in the same commit that moves the values it tests is how a real
signal gets lost.

### A method note worth keeping

I checked one migration by diffing **stdout** and read "no output" as "nothing
moved". Wrong instrument — those values are only ever written to the witness.
That is the same shape as the defect this bean chases: checking the artifact
you can see rather than the one that carries the claim.

### Remaining in this bean

- `derivation_chain.TR_M_AT_Q0` itself is **still grouped and unchanged.** With
  every live importer now reading the reference, the registry's remaining role
  is as a fallback and a historical record — so the question has changed from
  "what should its numbers be?" to "should it exist?". That is now a small
  owner call rather than a twelve-consumer tranche.
- `qou-nhkv` (the orphan) gates the mass table red until it lands.
- The witness arm is still at 48 candidates; the downstream-reflection taxonomy
  remains unbuilt.

## 2026-09-13 — the third category is BUILT, and the count converges

`10118c90b7f`. This closes the bean's own open ask: *"The taxonomy needs a third
category … otherwise the number never converges, because an audit that reports
the corpus will always mirror it."*

    46 candidates  ->  28 ACTIONABLE  +  16 downstream reflections  +  2 unresolved

(48 → 46 came from this session's earlier regenerations, not from the taxonomy.)

### The discriminator, and why it can be mechanical

**What can the producer possibly know?** A module that never calls the trace
machinery cannot have computed a |tr_M|, so any it emits came from something it
read. That is a fact about the code, not a judgement about intent — which is
exactly what a curated list can never be, and why this one will not rot the way
`SOURCE_DELIBERATE` nearly did.

**Validated against the bean's own examples**, which was the check available for
free: all three sites this bean named as reflections —
`witness_value_copy_audit`, `derivation_chain_validator`, `atomic_mass_via_rho_k`
— classify as `reflects`. **3/3.**

**AST, not substring**, same lesson as the source arm: eight candidate producers
*mention* `atom_braid_word_3A` in a docstring while never calling it. A grep
files them as computing their own traces, which is the opposite of true.

### "Actionable" is deliberately not called "computes"

Ten producers land in `neither` — no trace call, no artifact read. I checked
what that bucket actually holds rather than assuming it was one thing:

- **Hardcoders** — `path_b_defect_binding_probe`, `qbeta_chain_closed_form_probe`.
  Both are *independently* flagged by this same audit's SOURCE arm for carrying
  grouped literals. **Two detectors agreeing from opposite directions**, which
  is the strongest evidence either of them is right.
- **Computers by an unlisted idiom** — `vhat_per_crossing_chain` builds Hoefsmit
  matrices and takes the trace inline, calling nothing in `_COMPUTE_CALLS`.

Both own their value, so both are actionable. But a bucket labelled "computes"
would be false for the hardcoders, so it is named for the property they share
and the mixture is documented at the classifier. A bucket named for a property
it does not have is worse than a coarse one.

### What the number now means

**28** is the first figure this bean has produced that is a count of *work*
rather than a count of the corpus. The 16 reflections resolve when their inputs
do — and today already demonstrated that, twice: `graded-hecke-energy-probe` and
`skein-proton-canonical` went green the moment `canonical_trm_reference` served
canonical values, without either being touched.

The **2 unresolved** name no `scriptFile`. That is now a fixable class rather
than a mystery: `stamp_staleness_metadata` sets the field (fixed earlier in this
bean), so re-running each producer stamps it and moves it into a real bucket.

### Suggested order for the 28

1. The ones whose producers are already known here: the six hardcoded sites,
   most of which are recorded above with verdicts.
2. Then re-run and re-scan, because reflections resolve for free and the number
   should drop again without further work.
3. Only then read the residue per-site.

Do **not** re-run producers in bulk without the 0-byte diff the 2026-09-08
coordination note asks for — 252 producers still carry the truncating
open-with-import template.

## 2026-09-13 — the re-run pass, done safely. 27 actionable → 21.

`9238d6e25aa`. First sweep run against the new taxonomy, so "actionable" was a
real target list rather than the whole corpus.

### Truncation handled by PRE-classification, not damage control

This bean's 2026-09-08 coordination note says 252 producers carry an import
inside a truncating `with open(…, "w")`, and advises diffing for 0-byte outputs
*before committing*. That finds the damage. **AST-classifying the producers
first finds the risk:**

    24 distinct producers behind the 27 actionable witnesses
      23 SAFE
       1 UNSAFE — computations/cross_check_trM_cw_seminormal_leg.py L220

Only the safe set was run. The unsafe one is left for `qou-oyde`, which
repaired the identical template in `qbeta_chain_closed_form_probe`. Recommend
this pre-check become the standard opening move for any future sweep here — it
is one AST walk and it turns "hope nothing breaks" into a list.

### Result

    19 clean exits · 2 skipped as known-slow · 1 timeout at 600 s

    grouped-era witness files   46 → 40
    ACTIONABLE                  27 → 21
    downstream reflections      16 → 16

The reflections holding steady is the taxonomy working, not a failure: they
resolve when their **inputs** do, and 21 of those inputs are still open. Two
already demonstrated it earlier today — `graded-hecke-energy-probe` and
`skein-proton-canonical` went green the moment `canonical_trm_reference` served
canonical values, neither being touched.

### Every substantive move was grouped → canonical, checked

Five witnesses moved beyond provenance fields. The largest is
`sweeps/paper-six-term-isotope-sweep.witness.json`, whose `term1_canonical_tr_M`
rows go

    proton    1.14575969245730086968…  →  0.62932840220292191816…
    neutron   0.98774368811580957163…  →  0.47513351715568221250…
    deuteron  0.57517224391777187082…  →  0.15196833920423160759…

That is a **paper-facing** table, so this moves published numbers — in the
direction the ruling requires, from an artifact that was stale against it.

### A third slow producer

`markov/markov_peel_atomic_witness.py` times out at 600 s. That makes three
with `atomic_tr_m_helium4` and `binding_combiner_markov_peel_fallback`. Worth
connecting to `qou-bimg`: the sparse route is ~87× faster than the dense one on
the identical H₉ sweep, so this cluster has a candidate remedy rather than
merely a budget problem.

### Where the 21 stand

Of the 21, four are the documented hardcoded sites (`path_b`, three qbeta),
which are owner calls rather than re-runs; two are the known-slow skips; one is
the unsafe-template producer. So roughly **14 are ordinary re-run or read
work**, and the next pass should expect the reflections to start falling as
those land.

## 2026-09-13 — clusters, not sites: reading the flagged FIELD is the cheap move

After `qou-nhkv` closed, 19 actionable remained. Rather than open 19 files, I
dumped the flagged JSON path for each. That is nearly free and it groups them:

    /data/tr_M_cross_check/proton/markov_trace_assembly_chain   braid_encoding_audit
    /data/sources/proton/target_value                           applied_uniqueness_mass_table
        └── both were the ORPHAN proton assembly chain → closed by qou-nhkv

    /results[*]/peel_reference            cross_check_trM_cw_seminormal_leg
    /tr_M_proton_markov_peel_reference    markov_weights_symbolic
    /data/results[*]/bridge_witness_value markov_peel_atomic_witness  (×3 witnesses)
        └── the PEEL cluster, upstream = markov/markov_peel_atomic_witness.py

    /data/std_channel/proton_terms/T1_descended   vhat_std_vs_full_tower_compare
    /complex_tower_plus_i0/proton/T1/abs          vhat_tower_im_cancellation
    /trM_composition/proton_product_genuine       vhat_per_crossing_chain
        └── the VHAT cluster, T1 term

**The field name is a dependency edge.** `braid_encoding_audit`'s flagged field
is literally `markov_trace_assembly_chain` — it names its own upstream. Reading
19 fields found two clusters and confirmed a third had already been fixed;
reading 19 files would have cost far more and found the same thing.

### Peel cluster — in flight

`markov/markov_peel_atomic_witness.py` is the upstream and is one of the three
known slow producers (it timed out at 600 s in the safe sweep). Re-launched with
a 3000 s budget; it is emitting canonical values as it goes (deuteron bridge
`0.151968339204231607592665697751…`) and had reached ⁴He when this was written.
It is on the SAFE list — no truncating open-with-import template.

### VHAT cluster — upstream identified, and it is NOT what it first appears

`vhat_std_vs_full_tower_compare` reads `PER_GEN_WITNESS` =
`terms-2-3-atom-per-gen-mpfr-50dps.witness.json`. Two copies exist, one in
`_deprecated/` (2026-04-27) and a live one (2026-08-29, pre-ruling) — which
looks like the answer, and is not:

- **neither copy contains `T1_descended_50dps`**, the key the consumer reads;
- re-running the live producer `terms_2_3_atom_per_gen_mpfr_50dps.py` reports
  **unchanged**, i.e. it recomputes identical values, so nothing there depends
  on the intra-nucleon ordering. Terms 2 and 3 are not term 1.

So the grouped T1 enters via `derive_full_tower`, not via the per-gen witness.
**Not chased further** — that is the next thread rather than this one's tail,
and stopping at a mapped edge is better than a half-traced one.

### Method note for whoever continues

Two cheap checks have each caught something today that a re-run would not:

1. **Dump the flagged field before opening the file.** It names the upstream
   often enough to be worth doing first, every time.
2. **Compare the artifact's `computedAt` against your run.** A producer's exit
   code answers "did it run?", not "did THIS artifact get rebuilt?" — that is
   how the `--atoms` default hid two witnesses earlier today.

## 2026-09-14 — the residue is explained, and it is not a value problem

The live-emitter residue this bean had been chasing has a structural cause, now
beaned separately as **`qou-t29k`**: 18 sites assemble the grouped intra-nucleon
word BY CONSTRUCTION, by writing all of `_PROTON_G0` then all of `_PROTON_G1` —
which is verbatim `nucleon_word_letters`' `intra_order="grouped"` branch.

**Why this bean's tool could not see it.** The value fingerprint matches
committed *numbers*, so it needs a witness carrying a |tr_M| at a canonical
atom. It is blind to symbolic producers, to producers too slow to have been
re-run, and to witnesses recording a ratio or a slope. That is why re-running
six safe producers returned byte-identical output: the stale-value hypothesis
was correctly retired, and the residue was never a value.

The structural counterpart is
`computations/audits/intra_ordering_structural_assembly_audit.py`, gate
`intra-order assembly`, green on arrival.

### Correction to my own triage here

Three qbeta probes I filed under this bean as **hardcoded grouped values
awaiting an owner call** are grouped *assemblies*:

- `qbeta/qbeta_d_frame_trace_baseline_probe.py:103`
- `qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py:105`
- `qbeta/qbeta_epsnpq_functional_mismatch_probe.py:74`

That is a different defect with a mechanical fix (call `nucleon_word_letters`),
so they do **not** need the owner call I said they did. Two more of the
actionable items are on the same list — `probes/b_pred_mirror_slope_closed_form.py`
and `rho_k_h3a_gg_trajectory.py` — and move to `qou-t29k`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8352, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-13: "fix(qou-4383): TR_M_AT_Q0 becomes a live view — the last hardcoded grouped registry, closed"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-20 — the SYMBOLIC per-λ chi caches are a blind spot of the value audit, and two of them were wrong

Found by the W3 precision-gate pass (PR #8627) while draining the q0-anchor refill.
`intra_ordering_value_fingerprint_audit.py` keys on |tr_M| VALUES, so it cannot see
the symbolic per-partition caches `chi-<atom>-h<n>.witness.json` written by
`per_irrep_pole_atom.load_or_build_chi_atom` — they carry χ^λ_q as sympy strings,
no tr_M number.

Measured against a fresh `hoefsmit_symbolic.chi_lambda_symbolic` on today's
`atom_canonical_crossings(Z, N)`:

| cache | convention_fingerprint matches? | per-λ result |
|---|---|---|
| chi-proton-h3 | no | χ_(2,1) WRONG |
| chi-neutron-h3 | **yes** | χ_(2,1) WRONG |
| chi-deuteron-h6 | **yes** | (6) ok, (5,1) WRONG, (4,2) WRONG (stopped there) |
| chi-tritium-h9 | yes | (9) ok (stopped there) |
| chi-helium-3-h9 | no | (9) differs (stopped there) |

The H_3 fresh values were confirmed by a third, independent route: a from-scratch
sympy (2,1) rep (σ1 = diag(q,−1/q), σ2 solved from braid + Hecke relations,
averaged = (σ+σ⁻¹)/2) reproduces the FRESH χ_(2,1) for both nucleons exactly.

**The detector defect.** The resume guard compares `convention_fingerprint`, a ctype
**multiset**. A reordering of the same letters (the 2026-09-05 grouped → alternating
intra ruling, qou-hu1f) leaves the multiset unchanged, so the neutron and deuteron
caches were served as current. That is an order-blind fingerprint, the same class as
the value audit's own origin story.

**Done in #8627:** chi-proton-h3 and chi-neutron-h3 regenerated (commit 09a1a5d27d).
**NOT done, needs a decision:** deuteron-h6, tritium-h9, helium-3-h9, helium-4-h12
regeneration (h9/h12 are long symbolic computes) and re-running their consumers
(`delta_lambda_empirical_tabulation`, `chi_free_via_lr`, `aK_via_lp_dual`,
`binding_depth_stratified_lr`, `mass_vol_density`, the perknot-rerun probes, …), whose
committed numbers move. Fixing the guard (fingerprint the ORDERED word) is cheap and
corpus-derived; it is not done here because it would also invalidate every cache on
the next run.
