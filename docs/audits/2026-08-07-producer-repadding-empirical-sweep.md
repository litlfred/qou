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
| **`RE_PADS`** | **37** | wrote a witness carrying padding |
| `CLEAN` | 8 | ran, wrote, zero padding |
| `EXIT_NONZERO` | 7 | could not run — **untested** |
| `TIMEOUT` | 1 | exceeded budget — **untested** |

**Of the 45 producers that could actually be measured, 37 (82%) re-pad.**
They regenerate **289 padded fields** in a single pass — roughly two-thirds
of the 439 the strip removed — and that is a *lower* bound, since 8
producers remain untested.

**A producer that dies partway can still have written padding first**, and
three do. The first cut of this sweep scored exit status *before* padding
and therefore filed them as untested, hiding 77 fields:

| producer | fields | how it ended |
|---|---:|---|
| `rho_k_co_casimir_extended` | **71** | wall timeout |
| `habiro_interpolate_cross_validator` | 4 | exit 2 |
| `rho_k_h3a_lp_dual` | 2 | exit 2 |

`rho_k_co_casimir_extended` is the single largest re-padder in the corpus.
The tool now ranks `RE_PADS` above the failure verdicts: padding written is
padding written, regardless of how the run terminated.

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
| wall timeout, wrote nothing | 1 | `su4_1111_markov_trace_probe` |
| `snappy` missing | 1 | |
| stale `folio-assistant` path (residual) | 1 | `option_e_multi_isotope_…` — a second missing input |
| `codata_constants` import | 1 | |
| deliberate q₀-pin guard | 1 | refuses to run off the muon pin — correct behaviour |

`rho_k_co_casimir_extended` was previously reported as a confirmed
re-padder, then reverted on the grounds that the sandbox lacked scipy so
the re-run was not comparable. scipy 1.17.1 — the version the original
witness was computed under — installs fine here (as do numpy and sympy),
so that confound is gone. It re-pads **71 fields**, the largest in the
corpus. The original observation was right and the revert was unnecessary.

Environment note for whoever picks this up: `pip install mpmath numpy
scipy sympy` all succeed in this sandbox. Earlier sessions recorded these
as unavailable and scoped work around that; it is worth re-testing rather
than inheriting. `pyhecke_native` and `snappy` genuinely do not install.

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

---

# Root cause found (same day): constants built at import time

The per-file judgment the sweep deferred turned out to have a single
systematic answer for the largest class, and it is **not** the mechanism
anyone was looking for.

A module-level constant

```python
B_AME = {"D": mp.mpf("2.22456607"), ...}
```

is constructed at **import time**, when `mp.dps` is still mpmath's default
**15** — about binary64. The value is rounded to ~53 bits *before*
`set_compute_dps()` ever runs, and raising dps afterwards cannot recover
what was already discarded. Serialized at 50 dps it prints the binary64
expansion:

```
2.2245660699999998399789546965621411800384521484375000000...
                    ^^^ dyadic tail — this IS float64 padding
```

**String-sourcing is necessary but not sufficient; the timing matters too.**
That is why `mpf_float_source_audit.py` passes these lines — `mpf("...")` is
precisely the compliant form it asks for — while they produce exactly the
defect the gate exists to prevent. It also explains why 5661 "compliant"
call sites were not the reassurance they looked like.

Reproduction:

| built | serialized at 50 dps | padded? |
|---|---|---|
| at `dps=15` (module import) | `2.224566069999999839978954696562141180038452148437500…` | **yes** |
| after `set_compute_dps()` | `2.224566070000000000000000000000000000000000000000000` | no |
| inside `workdps(50)` | `2.224566070000000000000000000000000000000000000000000…` | no |

The corpus already contains both correct forms — `codata_constants.
_ame_binding_mev` wraps construction in `workdps(max(50, dps))`, and 152
producers call `set_compute_dps()` at module level before their constants.
The clean sibling `binding_depth_stratified.py` reads `B_AME` from the
registry; the three that re-padded hand-typed the same numbers.

## The second defect this exposed: drifted experimental constants

The hand-typed values do not agree with the vendored AME2020 registry:

| isotope | hand-typed | AME2020 registry | rel. diff |
|---|---|---|---|
| D | 2.22456607 | 2.2245662 | 5.8e-08 |
| ³He | 7.7180428 | 7.71804132 | 1.9e-07 |
| ⁴He | 28.295674 | 28.2956624 | 4.1e-07 |

and the corpus carries **four mutually inconsistent hardcoded sets**
(`2.22456607` / `2.224566` / `2.22452` / registry) across 14 producers.
Same class as the CODATA-2018 `U_MEV` literal fixed in #4653: a constant
typed by hand once and left to drift while the registry moved.

Routing to the registry fixes both at once — four producers done
(`binding_depth_stratified_{lr,rust,knot_weighted,selfconj}`), verified
0 padded fields where there were 3/3/9. It **changes those probes' numbers
by up to 410 ppb**: a correction, not a regression, but a real behavioural
change, so witnesses are regenerated separately from the source fix.

## The gate — and why it is not CI-enabled yet

[`computations/mpf_import_time_dps_audit.py`](../../computations/mpf_import_time_dps_audit.py)
detects the class directly: build each module-level literal at `dps=15` and
again at `dps=60`; if they differ, precision was lost. Exactly-representable
values (`mpf(0)`, `mpf("0.5")`, dyadic tolerances) are not flagged.

**Correction to a number published earlier in this branch.** The first cut
of this gate reported *1485 sites / 497 files*. That was wrong, inflated
about 9x. `scan_file` was purely static: it flagged every module-scope
`mpf` literal regardless of whether precision had already been raised
earlier in the module — so it also flagged the 152 producers that do it
correctly, and it kept flagging the 14 files above *after* they were fixed.
That is how the error surfaced. The detector now walks module statements in
order and stops flagging once it sees a raise (`set_compute_dps()`,
`mp.dps = N`, `workdps`). Position is the whole point: a constant appearing
after the raise is built at full precision and is correct.

Corrected count: **164 sites across 63 witness-emitting scripts.**

Even corrected, these are **candidates, not confirmed defects** — a lossy
`mpf('0.3')` used as a plot bound, or a `1e-12` comparison tolerance,
misrepresents nothing; it is a defect only when the constant reaches a
witness as a claimed high-precision datum.
`habiro_interpolate_cross_validator`'s `AGREEMENT_RTOL = 1e-12` is flagged
and should **not** be "fixed" — that is the agent-confirm step, and the
residue is expected. So `--strict` stays out of CI until the real defects
are drained; a gate with a standing backlog is one everyone learns to
ignore, which is exactly the failure #4653 avoided by holding its own gate
at baseline zero. Draining precedes enforcement.

## Drain result (qou-qrsp)

Measured with the same tool, same worktree method, before and after:

| | before | after |
|---|---:|---:|
| `RE_PADS` | 38 | **20** |
| `CLEAN` | 8 | **25** |
| padded fields regenerated in one pass | 307 | **229** |

**18 producers fixed** — the whole import-time class. Two idioms were in
play and each file kept its own: nine `option_e`/probe files set
`mp.dps = 50` inside `main()`; three called `set_compute_dps()` there; four
`binding_depth_stratified_*` hand-typed AME constants now read from the
registry. In every case the module-scope constants above the raise were
being built at dps=15.

### What the residual 20 are — CORRECTED

**An earlier revision of this section was wrong and is retained here as a
correction rather than quietly edited away.** It claimed:

> Every remaining re-padder reads an upstream witness and faithfully
> reproduces the padding it finds there … the fix has to walk the witness
> dependency graph upstream-first.

That was inferred, not measured. The producers *do* read upstream
witnesses — that part is true — and the conclusion that the padding came
from there was never checked. It is false.

**The test.** Run each producer, take every padded string it writes, and
search all 1000+ committed witnesses for that exact string. If the digits
already exist upstream, the producer reproduced its input; if they appear
nowhere else, it minted them.

**Result: 20 of 20 came back `LOCAL` — `propagated = 0`.** Not one padded
value exists anywhere else in the corpus. The padding is generated in
place. `computations/producer_repad_sweep.py`'s companion classifier is the
tool; the discriminator is a substring search, not a judgement call.

A second over-generalisation followed and is also corrected here: having
found that `gt_matrix_pslq_probe`'s `PDG_G_A_ERR = mp.mpf(str(G_A_PDG_ERR))`
was the *same* import-time bug (module scope, before `mp.mp.dps = DPS` on
the next line — verified: at dps=15 that yields
`0.00129999999999999994032551242639…`, byte-identical to the witness; at
dps=50 it yields `0.0013`), the natural conclusion was that all 20 were.
Applying the fix mechanically found **1 of 20**. The other 18 have no
module-scope `mpf` before the raise at all.

**So the residual is not one class.** For the 18, float64 enters *during*
the computation, inside functions — e.g. `markov_stab_trace_axis_probe`
accumulates `tr_m_identity = mp.mpf(0)` over `contrib` terms built from
`y4[lam]`, and the sum inherits whatever precision those carry, landing on
`0.99999999999999999999999999999999…` where the identity trace is exactly
1. Each needs its own trace from the padded field back to where float64
enters. That is genuine per-file work and is not mechanizable.

**Lesson recorded, because it is the third time in this arc:** the pattern
is inferring a mechanism from one or two examples and generalising. It
produced the original "producers don't re-pad" retraction (4-producer
sample, 3 from the one clean family), the "upstream propagation" claim
(4 producers checked for *reading* witnesses, none checked for the values),
and this one. The fix each time was the same — build the discriminator and
run it over the whole set.

