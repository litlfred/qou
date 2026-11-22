import QOU.Basic


/-!
# QOU.BraidKnot.rho_k_h3a_refinement
  — H_{3A} Wedderburn refinement of ρ_K beyond leading-order

Refines the leading-order constituent-mass ansatz
`ρ_K^LO = (Z·m_p + N·m_n) / (m_e·|tr_M|)` to the full
Wedderburn-Schur decomposition, with per-block binding-fraction
corrections `Δ_λ(K)`.

LaTeX: `\label{prop:rho-k-h3a-refinement}`

## Re-encoded 2026-09-04 (bean `qou-tmmt`) — and the class was UNINHABITABLE

The previous class had a single field which was the block's conclusion verbatim,
consumed by `inst.identity data Δ partitions` — a §3b-cond item-5 self-assuming
projection. Fixing that exposed a strictly worse defect underneath it.

That field universally quantified the *partition list* and the *correction map*
**inside** the hypothesis:

    identity : ∀ data Δ partitions, ρ_K − ρ_K^LO = (Σ_{λ ∈ partitions} …) / |tr_M|

Instantiating one data tuple at two different `partitions` forces the correction
sum to be independent of the list it sums over, which is false as soon as any
term is nonzero. `not_rhoKH3ARefinementNaive` below **proves** the class empty
(one witness: `y_chi ≡ 1`, `Δ ≡ 1`, `ρ_K = ρ_K^LO`, `|tr_M| = 1`, over the
one-element list). A conditional theorem whose hypothesis class has no instance
is vacuous — it was not a weak result, it was no result.

So `partitions` and the correction map are now *data carried by the class*
rather than universally quantified inside it, and the balance is a predicate on
that tuple. The class is consequently **inhabitable, and that is the point**:
a hypothesis bundle must be satisfiable or every theorem conditional on it says
nothing. What makes it an honest open conjecture is that no instance is
supplied — per §3b-tax — not that none could exist.

Two further changes, both forced by the same audit:

* `Float → ℝ`. `Float` has no field structure in Lean, so the division in the
  statement was not the division it stood for and no algebra was possible on it
   — which is why the original could only ever have been a projection.
* `BlockBindingFraction.leading_order` was a `Prop`-valued *data* field with a
  default, asserting nothing. It is now the predicate `IsLeadingOrder`, and
  `rho_k_eq_LO_of_isLeadingOrder` **derives** what its name promised: at leading
  order the refinement collapses to the constituent ansatz.
-/

namespace QOU.BraidKnot

/-- **Per-block binding-fraction correction.**

    For an atom `K` with nuclear-core Hecke word `β_K ∈ H_{3A}(q)` and irrep
    label `λ ⊢ 3A`, the per-block binding-fraction correction
    `Δ_λ(K)` measures the deviation of the λ-block mass
    contribution from the constituent-only piece
    `m_e · y_λ · χ^λ(β_K)`. -/
structure BlockBindingFraction (A : ℕ) where
  /-- Map λ ⊢ 3A to the per-block correction Δ_λ ∈ ℝ. -/
  delta : List ℕ → ℝ

/-- The **leading-order regime**: every per-block correction vanishes. Replaces
    the old `leading_order : Prop := …` field, which was a proposition-valued
    datum and therefore asserted nothing. -/
def BlockBindingFraction.IsLeadingOrder {A : ℕ} (Δ : BlockBindingFraction A) :
    Prop := ∀ lam, Δ.delta lam = 0

/-- **Per-atom Wedderburn data.**

    The structural inputs the refinement formula consumes for a
    given atom: the absolute Markov trace `|tr_M(β_K)|`, the
    leading-order density `ρ_K^LO`, the full density `ρ_K`, and
    per-partition `y_λ · χ^λ(β_K)` products supplied by the
    Wenzl bridge. -/
structure RhoKAtomData (A : ℕ) where
  /-- `|tr_M(β_K)|` at q_0. -/
  abs_tr_M     : ℝ
  /-- Leading-order constituent density `ρ_K^LO(Z, N)`. -/
  rho_K_LO     : ℝ
  /-- Full density `ρ_K(q_0)`. -/
  rho_K        : ℝ
  /-- `y_λ · χ^λ(β_K)` supplied by the Wenzl bridge. -/
  y_chi_term   : List ℕ → ℝ

/-- The Wedderburn correction sum `Σ_{λ ∈ partitions} y_λ χ^λ(β_K) · Δ_λ(K)`. -/
def blockCorrectionSum {A : ℕ} (data : RhoKAtomData A)
    (Δ : BlockBindingFraction A) (partitions : List (List ℕ)) : ℝ :=
  List.foldr (· + ·) 0 (partitions.map fun lam => data.y_chi_term lam * Δ.delta lam)

/-- At leading order every summand vanishes, so the correction sum does. -/
theorem blockCorrectionSum_eq_zero_of_isLeadingOrder {A : ℕ}
    (data : RhoKAtomData A) (Δ : BlockBindingFraction A)
    (partitions : List (List ℕ)) (hlo : Δ.IsLeadingOrder) :
    blockCorrectionSum data Δ partitions = 0 := by
  unfold blockCorrectionSum
  induction partitions with
  | nil => rfl
  | cons lam rest ih => simp [hlo lam, ih]

/-! ## The naive shape, and why it is empty

Recorded rather than deleted: this is the hypothesis the block was conditional
on before 2026-09-04, and the refutation is the reason the encoding changed. -/

/-- The **previous** hypothesis shape, with the partition list and the
    correction map quantified inside the field. Kept only as the subject of
    `not_rhoKH3ARefinementNaive`; do not build on it. -/
class RhoKH3ARefinementNaive (Z N : ℕ) : Prop where
  identity : ∀ (data : RhoKAtomData (Z + N)) (Δ : BlockBindingFraction (Z + N))
      (partitions : List (List ℕ)),
    data.rho_K - data.rho_K_LO =
      blockCorrectionSum data Δ partitions / data.abs_tr_M

/-- **The naive class has no instance.** Take an atom whose density already sits
    at its leading-order value, with unit trace magnitude, unit Wenzl-bridge
    terms and unit corrections. Over the one-element partition list the
    hypothesis reads `0 = 1`.

    Scope: this is a **structural exclusion** — the class is empty, so every
    theorem conditional on it is vacuous. It says nothing about whether the
    physical refinement identity holds. -/
theorem not_rhoKH3ARefinementNaive (Z N : ℕ) : ¬ RhoKH3ARefinementNaive Z N := by
  intro inst
  have h := inst.identity
    { abs_tr_M := 1, rho_K_LO := 0, rho_K := 0, y_chi_term := fun _ => 1 }
    { delta := fun _ => 1 } [[]]
  simp [blockCorrectionSum] at h

/-! ## The corrected encoding -/

/-- A tuple is **refinement-consistent** when the Wedderburn correction sum
    reproduces the density gap, stated division-free so that no well-definedness
    assumption hides inside a quotient. -/
def RefinementConsistent {A : ℕ} (data : RhoKAtomData A)
    (Δ : BlockBindingFraction A) (partitions : List (List ℕ)) : Prop :=
  (data.rho_K - data.rho_K_LO) * data.abs_tr_M = blockCorrectionSum data Δ partitions

/-- **Conditional hypotheses for the H_{3A} refinement of ρ_K.**

    The class carries the atom's own Wedderburn data — its partition list and
    per-block corrections included — and asserts that *that* tuple is
    refinement-consistent. The conjectural content is the assertion; the data
    fields are what make the assertion statable without the empty-class defect
    of `RhoKH3ARefinementNaive`.

    No instance is supplied. Per §3b-tax that is what an open primary
    conjecture looks like — a content-bearing carrier with nothing inhabiting
    it. -/
class RhoKH3ARefinement (Z N : ℕ) where
  /-- The atom's categorical data tuple at `q_0`. -/
  atomData : RhoKAtomData (Z + N)
  /-- Its per-block binding-fraction corrections `Δ_λ(K)`. -/
  blocks : BlockBindingFraction (Z + N)
  /-- The partitions of `3·(Z+N)` the Wedderburn decomposition ranges over. -/
  partitions : List (List ℕ)
  /-- **H1 — the refinement identity**, division-free. This is the conjectural
      content; nothing in this file derives it. -/
  consistent : RefinementConsistent atomData blocks partitions
  /-- **H2 — the trace magnitude is a magnitude.** The `abs_` prefix promises
      this and the type does not encode it (§3b-tax). -/
  abs_tr_M_nonneg : 0 ≤ atomData.abs_tr_M

variable (Z N : ℕ) [inst : RhoKH3ARefinement Z N]

/-- A nonzero trace magnitude is a positive one, by H2. -/
theorem rho_k_abs_tr_M_pos (h : inst.atomData.abs_tr_M ≠ 0) :
    0 < inst.atomData.abs_tr_M :=
  lt_of_le_of_ne inst.abs_tr_M_nonneg (Ne.symm h)

-- Ref: [leitner2026] prop:rho-k-h3a-refinement
/-- **The refinement identity in quotient form.** Derived from the division-free
    H1 by discharging the nonvanishing of `|tr_M(β_K)|`, which is a real side
    condition — see `rho_k_refinement_degenerate`. -/
theorem rho_k_h3a_refinement (h : 0 < inst.atomData.abs_tr_M) :
    inst.atomData.rho_K - inst.atomData.rho_K_LO =
      blockCorrectionSum inst.atomData inst.blocks inst.partitions
        / inst.atomData.abs_tr_M :=
  (eq_div_iff (ne_of_gt h)).mpr inst.consistent

/-- **At leading order the refinement collapses to the constituent ansatz.**
    This is what the old `leading_order` field named and did not prove. -/
theorem rho_k_eq_LO_of_isLeadingOrder (h : 0 < inst.atomData.abs_tr_M)
    (hlo : inst.blocks.IsLeadingOrder) :
    inst.atomData.rho_K = inst.atomData.rho_K_LO := by
  have hr := rho_k_h3a_refinement Z N h
  rw [blockCorrectionSum_eq_zero_of_isLeadingOrder _ _ _ hlo, zero_div,
    sub_eq_zero] at hr
  exact hr

/-- **The refinement says nothing at a Markov-trace zero.** H1 then forces the
    whole correction sum to vanish and leaves `ρ_K` unconstrained — the content
    the quotient form concealed inside its division. -/
theorem rho_k_refinement_degenerate (h : inst.atomData.abs_tr_M = 0) :
    blockCorrectionSum inst.atomData inst.blocks inst.partitions = 0 := by
  have hc := inst.consistent
  unfold RefinementConsistent at hc
  rw [h, mul_zero] at hc
  exact hc.symm

end QOU.BraidKnot
