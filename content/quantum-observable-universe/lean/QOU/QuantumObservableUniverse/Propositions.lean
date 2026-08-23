import QOU.QuantumObservableUniverse.Instanton
import QOU.QuantumObservableUniverse.CRRealisation
import QOU.QuantumObservableUniverse.Particles

/-!
# §6–§7  Lemmas, Propositions, and Classical Limits

Irreducibility of the instanton connection, self-duality of curvature,
the main commutative diagram, and classical-limit recovery theorems.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-! ## §6  Lemmas and Propositions -/

/-- A connection is **irreducible** if its covariant-constant adjoint
    sections are trivial. -/
def InstantonConnection.IsIrreducible {cr : CRManifoldData}
    (inst : InstantonConnection cr) : Prop :=
  Subsingleton inst.parallelAdjointSections

/-- **Lemma (Irreducibility of the connection).**
    LaTeX: `\label{lem:irreducible-connection}` -/
theorem irreducible_connection (cqou : CQuantumObservableUniverse)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (embed : inst.parallelAdjointSections → cqou.adjointSections)
    (h_inj : Function.Injective embed) :
    inst.IsIrreducible :=
  ⟨fun _ _ => h_inj (cqou.adjoint_cohomology_vanishes.allEq _ _)⟩

/-- **Proposition (Self-duality of the curvature).**
    LaTeX: `\label{prop:self-dual-curvature}` -/
theorem self_dual_curvature (cqou : CQuantumObservableUniverse)
    (hn : cqou.n = 2)
    (inst : InstantonConnection cqou.toCRManifoldData) :
    (inst.hodgeStar hn).IsSelfDual inst.curvature_H := by
  exact inst.self_dual hn

/-- **Main Commutative Diagram data.**
    LaTeX: `\label{prop:main-commutative-diagram}` -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
structure MainCommutativeDiagram (cqou : CQuantumObservableUniverse)
    (sp : ArchimedeanSubstrateField cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData) where
  /-- The type of first-order jet data `J¹E`. -/
  JetBundle : Type*
  /-- The type of field-equation solutions. -/
  FieldEqns : Type*
  /-- The type of linearised sections `Γ(E_lin)`. -/
  LinSections : Type*
  /-- The type of q-Schrödinger solutions. -/
  Solutions : Type*
  /-- Top: Euler–Lagrange operator `E[S_q] : J¹E → FieldEqns`. -/
  euler_lagrange : JetBundle → FieldEqns
  /-- Left: jet evaluation `j : J¹E → Γ(E_lin)`. -/
  jet_eval : JetBundle → LinSections
  /-- Right: substrate coupling `κ : FieldEqns → Solutions`. -/
  substrate_coupling : FieldEqns → Solutions
  /-- Bottom: parallel transport `∇^A : Γ(E_lin) → Solutions`. -/
  parallel_transport : LinSections → Solutions
  /-- **Commutativity**: `κ ∘ E[S_q] = ∇^A ∘ j`. -/
  commutes : ∀ (x : JetBundle),
    substrate_coupling (euler_lagrange x) = parallel_transport (jet_eval x)

-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
theorem main_commutative_diagram (cqou : CQuantumObservableUniverse)
    (sp : ArchimedeanSubstrateField cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (diag : MainCommutativeDiagram cqou sp inst) :
    ∀ (x : diag.JetBundle),
      diag.substrate_coupling (diag.euler_lagrange x) =
      diag.parallel_transport (diag.jet_eval x) :=
  diag.commutes

/-! ## §7  Classical Limit Properties -/

/-- At classicality (`q = 1`), the quantum Planck constant vanishes. -/
theorem planck_classical_limit {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) (hq : sp.field p = 1) :
    quantumPlanckConstant sp p = 0 := by
  unfold quantumPlanckConstant
  rw [hq, inv_one, sub_self]

/-- The q-deformed exterior derivative recovers `d` at `q = 1`. -/
theorem qExtDeriv_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (d_alpha lieDerivReeb theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qExtDeriv sp d_alpha lieDerivReeb theta p = d_alpha p := by
  unfold qExtDeriv
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

/-- The q-deformed Lie bracket recovers the classical bracket at `q = 1`. -/
theorem qLieBracket_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (bracket_VW thetaV_LxiW thetaW_LxiV : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qLieBracket sp bracket_VW thetaV_LxiW thetaW_LxiV p = bracket_VW p := by
  unfold qLieBracket
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

/-- The q-deformed connection recovers the classical connection at `q = 1`. -/
theorem qConnection_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (connA iotaXiA theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qConnection sp connA iotaXiA theta p = connA p := by
  unfold qConnection
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
