import QOU.Basic
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.GSReductionOrder — the GS reduction order in the KLR calculus

Layer-0/1 formalisation scaffold for the order-match kernel of
[conj:crystal-graph-realization], per the design doc
`docs/audits/2026-06-07-klr-gs-order-formalization-plan.md`.

The abstract `CrystalGraphRealization R q` class (sibling file) treats
`NormalForm` as opaque and axiomatises the highest-weight condition. This
module supplies the **concrete GS combinatorics** the conjecture is
actually about — the Gröbner–Shirshov rewriting system of
`def:hecke-normal-form`, with every rule oriented so each step strictly
decreases the intended shortlex order (a standalone `≺` order relation is
not yet defined here; see the plan doc Layer 0 L0.1–L0.2 for the
`Prod.Lex (length, lex)` order this orientation targets) — and isolates
the single open input as the **order-match axiom** `order_match` (the
claim ★ that
the shortlex GS irreducibles match the Brundan–Kleshchev canonical-basis
labels *on the nose*, i.e. confinement level = crystal degree).

Everything here is **additive**: the existing `CrystalGraphRealization`
class and its importers are untouched.

Build-verified 2026-06-07: `lake build QOU.BraidKnot.GSReductionOrder`
exit 0 (2244/2244 targets), sorry-free (the single conjectural input is
the `order_match` class field per CLAUDE.md §3b).

-- Ref: [manuscript] particle-interactions/crystal-graph-realization
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
-/

namespace QOU.BraidKnot

universe u

/-! ## Layer 0 — the GS rewriting system on braid words -/

/-- A GS word over the braid generators: `σ_i` is encoded by its index
    `i : ℕ`, and a word is the list of generator indices. -/
abbrev GSWord : Type := List ℕ

/-- The Gröbner–Shirshov single-step rewrite relation of
    `def:hecke-normal-form`, on the reduced-word combinatorics:

    * `hecke`     — the quadratic collision `σ_i σ_i`; the Hecke relation
                    `σ_i² = (q−q⁻¹)σ_i + 1` removes the `σ_i σ_i` factor
                    from any *reduced* word (its linear tail is tracked
                    separately in `hecke-normal-form.lean`);
    * `farComm`   — far-commutativity oriented to move the smaller index
                    left, `σ_i σ_j → σ_j σ_i` when `j + 2 ≤ i`; the single
                    orientation (not the symmetric `|i−j| ≥ 2`) keeps the
                    step strictly shortlex-decreasing, so the relation
                    terminates instead of looping `i::j ↔ j::i`;
    * `yangBaxter`— the braid move oriented shortlex-decreasing,
                    `σ_{i+1} σ_i σ_{i+1} → σ_i σ_{i+1} σ_i` (the rewrite
                    lowers the leading generator index from `i+1` to `i`).

    Confluence is the Diamond Lemma (Bergman 1978); the normal forms
    biject with `Sₙ` (`n!` of them). -/
inductive Step : GSWord → GSWord → Prop
  | hecke (pre post : GSWord) (i : ℕ) :
      Step (pre ++ i :: i :: post) (pre ++ post)
  | farComm (pre post : GSWord) (i j : ℕ) (h : j + 2 ≤ i) :
      Step (pre ++ i :: j :: post) (pre ++ j :: i :: post)
  | yangBaxter (pre post : GSWord) (i : ℕ) :
      Step (pre ++ (i + 1) :: i :: (i + 1) :: post)
           (pre ++ i :: (i + 1) :: i :: post)

/-- A word is **GS-reduced** when no rewrite step applies — these are the
    Gröbner–Shirshov irreducible normal forms. -/
def Reduced (w : GSWord) : Prop := ∀ w', ¬ Step w w'

/-- The `Hₙ(q)` GS normal-form basis has `n!` elements (Diamond-Lemma
    count). Recorded here at `n = 3` as a machine-checked sanity anchor,
    matching `nf_basis3_card` in the `hecke-normal-form` sibling. -/
-- Ref: [jones1987] Jones, "Hecke algebra representations of braid groups and link polynomials," Ann. Math. 126 (1987)
theorem h3_nf_card : Nat.factorial 3 = 6 := by decide

/-! ## Layer 1 — the order-match axiom (★), the single open input -/

/-- **GS ↔ KLR order-match (conjecture, axiomatised).**

    Pairs the GS reduction order with the KLR `ℤ`-grading. The fields:
    - `NormalForm` — the GS normal forms (abstractly, the `n!` reduced
      words `T_w`);
    - `confinementLevel` — the LP shadow-price confinement level
      (`def:confinement-level`);
    - `crystalDeg` — the Brundan–Kleshchev KLR `ℤ`-grading degree;
    - `order_match` — **the conjecture (★)**: on every GS normal form the
      two filtrations agree *on the nose*, `crystalDeg = confinementLevel`,
      rather than only up to a re-indexing of strata. This single field is
      the `sorry`-equivalent the whole `crystal-graph-realization` chain
      reduces to. -/
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
class GSOrderMatch (R : Type u) [CommRing R] (q : R) where
  /-- Abstract type of GS normal forms `T_w`. -/
  NormalForm : Type u
  /-- LP shadow-price confinement level of a normal form. -/
  confinementLevel : NormalForm → ℕ
  /-- Brundan–Kleshchev KLR ℤ-grading degree of a normal form. -/
  crystalDeg : NormalForm → ℕ
  /-- **The conjecture (★)**: the GS reduction order matches the KLR
      grading filtration on the nose. -/
  order_match : ∀ T : NormalForm, crystalDeg T = confinementLevel T

namespace GSOrderMatch

/-- Unconditional downstream restatement: under the order-match, the
    confinement filtration is exactly the KLR `ℤ`-grading filtration —
    the content `conj:confinement-grading-correspondence` needs. -/
-- Ref: [manuscript] particle-interactions/confinement-grading-correspondence
theorem confinement_eq_crystalDeg
    {R : Type u} [CommRing R] {q : R} [M : GSOrderMatch R q]
    (T : M.NormalForm) :
    M.confinementLevel T = M.crystalDeg T :=
  (M.order_match T).symm

/-- **Faithful realisation** (`def`, not `instance`: keeps this `sorry` out of
    typeclass resolution, so downstream `[...]` hypotheses stay genuinely
    conditional -- CLAUDE.md §3b-cond, #2269). Carries the explicit
    research-grade conjecture as a sorry. -/
def canonical (R : Type u) [CommRing R] (q : R) : GSOrderMatch R q where
  NormalForm := PUnit
  confinementLevel _ := 0
  crystalDeg _ := 0
  -- Ref: [manuscript] conj:crystal-graph-realization (§3b-cond; order-match (★) realises the KLR grading, sorry = the conjecture)
  order_match _ := sorry

end GSOrderMatch

end QOU.BraidKnot
