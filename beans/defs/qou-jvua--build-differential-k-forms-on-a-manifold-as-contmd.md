---
# qou-jvua
title: 'BUILD: differential k-forms on a manifold as ContMDiffSection of the alternating bundle — Mathlib has them on normed spaces only'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:07:55Z
updated_at: 2026-11-20T21:27:24Z
parent: qou-c8p8
---

**BUILD (also upstreamable).** The corpus cannot state `Θ ∧ dΘ`, or the hyperbolic
volume form, *as a form*. `QOU/Eightfold/ContactDistributionRank.lean` and
`QOU/Eightfold/HyperbolicVolumeFormType.lean` are honest about this and work entirely
in `ℕ` arithmetic as a result — every "degree 3" statement there is a `Nat.choose`
identity, not a statement about a form.

**Mathlib status, measured 2026-09-04 at mathlib `f897ebcf72c`:**
* `Analysis/Calculus/DifferentialForm/Basic.lean` — forms and `extDeriv` on a **normed
  space**, with `d ∘ d = 0`. Present.
* Manifolds — **absent**, and Mathlib says so: its own TODO at `Basic.lean:34-38` reads
  *"same for manifolds (**not defined yet**)"* and asks for a Zulip design discussion.
* `grep -rn 'MDifferentiableForm\|DifferentialForm' Geometry/` → nothing.
* No Hodge star (`Hodge` occurs once in all of Mathlib, at `ModelTheory/Fraisse.lean:60`,
  citing the model theorist W. Hodges).
* Stokes exists only as the divergence theorem
  (`MeasureTheory/Integral/DivergenceTheorem.lean`).

**Construction:** a `C^r` `k`-form on `M` is a `ContMDiffSection`
(`Geometry/Manifold/VectorBundle/SmoothSection.lean:325`) of the bundle whose fibre at
`x` is `ContinuousAlternatingMap ℝ (TangentSpace I x) F (Fin k)`. The fibre type, the
bundle constructions (`VectorBundle/Hom.lean`,
`Topology/VectorBundle/Constructions.lean`) and the pointwise exterior derivative all
exist; the work is assembling the bundle and transporting `extDeriv` chart-wise.

**Size: ~300-600 lines.** The largest BUILD item in the inventory, and the one that
unblocks the most: it is the prerequisite for any statement about the contact volume
form or the hyperbolic volume form as objects rather than as degree counts.

Classified BUILD rather than UPSTREAM because an in-repo version unblocks the arc now
and the upstream route is gated on Mathlib's requested design discussion. Upstreaming
later is not foreclosed.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B3, §H2.

SCOPE CORRECTION 2026-09-04 (roast R1-R3, docs/audits/2026-09-04-roast-of-the-two-inventories.md).

This bean justifies itself as 'the prerequisite for any statement about the contact volume form or the hyperbolic volume form as objects rather than as degree counts'. HALF of that is wrong.

For the HYPERBOLIC form it is right. For the CONTACT form it is not, and the arc's own strongest result says so: QOU/QuantumObservableUniverse/CalculusDimensionObstruction.lean:63 states the categorical route is 'stronger, because it needs no manifold, no metric, no H = ker Theta subset TM', and :156 has the volume form 'constructed with no manifold'. Theta_A wedge d Theta_A in the Woronowicz calculus on O_q(SU(2)) IS the contact volume form as an object. The corpus already has it.

CONSEQUENCE FOR RANKING. The surviving half serves the hyperbolic route, which bean qou-52fu (completed 2026-08-04, same epic) calls rank-1: the complement's holonomy is rho: pi_1 -> PSL(2,C), i.e. MORE SL(2), not SU(3). So 300-600 lines is not the cheapest next step and 'unblocks the most' overstates it. qou-tc8y (~5 lines, a sealed opaque whose body is already written sorry-free next door) almost certainly is.

STILL WORTH DOING, on a narrower claim: Milnor's Lambda-sum is currently a DEFINITION (MathlibExt/IdealTriangulation.lean:100 says so explicitly), and only forms would let anyone connect it to a metric volume. That is the honest motivation - not 'any statement about a volume form as an object'.

### Progress Update (2026-11-17, Round 61 — lane-e667)
- **PR:** `litlfred/qou#8303` (`https://github.com/litlfred/qou/pull/8303`), head `2a91d843d44db15a0190138e20fb1878634fbbeb` (`COMMIT1 = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`), labeled `ready-to-merge` + `release`, `ready: 2a91d843d44db15a0190138e20fb1878634fbbeb` (`https://github.com/litlfred/qou/pull/8303#issuecomment-6945508253`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AlternatingThreeFormPrimaryFactorUpperHalfPlaneCatalanClausenSymmetry.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-jvua`: `alternating_three_form_antisym_diag_and_unit_frame`.
  - `qou-kp89`: `primary_factor_linear_cancellation_and_cubic_remainder`.
  - `qou-m8xt`: `upper_half_plane_shifted_modulus_pos_and_cyclic_closure`.
  - `qou-mame`: `quarter_turn_even_vanishing_and_odd_alternation`.
  - `qou-u4mx`: `termwise_periodic_and_odd_two_harmonic_sum`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/alternating_three_form_primary_factor_upper_half_plane_catalan_clausen_symmetry_probe.py` + `computations/probes/alternating-three-form-primary-factor-upper-half-plane-catalan-clausen-symmetry.witness.json` (`scriptHash = 0ee532c9f9a2`, `scriptCommitSha = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`, `allPassed = True`).
- **Adversarial Cross-Review (Round 61):** Verified `litlfred/qou#8285` (`250465c60a6cea44d9f569e88cc79ee2c8d8051b`, `0` advisories on all 5 added theorems, valid witness `39a564805d3e`) and `litlfred/qou#8299` (`7794a07bbdcd4212b670d7ed777098efe60dc9a4`, `0` advisories, valid witness `001b12183bba`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.

## 2026-11-20 — first tranche (PR #8678): `QOU/Mathlib/ManifoldForms.lean`

Proved, sorry-free: `extDeriv_pullback` (naturality d∘φ* = φ*∘d for C² maps, any nontrivially normed field); `ManifoldForm` (pointwise), `inChart`, `extDeriv_inChart_eq_pullback` (chart-wise d is chart-independent, boundaryless). NOT built: alternating-map vector bundle / ContMDiff sections; global `d : ManifoldForm k → ManifoldForm (k+1)` and d∘d = 0 on M; wedge, integration, Stokes; boundary. Needs 18 manifold oleans missing from the cache (gap-cone script builds them).
