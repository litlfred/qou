---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-041-113-proof-of-theorem
section_title: "Proof of Theorem"
section_number: 11.3
pages: 37-38
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
τ1(M) = 1 by the deﬁnition. We also have ev1(JM) = 1 by Lemma 10.3. Hence,
we have (11.1) in this case.
Let r ≥2. Let L be as in the last subsection. By the deﬁnition of JM, we have
evζ(JM) = evζ(JL0(ω−f1, ω−f2, . . . , ω−fm))
(11.4)
Set d = ⌊r−2
2 ⌋. It follows from Theorem 8.2 that if x1, . . . , xm ∈P and we have
xi ∈Pd+1 for some i ∈{1, . . . , m}, then we have evζ(JL(x1, . . . , xm)) = 0. Hence,
by (11.4), we have
evζ(JM) = evζ(JL0(ωr,−f1, ωr,−f2, . . . , ωr,−fm)),
38
KAZUO HABIRO
where ωr,±1 is the truncation of ω±1 given by
ωr,±1 =
d
X
n=0
(±1)nv± 1
2 n(n+3)P ′
n ∈P.
Note that ωr,±1 ∈SpanAr{P0, P1, . . . , Pd} ⊂RAr. We also have Ωr,±1 ∈RAr.
Lemma 11.2. Let L = L1 ∪· · · ∪Lm ∪K be an (m + 1)-component, algebraically-
split, 0-framed link. Then, for x1, . . . , xm ∈RAr, we have
evζ(JL∪K(x1, . . . , xm, ωr,±1)) = evζ(JL∪K(x1, . . . , xm, Ωr,±1)).
(11.5)
Proof. If K is an unknot, then by Theorem 9.4 and the deﬁnition of ωr,±1 we have
evζ(JL∪K(x1, . . . , xm, ωr,±1)) = evζ(JL(K,∓1)(x1, . . . , xm)),
(11.6)
where L(K,∓1) is the result from L by surgery along K with framing ∓1. By (11.3)
and the standard fusing argument, we also have
evζ(JL∪K(x1, . . . , xm, Ωr,±1)) = evζ(JL(K,∓1)(x1, . . . , xm)).
Hence, we have (11.5).
Now, we consider the general case. A crossing change of two strands in K can
be done by a Hoste move. Applying this move ﬁnitely many times, we get a framed
link L ∪K′ ∪E1 ∪· · · ∪Et, t ≥0, such that all the linking numbers between
two components of L ∪K′ ∪E1 ∪· · · ∪Et are zero, K′ is a 0-framed unknot,
E1 ∪· · · ∪Et is an admissible framed unlink with framings g1, . . . , gt ∈{±1}, and
(L ∪K′)E1∪···∪Et ∼= L ∪K. Using (11.6) iteratively, we obtain
evζ(JL∪K(x1, . . . , xm, y))
= evζ(JL∪K′∪E0
1∪···∪E0m(x1, . . . , xm, y, ωr,−g1, . . . , ωr,−gt)),
where E0
i is Ei with 0-framing, and y is either ωr,±1 or Ωr,±1.
Since K′ is an
unknot, the assertion reduces to the special case proved above.
