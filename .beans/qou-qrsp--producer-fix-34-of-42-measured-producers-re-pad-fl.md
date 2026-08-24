---
# qou-qrsp
title: 'PRODUCER FIX: 37 of 45 measured producers re-pad float64 on re-run (qou-gqt5 follow-up)'
status: in-progress
type: task
priority: high
created_at: 2026-08-07T09:01:16Z
updated_at: 2026-08-24T09:34:03Z
---

Follow-up to qou-gqt5 (parent-less: beans disallows task-under-task).
MEASURED, not assumed -- docs/audits/2026-08-07-producer-repadding-empirical-sweep.md
Tool: computations/producer_repad_sweep.py (reproducible; detached worktree).

Commit 4aa48b63 stripped 58 witnesses (452 -> 13 padded fields). The strip is
value-preserving but NOT durable: re-running the producers regenerates 289 of
those fields in ONE pass. 37/45 measurable producers re-pad (82%); 8 could not
be measured at all and are NOT clean.

Consequence, and why this is high priority: the strip drains the ratchet BASELINE
while leaving the defect intact. The gate reads green, the producers still emit
fake precision, and the next routine re-run silently re-pads with no signal. This
is the hand-edit branch of what qou-gqt5 explicitly prescribed ("fix producers to
carry values as strings then re-run -- never hand-edit").

Clean (8, leave alone): binding_a3plus_joint_ji_combiner,
binding_block_multiplicative, binding_depth_stratified, meson_gen3_eta_phi,
probe_k_ud_bring_color_tube_empirical_baseline, probe_k_ud_fractional_and_alt_ansatz,
qbeta_habiro_element_probe, su2_spinor_multiplicity_resolution.
Heaviest re-padders: the qbeta_* and option_e_* families.

Known mechanism -- the mpf(<float-valued NAME>) blind spot, which the source
detector (23075055) documents it cannot catch. Live instance,
binding_factor_f_sequence.py:76:  return mpf(tf) - mpf(ta)   # tf, ta are floats

NOT MECHANIZABLE -- per-file judgment. For each re-padder decide whether the
quantity is GENUINELY float64 (then stop promoting it to mpf) or was DOWNCAST
upstream from full precision (then padding is a symptom and the real defect is the
lost precision). Guessing wrong either fakes precision or hides a real loss. This
is the part worth fanning out across agents; the strip was not.

Blocked in part by qou-wu80 (stale folio-assistant path) and qou-dgkf
(pyhecke_native has no wheel) -- both hide producers from measurement.

## Measured at the source (PR #4677) — "NOT MECHANIZABLE" was half wrong

The localization IS mechanizable: `computations/float64_entry_tracer.py`
patches mpmath's `from_float`/`from_npfloat` and reads off the source line
where a float64 enters. The *judgment* above stays per-file; the hunting does
not. Re-measured: RE_PADS 19 / 228 fields (was 20/229 — the delta is exactly
the one gt_matrix fix). 18 traced, `rho_k_co_casimir_extended` (+71) still
exceeds a 900s budget and is NOT measured.

- **A — float64 really enters (9 producers, 118 fields).** Three idioms, not
  nine investigations: one shared library downcast
  (`hecke/hecke_characters.py:214`, hit 527310x by su4), `mpf(<float out of
  JSON>)` across four producers, and `mpf(<float-valued name>)` — including
  the `binding_factor_f_sequence.py:76` instance this bean already names.
  The largest (chirality, 71) is DELIBERATE f64 — Rust kernel called with
  `precision="f64"`, witness records `kernel_precision: f64` — so the fix is
  to stop serializing 53 bits at 50 dps. Two sites are comparison tolerances
  and must not move.
- **B — no float64 enters at all (9 producers, 39 fields).** Their values are
  genuine computations of exact integers (tr_M(1) = 1 - 1.4e-51). Flagged
  because `is_f64_padded` catches anything within 1e-30 of a double, and so is
  a real padded value truncated at 50 dps (1.56e-50). No static test separates
  them. These need no producer fix.

**`propagated = 0` is refuted.** qbeta_markov_trace_compute_accuracy_diagnostic
regenerates a string already committed verbatim in
qbeta-markov-trace-norm-probe.witness.json. That classifier was never committed
with its claim, so it was never reproducible — the propagated class is
unmeasured, not zero, and an exact-string search over the POST-strip corpus is
biased toward LOCAL by construction.

Next: measure rho_k_co_casimir_extended; re-measure LOCAL vs propagated with a
committed tool; fix the two library-level Class A idioms (source fix and
witness regeneration as separate commits — they change numbers).

## CORRECTION to the section above: `propagated = 0` was NOT refuted

The claim above that `propagated = 0` is refuted was **wrong** and is retracted.
It rested on grepping a worktree this session had itself been running producers
in — the "upstream" witness holding the padded string was this session's own
regenerated output, not the committed corpus. `git show HEAD:` shows only the
short form. That is the failure `producer_repad_sweep.py` warns about in
capitals, committed while cataloguing the same habit in others.

Measured properly with a committed tool
(`computations/witness_padding_provenance.py`, indexes the COMMITTED corpus
before anything runs, excludes the producer's own fresh output), over all 19
re-padders / 218 padded fields:

  VERBATIM_UPSTREAM        0   <- the exact-string result is CONFIRMED
  VALUE_UPSTREAM          37   <- distinctive value upstream, invisible to it
  VALUE_UPSTREAM_ROUND    15   <- matched 1.0/6.0; vacuous, not propagation
  LOCAL                  166

So `propagated = 0` is right about strings and 17% short about values. The
round-number split is load-bearing: without it the gap_a4 near-integers read as
inherited only because `1.0` is everywhere.

The two tools agree and were built independently: where the tracer finds a
local float64 entry, provenance says LOCAL (chirality 71/71); where it finds
none, the value is upstream (qbeta diagnostic 7/7).

## All 19 measured — localization is DONE

`rho_k_co_casimir_extended` (+71), which had defeated the sweep (150s), a
provenance run (240s) and a 900s trace, is one line:

    computations/hoefsmit_numpy.py:161   return mp.mpf(float(np.trace(M)))   x148

numpy matmul at C-level BLAS, trace promoted to mpf, serialized at 50 dps —
the same shape as chirality. Two tracer limits had hidden it, both now flags:
forked `multiprocessing.Pool` workers are invisible to in-process
instrumentation (`--no-fork`), and stack-walking per conversion, not the
physics, is what made it slow (`--budget`). Both hide sites, never invent
them, so a zero only counts when `truncated` is false and the producer does
not fork — the earlier zero for this producer meant nothing.

  A. float64 enters   10 producers  189 fields  THREE library-level sites
  B. no entry          9 producers   39 fields  detector false positives

Class A is `hecke_characters.py:214`, `hoefsmit_numpy.py:161`, and the
`mpf(<float out of JSON>)` idiom — not ten producer-specific bugs. All three
are deliberate f64 kernels, so the fix is "serialize at true precision", which
changes numbers: source fix and witness regeneration stay separate commits.

Class B needs NO producer fix — the values are genuine, the detector is
wrong about them. Do not go hunting for a float64 entry there.

## First Class A fix landed — and a BLOCKER for the regeneration half

`chirality_avg_content_atomic`, the corpus's largest re-padder: all 71 fields
were `per_partition[].chi_lambda_beta` written as `str(<mpf>)` — 50 dps of a
53-bit kernel value. Fixed to `fmt(float(chi_val))`, which is the convention
`fmt()` already documents ("no spurious mpf-promotion noise on a 0.1-style
float"). mpf(float) is exact, so nothing moves.

Verified before/after in a detached worktree: 71 padded -> 0, 0 values moved.
71 of the residual 228 fields, fixed durably at the producer.

**BLOCKER — do not regenerate witnesses yet.** Re-running the producer drops
`q0Anchor` + `q0Value` from the witness. Every number is byte-identical; only
the q0 pin disappears. That pin exists so a muon/proton value can never be
silently misread (bean tnjb), audits/q0_anchor_consistency_audit.py enforces
it, and WitnessBuilder.build() sets q0Anchor unconditionally with a "proton"
fallback — yet this path does not reach it. Reproduced twice; cause NOT pinned.

This bean's plan ends in "re-run the producers". Doing that naively strips q0
provenance from every witness it touches — value-preserving, and silently
removing the guard against the exact misreading it was added to prevent.
Diagnose that first. The chirality fix is therefore source-only.

## BLOCKER RESOLVED — regeneration no longer drops the q0 pin

Diagnosed: not a bug in WitnessBuilder.build(). The q0Anchor code lives in
`stamp_staleness_metadata()`, a SEPARATE method a producer must call
explicitly; build() never touches the pin. Measured over the corpus:

  no pin at all                    2104
  pin + producer stamps it (safe)    36
  pin + producer does NOT stamp     557   <- lost it on every re-run
  unresolved                          3

557 of 596 pinned witnesses (93%) carried a pin their own producer cannot
reproduce. Five of the 19 re-padders are in that set, including both
71-field producers.

Fixed in save(), which already loads the on-disk witness for its drift check:
carry a recorded pin forward. PRESERVE ONLY — a witness with no pin still gets
none, since inventing "proton" for the 2104 would assert a pin no producer
established (Q0_ANCHOR_MISSING is tolerated). Two regression tests; the first
was checked to FAIL without the fix, not merely pass with it.

So "re-run the producers" is now safe to do. That was the last thing blocking
the second half of this bean.

## Second Class A fix — 219 fields done, and 228 was a FLOOR

`rho_k_co_casimir_extended` is not 71 fields, it is **148**. The sweep's 71
came from a run that hit the 150s wall and left a PARTIAL witness; that count
was then carried forward as complete. The sweep is careful that "untested is
not clean" — this is the neighbouring error, half-tested is not measured. So
the residual 228 is a FLOOR, at least 77 short on this producer alone.
habiro_interpolate_cross_validator and rho_k_h3a_lp_dual also died mid-run,
so their counts are lower bounds too.

148 matches the tracer exactly (hoefsmit_numpy.py:161 recorded x148).

The chirality one-liner would have been WRONG here: _chi_worker falls back to
full-precision mpmath `chi_numeric` when numpy is unavailable, so writing
float() unconditionally would discard real digits — the "conceals a real
loss" half of the trap. Decided per value instead: an mpf equal to its own
float64 holds 53 bits and nothing more; otherwise it is written in full.

Verified before/after, BOTH runs to completion (rc=0): 148 padded -> 0,
0 values moved. Source only — the committed witness already carries 0.

Running total: 219 of the Class A fields fixed at the producer.
Next: su4_1111_markov_trace_probe (10, hecke_characters.py:214 root) and the
four mpf(<float out of JSON>) producers.

## Third fix (231 done) — and the "JSON idiom" label was wrong

chirality_avg_content_chiral: 12 fields, same per-value fix as rho_k. It
already records the kernel tag (mpfr_50dps vs f64_numeric_fallback) after a
review caught it claiming precision_dps: 50 on fallback runs — the same
overstatement survived one level down in the serialized value. Verified
before/after, both rc=0: 12 padded -> 0, 0 of 53 numeric fields moved.

Running total fixed at the producer: 231 (71 + 148 + 12).

**Correction:** I grouped four producers as `mpf(<float out of JSON>)`. Only
TWO read JSON. The call sites look alike; the float's ORIGIN differs, and that
decides where the fix belongs:

  phi_q_spectral_combiner_probe   upstream witness (add_upstream)   -> UPSTREAM
  rho_k_h3a_lp_dual               json.loads (occam blob)           -> UPSTREAM
  v_hat_to_delta_lambda_bridge    wedderburn_pair_volumes(), in-mem -> here
  xi_ell_phi_q_probe              per_generator_V_hat_general()     -> here

For the two upstream ones the precision was lost when THAT witness was
written — promoting it here only makes the loss visible, so the fix is
upstream and ordering matters. That is the one place the original "upstream
propagation" reading was pointing at something real.

Caught before any of the four was fixed on the strength of the wrong label.

## 242 fields done; the rule now has one home

v_hat_to_delta_lambda_bridge (6) and xi_ell_phi_q_probe (5) fixed — both take
their value from an in-memory float64 helper (wedderburn_pair_volumes imports
numpy and computes 1.0/(q0**0.5+...); per_generator_V_hat_general is driven by
float braid words), NOT from JSON as the earlier grouping claimed.

Fourth/fifth use of the same rule, so it is now
`qou_substrate.precision.str_at_true_precision`, with 6 unit tests covering
BOTH inverse defects (don't print 50 dps of a 53-bit value; don't shorten a
real full-precision one). The three earlier producers are retrofitted onto it.

TRAP worth remembering: it is a drop-in for `str(<mpf>)` and NOT for
`fmt(<mpf>)`. fmt serializes at OUTPUT_DPS, str at the live mp.dps, and
producers set them differently (compute_dps 70 / output_dps 60 is typical), so
the wrong fallback silently rewrites the digit count of every value the helper
is not meant to affect. A test pins it.

Verified per producer in a detached worktree, every numeric field compared:
xi_ell 40 fields 5->0, v_hat 71 fields 6->0, and the retrofit 201/53 fields
with 0 moved. rho_k's substitution checked by direct equivalence (9 values,
0 disagreements) rather than a 25-minute re-run.

Remaining: su4 (10, floor), binding_factor_f_sequence (2),
bring_homology_pairing_integration (2 real + 2 tolerances that must NOT move),
and the two upstream-sourced ones where the fix belongs upstream.

## binding_factor_f_sequence — the documented blind spot, fixed the OTHER way

The `mpf(<float-valued name>)` instance this bean names. Needs the opposite fix
from the previous six: the input is a decimal STRING from binding_canonical
(mp.nstr at mp.dps) and builtin complex() reads it as binary64. Wrong in both
regimes — a 16-digit string becomes a double whose 50-dps expansion is the
padding, and where a producer writes ~30 digits complex() truncates them. The
corpus carries both populations. mpmathify parses a decimal as a decimal.

I expected it to RECOVER precision and measured instead: the runtime string is
16 digits, so there is none. Right fix, wrong reason.

NOT value-preserving — the first one that isn't. padded 2 -> 0; 1 of 34 fields
moved, rows[4].delta_tr by 4.2e-17 relative = exactly 1 ulp, the width of the
binary64 rounding that should never have been there. Source only; witness
regeneration is separate BECAUSE a number moves.

## FOURTH mechanism: `mp.dps = 50` that is a no-op

bring_homology_pairing_integration.py line 7: `import mpmath as mp` then
`mp.dps = 50` sets an attribute on the MODULE. Precision lives on the context
— `mp.mp.dps`. The whole file ran at mpmath's default 15 and printed 40 digits.
Not a serialization choice, not a bad parse: precision never raised.

Fixed and verified: padded 4 -> 0, and all four fields now match their closed
forms to every digit written (pi/20, 12pi, 2/(3pi)). |ratio - target| goes
6.94e-16 -> exactly 0 at 40 digits, against a 1e-10 assertion tolerance loose
enough to hide it indefinitely. Values move ~3.2e-15 = the 15-vs-50 gap.

All three tracer sites in that file were red herrings (two comparison
tolerances, one float mpmath computes inside mp.quad).

**FOUR MORE PRODUCERS HAVE THE SAME NO-OP — unfixed:**
  computations/qbeta/h5_wedderburn_tension_hp.py:11
  computations/qbeta/qbeta_h4_em_normalization_probe.py:11
  computations/qbeta/qbeta_h4_sign_block_exact.py:11
  computations/qbeta/qbeta_h4_sign_block_proof_search.py:11

None is among the 19 re-padders — they were never in the stripped-witness
cohort, so the sweep never reached them and their witnesses are unchecked.
Patched then REVERTED: none runs in this container (ModuleNotFoundError:
qou_substrate — they lack _path_bridge), so the change could not be verified,
and an unverified value-changing edit is what this bean argues against.
One line each; the finding is certain, the verification is what is missing.

## The four qbeta no-ops: fixed and verified after all

Recorded last round as unrunnable (ModuleNotFoundError: qou_substrate). That
was the CONTAINER missing the package, not the producers — with
PYTHONPATH=tools/qou-substrate/python all four run clean. "Cannot run here"
deserves the same suspicion as "untested is not clean"; only trying it settled
it.

All four rc=0 before and after, and all four CHANGE OUTPUT, so the no-op was
live in each (26/34/12/14 lines). Recovered precision, not moved results:
  q0 (anchor) = 1.10997858275138
             -> 1.1099785827513808075916690956107688798744991218736
= exactly Q_50_DIGIT_STR.

NONE emits a witness, so this adds no padded fields and does not move the
drain count — but any conclusion drawn from their output past 15 digits was
unsound.

## The mp.dps no-op class is INVISIBLE to the padding gate — 7 instances

Completed the sweep: 7 total, 2 found only after matching INDENTED imports
(inside `try:`). All fixed and verified.

  bring_homology_pairing_integration.py:7      witness, 4 padded
  e_hartree_round22_arch_bridge.py:69          witness, 0 padded (8 values gained digits)
  e_hartree_round23_normalization.py:68        witness, 0 padded (no observable change)
  qbeta/h5_wedderburn_tension_hp.py:11         no witness
  qbeta/qbeta_h4_em_normalization_probe.py:11  no witness
  qbeta/qbeta_h4_sign_block_exact.py:11        no witness
  qbeta/qbeta_h4_sign_block_proof_search.py:11 no witness

ONLY 1 OF 7 PRODUCED PADDING. At dps=15 `str(<mpf>)` prints ~15 digits and
is_f64_padded needs >=20 fractional digits before it even looks — so the no-op
hides from the audit that would catch it. bring_homology surfaced only because
it writes mp.nstr(..., 40).

The two defects are near-orthogonal: padding = claims MORE precision than it
has; no-op = silently carries LESS than asked. The corpus is swept
exhaustively for the first and never for the second. WORTH A GATE — the
detector is static and cheap (see the audit doc for the regex). Match indented
imports, and skip docstrings (qbeta_5two_phi_series_engine_probe mentions
"mp.dps = 60" in prose).

## END-TO-END RE-MEASUREMENT (same tool that set the baseline)

  RE_PADS      19 -> 12
  CLEAN        26 -> 32
  padded      228 -> 57

The 7 producers that left the list are exactly the 7 witness-emitting fixes.
Nothing claimed is missing; nothing untouched regressed.

Arithmetic note: sweep says 171 drained, per-producer runs say 248. The gap is
rho_k_co_casimir_extended — the sweep only ever credited it 71 (a 150s-timeout
partial); a complete run writes 148. The sweep's baseline was a floor, so its
delta is one too. TIMEOUT 0 -> 1 for the same reason: rho_k still exceeds 150s
but now writes no padding, so RE_PADS no longer outranks its verdict.

REMAINING 57 fields / 12 producers:
  Class B  9 producers, 39 fields  -> NO producer fix. Detector false
           positives (near-integers). Needs a decision about the DETECTOR.
  Class A  3 producers, 18 fields:
      su4_1111_markov_trace_probe   (+10)  hecke_characters.py:214; count is a
                                           FLOOR (both measured runs timed out)
      phi_q_spectral_combiner_probe (+6)   reads upstream witness -> fix UPSTREAM
      rho_k_h3a_lp_dual             (+2)   reads occam JSON      -> fix UPSTREAM


## su4_1111_markov_trace_probe: both halves of its entry above were wrong (2026-08-24)

This bean's "Next" named it as 10 padded fields with `hecke_characters.py:214`
as the root. Measured on a clean detached worktree at origin/main 2c8c27210:

- **It re-pads 0 fields.** The producer already uses `str_at_true_precision`
  (line 399). Someone fixed it and the count here went stale.
- **It CRASHES**, on main and everywhere: `M = c * sigmas[g] + d * I` with an
  mpf `d` hits scipy's `_mul_scalar` -> dtype object -> ValueError.

The crash is invisible to a padding sweep BY CONSTRUCTION — the sweep scores
what a producer writes, and this one writes nothing. `producer_repad_sweep.py`'s
own rule ("CLEAN only if it ran, wrote a witness, and that witness had zero
padded fields") is exactly the guard this case needed, and the stale 10 shows
what happens when a count outlives the run behind it.

Also: the two matrix branches disagreed on the same input. Sparse crashed;
**dense did not** — it silently built an object-dtype numpy array and ran the
whole product in Python-level mpf arithmetic from 53-bit inputs, for no gain.

### Fixed (PR #5623)

`chi_lambda_of_word` is a float64 kernel and `-> float` is the contract: both
branches end in `float(...)`, so no caller ever received >53 bits. Coerce the
word coefficients on the way in. **Measured: 8908 coerced, 2277 lossy, worst
relative loss 2.6e-17** = half an ulp. `chi_lambda_braid_mpf` is NOT a drop-in
alternative — at A=4 the largest irrep is f^lambda = 4158, ~7.2e10 mpf ops per
matrix multiply.

### What the crash was hiding — worth more than the padding

Because it cannot run, nobody could refresh its witness, which is therefore
**three weeks older than the convention-D cascade** (computedAt 2026-07-18;
cascade 2026-08-09) and is convention-C-frame:

    y_lambda [3,3,3,3]   -4.65e-09  ->  0.0
    y_lambda [5,3,3,1]   -1.77e-06  ->  0.0
    full_trM              0.0554    ->  0.1610   (2.9x)

Under D, `_wenzl_X_Q` collapses to X = q^4 = Q^2, integral level r = 2, row cap
l(lambda) <= 2 — y_lambda is EXACTLY 0 at >=3 rows. A nonzero y_lambda on a
4-row partition is only possible under C. That is the module's own docstring.

**The probe's conclusion survives**: verdict DOES-NOT, 3/3 assertions pass in
BOTH frames. The numbers were wrong and the answer was not.

### Generalised into a committed tool

`computations/audits/y_lambda_convention_c_fingerprint_audit.py` tests the
ANSWER rather than the source, since every existing convention detector keys on
how `z` was written and the blindness taxonomy lists thirteen evasions.
origin/main: **15 live files / 267 fields**. Two limits, both in its docstring:
a hit is about the witness not the producer (re-run to distinguish stale payload
from live source defect), and it keys on a FIELD NAME, so files where
`y_lambda` is not the Wenzl y_lambda are false positives it cannot rule out.
Only su4 is hand-confirmed. The other 13 are candidates, not verdicts.

Next on this front: re-run the 13 candidates' producers to split stale-witness
from live-source-defect.


### CORRECTION to the fingerprint count above: 15/267 -> 9/160 (same day)

The tool as first committed tested `y_lambda != 0`. Wrong: "y_lambda = 0 under
D" is ALGEBRAIC, the arithmetic that evaluates it is not, so a correct D-frame
producer writes a residue. Verified against live code, not inferred:

    y_lambda_wenzl_bridge_numeric([4,1,1],   q0, dps=50)  ->   3.229e-52
    y_lambda_wenzl_bridge_numeric([3,3,3,3], q0)          ->  -8.400e-108

Threshold now READ OFF THE DATA. Of 1635 >=3-row values: 1377 exactly 0; the
258 nonzero are trimodal with a 68-decade EMPTY band:

    1e-150..1e-140    17   D-residue (helium-4, 50 dps)
     1e-80.. 1e-70    81   D-residue (chi-* family)
     <<68 empty decades>>
     1e-10..  1e0    160   convention-C scale

C_SCALE_FLOOR = 1e-30, mid-band. The 107 false positives were 6 whole files,
including all 70 fields of chi-helium-4-h12 — correctly D, recording zero as
1e-148.

SHARPER RESULT SURVIVES: the chi-* family is PARTIALLY migrated. deuteron /
dineutron / diproton / helium-4 are residue-scale (D, correct); helium-3 and
tritium are C-scale (25 each). Same producer, same directory, different frames.
The producer's own source independently notes "(deuteron, tritium, helium-3 all
MISLABELLED)".

STRUCTURE — not 9 independent defects. `chi_at_q0_via_hoefsmit_mpfr.py` writes
the roots (chi-helium-3-h9, chi-tritium-h9) and the rest READ them by path:
delta-lambda-categorical-verification (35), probe-d-delta-lambda-terms (7),
gap-a1 (7), he4-binding-k-stage2 + ranking-xcheck (5+5, via y_lambda_at),
mu3-frechet-perblock (50, via y_lambda_at_q0_mpmath). Upstream-first with
ordering — the same upstream/here split this bean already drew. The roots carry
NO scriptFile, so none of it is traceable from the witness.

ALSO: a scan that examined nothing read as a CLEAN TREE. From inside
computations/ the glob matched 0 files and the tool exited 0 saying "0 files
with fingerprint". Now errors, exit 2 — "untested is not clean" applied to the
scanner. I hit that cwd trap myself while measuring, which is how it surfaced.

PR #5623, commit 50015f044.
