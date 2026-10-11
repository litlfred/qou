---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-002-21-galois-stability
section_title: "Galois-stability"
section_number: 2.1
pages: 3-4
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
group and Y an aﬃne G-variety, both deﬁned over K.
Deﬁnition 2.1. A point y ∈Y (K) is said to be Galois-stable up to G-action if for any
γ ∈Gal(K/K) there exists g ∈G(K) such that γ(y) = gy.
It is clear that whether or not a point y is Galois-stable up to G-action is determined by
its G(K)-orbit, and that if gy ∈Y (K) for some g ∈G(K) then y is Galois-stable. The
converse is false, however: e.g., take K = R, Y ⊂A1 deﬁned by the equation x2 = −1 (so
Y (K) = ∅), G = {1, −1} acting on x by multiplication, and y = i. So in general being
Galois-stable up to G-action is a strictly weaker condition than being conjugate to a point
deﬁned over K.
Example 2.2. Let A be a ﬁnitely generated K-algebra, N a positive integer, Y the variety
of N-dimensional matrix representations of A, and G = PGLN acting on Y by conjugation.
Then a representation η : A →MatN(K) is Galois-stable up to G-action if and only if for
any γ ∈Gal(K/K), the representations η and γ(η) are isomorphic. In particular, this notion
applies to representations of ﬁnitely generated groups, by taking A to be a group algebra.
For brevity, from now on we will speak about Galois-stable representations, dropping the
words “up to G-action”.
Now let G, Y be deﬁned over C and let K := C(q), where q := (q1, ..., qn) is a collection
of variables. Then for every y ∈Y (K) there exists a nonempty aﬃne open subset U ⊂Cn
4
PAVEL ETINGOF AND ALEXANDER VARCHENKO
and a ﬁnite unramiﬁed Galois cover p : eU →U such that y ∈Y (C[eU]).
Thus, given
a := (a1, ..., an) ∈U and ea ∈p−1(a), we can deﬁne the specialization y|ea ∈Y (C) of y at ea.
However, if η is Galois-stable up to G-action then the G(C)-orbit of y|ea depends only on a.
So when we only care about the G(C)-orbit of this specialization, we will denote it by y|a.
