---
# qou-qe81
title: phase3_triton producer wrote a GREEN witness with AssertionError strings for every row — broken since the E_0->Q_beta_n_mev rename missed a caller
status: in-progress
type: bug
created_at: 2026-09-02T22:01:09Z
updated_at: 2026-09-03T00:00:00Z
---

Found while enumerating the witness blast radius of `qou-uiut`.

## What happened

`e5dcd8f54` (2026-08-01) renamed `binding_canonical`'s `E_0=` keyword to
`Q_beta_n_mev=` because it was misnamed — the value is the free-neutron
β-decay Q-value, not the canonical energy scale E_0 ≈ 4.186 MeV. It added an
`assert "E_0" not in kwargs` to catch stragglers, and its docstring says it
updated "the single internal caller `kahler_lift.py:343`".

It missed one: `hecke_core_legacy.py:2521`, `_canon(Z, N, E_0=...)`.

So every call through `binding_energy(..., canonical=True)` raised
AssertionError from 2026-08-01 on. Fixed in `qou-uiut`'s follow-up commit —
a pure rename, `E_0_CALIBRATION_MEV` and `binding_canonical._Q_BETA_N` are
bit-identical (`mpf('0.78233340930999995')`), so no number moved.

## The part that needs a gate, not a fix

`phase3_triton_binding_convention_b.py` caught the exception per atom, wrote
the exception TEXT into each row, and then emitted a witness that declares
itself green:

    "atom": "T", "Z": 1, "N": 2, "A": 3, "hecke_level": "H_9",
    "error": "AssertionError: binding_canonical: the `E_0` keyword is
              deprecated; ..."

    allPassed: true      assertions: 0

Four rows, every one an error string, and the witness passed. It sat in the
corpus in that state until 2026-09-02. Post-fix the same producer emits real
values (D +0.435403, T +0.695131, 3He +0.698552, 4He +0.876064 MeV).

A witness whose rows are error strings must not serialise as passing. Two
things are wrong and both are general, not specific to this producer:

- [x] A row carrying an `error` key should fail the witness, or at minimum
      set `allPassed: false`. DONE — `_check_error_rows` / `_apply_error_row_gate`
      in `qou_substrate/witness.py`, keyed on the VALUE shape
      (`"<SomeError>: <message>"`) rather than the key's presence, because
      `error` is overloaded: five witnesses use it for a numeric error
      (`mass-from-q-symbolic` has `error = 9.98e-13`). Verified live:
      a clean payload builds `allPassed: True basis: assertions`, an
      error-row payload `allPassed: False basis: error-rows`.
- [x] `assertions: 0` + `allPassed: true` — DECIDED, deliberately not flipped.
      359 of 2522 witnesses (14%) have this shape, and flipping it was already
      tried and withdrawn under bean `qou-vfy1`: ~a dozen producers do
      `return 0 if wit["allPassed"] else 1`, so `None`/false trades a silent
      false positive for a loud false negative. Resolved with a discriminator
      instead — `allPassedBasis` ∈ {assertions, vacuous, failed-assertions,
      error-rows} — so earned green and vacuous green are now tellable apart
      while the boolean stays usable as an exit code.

## Also observed, separate

Post-fix the producer trips the corpus's own NO-FLOAT64 witness warning with
**25 raw float64 fields** (it was 1 while the run was erroring, because there
was nothing to serialise):

    ⚠ raw-float64: 25 raw float64 field(s) would enter the witness —
      .data.E_0_MeV, .data.rows[0].B_pred_MeV, ...
      Carry mpmath.mpf from the source and serialize with _precision.fmt

That is the producer serialising `float(...)` rather than carrying mpf out of
`binding_canonical`. Pre-existing pattern, unblocked rather than caused by the
fix. Worth its own pass under the NO-FLOAT64 directive.

## 2026-09-03 — the gate landed; the blast radius was measured first

Branch `claude/qou-qe81-witness-gate`. The producer fix is `372872149` and was
not touched.

### Blast radius, measured before landing anything

3175 `*.witness.json` scanned, `qou-mass/` and `/_deprecated/` excluded; 2522 of
them carry an `allPassed` field.

| shape | count | of which GREEN |
|---|---|---|
| (a) any nested dict with a truthy `error` key | 14 | 12 |
| (a′) …restricted to **exception-shaped** values | **4** | **4** |
| (b) `assertions: []` **and** `allPassed: true` | 359 | — |
| (b′) …of those, also declaring rows | 192 | — |

**`error` is overloaded, and that is the finding under (a).** Keying a gate on
the presence of the key would be wrong about half the time: 5 of the 14 mean a
NUMERICAL error — `mass-from-q-symbolic` has
`.data.proton.volumes[0].error = 9.98e-13`, `m-p-spectral-corrected-50dps` has
`.data.error = {leading_pct, full_ppm}`, `laplace-sum-theta-exactness` has
`error: "e^{-pi^2/a} = …"`, `qbeta-ck-local-taylor-around-u0-probe` a 50-digit
decimal string. The sibling key `err` is numeric in **all 34** of its
occurrences. So the discriminator is the SHAPE OF THE VALUE —
`"<SomeError>: <message>"`, what `f"{type(e).__name__}: {e}"` emits and what
every real offender is written as. On that signal: 4 witnesses, 0 of the
numeric-`error` ones touched.

The four that go red on their next producer run:

| witness | hits | assertions |
|---|---|---|
| `computations/sweeps/paper-six-term-isotope-sweep` | 30 `FileNotFoundError` | 2, both passing |
| `computations/audits/producer-importability-audit` | 13 `ModuleNotFoundError` | 2, both passing |
| `computations/term6-residues-at-roots` | 4 `ValueError` | 0 |
| `computations/probes/delta-coupling-closed-form-probe` | 3 `ValueError` | 0 |

Three of the four are the phase3_triton failure verbatim. The fourth
(`producer-importability-audit`) is a legitimate error COLLECTOR — the import
failures are its result — which is why the gate needed an opt-out at all.

Note the top two carry **passing assertions** alongside their error rows, so a
gate keyed on `assertions == []` would have missed the largest offender.

### What landed

`tools/qou-substrate/python/qou_substrate/witness.py`

* `_exception_text_paths` / `_apply_error_row_gate` / `_check_error_rows`, in
  the idiom of the existing `_check_raw_float64` / `_check_nonfinite` guards.
  Called at the end of `build()` (on the assembled dict, because
  `paper-six-term-isotope-sweep` carries its rows at TOP level, not under
  `data`) and again in `save()` after the `extra` merge; idempotent.
* **The demotion is unconditional.** `QOU_WITNESS_STRICT_ERROR_ROWS`
  (`warn` default / `1` raises / `0` silences) controls only how loudly the
  paths are REPORTED. An env var that could restore the green verdict would
  recreate the exact lie.
* The one opt-out is visible **in the witness**: top-level `expectErrors`, via
  `WitnessBuilder.expect_errors(reason)`. Same argument as the `preserved: true`
  freeze in `save()` — the escape hatch is a declaration in the file, not a
  docstring and not an environment variable.

Proved by construction: the same payload builds `allPassed: true` under the
pre-change module (extracted from `HEAD`) and `allPassed: false,
allPassedBasis: "error-rows"` under the new one.

### The second checkbox: zero assertions — LABELLED, deliberately NOT flipped

359 of 2522 (14 %) are green over an empty assertion array; 192 declare rows.
Flipping that is a corpus-wide red wall, and **it was already tried**: bean
`qou-vfy1` investigated emitting `allPassed: null` for an empty assertion list
and WITHDREW it, because about a dozen producers write
`return 0 if wit["allPassed"] else 1` and `None` is falsy — turning a silent
false positive into a loud false negative.

So the fix is a DISCRIMINATOR, not a flip: new top-level **`allPassedBasis`** ∈
`{assertions, vacuous, failed-assertions, error-rows}`. This is exactly what
`durationMsBaseline` (already in `build()`) does for the same class of problem —
904 ambiguous callers, fixed at the one place they pass through rather than in
the callers, because nothing at the call site distinguishes a right one from a
wrong one. `allPassed` is unchanged for all 359, so nothing goes red; what
changes is that a consumer can now tell earned green from vacuous green without
re-deriving it. Declared in `schemas/witness-schema/schema/witness.schema.json`
(`additionalProperties: true`; the JS/Python bindings already omit
`durationMsBaseline`, so they were left alone).

**Answer to "should zero-assertion green be green?"** — No, it should not be
*read* as green, and it no longer has to be: the witness now says which it is.
The verdict itself stays true because ~a dozen producers use it as an exit code
and 14 % of the corpus would flip at once, which is how a checker gets switched
off rather than fixed.

### Related gates, for whoever picks up the drain

This is the third sibling of a family the repo already runs two of:

* `computations/witness_hollowness_audit.py` — green with `assertions: []` (H1)
* `computations/witness_failed_assertion_audit.py` — a FAILED assertion,
  committed green (wired into `scripts/precision-gates.sh`, advisory, baselined
  at 111)
* this one — a failure recorded in the **data**, where neither of the other two
  looks

`witness_hollowness_audit.py` is **wired into no gate array** —
`precision-gates.sh` mentions it only in a comment, which is that file's own
"a gate wired nowhere is a gate nobody runs". Wiring it has a 359-witness
backlog in front of it.

### Tests

`tests/test_witness_error_row_gate.py`, 13 cases. The two load-bearing ones are
`test_numeric_error_field_stays_green` (holds the value-shape line, without
which the gate is a corpus-wide false alarm) and
`test_vacuous_green_is_labelled_not_flipped` (pins the decision above so a later
pass does not quietly re-litigate it).

`python3 -m pytest tools/qou-substrate/tests/ tests/ -q` → **191 passed**
(baseline 178 + 13). No module-scope `mp.dps`; the module needs no precision and
says so.

### Still open on this bean

- [x] The **NO-FLOAT64** item above — DONE in code (the witness artifact is
      tracked separately below). `b_pred` stays mpf; `AME_2020_BINDING_MEV`
      holds `mp.mpf` of exact decimals rather than float literals (those are
      the DENOMINATOR of the residual, so their f64 quantisation was
      propagating into every residual recorded); `E_0_MeV` at both sites and
      `compute_time_s` as a string. The only `float()` left is inside
      `print()` — a format width is presentation, not a value. Originally:
      `phase3_triton_binding_convention_b.py`
      serialises `float(...)` instead of carrying `mpf` out of
      `binding_canonical`; 25 raw float64 fields. Untouched here, genuinely
      separate.
- [ ] Drain the 4 witnesses above. Three are real defects whose producers need
      fixing; `producer_importability_audit.py` should declare
      `expect_errors(...)`. Each needs a producer re-run, so none was done here.
- [ ] The gate is not mirrored into the vendored
      `qou-mass/src/qou_mass/_internal/witness_base.py`.
      **Recommendation: do NOT hand-patch it.** `qou-mass/` is a vendored copy
      and is excluded from every audit in this corpus by standing convention;
      hand-editing it makes the vendored tree diverge from what it vendors,
      which is the same divergence-between-copies failure that produced the
      `.dot` and `a_rho` defects. It should pick the gate up by re-vendoring.
      Left open so the decision is someone's to confirm, not silently closed.


## 2026-09-03 — the NO-FLOAT64 item is now done in CODE; regeneration owed

Owner restated NO FLOAT64 EVER, which promoted this from "second item, not
taken" to something to land.

`b_pred` comes out of `binding_from_frobenius_pairing` as mpf and was
immediately downcast — `b_pred_f = float(b_pred)` — with everything downstream
computed from the float. So `B_pred_MeV`, `residual_pct` and `residual_keV`
all reached the witness at ~17 digits out of a 50-dps pipeline.

Worse, `AME_2020_BINDING_MEV` held Python float literals, and those values are
the DENOMINATOR of the residual: the f64 quantisation of `2.22456612` was
propagating into every residual the witness records. Now `mp.mpf("...")` of
the exact decimal.

Also `E_0_MeV` (both sites) and `compute_time_s`, the latter as a string,
matching `hadron_knot_table`'s `per_atom_wall_seconds` (bean `qou-c7g8`) — a
diagnostic must not add raw float64 to a witness either.

The only `float()` left in the file is in `print()` calls: a format width is
presentation, not a value.

- [ ] **Regenerate `phase3-triton-binding-convention-b.witness.json`.** NOT
      done here: the nuclide-table regeneration (bean `qou-uiut`) is running
      in this checkout and two producers must not run at once. Until it is
      regenerated the committed witness still carries the 25 raw-float64
      fields the corpus's own gate warns about — the code is fixed, the
      artifact is not.

## 2026-09-04 — measured the vendored qou-mass mirror's drift

Ran the mirror's own suite after merging origin/main (290 commits):

    PYTHONPATH=qou-mass/src python3 -m pytest qou-mass/tests -q
    7 failed, 13 passed

Not caused by anything on this branch. `qou-mass/src/qou_mass/_internal/
hecke_core.py` states outright that it imports nothing from
`hecke_core_legacy`, and the failing values come from the mirror's own
Decimal tables, so the braid fix, the Rust routing and the NO-FLOAT64 work
cannot reach them. Pre-existing drift between the mirror and the values the
computations layer now produces.

The seven, with the actual deltas — the spread is the useful part:

    test_proton_mass       938.7830883780143   vs 938.27185264      Δ 5.1e-01
    test_neutron_mass      939.5658930679812   vs 939.56518467      Δ 7.1e-04
    test_muon_mass         105.65839781134181  vs 105.65837565      Δ 2.2e-05
    test_deuteron_binding  2.248820797901309   vs 2.2488207948647   Δ 3.0e-09
    test_compute_tr_M_4he  0.16097414544240737 vs 0.16097419322912  Δ 4.8e-08
    test_compute_tr_M_prot 1.1457596924573008  vs 1.1457597822878   Δ 9.0e-08
    test_4he_binding       method is 'L3-α-cluster:n_α=1,pairs=0(magic-A-derived)',
                           test asserts 'L1' in method

Six are numeric-tolerance failures, one is a METHOD-STRING failure and that
last one is the informative one: 4He is now answered by an L3 α-cluster route
where the test still expects an L1 route. That is a change of derivation, not
a change of digits, so it will not be fixed by loosening a tolerance.

The numeric six do not share a scale — 5e-01 down to 3e-09, seven orders of
magnitude. A single upstream precision change would not produce that spread;
these look like several independent drifts (the proton at 5e-01 is a
different-quantity-sized gap, not a rounding one).

Disposition unchanged and now measured rather than assumed: do NOT hand-patch
the mirror's expected values. Hand-editing seven constants to match today's
output would convert a real signal — six drifts and one changed derivation —
into a green suite that asserts nothing. The mirror should be regenerated from
its source, or the tests should be pointed at the computations layer.


## 2026-09-05 — the mirror item resolves better than "do not hand-patch"

The open item read: "The gate is not mirrored into the vendored
`qou-mass/src/qou_mass/_internal/witness_base.py`. **Recommendation: do NOT
hand-patch it** ... It should pick the gate up by re-vendoring."

Both halves are now settled, and the first one dissolves.

### The gate needs no mirroring at all

`qou-mass/src/qou_mass/_internal/witness_base.py` is **82 lines** and is a
SHIM, not a copy — it bootstraps `tools/qou-substrate/python/` onto `sys.path`
and re-exports `qou_substrate.witness`, the real 3114-line module. So it
already carries the error-row gate, the atomic write (`qou-sidu`) and every
other guard, by delegation rather than duplication. `grep` for
`_check_error_rows` in the vendored file returns 0 not because the gate is
missing but because there is no implementation there to find.

My "not mirrored" framing assumed a full copy. It is the one file in that tree
that cannot drift on this axis.

(The standalone-shipping question is separate and untouched: outside the repo
the shim needs `qou_substrate` installed. That is packaging, not gating.)

### Re-vendoring is a supported operation, and I ran it

`scripts/sync-qou-mass-vendor.py` exists precisely for this, with
`--check` / `--apply` / `--list`, and its docstring records that on 2026-08-15
all 14 vendored modules had drifted ("the copies are simply behind", one by a
whole generation).

    --check  ->  DRIFTED from source (7): 3 modules + 4 witness JSON
                 markov_trace_recursive, q_parameter, tr_m_wenzl_bridge_mpfr
    --apply  ->  regenerated 49 modules
    --check  ->  in sync (49 modules, 25 witness JSON, 122 package-data)

Repo suites unaffected: 64 + 145 pass.

### The 7 mirror test failures are NOT drift

Measured before and after the re-vendor: **7 failed, 13 passed, unchanged**.
So the earlier disposition holds and is now evidence-backed rather than
inferred — those failures live in `qou-mass/tests/`'s own hardcoded expected
values (proton 938.783 vs 938.272, and the 4He method string moving from L1 to
`L3-α-cluster`), not in the vendored copies. Re-vendoring was the right thing
to do and does not touch them.

- [x] Mirror the gate — VOID. The vendored file is a shim; it delegates.
- [x] Re-vendor rather than hand-patch — done, 7 drifted items resynced.
- [ ] The 7 mirror test failures still want an owner decision: point the tests
      at the computations layer, or regenerate their expectations from it.
      Still do NOT hand-patch the constants.

---

## 2026-09-13 — the four error-row witnesses: NONE now needs a producer fix

Re-measured after the 702-commit merge. The bean's open item said "Three of
the four are real defects whose producers need fixing". **That is no longer
true of any of them** — all four are resolved or need only a re-run.

| witness | exception rows | state |
|---|---|---|
| `producer-importability-audit` | 163 | **drained** — declares `expectErrors`, `basis: assertions` |
| `delta-coupling-closed-form-probe` | **0** | **drained** — regenerated, `basis: vacuous` |
| `paper-six-term-isotope-sweep` | 8 | producer FIXED (returns EMPTY rather than raising); witness stale |
| `term6-residues-at-roots` | 4 | producer FIXED **by main**; witness stale |

### `term6` — diagnosed, and the fix was already upstream

Its four rows are the A≥2 atoms (A=1 proton and neutron succeed), all carrying
the same

    ValueError: LaurentQ.from_sympy: non-Laurent factor
        -(1 - 1/q**4)*(q - 1)**2/12 + 1/2

That factor **is** Laurent. Expanded it is

    -q²/12 + q/6 + 5/12 + q⁻²/12 − q⁻³/6 + q⁻⁴/12

— every exponent an integer. So the parser was rejecting an expression its own
docstring promised to accept ("sums and products of the above"): its `is_Mul`
branch takes only Numbers and powers of `q` as factors, so a PRODUCT OF SUMS
failed even though both factors, and the product, are Laurent.

**Main had already found it, from the identical expression, under bean
`qou-ls7l`**, and added an expand-and-retry to `pyhecke/laurent_q.py` —
expanding on RETRY rather than up front, so existing callers pay nothing.
Verified here against the exact failing input: it now parses to
`1/12 q³ − 1/6 q² − 1/2 q + 1/6 + 1/3 q⁻¹ + 1/6 q⁻² − 1/6 q⁻⁴ + 1/12 q⁻⁵`.

So the remaining work on this item is **two re-runs, no code**. Both are in
`.work/regen-queue.md`; both wait on the nuclide table, which holds the
checkout.

Worth noting for the gate's sake: both stale witnesses still serialise
`allPassed: true` over rows that are exception text, which is exactly what the
error-row gate demotes — they predate it. Re-running them is what makes the
gate's verdict visible on them.
