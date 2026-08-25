---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic ﬁelds are modular"
section_id: sec-007-4-this-means-that-there-is-only-one-q-rational-g
section_title: "This means that there is only one Q-rational g2"
section_number: 4
pages: 7-8
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
doc_brief: "Elliptic curves over totally real cubic fields are modular — 10 sections: Introduction; Images mod 3, 5, 7 and modularity; Modular curves"
---
6, namely the one corresponding to the degree
6 model given by u,w,v above. In particular every Q-rational automorphism has to come from an
automorphism h: P2
Q→ P2
Q in the degree 6 model. Such an automorphism h has to preserve the singular
locus{p1, p2, p3, p4} and is in fact uniquely determined by what it does on this singular locus. Of the 24
automorphisms of P2
Q preserving{p1, p2, p3, p4}, only the ones of the form (u:v:w)↦→(±u:±v:w)
are Q-rational. One easily sees that of these four only the identity and (u:v:w)↦→(−u:−v:w) are
actually automorphisms of the curve. □
Transferring c0 and c∞ to our new model D, we ﬁnd that they respectively are the Galois orbits of the
following two points deﬁned over Q(η)= Q(ζ7)+ by
(−4η2+ 21η+ 7:−η2+ 7η: 14), ( 4η2− 21η− 7:η2− 7η: 14).
We note that these are interchanged byw5:(u:v:w)↦→(−u:−v:w) as expected.
The Mordell–Weil group A(Q). In Lemma 6.1 we deﬁned the abelian subvariety A of J as the image of
w5− 1 and observed that A(Q) is torsion. We can now pin down A(Q) precisely. In particular, applying
the function ﬁeld class group algorithm of Hess [2002] (implemented in Magma) to our model D, we
obtain
J(F3)∼= Z/7Z× Z/(7· 23)Z, and J(F17)∼= Z/2Z× Z/(22· 73· 31· 271)Z.
Hence J(Q)tors is isomorphic to a subgroup of Z/7Z. Recall that the class[c0− c∞] has order 7. Thus
[c0− c∞] generates J(Q)tors. Now since w5 interchanges c0 and c∞,
(w5− 1)([3c0− 3c∞])= 6[c∞− c0]=[ c0− c∞].
Therefore[c0−c∞]∈ A(Q). As A(Q)= A(Q)tors⊆ J(Q)tors= Z/7Z we have now proved the following.
Lemma 6.3. A(Q)=(Z/7Z)·[ c0− c∞].
1798 Maarten Derickx, Filip Najman and Samir Siksek
