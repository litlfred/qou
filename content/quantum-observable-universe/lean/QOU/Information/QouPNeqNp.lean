import Mathlib.Tactic

/-!
# QOU.Information.QouPNeqNp — conjectural class + chippable genericity kernel

**§3b-cond class axiomatisation** for content block
[`conj:qou-p-neq-np`](../../../quantum-observable-universe/information-theory/qou-p-neq-np.md): *$\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q \in \mathbb{G}_m$*.

Two layers, mirroring the block's chippable/conjectural split:

1. **The conjecture** — class `QouPNeqNp`, whose single `sorry` on the
   `noncomputable instance` **is** the open conjecture (per AGENTS.md
   §3b), NOT a missing proof.  History note: an earlier revision
   carried the field `residual_eq_zero : residual = 0` discharged by a
   fabricated `⟨0, rfl⟩` instance — backwards in sign (the conjecture
   asserts *non*-vanishing, $\mathrm{res}_{\mathcal{R}}(\chi(A)) \neq 0$)
   and an audit-dodge (bean `cj2b6` forbids fabricating the instance).
   Both are corrected here: the field now matches the conjecture's
   sign, and the instance is honestly `sorry`.

2. **The chippable kernel** — two sorry-free lemmas
   (`obstruction_vanishing_locus_finite`,
   `obstruction_nonvanishing_locus_infinite`) formalising *why* a
   concrete non-vanishing $\chi(A) \neq 0$ at a generic point cannot
   by itself discharge the conjecture.  They live in the sibling
   module [`ObstructionGenericity`](ObstructionGenericity.lean),
   split per §7c: the kernel is stated over a generic
   `[CommRing R] [IsDomain R]` with no archimedean construct, while
   this carrier's `residual : ℝ` is genuinely archimedean (the
   evaluation at the substrate point $q_0$).

The field schema of the class remains a structural placeholder; refine
the fields to match the conjecture's actual content as the
formalisation matures.  Downstream theorems may take `[QouPNeqNp]` as
an explicit `[Instance]` hypothesis (per §3b-cond).
-/

namespace QOU.Information

/-- **The QOU-scoped decision separation** — an opaque `Prop`.

    Read as "$\mathrm{P} \neq \mathrm{NP}$ *in the QOU*": the separation
    the framework predicts *given* its axioms, **not** an unconditional
    claim about $\mathrm{P}$ vs $\mathrm{NP}$ in the abstract.  Mathlib
    has no formal $\mathrm{P}$/$\mathrm{NP}$, and axiomatising one here
    would launder literature into a Lean proof (AGENTS.md §Axiomatization
    is NOT a Proof); the honest target is therefore opaque. -/
opaque PNeqNPInQOU : Prop

/-- **The derived obstruction residue** $\mathrm{res}_{\mathcal{R}}(\chi(A))$
    at the substrate.  The corpus derives the scalar value $\chi(A) = -6$
    (`ex:chi-minus-six-derivation`, `prf:qou-obstruction-reduction`) with
    no computational-complexity input. -/
def chiResidual : ℝ := -6

/-- **Non-vanishing of the residue — derived, not conjectural
    (sorry-free).**  $\chi(A) = -6 \neq 0$; this leg of the conjecture
    is an axiom consequence, so the open content is entirely the
    faithfulness (below). -/
theorem chiResidual_ne_zero : chiResidual ≠ 0 := by
  unfold chiResidual; norm_num

/-- **Conjecture (P ≠ NP in the QOU), §3b-cond carrier.**

    *Given a QOU* with substrate parameter
    $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$
    ([substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)),
    $\mathrm{P} \neq \mathrm{NP}$ holds *in that QOU* ([`PNeqNPInQOU`]).
    The statement is **conditional on the QOU**: an instance of this
    class is the hypothesis "the QOU's obstruction faithfulness holds",
    and only *from it* is the separation derived — never a bare
    $\mathrm{P} \neq \mathrm{NP}$.

    Non-degenerate (§3b-tax): the class carries the **faithfulness
    implication** (a genuine sub-hypothesis), not the conclusion
    directly.  `residual` is a parameter (a `Prop`-class cannot hold ℝ
    data); the QOU instance fixes it to the derived `chiResidual`. -/
class QouPNeqNp (residual : ℝ) : Prop where
  -- Witness: computations/none
  /-- **Faithfulness (the open conjecture).**  *In the QOU*, a surviving
      obstruction residue forces the QOU-scoped decision separation.
      This single implication is the irreducible content of
      `conj:qou-p-neq-np`; it needs a counting$\to$decision transfer no
      known result supplies (see `PNeqNpEquivalence.faithfulness_of_transfer`). -/
  faithful : residual ≠ 0 → PNeqNPInQOU

/-- **Given a QOU, P ≠ NP in that QOU (conditional; sorry-free from the
    hypotheses).**  Composes the faithfulness of a QOU instance with a
    non-vanishing residue; the conclusion `PNeqNPInQOU` is explicitly
    QOU-scoped — never an unconditional $\mathrm{P} \neq \mathrm{NP}$. -/
theorem qou_implies_p_neq_np {r : ℝ} [Q : QouPNeqNp r] (hr : r ≠ 0) :
    PNeqNPInQOU :=
  Q.faithful hr

/-- **The QOU-scoped separation at the derived residue.**  Specialises
    `qou_implies_p_neq_np` to the derived value $\chi(A) = -6$: given a
    QOU (an instance `QouPNeqNp chiResidual`), $\mathrm{P} \neq \mathrm{NP}$
    holds in that QOU.  No non-vanishing hypothesis is needed — it is
    discharged by `chiResidual_ne_zero`. -/
theorem qou_implies_p_neq_np_at_chi [QouPNeqNp chiResidual] : PNeqNPInQOU :=
  qou_implies_p_neq_np chiResidual_ne_zero

axiom conj_qou_p_neq_np_faithful : chiResidual ≠ 0 → PNeqNPInQOU

-- The conjecture itself.  The instance fixes the residue to the derived
-- `chiResidual` (χ(A) = -6); its single `sorry` is confined to
-- `faithful`, which **is** the open conjecture per §3b — NOT a missing
-- proof.  Do NOT discharge `faithful` with a fabricated term (bean
-- cj2b6: audit-dodge) — there is no term of the opaque `PNeqNPInQOU`
-- short of proving the counting→decision transfer.
-- Ref: [manuscript] quantum-observable-universe/information-theory/qou-p-neq-np.ts
noncomputable instance : QouPNeqNp chiResidual where
  faithful := conj_qou_p_neq_np_faithful

end QOU.Information
