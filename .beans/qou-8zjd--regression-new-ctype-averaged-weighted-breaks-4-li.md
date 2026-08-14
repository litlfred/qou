---
# qou-8zjd
title: 'REGRESSION: new ctype averaged_weighted breaks 4 live consumers; canonical_word_for fails for every Z>=1,N>=1'
status: in-progress
type: task
created_at: 2026-08-14T15:59:06Z
updated_at: 2026-08-14T15:59:06Z
---

## What happened

The `qou-gdtb` fix landed on `main` (PR #4924) by giving the canonical
classifier a **new label**: `classify_crossing` now returns
`averaged_weighted` for the colour-weighted p–n interface
`d = -h(1/2 - δ/4)`, distinct from the colour-blind `averaged` at `-h/2`.
That fix is correct and should stay.

What it did not do is check who **consumes** the label. Four live consumers
carry their own `{sigma, sigma_inv, averaged}` table and reject anything else:

| site | failure |
|---|---|
| `markov/markov_peel.crossing_element` | `ValueError: unknown cross_type: 'averaged_weighted'` |
| `markov/markov_trace_via_wenzl_lr.CTYPE_TO_SIGN` | `KeyError: 'averaged_weighted'` |
| `canonical_tr_m_via_rust.CTYPE_TO_SIGN` | `KeyError: 'averaged_weighted'` |
| `tau_M_proton_closed_form_phase5l1._cross_to_cd` | `ValueError: Unknown cross_type` |

Measured at an entry point, not just at the table:

    canonical_tr_m_via_rust.canonical_word_for(1,0)  [proton]   -> OK
    canonical_tr_m_via_rust.canonical_word_for(1,1)  [deuteron] -> KeyError: 'averaged_weighted'
    canonical_tr_m_via_rust.canonical_word_for(2,2)  [He-4]     -> KeyError: 'averaged_weighted'

## Scope: exactly the nuclides with a p–n interface

The new label is emitted only where a proton meets a neutron, so:

| word | ctypes emitted | status |
|---|---|---|
| proton `(1,0)` | `sigma, sigma_inv, averaged` | unaffected |
| neutron `(0,1)` | `sigma, sigma_inv, averaged` | unaffected |
| deuteron `(1,1)` | + `averaged_weighted` | **broken** |
| ⁴He `(2,2)` | + `averaged_weighted` | **broken** |

Every `Z ≥ 1, N ≥ 1` nuclide is affected. The single-species words are why
this was not caught: the proton path is the one most probes exercise.

## The second half of the same defect: the marshaller still collapses

`canonical_braid_marshalling.marshal_to_symbolic_braid` is a **private
re-implementation** of `classify_crossing` — it never learned the new label,
and maps both averaged interfaces onto `"averaged"`. Its consumer resolves
that label through `d_for_ctype`, which returns `-h/2`. So the colour
asymmetry is still silently discarded on that path:

    gen=2  true d           = -0.10445824776972628678
      canonical 'averaged_weighted' d = -0.10445824776972631454
      marshall  'averaged'          d = -0.10453014939781968273
      rel error introduced by marshaller = 6.8833e-04
    DISAGREEMENTS: 1 of 23

That is `qou-gdtb`'s 6.879e-4, alive in a different file from the one the
merged PR fixed.

`marshal_to_chi_lambda_braid` is a separate case: it emits **signs**, not
`d`, so both averaged variants legitimately land in the σ channel. Lossy,
but equally lossy for both, and documented. Leave the behaviour; route it
through the shared classifier so it cannot drift.

## The recurring pattern, instances five and six

The arc's standing lesson — *a private copy cannot learn what the canonical
one learns* — now has two more instances, and this time the copy did not
merely under-report, it **broke the build**:

5. `marshal_to_symbolic_braid` — private classifier, silent 6.88e-4.
6. `tau_M_proton_closed_form_phase5l1._cross_to_cd` — private ctype→(c,d)
   lookup, hard failure.

Plus `qou-mass/src/qou_mass/_internal/canonical_braid_crossings.py`, which is
the **pre-fix** file verbatim: narrow `{0, -h, -h/2}` vocabulary, no
`classify_crossing`, no `d_for_ctype`. It will raise on any deuteron word.

## To close

1. Give the canonical module the ctype→sign map alongside `d_for_ctype`, so
   there is one vocabulary with one place to extend.
2. Repoint the four broken consumers and the marshaller at it.
3. Sync or delete the `qou-mass` private copy.
4. **Add the test that would have caught this**: enumerate the ctypes the
   canonical classifier actually emits, and assert every live consumer
   handles all of them. A new label must then fail loudly in CI rather than
   at a nuclide nobody ran. Without this the seventh instance is only a
   matter of time — the previous six were each found by hand.
