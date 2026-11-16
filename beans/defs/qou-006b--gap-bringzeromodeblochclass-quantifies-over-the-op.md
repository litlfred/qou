---
# qou-006b
title: 'GAP: BringZeroModeBlochClass quantifies over the opaque BlochWigner_unit_circle; the Bloch class [Z] on Bring''s surface is not identified'
status: in-progress
type: task
priority: normal
tags:
    - gap
    - reorg-2026-10-04
    - 8f-lean
    - 8f-open
    - lean
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-11-15T18:52:39Z
parent: qou-8lxd
pr: 8221
---

Advisory from the SM-surface Lean sweep (bean qou-08zf, 2026-09-03); not changed. lean/QOU/Archimedean/EmCouplingBringZeroMode.lean imports QOU.Archimedean.BlochWignerUnitCircle, where BlochWigner_unit_circle is declared "noncomputable opaque (_θ : ℝ) : ℝ" — an unconstrained function. The conjecture class BringZeroModeBlochClass has a single field, ∃ θ, BlochWigner_unit_circle θ = 2/(3π), which is therefore unfalsifiable as stated; against the Clausen definition in BlochWignerMathlibFiller it would be true by the intermediate value theorem (2/(3π) ≈ 0.212 lies in the range of Cl₂), which is not the open claim either. The open claim is the identification of the specific Bloch-group class [Z] from the Yekutieli triple on {T(2,9), T(3,5)} whose τ_arch-image is 2/(3π).

NEXT HONEST STEP: pin the field to the group-homology pairing the file's own docstring describes (pairing the Euler/volume class with the fundamental 2-cycle of Bring's surface), or carry the angle θ as an explicit parameter of the class with the identification as the field. No instance exists; none should be added. Recorded as an advisory entry in docs/audits/lean-vacuity-review-ledger.json.


## Triaged 2026-10-10 — OPEN Lean work, not mechanical; tagged `8f-open`

Read as part of working the `8f-lean` front. The bean's "NEXT HONEST STEP" is to
restructure a conjecture class — pin the field to the group-homology pairing its
own docstring describes, or carry the angle as an explicit class parameter. That
is formalisation, not a repair, and it needs a judgement about what the claim
asserts.

**The trap it documents is worth restating**, because it is the reason this
cannot be closed by making the Lean compile: the single field
`exists θ, BlochWigner_unit_circle θ = 2/(3π)` is **unfalsifiable as stated**,
since `BlochWigner_unit_circle` is `noncomputable opaque (_θ : ℝ) : ℝ` — an
unconstrained function. Against the real Clausen definition it would instead be
**true by the intermediate value theorem** (`2/(3π) ≈ 0.212` lies in the range of
`Cl₂`). Neither reading is the open claim, which is the identification of the
specific Bloch-group class from the Yekutieli triple on `{T(2,9), T(3,5)}`.

So a green Lean file here would mean nothing either way. The bean's instruction
stands: **no instance exists; none should be added.**



## 2026-11-15, PR #7946 (issue #7942)

The owner chose to give `BlochWigner_unit_circle` its documented body `Cl_2`, so the field is now **true by IVT** (`bringZeroModeBlochClass_holds`, sorry-free, standard axioms), exactly as this bean predicted. Per this bean's triage it is a **named theorem, not a global instance** (commit 6ff8649b54), so `[BringZeroModeBlochClass]` on `bring_zero_mode_additive_form` is not discharged silently. The angle-rationality sharpening is `BringZeroModeRootOfUnityClass` (no instance). **The open claim, the Bloch-class identification on {T(2,9), T(3,5)}, is untouched; this bean stays open.** The class should eventually be restated to carry that identification.



## 2026-11-15 analysis (thread on #7942; not yet acted on, owner card pending)
(1) Restate: the real claim is a Bloch-group element xi = sum n_i [z_i], z_i algebraic (Q(zeta_15)), with sum n_i D(z_i) = 2/(3pi); falsifiable and stateable in Lean now. (2) T(2,9), T(3,5) are torus knots: Seifert fibred, simplicial volume 0, so by |vol rho| <= v3 ||M|| every Bloch class from them has D = 0 (scope (b), cited invariant). (3) For algebraic z_i, D(z_i) is a period, so the identity would make 1/pi a rational multiple of a period; Kontsevich-Zagier predicts not. Expected outcome: false; unconditional proof is a transcendence problem, out of reach. Keep open.



## 2026-11-15, owner chose 'restate + record negative' (PR #7946, commit dc49a51dd9)
Field is now: exists finite s in C, n : C -> Z, all z algebraic with Im z > 0, sum n z * BlochWigner_lob z = 2/(3pi). Cocycle condition not imposed. No instance. Negative recorded in the docstring (period conjecture; torus knots give D = 0). Stays OPEN: the claim is now falsifiable but neither proved nor refuted.

## Implementation Note (PR #8221)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/TorusZeroVolumeConnectedRankOneBringChiralityMassClosureAndJordanTwentySix.lean` and `computations/probes/torus_zero_volume_connected_rank_one_bring_chirality_mass_closure_and_jordan_twenty_six_probe.py` (witness `computations/probes/torus-zero-volume-connected-rank-one-bring-chirality-mass-closure-and-jordan-twenty-six.witness.json`, `3849d3633186444056f013bfbcda743be84b0a9c`).
