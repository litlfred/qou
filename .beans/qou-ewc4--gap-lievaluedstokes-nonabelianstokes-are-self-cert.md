---
# qou-ewc4
title: 'GAP: LieValuedStokes + NonAbelianStokes are self-certifying carriers (Prop field + its own witness)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T17:00:30Z
updated_at: 2026-08-21T17:00:58Z
---

Found while draining the 22 small-category vacuity defects (qou-h3ly).

**The defect class.** A carrier declared as

    class C ... where
      p : Prop            -- the claim, as a FIELD
      p_witness : p       -- and its proof, as a FIELD

is inhabited by choosing `p := True`. So **no** existence / `Nonempty`
statement about such a class is falsifiable, and any theorem of the form
`∃ _ : C, True` or `Nonempty C` is vacuous no matter how it is spelled.
This is why such defects cannot be fixed by de-`True`-ing them — swapping
`∃ _, True` for `Nonempty` only silences the detector (AGENTS §1a
audit-dodging).

**Two live instances** (QOU/Mathlib/NonAbelianStokes.lean):
- `NonAbelianStokes`: `stokes_holds : Prop` + `stokes_holds_witness`;
  `punitInstance` sets both `stokes_holds` and `finite_slice` to `True`.
- `LieValuedStokes`: `stokes_identity : Prop` + `stokes_identity_witness`;
  `LieValuedStokes_canonical` sets `stokes_identity := (0 : 𝔤) = 0` with
  `rfl`, its own comment conceding 'Holds tautologically'.

**Consequence already actioned in qou-h3ly:** `lie_valued_stokes_discharged`
was DROPPED (not restated) and its conjunct removed from
`extended_upstream_discharge`; `yekutieli_finite_slice_substrate` was
restated against the *content-bearing* `YekutieliFiniteSliceMultTrace`
class instead (`trace n = z ^ n` for an arbitrary instance).

**The fix here:** replace the `Prop`+witness pairs with genuine Prop
fields stating the actual Stokes identity, then re-derive the instances.
Until then the Lie-valued Stokes obligation is NOT discharged; do not
write a theorem asserting that it is.
