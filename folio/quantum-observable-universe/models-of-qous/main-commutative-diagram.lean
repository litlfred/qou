import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.main_commutative_diagram — Central 4-square diagram

The diagram relating jets, Euler–Lagrange, Einstein equations, and
Schrödinger equation through the substrate field q:

  Jet bundle ──[EL operator]──→ Einstein equations
      |                              |
      | q-linearisation              | q → 1
      ↓                              ↓
  Sections ──[parallel transport]──→ Schrödinger equation

LaTeX label: `prop:main-commutative-diagram`

## References

- [leitner2026] §1-quantum-observable-universe/main-commutative-diagram

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section
/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Main commutative diagram data**.

    The four corners of the diagram are:
    1. Jet bundle J¹(S) (geometric, nonlinear)
    2. Einstein field equations (gravity)
    3. Linearized sections Γ(S) (quantum, linear)
    4. Schrödinger equation (quantum mechanics)

    The substrate parameter q mediates between geometric (gravity)
    and quantum (Schrödinger) descriptions. -/
-- Ref: [leitner2026] §1
structure MainCommutativeDiagram where
  /-- The substrate parameter q. -/
  q : R_q
  /-- The inverse indeterminate `q⁻¹`. Over `R_q = ℤ[q, q⁻¹]` the
      indeterminate is invertible; `qInv` names that inverse explicitly,
      since `R_q` is a `CommRing` without a global `Inv` instance. -/
  qInv : R_q
  /-- Defining relation `q · q⁻¹ = 1`. -/
  q_qInv : q * qInv = 1
  /-- Top-left corner: jet data (connection strength). -/
  jetValue : R_q
  /-- Top-right corner: Einstein tensor value. -/
  einsteinValue : R_q
  /-- Bottom-left corner: linearized section value. -/
  sectionValue : R_q
  /-- Bottom-right corner: Schrödinger evolution value. -/
  schrodingerValue : R_q
  /-- Top arrow: Euler–Lagrange operator maps jets to field equations. -/
  euler_lagrange : jetValue = einsteinValue
  /-- Bottom arrow: parallel transport maps sections to Schrödinger. -/
  parallel_transport : sectionValue = schrodingerValue
  /-- Left arrow: q-linearisation of jet data gives sections. -/
  q_linearisation : sectionValue = (1 - qInv) * jetValue

/-- **The diagram commutes.**

    Both paths from the jet bundle to the Schrödinger corner agree:
    going right along the Euler–Lagrange arrow and then down the
    `q → 1` edge gives `(1 − q⁻¹) · einsteinValue`, while going down
    the q-linearisation arrow and then right along parallel transport
    gives `schrodingerValue`.

    Commutativity is **derived** from the three arrow equations, not
    assumed: it was formerly a fourth field `commutativity` of
    `MainCommutativeDiagram`, which made this statement a restatement
    of its own hypothesis. The chain is
    `(1 − q⁻¹)·einstein = (1 − q⁻¹)·jet = section = schrodinger`. -/
-- Ref: [leitner2026] §1
theorem diagram_commutes (d : MainCommutativeDiagram) :
    (1 - d.qInv) * d.einsteinValue = d.schrodingerValue := by
  rw [← d.euler_lagrange, ← d.q_linearisation, d.parallel_transport]

end
end QOU
