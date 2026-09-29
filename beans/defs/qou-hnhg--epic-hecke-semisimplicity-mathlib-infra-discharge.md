---
# qou-hnhg
title: 'EPIC: Hecke-semisimplicity Mathlib infra — discharge WenzlCriterion (genericity⇒semisimple) end-to-end'
status: in-progress
type: epic
priority: normal
created_at: 2026-07-24T16:21:37Z
updated_at: 2026-07-24T16:28:03Z
---


PROGRESS 2026-07-24 (session): TRACK 3 COMPLETE + verified sorry-free.
- B1 (qou-6566): QIntegerFactorial.lean — q-integers/factorial/genericity iff/positivity. DONE.
- B3c (qou-ubz8): TraceNilpotent.lean — regTraceForm, trace kills nilpotents. DONE.
- B3a/B3b/B3d (dwxh/vh5o/u181): TraceFormSemisimple.lean — the KEYSTONE proven:
    isSemisimpleRing_of_regTraceForm_nondegenerate : nondegenerate regular trace form
    ⟹ IsSemisimpleRing A (fin-dim K-algebra). Trace-cyclicity sidesteps two-sided ideal.
  DONE. Abstract half of Wenzl's criterion is now a THEOREM, not a citation.
REMAINING: Track 5 arithmetic feeders (B5a-d, tractable) + Track 2 the big lift —
define H_n(q) (B2a-e; no Hecke algebra in Mathlib) then B2f instantiate track3 at the
Markov trace form ⟺ [n]_q!≠0. Track 2 is a genuine multi-session build; best as a
fresh focused effort. WenzlCriterion discharge = B2f (blocked only on track 2 now).
