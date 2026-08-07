# Do the producers re-pad? — empirical sweep of the float64 strip

**Date:** 2026-08-07
**Branch / PR:** `claude/eightfold-way-a2-lattice-ijoegv` — [#4653](https://github.com/litlfred/qou/pull/4653)
**Bean:** `qou-gqt5` (DRAIN: 452 float64-padded witness values)
**Tool:** [`computations/producer_repad_sweep.py`](../../computations/producer_repad_sweep.py)
**Raw result:** `repad_result.json` (regenerable; the tool is the artifact, not the JSON)

## The question

Commit `4aa48b63` stripped float64 padding from 58 committed witnesses,
taking the audit count from 452 padded fields to 13. The strip is
provably value-preserving (`float(new) == float(old)`, asserted per
replacement). What it does **not** establish is whether the result is
**durable** — a witness is a *derived* artifact, so if its producer still
promotes a float to `mpf`, the padding returns on the next run and the
strip is cosmetic.

Three claims were made about this in sequence, none of them measured:

1. The stripper's own docstring asserted it as fact — *"a producer that
   still promotes a float to `mpf` will re-pad on its next run."*
2. That was then retracted after spot-checking 4 producers, and replaced
   with the opposite claim: *"most producers don't re-pad… the padding is
   largely historical."*
3. A single counterexample (`rho_k_co_casimir_extended`) was then found,
   leaving the scope genuinely unknown.

Claim 2 was drawn from a 4-producer sample, **3 of which were from the
`binding_*` family** — which turns out to be exactly where the clean cases
cluster. This sweep measures all 53 instead.

## Method

For each of the 53 distinct producers behind the 58 stripped witnesses,
in a **detached git worktree** (never the live tree — an earlier attempt
at this contaminated the real checkout):

1. reset to pristine post-strip state (`git checkout` + `git clean`)
2. content-hash every `*.witness.json`
3. run the producer with a wall timeout
4. re-hash — any witness whose content changed was *written by this producer*
5. score padded fields on each written witness, using
   `is_f64_padded` **copied verbatim** from the committed audit, so the
   sweep and the CI gate agree by construction
6. reset again, so collateral never accumulates

A producer is `CLEAN` only if it **ran, wrote a witness, and that witness
had zero padded fields**. A producer that could not run is reported as
untested — never as clean.

## Result

| verdict | producers | meaning |
|---|---:|---|
| **`RE_PADS`** | **34** | ran, wrote, regenerated padding |
| `CLEAN` | 8 | ran, wrote, zero padding |
| `EXIT_NONZERO` | 9 | could not run — **untested** |
| `TIMEOUT` | 2 | exceeded budget — **untested** |

**Of the 42 producers that could actually be measured, 34 (81%) re-pad.**
They regenerate **299 padded fields** in a single pass — roughly two-thirds
of the 439 the strip removed — and that is a *lower* bound, since 11
producers remain untested.

**Claim 1 was right; claim 2 was wrong.** The retraction was the error, and
the stripper's original docstring should stand. The `binding_*` family is
genuinely clean, which is why a `binding_*`-weighted sample read as
reassuring; the `qbeta_*` and `option_e_*` families re-pad heavily.

The eight genuinely clean producers:

```
binding_a3plus_joint_ji_combiner   meson_gen3_eta_phi
binding_block_multiplicative       probe_k_ud_bring_color_tube_empirical_baseline
binding_depth_stratified           probe_k_ud_fractional_and_alt_ansatz
qbeta_habiro_element_probe         su2_spinor_multiplicity_resolution
```

## What this means for the strip commit

The strip is **not durable**, and that has a sharper consequence than
"more work remains": the strip drains the ratchet baseline while leaving
the defect that produces the padding untouched. The gate reads green, the
producers still emit fake precision, and the next routine re-run silently
re-pads — with no signal, because the baseline now says the corpus is clean.

This is what bean `qou-gqt5` already prescribed — *"drain by fixing
producers to carry values as strings then re-running — never hand-edit,
never `--rebaseline` to go green"*. The strip is the hand-edit branch of
that instruction, made safe (value-preserving) but not made correct.
The producer fix is the load-bearing half and it has not been done.

## Root causes found

**The `mpf(<float-valued name>)` blind spot.** The source-level detector
added in `23075055` catches `mpf(<literal>)` and `mpf(float(...))` — what
is statically decidable — and its docstring states that limitation. The
live instance is `binding_factor_f_sequence.py:76`:

```python
return mpf(tf) - mpf(ta)      # tf, ta are floats
```

promoted, subtracted, serialized at 50 dps →
`0.595239597908215012367350027489…` for a datum that is
`0.595239597908215`. The documented gap is now demonstrated, not
hypothetical.

**A stale `folio-assistant/computations` path — 22 producers.** Eight of
the sixteen initial failures were not producer defects at all:

```python
repo_root = Path(__file__).resolve().parent.parent.parent   # = PARENT of the repo
fn = repo_root / "folio-assistant" / "computations" / "atom-chi-rust-t.witness.json"
```

`folio-assistant` carries **no `computations/` directory**, and
`folio-assistant/computations` **never existed** in qou's history, so this
path cannot resolve under any setup — cloning the platform repo does not
fix it. Sibling producers read the same witness correctly as
`HERE / "atom-chi-rust-{atom}.witness.json"`. Fixing the parent depth and
dropping the `folio-assistant` segment makes them run (verified, exit 0),
at which point **7 of the 8 re-pad**. 22 files carry the stale form;
tracked separately, since it is a migration-residue bug rather than a
precision one.

## Remaining untested, with cause

| cause | count | note |
|---|---:|---|
| `pyhecke_native` missing (no wheel) | 3 | bean `qou-dgkf` |
| wall timeout | 2 | `rho_k_co_casimir_extended`, `su4_1111_markov_trace_probe` |
| `snappy` missing | 1 | |
| stale `folio-assistant` path (residual) | 1 | different missing input |
| `codata_constants` import | 1 | |
| deliberate q₀-pin guard | 1 | refuses to run off the muon pin — correct behaviour |
| `mpf.__format__` TypeError | 1 | pre-existing |
| no stderr | 1 | |

`rho_k_co_casimir_extended` was previously reported as a confirmed
re-padder, then reverted because the sandbox lacked scipy and the re-run
was therefore not comparable. scipy 1.17.1 — the version the original
witness was computed under — installs fine here, so that confound is
removed; it now times out instead and remains **untested**.

## Scope of this finding

Scope-(a): this measures that most producers *do* re-pad and that the
strip alone does not hold. It does **not** establish what the correct
per-producer fix is. That requires a per-file judgment the sweep
deliberately does not make: whether a given quantity is *genuinely*
float64-precision (in which case promoting it to `mpf` and serializing at
50 dps is the dishonest step, and the fix is to stop promoting) or was
*downcast upstream* from a full-precision value (in which case the padding
is a symptom and the real defect is the lost precision). Picking wrong
either fakes precision or conceals a real loss, so it is not mechanizable.
