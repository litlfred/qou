---
# qou-4sqq
title: derived_chi_catalogue_build is not idempotent — re-running duplicates its own cells
status: todo
type: bug
created_at: 2026-09-06T10:15:38Z
updated_at: 2026-09-06T10:15:38Z
---

Surfaced by the qou-hu1f regeneration pass. Pre-existing since at least 2026-06-07.

## Measured

    ValueError: duplicate catalogue cell ('borromean', (3,), 'borromean-baryon');
    re-derive or update the existing record explicitly.

`derived_chi_catalogue_build.py` calls `load_catalogue()` and then `cat.add(c)`
for cells it re-derives. `DerivedChiCatalogue.add` refuses a repeated
`(knot, partition, atom)` key by design. The committed
`derived-chi-catalogue.witness.json` is dated **2026-06-07**, holds **342
cells**, and already contains the key — so the builder has been unable to run
against its own output for three months.

## NOT the intra-ordering ruling, despite appearances

The duplicate key contains the string `borromean`, and I initially misread that
as the `intra_order="borromean"` default. It is not: `'borromean'` here is a
**knot** name, built from the hardcoded braid word `[-1, +2, -1, +2, -1, +2]`
= `(σ₁⁻¹σ₂)³`. The collision with the ordering's name is coincidental.
Confirmed by running under both orderings — fails identically.

## The decision this needs

The guard is deliberate and its message says so: *"re-derive or update the
existing record explicitly."* So the fix is not to relax it. Either the builder
should be re-runnable (skip or replace existing cells, explicitly), or it is a
one-shot generator and should say so and refuse to run against a populated
catalogue with a clearer message than a duplicate-key error.

- [ ] Decide: re-runnable builder, or one-shot generator with an explicit guard?
- [ ] Whichever, the current failure mode — a raw `ValueError` on a key that
      looks ordering-related — is the worst of both.