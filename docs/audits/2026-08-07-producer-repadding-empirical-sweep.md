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

---

# The residual measured at the source — and it is three classes, not one

**Tool:** [`computations/float64_entry_tracer.py`](../../computations/float64_entry_tracer.py)
(12-case `--self-test`)

The section above closed by declaring the residual "genuine per-file work
and … not mechanizable", on the strength of **one** example
(`markov_stab_trace_axis_probe`). That is the same one-example generalisation
the paragraph directly above it warns about — the fourth in the arc. Measured,
it is wrong twice over: the localization **is** mechanizable, and the residual
is not one class.

mpmath funnels every `float -> mpf` conversion through `from_float` /
`from_npfloat`. Patching those records the source line where a float64 enters,
so the entry point is *read off* rather than reasoned about.

## Re-measurement first

Re-running the sweep at `14865d3d`: **`RE_PADS` 19, `CLEAN` 26, 228 fields** —
the previous 20/229 minus exactly the one `gt_matrix_pslq_probe` fix, which
independently confirms that fix landed. ("The other 18" was arithmetic
slippage; 20 − 1 = 19.)

**All 19 are measured**, including `rho_k_co_casimir_extended`, which had
defeated every earlier attempt (see "the two coverage limits" below).

| class | producers | fields | mechanism |
|---|---:|---:|---|
| **A — float64 genuinely enters** | 10 | 189 | a located source line |
| **B — no float64 enters at all** | 9 | 39 | see below; not one thing |

## Class A: located, and it clusters

Not nine independent investigations — three idioms:

**A shared downcast in a library**, `computations/hecke/hecke_characters.py:214`:

```python
b = float(mp.sqrt(abs(b_sq)))
```

reached **527 310** times by `su4_1111_markov_trace_probe`, 11 868 by
`chirality_avg_content_atomic`, 4 by `chirality_avg_content_chiral`. One line,
three producers.

**`mpf(<float-valued dict entry>)`** — four producers promote a float pulled
out of a dict:
`v_hat_to_delta_lambda_bridge.py:125-127,152-153`, `xi_ell_phi_q_probe.py:181`,
`phi_q_spectral_combiner_probe.py:107,109`, `rho_k_h3a_lp_dual.py:403,420`.

**Correction — these were called "`mpf(<float out of JSON>)`" here, and only
half of them are.** The line shape is the same, but the float's *origin*
differs, and that decides the fix:

| producer | where the float comes from | fix belongs |
|---|---|---|
| `phi_q_spectral_combiner_probe` | upstream witness via `builder.add_upstream()` | **upstream** |
| `rho_k_h3a_lp_dual` | `json.loads` of an occam blob | **upstream** |
| `v_hat_to_delta_lambda_bridge` | `wedderburn_pair_volumes()`, in-memory | here |
| `xi_ell_phi_q_probe` | `per_generator_V_hat_general()`, in-memory | here |

Where the value arrives from a **committed witness**, the precision was lost
when *that* witness was written, and promoting it here only makes the loss
visible — the fix is upstream and the ordering matters, which is the one place
the original "upstream propagation" reading was pointing at something real.
Where it comes from an **in-memory helper**, the helper computes in float and
the choice is the usual one: make it compute in mpmath, or accept that the
quantity is f64 and serialize it as such.

Grouping them by the look of the call site rather than by the origin of the
value is the same shortcut this document keeps recording. It was caught here
before any of the four was "fixed" on the strength of it.

**`mpf(<float-valued name>)`** — including
`binding_factor_f_sequence.py:76`, the instance this document already
documented as live and unreachable by the static detector. It is reachable
here, which is the tracer's calibration case.

**The largest is deliberate, and the fix is the other one.** The 71 fields of
`chirality_avg_content_atomic` all come from line 201, `mpf(chi_val_f64)`,
fed by a Rust kernel invoked as `precision="f64"` under a comment reading
*"53-bit precision still"* — and the witness itself records
`"kernel_precision": "f64"`. The quantity **is** float64. So the defect is not
lost precision to recover; it is serializing 53 bits at 50 dps, contradicting
the witness's own declaration. Per the scope note above, that is the
"genuinely float64 ⇒ stop promoting / serialize at true precision" branch.

**Expected residue, not a defect:** `bring_homology_pairing_integration.py:89`
and `:122` are the comparison tolerances `1e-45` and `1e-10`. Like
`AGREEMENT_RTOL`, they must not be "fixed".

### The 71-field producer, finally measured

`rho_k_co_casimir_extended` is the corpus's largest re-padder and had never
been measured by any tool here — it outran the sweep's 150 s, a 240 s
provenance run and a 900 s trace. It is **one line**:

```python
# computations/hoefsmit_numpy.py:161
return mp.mpf(float(np.trace(M)))     # x148, sample 1.5597586581034242
```

The function accumulates `M` through numpy matmul at C-level BLAS, so the
trace is f64 by construction — the same shape as `chirality`: a deliberately
f64 kernel whose result is promoted and then serialized at 50 dps. That makes
**three** library-level entry points behind Class A (`hecke_characters.py:214`,
the JSON-read idiom, `hoefsmit_numpy.py:161`), not ten producer-specific bugs.

### The two coverage limits that had hidden it

Both were in the tracer, and both are now flags rather than silent bias.

**Forked workers are invisible.** `rho_k_co_casimir_extended` computes χ^λ
inside a `multiprocessing.Pool`; children inherit the patches but keep their
own counters, which die with them. Its earlier `repo_sites = 0` was
meaningless — the work happened where the instrument was not. `--no-fork`
reports `cpu_count() == 1` so the producer takes its serial path. Numerics
unchanged; only the scheduling is.

**Attribution is what made it slow, not the physics.** Walking the stack per
padding-prone conversion costs more than the computation on a producer doing
~5e5 of them. `--budget N` removes the patches once spent, restoring native
speed. With both flags the producer ran to completion, un-truncated, in ~20
minutes.

Both failures are one-directional — they hide entry sites, never invent them —
so a non-empty result stands alone, while a zero is only meaningful when
`truncated` is false and the producer does not fork. That asymmetry is why the
earlier zero for this producer should never have been read as Class B, and the
report now carries `truncated` and `no_fork` so it cannot be.

## Class B: no float64 enters — and the detector cannot see this

Nine producers convert no repo float64 at all; their only padding-prone
conversions are mpmath's own heuristic constants (`functions/zeta.py:483`,
`if abs(z) >= 1.4`, reached through `clsin`).

Their flagged values are genuine high-precision computations of quantities
that are **exactly integers**:

| producer | field | value | truth |
|---|---|---|---|
| `markov_stab_trace_axis_probe` | `tr_M_identity_H4_at_q0` | `0.999…99863` | 1 |
| `gap_a4_T11_klein_J_invariant_probe` | `f_leading_ratio` | `1.000…0001` | 1 |
| `gap_a4_T6_q_deformed_icosahedral_probe` | `…[4].h2` | `10.000…000323` | 10 |

`is_f64_padded` flags a string whose relative distance to the nearest binary64
is under `1e-30`. A value that is *mathematically* 1 and lands 1.4e-51 short
by rounding sits that close to `1.0` — so it is flagged, though no float64 was
ever involved. **The threshold cannot separate the two cases**, because a
padded value truncated at 50 dps is also non-zero distance:

| string | rel. distance to nearest f64 | flagged |
|---|---|---|
| `mpf(0.1)` printed at 55 dps | `0.0` | yes — really is padding |
| `mpf(0.1)` printed at 50 dps | `1.56e-50` | yes — really is padding |
| `tr_M(1)`, genuinely computed | `1.37e-51` | yes — **not** padding |

This is a limit of any *static* test, not a bug in the detector: the string
genuinely does not carry the answer. Only the source does. So some fraction of
the residual is **not the defect** — and hunting for a float64 entry in those
producers is looking for something that is not there.

## `propagated = 0` — a retracted refutation, and what is actually true

**An earlier revision of this section claimed `propagated = 0` was refuted.
That claim was wrong and is retracted here rather than deleted.** It said the
padded string

```
0.024180175767745112208606528270138369407504796981812
```

regenerated by `qbeta_markov_trace_compute_accuracy_diagnostic`, was committed
verbatim in `qbeta/qbeta-markov-trace-norm-probe.witness.json`. It is not. The
committed witness holds only the short form `0.024180175767745112`.

The padded string was found in a **worktree contaminated by this session's own
runs**: `qbeta_markov_trace_norm_probe` is itself one of the 19, it had just
been re-run there, and its regenerated output was left on disk. Grepping that
tree found this session's output and reported it as upstream evidence. It is
the failure `producer_repad_sweep.py`'s docstring warns about in capitals —
*never point this at a tree you have been running producers in* — committed by
the same session that was cataloguing the arc's habit of generalising from
unverified evidence. Checked against `git show HEAD:…`, the claim evaporates.

**So the exact-string `LOCAL` verdict stands.** What does not stand is treating
it as the whole answer, and that criticism survives the retraction:

> the strip removed padding from upstream witnesses, so an exact-string search
> over the post-strip corpus cannot see value-level inheritance.

That is now measured rather than argued.
[`computations/witness_padding_provenance.py`](../../computations/witness_padding_provenance.py)
asks provenance twice — is the padded **string** upstream (`VERBATIM_UPSTREAM`),
or is the same float64 **value** upstream in some other spelling
(`VALUE_UPSTREAM`) — and excludes the producer's own fresh output from its own
lookup, which is the guard the retracted check lacked.

On the qbeta case the two answers differ, which is the entire point:

| question | answer |
|---|---|
| padded string committed elsewhere? | **no** — hence `LOCAL` |
| same float64 value committed elsewhere? | **yes**, `qbeta-markov-trace-norm-probe.witness.json` |

Run over all 19 re-padders, **218 padded fields**:

| verdict | fields | |
|---|---:|---|
| `VERBATIM_UPSTREAM` | **0** | the exact-string result is **confirmed** |
| `VALUE_UPSTREAM` (distinctive) | **37** | value upstream, invisible to a string search |
| `VALUE_UPSTREAM_ROUND` | 15 | matched `1.0`/`6.0` — **vacuous** |
| `LOCAL` | 166 | minted here |

So `propagated = 0` is right about strings and **17 % short** about values. The
round-number split matters: without it the `gap_a4` near-integers would have
read as inherited purely because `1.0` is everywhere in the corpus — a
near-vacuous match dressed as evidence, which is how this section went wrong
the first time.

**The two tools agree, and were built independently.** Where
`float64_entry_tracer` finds a local float64 entry, provenance says `LOCAL`
(`chirality_avg_content_atomic` 71/71, `binding_factor_f_sequence` 2/2); where
it finds none, the value is upstream (`qbeta_markov_trace_compute_accuracy_
diagnostic` 7/7, `phi_q_spectral_combiner_probe` 6/6). That cross-check is
worth more than either result alone: Class B producers do not mint padding,
which is consistent with their carrying no float64 entry to mint it with.

**The classifier behind the original claim is still not in the repository**, so
that result remains unreproducible; the tool above is committed so this one
does not repeat that.

## First Class A fix: the 71-field producer

`chirality_avg_content_atomic` is the largest re-padder in the corpus and all
71 of its fields are the same one, `per_partition[].chi_lambda_beta`, written
as `str(<mpf>)`. The mpf promotion is correct — the downstream arithmetic needs
it — but serializing *that* prints 50 dps of a 53-bit number.

The repo already had the convention. `fmt()`'s own docstring calls out "no
spurious mpf-promotion noise on a 0.1-style float" and short-circuits floats to
their natural repr, so the fix is `fmt(float(chi_val))`. `mpf(float)` is exact,
so `float()` recovers the kernel's own value — value-preserving by
construction, not by assertion.

Measured before and after in a detached worktree:

| | before | after |
|---|---:|---:|
| chi fields | 71 | 71 |
| **values moved** | — | **0** |
| **padded fields** | **71** | **0** |

```
1.2320524541667656759358351337141357362270355224609375
                              -> 1.2320524541667657        (float-equal)
```

This is the durable form of what the strip did by hand: 71 of the residual 228
fields, fixed at the producer.

## Second Class A fix — and the residual 228 is a lower bound

`rho_k_co_casimir_extended` is the other 71-field producer. **It is not 71.**
A run that completes writes **148** padded `chi_lambda_at_q0` fields; the
sweep's 71 came from a run that hit the 150 s wall and left a *partial*
witness, and that number was carried forward as though complete.

The sweep is careful that "untested is not clean". This is the neighbouring
error — **half-tested is not measured** — and it means **228 is a floor**, at
least 77 short on this producer alone. Two more (`habiro_interpolate_cross_
validator`, `rho_k_h3a_lp_dual`) also exited non-zero mid-run, so their counts
are lower bounds too.

148 is also exactly what the tracer recorded at `hoefsmit_numpy.py:161` —
`x148` conversions, one per field.

**The chirality fix does not transfer.** `_chi_worker` has two paths:

```python
try:    from hoefsmit_numpy import chi_numpy   # numpy f64 kernel
except ImportError:  chi_numeric               # full mpmath precision
```

so χ is 53-bit only when numpy is importable. Writing `float()` unconditionally
would discard real digits in the fallback — the *"conceals a real loss"* half of
the trap this document warns about, where the f64 path is the *"fakes
precision"* half. The same one-line fix would have been wrong here.

So the decision is made **per value, exactly**: an mpf equal to its own float64
holds 53 bits and nothing more; one that is not carries more and is written in
full. A genuine high-precision value that happens to be representable loses
nothing either — the short form is then exact — so the test cannot misfire in
that direction.

| | before | after |
|---|---:|---:|
| chi fields | 148 | 148 |
| **values moved** | — | **0** |
| **padded fields** | **148** | **0** |

Both runs completed (`rc=0`, no timeout), so unlike the sweep's figures these
counts are complete. **219 fields now fixed at the producer** across the two.

## The `mpf(<float-valued name>)` instance — and it goes the other way

`binding_factor_f_sequence.py:76` is the case this document names above as the
detector's live blind spot. Closing it turns out to need the **opposite** fix
from the six before it.

Those found a value that genuinely held 53 bits and stopped printing 50 dps of
it. Here the input is a decimal **string** from `binding_canonical`, written
with `mp.nstr(..., mp.dps)`, and builtin `complex()` reads it as binary64 —
wrong in both regimes the field appears in:

- a 16-digit string becomes the double whose exact value is
  `0.98352601518469637…`; subtracting two of those and printing at 50 dps gives
  `0.595239597908215012367350027489` for a datum that is `0.595239597908215` —
  the number named above;
- some producers write ~30 digits into `tr_M_free`, and `complex()` discards
  everything past the 17th. The corpus carries **both** populations.

`mpmathify` parses a decimal as a decimal, faithful in both. The expectation
going in was that it would *recover* precision; measured, the runtime string is
16 digits and there is none to recover. Right fix, wrong reason — worth
recording, because "downcast upstream" and "genuinely f64" are the two branches
the scope note above says must not be confused, and this case reads like the
first while behaving like neither.

**This one moves a number**, unlike the six before it:

| | |
|---|---|
| padded | 2 → **0** |
| values moved | **1 of 34** compared |
| `rows[4].delta_tr` | `1.00105419197756849783442767432` → `1.00105419197756854` |
| | 4.2e-17 relative — **exactly 1 ulp** |

One ulp is the width of the binary64 rounding that should never have been
introduced, so it is a correction. Source only; the witness is regenerated
separately *because* a number moves.

## A fourth mechanism: `mp.dps = 50` that does nothing

`bring_homology_pairing_integration.py` was flagged for 4 padded fields. All
three sites the tracer reported there are red herrings — `1e-45` and `1e-10`
are comparison tolerances that must not be touched, and the third is a float
mpmath computes inside `mp.quad`, which the lexical origin rule files as repo
because it is not a literal in mpmath's source. The defect was on **line 7**:

```python
import mpmath as mp
mp.dps = 50          # sets an attribute on the MODULE — a no-op
```

Precision lives on the *context*, so under this alias the line has to read
`mp.mp.dps = 50`. The no-op had been silently in effect: everything was
computed at mpmath's default ~53 bits and written with `mp.nstr(..., 40)`, so
the witness claimed 40 digits and carried 16.

This is a **fourth distinct mechanism** — not a serialization choice like the
six before it, and not a bad parse like `binding_factor`: the precision was
never raised at all.

It is worth more than its 4 fields. The producer integrates the Euler class
over the Bring fundamental cycle and asserts the result matches the closed
forms. At 15 digits it agreed to ~15; at 50, all four match to every digit
written:

| field | value | equals |
|---|---|---|
| `computed_triangle_area` | `0.1570796326794896619231321691639751442099` | π/20 |
| `computed_total_area` | `37.69911184307751886155172059935403461037` | 12π |
| `pairing_ratio` | `0.2122065907891937810251783511633524827126` | 2/(3π) |
| `target_ratio` | same | 2/(3π) |

`|ratio − target|` goes from 6.94e-16 to **exactly 0** at 40 digits, against an
assertion tolerance of `1e-10` — loose enough to have hidden the shortfall
indefinitely. Values move ~3.2e-15 relative, which is the 15-vs-50 digit gap:
a correction.

### The same no-op is in four more producers — now fixed and verified

Swept the corpus for `import mpmath as <alias>` paired with a bare
`<alias>.dps =`:

```
computations/qbeta/h5_wedderburn_tension_hp.py:11
computations/qbeta/qbeta_h4_em_normalization_probe.py:11
computations/qbeta/qbeta_h4_sign_block_exact.py:11
computations/qbeta/qbeta_h4_sign_block_proof_search.py:11
```

All four said `mp.dps = 50` and ran at 15. **None is in the 19 re-padders** —
they were never in the stripped-witness cohort, so the padding sweep never
reached them.

They were first recorded here as found-but-unverified, because they died on
`ModuleNotFoundError: qou_substrate` — they import it directly rather than
through `_path_bridge`. **That was the container, not the producers.** With
`PYTHONPATH=tools/qou-substrate/python` all four run clean. Filing them as
unrunnable would have been wrong, and only trying it settled that; "cannot run
here" deserves the same suspicion this document gives "untested is not clean".

Verified before/after — all four `rc=0` both ways, and all four change output,
so the no-op was live in every one (26, 34, 12 and 14 lines respectively).
The change is recovered precision, not moved results: every value agrees to
the 15 digits it used to print and then continues.

```
q0 (anchor) = 1.10997858275138
           -> 1.1099785827513808075916690956107688798744991218736
```

— which is exactly `q_parameter.Q_50_DIGIT_STR`, so the anchor is now the
canonical pin rather than a 15-digit truncation of it.

**Scope:** none of the four emits a witness, so this adds no padded fields and
does not move the drain count. What it means is that any conclusion drawn from
their output beyond 15 digits was unsound — these probes print ratios and
compare them against exact predictions.

### The no-op class is invisible to the padding gate

Completing the sweep found **seven** instances in total, and two more only
because the first pass matched `^import mpmath as <alias>` at module scope
while these sit indented inside a `try:`:

```
computations/bring_homology_pairing_integration.py:7     emits a witness — 4 padded
computations/e_hartree_round22_arch_bridge.py:69         emits a witness — 0 padded
computations/e_hartree_round23_normalization.py:68       emits a witness — 0 padded
computations/qbeta/h5_wedderburn_tension_hp.py:11        no witness
computations/qbeta/qbeta_h4_em_normalization_probe.py:11 no witness
computations/qbeta/qbeta_h4_sign_block_exact.py:11       no witness
computations/qbeta/qbeta_h4_sign_block_proof_search.py:11 no witness
```

**Only one of the seven produced padding.** The other six were invisible, and
could not have been otherwise: at `dps=15` a plain `str(<mpf>)` prints ~15
digits, and `is_f64_padded` requires ≥20 fractional digits before it looks at a
value at all. The no-op hides itself from the audit that would catch it.
`bring_homology` surfaced only because it writes `mp.nstr(..., 40)`, forcing 40
digits out of a 15-digit value.

So the two defects are near-orthogonal:

| | claim | detectable by |
|---|---|---|
| float64 padding | value claims **more** precision than it has | `witness_float64_padding_audit` |
| `mp.dps` no-op | value silently carries **less** than asked for | nothing, today |

The corpus has been swept exhaustively for the first and never for the second.
The detector is static and cheap — for every alias binding the mpmath
**module** (not `from mpmath import mp`, where `mp` is the context), a bare
`<alias>.dps = …` is always a no-op:

```python
aliases = re.findall(r"^\s*import\s+mpmath(?:\s+as\s+(\w+))?\s*$", src, re.M)
#   then flag:  ^\s*<alias>\.dps\s*=
```

Two cautions from running it: match indented imports (two of the seven are
inside `try:`), and skip docstrings — `qbeta_5two_phi_series_engine_probe.py`
mentions "at mp.dps = 60" in prose and is a false positive.

## Regenerating a witness silently drops its q₀ provenance

**Source fix committed, witness NOT regenerated — and the reason generalises
well beyond this producer.** Re-running `chirality_avg_content_atomic` and
diffing against the committed witness:

```diff
-  "q0Anchor": "proton",
-  "q0Value": "1.1099785827513808075916690956107688798744991218736"
```

Every chi value is byte-identical and no number moves; the run just **loses
both q₀-pin fields**. That pin exists so a muon/proton value "can never be
silently misread" (bean `tnjb`), and
`computations/audits/q0_anchor_consistency_audit.py` enforces it.

**Diagnosed — and it is not a bug in `build()`.** The `q0Anchor` code is inside
`stamp_staleness_metadata()`, a **separate method a producer must call
explicitly**. `build()` never touches the pin. Across the corpus:

| | witnesses |
|---|---:|
| no q₀ pin at all | 2104 |
| pin + producer stamps it (safe) | 36 |
| **pin + producer does NOT stamp** | **557** |
| unresolved | 3 |

**557 of the 596 pinned witnesses (93 %) carry a pin their own producer cannot
reproduce** — backfilled once, and dropped by the next re-run. Five of the 19
re-padders are in that set, including `chirality_avg_content_atomic` and
`rho_k_co_casimir_extended`, the two 71-field producers.

`save()` already loads the on-disk witness for its drift check, so the fix
carries a recorded pin forward there — **preserve only**. A witness with no pin
still gets none: inventing `"proton"` for the 2104 unpinned would assert a pin
no producer established, and `Q0_ANCHOR_MISSING` is a tolerated state. Two
regression tests, the first checked to *fail* without the fix rather than only
to pass with it.

Re-running chirality now keeps `q0Anchor`/`q0Value`, and its diff reduces to
`commitSha`/`computedAt`/`durationMs`/`scriptHash`/`scriptCommitSha` — ephemeral
only, nothing substantive, so the witness stays uncommitted. **Regeneration is
no longer lossy**, which unblocks the drain plan's second half.

## End-to-end re-measurement — same tool, same method

Everything above was verified per producer. This is the corpus-level check
with `producer_repad_sweep.py`, the tool that set the baseline:

| | baseline (`14865d3d`) | now |
|---|---:|---:|
| `RE_PADS` | 19 | **12** |
| `CLEAN` | 26 | **32** |
| padded fields regenerated | 228 | **57** |

The seven producers that left the list are exactly the seven witness-emitting
fixes — `binding_factor_f_sequence`, `bring_homology_pairing_integration`,
both `chirality_avg_content_*`, `rho_k_co_casimir_extended`,
`v_hat_to_delta_lambda_bridge`, `xi_ell_phi_q_probe`. Nothing claimed is
missing and nothing untouched regressed.

**The arithmetic needs one note.** The sweep shows 171 fields drained, the
per-producer runs 248. The difference is `rho_k_co_casimir_extended`: the
sweep only ever credited it with 71, the count from a run that hit the 150 s
wall, while a complete run writes 148. Both numbers are right about what they
measure — 171 is the drain *as this tool scores it*, 248 is the drain in
fields that actually exist. The sweep's own baseline was a floor, so its delta
is one too.

(`TIMEOUT` moves 0 → 1 for the same reason: `rho_k` still exceeds 150 s, but
now writes no padding, so its verdict falls through to `TIMEOUT` instead of
being outranked by `RE_PADS`.)

### The remaining 57 split cleanly

| | producers | fields | needs a producer fix? |
|---|---:|---:|---|
| **Class B** — no float64 enters | 9 | **39** | **no** |
| **Class A** — real float64 entry | 3 | **18** | yes |

Class B is the detector's near-integer false positives — `gap_a4_*`,
`markov_stab`, `qbeta_markov_trace_*`, `habiro_*`, `verify_c_color_swap`.
Hunting for a float64 entry in them is looking for something that is not
there; what they need is a decision about the *detector*, not the producers.

Class A is three files and 18 fields:

```
su4_1111_markov_trace_probe.py   (+10)   hecke_characters.py:214 root
phi_q_spectral_combiner_probe.py (+6)    reads an upstream witness — fix upstream
rho_k_h3a_lp_dual.py             (+2)    reads an occam JSON blob — fix upstream
```

Two of the three take their value from a **committed witness**, so the
precision was lost when that witness was written: the fix is upstream and the
ordering matters. Only `su4` is fixable in place, and its count is a floor —
both runs that measured it timed out.

## The last 47 fields, mapped

`su4_1111_markov_trace_probe` (10) is fixed, which exhausts the Class A cases
fixable in place. Its count was recorded as a floor because both runs that
measured it timed out; given a longer budget it completes at exactly the 10 the
sweep saw — a floor that happened to be tight.

### 8 fields: a real upstream downcast, and it needs the chain

`phi_q_spectral_combiner_probe` (6) and `rho_k_h3a_lp_dual` (2) read their
values from a **committed witness**, so nothing they do locally can help. The
loss is in `qbeta_per_block_paper_closed_forms.py`, and it is not subtle:

```python
q_0 = sp.Float(q_0_str, 30)                          # 30 digits available
val = float(expr.subs(q, q_0))                       # -> 53 bits
y_lam[label] = float(entry["y_at_q0_50dps"])         # 50 digits available -> 53 bits
tau_diff  = sum(y_lam[s] * chi_at_q0[s] ...)         # float arithmetic
```

The second line is the clearest statement of the defect anywhere in this
corpus: **the field is named `y_at_q0_50dps` and the code takes a `float` of
it**, discarding 33 digits that are sitting right there. The witness then
stores the results as JSON *numbers*, so `mpf(v)` downstream faithfully
reproduces 53 bits and the consumer looks like the culprit.

This is the "downcast upstream" branch of the judgment the scope note sets out,
and it is where the original **"upstream propagation"** reading — retracted as a
general claim about all 20 — was pointing at something real. It is true here,
for these two, and the fix has the ordering that claim asserted: repair
`qbeta_per_block_paper_closed_forms`, regenerate its witness, then re-run both
consumers. Fixing the source without the regeneration changes nothing
downstream; regenerating without the source fix re-imports the same 53 bits.
**Not attempted here** — a three-step chain across two witnesses deserves its
own change, not the tail of this one.

### 39 fields: the detector, not the producers

Nine producers — `gap_a4_*`, `markov_stab`, `qbeta_markov_trace_*`, `habiro_*`,
`verify_c_color_swap`. Verified to convert **no repo float64 at all**; their
flagged values are genuine computations of quantities that are exactly integers
(`tr_M(1) = 1 − 1.4e-51`, `h2 = 10 + 3.2e-47`). No producer fix exists, because
there is no defect in the producer.

`is_f64_padded` flags anything within `1e-30` of a double, and a value that *is*
1 sits that close to `1.0` — as does a genuine padded value truncated at 50 dps
(`1.56e-50`). **No test on the string can separate them**, so the choice is
between two things, and it belongs to whoever owns the ratchet:

1. **Baseline them** as known false positives, with the reason recorded, so the
   gate reads a true zero for the real defect.
2. **Give the producers the knowledge** — a quantity known to be an exact
   integer can be emitted as one, which removes the value from the detector's
   reach honestly rather than by exception.

Option 2 is better where the exactness is actually known (an identity trace, a
representation-theoretic multiplicity) and unavailable where it is not. What
must **not** happen is a further search for a float64 entry in them: #4677
established there is none, and the next agent to go looking will spend the same
day rediscovering it.

## Why the per-block witness went stale — 122 producers are invisible to the drift detector

Regenerating `qbeta-per-block-paper-closed-forms.witness.json` moved two values
at the 8th digit *before any source change*: the committed numbers did not match
`float()` of their own upstream `y-lambda-at-q0.witness.json`. That witness had
moved and this one was never regenerated.

The repo has a detector for exactly this — `computations/witness_dependency_drift.py`,
which sees a dependency only when the producer declares it:

```python
per_block_witness = builder.add_upstream(upstream_path)   # phi_q — declared
y_data = json.load(open(_pb.witness_path("y-lambda-at-q0.witness.json", HERE)))
                                                          # per-block — invisible
```

`phi_q_spectral_combiner_probe` has a comment saying it uses `add_upstream`
*"so the drift detector sees the upstream hash"*. The per-block producer reads
two witnesses (`q-pinning-50-digit`, `y-lambda-at-q0`) with a plain
`json.load`, so neither edge exists as far as the detector is concerned.

**Swept:**

| | producers |
|---|---:|
| read a committed witness via plain `json.load`, **no** `add_upstream` | **122** |
| declare the dependency with `add_upstream` | 32 |

So roughly four in five witness-consuming producers are outside the drift
detector's reach, and any of them can go stale exactly the way this one did —
silently, with the gate green. That is the same shape as the two other gaps this
document records: the padding audit cannot see the `mp.dps` no-op, and the
staleness detector cannot see an undeclared dependency. Each gate is sound
about what it looks at; the misses are all in what never reaches it.

Not fixed here — 122 producers is its own change, and `add_upstream` alters
witness content (it records the upstream hash), so it is a regeneration wave,
not an edit. Recorded with the discriminator so it can be scoped:

```python
# a producer is invisible if it mentions ".witness.json" and json.load(s)
# one, but never calls add_upstream
```

## P30 — the missing `scriptHash` was concealing real staleness

`compute_audit_scan` reports witnesses lacking `scriptHash` + `scriptFile`,
without which `run_pipeline.py` treats a witness as current and skips
regeneration. Scoped, **excluding `_deprecated/`** (a first count said 448 and
had swept deprecated witnesses in — that number was wrong):

| | witnesses |
|---|---:|
| live, carry both fields | 2166 |
| **no `scriptFile` at all** | **173** |
| `scriptFile`, no `scriptHash` | **78** — 12 use `WitnessBuilder`, 66 hand-written |
| `scriptFile` naming a producer that no longer exists | 8 |

**`scriptHash` cannot be backfilled**, which is the first thing to establish
because it looks like it can: the field hashes the *script*, so it is
computable without running anything — and stamping the current hash onto a
witness that may be stale would assert a freshness nobody checked. That is
precisely the failure the field exists to catch. Only a real re-run produces a
witness and a hash that agree.

**Re-running is also not enough for most of them.** Of the 12 whose producer
does use `WitnessBuilder` (7 distinct scripts), re-running gave:

| | |
|---|---:|
| gained a `scriptHash` | **5 / 7** |
| …of those, with **no** value change | **1 / 5** |

The other four moved a large fraction of their numbers:

```
entanglement-orders                38 of 83 numeric fields changed
inverse-markov-qvalues             33 of 53
nf-qvalues                         32 of 43
markov-free-energy-qvalues         26 of 51
```

**That is the finding.** These are not cosmetic metadata gaps: 45–77 % of the
numbers in those four witnesses are stale, and the missing `scriptHash` is
exactly why nobody noticed — `run_pipeline.py` had no way to know they needed
re-running. P30's one-line description ("hand-written witnesses are treated as
current and silently skip regeneration") is understated; the consequence is a
corpus of committed numbers that no longer match their own producers.

The 66 hand-written ones cannot be fixed by re-running at all — they need
porting to `WitnessBuilder` first, and a first batch of 12 arbitrary targets
confirmed it: **0 of 12 gained a hash**, including one that exited 0.

Not regenerated here. Committing those four witnesses changes hundreds of
published numbers, which is a decision about the corpus rather than a cleanup,
and it should be made deliberately with the staleness quantified per witness —
which the table above now makes possible.

### Measured, then regenerated — and a fourth sub-class

All 12 unhashed `WitnessBuilder` witnesses (7 scripts) measured before deciding
what to commit:

| witness | rc | hash | stale |
|---|---|---|---:|
| `nf-qvalues` | 0 | ✓ | **32/43 (74 %)** |
| `inverse-markov-qvalues` | 0 | ✓ | **33/53 (62 %)** |
| `markov-free-energy-qvalues` | 0 | ✓ | **26/51 (51 %)** |
| `entanglement-orders` | 0 | ✓ | **38/83 (46 %)** |
| `qbeta-odd-carrier-sector-decomposition` | 0 | ✓ | 0/35 |
| `chi-*` ×6 | 0 | ✗ | 0 |
| `kite_tail_reconciliation` | 1 | ✗ | 0 |

Five regenerated and committed; **129 numbers move**. Nothing in the sources
changed — each producer run unmodified at HEAD already disagreed with its own
committed witness. `qbeta-odd-carrier` is included *because* it moved nothing:
it isolates the metadata change from the value change.

**The fourth sub-class: `scriptFile` naming a consumer.** The six `chi-*`
witnesses claim `delta_lambda_empirical_tabulation.py`, which **reads** them as
`chi_witness` inputs and never writes them — as do `mass_vol_density.py` and
`mass_per_knot_density.py`. Nothing in the corpus writes them. Re-running the
named "producer" therefore does nothing, which is exactly what was observed
(rc=0, hash absent, no value moved).

This invalidates an assumption in the counts above: **`scriptFile` was taken as
truthful**, and at least 6 of the 12 are misattributed. The earlier split (173
no `scriptFile` / 78 unhashed / 8 orphaned) is a floor on the provenance
problem, not a description of it — a witness naming a real script is not
evidence that script produces it. The honest discriminator is whether the
script *writes* that filename, which none of these do.

## What remains

Localization is done: all 19 re-padders are measured and every Class A field
has a named source line. What is left is the per-file *judgment*, which is
where this document said the non-mechanizable part lived all along.

- **Regeneration is no longer lossy** — the q₀-pin drop is diagnosed and fixed
  (section above), so the drain plan's "re-run the producers" half is unblocked.
  557 witnesses were exposed to it.
- **Class A — 10 producers, 189 fields, three library-level entry points.**
  `hecke_characters.py:214`, `hoefsmit_numpy.py:161`, and the
  `mpf(<float out of JSON>)` idiom. All three are deliberate f64 kernels, so
  the fix is "serialize at true precision", not "recover lost precision".
  **219 fields are done** — `chirality_avg_content_atomic` (71) and
  `rho_k_co_casimir_extended` (148). Neither touches the shared helper: both
  fix serialization in the producer, which is why `hoefsmit_numpy.py:161`
  can stay as it is for its other callers.
  **242 fields are done** — `chirality_avg_content_atomic` (71),
  `rho_k_co_casimir_extended` (148), `chirality_avg_content_chiral` (12),
  `v_hat_to_delta_lambda_bridge` (6), `xi_ell_phi_q_probe` (5). The rule they
  share is `qou_substrate.precision.str_at_true_precision` — an mpf equal to
  its own float64 holds 53 bits and nothing more. It is a drop-in for
  `str(<mpf>)` and **not** for `fmt(<mpf>)`: those serialize at `mp.dps` and
  `OUTPUT_DPS` respectively, which producers set differently, so the wrong
  fallback silently rewrites every value it was not meant to touch.
  Remaining: `su4_1111_markov_trace_probe` (10, floor — its measured runs
  timed out) on the `hecke_characters.py:214` root; `bring_homology_pairing_integration` (2 real, 2 tolerances that must
  not move); and the two that read the value from a committed witness, where
  the fix is upstream and ordering matters.
  Counts for the producers that exit non-zero or time out are floors.
- **Class B — 9 producers, 39 fields — needs no producer fix.** The values are
  genuine; the *detector* calls them padding. Either it learns to tell a
  computed near-integer from a truncated double (it cannot, from the string
  alone — so this would need producer-side knowledge that the quantity is
  exact), or these are baselined as known false positives with that reason
  recorded. What must not happen is someone hunting for a float64 entry in
  them: it is not there.
- **Provenance:** 37 fields carry a distinctive value already committed
  upstream. Those consumers should be checked against their producers before
  being "fixed" in place.
- **Two producers still cannot be run at all** here
  (`habiro_interpolate_cross_validator`, `rho_k_h3a_lp_dual`, both exit 2), so
  their traces are partial — sites found are real, absence is not evidence.


## P32 — `UNCONFIRMED` triage: follow the filename to the write sink

`witness_provenance_audit.py` shipped (#4717) recognising exactly one way to
write a witness: `WitnessBuilder`. That is not how most of this corpus writes
one. 250 producers assemble the payload by hand, write it to an explicit path,
and stamp the staleness metadata afterwards (`stamp_staleness_metadata`, 185
call sites). All of them read as non-writers, which is why `UNCONFIRMED` stood
at **466 of 2250** — a number large enough to make the verdict useless.

The upgrade traces a filename from a literal to a **write sink**. Sinks are
asymmetric on purpose: `write_text` / `write_bytes` and `open(…, "w"|"a"|"x")`
count; `read_text` and a bare `open()` do not. That asymmetry is the whole
safeguard, and it is the difference between this and the "mentions it" test
that produced the original mis-attribution.

Three path idioms, found by reading what was left after each pass rather than
by guessing up front:

| idiom | example | after |
|---|---|---|
| `Path(x)`, `HERE / x`, via a variable | `out = HERE / "…"; out.write_text(…)` | 466 → 198 |
| `os.path.join(…, x)` | the whole `alpha_em` probe family | 198 → 53 |
| `p.with_name(x)` | the `borromean` cluster | 53 → **32** |

Each idiom landed with a **paired negative test** — the same construct reaching
a read instead of a write, which must stay `UNCONFIRMED`.

### What was checked, given this arc's history

Three earlier cuts of this tool were wrong by ~10× each (324 → 189 → 28 → 3),
so a clean-looking jump is precisely when to stop and verify:

- **`NOT_A_PRODUCER` held at 3 across all three extensions — by name, not by
  count.** This is structural, not luck: the verdict is reached only when the
  source mentions no witness at all, and finding *more* writes cannot create
  that condition. The upgrade can only move `UNCONFIRMED → WRITES`.
- **The regression is pinned on real corpus data, not only in a unit test.**
  All six `chi-*.witness.json` that name `delta_lambda_empirical_tabulation.py`
  remain `UNCONFIRMED`: that script contains their filenames, hands them to a
  read, and writes a different witness. This is the exact shape the tool exists
  to reject, and it survives the upgrade.
- **Five newly-promoted witnesses were read by hand**, all confirmed genuine
  writers. One was worth the trip: `chi_at_q0_via_hoefsmit_mpfr.py` was cited in
  the tool's own docstring as unresolvable ("writes via a helper"). It does have
  an atomic-save helper — and also writes `out.write_text(...)` directly at line
  341, so the f-string pattern resolves it correctly. The docstring's example
  was stale and has been replaced with one that is still true
  (`binding_canonical.py`, whose builder name is not a literal).
- **A self-test case had to be retired, not satisfied.** `"hand-rolled write"`
  asserted `UNCONFIRMED` for `Path("out.witness.json").write_text(j)` — the
  documented limitation this change removes. Replaced by the identical source
  expecting `WRITES`, with a comment recording the swap so it does not read as
  a silently loosened test. 25/25 pass.

### Two findings recorded, not fixed here

- **Six `chi-*` witnesses are mis-attributed.** Their `scriptFile` names a
  script that reads them. `UNCONFIRMED` is the honest verdict — the tool cannot
  prove no unseen path writes them — but the correct producer should be
  identified and the claim repaired.
- **`computations/computations/` exists and is committed** (3 duplicate
  witnesses, commit `e5dcd8f5`), the signature of a producer run from the wrong
  working directory. Checked specifically because this arc has already been
  burned once by mistaking self-inflicted contamination for a finding
  (`/tmp/trace-wt`); `git ls-files` confirms these are tracked and pre-existing.
  Shadow copies of files that also exist at the correct path — a corpus
  decision, not a tool fix.

## P33 — the six `chi-*` mis-attributions, and why `computations/computations/` existed

### The doubled directory: a cwd-relative path plus a silent `mkdir`

Three producers wrote to the **string literal** `"computations/<name>.witness.json"`
— resolved against the *current working directory*, not the script. Run from the
repo root it lands correctly; run from inside `computations/` it lands in
`computations/computations/`. Two of the three then call
`out_path.parent.mkdir(parents=True, exist_ok=True)`, which **creates** the
spurious directory instead of failing, so the mistake left no trace but the
files. `binding_bring_enhancement_compare.py` already defined `HERE` at line 40
and did not use it for output; `binding_alpha_shift_witness.py` documented its
default as *"alongside the script"*, which is precisely what it was not.

All three now build the default from `__file__`. Verified the way the bug was
caused rather than statically: run each from inside `computations/`, confirm the
witness lands at the correct path and no doubled directory reappears.

The three committed copies were stale — written 17:36–17:42 on 2026-07-18,
where the correct-path copies date from 19:19–23:59 the same day — and they
differ in numbers, not just metadata. Deleted, along with their three keys in
`raw-float64-baseline.json` (83 baselined fields; removing baseline entries only
tightens the gate). Audit totals move by exactly those three files and 83 fields
and nothing else; `NEW dirty 11 / REGRESSED 1` reproduce identically on a clean
tree, so they are pre-existing and unrelated.

**A drift found while verifying, and deliberately not committed.** Re-running
those three today reproduces the *older* numbers:
`binding-bring-enhancement-compare` regenerates `q_0_50dps` at 68 digits where
the committed witness holds the 50-digit proton anchor, and its
`delta_flavor_split_subleading` comes back as the value from the stale doubled
copy. That is a genuine reproducibility failure in the producer's q₀ sourcing —
unrelated to the path fix, which only changes *where* the file is written. The
regenerated witnesses were reverted; committing them would leak a drifted value
over a committed one, the failure `q0_muon_reproduction_sweep.py:145` names as
the tnjb corruption. Recorded here as its own item.

### Five of the six `chi-*` claims repaired; the sixth is an orphan

Each producer was identified twice over, by independent means — a static trace
from filename to write sink, and the shape of the payload the candidate writes:

| witness | producer | fingerprint |
|---|---|---|
| `chi-proton-h3`, `chi-neutron-h3`, `chi-tritium-h9`, `chi-helium-3-h9` | `per_irrep_pole_atom.py` | 8/8 keys, incl. `compute_time_sec_so_far` |
| `chi-deuteron-h6` | `per_irrep_pole_deuteron_h6.py` | its smaller payload, and `compute_time_sec` |
| `chi-helium-4-h12-numeric` | **none** | 1/8 — matches neither |

`per_irrep_pole_atom.py` carries all six atoms in its table and writes
`chi-{atom}-h{3(Z+N)}.witness.json`; `canonical_tr_m_via_chi_cache.py:82` says
so outright in a `FileNotFoundError` — *"Run `per_irrep_pole_atom.py {atom_name}`
to build it."* The `-numeric` suffix on the helium-4 file is why it is not that
script's output: the live counterpart `chi-helium-4-h12.witness.json` exists and
fingerprints 8/8. `-numeric` is a superseded variant with no producer — a fourth
orphan alongside the three already triaged, to be deleted or re-attributed as a
corpus decision.

Only `scriptFile` was changed. None of the six carried a `scriptHash` (asserted,
not assumed — the repair aborts if one is present), so no hash was desynced and
none was invented; `run_pipeline` still sees them as needing a run. The repair
then **verifies itself**: all five reclassify `UNCONFIRMED → WRITES` under an
audit that was given no knowledge of the fix.

`_path_bridge.witness_path(name, HERE)` — this repo's own resolver, 208 call
sites — was added to the tracer as a fifth idiom. It moved only 2 witnesses:
those call sites are overwhelmingly reads. **`UNCONFIRMED` now stands at 25**,
`NOT_A_PRODUCER` still the same three by name.

## P34 — Class B closed: the digits decide what the distance cannot

The Class B verdict above was **"needs a decision about the detector, not the
producers"**, and reasoned that no static test could separate a genuine
near-integer from a truncated double, because the two overlap on distance:

    mpf(0.1) printed at 50 dps   rel. distance 1.56e-50   IS padding
    tr_M(1), genuinely computed  rel. distance 1.37e-51   is NOT

That is correct **about a threshold** — and the detector was a threshold
(`abs(x - mpf(float(x))) / abs(x) < 1e-30`). It is not correct about static
tests in general, and the difference is worth stating precisely, because the
earlier conclusion generalised one to the other.

Padding is not "close to a double". Padding is *printing a double's own
digits*. `mpf(0.1)` at 50 dps emits
`0.10000000000000000555111512312578270211815834045410` — the exact expansion of
the binary64, truncated. `tr_M(1)` emits `0.999…99863`, and the nearest double
is `1.0`, whose exact expansion is `1`. Those are different digit strings, and
proximity does not make them the same one. `Decimal(<float>)` gives the double's
exact value, so the comparison is available and cheap.

`is_double_expansion` asks that question, with a tolerance of exactly one
half-ulp **of the shown precision** — mpmath rounds the last digit it prints,
and a first draft that demanded exact string equality wrongly cleared the
expansion of `1e-09` for precisely that reason. The place value is read from
`Decimal.as_tuple().exponent`, not by counting characters after the `.`, so
exponent-notation strings get the right ulp. The old threshold is kept as a
cheap pre-filter and is no longer the discriminator.

### Validated in both directions, because this change can only *remove* flags

The dangerous direction here is the opposite of the provenance work: an
over-eager discriminator hides real padding instead of inventing it.

- **Nothing real was cleared.** All 15 flags in the committed corpus survive;
  the audit reports the same 14 occurrences / 7 files / 1 NEW as before.
- **The false positives clear.** Three of the nine Class B producers were
  re-run in a throwaway worktree — never the live checkout — and their fresh
  output carries 15 flagged fields under the old test and **0** under the new
  one, including `tr_M_identity_H4_at_q0`, `f_leading_ratio`, `H_leading_ratio`
  and the `h_expansion` table. The remaining six producers were not re-run;
  their share of the 39 is expected to clear on the same grounds but is **not
  measured**, and should not be reported as if it were.
- Seven self-test cases were added, four of them the values those producers
  actually emit and three the padding shapes that must still be caught —
  including the `1e-09` expansion that broke the first draft.

### A sixth padding mechanism, found on the way

The audit reported 2 NEW padded fields, both `m_tau/m_e = 3477.23`, in
producers that already do the right thing (`mpf("3477.23")`, a string, never a
float). The constant is built at **module scope**, and `set_compute_dps()` is
called inside `main()` — so the constant is constructed at import time at
mpmath's default 15 dps, frozen at 53 bits, and serialized later at compute
precision, printing the binary64 tail. Confirmed directly:

    early = mpf('3477.23')   # at 15 dps      -> 3477.23000000000001818989403545856475830078125
    mp.dps = 70
    late  = mpf('3477.23')   # after the raise -> 3477.23
    early == late            -> False

Not a formatting artifact: the values genuinely differ.
`m_tau_hecke_energy_route.py` is worse than the literals suggest — it also
*divides* at 15 dps (`mpf("1776.86") / mpf("105.6583755")`).

Both now call the idempotent `set_compute_dps()` at module scope before any
constant. `m_tau_hecke_energy_route` is fixed and regenerated: the padding is
gone and `abs_rel_error_pct` shifts in the ~14th digit, which is the fix
working rather than drift.

**The class is larger than the two.** An AST sweep finds **170 module-level
`mpf("…")` constants across 63 files** built before precision is raised. Most
are harmless — tolerances (`mpf('1e-25')`) and constants with fewer
significant digits than 53 bits carries (`mpf('0.51099895069')`, 11 digits) —
so this is a *potential*, not a backlog of 170 defects. It deserves its own
gate on the same argument that justified `mpf_context_dps_audit.py`: neither
existing gate can see it, because a value that is merely *wrong* past digit 16
is not padded and carries no float64 marker. Not built here.

### Un-regenerated, then regenerated — the census was installable after all

`m_tau_census_sweep.py` was first left with its fix committed and its witness
not, because a re-run here searched 180,511 manifolds where the committed
record has 433,804: SnapPy installs, but this build shipped without the large
census databases. That was reported as an honest red rather than a green bought
with a degraded environment.

It was worth one more attempt. `pip install snappy_15_knots` supplies the
missing database, and `len(HTLinkExteriors)` then reads **433,804** — the exact
figure in the committed witness, which is what makes the re-run trustworthy
rather than merely successful. Regenerated on that basis: every census count,
volume ceiling and ceiling manifold is byte-identical to the committed record,
so the only changes are the padding fix (`m_tau_over_m_e` → `3477.23`) and
`vol_target_k2` moving in the 17th significant digit, which is the correctly-
precise constant propagating.

The padding audit is now **NEW: 0** and `--strict` exits 0.

The general point stands and is worth keeping: three environment mismatches
turned up in one session (mpmath 1.3.0 vs 1.4.1, this census, and
`pyhecke_native`/`clarabel` with Python 3.11 vs 3.13). Two were repairable and
one is not. The rule that held throughout is not "never regenerate" but
**match the reference environment first, and verify the match on a value the
committed witness already records** — here, the manifold count.

## P35 — undeclared upstreams: the count was 122 because the sweep was a grep

`witness_upstream_declaration_audit.py` replaces the ad-hoc sweep that produced
the 122 figure above. It shares its path resolver with
`witness_provenance_audit` — same idioms (`Path(x)`, `HERE / x`,
`os.path.join`, `p.with_name`, `_pb.witness_path`, and values reached through
a variable), with the read/write sinks **inverted**: here `read_text`,
`json.load(open(p))` and a bare `open(p)` are what count, and a write is not.

| | producers | edges |
|---|---:|---:|
| undeclared upstream (invisible to drift) | **331** | **410** |
| fully declared via `add_upstream` | 23 | |
| declares, but via a computed path — not counted either way | 7 | |

The earlier 122 was a grep for `json.load` adjacent to a literal filename, so
it saw only the plainest spelling. Every path that reaches a read through a
variable, a helper, or `os.path.join` was invisible to it — the same
undercount, in the same direction, that recognising only `WitnessBuilder` made
in P32. **331 is not a correction of a wrong method; it is the same question
asked with a resolver instead of a regex.**

Three flagged producers were read by hand and all three are real:
`aK_via_lp_dual.py:56` (`json.load(Q_PIN.open())`),
`alpha_star_vs_binding_gap.py:68-72` (three witnesses opened directly), and
`_habiro_coefficient_extract.py:136`. The last one is worth naming as a
limitation rather than a win: it resolves because a module-level variable and
a function parameter share the name `habiro_path`, and here they do denote the
same file. A different file passed under a reused name would resolve wrongly.

**Bounding the noise:** 21 of the 410 edges (5%) name a witness that does not
exist in the corpus — dangling reads, or name-collision artifacts of exactly
the kind above. The count is a floor with ~5% noise, not a precise inventory,
and reading it as either would be a mistake.

The useful structure is the ranking, not the total:

| undeclared dependents | upstream |
|---:|---|
| 71 | `q-pinning-50-digit.witness.json` |
| 31 | `y-lambda-at-q0.witness.json` |
| 30 | `habiro-coefficients-atomic.witness.json` |
| 18 | `q-beta-operator-valued-N3.witness.json` |

`q-pinning-50-digit` moving silently invalidates 71 producers. That is where a
port earns the most, and it is a far better unit of work than "331 producers".

**Report-only, not wired into CI.** Every other gate in this arc was
introduced at baseline zero so it could fail the build. This one starts at 331,
so gating it would install a standing red — the failure mode #4653 avoided.

### Why no producer was ported here

`add_upstream` rewrites the witness (it records the upstream's hash), so a port
is a re-run, not an edit — and **this container cannot faithfully re-run these
producers**. Four candidates were screened in a throwaway worktree:

| producer | what a re-run here would record |
|---|---|
| `alpha_star_vs_binding_gap` | already broken: reads `base / "joint-tower-sdp-rust.witness.json"` where `base` is its own directory and the upstream is not there |
| `alpha_k_jones_markov_h12` | exits 1 |
| `aK_via_lp_dual` | `python 3.13.12 → 3.11.15`, drops `pyhecke_native 0.9.0` |
| `a3_mirror_residual_reconciliation` | drops `clarabel 0.11.1` |
| `alpha_em_shift_chain` | drops `pyhecke_native`, and **loses `q0`, `inv_alpha_chain`, `inv_alpha_bare`** — the computation degrades without the native module |

That is the third environment mismatch this session, after mpmath 1.3.0 vs
1.4.1 (resolved by installing 1.4.1) and SnapPy's missing census databases (not
resolved). A port committed from here would record a degraded environment as
though it were the reference one. The detector is committed and the work is
scoped; the regeneration wave needs the reference environment — Python 3.13,
`pyhecke_native`, `clarabel`, the full SnapPy census, mpmath 1.4.1.

`alpha_star_vs_binding_gap.py` reading an upstream from a directory that does
not contain it is a live bug found on the way, not a consequence of anything
here. Recorded, not fixed.

## P36 — porting to `add_upstream`: 40 are mechanical, 290 need the API to change

Scoping the port properly changed what the work *is*. Two measurements, each
of which corrected a guess:

**Where the read happens.** The first cut said all 331 undeclared producers
read their upstream at import time, which would have meant no builder could
possibly exist yet. That was a bug in the measurement — the walk descended into
module-level `def` bodies, so a read anywhere in the file counted as
import-time. Corrected: **40 read at import, 291 inside a function.** (Same
error shape as the `try:`-block false positive in P34's gate, found the same
way: the number was too round to believe.)

**Whether a builder is in scope yet.** The binding constraint is not *where*
the read is but whether a `WitnessBuilder` exists when it happens, since
`add_upstream` is a method and the hash record needs somewhere to land:

| | producers |
|---|---:|
| builder constructed **before** the first upstream read — directly portable | **40** |
| builder exists but is constructed **after** the read — needs a reorder | **290** |
| no builder call at all | 0 |

So the dominant shape in this corpus is *read your inputs at the top, build the
witness at the bottom* — and `add_upstream` requires exactly the opposite
order. **That, not oversight, is why adoption sits at 5.7%.** The API asks for
a structure most of these producers do not have.

### One port, verified end to end

`probe_inter_knot_decoupling.py` is one of the 40. `_load_q_0()` now takes the
builder and calls `add_upstream(Q_PINNING)`. Re-run, the witness gains exactly
what it should:

```json
"upstream_witness_hashes": [
  {"path": "q-pinning-50-digit.witness.json",
   "sha256": "91beff98ef672777d26f345705ca569bfdeec4f388a9d2bb0b9fd6df015ab0db",
   "commitSha": "7f9474204b81a19d3044c75259238003c8c47037",
   "computedAt": "2026-07-18T17:30:49.888071+00:00"}]
```

**No numeric value moves.** Only the source is committed: this container's run
drops `pyhecke_native 0.9.0` and `clarabel 0.11.1` from the environment block,
so the witness itself must be regenerated where those exist. The declaration
takes effect on that re-run; until then the source is strictly better and the
witness is unchanged.

### What the other 290 need

A reorder per producer is 290 hand-edits with no mechanical check — the shape
of change this arc has already been burned by once, when a blind regex patched
ten scratch files where the gate named five.

The alternative is to let the record be taken before a builder exists and
attach later: a module-level `record_upstream(path)` that wraps the existing
`load_and_hash_upstream` and accumulates, with `WitnessBuilder` draining the
pending list on construction. That would make all 290 a one-line substitution
at the read site, with no restructuring.

**Deliberately not implemented here.** A global mutable accumulator in the
witness substrate can leak records between producers when two builders are
constructed in one process, or when a test imports a producer module for its
symbols — silent cross-contamination of provenance metadata, which is the
precise failure this whole audit arc exists to prevent. It needs an ownership
rule (drain-on-construct vs. explicit scope), and that is a substrate design
decision, not a side effect of a porting pass.
