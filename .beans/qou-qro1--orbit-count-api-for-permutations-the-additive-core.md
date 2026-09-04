---
# qou-qro1
title: 'Orbit-count API for permutations: the additive core, and the one classical lemma Mathlib lacks'
status: completed
type: task
priority: normal
created_at: 2026-09-04T02:38:34Z
updated_at: 2026-09-04T10:16:15Z
---

Owner-directed (2026-09-04), successor to qou-zrx2 follow-up (5). ClassicalTraceFloor and LeadingOrderTraceCoefficient take c(sigma_free)=2A and c(sigma_atom)=A+1 as stated hypotheses because Mathlib has no orbit-count API and no transposition-step lemma. QOU/MassTheory/OrbitCount.lean supplies the API: orbitDefect = #support - card cycleType (additive, unlike the count), proved additive over disjoint products and over lists; orbitDefect_swap = 1; sign = (-1)^orbitDefect, so the transposition step's PARITY is proved free. The FREE half of ClassicalTraceFloor's hypotheses is now closed outright (orbitCount_prod_of_disjoint_unit_defect: A disjoint blocks of defect 1 on 3A strands leave 2A orbits). REMAINING: the magnitude |Delta| <= 1 of the transposition step, which reduces via cycleOf splitting to the two-cycle JOIN -- Mathlib has the split direction (IsCycle.swap_mul) but not the merge. Carried as two sorry + -- Ref: [manuscript] per the state-and-queue disposition; consumed by nothing.


COMPLETED 2026-09-04. OrbitCount.lean is SORRY-FREE; lean-direct exit 0 (4.8 s),
`#print axioms` on all five public results = [propext, Classical.choice,
Quot.sound], no sorryAx. Commit 323916b05d3 on
claude/orbit-count-swap-lemma-2026-09-04 (PR #6568).

THE BODY ABOVE HAS TWO WRONG CLAIMS; recording them because both misdirected
the attack:

1. "reduces to the two-cycle JOIN -- Mathlib has the split direction
   (IsCycle.swap_mul) but not the merge" is BACKWARDS. The MERGE is the free
   half: it is derived in four lines from the split plus (R), because
   swap a b is an involution. What Mathlib has is not "the split direction"
   but only its ADJACENT case (b = f a, one arc a single point). The general
   split was the whole problem.
2. Mathlib has no lemma about cycleType (swap _ _ * _) ANYWHERE -- zero hits
   across the library. So no amount of searching was going to shorten this.

WHAT ACTUALLY WORKED, and it is not the plan the earlier docstring recorded:
* (S-adj) orbitDefect_swap_apply_mul, the adjacent case. Split
  f = cycleOf f a * (f * (cycleOf f a)^-1) into disjoint halves via
  disjoint_mul_inv_of_mem_cycleFactorsFinset; the transposition cannot leave
  the first half, so orbitDefect_mul_of_disjoint reduces to ONE cycle, where
  IsCycle.swap_mul + support_swap_mul_eq finish it.
* orbitDefect_swap_mul_aux, the arc induction. b = sigma^k a for least k >= 1;
  each step peels the front letter of the arc off with (S-adj) and puts it back
  at the far end with (S-adj) again, glued by the three-cycle identity
  swap (sa) b * swap a (sa) = swap a (sa) * swap a b. One base case, reached
  twice per step. Crucially it never uses the merge lemma, which would have
  been circular.
The WITHDRAWN plan was to construct the two arc-cycles of the split explicitly
via cycleFactorsFinset. That needs an edge case at each end of the arc (k=1 and
k=L-1, where one arc is a single point and the corresponding factor is trivial);
the induction avoids all of it.

STILL NOT DISCHARGED, and the file's docstring now carries this in its own
section: the ClassicalTraceFloor counts. Knowing every letter moves the orbit
count by +-1 leaves the bookkeeping of WHICH sign each letter of the canonical
word takes -- whether its two strands already lay in one orbit. That is a fact
about the specific word, not about permutations, and it is not in this file.
Do not cite OrbitCount.lean as verifying c(sigma_atom) = A + 1.


FOLLOW-UP TARGET, sharpened 2026-09-04 while checking the PR against main
(158 commits later; ClassicalTraceFloor.lean still present and unchanged in
shape). Its atom-count hypothesis is phrased

    hmerge : cFree = cAtom + (A - 1)

i.e. 'each of the A-1 interfaces merges one pair'. That is LITERALLY A-1
applications of orbitDefect_swap_mul_of_not_sameCycle, the merge lemma this
bean proved. So the word-specific accounting that OrbitCount.lean deliberately
does NOT do is now a concrete induction over the A-1 interface letters, with
the per-letter step already in hand; what has to be supplied per letter is the
side condition -- that the letter's two strands were NOT already in one orbit
(¬ SameCycle), which is the hypothesis the merge lemma takes.

That is a statement about the canonical word, not about permutations, and it
belongs in a fresh bean rather than reopening this one. Not claimed here.
