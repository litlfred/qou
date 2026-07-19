---
# qou-svnb
title: 'F4 option-2: prove abstract cyclic_iff_gram_symm reduction; refactor trM_cyclic into proved-reduction + scoped Gram residual'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T03:00:12Z
updated_at: 2026-07-19T06:19:25Z
---


## Scope (option 2 — direct abstract sub-lemma; honest partial, NOT a closure)
Prove the abstract, Fin-24-FREE reduction lemma that cleanly isolates the hard
half of F4 cyclicity, and refactor `trM_cyclic` (QOU.Machinery.H4, PR #4046)
into [proved reduction] + [precisely-scoped finite residual sorry].

The lemma (true, general, no computation):
  For a finite free module with basis {e_i} (here Fin 24 -> R), a bilinear
  product `mulNF` and a LINEAR functional `trM`, define the Gram matrix
  `G i j := trM (mulNF (e i) (e j))`. Then
      (forall i j, G i j = G j i)  ->  forall u v, trM(mulNF u v) = trM(mulNF v u).
  i.e. cyclicity follows from symmetry of the trace-form Gram matrix.

## Why this is honest and non-vacuous
- The reduction is a REAL theorem (bilinear expansion + basis decomposition),
  provable WITHOUT touching the depth-6 whnf wall.
- It does NOT close F4: the hypothesis `forall i j, G i j = G j i` (276 concrete
  identities) still needs the blocked Fin-24 compute or a full Mathlib build.
  The residual becomes a single, precisely-stated `gram_symm` sorry - cleaner
  and reusable, but STILL a cited sorry. Label as such (no laundering: a proved
  reduction is not a proved theorem while its premise is open).

## Plan of attack (bounded - the reduction only, not the Gram residual)
1. mulNF bilinearity at Fin 24: mulNF_add_left/right, mulNF_smul_left/right.
   Right-side (in v) trivial (v are scalar coeffs). Left-side (in u): each word
   W_j is linear; test `funext i; simp [mulNF]; ring` WITHOUT unfolding mulsigma
   (keep W_j opaque) - linearity should not need depth unfolding. If it explodes,
   fall back to proving each generator linear once (mulsigmaK_add, depth-1 cheap)
   and composing.
2. Basis decomposition: u = sum_i u i . (e i) for u : Fin 24 -> R
   (Finset.sum + Pi.single; standard, cheap).
3. Prove reduction `cyclic_of_gram_symm`:
   trM(mulNF u v) = sum_{i,j} u_i v_j G_{i,j}  [bilinear expand + trM linear],
   then swap i,j using the G-symmetry hypothesis. All formal, no Fin-24 grind.
4. Refactor MarkovTraceH4: Gram i j := trM(mulNF (e i)(e j)); prove trM_cyclic
   FROM gram_symm : forall i j, Gram i j = Gram j i via the reduction. Keep
   gram_symm as the single cited sorry (residual). Net: monolithic sorry ->
   proved reduction + one scoped residual sorry.
5. Verify lean-direct exit 0. Update audit + this bean. Do NOT claim closure.

## Risk / stop conditions
- If step 1 bilinearity or step 3 reduction ALSO grind at Fin 24 (the bilinear
  expansion over 24x24 basis pairs may itself be large even without depth-6
  unfolding), record which step and STOP - do not force. Report the finding.
- The 276-entry Gram symmetry residual is explicitly OUT of scope here (blocked).

## Definition of done
`cyclic_of_gram_symm` proved sorry-free; trM_cyclic derived from it modulo the
single honestly-labelled `gram_symm` residual sorry. Stepping stone toward
option-1's abstract closure, not a substitute.

## Relationship to option-1 (qou-0vsu)
Complementary: option-2's `cyclic_of_gram_symm` is exactly the reduction the
abstract MarkovStabilization cyclic-trace lemma (option-1) supplies generically.
If option-1 lands the abstract lemma first, option-2 is subsumed. If option-2
lands first, it is the concrete-basis instance of that reduction. OK to pursue
in parallel (different route, different context).

## LANDED (2026-07-19) — reduction proved sorry-free
trM_cyclic is now DERIVED (no new sorry) from the sorry-free reduction
trM_cyclic_of_gram_symm + single residual gram_symm. All added lemmas compile
(lean-direct exit 0): mulσk_{add,smul,zero}, mulNF_{add,smul}_{left,right},
mulNF_zero_left, e, basis_decomp, mulNF_sum_{left,right}, trM_sum,
trM_mulNF_{left,right}_expand, trM_mulNF_gram, trM_cyclic_of_gram_symm.
KEY: mulNF bilinearity proved with mulσ kept OPAQUE (only linearity lemmas fire)
— never touches the depth-6 whnf wall. Sorry count unchanged (1) but content
shrank from "all cyclicity" to the finite 276-entry Gram-symmetry base
(gram_symm), still whnf-blocked. Stop-condition was NOT hit — bilinearity and
expansion did NOT grind. Honest partial as planned; not a closure. Audit updated.
