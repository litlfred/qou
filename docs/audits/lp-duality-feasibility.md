# LP Duality Infrastructure Feasibility Assessment

## Overview
This report assesses the feasibility of proving the `strong_duality` class fields (currently assumed as axioms or data fields) across 8 locations in the QOU formalization, focusing on the four representative files provided.

## Findings from Mathlib
A search of Mathlib (`Mathlib.Analysis.Convex.Cone.*`) reveals that:
- **Farkas' Lemma exists:** Mathlib contains geometric and relative interpretations of Farkas' Lemma for proper cones in topological real vector spaces and Hilbert spaces (e.g., `ProperCone.hyperplane_separation`).
- **Turnkey LP/SDP Strong Duality is missing:** The `Mathlib/Analysis/Convex/Cone/Basic.lean` explicitly lists in its TODOs to "Prove regular and strong duality for cone programs using Farkas' lemma". There is currently no out-of-the-box theorem for standard finite-dimensional LP duality or SDP strong duality.

## Assessment by File/Domain

### 1. `QOU.Molecular.shell_filling_rule`
- **Structure:** `ShellFillingRuleContext` assumes `primal_obj = Z * y_0`. A stronger class `ShellFillingLPDuality` provides an explicit dual optimality certificate (stationarity + complementary slackness).
- **Feasibility:** **Already proved (conditionally).** The strong duality identity is explicitly proved in 8 lines (`shell_filling_lp_strong_duality_of_certificate`) using pure algebra from the certificate, avoiding the need for a general strong duality theorem. However, constructing this certificate for any specific atom remains an open problem.

### 2. `QOU.ParticleInteractions.lp_dual_stability` & `confinement_frobenius_reciprocity`
- **Structure:** Both `LpDualStabilityContext` and `ConfinementFrobeniusReciprocityContext` abstractly assume strong duality over finite-dimensional LPs (e.g., `Fin channels → ℝ` and `Fin d → ℝ`).
- **Feasibility:** **Requires new infrastructure.** Because the problems do not carry explicit optimality certificates, the general LP strong duality theorem is required.
- **Path Forward:** One would need to formalize standard LP duality by instantiating Mathlib's conic Farkas' lemma for the positive orthant cone $\mathbb{R}^n_{\geq 0}$.

### 3. `QOU.Interactions.ConfinementSDP`
- **Structure:** `HasConfinementSDPStrongDuality` conditionally asserts `primalOpt = nTarget * y0Star` based on Slater-strict feasibility.
- **Feasibility:** **Requires new infrastructure.** Mathlib currently lacks SDP duality API.
- **Path Forward:** Requires building out conic duality (e.g., Boyd–Vandenberghe Thm 5.5) for the positive semidefinite cone using Slater's condition and Mathlib's existing Hahn-Banach/Farkas separation theorems.

## Conclusion and Estimated Difficulty
- **Provable with existing Mathlib?** No. While Farkas' lemma is present, the specific LP and SDP duality theorems have not yet been built on top of it.
- **New Infrastructure Needed:**
  1. Finite-dimensional LP Strong Duality (from Farkas' lemma).
  2. Conic/SDP Duality under Slater's condition.
- **Estimated Difficulty:** **Moderate to High.** Bridging Mathlib's abstract topological Farkas lemma to concrete matrix/vector block LPs involves significant boilerplate. SDP duality is particularly challenging due to the interior condition (Slater) on the PSD cone.
