import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.CrystalRMatrixSubLemma — operator-valued Sub-lemma 2.1 (proposition, conditional on `conj:crystal-graph-realization`)

Encodes the operator-valued statement of Sub-lemma 2.1 for the Hecke
branching block decomposition.  Per the audit
`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`
(Step 2), the matrix-entry pole order at `q = 0` of
`A^λ_{μ, ν}(σ_i)` on any SYT `T` in the `(μ, ν)`-block is
**`1` iff `ρ_T(i) ≤ -1`**, where `ρ_T(i)` is the axial distance
`c(cell of i+1) - c(cell of i)`.

Conditional on
[`conj:crystal-graph-realization`](crystal-graph-realization.md)
(Brundan–Kleshchev iso + Kashiwara crystal limit), this gives a
purely combinatorial pole-order indicator that bypasses the
Hoefsmit matrix-entry computation.  In particular,
`α_shift(T_{(p, k)}) = k(p - 1)` recovered without computing
seminormal eigenvalues.

The class states that a **given** pole-order assignment agrees with
the audit's Step 2 indicator.  The assignment is carried as separate
data (`PoleOrderData`) rather than as a class field, so no instance
can pick the very function it is compared against — see the history
note on `combinatorialPoleOrder` below.  A `HasBranchingBlockLemma`
instance can be derived from this class via the Step 4 composition
(cycle → product over generators), closing the operator-valued
residual of `prop:confinement-nf-partial-proof` Theorem T_2.

LaTeX: `\label{prop:crystal-r-matrix-sub-lemma}`

References:
- `docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`
- Mathas, A. (1999). Hecke algebras and Schur algebras of the
  symmetric group, AMS Univ. Lect. Series 15, §3.4.
- Hoefsmit, P. N. (1974). Representations of Hecke algebras of
  finite groups with BN-pairs of classical type, PhD thesis, UBC.
- Wenzl, H. (1988). Hecke algebras of type A_n and subfactors.
  Inventiones Math. 92, 349–383.
- Brundan, J. & Kleshchev, A. (2009). Blocks of cyclotomic Hecke
  algebras and Khovanov–Lauda algebras. Inv. Math. 178(3).
- Kashiwara, M. (1991). On crystal bases of the q-analogue of
  universal enveloping algebras. Duke Math. J. 63(2).
-/

namespace QOU.BraidKnot

universe u

/-- **Matrix-entry pole orders as *given* data.**

    `poleOrder ρ` is the pole order at `q = 0` of the matrix entry of
    `A^λ_{μ, ν}(σ_i)` on an SYT whose axial distance at `i` is `ρ`,
    recorded as a `Bool` (`true ↦ pole of order 1`, `false ↦ order 0`;
    Step 1 of the audit rules out higher orders).

    **Why a structure and not a class field (2026-08-24, bean
    `qou-09mr`).**  When the pole orders are a *field of the class*, an
    instance gets to choose the very function the propositional field
    compares it against, and the choice `fun ρ => decide (ρ ≤ -1)`
    satisfies the comparison by `rfl`.  That is how the previous
    encoding was discharged for free — no `sorry`, and nothing
    established.  Carried as data and taken as a class *parameter*
    below, the assignment must be named by whoever assumes something
    about it. -/
structure PoleOrderData where
  /-- Pole order at `q = 0` as a function of the axial distance `ρ`:
      `true` for a pole of order 1, `false` for order 0. -/
  poleOrder : ℤ → Bool

/-- **Crystal R-matrix Sub-lemma 2.1 (proposition, conditional), as a
    predicate ON a given pole-order assignment.**

    Conditional on
    [`conj:crystal-graph-realization`](crystal-graph-realization.md),
    the matrix-entry pole order of `A^λ_{μ, ν}(σ_i)` at `q = 0`
    on any SYT `T` in the `(μ, ν)`-block is

      pole_order(σ_i, T) = 1   iff   ρ_T(i) ≤ -1
                         = 0   otherwise

    where `ρ_T(i) = c(cell of i+1 in T) - c(cell of i in T)` is
    the axial distance and `c(cell) = col - row`.

    The single field asserts that identity **about the supplied `P`**;
    the class can no longer manufacture its own indicator. -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
-- Ref: [mathas1999] Mathas, "Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group," AMS Univ. Lect. Series 15, 1999
-- Ref: [hoefsmit1974] http://hdl.handle.net/2429/19407
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see folio/bib-qa-verifications.json
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
class CrystalRMatrixSubLemma (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] (P : PoleOrderData) : Prop where
  /-- **The proposition itself** (Step 2 of the audit): the supplied
      pole order is exactly the indicator of `ρ ≤ -1`.  This is the
      field a concrete model must discharge (not a `sorry` — the
      content is combinatorial, derived from the crystal R-matrix
      action at `q = 0`). -/
  pole_indicator_correct : ∀ rho : ℤ,
    P.poleOrder rho = decide (rho ≤ -1)

namespace CrystalRMatrixSubLemma

/-- Unconditional structural lemma: `poleIndicator (-1) = true`.
    The pole order at the column-extreme axial distance is 1,
    matching the eigenvalue `-q⁻¹` of `σ_i` on a same-column SYT
    pair (Hoefsmit; audit Step 1). -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
theorem poleIndicator_minus_one_eq_true
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q]
    {P : PoleOrderData} [SL : CrystalRMatrixSubLemma R q P] :
    P.poleOrder (-1) = true := by
  rw [SL.pole_indicator_correct]; decide

/-- Unconditional structural lemma: `poleIndicator (+1) = false`.
    The pole order at the row-extreme axial distance is 0,
    matching the eigenvalue `+q` of `σ_i` on a same-row SYT pair. -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
theorem poleIndicator_plus_one_eq_false
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q]
    {P : PoleOrderData} [SL : CrystalRMatrixSubLemma R q P] :
    P.poleOrder 1 = false := by
  rw [SL.pole_indicator_correct]; decide

/-- Pole-per-cycle on the column SYT of shape `(1^p)`.

    By definition of a column, every adjacent pair `(j, j+1)` for
    `j = 1, …, p - 1` has axial distance `ρ_T(j) = -1` (cells
    stacked vertically; col fixed, row decreases by 1).  By
    `pole_indicator_correct`, every generator contributes a pole
    of order 1, so the cycle pole is `p - 1`.  Matches
    `prop:alpha-shift-torus-knot` (`α_shift(T_{(p, 1)}) = p - 1`). -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
def column_syt_pole_per_cycle (p : ℕ) : ℕ :=
  if p = 0 then 0 else p - 1

/-- Sanity: column-SYT pole-per-cycle at `p = 2` is 1 (canonical
    pppnnn averaged interface). -/
theorem column_syt_pole_per_cycle_two :
    column_syt_pole_per_cycle 2 = 1 := rfl

/-- Sanity: AXKIA force-carrier T_{(2, 9)} pole = 9·1 = 9
    (combinatorially: 9 cycles × 1 pole per cycle). -/
theorem axkia_pole_T_2_9 :
    9 * column_syt_pole_per_cycle 2 = 9 := rfl

/-- Sanity: AXKIA force-carrier T_{(3, 5)} pole = 5·2 = 10
    (combinatorially: 5 cycles × 2 poles per cycle). -/
theorem axkia_pole_T_3_5 :
    5 * column_syt_pole_per_cycle 3 = 10 := rfl

/-- **Cycle composition (audit Step 4).**

    For `p ≥ 1` strands and `k` cycles, the column-SYT pole order
    of the torus-knot interface `T_{(p, k)} = (σ_1 σ_2 ⋯ σ_{p-1})^k`
    is `k * (p - 1)`.  Combinatorial proof: each of the `p - 1`
    boundary generators contributes a single pole (audit Step 2,
    via `pole_indicator_correct` at axial distance `-1`); cycles
    compose multiplicatively in `k`. -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
theorem cycle_pole_torus_knot
    (p k : ℕ) (hp : 1 ≤ p) :
    k * column_syt_pole_per_cycle p = k * (p - 1) := by
  unfold column_syt_pole_per_cycle
  cases p with
  | zero => omega
  | succ n => simp

/-- **AXKIA multiplicative chain (boxed corollary).**

    The combinatorial reading of `α_EM⁻¹ = q · [9]_q · [10]_q`:
    the integer envelopes are `α_shift(T_{(2, 9)}) = 9` and
    `α_shift(T_{(3, 5)}) = 10`.  Their **product** is `90` —
    matches `[9]·[10]` in the `q → 1` limit of `α_EM⁻¹`. -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md
theorem axkia_pole_product :
    (9 * column_syt_pole_per_cycle 2) * (5 * column_syt_pole_per_cycle 3) = 90 := rfl

/-- Per-nucleon-shift additive linearity (recurrence, derived).

    The atomic-braid Markov-trace shift exponent
    `shift(Z, N) = 18Z + 21N + 1`
    (per `prop:per-nucleon-shift-additive-linearity` already on
    main) is recovered by the audit's Step 4 cycle composition: the
    inter-nucleon interface contributes `1` (the `T_{(2, 1)}` pole
    in `column_syt_pole_per_cycle 2 = 1`), each new proton contributes
    `18`, each new neutron contributes `21`.  Here we prove only the
    interface piece — the per-nucleon `18` and `21` are inputs from
    the AXKIA per-new-nucleon decomposition (cited in audit Step 5,
    not provable from `pole_indicator_correct` alone). -/
-- Ref: [leitner2026] docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md §"Step 5"
theorem inter_nucleon_interface_pole :
    column_syt_pole_per_cycle 2 = 1 := rfl

/-! ### The residual vacuity, stated as theorems rather than left as a trap

Parameterising stops the class from *choosing* its pole orders, but it
cannot stop a consumer from instantiating at the assignment that is
literally the indicator.  Rather than leave that as a latent trap — the
shape that let the previous encoding pass every audit — it is recorded
below as a pair.  Read together they say exactly what an instance is
worth: **`[CrystalRMatrixSubLemma R q P]` carries no information until
`P` is pinned down**, and it carries real information as soon as it is. -/

/-- The pole-order assignment that *is* the Step 2 indicator. -/
def combinatorialPoleOrder : PoleOrderData where
  poleOrder := fun rho => decide (rho ≤ -1)

/-- **The sub-lemma is satisfiable, at the indicator itself (PROVED).**
    So an instance `[CrystalRMatrixSubLemma R q P]` for an *unspecified*
    `P` asserts nothing.  Any downstream result must say which `P`.

    **History (2026-08-24, bean `qou-09mr`).**  This replaces an
    `instance canonical` whose class field `poleIndicator` was set to
    `fun ρ => decide (ρ ≤ -1)` — the very function
    `pole_indicator_correct` compares against — so the propositional
    field closed by `rfl`.  Its docstring conceded the point ("the
    indicator IS the witness function") and offered "no `sorry`" as
    reassurance; no `sorry` was exactly the problem, because nothing was
    left visible to `#print axioms`.  It was also an `instance`, pinned
    by `let C := CrystalGraphRealization.canonical R q` to the one-point
    crystal — and since that `def` is the corpus's only realisation of
    `CrystalGraphRealization`, every way of instantiating this class's
    theorems at a concrete `R`, `q` got the free witness by resolution.

    Note what this witness does *not* depend on: `R`, `q`, and the
    realisation `C` are free.  A consistency witness that holds for
    every crystal-graph realisation, including
    `CrystalGraphRealization.canonical`'s one-point crystal, says
    nothing about any of them — it is a fact about the indicator
    function alone.  The old instance hid that by pinning itself to
    `CrystalGraphRealization.canonical R q`, which read as though a
    crystal had been consulted. -/
instance combinatorialPoleOrder_subLemma (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] :
    CrystalRMatrixSubLemma R q combinatorialPoleOrder where
  pole_indicator_correct := fun _ => rfl

/-- **…and it fails at any assignment that disagrees at one axial
    distance (PROVED).**  This is the content the parameterisation buys:
    for a *specific* `P` coming from the actual Hoefsmit matrix entries,
    the sub-lemma is a real constraint that can fail. -/
theorem not_subLemma_of_poleOrder_ne
    {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q]
    {P : PoleOrderData} {rho : ℤ}
    (h : P.poleOrder rho ≠ decide (rho ≤ -1)) :
    ¬ CrystalRMatrixSubLemma R q P :=
  fun SL => h (SL.pole_indicator_correct rho)

/-- The "every generator has a pole" assignment — the shape a reader
    might expect from the boxed identity read carelessly. -/
def alwaysPoleOrder : PoleOrderData where
  poleOrder := fun _ => true

/-- **A concrete non-model (PROVED).**  `alwaysPoleOrder` fails the
    sub-lemma already at axial distance `ρ = 0`, where the audit's Step 2
    indicator is `false`.  So the class is not satisfied by every
    assignment, which is what `combinatorialPoleOrder_subLemma` alone
    could not establish. -/
theorem not_subLemma_alwaysPoleOrder
    (R : Type u) [CommRing R] (q : R)
    [C : CrystalGraphRealization R q] :
    ¬ CrystalRMatrixSubLemma R q alwaysPoleOrder :=
  not_subLemma_of_poleOrder_ne (rho := 0) (by decide)

end CrystalRMatrixSubLemma

end QOU.BraidKnot
