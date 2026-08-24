import Mathlib.Analysis.SpecialFunctions.Pow.Real
import QOU.Shared.ArchimedeanEval

/-!
# QOU.Information.toffoli_transfer_matrix

**Canonical declaration** for content block
[`prop:toffoli-transfer-matrix`](../../../quantum-observable-universe/information-theory/toffoli-transfer-matrix.md): *QOU.Information.toffoli_transfer_matrix*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

## Base ring (§7c) — `ℝ` here is correct

`ToffoliTransferMatrixContext` inherits a generic coefficient ring `R` from
`QOU.Shared.MarkovTraceContext`, but this block's amplitudes stay at
`ℝ`: sub-claim (vi) is the closed form
`P_{7,7} = (q + Real.sqrt q − 1) / (q + 1)`, and a square root is an
archimedean construct with no counterpart over a generic `CommRing`.  The whole
family of amplitudes is stated at the same specialisation for coherence, so the
block sits after the substrate→archimedean wall.  Reviewed under bean
`qou-mtcx`; do not "port" it to `R` to reduce an `ℝ` count.

`q_real` is genuinely used (it is the argument of `Real.sqrt`) and is now
**tied** to the inherited `q : R` (bean `qou-mt7r`): the class extends
`QOU.Shared.ArchimedeanEval`, which carries an assumed evaluation
`eval : R →+* ℝ` and derives `q_real := eval q`.  It used to be an independent
field, so sub-claim (v) — the classical limit `q_real = 1 → P_flip k = 0` —
could hold at `q_real = 1` while the substrate parameter sat anywhere at all.
The evaluation is assumed, not constructed: it is **not** the archimedean
τ-functor, and `ArchimedeanEval.ofRingHom` machine-checks how little it takes
to inhabit.
-/


namespace QOU.Information


/-- Abstract context for the `toffoli_transfer_matrix` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class ToffoliTransferMatrixContext extends QOU.Shared.ArchimedeanEval where
  /-- Target-flip amplitude on a 3-strand nuclear braid, indexed by
      the two control types `(k₁, k₂) ∈ {0,1}²`. -/
  P_flip : ℕ × ℕ → ℝ
  /-- Crossing coefficient `c_{k₁ k₂}` of the control–control pair. -/
  c : ℕ × ℕ → ℝ
  /-- Universal core amplitude `Φ(q) = (q − 1)(q^{3/2} + q^{1/2} − 1)
      (q^{3/2} + q + 1) / (2(q + 1)²)`. -/
  Phi : ℝ
  /-- Manuscript sub-claim (i) — Universal factorisation: every target-
      flip amplitude factors as `P_flip(k₁, k₂) = c_{k₁ k₂} · Φ(q)`. -/
  claim_i_target_flip_amplitude : ∀ k : ℕ × ℕ, P_flip k = c k * Phi
  /-- Markov parameter `z = 1/(q^{1/2} + q^{-1/2})` specialised to `ℝ`. -/
  z_real : ℝ
  /-- Traced volume `V̂₁(k)` at generator `σ₁` for control type `k`. -/
  V_hat_1 : ℕ × ℕ → ℝ
  /-- Affine offset `d_{k₁k₂}` of the σ₁ transfer: `0` for `𝔭𝔭`,
      `−(q − q⁻¹)/2` for mixed, `−(q − q⁻¹)` for `𝔫𝔫`. -/
  d : ℕ × ℕ → ℝ
  /-- Manuscript sub-claim (ii) — σ₁ control-crossing transfer:
      `V̂₁(k) = z·c(k) + d(k)`, which is **type-dependent** (NOT `= z`;
      the `d` offset distinguishes the control types). A target-flip
      fixes the control pair `k`, so the target-flip difference
      `Δ₁ = 0` — the control crossing is unchanged, not type-blind. -/
  claim_ii_generator_crossing_traced : ∀ k : ℕ × ℕ, V_hat_1 k = z_real * c k + d k
  /-- The target-flip amplitude `P_{7,6}(q) = 1 · Φ(q) = Φ(q)`
      (governor / q-AND choice). -/
  P_7_6 : ℝ
  /-- Manuscript sub-claim (iii) — Governor choice: the Toffoli gate
      selects the all-proton control pair (`c = 1`), giving
      `P_{7,6}(q) = Φ(q)`. -/
  claim_iii_toffoli_gate_selects : P_7_6 = Phi
  /-- The target-flip amplitude `P_{6,7}(q)` in the antisymmetric
      orbit position. -/
  P_6_7 : ℝ
  /-- Manuscript sub-claim (iv) — Antisymmetry: `P_{6,7}(q) =
      −P_{7,6}(q)`. -/
  claim_iv_antisymmetry : P_6_7 = - P_7_6
  /-- Manuscript sub-claim (v) — Classical limit: every target-flip
      amplitude vanishes at `q = 1` because the core carries `(q − 1)`. -/
  claim_v_classical_limit : ∀ k : ℕ × ℕ, toArchimedeanEval.q_real = 1 → P_flip k = 0
  /-- The Toffoli-diagonal amplitude `P_{7,7}(q) = (q + q^{1/2} − 1) /
      (q + 1)`. -/
  P_7_7 : ℝ
  /-- Manuscript sub-claim (vi) — Toffoli diagonal closed form:
      `P_{7,7}(q) = (q + √q − 1) / (q + 1)`. -/
  claim_vi_diagonal_formula :
    P_7_7 = (toArchimedeanEval.q_real + Real.sqrt toArchimedeanEval.q_real - 1) / (toArchimedeanEval.q_real + 1)
/-- **Proposition statement** (from manuscript):

Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip
amplitude on a $3$-strand nuclear braid with control types
$(k_1, k_2) \in \{0,1\}^2$ and target strand $3$, constructed
from the Hecke crossing coefficients
([transfer matrix product](#prop:skein-polynomial-transfer-matrix)).
Then:*

1.

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/information-theory/toffoli-transfer-matrix.ts
noncomputable def toffoli_transfer_matrix [ctx : ToffoliTransferMatrixContext] :
    (∀ k : ℕ × ℕ, ctx.P_flip k = ctx.c k * ctx.Phi) ∧
    (∀ k : ℕ × ℕ, ctx.V_hat_1 k = ctx.z_real * ctx.c k + ctx.d k) ∧
    ctx.P_7_6 = ctx.Phi ∧
    ctx.P_6_7 = - ctx.P_7_6 ∧
    (∀ k : ℕ × ℕ, ctx.q_real = 1 → ctx.P_flip k = 0) ∧
    ctx.P_7_7 = (ctx.q_real + Real.sqrt ctx.q_real - 1) / (ctx.q_real + 1) :=
  ⟨ctx.claim_i_target_flip_amplitude, ctx.claim_ii_generator_crossing_traced,
   ctx.claim_iii_toffoli_gate_selects, ctx.claim_iv_antisymmetry,
   ctx.claim_v_classical_limit, ctx.claim_vi_diagonal_formula⟩

end QOU.Information
