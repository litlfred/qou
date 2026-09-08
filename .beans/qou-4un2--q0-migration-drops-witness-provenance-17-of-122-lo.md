---
# qou-4un2
title: 'q0 migration DROPS witness provenance: 17 of 122 lost scriptFile/commitSha, and the audit is blind to it by construction'
status: todo
type: bug
priority: normal
created_at: 2026-08-28T14:08:26Z
updated_at: 2026-09-08T08:54:55Z
---

## Measured 2026-08-28, on origin/main at cdbdc84af1

The `migrate(q0) batch*` sweep (bean `qou-1c4y`, still **in-progress**) regenerates
witnesses through producers that do not emit provenance. Those producers write a
witness WITHOUT the top-level fields, so the regeneration DELETES them.

Method: for each of the 9 `migrate(q0) batch*` commits, diff every modified
`*.witness.json` between `sha~1` and `sha`, and record keys present before and
absent after.

    9 migration batch commits
    122 witness files modified
    17 lost at least one provenance field
    per-field: scriptFile 17, commitSha 17, engine 16, auditOnly 15

Worked case — `sublemma-2-1-alpha-shift-extract.witness.json`:

    c3a7e16856  present: auditOnly, commitSha, engine, scriptFile
    3563e08910  present: NONE          <- migrate(q0) batch 4
    253e2ffaf5  present: NONE          <- still gone on main today

I found this on 2026-08-23 while regression-testing #5517: a fresh run of that
producer dropped exactly those four fields, so I DECLINED to commit the
regeneration. The migration sweep committed it five days later.

## Why no gate caught it

`computations/witness_provenance_attribution_audit.py`, line 12, in its own words:

  > "no `scriptFile` at all are invisible to the method, because there is
  >  nothing to [attribute]"

The gate reports "N witnesses carry a scriptFile claim" — a count over the
witnesses that HAVE one. Deleting the field removes the witness from the
denominator rather than failing anything. A provenance regression is therefore
structurally unobservable to the check meant to police provenance: the metric
is a numerator with no fixed denominator.

## Scope caveat — do NOT quote the aggregate as the loss

Witnesses lacking `scriptFile` went 463 -> 505 across the same window, but the
corpus grew 3060 -> 3170 in it, so most of that +42 is new witnesses that never
had the field. **17 is the defensible number** (per-file before/after); 42 is not.

## Second, separate defect this exposes

These are AGENTS.md "bare producers": the provenance on disk was added
downstream, so re-running one destroys it. That is already recorded as a hazard
in the idle-pass witness policy. What is new here is that a *bulk sweep* is now
executing that hazard at scale, unattended, and `qou-1c4y` has more batches to
run.

## Next honest step (ordered)

1. **Stop the bleed.** Make the migration refuse to write a witness that would
   drop a provenance key present in the committed version. Cheap, and it is the
   only step that must land before the next batch.
2. **Fix the gate.** Make `witness_provenance_attribution_audit` ratchet the
   COUNT of provenance-less witnesses rather than only auditing those that have
   it, so a deletion is a red rather than a smaller denominator.
3. **Restore the 17.** Their prior values are in git; a restore is a JSON merge,
   not a producer re-run (re-running is what deleted them).
4. **Fix the bare producers** so a future re-run emits provenance itself.

Steps 1 and 2 are small and independent of the science. Step 3 is mechanical.
Step 4 is per-producer and is the real fix.


--------

## 2026-08-28 follow-up: the population at risk, and TWO corrections to my own method

### Correction 1 — urgency. The batch sweep already converged.

I first wrote "qou-1c4y is in-progress, so more batches will do the same". Precisely:
the `migrate(q0) batch*` commits ran on 2026-08-24 and ended at batch 8/9
("iteration at practical convergence", "final fixed-point writes"). The 17 are
**static damage, not a growing count.**

The live hazard is different and still real: PR #5818 (MERGED) re-partitioned the
remaining reroute into 12 producers that are safe alone, 5 BLOCKED by a straddle,
4 proton, 3 unlabelled — and recorded them in `qou-aj91` **to be picked up cold**.
Each reroute is a producer RE-RUN, which is the operation that deletes provenance.
So the next agent on `qou-aj91` walks into this unless step 1 lands first.
Nobody is holding that work right now, so this is pre-emptive, not a collision.

### Correction 2 — diagnosis. All 17 are bare; my "4 exceptions" were a grep artifact.

I measured that 4 of the 17 casualties DO use `WitnessBuilder`, which would have
meant the emitter itself can drop provenance — a much worse finding. It is wrong.

The marker `witness_base` matched **line 45 of the Phase-6 path-bridge boilerplate**:

    # Keeps flat-namespace imports (`from witness_base import …`)

a COMMENT, present in nearly every producer. All four have `WitnessBuilder=0`.
Re-measured through `_source_normalise.code_only` (comments and docstrings blanked):

    17 casualties: 17 bare, 0 use WitnessBuilder

This is exactly the defect class PR #5818 built `code_only` for — a name in a
comment is not a usage — and I walked into it with the module already on main.
(An earlier pass also resolved producers by `rglob(base)[0]`, arbitrary among
duplicate basenames; re-run with sibling-preferring resolution the casualty
result was unchanged, so that bug did not affect the count.)

### The population at risk

Witnesses that currently CARRY `scriptFile` but whose producer never calls
`WitnessBuilder` — i.e. a re-run drops provenance, as it did for the 17.
Measured through `code_only`, excluding `_deprecated`:

    carry scriptFile, producer really uses WitnessBuilder : 2226
    carry scriptFile, producer does NOT                   :  281   <-- AT RISK
    no scriptFile at all                                  :  325
    producer unresolvable / ambiguous                     :    8

So the 17 are the realised part of a **281-witness** exposure. Any sweep that
re-runs producers — the `qou-aj91` reroute, an idle-pass witness refresh, a
convention migration — draws from that pool.

**The 8 unresolvable are a separate small finding**: `scriptFile` names a producer
that is not uniquely locatable, so provenance is recorded but not followable.

### Step 1 restated, now that the diagnosis is right

Because all 17 are bare, step 1 does not need to change any producer to land:
a pre-write guard that refuses to drop a provenance key present in the committed
witness covers every one of the 281 regardless of how it writes. Step 4 (make the
producers emit it themselves) remains the real fix, and is now scoped: 281 files,
none of which currently touch `WitnessBuilder`.


--------

## 2026-08-28 — CORRECTION 3: step 1 was designed at the wrong layer, and a guard already exists

Corpus-grepped before writing the guard, per the checklist. **It already exists**:
`_check_producer_takeover` in `tools/qou-substrate/python/qou_substrate/witness.py`
(bean `qou-okl8`), with its own test file and a
`QOU_WITNESS_ALLOW_PRODUCER_TAKEOVER` override. It raises with, literally,
*"drops N field(s) the committed one carries"*.

It cannot catch this class, for a reason that invalidates my step 1 as written.

**1. It lives inside the writer, and these producers bypass the writer.**
`_check_producer_takeover` has exactly ONE call site — `witness.py:2022`, inside
`WitnessBuilder.save()`. Measured on the casualties through `code_only`:

    sweeps/low_isotope_binding_sweep.py      WitnessBuilder=False  json.dump=True
    probes/gt_matrix_pslq_probe.py           WitnessBuilder=False  json.dump=True
    sublemma_2_1_alpha_shift_extract.py      WitnessBuilder=False  json.dump=True

A producer writing json.dump(...) directly never reaches line 2022. **No amount
of strengthening the in-writer guard helps.**

**2. Even if reached, two early returns skip this case by design.**

    if not isinstance(new_script, str): return    # a bare producer has NO scriptFile
    if PurePath(old).name == PurePath(new).name: return

The second is deliberate and documented: *"The same producer dropping a field is
schema evolution and is not this function's business."* That is the right scope
for `qou-okl8` (producer TAKEOVER) and the wrong scope for this bean (provenance
DELETION by the owning producer).

### Revised step 1 — one tree-level ratchet, replacing steps 1 AND 2

The check must be independent of how a producer writes, so it belongs where the
repo already puts this idiom: a **pre-commit ratchet over the tree**, alongside
the raw-float64 and float64-padding ratchets in `scripts/precision-gates.sh`.

    for each changed *.witness.json:
        committed = git show HEAD:<path>
        if any of (scriptFile, commitSha, engine, auditOnly) present in
           committed and absent in the working tree  ->  RED

Properties, none of which the in-writer guard has:

  * catches all 281 at-risk AND the 325 that already carry no scriptFile,
    because it keys on the FILE, not on the producer;
  * needs no producer edits at all;
  * subsumes old step 2 — a deletion becomes a red rather than a smaller
    denominator, so there is no separate "fix the gate" item;
  * `--changed` makes it free when no witness was touched.

**Do NOT extend `_check_producer_takeover` for this.** Widening its early returns
would make it fire on ordinary schema evolution by the owning producer, which is
the exact false positive its author measured against ("how a guard like this
earns a reputation for crying wolf and gets switched off"). Two guards, two
scopes.

### Plan, as revised

  1. tree-level provenance ratchet in precision-gates.sh   (was steps 1 + 2)
  2. restore the 17 from git (JSON merge, not a re-run)     (was step 3)
  3. route the 281 through WitnessBuilder                   (was step 4, the real fix)


## 2026-09-08 — re-measured: the DAMAGE is repaired, the GATE is not. 2 of 3, and the missing one is step 1.

Pulled off the `qou-bstl` completion-candidate queue, flagged by `c29e0752bbd`
("P30 provenance on 17 hand-rolled producers"). Measured all three steps of the
revised plan against `main`.

### Step 2 — restore the 17: **DONE**

Worked case from this bean's own opening, `sublemma-2-1-alpha-shift-extract.witness.json`:

    scriptFile PRESENT   commitSha PRESENT   engine PRESENT   auditOnly PRESENT

against the bean's recorded `present: NONE` at `253e2ffaf5`. And it was fixed at
the producer, not by a JSON merge: `sublemma_2_1_alpha_shift_extract.py:344`
emits `"scriptFile": Path(__file__).name` in its own payload, and `:385-388`
imports `WitnessBuilder as _WB` and calls `_WB.stamp_staleness_metadata(...)`.
Landed by `7decba09cf1` on bean `1j39` ("the strip-provenance blocker was a
producer defect — fixed 5, stamped 4"), i.e. by a *different* arc than the one
flagged here — two beans converged on this without either citing the other.

### Step 3 — route the at-risk population: **281 -> 0**

Same measurement, re-run today: 2990 witnesses carry `scriptFile`, and the
number whose producer emits no provenance **by any route** is **1**. That one,
`per_irrep_pole_proton_h3.py`, is a false positive of my own test — its witness
carries all four fields, and its docstring says `per_irrep_pole_atom.py` is now
the de-facto owner and `WitnessBuilder.save()` handles it. It is a retired
intruder, not an exposure. **The real count is 0.**

Both remaining named casualties verified individually, since they are the only
controls this bean supplies:

    sweeps/low_isotope_binding_sweep.py   :294 setdefault scriptFile, :295 _WB.stamp
    probes/gt_matrix_pslq_probe.py        :236 setdefault scriptFile, :237 _WB.stamp

### 🛑 Three measurements, three answers, and two of them were mine and wrong

Worth recording because the failure is this corpus's most common one and I hit
it twice inside twenty minutes:

| test | at-risk | why it is wrong |
|---|---|---|
| `"WitnessBuilder" in code_only(src)` | **3** | too permissive — the bare NAME is present as an import in 906 producers that never construct one |
| `"WitnessBuilder(" in code_only(src)` | **909** | too strict — misses `_WB.stamp_staleness_metadata`, a static call through an ALIASED import, which is exactly how all three named casualties were repaired |
| emits `scriptFile` / `stamp_staleness_metadata` / `WitnessBuilder(` / `wrap_legacy` | **1 (really 0)** | asks the question the bean asks — does the producer emit provenance — instead of asking which helper it names |

The first two disagree by 300x on the same tree at the same commit. The
discriminator was not a better regex: it was checking the three producers the
bean had already measured, and finding that the answer my test gave for them
contradicted their source.

### Step 1 — the tree-level provenance-deletion ratchet: **NOT BUILT**

`scripts/precision-gates.sh` has no gate comparing a changed witness's
provenance keys against `git show HEAD:<path>`. The two provenance rows it does
carry answer a different question:

    witness scriptFile provenance          computations/witness_provenance_audit.py
    witness provenance completeness (adv)  computations/audits/witness_provenance_audit.py

Both ask *"does the named `scriptFile` actually write this witness?"* — neither
can see a key that was present yesterday and is absent today. So this bean's own
central finding stands verbatim and unaddressed: **a provenance regression is
still structurally unobservable to the checks meant to police provenance.**

### So the shape is the one this session keeps finding

The 17 casualties are repaired and the 281-witness pool is drained — real work by
two independent arcs. What was not built is the thing that stops it recurring,
and the bean had already designed it in full. The next producer re-run that drops
a provenance key will land exactly as the first 17 did.

### 🟡 DECISION for the owner — this is the one thing this bean is waiting on

**What is being decided:** whether to add a blocking pre-commit ratchet that
refuses any commit in which a `*.witness.json` loses a provenance key
(`scriptFile`, `commitSha`, `engine`, `auditOnly`) it carries in `HEAD`.

**Why it needs you rather than me.** Under the 2026-09-07 ask-first directive
this is neither exemption: it does not increase precision, and no corpus
artifact fixes what the gate should be — a bean's design is a proposal, not a
corpus decision. More to the point, a new BLOCKING gate changes what every other
agent's commits are allowed to do, which is a policy change, not a repair.

**Option A — build it as a blocking gate in `precision-gates.sh`.**
*Means:* one new script, one row in the gate table, `--changed` makes it free
when no witness was touched. *Costs:* ~1 h; the gate table gains a row.
*Risks:* a legitimate schema evolution that intentionally drops a field now
needs an override; false reds annoy siblings mid-sweep and that is precisely
"how a guard like this earns a reputation for crying wolf and gets switched
off", which this bean already quotes about the neighbouring guard.
*Commits to:* provenance keys becoming append-only in practice.

**Option B — build it as WARN-only, on the commit hook.**
*Means:* same check, printed not enforced, alongside
`precommit-precision-warn.sh`. *Costs:* the same hour. *Risks:* a warning that
nobody reads is what the existing provenance audits already are. *Commits to:*
nothing; reversible in one line.

**Option C — do nothing.** *Means:* the 17 stay repaired and the 18th is
unguarded. *Costs:* nothing today. *Risks:* the corpus has now executed this
exact regression once at scale, unattended; the `qou-aj91` reroute is still
recorded to be picked up cold, and each reroute is a producer re-run.
*Commits to:* re-doing the repair work when it happens again.

**The default if you say nothing is C** — the bean stays `todo`, the damage
stays repaired, and nothing is at risk *right now* because the migration
batches converged.

**My judgement, marked as judgement:** B. The measured harm was 17 files that
were fully recoverable from git, so the blast radius does not justify a blocking
gate that can red-line a sibling mid-sweep; but the class recurred twice under
two different beans without either noticing, which is what a warning at the
commit boundary would have surfaced. It is also the reversible one.

Bean stays `todo`, waiting on that call.
