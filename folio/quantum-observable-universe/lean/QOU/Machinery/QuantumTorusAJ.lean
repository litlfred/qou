import QOU.Machinery.QuantumTorus
import QOU.BraidKnot.AJFigureEight
import QOU.Mass.QDifferenceConfluentObstruction

/-!
# QOU.Machinery.QuantumTorusAJ — GGM/AJ and the binding q-lift as co-resident quantum-torus elements

**Infrastructure wiring** connecting three previously-separate corpus objects:

* the abstract quantum torus `T = A[L^±; σ]`
  (`QOU.Machinery.QuantumTorus`, brick B1 of the Nguyen–Tran strong-AJ
  decomposition),
* the concrete, sorry-free order-2 GGM/AJ annihilator of the figure-eight
  colored Jones tower (`QOU.BraidKnot.AJFigureEight.figureEightOperator`), and
* the proved binding q-lift kernel `[m+2]_q b_{m+2} = b_{m+1} + b_m`
  (`QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`).

## What is established here (sorry-free)

The coefficient ring is realised as the **diagonal M-operators** `A = ℤ → K`
(functions of the integer colour), carrying the σ-twist as translation
`σ(a)(N) = a(N+1)` — the paper's `σ(M) = c·M` with `M = q^N`, `c = q`.  On this
`A` the quantum torus `QuantumTorus (ℤ → K)` is a genuine skew-Laurent ring and:

1. **`act2`** — the order-≤2 **function-model action** of a torus element on a
   colour tower `J : ℤ → K`: it reads the element's `L^0, L^1, L^2` coefficients
   (`QuantumTorus.coeffAt`) and assembles the q-difference operator
   `coeffAt f 0 · J + coeffAt f 1 · shift J + coeffAt f 2 · shift² J`.  This is the
   diagonal-`M` / shift-`L` representation whose q-Weyl relation is
   `QuantumTorus.funcModel_qWeyl` (`L·M = q·M·L`); `act2` is additive
   (`act2_add`).  (The bijective `torusEval`-into-`AddMonoid.End` ring
   homomorphism is mathematically the same object but is elaboration-intractable
   over `AddMonoid.End (ℤ → K)` — the concrete `liftNCRingHom` instance blows the
   `isDefEq` budget; `act2` is the tractable equivalent for the order-2 elements
   at hand, and is faithful on them since they are supported in degrees `{0,1,2}`.)
2. **GGM lives in the torus (a theorem).**  The order-2 figure-eight annihilator
   is the torus element `ggmElement`, whose `L^j` coefficient is **exactly**
   `figureEightOperator.coeff j` (`coeffAt_ggmElement`), and under `act2` it
   reproduces the **exact** concrete `figureEightOperator` action
   `∑_{j≤2} coeff_j(q, q^N)·J(N+j)` (`act2_ggmElement_matches_figureEight`).
   So "the GGM/AJ operator is an element of the quantum torus" is machine-checked,
   not a slogan.
3. **The C1 binding kernel lives in the SAME torus.**  The proved q-lift kernel
   `[m+2]_q σ² − σ − 1` is the torus element `c1Element`, acting as
   `act2 (c1Element c) b m = c m · b(m+2) − b(m+1) − b(m)`
   (`act2_c1Element`); with `c m = [m+2]_q` this is the operator form of
   `qlift_normalized_kernel_exists`.

Both `ggmElement` and `c1Element` are elements of the **one** ring
`QuantumTorus (ℤ → K)` (`act2_ggm_add_c1`, a non-vacuous witness: the algebraic
sum only typechecks because they are co-resident, and its action is the explicit
combined operator).  The proved five-route module distinction — Newton-polygon
slopes `{½,½}` (C1) vs `{−1,+1}` (GGM) — is therefore a statement about **two
concrete elements of a common q-difference ring**.  The inequivalence itself is
*not* proved here (it needs Ramis–Sauloy–Zhang Newton-polygon theory, outside
Mathlib); see
[`docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md`](../../../../../../docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md).
This file only makes the two kernels **co-resident** and pins the GGM action
compatibility — pure infrastructure, no module-theoretic claim.

## Base ring (§7c)

Generic `{K : Type*} [Field K]` throughout (inverses appear only through
`q`-powers and the `field`-valued coefficients); no `ℝ`, no ordering, no
archimedean construct.  The diagonal action and the evaluation are algebraic.

  -- Ref: [nguyen-tran-2021] strong AJ for 4₁;
  --      [leitner2026] mass-theory, prop:binding-genfun-qdifference;
  --      docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md
-/

noncomputable section

namespace QOU.Machinery.QuantumTorusAJ

open SkewMonoidAlgebra
open QOU.Machinery.QuantumTorus

-- The colored-Jones / binding towers this file evaluates on; field-generic.
variable {K : Type*} [Field K]

/-! ### The coefficient ring: diagonal M-operators `A = ℤ → K` with the σ-twist -/

/-- **The σ-twist as translation.**  The M-coefficient ring `A = ℤ → K` (a
    colour-indexed diagonal operator) carries the L-degree group `Multiplicative
    ℤ` acting by the shift `(ofAdd k) • a = fun N => a (N + k)`.  This is the
    paper's `σ(M) = c·M` realised on `M = q^N`: `σ(q^{·})(N) = q^{N+1} = q·q^N`,
    i.e. `c = q`.  A genuine `MulSemiringAction` (ring-automorphism action), so
    `QuantumTorus (ℤ → K)` is the skew-Laurent ring on this coefficient ring. -/
instance instTransAction : MulSemiringAction (Multiplicative ℤ) (ℤ → K) where
  smul g a := fun N => a (N + Multiplicative.toAdd g)
  one_smul a := by
    funext N; show a (N + Multiplicative.toAdd (1 : Multiplicative ℤ)) = a N; congr 1; simp
  mul_smul g h a := by
    funext N
    show a (N + Multiplicative.toAdd (g * h))
        = a (N + Multiplicative.toAdd g + Multiplicative.toAdd h)
    rw [show Multiplicative.toAdd (g * h)
        = Multiplicative.toAdd g + Multiplicative.toAdd h from rfl]
    congr 1; ring
  smul_zero g := by funext N; rfl
  smul_add g a b := by funext N; rfl
  smul_one g := by funext N; rfl
  smul_mul g a b := by funext N; rfl

@[simp] theorem trans_smul_apply (y : Multiplicative ℤ) (a : ℤ → K) (N : ℤ) :
    (y • a) N = a (N + Multiplicative.toAdd y) := rfl

/-- `σ` on the diagonal coefficient ring is the unit forward shift — the
    operator-level face of `L`'s q-Weyl action (`QuantumTorus.funcModel_qWeyl`,
    `L·M = q·M·L`). -/
theorem sigma_diag (a : ℤ → K) : sigma a = fun N => a (N + 1) := by
  funext N
  show a (N + Multiplicative.toAdd (Multiplicative.ofAdd (1 : ℤ))) = a (N + 1)
  simp

/-! ### The order-≤2 function-model action `act2` -/

/-- Coefficient reading is additive: `coeffAt (f + g) = coeffAt f + coeffAt g`. -/
@[simp] theorem coeffAt_add (f g : QuantumTorus (ℤ → K)) (n : ℤ) :
    coeffAt (f + g) n = coeffAt f n + coeffAt g n := by
  simp [coeffAt, coeff_add]

/-- **The order-≤2 function-model action.**  A torus element `f` acts on a colour
    tower `J : ℤ → K` as the q-difference operator whose `L^j`-coefficient is the
    diagonal `coeffAt f j` (`j = 0,1,2`): `L` shifts, `coeffAt f j` scales.  For
    an element supported in degrees `{0,1,2}` (every operator in this file) this
    is its full action; the corresponding q-Weyl relation for the `L, M`
    generators is `QuantumTorus.funcModel_qWeyl`. -/
def act2 (f : QuantumTorus (ℤ → K)) (J : ℤ → K) (N : ℤ) : K :=
  coeffAt f 0 N * J (N + 0) + coeffAt f 1 N * J (N + 1) + coeffAt f 2 N * J (N + 2)

/-- `act2` is additive in the torus element (it is a coefficient-linear
    readout). -/
theorem act2_add (f g : QuantumTorus (ℤ → K)) (J : ℤ → K) (N : ℤ) :
    act2 (f + g) J N = act2 f J N + act2 g J N := by
  simp only [act2, coeffAt_add, Pi.add_apply]; ring

/-! ### 1. The GGM/AJ figure-eight annihilator as a torus element -/

/-- **The order-2 GGM/AJ operator as a torus element.**  `ggmElement a0 a1 a2 =
    a0 + a1·L + a2·L²` in `QuantumTorus (ℤ → K)` — the abstract shape of the
    figure-eight annihilator (`AJFigureEight.figureEightOperator`, order 2). -/
def ggmElement (a0 a1 a2 : ℤ → K) : QuantumTorus (ℤ → K) :=
  monomial 0 a0 + monomial 1 a1 + monomial 2 a2

/-- The torus element carries **exactly** the three operator coefficients:
    `coeffAt (ggmElement a0 a1 a2) j = a_j` for `j = 0,1,2`. -/
theorem coeffAt_ggmElement (a0 a1 a2 : ℤ → K) :
    coeffAt (ggmElement a0 a1 a2) 0 = a0
      ∧ coeffAt (ggmElement a0 a1 a2) 1 = a1
      ∧ coeffAt (ggmElement a0 a1 a2) 2 = a2 := by
  refine ⟨?_, ?_, ?_⟩ <;>
    · funext N
      simp only [ggmElement, coeffAt_add, coeffAt_monomial, Pi.add_apply]
      norm_num

/-- The GGM torus element acts as the order-2 difference operator
    `a0 N · J N + a1 N · J(N+1) + a2 N · J(N+2)`. -/
theorem act2_ggmElement (a0 a1 a2 J : ℤ → K) (N : ℤ) :
    act2 (ggmElement a0 a1 a2) J N
      = a0 N * J (N + 0) + a1 N * J (N + 1) + a2 N * J (N + 2) := by
  simp only [ggmElement, act2, coeffAt_add, coeffAt_monomial, Pi.add_apply]
  norm_num

/-- **GGM lives in the torus (compatibility theorem).**  The torus element
    carrying the figure-eight coefficient functions maps under `act2` to the
    **exact** action of the concrete `figureEightOperator`
    (`∑_{j≤2} coeff_j(q, q^N)·J(N+j)`).  So the sorry-free GGM/AJ annihilator of
    `QOU.BraidKnot.AJFigureEight` is genuinely an element of the abstract
    quantum torus, and `act2` realises it. -/
theorem act2_ggmElement_matches_figureEight (q : K) (J : ℤ → K) (N : ℤ) :
    act2 (ggmElement
          (fun M => (QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).coeff 0 q (q ^ M))
          (fun M => (QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).coeff 1 q (q ^ M))
          (fun M => (QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).coeff 2 q (q ^ M)))
        J N
      = ∑ j ∈ Finset.range ((QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).order + 1),
          (QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).coeff j q (q ^ N) * J (N + j) := by
  rw [act2_ggmElement]
  show _ = ∑ j ∈ Finset.range (2 + 1),
      (QOU.BraidKnot.AJFigureEight.figureEightOperator (K := K)).coeff j q (q ^ N) * J (N + j)
  rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ,
      Finset.sum_range_zero]
  push_cast
  ring

/-! ### 2. The binding q-lift kernel `[m+2]_q σ² − σ − 1` in the SAME torus -/

/-- **The C1 binding q-lift kernel as a torus element.**  With coefficient
    function `c : ℤ → K` (canonically `c m = [m+2]_q`, `c1Coeff`),
    `c1Element c = c·L² − L − 1` in the **same** `QuantumTorus (ℤ → K)` (written
    with negated constant coefficients so only `+` is needed).  For `c m =
    [m+2]_q` this is the operator form of the proved kernel
    `[m+2]_q · b_{m+2} = b_{m+1} + b_m`
    (`QOU.Mass.QDifferenceConfluentObstruction.qlift_normalized_kernel_exists`),
    whose Newton-polygon slopes at ∞ are the pure-isoclinic `{½,½}` — disjoint
    from the GGM/AJ carrier's `{−1,+1}` (five independent routes; see
    `docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md`).  That module
    inequivalence is **not** proved here (Ramis–Sauloy–Zhang Newton-polygon
    theory, outside Mathlib); this element only makes C1 **co-resident** with
    `ggmElement` so the distinction becomes a statement about two concrete
    elements of one ring. -/
def c1Element (c : ℤ → K) : QuantumTorus (ℤ → K) :=
  monomial 2 c + monomial 1 (-1) + monomial 0 (-1)

/-- The C1 kernel torus element acts as `[m+2]_q σ² − σ − 1`:
    `act2 (c1Element c) b m = c m · b(m+2) − b(m+1) − b(m)`. -/
theorem act2_c1Element (c b : ℤ → K) (m : ℤ) :
    act2 (c1Element c) b m = c m * b (m + 2) - b (m + 1) - b (m + 0) := by
  simp only [c1Element, act2, coeffAt_add, coeffAt_monomial, Pi.add_apply]
  norm_num
  ring

/-- The canonical C1 coefficient `c m = [m+2]_q` (the q-integer of the shifted
    colour), matching `qlift_normalized_kernel_exists`'s `[n+2]_q` factor.  For
    `m ≥ 0` this is `QOU.Mass.QDifferenceConfluentObstruction.qint q (m+2)`. -/
def c1Coeff (q : K) : ℤ → K := fun m =>
  QOU.Mass.QDifferenceConfluentObstruction.qint q (m + 2).toNat

/-! ### Co-residence: both kernels are elements of the one quantum torus -/

/-- **Co-residence (the point of this file), operationally.**  Because
    `ggmElement …` and `c1Element …` are elements of the **same** ring
    `QuantumTorus (ℤ → K)`, their sum is again a torus element, and its `act2`
    action is the concrete order-2 operator obtained by adding the two kernels
    coefficient-by-coefficient: `((a0−1) + (a1−1)L + (a2+c)L²)`.  This is a
    non-vacuous witness that the two kernels live in one q-difference ring — the
    algebraic sum only typechecks because of co-residence, and the result is an
    explicit operator.  The proved five-route module distinction (slopes `{½,½}`
    (C1) vs `{−1,+1}` (GGM),
    `docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md`) is therefore a
    statement comparing these two concrete elements of the common ring; the
    inequivalence itself is not formalised here (Newton-polygon theory, outside
    Mathlib). -/
theorem act2_ggm_add_c1 (a0 a1 a2 c J : ℤ → K) (N : ℤ) :
    act2 (ggmElement a0 a1 a2 + c1Element c) J N
      = (a0 N - 1) * J (N + 0) + (a1 N - 1) * J (N + 1) + (a2 N + c N) * J (N + 2) := by
  rw [act2_add, act2_ggmElement, act2_c1Element]
  ring

end QOU.Machinery.QuantumTorusAJ
