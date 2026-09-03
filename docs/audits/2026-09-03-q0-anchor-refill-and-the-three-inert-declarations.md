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

## Three ways a q₀ declaration silently does nothing

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
grep -l 'WitnessBuilder' <producer>          # manifest route works
grep -l 'write_text\|json.dump' <producer>   # manifest is inert
```

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
