---
# qou-ewc4
title: 'GAP: LieValuedStokes + NonAbelianStokes are self-certifying carriers (Prop field + its own witness)'
status: in-progress
pr: 8218
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T17:00:30Z
updated_at: 2026-10-04T15:20:10Z
parent: qou-6qbv
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


---

## 2026-09-07 — the encoding landed (PR #7116); the bean stays open for ONE thing

**Done, and do not redo it.** Both `Prop`+witness pairs are gone. The fields
now state the identities:

- `NonAbelianStokes.stokes` — `MI₁(α; ∂σ) = MI₂(α, d_α β; σ)`, with
  `boundary`, `covariantD` and `slice` carried as fields (the class had
  integrals and no boundary, no covariant derivative and no slicing, which is
  why it could not state its own subject).
- `NonAbelianStokes.finite_slice` — the multiplicative integral IS
  `piecewiseAffineLineIntegral (slice γ)`, which this file already proves
  theorems about.
- `LieValuedStokes.stokes_identity` — `∫_{∂σ} α = ∫_σ d_α β`, with the three
  integrals carried.

The instances were re-derived as the bean asks. `punitInstance` survives and
is now honest: it *satisfies* `1 = 1` and `piecewiseAffineLineIntegral [] = 1`
by `rfl` rather than choosing them.

**Two things found while doing it that the bean did not name.**

1. `LieValuedStokes_canonical` was a global **`instance`**, so
   `[LieValuedStokes M 𝔤]` was discharged corpus-wide with `(0 : 𝔤) = 0` —
   the same defect `punitInstance` was demoted for on 2026-08-24, one class
   up in the same file, left live. Demoted to `def`.
2. `closedCellStokesIdentity` / `content_bearing_stokes` were a second model
   holding a differently-spelled tautology (`(1 : G) = 1`). With the field
   encoded there is no `Prop` field left for it to differ from
   `punitInstance` in, so it had become that model under another name.
   Deleted; nothing referenced either outside the file.

## 🛑 STILL OPEN — and this is now the whole bean

**The only model of `LieValuedStokes` is the zero one** (every integral
constantly `0`). By the `qou-z9ws` inhabitation discriminator that is
evidence the axioms are consistent and none that they constrain anything, so
`Nonempty (LieValuedStokes M 𝔤)` is still as empty as the `∃ _, True` that
`UpstreamSubstrateBridge.lean` deleted.

**So the bean's closing instruction is UNCHANGED: the Lie-valued Stokes
obligation is NOT discharged; do not write a theorem asserting that it is, and
do not restore `lie_valued_stokes_discharged`.** What changed is that the
carrier can now be *contradicted* by a non-zero model. What has not changed is
that no such model exists here.

What closing it needs: a `LieValuedStokes` model with a non-zero integral
satisfying the identity — i.e. the analytic theory this file abstracts away, or
a finite/combinatorial model on the braid surface where the integrals are
literal finite products. The same gap applies to `NonAbelianStokes`, whose
only model is likewise `punitInstance`. Related: `qou-ghc6` (build
Lie-algebra-valued 1-forms on a normed space).


## Progress (Round 52 — PR #8218)
- Resolved in PR `litlfred/qou#8218` (`claude/round52-devacuify-6qbv-uot9`, HEAD `31f749976663905d17c11fe898c73116da2e8d1b`) with 80-dps mpmath witness `computations/probes/round52-devacuify-6qbv-uot9.witness.json` (`scriptCommitSha = 5355a18ce7a60c5cabb79019663bff82e103d505`).
