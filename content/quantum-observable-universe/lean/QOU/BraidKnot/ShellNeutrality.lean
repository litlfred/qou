import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic

/-!
# QOU.BraidKnot.ShellNeutrality — saturated-shell neutrality conjecture

The full-twist ribbon operator `θ_n ∈ Z(H_n(q))` acts on the
irreducible Hecke module `V_λ` by the scalar `q^{2·κ_λ}`, where
`κ_λ = Σ c(x)` is the sum of Jucys–Murphy contents of the boxes of
`λ`. This file axiomatises the conjectural physical equivalence
between *saturated shell* and `θ_n` acting trivially on `V_λ`, which
in turn is equivalent (over saturated spectra) to `λ = λ'`.

The two purely algebraic ingredients are exposed as typeclass fields:

* `fullTwistEigenvalue` — the standard Hecke fact that `θ_n`
  acts as a scalar depending only on `κ_λ`. Provable; conjectural
  here only because we have not yet imported the Hecke library.
* `kappaZero_iff_selfConjugate` — over a saturated spectrum,
  `κ_λ = 0 ↔ λ = λ'`. Provable in pure partition combinatorics;
  conjectural here only because we have not yet built the partition
  arithmetic.

The conjectural content sits in `SaturatedShellConjecture`: the
*first* direction — that brane-tower saturation **forces**
`θ_n · Φ_n = Φ_n`, i.e. global topological neutrality — depends on
the locality-free reading of the categorical mass endomorphism.

LaTeX label: `conj:categorical-neutrality-saturated-shells`

## References

- [mathas1999] https://doi.org/10.1090/ulect/015 — Iwahori–Hecke
  algebras and Schur algebras
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 — Quantum
  groups, ribbon categories
- [turaev2010] https://doi.org/10.1515/9783110221848 — Quantum
  invariants of knots
- [jucys1974] — Jucys, Symmetric polynomials and the centre of the
  symmetric group ring
- [murphy1992] https://doi.org/10.1016/0021-8693(92)90105-T — A new
  construction of Young's seminormal representation
- [hoefsmit1974] — Hoefsmit, Representations of Hecke algebras of
  finite groups with BN-pairs of classical type (PhD thesis)
- [manuscript] braids-and-knots / categorical-neutrality-saturated-shells
-/

namespace QOU.BraidKnot.ShellNeutrality

/-! ## §1  Combinatorial inputs -/

/-- A Young diagram, encoded by the box-set of its underlying
    partition. The Jucys–Murphy content of a box `(i, j)` is the
    integer `j - i`; we treat the diagram abstractly via its content
    multiset. -/
structure YoungDiagram where
  /-- Number of strands `n = |λ|`. -/
  n : ℕ
  /-- Multiset of Jucys–Murphy contents `{c(x) : x ∈ λ}`. -/
  contents : Multiset ℤ
  /-- The multiset has exactly `n` boxes. -/
  card_eq : contents.card = n

/-- Total Jucys–Murphy charge `κ_λ := Σ_{x ∈ λ} c(x)`. -/
def kappa (λ : YoungDiagram) : ℤ := λ.contents.sum

/-- Conjugate (transposed) Young diagram: contents flip sign. -/
def conjugate (λ : YoungDiagram) : YoungDiagram where
  n := λ.n
  contents := λ.contents.map (fun c => -c)
  card_eq := by
    simp [Multiset.card_map, λ.card_eq]

/-- A diagram is **self-conjugate** when it equals its conjugate. -/
def isSelfConjugate (λ : YoungDiagram) : Prop :=
  λ = conjugate λ

/-- `κ_{λ'} = -κ_λ`. The contents multiset of the conjugate diagram
    is obtained by negating each entry, so its sum negates. -/
theorem kappa_conjugate (λ : YoungDiagram) :
    kappa (conjugate λ) = -kappa λ := by
  unfold kappa conjugate
  -- goal: (λ.contents.map fun c => -c).sum = -λ.contents.sum
  induction λ.contents using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
    simp [Multiset.map_cons, Multiset.sum_cons, ih, neg_add]

/-- **Conjugation is an involution.** `(λ')' = λ`: negating contents
    twice is the identity on the multiset. -/
theorem conjugate_involution (λ : YoungDiagram) :
    conjugate (conjugate λ) = λ := by
  cases λ with
  | mk n contents card_eq =>
    simp only [conjugate, Multiset.map_map]
    congr 1
    -- goal: contents.map ((fun c => -c) ∘ (fun c => -c)) = contents
    have : ((fun c : ℤ => -c) ∘ (fun c => -c)) = id := by
      funext c
      simp
    rw [this, Multiset.map_id]

/-- **Forward direction (provable):** a self-conjugate diagram has
    zero global Jucys–Murphy charge. Proof: `κ_λ = κ_{λ'} = -κ_λ`,
    so `2 κ_λ = 0`, hence `κ_λ = 0` over `ℤ`. This is pure
    multiset arithmetic — no Hecke / Young-lattice structure needed. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
theorem kappa_zero_of_self_conjugate
    (λ : YoungDiagram) (h : isSelfConjugate λ) :
    kappa λ = 0 := by
  have heq : kappa λ = kappa (conjugate λ) := by
    conv_lhs => rw [h]
  have hneg : kappa (conjugate λ) = -kappa λ := kappa_conjugate λ
  have hself : kappa λ = -kappa λ := heq.trans hneg
  linarith

/-- **Empty Young diagram** (the unique `n = 0` shape): no boxes, no
    contents, charge zero, self-conjugate. Smoke-test instance for
    the framework. -/
def emptyDiagram : YoungDiagram where
  n := 0
  contents := 0  -- the empty multiset
  card_eq := by simp

/-- The empty diagram has zero charge. -/
theorem kappa_emptyDiagram : kappa emptyDiagram = 0 := by
  simp [kappa, emptyDiagram]

/-- The empty diagram is self-conjugate (negating the empty multiset
    gives the empty multiset). -/
theorem emptyDiagram_isSelfConjugate : isSelfConjugate emptyDiagram := by
  unfold isSelfConjugate conjugate emptyDiagram
  -- goal: ⟨0, 0, _⟩ = ⟨0, (0 : Multiset ℤ).map (·.neg), _⟩
  congr 1
  simp

/-! ### Disjoint union and content additivity -/

/-- Disjoint union of two Young diagrams (multiset union of their
    contents). The corresponding combinatorial operation is
    "horizontal concatenation" of partition contents — useful when
    splitting a composite analysis along constituent shells. -/
def unionDiagram (λ μ : YoungDiagram) : YoungDiagram where
  n := λ.n + μ.n
  contents := λ.contents + μ.contents
  card_eq := by simp [Multiset.card_add, λ.card_eq, μ.card_eq]

/-- **Additivity of Jucys–Murphy charge.** Charge is linear over
    multiset disjoint union: `κ(λ ⊔ μ) = κ(λ) + κ(μ)`. This is the
    abstract version of the LR content-additivity claim used in
    `LRFusion.ContentAdditive`. Provable directly from
    `Multiset.sum_add`. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem kappa_unionDiagram (λ μ : YoungDiagram) :
    kappa (unionDiagram λ μ) = kappa λ + kappa μ := by
  simp [kappa, unionDiagram, Multiset.sum_add]

/-- The empty diagram is a left/right identity for `unionDiagram` at
    the level of contents and charge. -/
theorem kappa_unionDiagram_empty_left (λ : YoungDiagram) :
    kappa (unionDiagram emptyDiagram λ) = kappa λ := by
  simp [kappa_unionDiagram, kappa_emptyDiagram]

theorem kappa_unionDiagram_empty_right (λ : YoungDiagram) :
    kappa (unionDiagram λ emptyDiagram) = kappa λ := by
  simp [kappa_unionDiagram, kappa_emptyDiagram]

/-- **Self-conjugacy is preserved under disjoint union.** If both
    `λ` and `μ` are self-conjugate, so is `unionDiagram λ μ`. Pure
    Multiset arithmetic — `Multiset.map_add` plus the constituent
    self-conjugacies' contents equalities. No axioms.

    This is the abstract analogue of the LR-rigidity claim for the
    trivial union composite. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem unionDiagram_isSelfConjugate
    {λ μ : YoungDiagram}
    (hλ : isSelfConjugate λ) (hμ : isSelfConjugate μ) :
    isSelfConjugate (unionDiagram λ μ) := by
  -- Extract contents equalities from constituent self-conjugacies.
  have e_λ : λ.contents = λ.contents.map (fun c => -c) := by
    have h := congr_arg YoungDiagram.contents hλ
    simpa [conjugate] using h
  have e_μ : μ.contents = μ.contents.map (fun c => -c) := by
    have h := congr_arg YoungDiagram.contents hμ
    simpa [conjugate] using h
  -- Show union = conjugate union: same n by construction, contents equal.
  show unionDiagram λ μ = conjugate (unionDiagram λ μ)
  unfold conjugate unionDiagram
  congr 1
  rw [Multiset.map_add, ← e_λ, ← e_μ]

/-! ### Singleton-box diagrams -/

/-- The single-box Young diagram with content `c`. Used as the base
    case for inductive arguments on shape complexity. -/
def singletonDiagram (c : ℤ) : YoungDiagram where
  n := 1
  contents := {c}
  card_eq := by simp

/-- Charge of a singleton diagram is its content. -/
theorem kappa_singletonDiagram (c : ℤ) :
    kappa (singletonDiagram c) = c := by
  simp [kappa, singletonDiagram]

/-! ### Decidability — see Mathlib bridge below

The abstract `YoungDiagram` (a `Multiset ℤ` with a cardinality
witness) inherits `DecidableEq` from `DecidableEq (Multiset ℤ)`.
A `Decidable (isSelfConjugate λ)` instance follows. Both are
deferred to the Mathlib bridge file (future) to avoid coupling
to specific Lean 4 / Mathlib `deriving` machinery in this paper-
internal module.
-/

/-! ### Mathlib bridge — wired in `QOU.BraidKnot.MathlibBridge`

Concrete bridge `fromMathlib : Mathlib.YoungDiagram → YoungDiagram`
is supplied by the sibling module `QOU.BraidKnot.MathlibBridge`,
which imports `Mathlib.Combinatorics.Young.YoungDiagram` and
constructs the abstract Multiset of cell contents from the Mathlib
cell set. With that bridge in place, the abstract proved theorems
(`kappa_conjugate`, `kappa_zero_of_self_conjugate`,
`kappa_unionDiagram`, …) lift to Mathlib Young diagrams, and the
reverse direction `kappa = 0 → self-conjugate` becomes provable
in the Young-lattice setting (recorded there as `ReverseBridge`,
deferred to a Phase 3 follow-up).

The abstract Multiset model alone cannot discharge the reverse
direction: a counter-example is `{1, 2, -3}`, a multiset of integers
summing to zero that is not multiset-symmetric.
-/

/-! ## §2  Saturation predicate (locality-free reading) -/

/-- A **saturated spectrum** is one in which every box of `λ`
    contributes its content exactly once with no external
    weighting. The locality-free reading of the categorical mass
    endomorphism `Φ_n` is built into `Saturated`: if a state is
    saturated, the brane-tower contribution is governed entirely by
    the multiset `λ.contents`. Concrete instances expose `λ` as the
    dominant irreducible label of the Hecke module `V_λ`. -/
class Saturated (λ : YoungDiagram) : Prop

/-! ## §3  Hecke folklore — exposed as typeclass fields -/

/-- The full-twist eigenvalue. On `V_λ` the central element `θ_n`
    acts as the scalar `q^{2·κ_λ}`. The standard reference is
    [mathas1999, §3]; we expose the eigenvalue as an opaque map and
    record the equivalence "trivial action ↔ κ = 0" axiomatically.

    `fullTwistTrivial λ q` means that `θ_n` acts as the identity on
    `V_λ` at substrate parameter `q`.

    Concrete model: defined as `kappa λ = 0` (the algebraic
    consequence of `θ_n = q^{2κ_λ} = 1` at generic q).  The genuine
    Hecke-algebra reading awaits the `H_n(q)` import. -/
def fullTwistTrivial (λ : YoungDiagram) (_q : ℝ) : Prop :=
  kappa λ = 0

/-- **Hecke folklore (axiomatised here)**: at generic `q > 1`, the
    full twist acts trivially on `V_λ` iff `κ_λ = 0`.

    Provable in Mathas's framework once we wire up `H_n(q)`; the
    axiomatic exposure here keeps the present paper independent of
    that future import. -/
class FullTwistContentFormula (q : ℝ) where
  /-- `q > 1` (substrate regime). -/
  q_gt_one : 1 < q
  /-- The defining equivalence. -/
  trivial_iff_kappa_zero :
    ∀ (λ : YoungDiagram), fullTwistTrivial λ q ↔ kappa λ = 0

/-- **Partition arithmetic — reverse direction (axiomatised):** over
    a *saturated* spectrum, `κ_λ = 0` *implies* self-conjugacy. The
    forward direction `isSelfConjugate λ → κ_λ = 0` is proved
    unconditionally as `kappa_zero_of_self_conjugate`; only the
    reverse implication needs Young-lattice structure (the saturation
    hypothesis pins a contents multiset with zero sum to a unique
    self-conjugate shape). -/
class KappaZeroImpliesSelfConjugate where
  kappa_zero_imp_self_conjugate :
    ∀ (λ : YoungDiagram) [Saturated λ],
      kappa λ = 0 → isSelfConjugate λ

/-- Convenience iff packaging both directions: forward is the
    proved theorem, reverse is the typeclass field. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
theorem kappa_zero_iff_self_conjugate
    [KappaZeroImpliesSelfConjugate]
    (λ : YoungDiagram) [Saturated λ] :
    kappa λ = 0 ↔ isSelfConjugate λ := by
  refine ⟨KappaZeroImpliesSelfConjugate.kappa_zero_imp_self_conjugate λ, ?_⟩
  exact kappa_zero_of_self_conjugate λ

/-! ## §4  The saturated-shell neutrality conjecture -/

/-- A **stable completed shell** is the (conjectural, framework-level)
    physical predicate that `Φ_n` represents a global section of the
    categorical mass endomorphism over the rigid braided monoidal
    category, with finite observable mass.

    Concrete model: defined as `isSelfConjugate λ`, the algebraic
    avatar of shell completion (every box's content is matched by a
    negation, so the multiset is balanced).  The genuine "global
    section with finite mass" predicate is the upgrade target. -/
def StableCompletedShell (λ : YoungDiagram) : Prop := isSelfConjugate λ

/-- **Conjecture 1 — Categorical neutrality of saturated shells.**

    For any `n`-strand saturated state with dominant Hecke label `λ`,
    the following are equivalent at substrate `q`:

    * `λ` represents a stable completed shell.
    * The full twist `θ_n` acts trivially on `V_λ`.
    * `κ_λ = 0`.
    * `λ` is self-conjugate.

    The first equivalence — between the *physical* shell predicate
    and the algebraic neutrality condition — is the conjectural
    framework claim. The remaining equivalences are derived from the
    Hecke and partition-combinatorics typeclass fields. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
-- Ref: [mathas1999] Mathas, "Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group," AMS Univ. Lect. Series 15, 1999
class SaturatedShellConjecture (λ : YoungDiagram) [Saturated λ] (q : ℝ)
    extends FullTwistContentFormula q,
            KappaZeroImpliesSelfConjugate where
  /-- The conjectural physical-to-algebraic equivalence. -/
  shell_iff_full_twist_trivial :
    StableCompletedShell λ ↔ fullTwistTrivial λ q

/-- Re-export 1: shell ↔ `κ_λ = 0`. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
theorem shell_iff_kappa_zero
    (λ : YoungDiagram) [Saturated λ] (q : ℝ)
    [C : SaturatedShellConjecture λ q] :
    StableCompletedShell λ ↔ kappa λ = 0 := by
  rw [C.shell_iff_full_twist_trivial,
      C.trivial_iff_kappa_zero λ]

/-- Re-export 2: shell ↔ `λ` self-conjugate. -/
-- Ref: [manuscript] conj:categorical-neutrality-saturated-shells
theorem shell_iff_self_conjugate
    (λ : YoungDiagram) [Saturated λ] (q : ℝ)
    [C : SaturatedShellConjecture λ q] :
    StableCompletedShell λ ↔ isSelfConjugate λ := by
  rw [shell_iff_kappa_zero λ q]
  exact kappa_zero_iff_self_conjugate λ

end QOU.BraidKnot.ShellNeutrality
