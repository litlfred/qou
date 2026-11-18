import QOU.Information.CountingModuliGrade
import Mathlib.Tactic

/-!
# QOU.Information.QouPNeqNp — conjectural class + concrete decision-cost target

**§3b-cond class axiomatisation** for content block
[`conj:qou-p-neq-np`](../../../quantum-observable-universe/information-theory/qou-p-neq-np.md): *$\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q \in \mathbb{G}_m$*.

Two layers, mirroring the block's chippable/conjectural split:

1. **The conjecture** — class `QouPNeqNp`, whose `faithful` field carries the
   open counting→decision transfer. **No instance is provided** (the honest
   §3b-cond form): downstream results take `[QouPNeqNp decisionCost chiResidual]`
   as an explicit hypothesis, so the assumption is visible in every signature.
   History: earlier revisions carried a fabricated `⟨0, rfl⟩` instance (bean
   `cj2b6`, sign-backwards) and then a **named `axiom`** discharging the instance
   (`conj_qou_p_neq_np_faithful`). The axiom + global instance made
   `qou_implies_p_neq_np_at_chi` *look unconditional* (its axiom-dependence hidden
   from the signature, visible only via `#print axioms`) — the "Axiomatization is
   NOT a Proof" pattern (AGENTS.md). **Both are removed here.** The transfer is a
   class hypothesis, never an axiom, never an instance.

2. **The chippable kernel** — two proved lemmas in the sibling module
   [`ObstructionGenericity`](ObstructionGenericity.lean) formalising *why* a
   concrete non-vanishing $\chi(A) \neq 0$ cannot by itself discharge the
   conjecture.

**Concrete target (no longer opaque).**  Earlier `PNeqNPInQOU` was an `opaque`
nullary `Prop` — a token disconnected from the framework's own content-bearing
cost predicates. It is now the concrete statement *the QOU decision-cost family
is not polynomially bounded*, `¬ FamilyPolyBounded decisionCost`
(`CountingModuliGrade`): "no uniform `c·nᵏ` bounds the decision cost at every
moduli point." This is **not** an axiomatisation of literature $\mathrm{P}$/
$\mathrm{NP}$ (Mathlib has none, and asserting one would launder — AGENTS.md);
it is the framework's *own*, falsifiable, QOU-scoped separation, wired to the
same `FamilyPolyBounded` infrastructure the counting axis proves super-poly
(`CountingModuliGrade.physical_point_hard`). The counting→decision *transfer*
from `res ≠ 0` to this remains the open conjecture (`faithful`).
-/

namespace QOU.Information

variable {M : Type*}

/-- **The QOU-scoped decision separation** — *the decision-cost family is not
    polynomially bounded*, `¬ FamilyPolyBounded decisionCost`.

    Read as "$\mathrm{P} \neq \mathrm{NP}$ *in the QOU*": no single `c·nᵏ`
    dominates the QOU decision cost at every moduli point.  This is the
    framework's own concrete, falsifiable separation — **not** an axiomatised
    literature $\mathrm{P}$/$\mathrm{NP}$ (Mathlib has none; asserting one would
    launder, AGENTS.md §Axiomatization is NOT a Proof).  It is wired to the same
    `FamilyPolyBounded` predicate the *counting* axis proves super-poly
    (`physical_point_hard`); the open content is the counting→decision transfer
    (`QouPNeqNp.faithful`), never this target's meaning. -/
def PNeqNPInQOU (decisionCost : M → ℕ → ℕ) : Prop := ¬ FamilyPolyBounded decisionCost

/-- **The derived obstruction residue** $\mathrm{res}_{\mathcal{R}}(\chi(A))$
    at the substrate.  The corpus derives the scalar value $\chi(A) = -6$
    (`ex:chi-minus-six-derivation`, `prf:qou-obstruction-reduction`) with
    no computational-complexity input. -/
def chiResidual : ℝ := -6

/-- **Non-vanishing of the residue — derived by definition, not conjectural.**
    $\chi(A) = -6 \neq 0$; this leg of the conjecture is an axiom consequence,
    so the open content is entirely the faithfulness (below). -/
theorem chiResidual_ne_zero : chiResidual ≠ 0 := by
  change (-6 : ℝ) ≠ 0; norm_num

/-- **Conjecture (P ≠ NP in the QOU), §3b-cond carrier.**

    *Given a QOU* with substrate parameter
    $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$, the QOU decision-cost family
    is not polynomially bounded ([`PNeqNPInQOU decisionCost`]).  The statement is
    **conditional on the QOU**: an instance of this class is the hypothesis "the
    QOU's obstruction faithfulness holds", and only *from it* is the separation
    derived — never a bare $\mathrm{P} \neq \mathrm{NP}$.

    Non-degenerate (§3b-tax): the class carries the **faithfulness implication**
    (a genuine sub-hypothesis — the counting→decision transfer), not the
    conclusion directly.  `residual` is a parameter (a `Prop`-class cannot hold
    ℝ data); the QOU application fixes it to the derived `chiResidual`.

    **No instance is provided** — `faithful` is the open conjecture (the transfer
    no known result supplies), so downstream results carry `[QouPNeqNp …]`
    explicitly. -/
class QouPNeqNp (decisionCost : M → ℕ → ℕ) (residual : ℝ) : Prop where
  -- Witness: computations/none
  /-- **Faithfulness (the open conjecture).**  *In the QOU*, a surviving
      obstruction residue forces the QOU-scoped decision separation (the decision
      cost is not poly-bounded).  This single implication is the irreducible
      content of `conj:qou-p-neq-np`; it needs a counting$\to$decision transfer
      no known result supplies. -/
  faithful : residual ≠ 0 → PNeqNPInQOU decisionCost

/-- **Given a QOU, P ≠ NP in that QOU (conditional on the hypotheses).**
    Composes the faithfulness of a QOU instance with a non-vanishing residue;
    the conclusion `PNeqNPInQOU decisionCost` is explicitly QOU-scoped — never
    an unconditional $\mathrm{P} \neq \mathrm{NP}$. -/
theorem qou_implies_p_neq_np {decisionCost : M → ℕ → ℕ} {r : ℝ}
    [Q : QouPNeqNp decisionCost r] (hr : r ≠ 0) :
    PNeqNPInQOU decisionCost :=
  Q.faithful hr

/-- **The QOU-scoped separation at the derived residue.**  Specialises
    `qou_implies_p_neq_np` to the derived value $\chi(A) = -6$: given a QOU (a
    hypothesis `QouPNeqNp decisionCost chiResidual`), the decision cost is not
    poly-bounded.  No non-vanishing hypothesis is needed — it is discharged by
    `chiResidual_ne_zero`.  **The `[QouPNeqNp …]` hypothesis is explicit**: this
    theorem is genuinely conditional (no axiom, no auto-resolving instance). -/
theorem qou_implies_p_neq_np_at_chi (decisionCost : M → ℕ → ℕ)
    [QouPNeqNp decisionCost chiResidual] : PNeqNPInQOU decisionCost :=
  qou_implies_p_neq_np chiResidual_ne_zero

/-- **Explicit witness of polynomial-bound violation at $\chi(A) = -6$.**
    For every candidate polynomial budget $c \cdot n^k$, there exist a moduli
    point $m \in M$ and an input size $n \in \mathbb{N}$ where
    `decisionCost m n` strictly exceeds $c \cdot n^k$. -/
theorem exists_exceeds_poly_at_chi (decisionCost : M → ℕ → ℕ)
    [QouPNeqNp decisionCost chiResidual] (c k : ℕ) :
    ∃ m n, c * n ^ k < decisionCost m n := by
  have hnot : ¬ FamilyPolyBounded decisionCost :=
    qou_implies_p_neq_np_at_chi decisionCost
  unfold FamilyPolyBounded at hnot
  push_neg at hnot
  exact hnot c k

/-- **Inhabitation depends on the decision-cost family.**
    The identically-zero decision cost is uniformly bounded by $0 \cdot n^0$,
    so `QouPNeqNp` is refuted at the zero cost family. -/
theorem not_qouPNeqNp_of_const_zero :
    ¬ QouPNeqNp (fun (_ : M) (_ : ℕ) => 0) chiResidual := by
  intro h
  have hsep : ¬ FamilyPolyBounded (fun (_ : M) (_ : ℕ) => 0) :=
    @qou_implies_p_neq_np_at_chi M (fun _ _ => 0) h
  exact hsep ⟨0, 0, fun _ _ => Nat.zero_le _⟩

end QOU.Information
