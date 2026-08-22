---
# qou-3quc
title: 'GAP(lean): general-n Molien/fake-degree q-analogue -- concrete n<=4 proved, general blocked on #SYT + coinvariant grading'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:13:18Z
updated_at: 2026-08-21T21:43:00Z
---

OPENED 2026-08-21 alongside the concrete cases, per AGENTS.md "if you cannot
close a derivation, CREATE A BEAN" -- not faked with a sorry.

PROVED (content/quantum-observable-universe/lean/QOU/MathlibExt/MolienFakeDegree.lean,
sorry-free, axioms [propext, Classical.choice, Quot.sound]):

    sum_{lam |- n}  f^lam * q^(-kappa_lam) * qDim q lam  =  qFactorial q n

for n = 2, 3, 4, plus the contrast sum_qDim_sq_ne_qFactorial_n3_at_two showing
sum_lam qDim^2 != qFactorial (33/4 vs 105/8 at q=2) -- which is the Z(n) defect in
its smallest exact form, and is what makes the identities non-vacuous.

OPEN: the general-n statement. Blockers, in order:
  1. f^lam as #SYT in Lean. Mathlib v4.24.0 has YoungDiagram and Nat.Partition but
     NO hook lengths, arms, legs, standard/semistandard tableaux, or hook-length
     formula (probed by name, all absent). This corpus supplies Partition.hookLength
     and qDim itself, so the missing piece is the SYT count and its hook formula --
     already tracked by qou-8dhg (numSYT_mul_hookProduct), qou-phl4
     (YoungTableauStandard 3 cited sorries) and qou-apqw. DO NOT duplicate those;
     this bean depends on them.
  2. The graded decomposition of the coinvariant algebra (Chevalley/Steinberg) --
     the actual content of the identity. Nothing in Mathlib or the corpus.
  3. Partitions of n as a Finset with the induction needed to sum over them.

METHOD NOTE for whoever picks this up: qDim on a CONCRETE partition reduces by rfl
to qFactorial / prod_cells qBracket (hookLength ...), which is how the bridge lemmas
in that file are proved. The identity then falls to
`simp only [bridges, qFactorial]; norm_num [qBracket]; field_simp; ring`. That will
not scale to general n -- it is per-partition -- but it is the right shape for
extending the concrete range cheaply (n = 5, 6 are mechanical).

DISCARDED APPROACH, recorded so it is not retried: an earlier draft introduced its
own balQInt/balQFact. Discarded on finding qBracket is DEFINITIONALLY the same
object. A second q-bracket would be exactly the divergence surface qou-m7py removed
from the Rust engine.

SIDE OBSERVATION (not fixed here): qDim/qBracket are R-specialised upstream in
QPartitionCombinatorics although purely algebraic -- AGENTS.md section 7c would
prefer a generic {R : Type*} [Field R]. The statements in MolienFakeDegree.lean are
over R only because they inherit it.


CORRECTION 2026-08-21 (same day): this bean's blocker list was WRONG on its first
item, and it is the third time in this arc that I claimed the corpus lacked
machinery it already has.

Blocker 1 said 'f^lam as #SYT in Lean ... missing'. IT IS NOT MISSING.
QOU/Mathlib/SYTEnumerationFintype.lean (760+ lines, namespace QOU.Mathlib.SYTEnum)
supplies numSYTenum -- KERNEL-COMPUTABLE, a `by decide` proof evaluates it -- plus
numStandardYoungTableaux and the bridge numSYTenum_eq_numStandardYoungTableaux.
I had probed MATHLIB by name, found nothing, and never grepped the corpus's own
Lean tree.

CONSEQUENCE, now landed: MolienFakeDegree.lean no longer carries hand-typed f^lam
literals. The identity theorems read (numSYTenum [2,1] : R) etc., and the kernel
computes the count. Previously a mis-counted f^lam would have yielded a TRUE
theorem about a WRONG coefficient; that failure mode is now closed. The numSYT_*
lemmas depend on [propext] alone, confirming decide is doing genuine finite
computation rather than masking anything (AGENTS.md permits decide exactly for
a genuinely decidable finite computation).

REVISED remaining blocker -- narrower than 'hook-length theory':
  * the graded decomposition of the coinvariant algebra (Chevalley/Steinberg),
    which is the actual mathematical content of the identity. Nothing in Mathlib
    or the corpus.
  * an induction over Finset-many partitions of n.
The dependency on qou-8dhg / qou-phl4 / qou-apqw is therefore WEAKER than stated:
those sharpen the SYT layer, but the general-n proof is not waiting on them.

PATTERN WORTH RECORDING: three times this arc I wrote 'the corpus lacks X' after
checking only the obvious upstream -- the Webster-Williamson citation (it was
cited), qBracket (it existed, definitionally identical to my draft's balQInt),
and now #SYT. Grep content/**/*.lean before writing a scope note.
