---
# qou-c8p8
title: 'Mathlib infra: close class field debt'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-24T06:35:32Z
updated_at: 2026-11-17T10:22:29Z
parent: qou-rtxm
---

Epic to close conjectural class fields that are standard math (not manuscript claims). Three axes: LP/SDP duality, parallelogram contour, RSK combinatorics.

This is the same triage first filed as `qou-bi00`, which I created without running the exact-title existence check `AGENTS.md` requires. `qou-bi00` is scrapped in favour of this entry; the check would have found this bean, whose three named axes already include "parallelogram contour".

The `#6491` audit found 491 uninhabited classes, 38 of them in the Mathlib-shaped directories (`Mathlib`, `MathlibExt`, `Machinery`) — the subset where "build the Mathlib infra" is the right response rather than "do the physics". This triages that subset by the only question that decides it: **does the pinned Mathlib v4.24.0 actually carry the thing the carrier needs?**

## Measured, against `.lake/packages/mathlib/Mathlib`

| carrier | Mathlib support | verdict |
|---|---|---|
| `Mathlib/EllipticDivisorDegree.lean:212 HasArgumentPrinciple` | **nothing** (`argumentPrinciple`, `argument_principle` occur nowhere) | genuine gap |
| `MathlibExt/SphericalCategory.lean:79 SphericalCategory` | **nothing** — no `PivotalCategory` either | genuine gap |
| `MathlibExt/FrechetShohat.lean:210,235 CarlemanDeterminacyStieltjes / FrechetShohatStieltjes` | **nothing** (`Carleman`, `moment_problem` occur nowhere) | genuine gap |
| `Mathlib/HadamardFactorization.lean:300 HasHadamardFactorization` | a **DIFFERENT** Hadamard theorem | see below |
| `Mathlib/PermutationEnumeration.lean:353 CoxeterSwapFormulaHolds` | real API (`GroupTheory/Coxeter/{Basic,Length}.lean`) | **the one wiring candidate** — but see the overlap note |

## The Hadamard hit is a name collision, and it is Mathlib's

`Analysis/Complex/Hadamard.lean` exists and is the **three-lines theorem** — a bound on `‖f‖` across a vertical strip. `HasHadamardFactorization` needs the **factorization theorem**, `f(z) = exp(g(z))·∏ₙ Eₚ(z/aₙ)`. Different statements, different proofs, sharing only a surname. A keyword probe scores it as supported; it is not.

Worth noting the corpus file here is exemplary and should not be "fixed": the carrier is stated in full strength, its docstring explains why the product equation already forces the zero enumeration to be complete, and `hadamard_factorization_needs_nonneg_order` **proves** that dropping `0 ≤ ρ` makes the statement false. It names its own requirements — Jensen's formula, zero-counting, Weierstrass/Borel–Carathéodory growth. That is a genuine multi-session build, honestly labelled.

## Coxeter: do not take it without coordinating

`GroupTheory/Coxeter/Length.lean` is real and `CoxeterSwapFormulaHolds` is plausibly a wiring job against it. But `main` landed `fec0f466dd lean(qou-phir): length additivity iff no inversion is undone` on 2026-09-03 — active sibling work in exactly this API. Per `AGENTS.md`, measured research-overlap is permitted for **open-outcome** questions; wiring an existing Mathlib API is **mechanical** and has one owner. Coordinate on `qou-phir` before touching it.

## Consequence for `ParallelogramContour.lean`, landed alongside

`windingNumber` occurs **nowhere** in Mathlib, and there is no residue theorem (the only `residue` hits are p-adic and local-field ring homs — an unrelated sense). So both classical routes to `parallelogramIntegral_inv_sub_eq_two_pi_i` are absent upstream.

**That axiom is genuinely blocked; the Cauchy one next to it never was.** The file carried one shared "Goursat is infeasible" argument for both, and it was right about the pole integral and wrong about Cauchy — Cauchy for an *entire* function needs only a primitive, which is why `#6491` proved it in one pass. The discriminator is the pole, not the parallelogram. The stale clause "requires the Cauchy-Goursat theorem for parallelograms (which is blocked above)" is corrected in the same commit: that theorem is proved and is above.

## The honest bottom line

**The tractable Mathlib-infra tier is exhausted.** Of 38 Mathlib-shaped carriers, one (`StandardYoungCount`, `#6491`) was a leaf and is closed; one axiom (Cauchy, `#6491`) was a mis-diagnosis and is proved; one candidate (Coxeter) is a real wiring job owned by a sibling; the rest need mathematics Mathlib does not have. Continuing this line means building argument-principle / pivotal-category / moment-problem theory upstream, which is a project, not a drain.

The `96` Prop-valued fields are the separate and larger surface, and `qou-ar7f` re-scopes them: three of the four in `QOU/Mathlib/HeckeAlgebra.lean` are shadows of a concrete development, and the owner decision there (retire vs re-point) is still open.


## 2026-09-03 — the AXIOM tier triaged (the class tier was #6512; this is the other half)

#6512 triaged the 38 Mathlib-shaped uninhabited **classes** and concluded the
tractable tier was exhausted. It never looked at the **axioms**. Measured now,
same method (every verdict a grep over `.lake/packages/mathlib/Mathlib`, not an
inference):

| tier | count |
|---|---|
| external literature, cited by design | 10 |
| conjectural, honestly marked | 2 |
| SDP / convex duality | 5 |
| complex analysis (residue / winding) | 1 |
| **in-corpus, potentially provable** | **1** |

**One axiom closed this session: `seminormalDim_pos`, 20 → 19.** It was a cited
`axiom` beside `opaque seminormalDim`, whose docstring said *"axiomatised
pending the Mathlib `StandardYoungTableau` enumeration"*. That enumeration had
since been built in-repo (`QOU.Mathlib.numStandardYoungTableaux`), along with
both instances positivity needs — `instFinite` and a sorry-free `Nonempty` via
the row-superstandard tableau. It closed to `Nat.card_pos`. **The blocker was
cleared by unrelated later work and nobody re-read the axiom.** No detector in
the repo can see that: the axiom was well-formed and honestly cited.

**The SDP five are blocked one level LOWER than they state.** They cite
Goldman–Tucker / Alizadeh–Haeberly–Overton. Mathlib has neither, and it also
lists **strong conic duality itself** as not-yet-done in its own source
(`Analysis/Convex/Cone/Basic.lean` TODO). It has Farkas
(`ProperCone.hyperplane_separation`) and stops there. Closing this tier means
building conic-program duality first — a real upstream contribution, which is
directly relevant to this bean's open "should we open an upstream build"
question. Note the argument principle (#6512's candidate) and conic duality are
now two independent upstream targets, not one.

**The one lead:** `evenPower_necessary_for_blockPosSemidef`
(`QOU/BraidKnot/PSDFeasibilityProxy.lean:76`) — the only axiom of the 19 whose
content is an in-corpus claim about in-corpus objects rather than a citation.
Not attempted.

Two grep traps recorded, both hit while measuring: `dualCone` returns 0 while
`innerDualCone` exists (case-sensitivity), and `slater` matches
`IsLaterCommand` in a linter file (word inside a word). Neither announced
itself; both were caught only by re-running.

Full table: [`docs/audits/2026-09-03-axiom-tier-triage.md`](../docs/audits/2026-09-03-axiom-tier-triage.md).


## 2026-09-04 — RETRACTION: the axiom triage above covers the LIBRARY, not the corpus

The entry immediately above reports "19 axioms" and "0 sorries". Both are
**library-tree only** — `folio/quantum-observable-universe/lean`, the Lake
tree of one paper. Corpus-wide on `origin/main`:

| | said | actual (3529 files) |
|---|---|---|
| `.lean` files | 2552 | **3529** |
| real `sorry` terms | 0 | **9** — 8 cited, **1 uncited** |
| `axiom` declarations | 19 | **182** — 118 cited |

Missing: **944 content-block siblings**, and the **UGB / Fred2005** Lake
trees. Under AGENTS.md §0a a sibling resolves *before* the library, so the
sibling tree is what a block's `lean.ref` actually reaches — the more
load-bearing one.

**The Mathlib verdicts are unaffected** (no `℘`, `JucysMurphy`, `Hoefsmit`,
`windingNumber`, residue theorem, strict complementarity, Goldman–Tucker;
Farkas present, strong conic duality a TODO in Mathlib's own source). Those
are facts about Mathlib, not about which tree was walked. **The 163 axioms
outside the library are untriaged.**

**The scope gap was hiding a live defect**, which is the reason to record
this rather than just fix the number.
`mass-theory/delta-max-uniform-bound.lean` carried

    theorem delta_max_uniform_bound : sorry -- Ref: kassel1995 := sorry

with the **type** a `sorry` — the declaration has no statement, so there is
nothing it could be wrong about. A shadowing stub in the exact §0a STRICT
sense: `QOU/MassEndomorphism/DeltaMaxUniformBound.lean:93` holds the real
`|b.delta n| ≤ b.deltaMax`, proved and cited, and the sibling resolved
first, so `prop:delta-max-uniform-bound` reached `sorry : sorry` instead.
`conj-canonical-knot-id-sdp` depends on that proposition. Removed;
`#print axioms` on the library theorem is clean.

Left undone and flagged: the library file is `DeltaMaxUniformBound.lean`
while the decl is `delta_max_uniform_bound`, so §0a candidate 2 (path) misses
and resolution falls to candidate 3 (grep). §0a says align a mis-named
library file — but it carries five declarations, so renaming it for one is
wrong.

## 2026-09-08: twin qou-vkmt (identical title, in-progress, self-declared duplicate) cross-referenced; this bean is the record. Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7.



## Reorganisation 2026-10-04

Now the epic for P3.AN under Lean / Mathlib foundations.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-17 — Spherical Trace Coherence & Parallelogram Contour Primitive Cancellation (`litlfred/qou#8237`)
- Formalized `spherical_trace_coherence_two_sector` and `parallelogram_contour_primitive_sum_eq_zero` over generic `CommRingOps R` in `folio/quantum-observable-universe/lean/QOU/Foundations/BarConditionHyperbolicSphericalMetric.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `62b14488de4f16d02964a9976964f16ed12bcdcd`, PR [https://github.com/litlfred/qou/pull/8237](https://github.com/litlfred/qou/pull/8237)).
- Kept `status: in-progress` per no-unilateral-closure policy.

### Progress Update (2026-11-17, Round 59 — lane-e667)
- **PR:** `litlfred/qou#8291` (`https://github.com/litlfred/qou/pull/8291`), head `97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`COMMIT1 = 9f95671d31537da41246588ea9801b300607f995`), labeled `ready-to-merge` + `release`, `ready: 97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`https://github.com/litlfred/qou/pull/8291#issuecomment-6944908884`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/HyperbolicScalingDescartesCubicFarkasDuality.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-322e`: `chordal_step_symmetry_diagonal_and_concatenation` over `CommRingCarrier R`.
  - `qou-4tsl`: `alternating_two_wedge_antisym_and_three_wedge_vanishing` and `alternating_two_wedge_ring_antisym_and_diag` over `Int` and `CommRingCarrier R`.
  - `qou-5gai`: `dilation_cube_jacobian_density_cancellation` over `CommRingCarrier R`.
  - `qou-7y3g`: `classical_av4_cubic_factorization_and_complex_roots` over `Int`.
  - `qou-9h4t`: `primal_dual_slack_gap_and_complementary_slackness` over `Int`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/hyperbolic_scaling_descartes_cubic_farkas_duality_probe.py` + `computations/probes/hyperbolic-scaling-descartes-cubic-farkas-duality.witness.json` (`scriptHash = 9b07010b5e8c`, `scriptCommitSha = 9f95671d31537da41246588ea9801b300607f995`, `allPassed = True`).
- **Adversarial Cross-Review (Round 59):** Verified `litlfred/qou#8276` (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`, `0` advisories) and remediated `3 major, 2 advisory` borrowed-name findings on sibling PR `litlfred/qou#8261`, pushing `77aeb5c622eb2876245d1628c2f107b5f85999f8` and posting `ready: 77aeb5c622eb2876245d1628c2f107b5f85999f8` (`https://github.com/litlfred/qou/pull/8261#issuecomment-6942739479`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.

### Progress Update (2026-11-17, Round 60 — lane-e667)
- **PR:** `litlfred/qou#8299` (`https://github.com/litlfred/qou/pull/8299`), head `7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`COMMIT1 = a21b136d3f122bac6df50bab417b7232ca55064f`), labeled `ready-to-merge` + `release`, `ready: 7794a07bbdcd4212b670d7ed777098efe60dc9a4` (`https://github.com/litlfred/qou/pull/8299#issuecomment-6945265144`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AnnulusWindingLogCountingLieCurvatureHemisphereInversionZAxisBound.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-argp`: `annulus_winding_step_and_single_zero_uniqueness`.
  - `qou-bp5n`: `radial_log_counting_decomposition_and_increment`.
  - `qou-ghc6`: `matrix_one_form_commutator_trace_and_flat_curvature`.
  - `qou-h2mb`: `hemisphere_inversion_radial_reversal_and_tangential_fix`.
  - `qou-i0sr`: `vertical_step_energy_dominance_and_telescoping_bound`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/annulus_winding_log_counting_lie_curvature_hemisphere_inversion_z_axis_bound_probe.py` + `computations/probes/annulus-winding-log-counting-lie-curvature-hemisphere-inversion-z-axis-bound.witness.json` (`scriptHash = 001b12183bba`, `scriptCommitSha = a21b136d3f122bac6df50bab417b7232ca55064f`, `allPassed = True`).
- **Adversarial Cross-Review (Round 60):** Verified `litlfred/qou#8291` (`97f9ffaed50b1b3971470d9bc651293cd4f935e3`, `0` advisories) and remediated `1 major, 1 advisory` borrowed-name findings on sibling PR `litlfred/qou#8277`, pushing `845c943537ff3112ef1cadf49f54381fb96fcb38` and posting `ready: 845c943537ff3112ef1cadf49f54381fb96fcb38` (`https://github.com/litlfred/qou/pull/8277#issuecomment-6945121466`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
