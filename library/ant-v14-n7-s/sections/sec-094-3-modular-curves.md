---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-094-3-modular-curves
section_title: "Modular curves"
section_number: 3
pages: 127-129
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
We quickly sketch some background on modular curves; for fuller details the reader may want to
consult [Deligne and Rapoport 1973; Freitas et al. 2015, Section 2.2.2; Rohrlich 1997]. Let H∗=
H ∪Q ∪{∞} denote the extended upper half-plane. The modular group SL2(Z) acts on H by fractional
linear transformations. The quotient SL2(Z)\H∗is a compact Riemann surface of genus 0, and hence is
the analytiﬁcation of a genus 0 algebraic curve deﬁned (a priori) over C which is denoted by X(1). The
set Q ∪{∞} ⊂H∗forms a single orbit under the action of SL2(Z), and hence that orbit corresponds to
a point of X(1) which is called the cusp. In fact X(1) has a model deﬁned over Spec(Z) in which it is
identiﬁed with P1, and where the cusp is simply the point at inﬁnity.
Let p be a prime and let H be a subgroup of GL2(Fp) satisfying det(H) = F∗
p. Associated to
H is a congruence subgroup 0H which is deﬁned as the preimage of H ∩SL2(Fp) under the map
SL2(Z) →SL2(Fp). The modular curve X H/C is the proper algebraic curve whose analytiﬁcation is the
compact Riemann surface 0H\H∗. In fact the condition det(H) = F∗
p ensures that X H has a model over
Spec(Z[1/p]). The inclusion 0H ⊂SL2(Z) induces a morphism j : X H →X(1), which is also deﬁned
over Spec(Z[1/p]). The cusps of X H are the preimages of ∞∈X(1), and thus also the orbits of Q∪{∞}
under the action of 0H.
We now come to the modular interpretation of rational points on X H, and here it is convenient to make
an additional assumption, namely −I ∈H. Let K be a ﬁeld of characteristic̸ = p. Let E/K be an elliptic
curve such that ρ E,p(G K) is conjugate to a subgroup of H. Then there is at least one noncuspidal point
P ∈X H(K) such that j(P) = j(E) where j(E) is the j-invariant of the elliptic curve E. The converse
of this statement is false in general. There is however a partial converse which is true: if P ∈X H(K)
is a noncuspidal point and j(P)̸ = 0, 1728 then there is an elliptic curve E/K such that ρ E,p(G K) is
conjugate to a subgroup of H and j(E) = j(P).
If we take H = B0(p), C+
s (p), C+
ns(p) then X H is the modular curve usually denoted by X0(p),
Xsplit(p) and Xnonsplit(p) respectively. For convenience, instead of using the standard notation for these
modular curves, we shall mostly follow the notation of [Freitas et al. 2015] and denote these modular
curves by X(bp) := X0(p), X(sp) := Xsplit(p) and X(nsp) := Xnonsplit(p).
Now let K be a totally real cubic ﬁeld, and for simplicity suppose K̸ = Q(ζ7)+. By Theorems 3, 4
and 5, a potentially nonmodular elliptic curve E deﬁned over K would give rise to a noncuspidal K-point
P on either X(b3) or X(s3), and simultaneously a noncuspidal K-point Q on X(b5), and simultaneously
a noncuspidal K-point R on either X(b7) or X(ns7). Observe that j(P) = j(Q) = j(R) = j(E). Thus
we obtain a K-point on one of the ﬁber products
X(u3) ×X(1) X(b5) ×X(1) X(v7),
u ∈{b, s},
v ∈{b, ns}.
(1)
We denote the normalization of (1) by X(u3, b5, v7). As E is hypothetically nonmodular, it is non-CM,
and in particular j(E)̸ = 0, 1728. The maps X H →X(1) are ramiﬁed only above 0, 1728 and ∞, and
thus the K-point we obtain from E on (1) is a smooth point and hence gives rise to a K-point on the
1794
Maarten Derickx, Filip Najman and Samir Siksek
normalization X(u3, b5, v7). Thus to prove Theorem 2 for K̸ = Q(ζ7)+ it is enough to show that K-points
on the four possible curves X(u3, b5, v7) are cuspidal. In fact it is plainly enough to do this for the two
curves X(b5, b7) and X(b5, ns7).
An overview of the proof of Theorem 2. In Section 4 we prove modularity of elliptic curves deﬁned over
Q(ζ7)+. In view of the above discussion the following two theorems immediately imply Theorem 2.
Theorem 6. Let K be a totally real cubic ﬁeld. Then X(b5, b7)(K) consists only of cusps.
Theorem 7. Let K be a cubic ﬁeld. Then X(b5, ns7)(K) consists only of cusps.
The remainder of the paper is devoted to the proof of these two theorems.
4. Modularity of elliptic curves over Q(ζ7)+
In this section we prove Theorem 2 for K = Q(ζ7)+.
Lemma 4.1. Let K = Q(ζ7)+. Let E be an elliptic curve deﬁned over K. Then E is modular.
Proof. By Theorem 4 we may suppose that ρ E,5 is reducible. By Theorem 3 we may suppose that the
image of ρ E,3 is contained in B(3) or C+
s (3). Thus E gives rise to a noncuspidal K-point on one of
the two modular curves X(b3, b5), X(s3, b5). It is shown in [Freitas et al. 2015, Section 5.4.2] that
these are in fact elliptic curves deﬁned over Q with Cremona labels 15A1 and 15A3. We computed the
Mordell–Weil groups X(K) for X = X(b3, b5), X(s3, b5) using Magma. In both cases we found
X(K) = X(Q) ∼= Z/4Z ⊕Z/2Z.
In particular E gives rise to Q-point on X and so is a twist of an elliptic curve deﬁned over Q. It is
therefore modular by [Breuil et al. 2001].
□
5. Proof of Theorem 6
Let X = X(b5, b7) (in standard notation denoted by X0(35)). It is known that X has four Q-points and
that these are cusps. Let K be a totally real cubic ﬁeld. For the proof of Theorem 6 it will be sufﬁcient
to show that X(K) = X(Q). Suppose P ∈X(K)\X(Q). Let P1, P2, P3 be the conjugates of P given
by the three embeddings of K in Q, and write D = P1 + P2 + P3. Then D is an irreducible Q-rational
divisor on X of degree 3. We shall determine all the irreducible Q-rational divisors of degree 3 on X and
show that none of them arise from totally real cubic points, giving a contradiction.
The arithmetic of X and its Jacobian are studied in [Freitas et al. 2015, Section 5.1]. The curve X is
hyperelliptic of genus 3. A model for X, derived by Galbraith [1996, Section 4.4], is given by
X : y2 = (x2 + x −1)(x6 −5x5 −9x3 −5x −1).
(2)
Write ∞± for the two points at inﬁnity. Write J for J0(35) — the Jacobian of X. Then
J(Q) =
Z
24Z · [∞−−∞+] + Z
2Z · [3(0, −1) −3∞+].
Elliptic curves over totally real cubic ﬁelds are modular
1795
Let D1, . . . , D48 be rational divisors of degree 0 on X representing the 48 classes in J(Q), and let
D′
i = Di +3∞+. Recall that D is an irreducible Q-rational divisor of degree 3. Then D ∼D′
i for some i.
We shall write L(D′
i) for the Riemann–Roch space corresponding to D′
i and |D′
i| for the corresponding
complete linear system. By Riemann–Roch and Clifford’s inequality, dim L(D′
i) = 1 or 2. Moreover, if
dim L(D′
i) = 2, then |D′
i| contains a base point (see [Arbarello et al. 1985, Chapter I, Exercise D.9]),
and therefore cannot contain an irreducible divisor. To sum up, D ∼D′
i for some 1 ≤i ≤48 such that
dim L(D′
i) = 1. We computed these spaces using Magma; for this Magma uses an algorithm of Hess [2002].
We found that dim L(D′
i) = 1 for precisely 44 of the 48 divisors D′
i. For these, letting fi be a Q-basis for
L(D′
i), gives D = D′
i + div( fi) for some i. We found that precisely 28 of the effective degree 3 divisors
D′
i + div( fi) are irreducible. However, all of these split over a cubic ﬁeld with a complex embedding
giving the required contradiction.
