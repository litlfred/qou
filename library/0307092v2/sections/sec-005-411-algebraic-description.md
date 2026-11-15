---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-005-411-algebraic-description
section_title: "Algebraic description"
section_number: 4.1.1
pages: 14-15
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
Algebraic description
We recall a standard chain complex for homology of G = PSL(2, C), the chain
complex of “homogeneous simplices for G.” We will, however, diverge from
the standard by using only non-degenerate simplices, ie, simplices with distinct
vertices — we may do this because G is inﬁnite.
Let Cn(G) denote the free Z–module on all ordered (n+1)–tuples ⟨g0, . . . , gn⟩
of distinct elements of G. Deﬁne δ : Cn →Cn−1 by
δ⟨g0, . . . , gn⟩=
n
X
i=0
(−1)i⟨g0, . . . , ˆgi, . . . , gn⟩.
Then each Cn is a free ZG–module under left-multiplication by G. Since G is
inﬁnite the sequence
· · · →C2 →C1 →C0 →Z →0
is exact, so it is a ZG–free resolution of Z. Thus the chain complex
· · · →C2 ⊗ZG Z →C1 ⊗ZG Z →C0 ⊗ZG Z →0
computes the homology of G. Note that Cn⊗ZGZ is the free Z–module on sym-
bols ⟨g0 : . . . : gn⟩, where the gi are distinct elements of G and ⟨g0 : . . . : gn⟩=
⟨g′
0 : . . . : g′
n⟩if and only if there is a g ∈G with ggi = g′
i for i = 0, . . . , n (we
call these homogeneous n–simplices for G).
Thus an element of α ∈Hn(G; Z) is represented by a sum
X
ǫi⟨g(i)
0 : . . . : g(i)
n ⟩
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
427
of homogeneous n–simplices for G and their negatives (here each ǫi is ±1).
The fact that this is a cycle means that the (n−1)–faces of these homogeneous
simplices cancel in pairs. We choose some speciﬁc way of pairing canceling faces
and form a geometric quasi-simplicial complex K by taking a n–simplex ∆i for
each homogeneous n–simplex of the above sum and gluing together (n −1)–
faces of these ∆i that correspond to (n−1)–faces of the homogeneous simplices
that have been paired with each other.
As already mentioned, a quasi-simplicial complex actually suﬃces for our pur-
poses. But we can obtain a simplicial complex by replacing K by its barycentric
subdivision if necessary (label the barycenter of each simplex by an arbitrary
element of G that diﬀers from the G–labels of the barycenters of all proper
faces of that simplex). A standard argument shows that this does not change
the homology class represented by K.
We thus get a representation of the
homology class in the promised form.
