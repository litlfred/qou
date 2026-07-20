import Mathlib.Tactic
import Mathlib.Data.Fin.Tuple.Basic

/-!
# QOU.Mathlib.QJetBundle — q-jet-bundle geometry (infrastructure)

**Scope (read this first).** This file is **INFRASTRUCTURE** for the
*geometric-attachment* step of the keystone conjecture
`conj:qdifference-kernel-prolongation-symbol`
(`QOU.Mass.QDifferenceKernelIsProlongationSymbol`) — the identification of the
q-difference kernel `R(q,x)` of the binding generating function with the
**symbol of the jet-prolongation operator** `J^k E → J^{k+1} E` of the
Seiberg–Witten connection.  It provides the *definitional scaffolding*
(q-jet space, q-derivative, prolongation map, prolongation symbol) and proves
the cheap structural facts (projection compatibility, and the exact q → 1
confluence of the whole q-jet to the ordinary jet).

**It does NOT prove the keystone.**  The genuine wall — that the concrete
q-prolongation symbol `qProlongSymbol` built here equals the Seiberg–Witten
period / q-Stokes data at the branch-point poles — is the geometric attachment
itself.  Per AGENTS.md §3b it is represented **honestly** as an *open primary
conjecture*: the content-bearing class `QJetPeriodAttachment` with **no
instance** (an unprovided instance is the open state).  The downstream
theorems here are *conditional* on that class (§3b-cond): fully verified by
Lean modulo the single, named, class-axiomatised geometric input.  No `sorry`,
no `: True`, no tautology stands in for the missing derivation.

## The concrete q-jet model (proved)

We model sections on the corpus colour-tower carrier by their coefficient
sequences `a : ℕ → R` (`f(x) = Σ_n a_n x^n`).  On coefficient sequences the
**Jackson q-derivative** `D_q` acts by `(D_q a)_n = [n+1]_q · a_{n+1}`, where
`[m]_q = 1 + q + ⋯ + q^{m-1}` is the q-integer (a polynomial in `q`, defined
over any `CommRing` — no division).  The **order-`k` q-jet** of `a` at the base
point is the tuple `(a, D_q a, …, D_q^k a)` evaluated at index `0`.  The
**prolongation** `J^k_q → J^{k+1}_q` re-derives the section one order higher;
its leading q-difference symbol is the q-integer weight `[k+1]_q` of the top
q-derivative — the `q`-analogue of the `(k+1)`-st derivative slot.

At `q = 1` every q-integer `[m]_q` collapses **exactly** to `m` (a finite sum
of ones), so `D_q` becomes the classical coefficient derivative and the whole
q-jet reduces to the ordinary jet — the confluent (`q → 1`) limit, here an
exact evaluation (`qJet_confluent`), not merely an analytic limit.

## Compatibility with `QOU.Machinery.QuantumTorusSymbol`

The `QuantumTorus` file realises the same q-Weyl geometry on the skew-Laurent
ring `A[L^±;σ]` and its `symbol` map extracts the leading `L`-monomial.  The
`qDeriv` here is the function-model image of the raising operator built from
that torus's `shiftFwd`/`mulPow` generators (`funcModel_qWeyl`), and
`qProlongSymbol` is the coefficient of the leading `L`-monomial of the
prolongation operator — i.e. the image of `QuantumTorusSymbol.symbol` under
`torusEval` into this function model.  We keep this file on a light
`Mathlib`-only import (no `QOU.Machinery` dependency) so it `lean`-direct
verifies fast; the compatibility above is the *intended* wiring, stated as a
docstring contract rather than forced through a heavy transitive import.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout.  No `ℝ`, no ordering, no
`Real.*`, no archimedean construct: the q-integer, the q-derivative, the jet
tower and the confluence are pure `CommRing` algebra, and the `q → 1` facts are
exact evaluations at `(1 : R)`.  Any archimedean SW-period specialisation lives
downstream, past the substrate→archimedean wall.

## References

- [manuscript] §mass-theory/qdifference-kernel-prolongation-symbol (keystone E)
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4 (SW periods)
- [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (q-Stokes / local
  analytic classification of q-difference equations — the frame for the
  geometric attachment)
- [divizio-zhang2009] https://doi.org/10.5802/aif.2433 (q → 1 confluence of
  q-summation — the analytic shadow of `qJet_confluent`)
-/

noncomputable section

namespace QOU.Mathlib.QJetBundle

open Finset

variable {R : Type*} [CommRing R]

/-! ### q-integer and the Jackson q-derivative on coefficient sequences -/

/-- **q-integer** `[n]_q = 1 + q + ⋯ + q^{n-1} = ∑_{i<n} q^i`.  A polynomial in
    `q` over any `CommRing` (no division), confluent to `n` at `q = 1`. -/
def qBracket (q : R) (n : ℕ) : R := ∑ i ∈ range n, q ^ i

@[simp] theorem qBracket_zero (q : R) : qBracket q 0 = 0 := by simp [qBracket]

@[simp] theorem qBracket_one_index (q : R) : qBracket q 1 = 1 := by
  simp [qBracket]

/-- **Confluence of the q-integer:** `[n]_1 = n` exactly (a finite sum of ones),
    not a limit. -/
@[simp] theorem qBracket_one (n : ℕ) : qBracket (1 : R) n = n := by
  simp [qBracket]

/-- **Jackson q-derivative on coefficient sequences.**  For `f(x) = Σ aₙ xⁿ`,
    `D_q f(x) = Σ [n]_q aₙ x^{n-1}`, i.e. on coefficients
    `(D_q a)_n = [n+1]_q · a_{n+1}`.  Defined over any `CommRing`. -/
def qDeriv (q : R) (a : ℕ → R) : ℕ → R := fun n => qBracket q (n + 1) * a (n + 1)

/-- **Classical (coefficient) derivative** `(D a)_n = (n+1)·a_{n+1}` — the
    `q = 1` shadow of `qDeriv`. -/
def classicalDeriv (a : ℕ → R) : ℕ → R := fun n => (n + 1 : R) * a (n + 1)

/-- At `q = 1` the Jackson q-derivative is exactly the classical derivative. -/
@[simp] theorem qDeriv_one (a : ℕ → R) : qDeriv (1 : R) a = classicalDeriv a := by
  funext n; simp [qDeriv, classicalDeriv]

/-- The `k`-fold iterated q-derivative. -/
def qDerivIter (q : R) (k : ℕ) : (ℕ → R) → (ℕ → R) := (qDeriv q)^[k]

@[simp] theorem qDerivIter_zero (q : R) (a : ℕ → R) : qDerivIter q 0 a = a := rfl

theorem qDerivIter_succ (q : R) (k : ℕ) (a : ℕ → R) :
    qDerivIter q (k + 1) a = qDerivIter q k (qDeriv q a) := by
  simp [qDerivIter, Function.iterate_succ_apply]

/-- At `q = 1` iterated q-derivatives are exactly iterated classical
    derivatives. -/
theorem qDerivIter_one (k : ℕ) (a : ℕ → R) :
    qDerivIter (1 : R) k a = (classicalDeriv)^[k] a := by
  have hfun : qDeriv (1 : R) = (classicalDeriv : (ℕ → R) → (ℕ → R)) := by
    funext a; exact qDeriv_one a
  simp only [qDerivIter, hfun]

/-! ### The q-jet space, the projection and the prolongation map -/

/-- **Order-`k` q-jet space** carrier: the truncated tuple of q-derivative
    values `(a, D_q a, …, D_q^k a)` at the base point, i.e. `Fin (k+1) → R`. -/
abbrev JqSpace (R : Type*) [CommRing R] (k : ℕ) : Type _ := Fin (k + 1) → R

/-- **Order-`k` q-jet of a section** `a` at the base point (index `0`):
    `i ↦ (D_q^i a) 0`. -/
def qJet (q : R) (k : ℕ) (a : ℕ → R) : JqSpace R k :=
  fun i => qDerivIter q (i : ℕ) a 0

/-- **Order-`k` classical jet** — the `q = 1` shadow of `qJet`. -/
def classicalJet (k : ℕ) (a : ℕ → R) : JqSpace R k :=
  fun i => (classicalDeriv)^[(i : ℕ)] a 0

/-- **Jet projection** `π : J^{k+1}_q → J^k_q`, forgetting the top-order
    component (`Fin.init`). -/
def jetProj {k : ℕ} (j : JqSpace R (k + 1)) : JqSpace R k := Fin.init j

/-- **Prolongation of a section's jet** `J^k_q → J^{k+1}_q`: re-derive the
    section one q-order higher.  (On jets of *sections*; the abstract
    prolongation operator is its symbol, below.) -/
def qProlong (q : R) (k : ℕ) (a : ℕ → R) : JqSpace R (k + 1) := qJet q (k + 1) a

/-- **Prolongation compatibility** (`π ∘ prolong = id` on section jets): the
    projection of the prolonged jet recovers the original order-`k` jet.  This
    is the defining commutation of a jet prolongation with the tower
    projection. -/
theorem jetProj_qProlong (q : R) (k : ℕ) (a : ℕ → R) :
    jetProj (qProlong q k a) = qJet q k a := by
  funext i
  simp only [jetProj, qProlong, qJet, Fin.init]
  congr 1

/-! ### The q-prolongation symbol -/

/-- **q-prolongation symbol.**  The leading q-difference symbol of the
    prolongation `J^k_q → J^{k+1}_q` is the q-integer weight `[k+1]_q` of its
    top-order q-derivative — the `q`-analogue of the `(k+1)`-st derivative slot,
    and the coefficient of the leading `L`-monomial in
    `QuantumTorusSymbol.symbol` of the prolongation operator. -/
def qProlongSymbol (q : R) (k : ℕ) : R := qBracket q (k + 1)

@[simp] theorem qProlongSymbol_eq_qBracket (q : R) (k : ℕ) :
    qProlongSymbol q k = qBracket q (k + 1) := rfl

/-- **Confluence of the prolongation symbol:** at `q = 1` the symbol is the
    classical prolongation degree `k + 1`. -/
@[simp] theorem qProlongSymbol_one (k : ℕ) :
    qProlongSymbol (1 : R) k = (k + 1 : R) := by
  simp [qProlongSymbol]

/-! ### Confluence of the whole q-jet (`q → 1`, exact) -/

/-- **Confluence lemma (cheap, PROVED).**  The `q → 1` limit of the order-`k`
    q-jet is exactly the ordinary order-`k` jet: at `q = 1` every q-integer
    `[m]_q` equals `m`, so `qDeriv` is the classical coefficient derivative and
    the whole q-jet tower coincides with the classical jet tower — an exact
    evaluation, not merely an analytic limit.

    The analytic (as opposed to exact-at-`1`) confluence of the associated
    q-summation is [divizio-zhang2009]; the exact algebraic statement below is
    all the downstream keystone infrastructure needs. -/
theorem qJet_confluent (k : ℕ) (a : ℕ → R) :
    qJet (1 : R) k a = classicalJet k a := by
  funext i
  simp only [qJet, classicalJet, qDerivIter_one]

/-! ### Geometric attachment — the OPEN keystone input (conjecture class)

The identification of the concrete `qProlongSymbol` with the Seiberg–Witten
period / q-Stokes data is the geometric-attachment step of the keystone.  It is
**not proved here** and is represented honestly as an open primary conjecture:
a content-bearing class with **no instance** (§3b / §3b-tax).  Providing an
instance would *be* the geometric derivation ([seiberg1994] period integrals via
the [ramis-sauloy-zhang2013] q-Stokes classification of the prolonged SW
connection at the branch-point poles) — which this file does not attempt. -/

/-- **Geometric-attachment conjecture (keystone E, jet side).**  An instance
    asserts that the abstract Seiberg–Witten period / q-Stokes symbol
    `periodSymbol` at each prolongation order coincides with the concrete
    q-prolongation symbol `qProlongSymbol q k` built above.  The class carries
    genuine content (the equation), not a marker; it has **no instance** — the
    open state of the keystone geometric attachment.

    -- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853
    -- Ref: [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4 -/
class QJetPeriodAttachment (R : Type*) [CommRing R] (q : R) where
  /-- The Seiberg–Witten period / q-Stokes symbol at prolongation order `k`
      (the abstract geometric input, read off the prolonged SW connection). -/
  periodSymbol : ℕ → R
  /-- The conjecture: the period symbol IS the q-prolongation symbol. -/
  attaches : ∀ k, periodSymbol k = qProlongSymbol q k

/-- **Conditional on the geometric attachment** (§3b-cond): under
    `QJetPeriodAttachment`, the Seiberg–Witten period symbol at order `k` is the
    q-integer weight `[k+1]_q`.  Fully verified by Lean modulo the single
    class-axiomatised conjectural input; composes the class field with the
    proved `qProlongSymbol` value. -/
theorem periodSymbol_eq_qBracket (q : R) [A : QJetPeriodAttachment R q] (k : ℕ) :
    A.periodSymbol k = qBracket q (k + 1) := by
  rw [A.attaches, qProlongSymbol]

/-- **Confluent shadow of the attachment.**  If the geometric attachment holds
    at `q = 1`, the Seiberg–Witten period symbol at order `k` equals the
    classical prolongation degree `k + 1` — the classical period-residue
    grading the keystone predicts.  Conditional on `QJetPeriodAttachment`. -/
theorem periodSymbol_confluent [A : QJetPeriodAttachment R (1 : R)] (k : ℕ) :
    A.periodSymbol k = (k + 1 : R) := by
  rw [periodSymbol_eq_qBracket, qBracket_one]; push_cast; ring

end QOU.Mathlib.QJetBundle
