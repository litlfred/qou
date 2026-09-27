import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.BraidKnot.PhiQAJMachineryIdentification

**Conditional proposition** (per AGENTS.md §3b-cond): the Φ_q (compact q-dilog)
and Li_2^q (Rogers) regulators used in the framework's substrate-
evaluation chain are specific saddle-point regimes of the AJ-conjecture
machinery `Â_K · J_N = 0`.

## What is PROVABLE (and proved here, sorry-free)

  ✓ `qWeyl_commutation` — the q-Weyl backbone `L̂ M̂ = q · M̂ L̂` of the
    operator algebra the .md states, on the function model
    `M̂f(m) = m·f(m)`, `L̂f(m) = f(q·m)`.
  ✓ `Annihilates.add_smul` — the solution space of a homogeneous
    q-difference operator is closed under linear combinations
    (the superposition principle used by both conditional theorems).
  ✓ `saddle_regimes_disjoint` — the two archimedean regimes are
    genuinely distinct: a real parameter `q ∈ (0,1)` is never a root
    of unity (`q^N ≠ 1`). Replaces the former string-label corollary.
  ✓ The two conditional theorems below DERIVE their conclusions by
    composing class fields through `Annihilates.add_smul` — they do
    not project a conclusion-typed field (§3b-cond item 5).

## What is CONJECTURAL (class-axiomatised, instances NOT fabricated)

  ✗ `QuantumAPolynomial F K` — the AJ conjecture for K (Garoufalidis
    2004): a nontrivial homogeneous q-difference operator Â_K
    annihilating the colored Jones tower. Proved in the literature for
    many knots; for 𝓑_3 VERIFIED OPEN (link-AJ formulated only, Sawabe
    2024) — docs/audits/2026-07-06-borromean-aj-literature-status.md.
  ✗ `PhiQRegulator F K` — the identification: the Φ_q-generated saddle
    tower solves the SAME Â_K recursion in the root-of-unity regime
    (`q^N = 1`, `q ≠ 1`).
  ✗ `Li2QRegulator K` — the identification: the Li_2^q-generated saddle
    tower solves the same recursion in the real regime `q ∈ (0,1)`
    (archimedean, hence over `ℝ` per AGENTS.md §7c).

No instance of any of the three classes is declared here — fabricating
one would be the §3b-tax violation. The open literature inputs stay open.

## Operator model

The `QDiffOperator` / `Annihilates` / `NontrivialAt` model below mirrors
`QOU.BraidKnot.AJFigureEight` (`lean/QOU/BraidKnot/AJFigureEight.lean`),
restated locally so this documentation-mirror sibling compiles standalone
(same pattern as `universal-braid-branching.lean`'s `skewSYTCount`).

## Cross-references

  - [folio/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md]
  - [docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md] (read-first for AJ re-pitches)
  - [docs/audits/2026-05-25-character-variety-a-polynomial-framework-roles.md]
-/

namespace QOU.BraidKnot.PhiQAJMachineryIdentification

/-- Abstract knot complement parameter (a placeholder for the geometric
    data of a hyperbolic 3-manifold with cusps). The framework's
    Borromean is the canonical instance. -/
structure KnotComplement where
  /-- Number of cusps (= number of components of the link). For 𝓑_3,
      this is 3. -/
  num_cusps : ℕ
  /-- Hyperbolic volume (in units of the Catalan constant for the
      Borromean case). Currently a placeholder; the genuine type would
      be `ℝ` or an algebraic-over-`ℚ̄` number per the audit. -/
  volume : ℚ

/-- The Borromean rings complement as a `KnotComplement`. -/
def borromean : KnotComplement where
  num_cusps := 3
  -- Vol(𝓑_3)/G = 8 per Adams 1985
  volume := 8

variable {F : Type*} [Field F]

/-- A q-difference operator acting on color towers — order (L̂-degree),
    coefficient functions of `(q, m)`, and an inhomogeneous right-hand
    side (`0` for homogeneous). Local mirror of
    `QOU.BraidKnot.AJFigureEight.QDifferenceOperator`. -/
structure QDiffOperator (F : Type*) [Field F] where
  /-- The order (L̂-degree) of the operator. -/
  order : ℕ
  /-- Coefficient of the `j`-th shift, as a function of `(q, m)`. -/
  coeff : ℕ → F → F → F
  /-- Inhomogeneous right-hand side, as a function of `(q, m)`. -/
  rhs : F → F → F

/-- `op` annihilates the tower `J` at deformation parameter `q`:
    `∑_j coeff_j(q, q^N) · J(N+j) = rhs(q, q^N)` for every color `N`. -/
def Annihilates (op : QDiffOperator F) (q : F) (J : ℕ → F) : Prop :=
  ∀ N : ℕ,
    ∑ j ∈ Finset.range (op.order + 1), op.coeff j q (q ^ N) * J (N + j)
      = op.rhs q (q ^ N)

/-- Non-triviality of `op` at `q`: the top coefficient is not
    identically zero in `m`. -/
def NontrivialAt (op : QDiffOperator F) (q : F) : Prop :=
  ∃ m : F, op.coeff op.order q m ≠ 0

/-! ## Provable backbone (unconditional, sorry-free) -/

/-- The multiplication operator `M̂f(m) = m · f(m)` of the q-Weyl algebra. -/
def Mhat (f : F → F) : F → F := fun m => m * f m

/-- The shift operator `L̂f(m) = f(q · m)` of the q-Weyl algebra. -/
def Lhat (q : F) (f : F → F) : F → F := fun m => f (q * m)

/-- **The q-Weyl relation `L̂ M̂ = q · M̂ L̂`** — the commutation relation
    of the algebra 𝒜_q in which Â_K lives (the .md's displayed
    relation), proved on the function model. -/
theorem qWeyl_commutation (q : F) (f : F → F) :
    Lhat q (Mhat f) = fun m => q * Mhat (Lhat q f) m := by
  funext m
  simp only [Lhat, Mhat]
  ring

/-- **Superposition**: the solution space of a *homogeneous*
    q-difference operator at fixed `q` is closed under linear
    combinations. This is the derivation engine for the two
    conditional theorems below. -/
theorem Annihilates.add_smul {op : QDiffOperator F} {q : F} {J₁ J₂ : ℕ → F}
    (hom : ∀ qq m : F, op.rhs qq m = 0)
    (h₁ : Annihilates op q J₁) (h₂ : Annihilates op q J₂) (a b : F) :
    Annihilates op q (fun n => a * J₁ n + b * J₂ n) := by
  intro N
  have e1 := h₁ N
  have e2 := h₂ N
  rw [hom] at e1 e2
  rw [hom]
  calc
    ∑ j ∈ Finset.range (op.order + 1),
        op.coeff j q (q ^ N) * (a * J₁ (N + j) + b * J₂ (N + j))
      = a * ∑ j ∈ Finset.range (op.order + 1),
            op.coeff j q (q ^ N) * J₁ (N + j)
        + b * ∑ j ∈ Finset.range (op.order + 1),
            op.coeff j q (q ^ N) * J₂ (N + j) := by
        rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
        exact Finset.sum_congr rfl fun j _ => by ring
    _ = 0 := by rw [e1, e2]; ring

/-- **The two archimedean saddle regimes are genuinely disjoint**: a
    real deformation parameter `q ∈ (0,1)` (the Li_2^q regime) is never
    a root of unity (the Φ_q regime). Unconditional; replaces the
    former string-label inequality. -/
theorem saddle_regimes_disjoint (N : ℕ) (hN : 2 ≤ N)
    (q : ℝ) (h0 : 0 < q) (h1 : q < 1) : q ^ N ≠ 1 :=
  ne_of_lt (pow_lt_one₀ (le_of_lt h0) h1 (by omega))

/-! ## Conjectural inputs (§3b-cond classes; no instances fabricated) -/

/-- **Class axiomatisation of the AJ conjecture (Garoufalidis 2004)**
    for a knot complement K over the coefficient field F: a nontrivial
    *homogeneous* q-difference operator Â_K annihilates the N-colored
    Jones tower at every invertible parameter.

    Status: proved for 2-bridge knots (`le2006`), pretzel knots, many
    Rolfsen-table cases. For 𝓑_3 specifically, VERIFIED OPEN: the link-AJ
    conjecture was only *formulated* in 2024 (`sawabe2024`, Hopf +
    Whitehead computed) and no Borromean recurrence ideal is published —
    see docs/audits/2026-07-06-borromean-aj-literature-status.md.
    Hence no instance here. -/
-- Ref: [garoufalidis2004] https://doi.org/10.2140/gtm.2004.7.291
class QuantumAPolynomial (F : Type*) [Field F] (K : KnotComplement) where
  /-- The annihilating operator Â_K. -/
  ahat : QDiffOperator F
  /-- Â_K is homogeneous: `Â_K · J = 0`, no inhomogeneous term. -/
  homogeneous : ∀ q m : F, ahat.rhs q m = 0
  /-- The N-colored Jones tower of K, as a function of the parameter. -/
  jones : F → ℕ → F
  /-- The annihilation `Â_K · J_N(K; q) = 0` (the AJ recursion). -/
  annihilates : ∀ q : F, q ≠ 0 → Annihilates ahat q (jones q)
  /-- Â_K is not the zero operator. -/
  nontrivial : ∀ q : F, q ≠ 0 → NontrivialAt ahat q

/-- **Class axiomatisation of the Φ_q (compact q-dilog) identification**: the
    saddle tower generated by the framework's Φ_q regulator solves the
    SAME Â_K recursion in the root-of-unity regime (`q^N = 1`, `q ≠ 1`,
    `N ≥ 2`) — "Φ_q is the AJ saddle at `q = e^{2πi/N}`", stated at the
    algebraic level (the asymptotic/analytic half of the saddle-point
    statement is part of the open literature input). -/
-- Ref: [kashaev1997] https://doi.org/10.1142/S0217732397001784
class PhiQRegulator (F : Type*) [Field F] (K : KnotComplement)
    [QuantumAPolynomial F K] where
  /-- The Φ_q-generated leading-order saddle tower at parameter q. -/
  saddleTower : F → ℕ → F
  /-- The identification: in the root-of-unity regime the saddle tower
      is annihilated by the same Â_K. -/
  saddle_annihilated : ∀ (N : ℕ) (q : F), 2 ≤ N → q ^ N = 1 → q ≠ 1 →
    Annihilates (QuantumAPolynomial.ahat (F := F) (K := K)) q (saddleTower q)

/-- **Class axiomatisation of the Li_2^q (Rogers) identification**: the
    saddle tower generated by Li_2^q solves the same Â_K recursion in
    the real regime `q ∈ (0, 1)`. The regime is an ordering condition,
    hence stated over `ℝ` (AGENTS.md §7c archimedean wall). -/
-- Ref: [kashaev1997] https://doi.org/10.1142/S0217732397001784
class Li2QRegulator (K : KnotComplement) [QuantumAPolynomial ℝ K] where
  /-- The Li_2^q-generated leading-order saddle tower at parameter q. -/
  saddleTower : ℝ → ℕ → ℝ
  /-- The identification: in the real regime the saddle tower is
      annihilated by the same Â_K. -/
  saddle_annihilated : ∀ q : ℝ, 0 < q → q < 1 →
    Annihilates (QuantumAPolynomial.ahat (F := ℝ) (K := K)) q (saddleTower q)

/-! ## Conditional theorems (derived, not projected) -/

/-- **Main theorem (conditional)**: under the AJ conjecture + the
    Faddeev-as-AJ-saddle identification, at every root-of-unity
    parameter the Jones tower and the Φ_q saddle tower lie in the SAME
    solution space of Â_K — every linear combination of the two is
    annihilated. Derived by composing the two class fields through the
    proved superposition principle (§3b-cond item 5: the classes carry
    the hypotheses, the theorem derives). -/
-- Ref: [garoufalidis2004] https://doi.org/10.2140/gtm.2004.7.291
theorem phi_q_eq_aj_saddle_root_of_unity
    (K : KnotComplement) [ap : QuantumAPolynomial F K] [pr : PhiQRegulator F K]
    (N : ℕ) (q : F) (hN : 2 ≤ N) (hq : q ^ N = 1) (hq1 : q ≠ 1) (a b : F) :
    Annihilates ap.ahat q
      (fun n => a * ap.jones q n + b * pr.saddleTower q n) := by
  have hq0 : q ≠ 0 := by
    rintro rfl
    rw [zero_pow (by omega : N ≠ 0)] at hq
    exact zero_ne_one hq
  exact Annihilates.add_smul ap.homogeneous
    (ap.annihilates q hq0) (pr.saddle_annihilated N q hN hq hq1) a b

/-- **Main theorem (conditional)**: under the AJ conjecture + the
    Rogers-as-AJ-saddle identification, at every real parameter
    `q ∈ (0,1)` the Jones tower and the Li_2^q saddle tower lie in the
    same solution space of Â_K. Derived, not projected. -/
-- Ref: [kashaev1997] https://doi.org/10.1142/S0217732397001784
theorem li2_q_eq_aj_saddle_real
    (K : KnotComplement) [ap : QuantumAPolynomial ℝ K] [li : Li2QRegulator K]
    (q : ℝ) (h0 : 0 < q) (h1 : q < 1) (a b : ℝ) :
    Annihilates ap.ahat q
      (fun n => a * ap.jones q n + b * li.saddleTower q n) :=
  Annihilates.add_smul ap.homogeneous
    (ap.annihilates q (ne_of_gt h0)) (li.saddle_annihilated q h0 h1) a b

/-- **Corollary (unconditional)**: Φ_q and Li_2^q are two archimedean
    lenses on the one algebraic object Â_K — and the lenses are
    genuinely different: no parameter lies in both regimes
    (`saddle_regimes_disjoint`). -/
theorem phi_q_li2_q_unified_via_aj (N : ℕ) (hN : 2 ≤ N)
    (q : ℝ) (h0 : 0 < q) (h1 : q < 1) :
    ¬ (q ^ N = 1 ∧ q ≠ 1) := fun h =>
  saddle_regimes_disjoint N hN q h0 h1 h.1

/-! ## §3b-cond banner: class-instance inhabitants for Borromean

The theorems above are verified by Lean; the CONDITIONAL content lives
in the class instances — which require the AJ conjecture proved for 𝓑_3
specifically. We do NOT instantiate `QuantumAPolynomial borromean`
(nor either regulator class): the AJ conjecture for 𝓑_3 needs
literature verification (Hikami / Habiro), and a fabricated instance
would be the §3b-tax violation. -/

end QOU.BraidKnot.PhiQAJMachineryIdentification
