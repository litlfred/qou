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
| `mp.dps` no-op | value silently carries **less** than asked for | `mpf_context_dps_audit` |

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

**Both cautions are moot, and the sketch above is superseded.** The gate was
built as `computations/mpf_context_dps_audit.py` and wired into
`scripts/precision-gates.sh` as `mp.dps no-op`, and it parses rather than
matches: indentation is not something the grammar cares about, and a
docstring is a `Constant`, never an assignment. The table above said this
class was caught by "nothing, today" and is corrected in place — **it was
accurate when written and had not been for weeks**, which is the same way a
stale count outlives the run behind it everywhere else in this document.

Scope-resolved since 2026-09-13. A name bound both ways *in one scope* is
still read as the context, deliberately; bindings at different depths are no
longer treated as that tie. Three files here have the shape —
`categorical_q_decay_ba_low_isotopes.py` takes the context at module level
and the package inside a function — so a flat reading abstains on the whole
file, and a no-op inside that function would read clean. None assigns `.dps`
today. Verified both ways: across all 3223 mpmath-naming files the two
readings agree everywhere on the current corpus, and both still catch all
seven of the pre-fix files pulled from history.

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

## P37 — `record_upstream`, 21 producers ported, and two corrections

### The API: the list belongs to the caller

P36 measured that 290 of 330 witness-consuming producers read their upstreams
*before* constructing a builder, so `add_upstream` — a method — could not reach
them. `record_upstream(path, into)` closes that without a restructure:

```python
_UP: list = []
q0 = mpf(record_upstream(Q_PIN, _UP)["derived_50_digit"]["q"])
...
w = WitnessBuilder("my-witness").add_upstream_records(_UP)
```

The obvious alternative was a module-level accumulator drained on builder
construction — one edit per producer instead of two. **Rejected, and the
rejection is the design.** It breaks in two ordinary situations: producer P
imports Q, and Q recorded upstreams at *its* import, so P's builder drains and
claims Q's records; or a test imports a producer for its symbols and any later
builder inherits them. Both silently attach the wrong provenance — the precise
failure this metadata exists to detect. An explicit list makes that class of
bug unrepresentable: a record can only reach the witness whose author named the
list. `test_lists_do_not_leak` pins it, and `add_upstream_records` is
idempotent by `(path, sha256)` so recording early and declaring late cannot
double an edge. 7 tests, all passing.

### 21 producers ported, by a rewriter that only touches what it can prove

Hand-editing 40 files of varied shape is the blind-regex hazard this document
has already paid for once. Instead an AST rewriter replaced only reads it could
prove: the whole read is **one expression** (`json.loads(X.read_text())` or
`json.load(X.open())`), `X` resolves via the audit's own resolver to a witness
the module does not itself write, and a `WitnessBuilder` is assigned to a plain
name **in the same function, strictly before** the read. Everything else was
left alone.

Verification was external to the rewriter, which is the point:

- 23 files changed, 25 reads rewritten; **all 23 compile**.
- The audit — which knows nothing about the rewriter — moves from 330/409 to
  **309 producers / 384 edges**, and declared from 24 to 45. The edge count
  fell by exactly 25, matching the rewriter's own report.
- Sampled runs: 3 of 4 exit 0 and emit the declaration, including a two-edge
  case (`delta-lambda-z4N-phase4` → `delta-lambda-jsj-phase3` +
  `delta-lambda-empirical-tabulation`). The fourth,
  `delta_lambda_jsj_phase3`, fails on a missing `probe_he4_jsj_topology` —
  **identical before and after the port**, so pre-existing.

Source only again: this container drops `pyhecke_native` and `clarabel`, so the
witnesses must be regenerated where those exist.

### Correction: the `chi-helium-4-h12-numeric` readers cannot be repointed

The previous pass proposed repointing its three readers at
`chi-helium-4-h12.witness.json` and retiring the variant. **That was wrong**,
and reading the two files settles it: the `-numeric` witness carries
`per_partition` (with `y_at_q0`, `chi_q_at_q0`) and `abs_tr_M`, while
`chi-helium-4-h12` carries `chi_lambda_symbolic`. They are a numeric result and
a symbolic cache — not two spellings of one thing, and
`delta_lambda_2row_stratum_analysis.py:177` reads `cached["per_partition"]`,
which the symbolic file does not have.

Its producer is gone from the tree entirely — every script emitting `abs_tr_M`
is under `_deprecated/`, and none of them writes this filename. So it is an
**un-reproducible live input**, and its `scriptFile` was the same false claim
the five `chi-*` witnesses carried: `delta_lambda_empirical_tabulation.py`,
which only reads it. Repaired to the corpus's existing convention for this
situation — a parenthesized prose value, as used by 6 other witnesses
("(legacy orphan — no current producer; …)"), naming the confusion so the next
reader does not repeat it. No `scriptHash` was present, so nothing desynced.
`UNCONFIRMED` 21 → **20**.

### Triage: `PADDING_RISK` needs no bulk fix, and that is now demonstrated

Of the 133, roughly 95 are measured physical constants (CODATA/AME/PDG) and 38
are tolerances. In both, the value survives 53 bits — six significant digits is
all `1776.86` *has*. Harm only reaches a witness by serializing at compute
precision, and that path is already gated: build each at 15 dps, `str()` at 70,
and `is_f64_padded` flags **every one**, including `1e-25`. The padding audit
sits at zero under `--strict`, and it is exactly how the two `m_tau` producers
were caught. Gating this tier would add 133 obligations against a failure
another gate already stops.

### Recorded, not fixed

`tools/qou-substrate/tests/test_smoke.py::test_substrate_constants_have_expected_values`
fails on clean `main` (verified by stash): `HBAR_Q_SQ` disagrees with
`VOL_FIGURE_EIGHT / MASS_RATIO_MU_E` by 2.06e-09 against a 1e-15 tolerance.
A substrate-constants inconsistency, unrelated to anything here, and not
something to silently adjust.

## P38 — the reference environment was reachable after all; 4He leaves a dead anchor

### Three "environment blockers" were two installs and a misreading

P36/P37 held witnesses back because this container could not reproduce the
reference environment. Pushing on that dissolved most of it:

| gap | resolution |
|---|---|
| mpmath 1.3.0 vs 1.4.1 | `pip install mpmath==1.4.1` |
| SnapPy census: 180,511 vs 433,804 manifolds | `pip install snappy_15_knots` → `len(HTLinkExteriors)` = 433,804, matching the committed witness exactly |
| `clarabel` absent | `pip install clarabel` → 0.11.1, the recorded version |
| `pyhecke_native` absent | built from `tools/pyhecke-native` with maturin + `libgmp-dev`/`libmpfr-dev` → **0.9.0**, the recorded version |
| "Python 3.12/3.13 vs this container's 3.11.15" | **a misreading.** 1463 of 1680 witnesses already record 3.11.15; 3.13.12 accounts for 141 and 3.12.3 for 65. This container *is* the corpus norm — regenerating here converges rather than downgrades. |

The last one is worth naming as an error rather than a discovery: two witnesses
that happened to be built elsewhere were generalised into a blanket rule, and
that rule then blocked ~130 regenerations for two passes. The check that
settled it — count what the corpus actually records — cost one command.

### Regeneration: mechanism proven, wave not finished

A harness runs every producer that declares an upstream, then classifies:
`DECLARED` (the hashes appeared and nothing but metadata moved) is kept;
`VALUES`, `NOCHANGE` and `FAILED` are reverted, so a drift cannot be committed
by accident. It reverts *only* dirty `*.witness.json` paths — a blanket
`git checkout -- computations/` would have undone the ported sources, which is
why the ports are committed first.

163 producers now declare an upstream. The run is slow (many are minutes each)
and was stopped early; the two that completed are both clean `DECLARED` —
declaration present, **zero** non-metadata fields changed — and are committed.
The remaining 161 are a long run, not an unsolved problem.

### 4He was reading a superseded q₀, and that is a content change

`chi-helium-4-h12-numeric.witness.json` has no producer anywhere in the tree,
and reading it explains why that matters: its `q_0_float` is
**1.1099785955541805** — the *muon-anchored* q₀ — against the current
proton-anchored 1.1099785827513808. Three live producers were consuming
numbers computed at an anchor the repo deliberately retired.

The successor is already in the corpus:
`chi-helium-4-h12-at-q0-50dps.witness.json` carries the same 77 partitions of
12, at 50 dps instead of float64, with a live producer
(`chi_at_q0_via_hoefsmit_mpfr.py`). Two independent signs it was always the
intended replacement: `delta_lambda_empirical_tabulation.load_chi_per_lambda`
*already* normalises its `by_partition` / `y_lambda` / `chi_lambda` shape, and
the 5Li row beside 4He was migrated to this family earlier. 4He was the
straggler.

All three readers now point at it. **This moves a published number:**

    tr_M(4He), legacy   (muon-anchored q0) = 0.05534834587669884
    tr_M(4He), successor (proton anchor)   = 0.055358426266783106465
    relative change                        = 182 ppm

182 ppm is not a rounding artifact; it propagates into the helium-4 binding
prediction. It is a *correction* — the old value is anchored to a q₀ this repo
no longer uses — but accepting a 182 ppm move in a published quantity is a
content decision, so it is stated here in full rather than folded into an
infrastructure change. Nothing else in the repoint alters a value: the readers
downcast to float in any case, and `delta_lambda_2row_stratum_analysis`
computes `dim` itself rather than reading the field the successor lacks.

## P39 — two corrections, and why `--strict` must wait

### The 4He successor is muon-anchored too; the 182 ppm is not an anchor change

P38 said the repoint moved 4He "to the proton anchor". **It did not.**
`chi-helium-4-h12-at-q0-50dps.witness.json` carries
`q_0_50dps = 1.1099785955573347…` — the **muon** prefix. The repoint moved 4He
from one muon-anchored value to another.

The arithmetic should have caught this before the claim was made. The two q₀
values differ at the **12th** significant digit (`1.10997859555_41805` vs
`1.10997859555_73347`, ~3e-12 relative). A 3e-12 perturbation cannot move χ at
the 5th digit. So the 182 ppm was never the anchor: it is a *methodological*
gap between two computations of the same quantity — the successor via
`pyhecke_native 0.9.0` `chi_lambda_all_partitions_mpfr` (branch decomposition,
50 dps), the legacy one by another route at float64. **Two computations of
tr_M(4He) disagreeing by 182 ppm is an open question, not a resolved one.**

### 4He was not a straggler — the muon anchor is the majority

| | witnesses |
|---|---:|
| muon-anchored q₀ only | **650** |
| proton-anchored q₀ only | 379 |
| both | 60 |
| `q0Anchor` field: muon / proton / ambiguous | 344 / 232 / 23 |

The migration to the proton anchor is roughly **37% done**. Calling 4He "the
straggler" inverted the picture; it sits with the majority.

What actually re-anchors it: `chi_at_q0_via_hoefsmit_mpfr.py` imports `Q` from
`q_parameter` (`1.1099785827513808…`, proton), so the committed cache is simply
stale — written before the re-anchoring — and the producer's resume logic skips
recomputation whenever a complete cache exists, which is why re-running it
changed nothing. Forced to rebuild it writes
`q_0_50dps = 1.10997858275138080759166909561076`, correct. That rebuild is 77
partitions through `pyhecke_native` and is slow (~13 partitions per 10 min);
it is incremental and SIGTERM-safe, so it resumes.

### `--strict` cannot be turned on yet, and the porting made that worse

`witness_dependency_drift.py` runs warn-mode (`|| true`) pending a drained
backlog. It is not drained:

|  | before this session's ports | now |
|---|---:|---:|
| self-stale (`scriptHash` ≠ producer) | 479 | **567** |
| drift records | 633 | 634 |
| witnesses carrying `upstream_witness_hashes` | 155 | 161 |

**The +88 is mine.** Porting a producer changes its source, hence its
`scriptHash`, while its witness stays unregenerated — so every source-only port
converts an *undeclared-edge* problem into a *self-staleness* problem until the
witness is re-run. Producer-side declaration is now at 44%, but witness-side
adoption is still 5.9%, and only regeneration closes that gap.

That is an argument for **finishing the regeneration wave before porting the
remaining 197**, not for porting more: each additional port raises the very
backlog that keeps `--strict` off. The residual 197 break down as 91 with no
plain-`Name` builder assignment (they use `wrap_legacy` /
`stamp_staleness_metadata`, so `add_upstream_records` has nowhere to attach),
88 with an unhandled read shape, and 18 using `with X.open() as fh`.

Precondition for escalation, stated so it can be checked rather than judged:
self-staleness back to its pre-port level or below, and witness-side upstream
adoption tracking the 44% producer-side figure. The three precision gates
(`mpf_context_dps`, `module_const_precision`, `witness_float64_padding`) are
already `--strict` and already green; the staleness validator is the only step
still carrying `|| true`.

## P40 — I committed drift I had built a harness to prevent

Three witnesses reached a commit here with moved values and no review:
`braid-encoding-audit` (87 fields), `c3-hopf-habiro-analysis` (9),
`binding-energy-categorical-deuteron` (1). They came from **manual sample
runs** of the ported producers, swept up by `git add -A` — the regeneration
harness, which exists precisely to revert anything that is not a clean
declaration landing, was never involved. A fourth, the 4He chi cache, was
committed **13/77 complete** because a background rebuild was mid-flight when
the same `git add -A` ran. All four are reverted to `origin/main`.

The lesson is not "be careful with `git add -A`" but that the discipline has to
be *in the tooling path*: I ran producers outside the harness and then staged
everything, so the harness's guarantees did not apply to the thing being
committed.

### What the reverted diff shows, though, is the migration answering itself

`braid-encoding-audit`'s 87 moved fields are all one substitution:

    old  -0.10453016099779683   = -h/2 at the MUON anchor
    new  -0.10453014939781968   = -h/2 at the PROTON anchor

The producer reads `Q` from `q_parameter`, which is proton-anchored, so
**re-running it re-anchors it automatically**. That generalises: the 650
muon-anchored witnesses are not a separate migration project — they re-anchor
as a side effect of being regenerated, and they stay muon-anchored precisely
because nothing has re-run them.

**This breaks my regeneration harness's classification.** It keeps `DECLARED`
(hashes appeared, nothing else moved) and reverts `VALUES`. But a producer that
both declares an upstream *and* re-anchors will be classified `VALUES` and
reverted — the harness would discard a correct migration as drift. It needs a
third verdict that recognises a muon→proton anchor substitution as intended,
rather than lumping it with unexplained movement.

### The 4He native path is bypassed for an unrelated reason

Forcing the rebuild reveals `chi_at_q0_via_hoefsmit_mpfr` falling back off
`pyhecke_native` to the pure-mpmath loop, which is far too slow for n=12:

    native chi path bypassed (ValueError: unrecognised d=-0.10445824776972628903…
    expected 0, -h, or -h/2)

That `d` matches `-h/2` under **neither** anchor — proton gives
`-0.1045301493978196`, muon `-0.1045301609977968`, and the value seen is
`-0.1044582477697262`, differing at the 4th significant digit. So this is not
an anchor artifact and not caused by the re-anchoring; it is a pre-existing
incompatibility between the word encoding and the native path's expectations,
surfacing only because the resume logic normally skips the computation
entirely. Re-anchoring 4He is blocked behind it. Not diagnosed here.

## P41 — the 182 ppm was a crossing convention, and the 4He block is the same fact

Both open 4He questions resolve to one distinction, and the code says so itself.

### `chi_at_q0_via_hoefsmit_mpfr` disagrees with itself

Lines 101–108 substitute a **colour-weighted** crossing value when an optional
import succeeds:

```python
_cw_d = -_hm * (mp.mpf(1) / 2 - _avg_color_delta() / 4)
```

with a comment stating it is *"distinct from the color-blind −h/2 by ~7e-5"*.
Lines 175–188, the native fast path, then accept only `{0, −h, −h/2}` — the
colour-**blind** set — and reject anything else:

    unrecognised d=-0.10445824776972628903… (expected 0, -h, or -h/2)

Computed directly, the observed `d` matches the colour-weighted value to 18
digits (`-0.1044582477697262889495`) and matches `−h/2` under **neither**
anchor (proton `-0.1045301493978196`, muon `-0.1045301609977968`). So the
earlier reading — "a pre-existing word-encoding incompatibility" — was right
that it is not an anchor artifact, and wrong to leave it unexplained: the two
halves of one file were written to different conventions, and which one runs
depends on whether `canonical_braid_crossings._avg_color_delta` imports. It
imports in this container, so the native path is refused and the run falls to
a pure-mpmath loop too slow for n=12.

### The 182 ppm is that same convention, stated in the witnesses

| witness | `convention` |
|---|---|
| `chi-helium-4-h12-numeric` | `averaged-crossings` |
| `chi-helium-4-h12-at-q0-50dps` | `colour-weighted-averaged-crossing` |

Not an anchor difference, not precision: **colour-blind versus colour-weighted
crossings**, which is exactly the ~7e-5-in-`d` distinction the source comment
describes, propagating to 1.8e-4 in `tr_M`. The repoint in the previous PR
therefore changed 4He's *crossing convention*, which is a physics choice and
was not what it was advertised as.

One more thing worth recording: the 50dps cache carries
`compute_time_sec: 0.0`, so the run that stamped its `_provenance`
(`rust_fn: chi_lambda_all_partitions_mpfr`) resumed a complete cache and
computed nothing. That provenance block describes a *configuration*, not the
computation behind those numbers — which is why it cannot be used to argue the
native path once handled a colour-weighted word.

## P42 — `witness_regen_classify`: the verdict the guard was missing

Committed as a tool rather than left in scratch, because the previous guard
lived only in a throwaway script and was bypassed the one time it mattered.

| verdict | meaning | commit? |
|---|---|---|
| `DECLARED` | upstream hashes appeared, nothing else but metadata moved | yes |
| `ANCHOR_MIGRATION` | the witness's own q₀ flipped muon → proton, all other movement bounded | yes |
| `VALUES` | movement neither explains | **no** |
| `NOCHANGE` | ran, nothing new | n/a |

`ANCHOR_MIGRATION` is the verdict whose absence would have made the guard
actively harmful: producers read the proton-anchored `Q` from `q_parameter`, so
regeneration re-anchors automatically, and a guard without this verdict reverts
that as drift — holding the corpus on the retired anchor precisely while trying
to protect it.

The acceptance rule is **evidence-gated, not bound-only**: a q₀-valued field
must be seen flipping from the muon prefix to the proton prefix. Small movement
alone is never sufficient, and the collateral bound (1e-5) sits deliberately
below the 1.8e-4 crossing-convention shift, so that change can never be
mistaken for an anchor migration. Reverse flips and non-numeric changes are
rejected outright. Nine self-test cases, including the real
`braid-encoding-audit` shape and the 182 ppm case as a negative.

Validated against the corpus: re-running `braid_encoding_audit` produces 87
moved fields on 1 positive flip and classifies `ANCHOR_MIGRATION`, which is the
migration this document has been describing, now committed rather than
reverted.

## P43 — teaching the native path a colour-weighted crossing

The block on 4He was that `chi_at_q0_via_hoefsmit_mpfr` could not use its own
fast path when colour weighting is on. Tracing it gives a one-line cause and a
small fix.

### The representation, and what the sign encoding threw away

A crossing here is `σ_g + d·I`, so `d` picks an affine combination of σ and
σ⁻¹ via the Hecke relation `σ⁻¹ = σ − h`:

| `d` | crossing | weight on σ |
|---|---|---|
| `0` | σ | 1 |
| `−h` | σ⁻¹ | 0 |
| `−h/2` | symmetric average `(σ+σ⁻¹)/2` | ½ |
| `−h(½ − δ/4)` | **colour-weighted** p–n | **½ + δ/4** |

The FFI passed only `sign ∈ {1, −1, 0}`, and the MPFR kernel hardcoded `h/2`
for `sign == 0`. The colour-weighted crossing is a *fourth* affine
combination, so quantising `d` to a sign cannot express it — hence the
`unrecognised d=…` raise and the fall back to a pure-mpmath loop, which at
H_12 is impractical (13 partitions of 77 in ten minutes).

The 2^k sub-word path could not have carried it either: uniform ½ weighting is
what lets `chi_factor` sum 2^k sub-words in exact integer arithmetic and defer
one division. Weights `(½±δ/4)` are irrational, so that trick dies. The MPFR
path is different — it substitutes `σ_g − shift·I` directly — and there the
generalisation is free.

### The change

`apply_sigma_averaged_mpfr(v, blocks, h, prec)` becomes
`apply_sigma_shift_mpfr(v, blocks, shift, prec)`; the shift is threaded up
through `chi_lambda_braid_mpfr_shift`, `chi_lambda_canonical_h_n_mpfr_shift`
and `chi_lambda_canonical_all_partitions_mpfr_shift`, each of which the
original four-argument function now delegates to with `None`. The pyo3 entry
takes an optional fifth argument. **A decimal string, not an `f64`** — the
shift carries δ and has to cross the boundary at the same precision as
`q_str`, or χ is capped near 1e-16 whatever `dps` says. A malformed string
panics rather than silently falling back to `h/2`, which would return a
plausible number for a *different physical convention*.

Verified in both directions:

- **Backwards compatible, bit-identical.** The four-argument call and an
  explicit `h/2` return the same strings.
- **Correct, not merely different.** Native colour-weighted χ^λ at H_3 against
  the independent pure-mpmath `_chi_lambda_of_word_mpf` (which accepts
  arbitrary `d`):

    | λ | relative difference |
    |---|---|
    | (3) | 3.8e-50 |
    | (2,1) | 4.7e-50 |
    | (1,1,1) | 8.8e-51 |

  Machine precision at 50 dps.

Python now derives the shift from the word instead of raising, and still
refuses a word that mixes two different averaged `d` values — that genuinely
has no single-shift form.

### Two process failures, recorded

**The 4He rebuild was clobbered by my own wave.** I left the regeneration wave
and the 4He rebuild running concurrently over the same tree. The wave reverts
dirty witnesses; the 4He cache is a dirty witness while being rebuilt, so the
wave restored the committed muon version mid-flight and the rebuild then
"resumed" from a complete cache and did nothing. Two writers, one tree.

**The wave discards its own successes.** `_revert` reverts *every* dirty
witness at the moment it fires, not just the one under judgement — so each
`VALUES` verdict also wipes the `DECLARED` and `ANCHOR_MIGRATION` results
accumulated before it. The run reported `DECLARED 26 / ANCHOR_MIGRATION 4` at
90/163 while leaving a clean tree, which is how the bug surfaced: the counters
were right and the retention was not. The classifier
(`witness_regen_classify`, 9/9) is committed and sound; the *driver* around it
needs per-witness revert before the wave is worth re-running.

## P44 — the shift is per crossing, and three other call sites share the block

The word-level shift of P43 was not enough, and the guard I added caught why:

    native chi path needs one averaged-crossing shift per word; saw
    0.10453014939781968273…  (= h/2, colour-blind)
    0.10445824776972628903…  (= h(1/2 − δ/4), colour-weighted)

**An atomic braid mixes both conventions.** p–p and n–n crossings are
colour-symmetric, p–n crossings are not, and ⁴He at H_12 contains all three
kinds. So no single word-level shift can represent it — the first fix was the
right idea at the wrong granularity, and it is only visible because the guard
refused rather than quietly picking one.

`avg_shifts` is now indexed by word position, with an empty string meaning
`h/2` there. `shifts: Vec<Float>` is built once per call and `resolved` carries
`&Float` per crossing; a length mismatch panics rather than silently defaulting.

Verified on a genuinely **mixed** word (colour-blind averaged + σ +
colour-weighted averaged) against the independent pure-mpmath reference:

| λ | relative difference |
|---|---|
| (3) | 2.1e-50 |
| (2,1) | 2.2e-50 |
| (1,1,1) | 2.9e-51 |

and the four-argument call remains bit-identical to all-empty shifts.

### Where else colour weighting belongs

`_avg_color_delta` is consumed by **16 live modules**, so colour weighting is
pipeline-wide rather than a 4He quirk. Three further call sites carry the same
three-way `{0, −h, −h/2}` assumption and will refuse a colour-weighted word
exactly as this one did:

| site | what it is |
|---|---|
| `chi_at_q_inv_via_native_mpfr.py:110` | the q⁻¹ counterpart — χ at the Hecke bar image, structurally identical |
| `tr_m_wenzl_bridge_mpfr.py:393` | gates its **own** `_rust_chi_all` call the same way |
| `probe_9b_laurent_degree_10a5.py:129` | same assumption in a probe |

The middle one matters most and explains why ⁴He still does not rebuild:
`tr_m_wenzl_bridge_mpfr` sits **behind** the check just fixed. On a first build
(no cache to resume) `chi_at_q0_via_hoefsmit_mpfr` goes through
`tr_M_via_wenzl_bridge_mpfr`, whose `sign_map` snaps `round(float(d), 9)`
against three keys and raises for anything else. Fixing one gate exposed the
next; the Rust groundwork now serves both, but the ⁴He rebuild needs that
second Python gate ported too, and it is not done here.

Two smaller notes worth recording: the round-to-9-decimals snap in that
`sign_map` would collide colour-blind and colour-weighted `d` if δ ever fell
below ~1e-9 (they differ by ~7e-5 today, so it is safe now but fragile); and
the first-build path prints no progress, which is why the earlier run looked
hung when it was simply silent.

## P45 — the second gate, and what a clean deuteron rebuild revealed

`tr_m_wenzl_bridge_mpfr.py:393` is now ported too: `_translate` returns
`(sign, gen1, shift_str)` and the caller passes a per-position `avg_shifts`
list. The round-to-9 comparison survives only for the two *exact* classes (σ,
σ⁻¹), where it never has to separate two averaged variants — it could not,
since colour-blind and colour-weighted `d` differ by ~7e-5 today and nothing
pins δ above 1e-9.

**The fix works.** A clean deuteron rebuild (cache deleted, no resume) now
completes in **0.01 s** with no bypass warning, where before it raised
`unrecognised d` and dropped to the pure-mpmath loop. On the real ⁴He word the
native path likewise accepts it — 47 crossings, 9 averaged, **2 distinct
shifts**, confirming directly that an atomic braid mixes conventions.

**⁴He is still not rebuilt, and it is not a bug.** The native call runs rather
than raising, but H_12 at 50 dps is genuinely expensive: dim reaches ~7700, so
O(dim²·word_len) per partition over 77 partitions is hours. The
"sub-millisecond" figure in the source docstring compares direct substitution
against the 2^k expansion, not against zero. The legacy `-numeric` witness
records `compute_time_sec: 1033`, which is the right order.

### The committed caches are colour-weighted after all

I suspected they had been built colour-blind and labelled otherwise. Testing it
refuted that. Computing χ^λ(β_D) both ways at H_6 and comparing against the
committed cache:

| computed as | Σ\|diff\| vs committed |
|---|---|
| colour-blind | 3.13e-03 |
| colour-weighted | **4.23e-06** |

So the `colour-weighted-averaged-crossing` label is honest. The residual 4e-6
is the anchor: the committed cache is colour-weighted at the **muon** q₀, the
rebuild colour-weighted at **proton**. That also settles the earlier worry that
a mislabelled convention was lurking — it was not.

### Two classifier defects the rebuild exposed

Neither would have been found by a synthetic test; both came from classifying a
real regeneration.

1. **`engine` vetoed a genuine migration.** The deuteron rebuild's numerics were
   inside the bound and the q₀ flip was present, but `engine` changed from the
   fallback label to the native one and the classifier rejected on "a
   non-numeric field moved". `engine`, `_provenance` and
   `convention_inferred_by` are now metadata. `convention` deliberately is
   **not** — a colour-blind/colour-weighted change is worth 182 ppm in
   tr_M(4He) and must surface as `VALUES`.
2. **Anchor *labels* were not read as evidence.** `q0Anchor` carries "muon" /
   "proton" directly, which is stronger evidence than a numeric prefix, yet a
   change there was treated as a disqualifying string move. Now recognised
   (including `ideal_muon`), with reverse flips still rejected.

13 self-tests.

**The deuteron rebuild is still not committed**, and correctly so: its
`q0Anchor` goes `"ambiguous"` → *absent*. That is not a value change but it is
a provenance *loss*, and the classifier refusing it is the desired behaviour
rather than another special case to carve out. Why the rebuild drops the field
is the next thing to look at — not more classifier exceptions.

## P46 — the wave driver, committed and with its two bugs fixed

`witness_regen_wave.py` replaces the scratch driver. Both of that script's
failures came from it being a scratch script:

1. **It was bypassed.** Running producers by hand and then `git add -A` staged
   four unreviewed witnesses, one a 13/77 partial cache captured mid-rebuild.
   A guard outside the path actually used is not a guard.
2. **It discarded its own successes.** Its revert reverted *every* dirty
   witness at the moment it fired, so each `VALUES` verdict wiped the
   `DECLARED` / `ANCHOR_MIGRATION` results before it. It reported
   `DECLARED 26 / ANCHOR_MIGRATION 4` at 90/163 while leaving a clean tree —
   the counters were right and the retention was not.

Both are now structural. Revert takes an explicit path list, never a directory
and never "everything dirty"; `run_one` diffs the dirty set before and after a
single producer so it can only ever judge and revert what that producer
touched. Retention was verified on a 12-producer slice: the driver reported one
keep, the tree held exactly that one, and it survived a later `VALUES` revert
in the same run.

It also **refuses to start from a dirty tree** — it cannot otherwise tell its
own output from someone else's. That guard caught me during this very pass,
when a manual triage run had left `braid-encoding-audit` modified.

### Most of the failure rate was harness error, not defects

The slice initially showed 7 of 12 `FAILED`, which reads like a corpus in bad
shape. Sampling the errors gave one cause:

    ModuleNotFoundError: No module named 'pyhecke'

`pyhecke` (the Python package under `tools/pyhecke`) is a *different* thing from
the `pyhecke_native` extension, and it was simply absent from the child
`PYTHONPATH`. With both in-repo package roots on the path, the same slice gives
`FAILED 5`, and two of the recovered producers now run far enough to be judged
rather than aborting. **A driver that mis-blames its own environment produces
exactly the kind of number that sends someone hunting for bugs that are not
there** — the same failure mode as the earlier "unrunnable" qbeta producers and
the mis-read Python version.

Serial by design, and documented as such: producers write into a shared tree,
so two in flight revert each other's output. That is how the ⁴He rebuild was
clobbered by a concurrent wave earlier in this arc.

6 self-tests, covering the two structural properties rather than the verdict
policy — that lives in `witness_regen_classify` with its own 13.

## P47 — the dropped `q0Anchor`, and why the convention labels cannot be trusted

### The producer never stamped its own provenance

`chi_at_q0_via_hoefsmit_mpfr` imports `WitnessBuilder` and never used it:
`save_witness` hand-built a payload dict. So a rebuild wrote no `scriptHash`,
no `scriptFile` and **no `q0Anchor`** — the committed file's
`q0Anchor: "ambiguous"` had come from a one-off `chi_convention_audit --fix`,
and regenerating silently dropped it. Losing an anchor label is worse than the
stale one it replaced, and it is exactly what the classifier refused the
rebuild for.

Now stamped. `resolve_q0_anchor` reports **"proton"** for this script, so the
rebuild carries a correct anchor where the committed file had only
"ambiguous" — a strict provenance gain.

Three more classifier refinements, each forced by a real regeneration rather
than invented:

- **`ambiguous` → `proton` is a resolution, not movement**, accepted only when
  a numeric q₀ flip is independently present. The reverse (definite → unknown)
  is a loss and stays rejected.
- **`scriptFile` is metadata here** by separation of concerns, not
  indifference: `witness_provenance_audit` is what polices whether a
  scriptFile claim is *true* (it found five false ones); this classifier only
  answers "did a VALUE move", and a stamp adding the field must not veto an
  otherwise-clean run.
- With those, the deuteron rebuild classifies **`ANCHOR_MIGRATION`**: 37 fields
  moved, one flip, `tr_M` shifting 2.18e-07 — the muon→proton amplification,
  comfortably inside the 1e-5 bound. 15 self-tests.

### The `convention` labels are wrong, which changes the 4He question

I previously reported that only 1 witness of 28 uses
`colour-weighted-averaged-crossing`, and framed repointing 4He as moving it
onto a one-off. **That framing was built on labels, and the labels are not
reliable.**

The `-at-q0-50dps` family declares:

| count | `convention` |
|---:|---|
| 11 | `averaged-crossings` |
| 8 | `sign-only-crossings` |
| 1 | `colour-weighted-averaged-crossing` |
| 1 | `bring_color_weighted-averaged-crossings` |

But the deuteron witness in that family declares `averaged-crossings` while its
**values are colour-weighted** — computing χ^λ(β_D) both ways against it gives
4.23e-06 for colour-weighted against 3.13e-03 for colour-blind. The label says
one thing and the numbers say another, and the numbers are what the pipeline
actually computes: `_avg_color_delta` has 16 live consumers and installs the
colour-weighted crossing wherever it imports.

So the open question is **not** "should 4He be colour-weighted like the rest of
the corpus" — the corpus already *is* colour-weighted where it matters, and its
`convention` strings simply lag the code. The real defect is that a field
intended to record the convention does not, which makes every survey over it —
including mine — worthless until the labels are re-derived from the values
rather than trusted. That is a labelling repair, not a physics decision, and it
should be settled before anyone reads those strings again.

## P48 — the q_inv gate is not a mechanical copy, and probe_9b was never broken

Two corrections to the "port the remaining two gates" item.

### `probe_9b_laurent_degree_10a5` already handled colour weighting

I listed it as carrying the same three-way limitation. It does not — line 124
reads:

```python
elif abs(d_f - _D_PN_F64) < 1e-9:
    d = -H_SYMB * (sp.Rational(1, 2) - DELTA_SYM / 4)
```

It is a *symbolic* (sympy) path that already knows the colour-weighted p–n
crossing, and its `unrecognised d` raise is a genuine catch-all for a fourth
unexpected value rather than the defect fixed elsewhere. Grepping for the error
string found a match; reading the file found a different situation.

### The q_inv port was wrong, and nearly shipped a 3× error

Porting `chi_at_q_inv_via_native_mpfr` looked mechanical — same shape, same
call, same `{0, −h0, −h0/2}` snap. It ran, it was fast, and every one of the 11
deuteron partitions changed:

    chi[(6,)]   6.7692509169991208562  ->  2.1105940824945303718

A convention change is 4e-6 here. A factor of three is not a convention; it is
a wrong answer. The cause:

    h at q_0     =  0.209060298795639315
    h at q_0^-1  = -0.209060298795639315   (= -h0)

The producer evaluates at **q₀⁻¹**, so the `h` Rust derives internally is
`−h₀`, and the native default shift for an averaged crossing is `−h₀/2`. But
the `d` values in the braid word are expressed at **q₀**, so the old code
mapping `−h₀/2 → sign 0` was deliberately letting Rust re-derive the shift at
the inverse point. Passing `−d = +h₀/2` explicitly overrides that with the
wrong sign.

Reverted. The q_inv path needs its shift expressed at q₀⁻¹, which is a
semantic question about what a colour-weighted crossing means under
q → q⁻¹ — not something to infer from the q₀ code. **The Rust groundwork
serves it; the Python port does not transfer.**

Worth stating plainly because it is the second time in this arc that "the same
error string" turned out not to mean "the same bug", and the first time the
classifier's `VALUES` verdict caught a genuine error of mine rather than an
expected migration. A 4e-6 expectation is what made a 3× result obviously
wrong; without a calibrated sense of the right magnitude it would have looked
like just another regeneration.

## P49 — measured, not surveyed: every distinguishable χ cache is mislabelled

`chi_convention_from_values_audit.py` recomputes each atom's χ^λ both ways and
asks which one the stored values match, instead of reading the `convention`
string. Read-only — it writes no witness, so it is safe beside a running wave.

| atom | claims | Σ\|diff\| blind | Σ\|diff\| weighted | verdict |
|---|---|---|---|---|
| proton | `averaged-crossings` | 3.31e-07 | 3.31e-07 | `INDISTINGUISHABLE` |
| neutron | `averaged-crossings` | 2.68e-07 | 2.68e-07 | `INDISTINGUISHABLE` |
| deuteron | `averaged-crossings` | 3.13e-03 | **0.00e+00** | **`MISLABELLED`** |
| tritium | `averaged-crossings` | 1.52e-02 | 3.22e-05 | **`MISLABELLED`** |
| helium-3 | `averaged-crossings` | 1.94e-02 | 4.05e-05 | **`MISLABELLED`** |

**Every atom where the two conventions differ at all is mislabelled**, by two to
three orders of magnitude. Not one carries a correct label. proton and neutron
are not counter-examples: A=1 atoms have no inter-nucleon crossing, so the
colour-weighted substitution has nothing to act on and the conventions are the
same computation — decided structurally (zero p–n crossings in the word) rather
than by comparing floats, since a string-passed shift and an internally derived
`h/2` differ in the last bits.

deuteron reads `0.00e+00` because it was regenerated through the now-working
native path earlier in this pass — an exact reproduction, which is the
strongest possible confirmation that the stored values are colour-weighted.

### This inverts the question I put to the owner

I asked whether ⁴He should keep `colour-weighted-averaged-crossing` or revert
to `averaged-crossings` "like the rest of the corpus", on a survey showing 1
colour-weighted against 11 averaged. **⁴He was not the outlier — it was the
only one telling the truth.** The other labels say colour-blind while the
numbers are colour-weighted, so the survey counted labels that describe nothing.

There is accordingly no physics decision to make here: the corpus computes
colour-weighted throughout (`_avg_color_delta`, 16 live consumers), ⁴He's label
already matches its values, and what remains is repairing four wrong strings.
That is a labelling fix, and it should be done from measurement — this tool —
rather than by hand, since hand-labelling is how they came to be wrong.

⁴He itself is not in the table: at H_12 each measurement is a full 77-partition
recompute, hours per convention. It is the one atom whose label was never in
doubt anyway.

## P50 — the evidence gate cannot fire for half the corpus

The wave's early counts showed `VALUES` at 9 of 20 — a rejection rate high
enough to be suspicious rather than informative. Measuring the cause:

| declaring producers with a locatable witness | 115 |
|---|---:|
| witness carries a q₀-valued field | 56 |
| **carries none** | **59** |

`ANCHOR_MIGRATION` is evidence-gated: it requires seeing a q₀-valued field flip
muon → proton. **For 59 of 115 witnesses there is no such field to flip**, so a
genuine re-anchoring can only ever classify `VALUES` and be reverted. The
verdict added to stop the guard discarding correct migrations still discards
them for half the corpus.

That gating was a deliberate choice, made because "small movement" alone cannot
distinguish an anchor shift from a crossing-convention change. But the numbers
now say the bound does separate them: an anchor migration moves ~1e-7 relative,
the convention moves 1.8e-4, and the collateral ceiling already sits at 1e-5
between the two. So for a witness with no q₀ field, the available evidence is:

- `resolve_q0_anchor(producer)` reports **proton**, so a re-anchor is expected
  on any re-run; and
- every moved field is inside the 1e-5 bound, which excludes the convention
  change by an order of magnitude either side.

That is weaker than seeing the flip, and it should not be laundered into the
same verdict. The right shape is a distinct `ANCHOR_MIGRATION_INFERRED` that is
**reported but not auto-kept** — surfaced for a human rather than silently
committed or silently reverted.

**Deliberately not implemented in this pass.** Changing what the guard keeps,
while a wave is running against it and without measuring the outcome, is the
same move that produced every self-inflicted problem in this document. The
finding is the deliverable; the verdict needs its own pass with before/after
counts.

Two smaller gaps surfaced with it, both in the driver rather than the policy:
it reports counts but not *which* witnesses were rejected or why, which is what
made a 45% rejection rate uninvestigable without this separate measurement; and
witness-to-producer matching is by stem, so the 48 producers whose witness name
does not derive from the script name were not measurable here at all.

## P51 — the driver now keeps its evidence, and P50 survives a fuller measurement

### 95 rejections that could not be investigated

The first full wave reported `DECLARED 37 / ANCHOR_MIGRATION 5 / VALUES 59 /
FAILED 36 / NOCHANGE 26` and nothing else. Those 95 rejections were
**uninvestigable**: the witness is reverted moments later, so no artefact
survives, and the counters recorded neither which producer nor which field
triggered the verdict. Answering "why is the VALUES rate 45%" needed a separate
measurement pass — for evidence the driver had held in its hand and discarded.

Every producer now yields a record: verdict, the witnesses it touched, the
classifier's own `reason`/`sample` per rejection, and for a failure the exit
code (or `timeout`) with the last line of stderr. That last field is not
incidental — the dominant failure in the first wave was
`ModuleNotFoundError: No module named 'pyhecke'`, pure harness error, and the
counts alone could not tell it from 36 real defects.

Two details worth recording because they are easy to get wrong:

- **`TimeoutExpired.stderr` is raw bytes even under `text=True`**, because the
  exception is raised inside `_communicate` before the decode step. Assuming
  `str` loses the stderr of exactly the runs that hung — the ones hardest to
  diagnose afterwards.
- **The report is rewritten after every producer**, atomically. A 163-producer
  wave runs for hours; a report that only exists on clean exit is missing
  precisely when something went wrong enough to interrupt it.

The `VALUES` histogram keys on the *cause* rather than the field, so the P50
finding surfaces as one line instead of hiding behind 59 distinct field names.
21 self-tests (was 6), including the pure `roll_up` partition and a stubbed
end-to-end `main()` that spawns no producer.

### P50 re-measured over the fuller producer set

P50's denominator came from matching witnesses to producers by filename stem,
which missed 48 producers. All 48 are now resolvable — reusing the existing
machinery rather than a new resolver: `builder_names` (including f-string
patterns), the `written_filenames` dataflow resolver, and the `scriptFile`
back-reference filtered through `classify(...) == "WRITES"`. 44 have a committed
witness; the other 4 resolve cleanly by name but their witness has **never been
committed**, which is a finding rather than a resolver failure. Recovery was two
independent routes agreeing, with **zero witnesses claimed by more than one
producer** across all 278 — the check against f-string over-matching.

Measured pinned at `13ff8207`, never the working tree:

| | producers | q₀ field | none |
|---|---:|---:|---:|
| stem only (P50 baseline, reproduced exactly) | 115 | 56 | **59** |
| newly recovered | 44 | 25 | **19** |
| **fuller set** | **159** | **81** | **78** |

**78 of 159 (49%) against the reported 59 of 115 (51%).** The evidence gate's
inability to fire for roughly half the corpus was *not* an artefact of the
incomplete sample — a stronger statement than the original, and the figure any
`ANCHOR_MIGRATION_INFERRED` sizing should quote. The per-witness view (278, 79
without) is skewed by `canonical_isotope_witness.py`, a genuine per-Z shard
producer emitting 120 witnesses; excluding it gives 158 with 78 lacking a q₀
field, matching the per-producer figure.

## P52 — `ANCHOR_MIGRATION_INFERRED`, and two defects only measurement found

The verdict P50 asked for: where a witness carries no q₀ field to flip, infer a
migration from the producer resolving to `proton` plus every moved field sitting
inside the 1e-5 collateral bound. Reached only on the `not flips` branch — the
exact point the old rule returned `VALUES` unconditionally. **Not auto-kept**:
the driver's `KEEP` is exact set membership, so INFERRED lands in `drop` and is
surfaced for review, which needed no driver edit and is pinned by a self-test.

32 self-tests (was 15), all originals kept verbatim. The negatives matter more
than the positives: a convention-sized 1.8e-4 move → `VALUES`; a witness that
*does* carry a q₀ field → strict path → `VALUES`.

### The impact number is unmeasurable, and was not estimated

The wave reverted its 59 `VALUES` witnesses per file before they ever reached
the object store, and the log holds only totals. Those pairs exist nowhere
readable. What could be measured, all read-only from git:

- **Regression on the wave's own 42 pairs** (`13ff8207^` → `13ff8207`): 37
  DECLARED / 5 ANCHOR_MIGRATION under both old and new rules. Zero drift.
- **All 1287 commits, 222 real witness pairs**: VALUES 140 → 138, INFERRED 2
  (1.4%). Everything else unchanged. Of the 138 declining: 55 carry a q₀ field,
  34 moved a non-numeric field, 24 moved nothing numerically, 19 name no
  producer, 6 exceed the bound — and those 6 are 0.0019–2.8 relative, ≥190× the
  bound. **Nothing sits near the threshold**, which is the property that makes
  the bound safe rather than lucky.

History is dominated by hand-authored physics changes rather than producer
re-runs, so 1.4% bounds false-positive risk, not the wave conversion rate.

### Two defects the measurement caught

1. **float64 de-padding read as an anchor migration.** Commit `0de68792`
   ("strip float64 padding… no value moved") rewrites
   `2.029883212819307392038581383530981838703155517578125` as
   `2.0298832128193074` — different text, *identical* float. 24 of its 58 files
   classified INFERRED. A fourth gate (largest relative move strictly > 0) fixes
   it. Fitting that the padding drain this whole document is about turns out to
   be the thing most easily mistaken for a migration.
2. **The verdict would never have fired.** `witness_regen_wave` builds a
   PYTHONPATH for producer *subprocesses*, but calls `classify` in its own
   process, which has only `computations/` on `sys.path`. The resolver returned
   `None` for every producer and collapsed silently back to `VALUES` —
   indistinguishable from the verdict correctly declining. Shipped as-is it
   would have looked like a well-behaved gate that simply never applied.
   `_resolve_anchor` now falls back to the in-repo substrate path.

### Two things left open

- **Gate 2 filters nothing today.** Of 163 declaring producers, 13 resolve to
  muon and all 13 carry a q₀ field, so gate 1 already stops them. Kept — the
  manifest is editable and it is the condition the verdict claims — but the
  numeric gates do all the discriminating, and that is documented in-code
  rather than left to be rediscovered.
- **A one-producer disagreement on the stem-only baseline.** The agent measured
  55/60 where P50 and an independent re-measurement both give **56/59**; a third
  measurement here, pinned at `13ff8207`, also gives 56/59. Immaterial — both
  cite the fuller 78 of 159 — but the baseline should not be quoted again until
  someone names the producer.

## P53 — ⁴He rebuilt in 20 minutes, and the label bug was in the producer

The colour-weighted native path turned an "hours, dedicated run" job into
**1218 s** — 1199 s of it a single `chi_lambda_all_partitions_mpfr` batch over
all 77 partitions, no bypass warning, 9 of 47 crossings taking explicit
`avg_shifts`. The earlier estimate of hours measured the pure-mpmath fallback,
not the fixed path.

| | value |
|---|---|
| new `tr_M_at_q0` | `0.055358408216379032879226444353999291113592115895273` |
| old (`13ff8207`) | `0.055358426266783106464808452739349303052129025560984` |
| relative change | **−3.26e-07** |
| q₀ shift muon→proton | −1.15e-08 → amplification **28.3×** |

`q_0_50dps` carries the proton prefix, `q0Anchor` reads `proton`, `scriptHash`
is stamped. Largest per-λ move 1.99e-6, everything inside the 1e-5 bound. The
numerics are a clean anchor migration.

### The classifier still said VALUES, and it was right three times over

Peeling the diff back: normalise the `by_partition` ordering and drop the new
`dim` field → still `VALUES`; drop the fields the rebuild loses → then
`ANCHOR_MIGRATION`. Three structural problems, not one:

1. **Partition order changed and entries gained `dim`/`compute_time_sec`.** The
   classifier flattens `by_partition` positionally, so a reorder alone
   misaligns all 77 entries.
2. **`convention` regressed** — and this is the important one.
3. **Fields present at HEAD are dropped**: `producer`,
   `tr_M_markov_peel_xref`, `tr_M_dual_path_rel_gap`, `n_partitions_total`,
   `partial`. `save_witness`'s payload simply does not emit them.

### The mislabelling was never in the witnesses

`save_witness` **hardcoded** `"convention": "averaged-crossings"` — in both
payloads — while `build_chi_cache_at_q0` installs the colour-weighted p–n
crossing thirty lines above. Every A≥2 cache therefore shipped a label
contradicting its own numbers, which is precisely what
`chi_convention_from_values_audit` had to detect by recomputation.

So repairing the three mislabelled witnesses by hand would have been **undone
by the next rebuild** — and this very rebuild proved it, regressing ⁴He's one
*correct* label to `averaged-crossings`. Fixing witnesses while the producer
re-asserts the wrong string is a treadmill.

The label is now **derived from the word**: count the crossings the
colour-weighted substitution actually replaced, and label accordingly. A=1
atoms have none, so colour-blind stays honest for them — counted rather than
assumed from the atom. Confirmed end to end against the independent audit:

    proton     averaged-crossings                 INDISTINGUISHABLE
    deuteron   colour-weighted-averaged-crossing  AGREES

deuteron classifies `VALUES` on that rebuild, which is the guard working as
designed: `convention` is deliberately outside `META`, so a convention change
must surface for review rather than pass as metadata. It is committed here with
that justification and an independent measurement behind it, not waved through.

## P54 — labels repaired, the gate taught, and a correction to P47

Tritium and helium-3 repaired to `colour-weighted-averaged-crossing`; all three
now read `AGREES` under the values audit. The deuteron's repair is the
producer's, not a hand-edit, since the derived-label fix regenerated it — and
`convention_inferred_by` is deliberately kept on the two hand-set labels and
absent from the deuteron, so the asymmetry itself records which is which.

### Correcting P47

P47 said, of the deuteron: *"the `colour-weighted-averaged-crossing` label is
honest… that also settles the earlier worry that a mislabelled convention was
lurking — it was not."* **The cache declared `averaged-crossings` at the time.**
The residuals were read correctly and the label was read backwards, so a
sentence claiming the labels were fine sat directly beneath the measurement
proving three of them wrong. It is true of the deuteron now, for the first time,
and only because the producer was fixed.

### The gate asserted the wrong convention for the whole family

`chi_convention_audit` had `KNOWN_CONVENTIONS = {sign-only, averaged}` and both
`PRODUCER_CONVENTION["chi_at_q0_via_hoefsmit_mpfr.py"]` and the
`^chi-.*-at-q0-50dps$` pattern asserting `AVERAGED`. So it **agreed with the
wrong string** for every A≥2 cache, and adding the new vocabulary alone would
have converted that silent agreement into a CRITICAL mismatch — the repair
turning a green gate red for being correct.

Both are now word-dependent sets: this family substitutes the colour-weighted
crossing only where a p–n interface exists, so A=1 atoms and every `-free-`
word are honestly `AVERAGED` while A≥2 atoms are `COLOUR_WEIGHTED`. The gate
rejects strings outside the vocabulary; deciding *which* applies belongs to
`chi_convention_from_values_audit`, which recomputes instead of asserting.
`mismatch (CRITICAL)` returns to 0, with the one pre-existing
`unknown-convention` (`bring_color_weighted-…`) untouched.

Note the gate reads `producer` or `scriptFile`, and the rebuilt caches carry
neither — `stamp_staleness_metadata` does not set them — so expectations come
from the computation-id pattern. That is why fixing only the producer map would
not have been enough.

### The `-at-qinv-` family is correctly labelled, which vindicates a revert

Measured: colour-blind reproduces `chi-{deuteron,tritium,helium-3}-h*-at-qinv-`
to **exactly zero**, so `averaged-crossings` is right there. Not an accident —
`chi_at_q_inv_via_native_mpfr._word_to_signed` collapses every crossing to
±1/0 and passes no shift, letting the kernel derive −h/2 itself.

That is independent confirmation that reverting the q_inv port (P48) was
correct. Had it shipped, it would have made this family colour-weighted and
broken labels that were already right — a 3× error in the values *and* a
regression in the labels. The same sign trap caught the measurement too: a
first pass weighting with h(q₀) while evaluating at q₀⁻¹ produced a residual of
2.8e+01, a sign error masquerading as a decisive rival, until the word was
rebuilt at the evaluation q.

Also measured and needing nothing: dineutron, diproton and every `-free-` word
carry zero colour-weighted crossings, so the conventions coincide
(`INDISTINGUISHABLE`). And the proton/neutron residual floor of ~3e-07 is not
noise — those caches still store the muon-pinned q₀ while the audit recomputes
at the proton pin. The convention signal is ~500× larger, so the verdicts
survive it comfortably.

## P55 — ⁴He lands proton-anchored, and a classifier gap worth naming

Rebuilt against the fixed producer: 77/77, `convention`
**`colour-weighted-averaged-crossing`** restored *by derivation* rather than by
hand, `q0Anchor: proton`, `q_0_50dps` on the proton prefix, `scriptHash`
stamped. `chi_convention_audit` holds at `mismatch (CRITICAL): 0`.

Verified key-matched against HEAD rather than positionally:

| | |
|---|---|
| partitions | 77 → 77, identical set |
| largest per-λ relative move | 1.99e-06 at λ=(7,4,1) — inside the 1e-5 bound |
| `tr_M` relative change | 3.26e-07 |
| convention | unchanged (the regression never reached a commit) |

A clean anchor migration.

### The classifier still calls it VALUES, and that is a real gap

`reason: non-numeric change at by_partition[0].dim`. The rebuild reorders
partitions and each entry gains `dim` and `compute_time_sec`; `flatten` walks
lists **positionally**, so a reorder alone misaligns all 77 entries and one
added key is enough to veto. Peeling it back — sort `by_partition` by λ, drop
the added keys — yields `ANCHOR_MIGRATION`.

So the verdict is honest about what it saw and wrong about what happened. The
fix is to key list-of-record fields by their natural identity (here
`partition`) instead of by index, which would also stop a producer that merely
reorders its output from reading as 561 moved fields. **Not done here** — it
changes what the guard accepts, and doing that at the end of a long pass
without before/after counts across the corpus is the move this document keeps
recording the cost of.

Committed on the key-matched evidence above, with the limitation stated, rather
than by relaxing the guard to make a green light appear.

## P56 — the guard walks down to the real defect

Three fixes, and the order they surfaced in is the point: each cleared a layer
of schema churn and exposed the next, until what was left was a genuine data
loss.

### 1. Lists were addressed by position

`flatten` walked lists by index, so the ⁴He rebuild — which reorders
`by_partition` and gives each entry a `dim` — misaligned all 77 entries at
once and reported **560 moved fields**, rejecting on `by_partition[0].dim`. The
verdict was honest about what it saw and wrong about what happened; any
producer that merely reorders its output would read the same way.

Records carrying an identity key are now addressed by it —
`by_partition[partition=(7, 4, 1)].chi_lambda` compares like with like whatever
the order. Lists without one keep index addressing, which is right for
genuinely positional data, and duplicate identities fall back to index, since
collapsing two entries loses a field and that is worse than misaligning one.
560 → 241.

### 2. An added field is not a moved field

`dim` did not exist before, so it cannot have *moved*. Vetoing on it rejects a
clean migration for enriching its own output. Additions are now skipped on the
anchor path — and removals are the opposite, a rejection, which is what
surfaced the actual bug:

    VALUES  field removed at n_partitions_total

`description` also went to `META`, and the list now carries **the principle**
rather than growing until the light turns green: *a field belongs in META when
it describes how, when or by what the computation ran — never what it
computed.* `convention` fails that test and stays out; it changes what the
numbers mean, worth 182 ppm.

### 3. The rebuild was shrinking its own witness

`save_witness` dropped seven fields HEAD carried. Two (`scriptFile`,
`_provenance`) are metadata. Three — `producer`, `n_partitions_total`,
`partial` — are real and now restored: the last two are how a consumer tells a
complete cache from a resumed one, and `producer` is the first thing
`chi_convention_audit._producer_field` reads, which is why that gate had been
falling through to a computation-id pattern.

**Two are not restored, and must not be faked.** `tr_M_markov_peel_xref` and
`tr_M_dual_path_rel_gap` came from a cross-check the current producer does not
compute — `tr_M_via_wenzl_bridge_mpfr` returns no such values. Inventing them
to make a diff clean would be fabricating a cross-check that never ran. That is
a genuine capability regression in the producer, recorded here rather than
papered over.

### A fourth verdict: `SCHEMA_GAIN`

A diff that only *adds* fields moved no value. Restoring the three above
produces exactly that shape, and calling it `VALUES` would report a strict
provenance gain as drift. **Reported, not auto-kept** — an added field could
still carry a wrong new value, and this verdict certifies only that nothing old
moved. `KEEP` is unchanged, so the driver still reverts it for a human to look
at.

40 self-tests (was 32), including the negatives that keep each rule honest: an
addition *alongside* a real move is still `VALUES`, a reordered list hiding a
real move is still caught, and a removed field is still a loss.
