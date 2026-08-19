---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-014-33-let-c-be-the-set-of-conjugacy-classes-of-wn-a
section_title: "Let {C} be the set of conjugacy classes of Wn and let wC be an element"
section_number: 3.3
pages: 10-12
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
of minimal length in C which admits a decomposition as a product of negative
blocks (ordered by increasing length) followed by various positive blo cks (see
(2.4)). We can even ﬁx a unique choice of wC if we also require that the positive
Markov traces and knot invariants 11
blocks have increasing length. We then deﬁne an element gC ∈ Hn by taking
an expression wC = d1 · · ·dn (with di ∈ D i) and replacing each si by gi and
each ti by t′
i. As in (3.2) we have (with nC := nwC ) that
gwC = qnC gC + A-linear combination of elements gw with l(w) < l (wC).
A trace function on Hn is an A-linear map ϕ : Hn → A such that ϕ (hh′) =
ϕ (h′h) for all h, h ′ ∈ Hn. By [3], each trace function on Hn is uniquely deter-
mined by its values on the elements gwC , for all C. Conversely, given a set of
elements aC ∈ A, one for each conjugacy class C, there exists a unique trace
function ϕ on Hn such that ϕ (gwC ) = aC for all C. Using the above relations,
we deduce that these results on the determination of trace funct ions remain
valid when we replace each gwC by gC, for all C.
The following result will show how to reduce the computation of the va lue
of a trace function on any element to the values on elements in signed block
form.
Proposition 3.4 For each h ∈ Hn there exists a ﬁnite (non-empty) subset
I(h) ⊆ A × D′
1, 0 × . . . × D′
n, 0 such that
ϕ (h) =
∑
(r,d ∗
1,...,d ∗
n)∈I(h)
rϕ (d∗
1 · · ·d∗
n),
for all trace functions ϕ on Hn.
Proof. The result clearly holds if n = 1. Now let 1 < j ≤ n and assume that we
have already found a ﬁnite (non-empty) subset Ij ⊆ Hj ×D′
j+1,j −1×. . . ×D ′
n,j −1
such that
ϕ (h) =
∑
(hj ,d ′
j+1,...,d ′
n)∈Ij
ϕ (hjd′
j+1 · · ·d′
n),
for all trace functions ϕ on Hn. We will proceed by downward induction on j.
For j = n there is nothing to prove. We now show how to obtain an analogous
statement with j replaced by j − 1. This is done as follows.
Consider one element ( hj, d ′
j+1, . . . , d ′
n) ∈ Ij. The element hj is an A-
linear combination of basis elements gw with w ∈ Wj. By (3.2), this can
be rewritten as an A-linear combination of products r′
1 · · · r′
j with r′
i ∈ R ′
i.
Collecting terms with a ﬁxed value of r′
j, we obtain a ﬁnite (non-empty) subset
R(hj) ⊆ Hj−1 × R′
j such that
hj =
∑
(hj−1,r ′
j)∈R(hj )
hj−1r′
j.
We can write r′
j = d′
jr′′
j−1 with d′
j ∈ D ′
j and r′′
j−1 ∈ R ′
j−1 (cf. (2.1)). Now the
element r′′
j−1 either is a product of various generators g1, . . . , g j−2 or is like the
