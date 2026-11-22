---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-021-42-proof-of-lemma
section_title: "Proof of Lemma ??"
section_number: 4.2
pages: 20-21
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
Proof of Lemma 3.1. Let l be ﬁxed; we will use backward induction over
k. For k = l we know that f(µk) = 0 for inﬁnitely many choices of µk.
In other words, polynomial f has inﬁnitely many zeros hence f = 0, as
claimed.
Let us assume that the inductive assertion holds for some k ≤l. We can
write
f(xk−1, . . . , xl) =
X
0≤i≤N
xi
k−1 fi(xk, . . . , xl)
STRUCTURE OF KEROV CHARACTER POLYNOMIALS
21
for some N. Let us ﬁx integers µk, . . . , µl bigger than 1 which satisfy
(14) and (13). Then we can ﬁnd inﬁnitely many integer numbers µk−1 for
which the vector (µk−1, . . . , µl) satisﬁes both (14) and (13); for each such
a number we have f(µk−1, . . . , µl) = 0 therefore the polynomial xk−1 7→
f(xk−1, µk, . . . , µl) has inﬁnitely many zeros hence it is the zero polyno-
mial and fi(µk, . . . , µl) = 0. This shows that the inductive assertion can be
applied to the polynomial fi(xk, . . . , xl) and therefore fi(xk, . . . , xl) = 0.
This ﬁnishes the proof.
□
