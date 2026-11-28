import QOU.Observations.KnotConvolutionOperator
import QOU.LiftingDescent.GmFormalExp

/-!
# Knot convolution operators are exponentials of tangent elements

`KnotConvolutionOperator.lean`: a knot `K` acts on the colour-`N` Peter–Weyl block of
`O_q(SU(2))` by one scalar `c_N(K)`, the normalised coloured Jones polynomial, and connected sum
is composition (`ofJones_connSum`). Write `q = e^ℏ` and take the scalars in `K⟦ℏ⟧`. At `ℏ = 0`
(`q = 1`) the normalised coloured Jones polynomial of a knot is `1`, so each `c_N(K)` is a
`K⟦ℏ⟧`-point of `Ĝ_m`. Here that is the hypothesis `IsUnipotent z`:
`constantCoeff (z.c N) = 1` for every `N`. It is a property of the input series. The theorem that
it holds for every knot's coloured Jones expansion is not proved here.

* `logOp z`: the tangent family `N ↦ log c_N(K)`, with constant term `0` (`Ĝ_a`-points).
* `logOp_comp`: **`log` turns composition into addition**. With `ofJones_connSum`,
  `log c_N(K # K') = log c_N(K) + log c_N(K')` (`logOp_connSum`).
* `expOp`, `expOp_logOp`: **every unipotent operator is the exponential of its log**,
  `z = exp(log z)`.
* `logOp_expOp`, `expOp_add`: the inverse direction, and `exp(a + b) = exp a ∘ exp b`. So
  unipotent convolution operators under composition are isomorphic to tangent families under
  addition.

The operators are central (`act_mul_left`, `act_mul_right`), so no Baker–Campbell–Hausdorff
correction appears. Pure algebra over a field of characteristic `0`. No measured values.
-/

namespace QOU.Observations.KnotConvolutionOperator

open PowerSeries QOU.FormalGroups.GmLog

noncomputable section

variable {K : Type*} [Field K] [CharZero K]

/-- A convolution operator with scalars in `K⟦ℏ⟧` equal to `1` at `ℏ = 0`. -/
def IsUnipotent (z : ConvOp K⟦X⟧) : Prop := ∀ N, constantCoeff (z.c N) = 1

/-- A tangent family: scalars with constant term `0`. -/
def IsTangent (a : ConvOp K⟦X⟧) : Prop := ∀ N, constantCoeff (a.c N) = 0

/-- The tangent family `N ↦ log c_N`. -/
def logOp (z : ConvOp K⟦X⟧) : ConvOp K⟦X⟧ := ⟨fun N => formalLog (z.c N)⟩

/-- The operator `N ↦ exp a_N`. -/
def expOp (a : ConvOp K⟦X⟧) : ConvOp K⟦X⟧ := ⟨fun N => gmExp (a.c N)⟩

/-- Pointwise sum of tangent families. -/
def add (a b : ConvOp K⟦X⟧) : ConvOp K⟦X⟧ := ⟨fun N => a.c N + b.c N⟩

omit [CharZero K] in
theorem isTangent_logOp (z : ConvOp K⟦X⟧) : IsTangent (logOp z) :=
  fun _ => constantCoeff_formalLog _

omit [CharZero K] in
theorem isUnipotent_expOp (a : ConvOp K⟦X⟧) : IsUnipotent (expOp a) :=
  fun _ => constantCoeff_gmExp _

omit [CharZero K] in
theorem isUnipotent_comp {z w : ConvOp K⟦X⟧} (hz : IsUnipotent z) (hw : IsUnipotent w) :
    IsUnipotent (ConvOp.comp z w) := fun N => by
  simp [ConvOp.comp, map_mul, hz N, hw N]

/-- **`log` turns composition into addition.** -/
theorem logOp_comp {z w : ConvOp K⟦X⟧} (hz : IsUnipotent z) (hw : IsUnipotent w) :
    logOp (ConvOp.comp z w) = add (logOp z) (logOp w) := by
  simp only [logOp, add, ConvOp.comp, ConvOp.mk.injEq]
  funext N
  exact formalLog_mul (by rw [hz N]; exact one_ne_zero) (by rw [hw N]; exact one_ne_zero)

/-- **Connected sum is addition of logs.** -/
theorem logOp_connSum (J J' Jsum : ℕ → K⟦X⟧) (h : ∀ N, Jsum N = J N * J' N)
    (hJ : IsUnipotent (ConvOp.ofJones J)) (hJ' : IsUnipotent (ConvOp.ofJones J')) :
    logOp (ConvOp.ofJones Jsum) = add (logOp (ConvOp.ofJones J)) (logOp (ConvOp.ofJones J')) := by
  rw [ConvOp.ofJones_connSum J J' Jsum h, logOp_comp hJ hJ']

/-- **A unipotent operator is the exponential of its log.** -/
theorem expOp_logOp {z : ConvOp K⟦X⟧} (hz : IsUnipotent z) : expOp (logOp z) = z := by
  cases z with
  | mk c =>
    simp only [expOp, logOp, ConvOp.mk.injEq]
    funext N
    exact gmExp_formalLog (hz N)

theorem logOp_expOp {a : ConvOp K⟦X⟧} (ha : IsTangent a) : logOp (expOp a) = a := by
  cases a with
  | mk c =>
    simp only [expOp, logOp, ConvOp.mk.injEq]
    funext N
    exact formalLog_gmExp (ha N)

/-- **`exp(a + b) = exp a ∘ exp b`.** -/
theorem expOp_add {a b : ConvOp K⟦X⟧} (ha : IsTangent a) (hb : IsTangent b) :
    expOp (add a b) = ConvOp.comp (expOp a) (expOp b) := by
  simp only [expOp, add, ConvOp.comp, ConvOp.mk.injEq]
  funext N
  exact gmExp_add (ha N) (hb N)

/-- The unknot (identity operator) has log `0`. -/
theorem logOp_one : logOp (ConvOp.one : ConvOp K⟦X⟧) = ⟨fun _ => 0⟩ := by
  simp only [logOp, ConvOp.one, formalLog_one]

end

end QOU.Observations.KnotConvolutionOperator
