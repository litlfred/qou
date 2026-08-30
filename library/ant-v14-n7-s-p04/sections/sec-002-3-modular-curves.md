---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic ﬁelds are modular"
section_id: sec-002-3-modular-curves
section_title: "Modular curves"
section_number: 3
pages: 3-4
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
doc_brief: "Elliptic curves over totally real cubic fields are modular — 10 sections: Introduction; Images mod 3, 5, 7 and modularity; Modular curves"
---
We quickly sketch some background on modular curves; for fuller details the reader may want to
consult [Deligne and Rapoport 1973; Freitas et al. 2015, Section 2.2.2; Rohrlich 1997]. Let H∗=
H∪ Q∪{∞} denote the extended upper half-plane. The modular group SL2(Z) acts on H by fractional
linear transformations. The quotient SL2(Z)\H∗ is a compact Riemann surface of genus 0, and hence is
the analytiﬁcation of a genus 0 algebraic curve deﬁned (a priori) over C which is denoted by X(1). The
set Q∪{∞}⊂ H∗ forms a single orbit under the action of SL2(Z), and hence that orbit corresponds to
a point of X(1) which is called the cusp. In fact X(1) has a model deﬁned over Spec(Z) in which it is
identiﬁed with P1, and where the cusp is simply the point at inﬁnity.
Let p be a prime and let H be a subgroup of GL2(Fp) satisfying det(H)= F∗
p. Associated to
H is a congruence subgroup 0H which is deﬁned as the preimage of H∩ SL2(Fp) under the map
SL2(Z)→ SL2(Fp). The modular curve X H/C is the proper algebraic curve whose analytiﬁcation is the
compact Riemann surface0H\H∗. In fact the condition det(H)= F∗
p ensures that X H has a model over
Spec(Z[1/p]). The inclusion 0H⊂ SL2(Z) induces a morphism j: X H→ X(1), which is also deﬁned
over Spec(Z[1/p]). The cusps of X H are the preimages of∞∈ X(1), and thus also the orbits of Q∪{∞}
under the action of0H .
We now come to the modular interpretation of rational points on X H , and here it is convenient to make
an additional assumption, namely−I∈ H. Let K be a ﬁeld of characteristic⁄= p. Let E/K be an elliptic
curve such thatρ E,p(G K) is conjugate to a subgroup of H. Then there is at least one noncuspidal point
P∈ X H(K) such that j(P)= j(E) where j(E) is the j-invariant of the elliptic curve E. The converse
of this statement is false in general. There is however a partial converse which is true: if P∈ X H(K)
is a noncuspidal point and j(P)⁄= 0, 1728 then there is an elliptic curve E/K such thatρ E,p(G K) is
conjugate to a subgroup of H and j(E)= j(P).
If we take H= B0(p), C+
s (p), C+
ns(p) then X H is the modular curve usually denoted by X0(p),
Xsplit(p) and Xnonsplit(p) respectively. For convenience, instead of using the standard notation for these
modular curves, we shall mostly follow the notation of [Freitas et al. 2015] and denote these modular
curves by X(bp):= X0(p), X(sp):= Xsplit(p) and X(nsp):= Xnonsplit(p).
Now let K be a totally real cubic ﬁeld, and for simplicity suppose K⁄= Q(ζ7)+. By Theorems 3, 4
and 5, a potentially nonmodular elliptic curve E deﬁned over K would give rise to a noncuspidal K -point
P on either X(b3) or X(s3), and simultaneously a noncuspidal K -point Q on X(b5), and simultaneously
a noncuspidal K -point R on either X(b7) or X(ns7). Observe that j(P)= j(Q)= j(R)= j(E). Thus
we obtain a K -point on one of the ﬁber products
X(u3)×X(1) X(b5)×X(1) X(v7), u∈{ b, s}, v∈{ b, ns}. (1)
We denote the normalization of (1) by X(u3, b5, v7). As E is hypothetically nonmodular, it is non-CM,
and in particular j(E)⁄= 0, 1728. The maps X H→ X(1) are ramiﬁed only above 0, 1728 and∞, and
thus the K -point we obtain from E on (1) is a smooth point and hence gives rise to a K -point on the
1794 Maarten Derickx, Filip Najman and Samir Siksek
normalization X(u3, b5, v7). Thus to prove Theorem 2 for K⁄= Q(ζ7)+ it is enough to show that K -points
on the four possible curves X(u3, b5, v7) are cuspidal. In fact it is plainly enough to do this for the two
curves X(b5, b7) and X(b5, ns7).
An overview of the proof of Theorem 2. In Section 4 we prove modularity of elliptic curves deﬁned over
Q(ζ7)+. In view of the above discussion the following two theorems immediately imply Theorem 2.
Theorem 6. Let K be a totally real cubic ﬁeld. Then X (b5, b7)(K) consists only of cusps.
Theorem 7. Let K be a cubic ﬁeld. Then X (b5, ns7)(K) consists only of cusps.
The remainder of the paper is devoted to the proof of these two theorems.
