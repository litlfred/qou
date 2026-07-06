# Sorry Stubs Audit & Classification Report

This report presents a complete audit of all `sorry` stubs in the Lean project located under `content/quantum-observable-universe/lean/QOU/`. 

## 1. Executive Summary

A comprehensive scan and parsing of the codebase was conducted to identify and separate actual code occurrences of the `sorry` keyword from comments/docstring matches. 

### Key Statistics
| Category | Metric |
|---|---|
| Unique `.lean` files containing code `sorry` | **151** |
| **Total code `sorry` stubs** | **157** |
| ↳ Conjectural class-body/instance field sorries (§3b-cond permanent) | **8** |
| ↳ Regular proof stubs (to be formalized) | **149** |

---

## 2. Conjectural Class-Body / Instance Sorries (§3b-cond)

Under **AGENTS.md §3b-cond**, these stubs represent open mathematical conjectures. They are encoded as `sorry` fields inside typeclass instances or declarations, allowing downstream theorems to carry conditional hypotheses. **These must not be discharged.**

There are exactly **8** such stubs in the codebase:

1. **`AppendixSurreals/BigbangHeatdeath.lean:46`**
   - **Signature**: `noncomputable instance : BigbangHeatdeath := by sorry`
   - **Context**: Speculative evaluation of named surreal endpoints for cosmological functors.
2. **`Archimedean/EmCouplingBringZeroMode.lean:194`**
   - **Signature**: `bring_zero_mode_realised := sorry` in `instance canonical : BringZeroModeBlochClass`
   - **Context**: Conjectural representation of the Bring-surface Bloch class realising $2/(3\pi)$ Hodge ratio.
3. **`Archimedean/HyperbolicVolumeIndependence.lean:42`**
   - **Signature**: `no_relation := by sorry` in `noncomputable instance : HyperbolicVolumeIndependence`
   - **Context**: Conjectural algebraic independence over $\mathbb{Q}$ of hyperbolic volumes $\operatorname{Vol}(4_1)$, $\operatorname{Vol}(5_2)$, and $\operatorname{Vol}(\mathcal{B}_3)$.
4. **`BraidKnot/CemeteryGroupEmergence.lean:80`**
   - **Signature**: `monotone_under_extension _ _ := sorry` in `instance canonical : CemeteryGroupEmergence`
   - **Context**: Braid prune "kill switch" properties in the Garside-reduction order engine.
5. **`BraidKnot/ConfinementGradingCorrespondence.lean:80`**
   - **Signature**: `filtrations_agree _ := sorry` in `instance canonical : ConfinementGradingCorrespondence`
   - **Context**: Agreement between KLR $\mathbb{Z}$-grading filtration and the confinement filtration.
6. **`BraidKnot/GSReductionOrder.lean:128`**
   - **Signature**: `order_match _ := sorry` in `instance canonical : GSOrderMatch`
   - **Context**: General order-match for KLR grading and Garside-reduction confinement level.
7. **`BraidKnot/HeckeAnyonicSubstrate.lean:88`**
   - **Signature**: `anyonic_holds T := sorry` in `instance canonical : HeckeAnyonicSubstrate`
   - **Context**: Braid action compatibility on anyonic substrate states.
8. **`Interactions/QIntegerMassFormula.lean:177`**
   - **Signature**: `fits_AME := sorry` in `noncomputable instance canonical : QIntegerMassFormula`
   - **Context**: Binding energy fit of the 7-term q-integer formula against experimental Atomic Mass Evaluation (AME) data.

---

## 3. Regular Proof Stubs (149 Total)

These represent standard mathematical statements (theorems, lemmas, or non-conjectural definitions) that are currently sorry'd and represent active targets for formalization.

### A. Placeholder Stubs (139 stubs in 139 files)
A total of **139** files are placeholder stubs (managed via the `updatedPlaceholders` schema in `triage_report.json`). Each file contains exactly **1** regular theorem of the form:
`theorem foo [ctx : ContextType] : ctx.holds := sorry`
These stubs have been cleaned of outdated `- placeholder stub` headers and present clean `sorry` bodies waiting for mathematical implementation.

### B. Library / Extension Stubs (10 stubs in 4 files)
The remaining **10** regular stubs reside in 4 main source/extension files:

#### 1. `HyperellipticQuintic/zeta5_residue_monodromy.lean` (7 stubs)
Chiral lone-pair monodromy over the hyperelliptic quintic $y^2 = x^5 - 1$.
- **`zeta5_pow_five`** (line 50): Prove $\zeta_5^5 = 1$.
- **`zeta5_reductions`** (line 55): Exponent reductions $\zeta_5^9 = \zeta_5^4$ and $\zeta_5^{16} = \zeta_5$.
- **`gauss_sum_5_reduced`** (line 60): Gauss sum reduction to $1 + 2\zeta_5 + 2\zeta_5^4$.
- **`zeta5_add_inv`** (line 65): Identity $\zeta_5 + \zeta_5^4 = 2\cos(2\pi/5)$.
- **`cos_two_pi_fifths`** (line 73): Exact value $\cos(2\pi/5) = \frac{\sqrt{5}-1}{4}$ (reducible to Mathlib's `Real.cos_pi_div_five`).
- **`gauss_sum_5_eval`** (line 78): Proving the Gauss sum evaluates to $\sqrt{5}$.
- **`gauss_sum_5_abs`** (line 83): Proving the absolute value is $\sqrt{5}$.

#### 2. `LiftingDescent/JetProlongation.lean` (1 stub)
- **`pentagon_inter_level_placeholder`** (line 293): Backward-compatibility placeholder for inter-level operator lift.

#### 3. `Substrate/ProtonMassSubstrateIdentity.lean` (1 stub)
- **`F_Bor`** (line 22): Noncomputable definition representing the Borromean categorical observable.

#### 4. `MathlibExt/Scratch.lean` (1 stub)
- **`quadratic_form_two_index_proof`** (line 15): Quadratic form expansion for $2 \times 2$ symmetric matrices.

---

## 4. Batch 1 Recommendation (First 10 Easiest Stubs)

These 10 stubs are recommended as the first target batch. They are highly tractable, relying on basic algebra, trigonometric identities, or structural rewrites rather than deep topological or analytical proofs.

| # | File | Line | Name | Rationale |
|---|---|---|---|---|
| **1** | `BraidKnot/IsotopeKnot/equivalence.lean` | 73 | `equivalence` | **Structural**. Can be proved in a single line using constructor application `⟨ctx.claim_reflexivity, ...⟩` since the context class exposes all three required properties (refl, symm, trans) as fields. |
| **2** | `Torsion/antiparticle_crossing_reversal.lean` | 72 | `antiparticle_crossing_reversal` | **Structural**. Similar to `equivalence`, the theorem unpacks the context's `reversal_active` property and applies the `impl_*` fields directly. |
| **3** | `MathlibExt/Scratch.lean` | 15 | `quadratic_form_two_index_proof` | **Algebraic**. Expansion of `dotProduct` and matrix `mulVec` for a 2-dimensional index vector. Proved via basic matrix component rewrites and `ring` algebra. |
| **4** | `HyperellipticQuintic/zeta5_monodromy.lean` | 50 | `zeta5_pow_five` | **Algebraic**. Follows immediately from `zeta5` definition via `Complex.exp` and Mathlib's `exp_two_pi_mul_I` type identities. |
| **5** | `HyperellipticQuintic/zeta5_monodromy.lean` | 55 | `zeta5_reductions` | **Algebraic**. Directly follows from `zeta5_pow_five` using exponent arithmetic. |
| **6** | `HyperellipticQuintic/zeta5_monodromy.lean` | 60 | `gauss_sum_5_reduced` | **Algebraic**. Requires substituting the definition of `gauss_sum_5` and applying the reductions. |
| **7** | `HyperellipticQuintic/zeta5_monodromy.lean` | 65 | `zeta5_add_inv` | **Trigonometric**. Re-expressing $e^{i\theta} + e^{-i\theta} = 2\cos\theta$ using $\zeta_5^4 = \zeta_5^{-1}$ and Euler's formula on complex numbers. |
| **8** | `HyperellipticQuintic/zeta5_monodromy.lean` | 73 | `cos_two_pi_fifths` | **Trigonometric**. Double-angle relation `cos(2x) = 2\cos^2(x) - 1` applied to `Real.cos_pi_div_five`, which is a proven constant in Mathlib. |
| **9** | `HyperellipticQuintic/zeta5_monodromy.lean` | 78 | `gauss_sum_5_eval` | **Algebraic**. Combines the reduced form, the inverse sum evaluation, and the cosine value. |
| **10** | `HyperellipticQuintic/zeta5_monodromy.lean` | 83 | `gauss_sum_5_abs` | **Algebraic**. Follows immediately from `gauss_sum_5_eval` and the fact that $\sqrt{5}$ is a positive real number. |
