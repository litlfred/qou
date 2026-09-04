# The q₀-anchor refill, and three ways a declaration does nothing

*2026-09-03 — bean `qou-y98b`, PR #6537. Continues #6454, #6493.*

## What was measured

`computations/audits/q0_anchor_ratchet.py` reports the population it exists to
stop — witnesses newly arriving with no `q0Anchor`:

    unstamped witnesses (live scope) : 1626
    baseline                         : 1677
      drained since baseline         :   86
      NEW (not in baseline)          :   35   <- the refill

The 35 map to **34 producers**. One driver writes two of them
(`bpp_higher_a_resumable_driver.py`, whose `--neutron` flag flips a `label`
interpolated into the output filename), which is why a literal-name search
reports those two witnesses as orphans. **26 of the 34 hand-roll their
witness.**

### A scope correction

The prior session's ledger named the next tranche as "11 `wlambda_*`
producers". Measuring against the gate rather than against that filter:
**only 2 of the 35 are `wlambda_*`**. The other ~38 unstamped `wlambda`
witnesses are inside the tolerated baseline — real backlog, but not what
`--strict` fails on. The refill is a different family: `milnor-*` (6),
`probes/*` (14), and top-level binding / logratio / em-linking files.

## The classification, and the evidence for it

| verdict | producers |
|---|---|
| `independent` | 7 |
| `proton` | 27 |

Each `independent` rests on **two** checks, both required and neither
sufficient alone:

1. an **import-cone trace** — no `q_parameter` / `qou_substrate.constants`
   edge at any depth, with the witness emitter (`witness`, `witness_base`,
   `_precision`, `_path_bridge`) excluded so it does not mark every producer;
2. the new **`producer_baked_pin_audit.py`** — no q₀-*valued* literal in the
   source.

The witness payload was also checked for a q₀ field. The reason recorded on
each witness names that evidence rather than asserting the conclusion.

**A third, DYNAMIC check was added after #6519 pointed out that both of the
above are static** — a producer can be pin-dependent through what it computes
*with*, which neither a cone trace nor a source scan inspects. #6519 measured
that: two probes declaring themselves pin-independent whose own `_q0`-named
fields moved 428.7 ppb and 3.4 ppb under a re-pin.
[`computations/audits/q0_pin_flip_test.py`](../../computations/audits/q0_pin_flip_test.py)
forces a stem to the muon anchor, re-runs, and diffs the payload.
**Result: controls 2/2 moved, subjects 0/7 moved** — all seven `independent`
verdicts hold dynamically as well as statically.

Its own first run was **vacuous and reported the same conclusion**: the restore
between producers was `git checkout -- computations/`, and the manifest lives
under `computations/`, so the pin patch was reverted after the first producer
and everything after it ran unflipped. The second positive control caught it by
reading "no move" where it had to move; a single control would not have, since
`any(controls)` was already True. The gate is now `all(controls)`.

## Four ways a q₀ declaration silently does nothing

(Three found here; the fourth established independently on #6519 and
credited below. The document filename still says "three" — it is the
committed path and is left alone.)

The interesting result of this pass is not the 35. It is that **most of these
producers were already declared, and the declaration was inert.**

### 1. A manifest entry, for a hand-rolled producer — 18 producers

**22 of the 27 proton producers were already listed under `physical_proton`
in `computations/q0_anchor_manifest.json`, and their witnesses were unstamped
anyway.** 18 of those 22 hand-roll — `json.dumps` + `write_text` — and so
never enter `WitnessBuilder.build()`, which is where the manifest is read.

The ratchet's own header documents this mechanism. What was missing is how
much of the live refill it accounts for: **two-thirds**.

Consequence for triage: *"the stem is in the manifest"* is **not** evidence
that the witness is stamped, and a pass that treats it as done will skip
exactly the producers that need fixing. Check the write path first:

```sh
grep -l 'WitnessBuilder' <producer>          # manifest reaches the STAMP
grep -l 'write_text\|json.dump' <producer>   # manifest reaches the PIN only
```

**"Inert" is scoped to the STAMP, and the distinction is load-bearing — do NOT
read these entries as dead.** There are **two** steering mechanisms and they
have different reach:

1. **`q_parameter` steers the COMPUTATION by `sys.argv[0]`** — the entry point,
   whatever the producer's write path. So a hand-rolled producer listed in the
   manifest **does** evaluate at the pin the entry names.
2. **`WitnessBuilder.build()` reads the manifest to write the STAMP** — and
   only a producer that enters `build()` gets one.

So for a hand-rolled producer the entry is inert *for the stamp* and fully live
*for the pin*. Deleting it would silently change the q₀ the producer computes
at, which is a far worse defect than the missing stamp it was meant to fix.
`computations/audits/manifest_inert_entry_audit.py` makes the same point from
the other side, with the measurement: **"listed but never constructs a
WitnessBuilder" is 176 producers, and that is NOT a count of inert entries** —
which is exactly why that audit reports only the deprecated-source and
missing-source classes as findings.

The manifest entries are left in place — they state the pin correctly — and
the declaration is added producer-side, the only route that reaches the file.

### 2. The right value under the wrong key — 17 witnesses

`bpp_higher_a_resumable_driver.py` writes `"q0_anchor": "physical_proton"`
into its witness. The audits read **`q0Anchor`**. The declaration is present,
correct, deliberate — and invisible.

Measured on `origin/main` — 3469 tracked witnesses, 2002 unstamped —
**17 are unstamped while carrying a near-miss key**: 12 `q0_anchor`,
1 `anchor`, 4 `q0_pin`. A further 12 carry a variant *alongside* a correct
`q0Anchor`, which is harmless duplication.

This is a **small** class, not a large one, and is reported as such. **This
branch fixes 11 of the 17** as a side effect of the anchor declarations,
leaving 6 (5 `q0_anchor`, 1 `anchor`).

> **🛑 Both figures in this section were wrong when first written, by the
> error this whole document is about.** It read *"14 ... Four of the 14 are
> in this refill"*. Neither number was measured against a fixed baseline:
> the count was taken **mid-session, against the working tree this branch
> was itself mutating**, so declarations that had already landed had
> silently removed their own witnesses from the population being counted.
> Re-measured with `git show origin/main:<witness>` — a baseline the sweep
> cannot write to — the before-count is **17** and the number fixed here is
> **11**, not 4.
>
> This is the same defect AGENTS.md records for the witness-staleness
> sweep: *"baseline from git, never from a tree your own sweep writes to."*
> I had that rule in front of me and still measured against the live tree.
> The `q0_pin` sub-count is the tell — I recorded 1 where there were 4,
> because three had already been fixed by my own earlier commits.
>
> Corrected in the same PR; the earlier commit message
> (`audit(qou-y98b): the refill, and three ways...`) still carries the wrong
> figure and cannot be rewritten after pushing.

### 3. An `ambiguous` entry in the manifest

Already documented (bean `qou-fl0a`): `build()` writes the stamp only
`if _a in ("muon", "proton")`, so an `ambiguous` manifest entry resolves
correctly and is then discarded. Not encountered in this refill; listed so the
three are in one place.

### 4. A `physical_proton` entry is not what stamps `proton` (from #6519)

Established independently by the sibling working #6519 (`qou-9ugp`) and
reported on this PR, from the opposite direction to the three above. They wrote
that a witness stamps `proton` *because* its stem is in `physical_proton`, then
tested it by **removing the stem from two producers and re-running** — both
still stamped `proton`.

`q_parameter` branches only on `ideal_muon`
(`if _stem in _man.get("ideal_muon", []): ... else: proton`), so
`physical_proton` membership is a **declaration of intent that no code reads**.
Anything not listed under `ideal_muon` resolves to proton by default.

This is distinct from mechanism 1, and sharper in one respect. Mechanism 1 says
a manifest entry cannot stamp a *hand-rolled* producer, because the manifest is
read inside `build()`. Mechanism 4 says that even where the stamp *does* land,
the `physical_proton` entry is not what caused it. So a `physical_proton` entry
is never evidence of anything by itself: on a `WitnessBuilder` producer the
default would have stamped proton anyway, and on a hand-rolled one it does
nothing at all.

The practical consequence for triage: **`ideal_muon` membership is the only
manifest fact with behaviour attached.** Read `physical_proton` as
documentation.

## The new audit, and the two bugs in it

`computations/audits/producer_baked_pin_audit.py` decides whether a producer
bakes a q₀ pin **by value, not by spelling** — it parses the source and
evaluates every numeric literal and 1-/2-argument
`Rational`/`Fraction`/`mpf`/`Decimal` call to an exact `Fraction`.

It exists because the import-cone trace's own docstring records the case it
cannot see:

```python
sp.Rational("2584370278640139188197914756009",
            "2328306436538696289062500000000")   # = 1.1099785827513805...
```

A `1.1099785` prefix match sees a decimal and nothing else. **A hardcoded pin
need not look like the pin.**

Two defects in the first draft, both worth keeping on the record.

**Four anchors, not two.** Three different numbers are all called "the muon
q₀" — the retired self-certified pin, and the lepton-tower derivation at
CODATA 2018 and at CODATA 2022 (the live canonical one). They diverge at the
13th significant digit.

**One tolerance cannot serve separations four orders of magnitude apart.**

| separation | relative |
|---|---|
| proton vs any muon | 1.16e-8 |
| muon-retired vs muon-codata2022 | 7.7e-11 |
| muon-retired vs muon-codata2018 | 2.8e-12 |

The draft used a single **1e-6** window — ~100× the proton/muon gap. It did
**not** blur the answer; it silently returned the first candidate, and
reported the **retired muon pin as `proton` on 21 lines of one file.** The
general form is worth more than the instance: *a tolerance looser than the
separation it is meant to resolve does not produce an uncertain answer, it
produces a confident wrong one.*

Now three tiered windows; a value matching more than one anchor is reported
`ambiguous`, never guessed; a vintage is resolved only when the digits present
support it. A pin truncated to 8 significant digits is `1.1099785...`, a
prefix of every anchor, and is genuinely unattributable.

`--selftest` covers seven value-level invariants plus three file cases and
exits non-zero on any miss, so a later narrowing cannot quietly report a clean
tree the way the spelling-keyed check did.

### A verdict is not a diagnosis

Two of the 27 proton producers flag `BAKED_PIN`, and **neither bakes a pin**.
`alpha_scale_is_outside_the_trace_probe` and
`extensive_carrier_scale_inversion_probe` carry `1.10997858` inside a

```python
Q_50_DIGIT_STR.startswith("1.10997858")
```

**guard** asserting the proton anchor, added by a Copilot review on #6443. The
audit is right that a q₀ value is in the source; its verdict does not
distinguish a pin from a guard. Read as a pin, these two would have been
mislabelled — when in fact they self-assert the correct anchor, which is
stronger evidence than either audit supplies.

## Corpus baseline: baked pins by anchor

    python3 computations/audits/producer_baked_pin_audit.py --all --quiet

**369 of 4387 files** bake a q₀ pin:

| files | anchor |
|---|---|
| 196 | proton |
| **174** | **muon-retired** (retired 2026-08-22) |
| 46 | muon-codata2018 |
| 39 | muon (vintage unresolvable from the digits present) |
| 29 | ambiguous:truncated |
| 7 | muon-codata2022 — the **live** canonical anchor |

`muon-retired` concentrates in `computations/probes` (42), `qbeta` (31),
`deltalambda` (23).

**This is the producer-source surface.** It is a *different population* from
the ~40 witness **files** carrying the same string that AGENTS.md records, and
it has not been measured this way before. Do not fold the two counts together.
Nothing here is drained by this PR; it is a baseline, and the retired-pin
migration is scoped under `qou-3f7a` / `qou-tekx`.

## Method notes

Every producer was re-run **from its own directory** and **with the arguments
its committed witness records**. Both matter, and both have cost time before:

- run from the repo root, a CWD-relative `open(...,'w')` writes a stray
  witness at the root and leaves the real one untouched — which reads as
  "the producer did not stamp";
- run without its argument, `wlambda_covariance_epic_M1_edge_ratio_decomposition`
  defaults to `nmax=40` while its committed witness records **46**. The
  default run both failed an assertion and rewrote the witness with a shorter
  table. That output was discarded and the producer re-run correctly.

Diffs were checked stamp-only against `HEAD` with volatile provenance masked
(`computedAt`, `commitSha`, `scriptHash`, `scriptCommitSha`, `durationMs`,
`ms`, `pyhecke_native_build`) and prose timings normalised, since a figure
like `built 3.21s` formatted into an assertion message reads as a moved value.

## Not fixed, and why

- **Three producers cannot complete in a 900 s budget** —
  `all_nuclides_sdp_admissibility_mp`, `symbolic_nf_q_degree_magic_probe`,
  `tower_walk_magic_replication_probe`. These are long-computes, not stamping
  problems; all three are declared and will stamp whenever they next run.
- **Four witnesses are BLOCKED on a compute this environment cannot finish** —
  `bnn-higher-a-resumable`, `bpp-higher-a-resumable`, `chain-binding-closed-form`
  and `logratio-exactly-extensive`. Measured, not assumed; see the section
  below.
- **`bnn-higher-a-resumable.witness.json` carries the wrong description.**
  The driver interpolates `label` into the filename, the banner and the
  `species` field, but its `description` is a hardcoded string reading
  *"B_pp(A) for the pure-proton chain"*. So the pure-**neutron** witness
  describes the pure-proton computation. The data is correct; only the prose
  is. Reported rather than fixed here, because fixing it means a ~49-minute
  re-run per label and this PR's scope is the anchor.

## Verification

There is no CI to cite (`build.yml` is `workflow_dispatch`-only), so what was
actually run: `producer_baked_pin_audit.py --selftest` exit 0 (10/10); the
`--all` sweep completes over 4387 files; every regenerated witness diffed
stamp-only against `HEAD` under the mask above; `q0_anchor_ratchet.py` and
`witness_raw_float64_audit.py` re-run and reported on the PR.


## The four that did not land, and why the relaunch loop was stopped

Two of the four (`chain_binding_closed_form_probe`,
`logratio_exactly_extensive_probe`) **refuse by design** until
`bpp_higher_a_resumable_driver` has banked its checkpoint — announced on
stdout, exactly the guard behaviour AGENTS.md describes, not a defect. The
other two are that driver's own output.

The driver is checkpointed per completed partition and resumes cleanly. It was
relaunched four times. **It cannot finish in this environment**, and the reason
is the session-suspension cadence rather than the mathematics:

| launch | last write | window | banked |
|---|---|---|---|
| 23:03:00 | 23:10:30 | ~7.5 min | 1 `off` partition |
| 00:00:00 | 00:01:54 | ~1.9 min | A=2,3,4 (the cheap ones) |
| 00:46:02 | 00:47:40 | ~1.6 min | **nothing** |

The driver dies whenever the session suspends, and the windows have been
shortening. Two fixed costs decide it:

* the in-memory partition cache is **not** checkpointed and takes a measured
  **103 s** to rebuild on every launch;
* only a **completed** partition is banked, and the remaining A=5 `off`
  partitions run to ~543 s each at dim 2002 (measured on the `on` half).

The last window was **98 s against a 103 s rebuild** — zero seconds reached any
partition. A process that cannot outlive its own warm-up banks nothing, so
further relaunching would spend check-ins without moving the count. The loop
was stopped on that evidence rather than run indefinitely.

**Progress that did land**, and which survives in the checkpoint for whoever
resumes this on a machine that stays up: A=2, 3 and 4 are complete on both
halves, and A=5 `on` is complete (8 of 8). What remains is 7 A=5 `off`
partitions for the `pp` label, then the whole `nn` label, which has nothing
banked. The checkpoint is gitignored and is scratch, so that progress is local
to the machine that made it.

**Do not "fix" this by shortening the run.** The runner must pass `2 3 4 5`
(and `2 3 4 5 --neutron`). The driver reads
`A_LIST = [int(x) for x in args] or [5]`; both committed witnesses record
`by_A = {2,3,4,5}`; and `chain_binding_closed_form_probe` needs at least three
distinct A per species (`if len(As) < 3: continue`). A single-A run would
regenerate both witnesses with three A values dropped — **a regression wearing
the shape of a stamp**. That invocation was live in the runner for four
launches before it was caught, and it is the same class as the
`nmax=40`-vs-`46` trap recorded above: *a producer's argument list is part of
what its committed witness records, and re-running without it truncates the
result silently.*
