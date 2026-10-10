---
# qou-qk51
title: 'GAP: degLex_wellOrdered proof strategy is unsound -- List.Lex is not well-founded (axiom 1)'
status: completed
type: task
priority: normal
created_at: 2026-08-17T22:44:34Z
updated_at: 2026-08-18T20:58:40Z
---

Found by the ch1+ch2 elaboration sweep (qou-n4jv), 2026-08-17.
Audit: docs/audits/2026-08-17-ch1-ch2-lean-sibling-elaboration-sweep.md (F6).

File: quantum-observable-universes/braiding-induced-ordering.lean
Decl:  QOU.degLex_wellOrdered (n : N) : WellFounded (DegLex (alpha := Fin n))

THIS IS NOT A STALE-NAME REPAIR. The strategy cannot work.

The proof embeds into N x_lex List (Fin n) via w -> (w.length, w) and applies
WellFounded.prod_lex, which needs BOTH components well-founded. The second is
not well-founded:

    [0,1] > [0,0,1] > [0,0,0,1] > ...  descends forever
    (each step: Lex.cons down to Lex.rel with 0 < 1)

so List.Lex (.<.) on List (Fin n) is NOT well-founded for n >= 2.

The THEOREM IS TRUE -- length strictly decreases, or is equal and there are
only finitely many words of that length. Suggested route: encode into N x_lex N
    encode [] = 0 ; encode (a :: l) = a * n^(l.length) + encode l
    lemma: w.length = L -> encode w < n^L          (bound)
    lemma: Lex w w' -> w.length = w'.length -> encode w < encode w'
then DegLex is a subrelation of InvImage (Prod.Lex (<) (<)) under
w -> (w.length, encode w), and Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf closes it.

Already fixed in the same file (do not redo): Prod.lex_wf -> WellFounded.prod_lex,
and lex_append_suffix was written from scratch (Mathlib has only the common-PREFIX
List.Lex.append_left; the suffix version is FALSE without equal lengths --
w=[], w'=[0], v=[1] gives Lex [1] [0,1], false -- which is why
degLex_admissible_lex carries hlen).

WHY THIS MATTERS BEYOND ONE FILE: degLex_wellOrdered is the Lean content of
AXIOM 1 (temporal braiding) -- the axiom that makes time an ordering rather
than a coordinate. quantum-universe-axiom-motivation.md justifies it with
'what makes a before is that the reduction stops'. That currently rests on a
proof that does not compile and could not compile as written.
