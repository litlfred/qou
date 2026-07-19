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

/-- $\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q \in \mathbb{G}_m$

    Conjectural class — see
    [`conj:qou-p-neq-np`](../../../quantum-observable-universe/information-theory/qou-p-neq-np.md). -/
class QouPNeqNp where
  -- Witness: computations/none
  /-- **Conjecture statement** (from manuscript):

      At the physical substrate parameter
$q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$
([substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)),
$\mathrm{P} \neq \mathrm{NP}$.*

*Equivalently: the resolution-tree evaluation of the universal
obstruction class $\chi(A)$ is non-vanishing:*

$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0
  \qquad\text{at } q = q_0.
$$

      The residual is the evaluated obstruction
      $\mathrm{res}_{\mathcal{R}}(\chi(A))$ at $q_0$; field schema is a
      structural placeholder pending a formalised $\chi(A)$. -/
  residual : ℝ
  /-- The residual is non-vanishing (the conjecture is the assertion
      that this holds at the substrate point). -/
  residual_ne_zero : residual ≠ 0

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.  Do NOT replace it with
-- a fabricated instance such as `⟨1, one_ne_zero⟩` (bean cj2b6:
-- audit-dodge); an arbitrary nonzero real is not the obstruction
-- residual.
-- Ref: [manuscript] quantum-observable-universe/information-theory/qou-p-neq-np.ts
noncomputable instance : QouPNeqNp := sorry

end QOU.Information
