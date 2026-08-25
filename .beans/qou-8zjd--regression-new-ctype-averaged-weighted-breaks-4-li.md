---
# qou-8zjd
title: 'REGRESSION: new ctype averaged_weighted breaks 4 live consumers; canonical_word_for fails for every Z>=1,N>=1'
status: completed
type: task
priority: normal
created_at: 2026-08-14T15:59:06Z
updated_at: 2026-08-19T21:05:18Z
---

## What happened

The `qou-gdtb` fix landed on `main` (PR #4924) by giving the canonical
classifier a **new label**: `classify_crossing` now returns
`averaged_weighted` for the colour-weighted p–n interface
`d = -h(1/2 - δ/4)`, distinct from the colour-blind `averaged` at `-h/2`.
That fix is correct and should stay.

What it did not do is check who **consumes** the label. Four live consumers
carry their own `{sigma, sigma_inv, averaged}` table and reject anything else:

| site | failure | reached today? |
|---|---|---|
| `canonical_tr_m_via_rust.CTYPE_TO_SIGN` | `KeyError` | **live** — fed by `atom_canonical_crossings` |
| `markov/markov_trace_via_wenzl_lr.CTYPE_TO_SIGN` | `KeyError` | **live** — same feed |
| `chi_sym_alt_closed_form.count_factor_types_from_crossings` | `ValueError` | **live** — `light_isotope_sweep` feeds it canonical crossings |
| `atom_level_wedderburn_tower` (private `d_for` dict) | `KeyError` | **live** |
| `markov/markov_peel.crossing_element` | `ValueError` | latent — legacy test wrapper; `word_to_element`, the production path, always carried the weighted form |
| `tau_M_proton_closed_form_phase5l1._cross_to_cd` | `ValueError` | latent — its word is the proton `(1,0,include_inter=False)`, which has no p-n interface |

**Latent ≠ harmless, but it is not the same claim.** An earlier draft of this
table listed all sites as current failures; Copilot's review on PR #5018
correctly pushed back that a site downstream of the still-collapsing
marshaller could not yet see the new label. Two of the six are latent, for
two different reasons, and both are recorded above rather than flattened.
They are fixed anyway: a private copy that happens not to be reached today
is the same defect one caller away.

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

## What the mechanical scan found that reading did not

Reading the tree by hand found four consumers. A scan — *does this file name
the vocabulary without importing it?* — found **eleven more**, of which four
were real value-mapping defects and seven are prose or counting:

| site | defect |
|---|---|
| `atom_level_wedderburn_tower.py` | private `d_for` dict → `KeyError` on the trace |
| `chi_sym_alt_closed_form.py` | private bucket set → `ValueError`; and bucketing the weighted crossing as `averaged` would silently break an *exact* closed form |
| `audits/term5_aK_audit.py` | private classifier returned `"unknown"`, which `mirror_word`'s `else` branch then treated as `averaged` — **silent** |
| `theta_mn_linearchain_vs_allpairs.py` | regex `(?:sigma\|averaged\|sigma_inv)['"]` — the closing quote makes `averaged` fail to match `averaged_weighted` |

The regex one is the sharpest. It dropped gen 2 on the deuteron and gen 5 on
⁴He — both **interface** generators `3k−1`, which is exactly what that
function exists to count. It was silently missing precisely what it looks
for, and it is the same shape as the two drifted `WITNESS_REF` regexes
earlier in this arc.

`chi_sym_alt_closed_form` needed a derivation, not a bucket. On a 1-dim
irrep a crossing `c·σ + d·1` contributes `(image of σ) + d`, so with
`d = -h(1/2 - δ/4)`:

    sym:   q   - h(1/2 - δ/4) = [2]_q/2 + hδ/4
    alt:  -q⁻¹ - h(1/2 - δ/4) = -([2]_q/2 - hδ/4)

i.e. the colour-blind `[2]_q/2` shifted by `±hδ/4` — the colour asymmetry
carried exactly. Verified against the direct product at ≤ 4.9e-16 (f64 eps)
on p, n, D, T, ³He, ⁴He.

## The recurring pattern, instances five through nine

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
