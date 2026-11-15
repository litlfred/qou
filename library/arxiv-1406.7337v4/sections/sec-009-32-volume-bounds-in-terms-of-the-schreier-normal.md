---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-009-32-volume-bounds-in-terms-of-the-schreier-normal
section_title: "Volume bounds in terms of the Schreier normal form"
section_number: 3.2
pages: 13-14
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
Volume bounds in terms of the Schreier normal form
We begin this section by presenting a result that, for the family of closed 3-braids that satisfy Lemma 2.1,
states that the parameters k and s from the Schreier normal form of the 3-braid can actually be read oﬀ
of the original 3-braid word. We then use this result to obtain volume bounds in terms of the parameter s
from the Schreier normal form.
Theorem 3.1. Let D(K) = bβ denote the closure of a nice 3-braid β ∈B3 that satisﬁes the assumptions
of Lemma 2.1. Then β is generic and, furthermore, we are able to express the parameters k and s of the
Schreier normal form β′ in terms of the original 3-braid β as follows:
(1) k = −# {induced products σn2
2 σn1
1
of negative syllables of β, where n1, n2 ≤−3}.
(2) s = t−(D) = # {negative syllables in β}.
Note that, when looking for the induced products σn2
2 σn1
1
of negative syllables of β to ﬁnd k, we must
look cyclically in the braid word. As a special case of the above theorem, notice that if β = σp1
i σn1
j
· · · σpl
i σnl
j
is an alternating 3-braid where {i, j} = {1, 2}, then k = 0 and s = l.
Also note that the count
# {induced products σn2
2 σn1
1
of negative syllables of β, where n1, n2 ≤−3}
is the same as the count
#
n
induced products σn′
1
1 σn′
2
2
of negative syllables of β, where n′
1, n′
2 ≤−3
o
.
This is because, recalling from Lemma 2.1 that wandering corresponds to the existence of adjacent negative
syllables (in adjacent braid generators), the number of times a wandering circle wanders from braid string
position 1 to braid string position 3 is the same as the number of times a wandering circle wanders from
braid string position 3 to braid string position 1.
Remark 3.1. Since the 3-braids of Theorem 3.1 (which satisfy the assumptions of Lemma 2.1) are generic,
then Proposition 4.15 of [14] implies, with the assumption that k̸ = 0, that
|k| −1 ≤gT (K) ≤|k| ,
where K is the hyperbolic link with closed 3-braid diagram D(K) = bβ and where gT (K) denotes the Turaev
genus of K. Thus, since conclusion (1) of Theorem 3.1 gives that we can read the parameter k from the
original 3-braid β, then we can visually bound the Turaev genus of the braid closure.
Deferring the proof of Theorem 3.1 to the next section, we now relate the parameter s from the Schreier
normal form of a 3-braid from Lemma 2.1 to the stable penultimate coeﬃcient β′
K of the colored Jones
polynomial of the closure of this 3-braid.
Corollary 3.1. Let D(K) = bβ, where β ∈B3 satisﬁes the assumptions of Lemma 2.1. Then
s = t−(D) = |β′
K|.
Thus, t−(D) and s are link invariants.
13
Proof. Using the conclusions of Lemma 2.1, we can apply Theorem 3.1 of [2], Theorem 2.2, and Theorem 3.1
respectively to get that |β′
K| = 1 −χ(G′
A) = 1 + (t−(D) −1) = t−(D) = s.
Since the colored Jones
polynomial and therefore its coeﬃcients are link invariants, then we can conclude that t−(D) and s are link
invariants.
By combining Corollary 2.1, Corollary 3.1, and Proposition 3.2, we get the following result, which is a
more precise version of Theorem 1.2 from the introduction.
Theorem 3.2. Let D(K) = bβ, where β ∈B3 satisﬁes the assumptions of Lemma 2.1. Then we have the
volume bounds
v8 · (s −1) ≤vol(S3\K) < 4v8 · s.
Remark 3.2. Comparing the lower bound on volume of Theorem 3.2 to that of Proposition 3.2, we get
that v8 · (s −1) ≥4v3 · s −276.6 is equivalent to the condition that s ≤276.6 −v8
4v3 −v8
≈690. Therefore, the
lower bound found in Theorem 3.2 is sharper than the lower bound provided by Proposition 3.2 unless the
parameter s from the Schreier normal form is very large.
