---
# qou-qe81
title: phase3_triton producer wrote a GREEN witness with AssertionError strings for every row — broken since the E_0->Q_beta_n_mev rename missed a caller
status: todo
type: bug
created_at: 2026-09-02T22:01:09Z
updated_at: 2026-09-02T22:01:09Z
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

- [ ] A row carrying an `error` key should fail the witness, or at minimum
      set `allPassed: false`. Find where that is decided and make it so.
- [ ] `assertions: 0` + `allPassed: true` is indistinguishable from "ran
      correctly and had nothing to assert". Zero assertions on a producer
      that declares rows should not be green either.

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
