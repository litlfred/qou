---
# qou-3quc
title: 'GAP(lean): general-n Molien/fake-degree q-analogue -- concrete n<=4 proved, general blocked on #SYT + coinvariant grading'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:13:18Z
updated_at: 2026-08-29T02:22:57Z
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

## 2026-08-29 — n=3 template established (qou-sf1t / PR pending)

The Molien<->Jones-Markov identification is now EXACT for n=3: y_lambda =
M_nu(u=q^2, t=qz/(q^2-qz-1)) * (q^2-qz-1)^2, u=q^2 FORCED by an overdetermined
elimination (not fitted). General-n is the open target this bean names. The n=4
test: does the same monomial u=q^2 and a perfect-square normaliser Z_n reproduce the
S_4 Jones-Markov weights from the general S_n Molien series? Template + Lean
(MolienJonesMarkovN3.lean) + probe (molien_jones_markov_n3_identification_probe.py)
ready to generalise. Note: the refuted f^l q^-k/[n]! form had the WRONG normaliser;
the right one is the Molien Z, so the general-n normaliser is a Poincare series.

## 2026-08-29 — general-n formula CONFIRMED at n=4 (numeric+normalization); Lean n=3 only

y_lambda(q,z) = M_nu(u=q^2, t=qz/(q^2-qz-1)) * (1+qz-q^2)^(n-1), M_nu the S_n
reflection-rep Molien series. Normaliser is a power of ONE linear form (Poincare/
Molien), not [n]_q!. n=3 Z=(1+qz-q^2)^2=(q^2-qz-1)^2 (even); n>=4 the sign matters.
n=4 (molien_jones_markov_general_n_probe.py, 3/3): Sum f^lam y_lam=1 EXACT symbolic;
at z=z_D the >=3-row weights vanish (two-row cap) and survivors match corpus
y_lambda_su_n(4,q0,2) SU(2) q-dims to <1e-14.
LEAN STATUS: n=3 sorry-free (general z, MolienJonesMarkovN3.lean). n=4 needs the
INDEPENDENT general-z H_4 weights as polynomials for a ring proof (only have z=z_D
corpus pin + exact normalization). forall-n Lean = abstract S_n Molien + H_n Markov
machinery, a real formalization project = THIS BEAN. Nothing wired.
