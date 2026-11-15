import QOU.Machinery.QuantumTorusAJ
import QOU.BraidKnot.AJFigureEightAnnihilation

/-!
# QOU.Machinery.AJTorusAnnihilation — the GGM/AJ operator annihilates the 4₁ tower as a torus element

**Discharging the `aj_mem` transfer input of NT-T4 `TransferLemmas`, honestly.**

Bean `qou-aap2` (TL-aj_mem).  The `aj_mem` field of
`QOU.Machinery.StrongAJFigureEight.TransferLemmas` asks for `Â ∈ I` — the AJ
operator lies in the recurrence (annihilator) ideal `A_{4₁} = { P | P·J = 0 }`.
This file supplies the **concrete torus-level annihilation** that field encodes,
using the two just-landed corpus objects:

* the quantum-torus wiring `QOU.Machinery.QuantumTorusAJ` (`ggmElement`, `act2`,
  `act2_ggmElement`, `coeffAt_add`), and
* the corpus-PROVED `figureEightOperator_annihilates`
  (`QOU.BraidKnot.AJFigureEightAnnihilation`, division-free qZeilberger
  telescope, every `q ≠ 0`).

## The honest subtlety — the corpus operator is INHOMOGENEOUS

`figureEightOperator` is the *inhomogeneous* order-2 annihilator: it sends the
tower to `feRhs`, **not** to `0` (`figureEightOperator_annihilates` proves
`∑_{j≤2} feCoeff_j(q,q^N)·J(N+j) = feRhs(q,q^N)`, and `feRhs ≠ 0`).  So the
naive `ggmElement` carrying the figure-eight coefficients is **not** a member of
the strict annihilator ideal `{P | P·J = 0}` — it lands on `feRhs`.  This is
recorded honestly:

1. **`act2_ggmElement_inhom` (residence, `= feRhs`).**  The order-2 torus element
   `ggmElement (feCoeff 0) (feCoeff 1) (feCoeff 2)` acts on the tower `J41` as
   the corpus inhomogeneous operator: `act2 … J41 (M) = feRhs(q,q^M)` for every
   colour `M : ℕ`.  A genuine composition of `act2_ggmElement` with the summed
   annihilation lemma — it establishes co-residence, but the value is `feRhs`,
   not `0`.

2. **`ajHomElement_annihilates` (the real `aj_mem`, `= 0`).**  The *homogenised*
   order-3 torus element `Â_hom = (L − ρ)·P_FE`, realised concretely as
   `ajHomElement` with coefficients
   `c₀ = b(N+1)a₀(N)`, `c₁ = b(N+1)a₁(N) − b(N)a₀(N+1)`,
   `c₂ = b(N+1)a₂(N) − b(N)a₁(N+1)`, `c₃ = −b(N)a₂(N+1)`
   (where `b(N) = feRhs(q,q^N)`, `aⱼ(N) = feCoeff_j(q,q^N)`), annihilates the
   tower to **`0`**: `act3 ajHomElement J41 (M) = 0` for every `M : ℕ`.  The
   proof is `act3 Â_hom J = b(N+1)·(P_FE·J)(N) − b(N)·(P_FE·J)(N+1)
   = b(N+1)·b(N) − b(N)·b(N+1) = 0`, two instances of the corpus annihilation.
   This is the genuine "GGM/AJ operator annihilates the 4₁ tower as an element of
   the quantum torus", sorry-free.

## What the capstone `strong_aj_figure_eight_of_transfer` still needs

The `TransferLemmas.aj_mem` field is `Aop ∈ I` for an **abstract** left ideal
`I : Ideal (QuantumTorus A)`.  This file proves the **function-model** annihilation
`act3 ajHomElement J41 = 0` — the concrete content of "`ajHomElement` lies in the
annihilator ideal".  The remaining bridge to `Aop ∈ I` needs the ideal `I` to be
*defined* as the genuine left-annihilator submodule and `act` to be a genuine
torus **module action** (a ring homomorphism `QuantumTorus (ℤ→K) → AddMonoid.End
(ℤ→K)`).  Per `QuantumTorusAJ`, that full `torusEval`-into-`AddMonoid.End` map is
elaboration-intractable in Mathlib 4.24 (`act2`/`act3` are the tractable
order-bounded readouts, faithful only on low-order elements, not closed under the
ring product).  So the capstone still needs, to *use* this result:

* an executable definition of `I` as `{ P | act P J41 = 0 }` for a total action
  `act` (or the `AddMonoid.End` ring-hom), and
* the membership bridge `act3 ajHomElement J41 = 0 → ajHomElement ∈ I`.

Both are module-structure work orthogonal to this file's annihilation, which is
the concrete numerical fact those hypotheses quantify over.  This file does **not**
provide a `TransferLemmas` instance (the honest "primary open" state per the
anti-laundering rule).

## Base ring (§7c)

`{K : Type*} [Field K]` throughout (the tower needs `q⁻¹`); no `ℝ`, no ordering,
no archimedean construct.  The colour index bridges ℤ (torus degree) ↔ ℕ (tower)
by `Int.toNat` at nonnegative colours.

  -- Ref: [nguyen-tran-2021] Theorem 1, transfer input aj_mem;
  --      QOU.BraidKnot.AJFigureEightAnnihilation.figureEightOperator_annihilates;
  --      docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md
-/

noncomputable section

namespace QOU.Machinery.AJTorusAnnihilation

open QOU.Machinery.QuantumTorus
open QOU.Machinery.QuantumTorusAJ
open QOU.BraidKnot.AJFigureEight
open QOU.BraidKnot.HabiroNewtonLadder

variable {K : Type*} [Field K]

/-! ### Colour bridge ℤ ↔ ℕ: tower and coefficient functions on the torus degree -/

/-- The colored-Jones tower of `4₁` as a ℤ-indexed function (torus degree),
    agreeing with `coloredJones41 q` at nonnegative colours. -/
def J41 (q : K) : ℤ → K := fun N => coloredJones41 q N.toNat

/-- The `j`-th figure-eight coefficient as a ℤ→K function of the torus degree:
    `aⱼ(N) = feCoeff j q (q^N)` at nonnegative `N`. -/
def aFn (q : K) (j : ℕ) : ℤ → K := fun N => feCoeff j q (q ^ N.toNat)

/-- The inhomogeneous right-hand side as a ℤ→K function: `b(N) = feRhs(q,q^N)`. -/
def bFn (q : K) : ℤ → K := fun N => feRhs q (q ^ N.toNat)

/-! ### The order-≤3 function-model action `act3` (extends `act2`) -/

/-- **The order-≤3 function-model action.**  A torus element `f` acts on a colour
    tower `J : ℤ → K` as the q-difference operator whose `L^j`-coefficient is the
    diagonal `coeffAt f j` (`j = 0,1,2,3`).  For an element supported in degrees
    `{0,1,2,3}` this is its full action; it extends `QuantumTorusAJ.act2` by one
    shift, exactly as the homogenisation `(L − ρ)·P_FE` raises the order by one. -/
def act3 (f : QuantumTorus (ℤ → K)) (J : ℤ → K) (N : ℤ) : K :=
  coeffAt f 0 N * J N + coeffAt f 1 N * J (N + 1)
    + coeffAt f 2 N * J (N + 2) + coeffAt f 3 N * J (N + 3)

/-- **The order-3 homogeneous torus element** `c₀ + c₁L + c₂L² + c₃L³` in the
    same `QuantumTorus (ℤ → K)` as `ggmElement`. -/
def homElement (c0 c1 c2 c3 : ℤ → K) : QuantumTorus (ℤ → K) :=
  monomial 0 c0 + monomial 1 c1 + monomial 2 c2 + monomial 3 c3

/-- The order-3 element acts as the order-3 difference operator
    `c₀ N·J N + c₁ N·J(N+1) + c₂ N·J(N+2) + c₃ N·J(N+3)`. -/
theorem act3_homElement (c0 c1 c2 c3 J : ℤ → K) (N : ℤ) :
    act3 (homElement c0 c1 c2 c3) J N
      = c0 N * J N + c1 N * J (N + 1) + c2 N * J (N + 2) + c3 N * J (N + 3) := by
  simp only [homElement, act3, coeffAt_add, coeffAt_monomial, Pi.add_apply]
  norm_num

/-! ### The corpus annihilation, expanded to a clean 3-term ℕ identity -/

/-- **The corpus annihilation as a flat 3-term identity** (unfolding the summed
    `figureEightOperator_annihilates`): at every colour `n`,
    `feCoeff 0·J(n) + feCoeff 1·J(n+1) + feCoeff 2·J(n+2) = feRhs(q,q^n)`. -/
theorem annih {q : K} (hq : q ≠ 0) (n : ℕ) :
    feCoeff 0 q (q ^ n) * coloredJones41 q n
      + feCoeff 1 q (q ^ n) * coloredJones41 q (n + 1)
      + feCoeff 2 q (q ^ n) * coloredJones41 q (n + 2)
      = feRhs q (q ^ n) := by
  have h := figureEightOperator_annihilates (K := K) hq n
  simpa [Annihilates, figureEightOperator, Finset.sum_range_succ,
    Finset.sum_range_zero] using h

/-! ### 1. Residence: `ggmElement` acts as the inhomogeneous corpus operator (`= feRhs`) -/

/-- **Residence (honest, `= feRhs`).**  The order-2 torus element carrying the
    figure-eight coefficients acts on the tower `J41` as the corpus *inhomogeneous*
    operator — its value at colour `M` is `feRhs(q,q^M)`, **not** `0`.  So this
    `ggmElement` is co-resident with the C1 kernel in `QuantumTorus (ℤ→K)`, but it
    is *not* in the strict annihilator ideal; the homogenisation below is. -/
theorem act2_ggmElement_inhom {q : K} (hq : q ≠ 0) (M : ℕ) :
    act2 (ggmElement (aFn q 0) (aFn q 1) (aFn q 2)) (J41 q) (M : ℤ)
      = feRhs q (q ^ M) := by
  have hM0 : ((M : ℤ)).toNat = M := by omega
  have hM1 : ((M : ℤ) + 1).toNat = M + 1 := by omega
  have hM2 : ((M : ℤ) + 2).toNat = M + 2 := by omega
  rw [act2_ggmElement]
  simp only [aFn, J41, add_zero]
  rw [hM0, hM1, hM2]
  exact annih hq M

/-! ### 2. The homogenised order-3 operator annihilates the tower to `0` (the real `aj_mem`) -/

/-- The order-3 homogeneous coefficients `c₀,c₁,c₂,c₃` of `Â_hom = (L − ρ)·P_FE`. -/
def hc0 (q : K) : ℤ → K := fun N => bFn q (N + 1) * aFn q 0 N
def hc1 (q : K) : ℤ → K := fun N => bFn q (N + 1) * aFn q 1 N - bFn q N * aFn q 0 (N + 1)
def hc2 (q : K) : ℤ → K := fun N => bFn q (N + 1) * aFn q 2 N - bFn q N * aFn q 1 (N + 1)
def hc3 (q : K) : ℤ → K := fun N => -(bFn q N * aFn q 2 (N + 1))

/-- **The homogenised order-3 AJ operator as a torus element.**  `Â_hom =
    c₀ + c₁L + c₂L² + c₃L³ ∈ QuantumTorus (ℤ→K)` — the order-raised
    homogenisation `(L − ρ)·P_FE` of the corpus inhomogeneous operator, with `ρ`
    the shift ratio `b(N+1)/b(N)` cleared into the coefficients. -/
def ajHomElement (q : K) : QuantumTorus (ℤ → K) :=
  homElement (hc0 q) (hc1 q) (hc2 q) (hc3 q)

/-- **The GGM/AJ operator annihilates the 4₁ colored-Jones tower as a torus
    element (sorry-free) — the concrete content of `aj_mem`.**  The homogenised
    order-3 element `ajHomElement` sends the tower `J41` to `0` at every colour:
    `act3 ajHomElement J41 (M) = 0`.

    Proof: `act3 Â_hom J = b(N+1)·(P_FE·J)(N) − b(N)·(P_FE·J)(N+1)` and each
    `(P_FE·J)` is the corpus `feRhs` (`annih`), so the two `feRhs` products
    cancel.  This is `Â_hom ∈ { P | P·J = 0 }` at the function-model level. -/
theorem ajHomElement_annihilates {q : K} (hq : q ≠ 0) (M : ℕ) :
    act3 (ajHomElement q) (J41 q) (M : ℤ) = 0 := by
  have hM0 : ((M : ℤ)).toNat = M := by omega
  have hM1 : ((M : ℤ) + 1).toNat = M + 1 := by omega
  have hM2 : ((M : ℤ) + 2).toNat = M + 2 := by omega
  have hM3 : ((M : ℤ) + 3).toNat = M + 3 := by omega
  have hSM := annih hq M
  have hSM1 := annih hq (M + 1)
  rw [show M + 1 + 1 = M + 2 from rfl, show M + 1 + 2 = M + 3 from rfl] at hSM1
  rw [ajHomElement, act3_homElement]
  simp only [hc0, hc1, hc2, hc3, bFn, aFn, J41]
  rw [hM0, hM1, hM2, hM3]
  linear_combination (feRhs q (q ^ (M + 1))) * hSM - (feRhs q (q ^ M)) * hSM1

end QOU.Machinery.AJTorusAnnihilation
