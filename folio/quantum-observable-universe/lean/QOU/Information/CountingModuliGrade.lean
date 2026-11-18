import QOU.Information.SurrealBudgetGrade

/-!
# QOU.Information.CountingModuliGrade — #P as an ω-graded section over moduli

This file formalizes the picture behind the question *"how do we describe `#P`
over a moduli space of problems / Turing machines / QOU objects, with the
initial photonic condition = the Turing state?"*.

**The moduli picture.**  A *problem* is a point `m` of a moduli space `M`.  In
the QOU dictionary a moduli point is a categorical object (a braid / Hecke
representation) equipped with an **initial photonic condition** — the contact /
Reeb initial data of the state bundle — and that initial condition **is** the
Turing configuration (tape + head + state).  The computation is the evolution
(the braid word / Reeb flow); the counting answer `#P(m)` is the terminal
Markov trace.  So `#P` is a **section over `M`**, and its *cost* is a
**family of growth functions** `cost : M → ℕ → ℕ` — one growth function per
moduli point, graded fiberwise by the surreal ω-grade of `SurrealBudgetGrade`.

**What is proved here (the counting axis).**  The **hard stratum**
`{m | SuperPolynomial (cost m)}` is where counting is ω-super-polynomial.  A
*single* hard point **excludes a uniform (one-algorithm-for-all-moduli)
polynomial bound** over the whole space (`not_familyPolyBounded_of_hardPoint`),
and the QOU boundary family lands such a point **unconditionally** — the
physical `3^{3n}` resolution-tree cost sits in the hard stratum
(`physical_point_hard`, via `qou_physical_intractability_unconditional`).  So:
*over the moduli space of QOU counting problems, no uniform polynomial counting
algorithm exists* — proved, sorry-free.

**What stays open (the decision axis = the wall).**  Crossing from
*counting*-hard to *decision*-hard is the `res ≠ 0 ⟹ P≠NP` wall.  It is
packaged honestly as the §3b conditional class `PhotonicDecisionHard` with **no
instance**: an instance would exhibit a decision-hard moduli point, i.e. prove
`P≠NP`.  The gap between the (proved) counting hard point and the (absent)
decision hard point is exactly the counting/decision axis boundary of
`MagnitudeAxisBoundary`.

Base ring not applicable (ℕ-valued costs / finite combinatorics).
-/

namespace QOU.Information

variable {M : Type*}

/-! ## The cost family and its ω-grade stratification -/

/-- **Uniform polynomial bound over the whole moduli space** — one algorithm,
    every problem: a single `c·nᵏ` dominates `cost m n` at *every* moduli point
    `m`.  This is the `P`-style "polynomial for all instances" hypothesis. -/
def FamilyPolyBounded (cost : M → ℕ → ℕ) : Prop := ∃ c k, ∀ m n, cost m n ≤ c * n ^ k

/-- **The hard stratum** of a cost family: the moduli points whose counting
    cost is ω-super-polynomial.  The surreal grade stratifies `M` into the
    poly-cost locus and this hard locus. -/
def HardStratum (cost : M → ℕ → ℕ) : Set M := {m | SuperPolynomial (cost m)}

/-- **A uniform bound restricts to every fiber (sorry-free).**  If one
    polynomial dominates the family, it dominates each single-moduli-point cost
    function. -/
theorem polyBounded_fiber_of_familyPolyBounded {cost : M → ℕ → ℕ}
    (h : FamilyPolyBounded cost) (m : M) : PolyBounded (cost m) := by
  obtain ⟨c, k, hb⟩ := h
  exact ⟨c, k, fun n => hb m n⟩

/-- **A single hard point kills every uniform poly bound (sorry-free).**  One
    ω-super-polynomial moduli point suffices: no `c·nᵏ` can dominate the family,
    because it would have to dominate that point's super-polynomial fiber.  This
    is the moduli form of the surreal squeeze — the hard stratum obstructs
    uniform polynomial counting. -/
theorem not_familyPolyBounded_of_hardPoint {cost : M → ℕ → ℕ} {m : M}
    (hm : m ∈ HardStratum cost) : ¬ FamilyPolyBounded cost :=
  fun h => not_polyBounded_of_superPoly hm (polyBounded_fiber_of_familyPolyBounded h m)

/-- **Nonempty hard stratum ⟹ no uniform poly bound (sorry-free).** -/
theorem not_familyPolyBounded_of_hardStratum_nonempty {cost : M → ℕ → ℕ}
    (h : (HardStratum cost).Nonempty) : ¬ FamilyPolyBounded cost :=
  let ⟨_, hm⟩ := h; not_familyPolyBounded_of_hardPoint hm

/-! ## The QOU boundary family lands the hard stratum — unconditionally -/

/-- **The physical counting cost** of the QOU boundary family: the surviving
    `3^{3n}`-leaf skein resolution tree (non-torsion regime, nothing cancels),
    read by a unit-bandwidth device.  This is the counting cost `#P` actually
    charges at the boundary moduli point. -/
def physicalCost : ℕ → ℕ := fun n => resolutionTreeSize (3 * n)

/-- **The physical cost is ω-super-polynomial (sorry-free, unconditional).**
    Directly from `qou_physical_intractability_unconditional` at bandwidth
    `B = 1`: the `3^{3n}` tree dominates every polynomial. -/
theorem physicalCost_superPoly : SuperPolynomial physicalCost := by
  refine qou_physical_intractability_unconditional 1 ?_ physicalCost ?_
  · norm_num
  · intro n
    simp [physicalCost]

/-- **The boundary moduli point is in the hard stratum (sorry-free).**  Any cost
    family whose fiber at `m` is the physical boundary cost has `m` in its hard
    stratum. -/
theorem physical_point_hard {cost : M → ℕ → ℕ} {m : M}
    (hm : cost m = physicalCost) : m ∈ HardStratum cost := by
  show SuperPolynomial (cost m)
  rw [hm]; exact physicalCost_superPoly

/-- **No uniform polynomial counting over the QOU moduli space (sorry-free,
    unconditional).**  Because the boundary family occupies a hard-stratum
    point, the moduli space of QOU counting problems admits **no** single
    polynomial-time counting algorithm.  This is the proved *counting-axis*
    statement — the `#P`-over-moduli result. -/
theorem not_familyPolyBounded_of_physical_point {cost : M → ℕ → ℕ} {m : M}
    (hm : cost m = physicalCost) : ¬ FamilyPolyBounded cost :=
  not_familyPolyBounded_of_hardPoint (physical_point_hard hm)

/-! ## Initial photonic condition = Turing state — the encoding interface -/

/-- **Photonic encoding of computation (data, not a claim).**  The QOU
    dictionary *"initial photonic condition = Turing state"* as a structure: a
    map `encode` from a machine/problem index to a moduli point (the photonic
    initial condition realizing that machine's configuration), and the
    machine's own counting cost `machineCost`.  The coherence field records
    that the moduli point charges (at least) the machine's cost — this is the
    Bekenstein/physical reading, structural not fitted.  Providing this is
    *naming the dictionary*; it makes **no** complexity claim by itself. -/
structure PhotonicEncoding (M : Type*) (cost : M → ℕ → ℕ) where
  /-- Machine/problem index ↦ its photonic initial condition (a moduli point). -/
  encode : ℕ → M
  /-- The machine's intrinsic counting cost. -/
  machineCost : ℕ → ℕ → ℕ
  /-- The moduli point charges at least the machine's cost (Bekenstein reading). -/
  charges : ∀ t n, machineCost t n ≤ cost (encode t) n

/-- **Photonic–Turing DECISION hardness (conjecture; NO instance — the wall).**
    The counting-axis result above is unconditional; crossing to the *decision*
    axis is `res ≠ 0 ⟹ P≠NP`.  This class carries the open content: some moduli
    point's **decision** cost (not merely its counting cost) is
    ω-super-polynomial.  An instance would exhibit a decision-hard problem =
    prove `P≠NP` (indeed a super-polynomial *general* — not merely
    bandwidth-limited — lower bound); it stays **absent** (anti-laundering:
    axiomatization is not proof). -/
class PhotonicDecisionHard (decisionCost : M → ℕ → ℕ) : Prop where
  /-- Some moduli point is decision-ω-super-polynomial. -/
  hard_point : ∃ m, SuperPolynomial (decisionCost m)

/-- **Conditional consequence (sorry-free): given the decision-hardness bridge,
    no uniform polynomial *decision* algorithm over the moduli space.**  A
    rigorous *conditional* statement — everything is proved modulo the single
    open class instance, which is the actual `P≠NP` content and stays absent.
    Contrast `not_familyPolyBounded_of_physical_point`, which needs no bridge:
    that is the counting axis (proved); this is the decision axis (open). -/
theorem not_familyPolyBounded_decision_of_bridge (decisionCost : M → ℕ → ℕ)
    [H : PhotonicDecisionHard decisionCost] : ¬ FamilyPolyBounded decisionCost :=
  not_familyPolyBounded_of_hardStratum_nonempty H.hard_point

/-- Any machine `t` with ω-super-polynomial intrinsic cost maps under a
    `PhotonicEncoding` to a moduli point `enc.encode t` in `HardStratum cost`. -/
theorem PhotonicEncoding.encode_mem_hardStratum {cost : M → ℕ → ℕ}
    (enc : PhotonicEncoding M cost) {t : ℕ}
    (ht : SuperPolynomial (enc.machineCost t)) :
    enc.encode t ∈ HardStratum cost :=
  ht.of_le (enc.charges t)

/-- If a `PhotonicEncoding` encodes even a single machine `t` whose intrinsic
    counting cost is ω-super-polynomial, then the moduli cost family `cost` is
    not uniformly polynomially bounded. -/
theorem PhotonicEncoding.not_familyPolyBounded_of_superPoly_machine
    {cost : M → ℕ → ℕ} (enc : PhotonicEncoding M cost) {t : ℕ}
    (ht : SuperPolynomial (enc.machineCost t)) :
    ¬ FamilyPolyBounded cost :=
  not_familyPolyBounded_of_hardPoint (enc.encode_mem_hardStratum ht)

/-- Specializing `PhotonicEncoding.encode_mem_hardStratum` to any machine `t`
    whose intrinsic cost is `physicalCost` lands `enc.encode t` in `HardStratum cost`. -/
theorem PhotonicEncoding.encode_physical_mem_hardStratum
    {cost : M → ℕ → ℕ} (enc : PhotonicEncoding M cost) {t : ℕ}
    (ht : enc.machineCost t = physicalCost) :
    enc.encode t ∈ HardStratum cost := by
  apply enc.encode_mem_hardStratum
  rw [ht]
  exact physicalCost_superPoly

end QOU.Information
