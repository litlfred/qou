---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-007-1-the-set-y-s2-r1-is-a-monotone-union-of-sets
section_title: "The set Y ∩ S[2, r1) is a monotone union of sets,"
section_number: 1
pages: 7-8
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
doc_brief: "Möbius Energy of Thick Knots Eric J. Rawdon 2 — The M¨ obius energy of a knot is an energy functional for smoot h curves based on an idea of self-repelling."
---
each with measure < ν 1. Thus, µ(Y ∩ S[2, ρ1)) ≤ ν1. On the other hand,
Y ∩ S(r′
1, ∞) is a monotone union of sets, each with measure < µ (Y ) − ν1.
Thus, µ(Y ∩ S(ρ1, ∞)) ≤ µ(Y ) − ν1, so µ(Y ∩ S[2, ρ1]) ≥ ν1.
7
Using Lemma 6, we extract a subset of Y ∩ S[ρ1] whose measure is whatever
µ(Y ∩ S[2, ρ1)) may lack to make ν1, and let W1 be the union of this set with
Y ∩ S[2, ρ1).
To continue the induction, let Y1 = Y − W1. Note Y1 ⊆ Y ∩ S[ρ1, ∞).
Suppose ρ1, · · · , ρj−1 and W1, · · · , Wj−1 have been chosen as required in the
statement of the lemma and the set Yj−1 = Y −(W1 ∪· · ·∪Wj−1) ⊆ S[ρj−1, ∞).
Note that since W1, · · · , Wj−1 ⊆ Y ∩ S[2, ρj−1], Y ∩ S(ρj−1, ∞) ⊆ Yj−1. So for
any ρ, ρ′ with ρj−1 < ρ < ρ ′, we have Yj−1 ∩ S[ρ, ρ′] = Y ∩ S[ρ, ρ′].
Now proceed much like the initial case. If j = m, we ﬁnish by taking Wj = Yj−1
and ρm as above.
There are two cases: If µ(Yj−1 ∩ S[ρj−1]) ≥ νj, then let Wj be a subset of
Yj−1 ∩ S[ρj−1] of measure νj, ρj = ρj−1, and Yj = Yj−1 − Wj.
Suppose now µ(Yj−1 ∩ S[ρj−1]) < ν j. Deﬁne
Rlow = {ρ : µ(Yj−1 ∩ S[ρj−1, ρ]) < ν j}
and rj = sup(Rlow). Similarly, let
Rhigh = {ρ : µ(Yj−1 ∩ S[ρj−1, ρ]) ≥ νj}
and let r′
j = inf( Rhigh). Here Rlow ⁄= ∅ because ρj−1 ∈ Rlow and Rhigh ⁄= ∅
because ρm ∈ Rhigh.
As in the initial case, we have rj = r′
j, and we deﬁne ρj = rj = r′
j. Also,
µ(Yj−1 ∩ S[ρj−1, ρj)) ≤ νj and µ(Yj−1 ∩ S[ρj−1, ρj]) ≥ νj.
Let Wj be the union of Yj−1∩S[ρj−1, ρj) with a subset of Yj−1∩S[ρj] of however
much additional measure is needed to reach νj. Finally, let Yj = Yj−1 − Wj.
Note then Yj ⊆ Y ∩ S[ρj, ∞). ✷
