import QOU.Machinery.AJTorusAnnihilation

/-!
# QOU.Machinery.AJMinimality — the honest formalizable fragment of NT-T4 `minimality`

**Bean `qou-jshd` (TL-minimality).**  The `minimality` field of
`QOU.Machinery.StrongAJFigureEight.TransferLemmas` asks that the order-3 AJ
operator `Â_hom` be the **minimal-order nonzero annihilator** of the `4₁`
colored-Jones tower, so that `principal_of_division_minimality` makes the
recurrence ideal principal (`I = span {Â_hom}`).  The Nguyen–Tran figure-eight
paper obtains this by CITING Tran's transfer machinery.  This file records what
is honestly formalizable now, and — in the companion audit
`docs/audits/2026-07-20-tl-minimality-wall.md` — what is a genuine wall.

**Note (2026-11-21).** `TransferLemmas.minimality` is now stated in L-length
(`lLength`), not `topDeg`: the `topDeg` form had no instance over a nontrivial
ring (`StrongAJFigureEight.Instances.topDeg_minimality_forces_zero`). The
`topDeg` facts below are still correct and still necessary, but "order" in the
class now means L-length, and `principal_of_measure lLength` replaces
`principal_of_division_minimality` as the composing lemma.

## What [Tr4] = arXiv:1404.0331 Lemmas 3.1–3.3 actually prove (honest reading)

Tran, "The strong AJ conjecture for cables of torus knots".  §3 (case `s` odd,
`q > 2`):

* **Lemma 3.1** — for the *torus* knot `T(p,q)`:
  `(L^{2m} − t^{-4pqm²}M^{-2pqm}) J_T ∈ R[M^{±1}]` for all `m > 0`.  A
  power-of-the-base annihilation: powers of the order-1 base recurrence still
  send `J_T` into the coefficient ring.
* **Proposition 3.2** — builds explicit σ-invariant operators `P₁, P₂` with
  `Pᵢ Gᵢ ∈ R[M^{±1}]` for the cable pieces `G₁, G₂`.
* Assembled with **Lemma 2.3** (an *existence*-of-annihilator construction) into
  an element `R ∈ A^σ_C` with `ε(R) = M^{k}L^{l}(A_C)^{2k}`, which feeds
  **Lemma 2.2** (`∃ P ∈ A^σ with ε(P) = M^kL^l A^{2m} ⟹ p ⊂ √ε(A^σ)`).

**Two honest facts follow, both material to this bean:**

1. **[Tr4] L3.1–3.3 are an annihilator *construction* (existence), NOT a
   minimality theorem.**  They exhibit a specific (high-degree, non-minimal)
   σ-invariant element to feed the radical-inclusion Lemma 2.2.  Nowhere is any
   operator shown to be minimal-degree.  Tran's whole strong-AJ route works at
   the level of *radicals of σ-invariant ideals* (`√ε(A^σ_K) = p`); it never
   proves the recurrence ideal is **principal**.  Principality/minimality is the
   content of the *plain* AJ conjecture (Garoufalidis's recurrence polynomial =
   minimal-order generator), which Tran **assumes** as a hypothesis (Lemma 2.1:
   "Suppose the AJ conjecture holds for `K`").
2. **[Tr4] §3 is about *cables of torus knots*, not `4₁`.**  The figure eight is
   hyperbolic — neither a torus knot nor a cable of one — so these lemmas do not
   literally apply to it.  The figure-eight paper reuses the *method* (build a
   σ-invariant annihilator, feed Lemma 2.2), not these statements.

So `TransferLemmas.minimality` is **not discharged** by [Tr4] L3.1–3.3.  The
minimal-order-generator fact is the plain-AJ input, and its Lean-honest status is
a **wall** (needs the character-variety A-polynomial / holonomic-rank machinery,
absent from Mathlib 4.24 + corpus).  See the audit doc for the wall analysis.

## What IS formalizable now (sorry-free, this file)

Minimality of the order-3 operator among homogeneous annihilators is
`NoLowOrderHomogAnnihilator` below: no nonzero order-≤2 homogeneous operator
annihilates the tower.  Two genuine *ingredients* of it are corpus-provable and
proved here (they are NECESSARY, not sufficient — full minimality remains the
wall):

* **Order-exactness (`hc3_ne_zero`).**  The homogenised operator `ajHomElement`
  genuinely has order 3: its `L³` coefficient `hc3 = −feRhs·feCoeff₂` is nonzero
  at every colour where `feRhs` and the top figure-eight coefficient `feCoeff₂`
  are nonzero (the generic-`q` condition).  So `Â_hom` is not a disguised
  lower-order operator — `topDeg Â_hom = 3`, the reference degree minimality is
  stated against.
* **Order-2 obstruction (`figureEight_not_homogAnnihilator`).**  The order-2
  figure-eight coefficient triple `(feCoeff₀, feCoeff₁, feCoeff₂)` is **not** a
  homogeneous annihilator: it sends the tower to `feRhs ≠ 0`, not `0`.  This
  rules out exactly the naive order-2 candidate — the concrete reason the
  homogenisation to order 3 is forced.

The remaining `NoLowOrderHomogAnnihilator` (rule out *all* order-≤2 triples) is
the wall.  **No `TransferLemmas` instance is provided and `minimality` is not
axiomatised** — per the anti-laundering rule this is the honest "open" state.

## Base ring (§7c)

`{K : Type*} [Field K]` throughout (inherited from the tower's `q⁻¹`); no `ℝ`,
no ordering, no archimedean construct.

  -- Ref: [nguyen-tran-2021] Theorem 1, transfer input `minimality`;
  --      [Tr4] = arXiv:1404.0331 (Tran) Lemmas 2.1–2.3, 3.1, Prop 3.2;
  --      QOU.Machinery.AJTorusAnnihilation.ajHomElement_annihilates;
  --      docs/audits/2026-07-20-tl-minimality-wall.md
-/

noncomputable section

namespace QOU.Machinery.AJMinimality

open QOU.Machinery.QuantumTorus
open QOU.Machinery.QuantumTorusAJ
open QOU.Machinery.AJTorusAnnihilation
open QOU.BraidKnot.AJFigureEight

variable {K : Type*} [Field K]

/-! ### 1. Order-exactness: the `L³` leading coefficient of `Â_hom` is nonzero -/

/-- The `L³` coefficient of the homogenised order-3 operator, evaluated at a
    nonnegative colour, is `−(feRhs·feCoeff₂)`. -/
theorem hc3_eq (q : K) (M : ℕ) :
    hc3 q (M : ℤ) = -(feRhs q (q ^ M) * feCoeff 2 q (q ^ (M + 1))) := by
  have hM0 : ((M : ℤ)).toNat = M := by omega
  have hM1 : ((M : ℤ) + 1).toNat = M + 1 := by omega
  simp only [hc3, bFn, aFn]
  rw [hM0, hM1]

/-- **`Â_hom` is genuinely order 3 — order-exactness (sorry-free).**  Wherever
    `feRhs` and the top figure-eight coefficient `feCoeff₂` are nonzero (the
    generic-`q` condition), the `L³` coefficient `hc3` of the homogenised
    operator is nonzero.  So `ajHomElement` is not a disguised order-≤2 operator;
    its `topDeg` is exactly 3, the reference degree the `minimality` field is
    stated against.  This is a NECESSARY ingredient of minimality, not the whole
    of it. -/
theorem hc3_ne_zero {q : K} (M : ℕ)
    (hb : feRhs q (q ^ M) ≠ 0) (ha2 : feCoeff 2 q (q ^ (M + 1)) ≠ 0) :
    hc3 q (M : ℤ) ≠ 0 := by
  rw [hc3_eq]
  exact neg_ne_zero.mpr (mul_ne_zero hb ha2)

/-- `hc3` is literally the `L³` coefficient of the torus element `ajHomElement`
    (`coeffAt … 3 = hc3`).  Combined with `hc3_ne_zero`, this witnesses
    `topDeg (ajHomElement q) = 3` at generic `q`. -/
theorem coeffAt_ajHomElement_three (q : K) :
    coeffAt (ajHomElement q) 3 = hc3 q := by
  funext N
  simp only [ajHomElement, homElement, coeffAt_add, coeffAt_monomial, Pi.add_apply]
  norm_num

/-! ### 2. The homogeneous-annihilator predicate and the order-2 obstruction -/

/-- An order-≤2 **homogeneous** annihilator of the `4₁` tower: coefficient
    functions `c₀,c₁,c₂ : ℤ→K` with
    `c₀(N)·J(N) + c₁(N)·J(N+1) + c₂(N)·J(N+2) = 0` at every colour. -/
def IsHomogAnnihilator (q : K) (c0 c1 c2 : ℤ → K) : Prop :=
  ∀ N : ℤ, c0 N * J41 q N + c1 N * J41 q (N + 1) + c2 N * J41 q (N + 2) = 0

/-- **Minimality of the order-3 operator among homogeneous annihilators.**  The
    sharp concrete statement that `minimality` reduces to: no *nonzero* order-≤2
    homogeneous operator annihilates the `4₁` tower.  This is the residual WALL —
    it needs the holonomic-rank / A-polynomial-degree fact absent from Mathlib +
    corpus.  It is stated here (as the honest reduction target), **never
    axiomatised**. -/
def NoLowOrderHomogAnnihilator (q : K) : Prop :=
  ∀ c0 c1 c2 : ℤ → K, IsHomogAnnihilator q c0 c1 c2 → c0 = 0 ∧ c1 = 0 ∧ c2 = 0

/-- **Order-2 obstruction (sorry-free).**  The order-2 figure-eight coefficient
    triple `(feCoeff₀, feCoeff₁, feCoeff₂)` is **not** a homogeneous annihilator:
    at any colour `M` where `feRhs q (q^M) ≠ 0` it sends the tower to
    `feRhs ≠ 0`, not `0`.  So the naive order-2 candidate — whose homogenisation
    is `Â_hom` — fails, which is the concrete reason order 3 is forced.  This
    rules out ONE triple; ruling out all of them is `NoLowOrderHomogAnnihilator`
    (the wall). -/
theorem figureEight_not_homogAnnihilator {q : K} {M : ℕ}
    (hq : q ≠ 0) (hb : feRhs q (q ^ M) ≠ 0) :
    ¬ IsHomogAnnihilator q (aFn q 0) (aFn q 1) (aFn q 2) := by
  intro h
  have hM := h (M : ℤ)
  have hact : act2 (ggmElement (aFn q 0) (aFn q 1) (aFn q 2)) (J41 q) (M : ℤ)
      = feRhs q (q ^ M) := act2_ggmElement_inhom hq M
  rw [act2_ggmElement] at hact
  simp only [add_zero] at hact hM
  rw [hM] at hact
  exact hb hact.symm

/-! ### 3. The reduction, stated honestly (no instance provided) -/

/-- **Minimality reduces to `NoLowOrderHomogAnnihilator` (sorry-free logical
    reduction).**  Given the sharp concrete statement `NoLowOrderHomogAnnihilator`
    (no nonzero order-≤2 homogeneous operator annihilates the tower), any
    homogeneous annihilator with a nonzero coefficient is impossible — i.e. the
    minimal homogeneous annihilation order is `> 2`.  Together with
    `ajHomElement_annihilates` (order-3 annihilation, corpus-proved) and
    `hc3_ne_zero` (order-exactness), this pins the minimal order at exactly 3.

    This lemma REDUCES the [Tr4]-cited `minimality` to the single sharp premise
    `NoLowOrderHomogAnnihilator q` — the smallest honest gap.  That premise is
    **not** provided here: it is the wall (see the audit doc). -/
theorem minimal_order_gt_two_of_noLowOrder {q : K}
    (hno : NoLowOrderHomogAnnihilator q)
    (c0 c1 c2 : ℤ → K) (hann : IsHomogAnnihilator q c0 c1 c2)
    (hne : ¬ (c0 = 0 ∧ c1 = 0 ∧ c2 = 0)) : False :=
  hne (hno c0 c1 c2 hann)

end QOU.Machinery.AJMinimality
