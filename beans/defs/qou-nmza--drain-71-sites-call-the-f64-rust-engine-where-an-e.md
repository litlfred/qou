---
# qou-nmza
title: 'DRAIN: 71 sites call the f64 Rust engine where an exact MPFR sibling exists'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T13:16:05Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Opened by the `F64_ENGINE_ENTRY` tier added to
`computations/f64_into_mpmath_audit.py` (2026-08-24). Sibling of `qou-840k`.

## The class

`pyhecke_native` exposes five f64 entry points that each have an exact MPFR
sibling:

    chi_lambda_all_partitions_f64  -> chi_lambda_all_partitions_mpfr
    chi_lambda_braid               -> chi_lambda_braid_mpfr
    chi_lambdas_braid              -> chi_lambdas_braid_mpfr
    chi_q_atomic                   -> chi_q_atomic_mpfr
    chi_q_atomic_all_partitions    -> chi_q_atomic_all_partitions_mpfr

**71 site(s) in 46 file(s)** reach the f64 one, over two hops:

1. **Direct** — `pyhecke_native.chi_lambda_braid(...)`.
2. **Wrapper** — `hecke_characters.chi_lambda_braid(...)` with no
   `precision=`. That keyword selects the path and DEFAULTS to f64; 20 of 30
   wrapper sites omit it.

`_iter_rows` / `--tier F64_ENGINE_ENTRY` gives the live list. Do not re-derive
it by grep — see the two failed censuses below.

## What makes a site actionable (it is NOT "calls the f64 entry")

The f64 entry is ~10-30x faster and is frequently the right choice. Measured
against MPFR at 50 dps, proton q0:

    H3  sigma_1        rel diff 2.917e-16
    H3  borromean-ish  rel diff 7.746e-16
    H6  deuteron-ish   rel diff 7.362e-16

~15-16 real digits. So the defect is **calling it and then serialising the
result at more digits than that**. Triage each site by what it does with the
value, not by the call:

- writes a witness at 30/50 dps  -> **fix**
- feeds a downstream mpmath chain -> **fix**
- a fast scan / ranking / plot    -> **leave, and say so in a comment**

Worked example: `fr-pullback-k1-k2.witness.json` carries **697** numbers at
>=18 significant digits, every one from the f64 path.

## The half-fix that will look like a fix

`precision="mpfr_50dps"` alone is NOT sufficient. The wrapper preserves the
boundary only when `q_value` is a **string**; a float is put through
`format(float(q_value), ...)` first, which the wrapper's own comment calls
"implicit acceptance of f64 boundary loss". Pass `Q_50_DIGIT_STR`, not `Q`.

Cost: the MPFR path is ~10-30x slower (its docstring's figure). Long-running
producers need the compute-audit long-compute logging discipline
(`python3 -u ... 2>&1 | tee /tmp/<script>.log`) rather than a silent re-run.

## Do not re-measure by grep — two censuses were wrong first

Both were mine, in opposite directions:

* **120 sites / 64 files** — regex over call names, which counted **string
  literals**. `closed_form_tau_M.py` declares `PnConvention =
  Literal["chi_lambda_braid", ...]`: convention names, not calls.
* **51 sites / 39 files** — the AST detector before the wrapper hop existed,
  blind to every caller going through `hecke_characters`.

Guard cases for both are in the audit's self-tests (36/36).

## Also corrected

`qou-840k`'s "49 of 116 F64_CAST files use no f64 engine" is **43**, not 49 —
the engine regex behind it had `pyhecke.gram` but not `pyhecke_native`. Six
modules routing through the Rust engine were counted as engine-free. And the
framing was too generous regardless: "f64 engine" exempts a module only when
**no exact sibling exists**. Where one does, it is not an f64 pipeline by
design, it is the wrong entry point.


## CORRECTION to this bean's own headline: 18 actionable, not 71

The title says 71 and that is the CANDIDATE count. Hand-checking two sites
found both legitimate — two for two — so the split is now computed by the
audit itself (`native_entry_disposition`) rather than asserted here:

    deliberate    5 file(s)   7 site(s)  — also calls an _mpfr entry
    harmless     33 file(s)  46 site(s)  — never serialises above 17 digits
    actionable   13 file(s)  18 site(s)  — serialises wide from an f64 value

**The harmless bucket is the larger half.** A drain driven by the bare 71
would have spent most of its effort on modules where the f64 entry is right.

The two that taught this, both of which the proxy now classifies correctly:

* `chi_4he_binding_lossless.py` — calls the f64 entry ON PURPOSE, as a
  same-convention cross-check floor for its own MPFR result. Its comment says
  so. The module name says the opposite of what a raw flag implies.
* `atomic_chirality_residue.py` — `float(mp.log(abs(chi)))` three lines after
  the call. The downstream is f64 throughout, so MPFR buys nothing.

### The 13 actionable candidates

    1x  computations/all_nuclides_wedderburn_spectral_v2.py
    1x  computations/averaged_block_swap_binding.py
    1x  computations/deltalambda/delta1g_deuteron_measurement_probe.py
    1x  computations/deltalambda/gap10_tjon_correlation_probe.py
    1x  computations/deltalambda/mu3_abs_choice_robustness_probe.py
    1x  computations/deltalambda/mu3_anchor_consistency_probe.py
    1x  computations/deltalambda/mu3_frechet_perblock_probe.py
    1x  computations/fr_pullback_cosh_h_test.py
    1x  computations/fr_pullback_k1_k2_test.py
    1x  computations/fr_pullback_k3_test.py
    4x  computations/qbeta/qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py
    3x  computations/qbeta/qbeta_hoefsmit_tbeta_matrix_build_probe.py
    1x  computations/qbeta/qbeta_stage_c_per_block_chi_closed_form_probe.py

Re-derive with `python3 computations/f64_into_mpmath_audit.py`; do not quote
this list once it has aged.

Note the three `mu3_*` probes: `mu3_anchor_consistency_probe.py` is AGENTS.md's
own worked example of a LAYER STRADDLE (11.54 ppb, ideal-muon `y_λ` against a
proton-pinned `χ_λ`). A layer straddle and an f64 boundary in the same probe
means the recorded number has two independent error sources — resolve the
straddle first, since it is ~1e-7 relative and dominates the ~1e-16 f64 floor
by nine orders. Fixing the f64 there first would be measuring the smaller
error while the larger one is live.

### The proxy's known blind spot

It keys on `fmt(` and `nstr(x, N>=18)`. A module serialising some other way
(hand-built f-string at width, `json.dump` of an mpf via `str()`) reads as
harmless. The printed line says "a proxy, not a verdict" for this reason.


## Three sites investigated in depth — three DIFFERENT reasons the naive fix was wrong

This is the most useful thing in this bean. The `F64_ENGINE_ENTRY` flag points
at a real f64 boundary every time; it is almost never the BINDING constraint.
Check all four of these before editing any site.

**1. `fr_pullback_k1_k2_test.py` — TERMINAL.** The single worst site by raw
count: its witness carries **697** numbers at >=18 significant digits, every
one downstream of the f64 entry. Nothing reads that witness. I was three edits
into fixing it when the check said so. Now gate 3 in the audit.

**2. `all_nuclides_wedderburn_spectral_v2.py` — the f64 call is a REFERENCE.**
`ref = float(nat.chi_lambda_braid(...))` exists to cross-check `chi_std`
against the native kernel. The module never calls an `_mpfr` entry, so the
"deliberate" proxy misses it — a known false positive of that proxy.

**3. `averaged_block_swap_binding.py` — the witness is f64 AT THE BOUNDARY
anyway.** Every field is written `float(v)` (`atom_traces`, `S_atom`,
`S_free`, `binding_signal_...`), and the downstream `q_weighted_block_swap.py`
re-lifts them with `mp.mpf(str(v))`. Swapping the engine call to MPFR alone
would have changed **nothing**. The proxy called it actionable because of an
`nstr(total, 40)` inside the multiprocessing worker — an INTERNAL transport
string, not a witness field. Fourth false-positive mode.

**4. The `dim_q` trap** (see the audit's printed HALF-FIX WARNING):
`mass_at_3A_proper.dim_q` / `qfac` return Python floats and multiply into
every weight in the `fr_pullback_*` and `binding_depth_stratified_*` family,
so an MPFR engine swap there is capped regardless. 8 importers.

### The rule this yields

A site is only worth the 30x MPFR cost when the f64 value reaches a **witness
field serialised above 17 digits** that **another module reads**. Fixing the
engine call is one half; the serialisation is the other. **Either half alone
is a defect** — the engine alone changes nothing, the serialisation alone
publishes 50 digits of a 15-digit value.

### Measured cost, so nobody has to guess

`chi_q_atomic_mpfr` vs `chi_q_atomic`, 4He word (47 factors), shape (6,6):

    f64   0.002 s
    mpfr  0.056 s      -> 30.1x  (the docstring's UPPER bound, not its lower)
    rel diff 6.489e-15 -> the f64 result carries ~14-15 real digits

At that ratio the `averaged_block_swap_binding` producer goes 78 s -> ~40 min.
A 600 s timeout kills it; budget 3300 s and use the compute-audit teed-log
discipline.


## Head-of-3 triaged: the real head is 2

Verdicts recorded here because standalone `computations/*.py` has no `.qa.json`
sidecar to hold them.

**`all_nuclides_wedderburn_spectral_v2.py:314` — LEGITIMATE, do not fix.**
The f64 call is a cross-check assertion, and it floats BOTH sides:

    mine = float(m_tr(m))                              # its own mpmath value
    ref  = float(nat.chi_lambda_braid([2, 1], word, qf))
    w.add_assertion(name="chi_std_vs_native_hoefsmit", ..., tolerance=1e-9)

Symmetric f64 for an f64-tolerance agreement test is the correct arithmetic.
Switching to MPFR would tighten the assertion past its intent and change no
published value. This is the second instance of the same class as
`chi_4he_binding_lossless` — the "deliberate" proxy misses both because
neither module calls an `_mpfr` entry anywhere.

**So the actionable head is 2**, not 3:

    gap10_tjon_correlation_probe  -> tjon_external_cross_check_probe
    fr_pullback_cosh_h_test       -> convention_frame_staleness_audit

and `fr_pullback_cosh_h_test` imports the f64 `dim_q` from
`mass_at_3A_proper`, so it carries the HALF-FIX WARNING: the engine swap alone
leaves it capped. Fixing it properly needs an mpf-capable `dim_q` first, which
is its own change with 8 importers.

### Running total for the class

    71  candidates (AST, both hops)
    18  serialise wide from an f64 value
     3  ... and their witness is read by another module
     2  ... and the call is not a deliberate f64-tolerance cross-check

Two of the four reductions came from measurement catching my own over-claim.


## Re-measured 2026-09-13 — the class drained modestly, and the title is still wrong

Run before starting any drain, because the figures above are 20 days old.
`python3 computations/f64_into_mpmath_audit.py --tier F64_ENGINE_ENTRY`:

| bucket | 2026-08-24 | **2026-09-13** |
|---|---|---|
| candidates | 71 sites / 46 files | **63 / 43** |
| deliberate | 7 / 5 | **9 / 6** |
| harmless | 46 / 33 | **38 / 26** |
| **actionable** | **18 / 13** | **16 / 11** |

Modest drain, not a collapse — so the correction this bean already made to its
own headline (71 → 18 actionable) is the one that matters, and **the title still
says 71**. Quote `actionable`, and re-run rather than quoting this table too.

### The priority rule the audit prints, which this bean's body does not

> Fix the propagating ones FIRST — they carry the f64 floor into another
> producer's numbers. A terminal probe publishing 50 digits of a 15-digit value
> is a documentation defect: worth fixing, not worth the 10-30x MPFR cost ahead
> of these.

Of the 16 actionable, **2 PROPAGATE and 9 are TERMINAL**:

    PROPAGATES  1x  computations/all_nuclides_wedderburn_spectral_v2.py
    PROPAGATES  1x  computations/fr_pullback_cosh_h_test.py
    terminal    4x  computations/qbeta/qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py
    terminal    3x  computations/qbeta/qbeta_hoefsmit_tbeta_matrix_build_probe.py
    terminal    1x  computations/qbeta/qbeta_stage_c_per_block_chi_closed_form_probe.py
    terminal    1x  computations/deltalambda/convention_systematic_audit_probe.py
    terminal    1x  computations/deltalambda/delta1g_deuteron_measurement_probe.py
    terminal    1x  computations/deltalambda/mu3_abs_choice_robustness_probe.py
    terminal    1x  computations/deltalambda/mu3_anchor_consistency_probe.py
    terminal    1x  computations/deltalambda/mu3_door_budget_probe.py
    terminal    1x  computations/deltalambda/mu3_frechet_perblock_probe.py

**Only one of the two propagators is a clean target.** `fr_pullback_cosh_h_test`
is in the family the audit's own HALF-FIX WARNING names: `mass_at_3A_proper.dim_q`
and `qfac` return Python **floats** (`math.prod` over f64 `q_int`) and `dim_q`
multiplies into every weight, so swapping the Rust entry to MPFR alone leaves
the result f64-capped. 8 modules import them; the mpmath equivalent is
`delta_lambda_empirical_tabulation.dim_q_at_q0`. So that one is a two-part fix.
`all_nuclides_wedderburn_spectral_v2.py` is the single clean propagator.

### A site of this bean I hit from the other direction, and a claim I got wrong

`qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py` — **4 of the 16**,
terminal — is the probe PR #7271 fixes the *anchors* of (bean `qou-gqt5`). In
that PR I wrote that `chi_lambda_braid` "takes a float `q_value` by **engine
contract**, so every χ there is float64". **That is false and is corrected on
the PR.** Measured:

    hecke_characters.py:479  def chi_lambda_braid(shape, word, q_value=None,
                                                  precision=None, ...)
    hecke_characters.py:610  def chi_lambda_braid_mpf(... dps=None)
    dir(pyhecke_native) -> ['chi_lambda_braid', 'chi_lambda_braid_mpfr']

float64 **by default**, not by contract — exactly the wrapper hop this bean
counts. I reached the wrong claim by grepping `def chi_lambda_braid` and reading
**string literals inside `f64_into_mpmath_audit.py`'s own selftest fixtures**
(`"def chi_lambda_braid(a, b, c):\n    return 0\n"`), inferring a
three-positional-argument API from a test input without opening the real
definition.

**Routing that probe to MPFR is blocked, not declined:** it PANICS in the Rust
engine before completing (`invalid generator index 0 for n = 3`, bean
`qou-2t9y`), verified against pristine `origin/main`, so no MPFR route can be
verified there end-to-end today.

### 🛑 The "single clean propagator" is a FALSE POSITIVE — and the proxy's blind spot is new

I named `all_nuclides_wedderburn_spectral_v2.py` above as the one clean
propagator and the right first drain target. **Hand-checked, it should not be
drained at all.** Three for three now on this bean's own rule that a hand-check
of a flagged site finds it legitimate.

`all_nuclides_wedderburn_spectral_v2.py:370-392`, under a comment reading
`# 3. chi_std vs native Hoefsmit (f64)`:

```python
mine = float(m_tr(m))                                  # the module's OWN mpmath result, cast DOWN
ref  = float(nat.chi_lambda_braid([2, 1], word, qf))   # the native f64 entry
devs.append(abs(mine - ref))
native_dev = max(devs)
w.add_assertion(name="chi_std_vs_native_hoefsmit",
                computed=native_dev, expected=0.0, tolerance=1e-9, ...)
```

**It exists to test the f64 kernel.** Both arms are cast to `float` on purpose
so the comparison is like-for-like, and the tolerance is `1e-9` — about seven
orders above the f64 floor for an O(1) quantity, so the check is insensitive to
the f64 path by construction. Routing it to MPFR would not improve it; it would
**destroy** it, leaving MPFR compared against MPFR and nothing validating the
native kernel.

**And the `PROPAGATES` flag does not attach to this value.** The witness is read
by `delta_lambda_feed_analysis.py`, which is what earns the flag — but that
consumer **never reads `chi_std_vs_native_hoefsmit`**. It reads `data.rows`
(`A`, `T_crossings`, `B_AME_MeV`) and `markov_weights_y_lambda`. Its `_cell`
docstring settles the rest on its own:

> Kept as `float` deliberately, NOT promoted to mpf: everything downstream here
> is numpy (`np.polyfit`, `np.log10`) and is float64 by construction. …
> converting at the read would dress a float64 analysis in digits it does not
> have.

So the propagation target is deliberately float64 too.

**Why `native_entry_disposition` misses it — this is the reusable part.** The
`deliberate` bucket is defined as *"also calls an `_mpfr` entry"*. This site
cannot: its reference arm is **the module's own mpmath result cast down**, not a
second engine call. A deliberate f64 cross-check whose other arm is INTERNAL is
structurally invisible to that test, and lands in `actionable`.

Narrowing the proxy is a detector change, not a precision fix, so it is reported
rather than done. The shape to key on, if someone does: a site whose flagged
value is subtracted from a `float(...)` of a locally-computed quantity and
asserted against a tolerance orders above the f64 floor.

**Consequence for the drain: there is no clean propagator.** Both flagged
propagators are now accounted for — this one is deliberate, and
`fr_pullback_cosh_h_test` is in the HALF-FIX family (`dim_q`/`qfac` return
floats). The next agent should start from the **terminal** list, or narrow the
proxy first.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Not a convention question. f64 Rust engine entry points vs exact MPFR siblings
is the float64 axis (sibling of `qou-840k`, as the bean itself says). Keep
open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8381, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
