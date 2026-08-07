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

**`mpf(<float out of JSON>)`** — `json.load` yields Python floats, and wrapping
one in `mpf` promotes 53 bits to 50 dps:
`v_hat_to_delta_lambda_bridge.py:125-127,152-153`, `xi_ell_phi_q_probe.py:181`,
`phi_q_spectral_combiner_probe.py:107,109`, `rho_k_h3a_lp_dual.py:403,420`.

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
silently misread" (bean `tnjb`), `computations/audits/q0_anchor_consistency_
audit.py` enforces it, and `WitnessBuilder.build()` contains code that sets
`q0Anchor` unconditionally with `"proton"` as the fallback — yet this path
does not reach it. Reproduced twice; the cause is **not** pinned down here.

The consequence is the load-bearing part: **the drain plan for this bean ends
in "re-run the producers", and doing that naively strips q₀ provenance from
every witness it touches** — a value-preserving change that silently removes
the guard against the exact misreading it was added to prevent. That has to be
diagnosed before any witness is regenerated, and it is why this fix is
source-only.

## What remains

Localization is done: all 19 re-padders are measured and every Class A field
has a named source line. What is left is the per-file *judgment*, which is
where this document said the non-mechanizable part lived all along.

- **Blocking everything below: witness regeneration loses the q₀ pin.** See the
  section above. No witness should be regenerated until that is diagnosed.
- **Class A — 10 producers, 189 fields, three library-level entry points.**
  `hecke_characters.py:214`, `hoefsmit_numpy.py:161`, and the
  `mpf(<float out of JSON>)` idiom. All three are deliberate f64 kernels, so
  the fix is "serialize at true precision", not "recover lost precision".
  **71 of the 189 are done** (`chirality_avg_content_atomic`, above).
  `rho_k_co_casimir_extended` (71) is the same shape one level down, in
  `hoefsmit_numpy.py:161` — a shared helper, so unlike the chirality fix it
  needs its callers checked before the return type is touched.
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

