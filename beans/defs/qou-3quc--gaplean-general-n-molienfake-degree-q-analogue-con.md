---
# qou-3quc
title: 'GAP(lean): general-n Molien/fake-degree q-analogue -- concrete n<=4 proved, general blocked on #SYT + coinvariant grading'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T21:13:18Z
updated_at: 2026-11-17T12:24:25Z
parent: qou-1oif
---

OPENED 2026-08-21 alongside the concrete cases, per AGENTS.md "if you cannot
close a derivation, CREATE A BEAN" -- not faked with a sorry.

PROVED (folio/quantum-observable-universe/lean/QOU/MathlibExt/MolienFakeDegree.lean,
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

2026-08-29 Molien->binding hook (probe molien_binding_signed_dimension_probe.py, exact sympy, S3+S4 pass): the PROVED binding signed dims Delta_lambda=(-1)^{n(lambda)} dim V_lambda are read off the SAME M_nu(u,t) as the weights, at the fake-degree edge t=0: fd_lambda(u)=M_nu(u,0)*prod_{i=2}^n(1-u^i), n(lambda)=u-valuation, dim=fd(1). Weights at (u=q^2,t=qz/W); binding signed-dims at (u,t=0). Whole B=Sum y chi Delta is one bigraded Molien object read at two corners. HONEST: needs the FULL coinvariant denominator (reduced numerator gives dim=1 for all lambda -- corrected). Does NOT touch the open binding MAGNITUDE (extensive M_n(K) term). forall-n still open. Nothing wired.

## 2026-08-29 — general-n REDUCTION landed (sorry-free), gap re-scoped precisely

New uncommitted file: folio/quantum-observable-universe/lean/QOU/MathlibExt/MolienFakeDegreeGeneralN.lean
(lean-direct exit 0; axioms [propext, Classical.choice, Quot.sound] — no sorryAx).

PROVED sorry-free, GENERAL n, over the canonical Fintype Nat.Partition n (same index as RSKBurnsideHolds):
 - hookProd + qDim_eq_qFactorial_div: qDim q lam = [|lam|]_q!/prod[h_x]_q, by rfl, generic [Field R].
 - molienSum_eq_qFactorial_mul_normalized: molienSum n q = [n]_q! * normalizedSum n q. The genuine
   content-bearing step: uses PartitionListBridge.toList_sum ((toList p).sum = n) so every partition of
   n shares the SAME [n]_q! numerator, which is what lets it factor out.
 - molienSum_eq_qFactorial_iff (1<q): molienSum n q = [n]_q!  <->  normalizedSum n q = 1.
   Isolates the mathematical content into ONE normalized identity.

GAP re-scoped (the two prior blockers are RESOLVED as blockers, only the deformation content remains):
 - #SYT: done (SYTEnum). Finset-induction over partitions: done in corpus (PartitionsOfBridge /
   Nat.Partition Fintype; sum_map_partitionsOf). The classical q=1 face Sum (f^lam)^2 = n! is proved
   general-n (QOU.Mathlib.rskBurnsideHolds, sorry-free, via Robinson-Schensted).
 - REMAINING open content = normalizedSum n q = 1 for general n (the q-deformation away from q=1).
   Two routes, NEITHER in Mathlib v4.24.0: (1) coinvariant-algebra graded Poincare = [n]_q! with
   fake-degree graded multiplicities (needs graded S_n-module Poincare API + coinvariant algebra +
   fake-degree=graded-mult theorem); (2) maj-Mahonian [n]_q! = Sum_w q^maj(w) + q-RSK + fake-degree =
   Sum_T q^maj(T). Genuine multi-week formalization; not a one-line lemma. Bean stays OPEN.

NOT taken (documented in the file): the mechanical faithfulness bridge molienSum n = concrete LHS via
sum_map_partitionsOf + dimSYT_eq_numSYTenum — blocked only by the un-cached SchenstedRSKBurnside olean
chain (from-source build), touches none of the open content.

## 2026-08-29 CORRECTION (same session) — the reduction was ALREADY committed; I duplicated it

The note just above overstated my contribution. MolienFakeDegreeGeneralN.lean was NOT new: commit
53f42206c8 ('lean(3quc): general-n Molien/fake-degree REDUCTION') on THIS branch already committed the
exact reduction theorems (hookProd, qDim_eq_qFactorial_div, molienSum/normalizedSum,
molienSum_eq_qFactorial_mul_normalized, molienSum_eq_qFactorial_iff, normalizedSum_iff_molien),
sorry-free. I independently re-derived a near-identical file WITHOUT knowing it existed, my Write
overwrote it, then I restored it via git checkout so as not to clobber the prior theorem.

Net verified outcome of THIS session:
 - Independently reproduced + re-verified the committed reduction is correct and sorry-free (lean-direct
   exit 0; axioms [propext, Classical.choice, Quot.sound], no sorryAx). Confirmation value only.
 - Added ONE additive doc paragraph (uncommitted, +11 lines) naming the exact faithfulness-bridge route
   (PartitionsOfBridge.sum_map_partitionsOf + SYTEnum.dimSYT_eq_numSYTenum) and why it is unbuilt here
   (SchenstedRSKBurnside olean chain not in lake-cache).
 - No new theorem proved. The real gap (normalizedSum n q = 1 general n; the q-deformation) is UNCHANGED
   and remains a multi-week Mathlib project via coinvariant-algebra Poincare OR maj-Mahonian+q-RSK,
   neither in Mathlib v4.24.0.

2026-08-29: general-n gap SHARPENED via induction route (qou-x4zl). normalizedSum n q=1 reduced (sorry-free, MolienFakeDegreeInduction.lean) to the one-step recursion normalizedSum(n+1)=normalizedSum(n), then to the addable-box hook identity (B) [verified n<=6] + SYT branching (A) [corpus infra exists]. (B) is more elementary than the coinvariant/maj-RSK routes -- no rep theory. Remaining: prove (B) in Lean (q-JM contents) + the Nat.Partition addable-box reindexing.

2026-08-29 CLOSED (math) via corpus telescope, NOT open: normalizedSum n q = 1 follows from MacdonaldTelescopeGeneralX.telescope_generalX at X=0. Convention bridge (exact n<=5): q^-kappa/hookProd_q(lam) = jonesMarkovCoeff(q^2,0,lam) = schurElement(q^2,0,lam)*(1-q^2)^n; telescope@X=0: Sum f schurElement(q^2,0) = (1/(1-q^2))^n; chain = 1. Per-cell 1-q^2h = -q^h(q-q^-1)[h]_q; n-stat identity kappa = Sum h - n - 2 n(lam). Probe fake_degree_via_telescope_probe.py 3/3. So NOT multi-week coinvariant/maj-RSK. Remaining = MECHANICAL Lean bridging (convention foldl + Nat.Partition<->YoungDiagram carrier). Audit 2026-08-29-normalizedsum-closes-via-telescope.md.


UPDATE 2026-08-29 (PR #6011): the telescope closure is now assembled and VERIFIED
sorry-free in Lean. normalizedSum_eq_one_of_convBridge (NormalizedSumClosure.lean)
compiles lean-direct exit 0; #print axioms = [propext, Classical.choice, Quot.sound],
no sorryAx. Carrier reindex (CarrierReindexBridge.lean) + per-cell brick
(one_sub_qsq_pow_eq, #5975) also sorry-free.

The general-n statement's three original blockers (#SYT, coinvariant grading,
q-RSK) are BYPASSED: the corpus general-X Macdonald telescope (telescope_generalX,
#5970) closes it at X=0 via the (Q=q^2, X=0) convention bridge. Math CLOSED (probe
exact n<=5). The ONE remaining unproved Lean input is that per-lambda convention
bridge hconv itself (q^(-kappa)/hookProd = schurElement(q^2,0)*(1-q^2)^n), carried
as an explicit hypothesis (NOT a sorry). It reduces to the n-statistic identity
kappa = sum h - n - 2 n(lambda) + foldl chaining of the per-cell brick -- mechanical,
no open combinatorics. Follow-up bean for hconv if pursued.


UPDATE 2026-09-03 (PR #6447, branch claude/hconv-convention-bridge-2026-09-03):
the ENTIRE COMBINATORIAL CORE of hconv is now proved sorry-free in
QOU/MathlibExt/ContentSumNStatistic.lean. Two milestones:

1. contentSum lambda = n(lambda') - n(lambda) (was only a prose comment at
   QPartitionCombinatorics def nLambda). Via cell_fubini column-regrouping.
2. THE n-STATISTIC IDENTITY, in the Partition.hookLength encoding hconv needs:
   contentSum lambda = (Sum_cells Partition.hookLength) - |lambda| - 2 nLambda lambda.
   Combines (1) with HookSumComplete.hookSum_eq (Sum h = n' + n + |lambda|), plus a
   new colLen-register bridge hsc_colLen_eq (proved by induction) reconciling
   HookSumComplete's row-index-card colLen with IdentityI's list-value colLen.

All lean-direct exit 0; axioms = propext/Classical.choice/Quot.sound (no sorryAx).

REMAINING for hconv: ONLY the sign/monomial foldl aggregation (piece 3). The
worked algebra (audit 2026-08-29): schurElement(q^2,0,lambda)*(1-q^2)^n =
q^{2 nLambda + |lambda| - Sum h}/hookProd, using the per-cell brick
one_sub_qsq_pow_eq (already sorry-free) chained over the nested foldl of
schurElement/hookProd + (1-q^2)/(q-q^-1) = -q; then substitute the n-statistic
identity to get q^{-contentSum}/hookProd = hconv. This is the laborious nested-
foldl product bookkeeping over R (signs (-1)^n, q^{Sum h}, (q-q^-1)^n powers);
no open combinatorics remain, only mechanical algebra.


UPDATE 2026-09-03 (PR #6447) -- LEAN SIDE CLOSED, UNCONDITIONALLY.
Piece 3 (the sign/monomial foldl aggregation) is proved sorry-free, and wired in:

- HconvConventionBridge.hconv (new, sorry-free): for sorted l and 1 < q,
  q^(-contentSum l)/hookProd q l = schurElement(q^2,0,l)*(1-q^2)^(l.sum).
  Via denomProd_factor (prod_x (1-q^2h) = (-1)^|l| q^Sum_h (q-q^-1)^|l| hookProd,
  cell-by-cell with the per-cell brick one_sub_qsq_pow_eq), schurElement_zero_eq,
  (1-q^2)=-q(q-q^-1), and the n-statistic identity contentSum = Sum_h -|l| -2n(l).

- NormalizedSumUnconditional.normalizedSum_eq_one (new, sorry-free):
    (n : Nat) (q : R) (hq : 1 < q) : normalizedSum n q = 1
  Discharges the last hypothesis of NormalizedSumClosure.normalizedSum_eq_one_of_convBridge
  (#6011) with hconv on the sorted carrier toList p; supplies hq2, hgen from 1 < q.

#print axioms normalizedSum_eq_one = [propext, Classical.choice, Quot.sound] (no sorryAx).
The general-n q-analogue fake-degree identity normalizedSum n q = 1 is now
machine-verified for every n, every 1 < q, with NO hypotheses beyond the substrate
regime. The math (probe exact n<=5) AND the Lean are both closed. Nothing open remains
on qou-3quc's Lean side; the induction/(B) route (qou-x4zl/qou-ognw) remains an
independent second proof.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Note 2026-10-10 (independent route, not a closure)

An independent second route to the nonnegativity of `[n]_Q!/c_λ` now exists:
`QOU.Mathlib.MajFormula.qFactorial_eq_schurElt_mul_fmaj` writes it as `Σ_{T∈SYT(λ)} Q^{maj T}`
(`coeff_fmaj_nonneg`), and `QOU.Mathlib.MajSYTBridge.fmaj_eval_one` ties the count at `Q = 1` to
`numStandardYoungTableaux`. Status of this bean is left unchanged (not this thread's arc).

NOTE 2026-11-15 (thread "Polish the paper's exposition"): the general-n statement now exists as
QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial (n : ℕ) (q : ℝ) (hq : 1 < q),
via normalizedSum_eq_one and molienSum_eq_qFactorial_iff; source grep finds no `sorry` in its
import cone (MolienFakeDegreeGeneralN, WenzlSchurElement hits are docstring words only). Not
lean-direct verified in this session, so the bean is NOT closed here -- the next step is a
lean-direct run on NormalizedSumUnconditional.lean, then close. AGENTS.md updated to say proved.

## Progress 2026-11-17 (Round 66 — PR #8340)

- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/AddableCellRatioFakeDegreeTwoRowBallotWeightTensorPowerCharacterOrbitTrace.lean` (Lean 4.24.0, `0` `sorry`, `0` `axiom`, `0` warnings, `0` directory-mode static vacuity & borrowed-name advisories).
- 80-dps `mpmath` numerical witness stamped in `computations/probes/addable-cell-ratio-fake-degree-two-row-ballot-weight-tensor-power-character-orbit-trace.witness.json` (`scriptHash = 0309390e769d`, `scriptCommitSha = c43b700db42337a2547c8ff1e2a1665156dd27ea`, `HEAD = d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
- PR: https://github.com/litlfred/qou/pull/8340 (`ready: d46ecc77d14e0e9528cfc49310e88f4e88eb306a`).
