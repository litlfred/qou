---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-087-3-modular-curves
section_title: "Modular curves"
section_number: 3
pages: 127-133
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
4. Modularity of elliptic curves over Q(ζ7)+
In this section we prove Theorem 2 for K= Q(ζ7)+.
Lemma 4.1. Let K= Q(ζ7)+. Let E be an elliptic curve deﬁned over K . Then E is modular.
Proof. By Theorem 4 we may suppose that ρ E,5 is reducible. By Theorem 3 we may suppose that the
image of ρ E,3 is contained in B(3) or C+
s (3). Thus E gives rise to a noncuspidal K -point on one of
the two modular curves X(b3, b5), X(s3, b5). It is shown in [Freitas et al. 2015, Section 5.4.2] that
these are in fact elliptic curves deﬁned over Q with Cremona labels 15A1 and 15A3. We computed the
Mordell–Weil groups X(K) for X= X(b3, b5), X(s3, b5) using Magma. In both cases we found
X(K)= X(Q)∼= Z/4Z⊕ Z/2Z.
In particular E gives rise to Q-point on X and so is a twist of an elliptic curve deﬁned over Q. It is
therefore modular by [Breuil et al. 2001]. □
5. Proof of Theorem 6
Let X= X(b5, b7) (in standard notation denoted by X0(35)). It is known that X has four Q-points and
that these are cusps. Let K be a totally real cubic ﬁeld. For the proof of Theorem 6 it will be sufﬁcient
to show that X(K)= X(Q). Suppose P∈ X(K)\X(Q). Let P1, P2, P3 be the conjugates of P given
by the three embeddings of K in Q, and write D= P1+ P2+ P3. Then D is an irreducible Q-rational
divisor on X of degree 3. We shall determine all the irreducible Q-rational divisors of degree 3 on X and
show that none of them arise from totally real cubic points, giving a contradiction.
The arithmetic of X and its Jacobian are studied in [Freitas et al. 2015, Section 5.1]. The curve X is
hyperelliptic of genus 3. A model for X, derived by Galbraith [1996, Section 4.4], is given by
X: y2=(x2+ x− 1)(x6− 5x5− 9x3− 5x− 1). (2)
Write∞± for the two points at inﬁnity. Write J for J0(35) — the Jacobian of X. Then
J(Q)= Z
24Z·[∞−−∞+]+ Z
2Z·[ 3(0,−1)− 3∞+].
Elliptic curves over totally real cubic ﬁelds are modular 1795
Let D1,..., D48 be rational divisors of degree 0 on X representing the 48 classes in J(Q), and let
D′
i= Di+ 3∞+. Recall that D is an irreducible Q-rational divisor of degree 3. Then D∼ D′
i for some i.
We shall write L(D′
i) for the Riemann–Roch space corresponding to D′
i and|D′
i| for the corresponding
complete linear system. By Riemann–Roch and Clifford’s inequality, dim L(D′
i)= 1 or 2. Moreover, if
dim L(D′
i)= 2, then|D′
i| contains a base point (see [Arbarello et al. 1985, Chapter I, Exercise D.9]),
and therefore cannot contain an irreducible divisor. To sum up, D∼ D′
i for some 1≤ i≤ 48 such that
dim L(D′
i)= 1. We computed these spaces using Magma; for this Magma uses an algorithm of Hess [2002].
We found that dim L(D′
i)= 1 for precisely 44 of the 48 divisors D′
i. For these, letting fi be a Q-basis for
L(D′
i), gives D= D′
i+ div( fi) for some i. We found that precisely 28 of the effective degree 3 divisors
D′
i+ div( fi) are irreducible. However, all of these split over a cubic ﬁeld with a complex embedding
giving the required contradiction.
6. The modular curve X(b5, ns7)
We shall henceforth restrict our attention toX(b5, ns7). To simplify the notation we write X= X(b5, ns7).
We denote the Jacobian of X by J= J(b5, ns7). The curve X and its Jacobian J are studied in Le
Hung’s thesis [2014, Section 6.4] and we make extensive use of his results. In particular, this curve is
nonhyperelliptic and has genus 6.
The Jacobian J = J(b5, ns7). Le Hung shows that
J∼ A1× A2× A3
where∼ here denotes isogeny over Q, and A1, A2, A3 are modular abelian surfaces deﬁned over Q.
Moreover the Ai are absolutely simple. The involution w5 on J is compatible with the isogeny and
acts by multiplication by 1,−1,−1 respectively on A1, A2, A3. The analytic ranks of A1, A2, A3 are
respectively 2, 0, 0. In particular, by the work of Kolyvagin and Logachëv [1989], the Mordell–Weil
groups A2(Q) and A3(Q) are torsion. We immediately deduce the following.
Lemma 6.1. Let A/Q be the abelian subvariety of J that is the image ofw5− 1. Then A∼ A2× A3 has
dimension 4. Moreover, the Mordell–Weil group A(Q) is torsion.
Le Hung’s model for X = X(b5, ns7). We need a good model for X(b5, ns7). Le Hung [2014, page 47]
gives a model which will be a good starting point for us. We brieﬂy sketch Le Hung’s derivation of his
model, but work with projective rather than afﬁne coordinates. Later we explain how to derive a better
model. The curves X(b5) and X(ns7) are both isomorphic to P1 over Q. Let
F1(x1, x2)=(x2
1+ 10x1x2+ 5x2
2)3,
F2(x1, x2)= x1x5
2,
G1(y1, y2)= 64·(y1·(y2
1+ 7y2
2)·(y2
1− 7y1y2+ 14y2
2)·(5y2
1− 14y1y2− 7y2
2))3, and
G2(y1, y2)=(y3
1− 7y2
1 y2+ 7y1y2
2+ 7y3
2)7.
1796 Maarten Derickx, Filip Najman and Samir Siksek
For appropriate choices of projective coordinates(x1: x2) for X(b5) and(y1: y2) on X(ns7), the j-maps
are given by
j: X(b5)→ X(1), ( x1: x2)↦→(F1(x1, x2): F2(x1, x2)),
and
j: X(ns7)→ X(1), ( y1, y2)↦→(G1(y1, y2): G2(y1, y2)).
As X is the normalization of X(b5)×X(1) X(ns7) we immediately deduce the following model for X in
P1× P1:
C: F1(x1, x2)G2(y1, y2)= F2(x1, x2)G1(y1, y2).
The curve X is the normalization of this model. The parametrization (x1: x2) on X(b5) is chosen so that
the 0 and∞ cusps are(x1: x2)=(0: 1) and(x1: x2)=(1: 0), respectively. We shall denote these by a0,
and a∞. Letζ7 be a primitive 7-th root of unity. Letη= 2(ζ7+ζ7)+3∈ Q(ζ7)+. Then G2(η: 1)= 0. The
three cusps of X(ns7) are(η: 1) and its Galois conjugates. It follows that the cusps of X are the points
belonging to the normalization of C lying above the points(x1: x2, y1: y2)=(0: 1,η: 1),(1: 0,η: 1)
and their Galois conjugates. Although these points on C are singular, it is easy to check (see [Freitas et al.
2015, Section 5.5.1]) that there is only one point on the normalization above each, and to deduce:
• X has two Galois orbits of cusps, both of degree 3 and deﬁned over Q(ζ7)+, which we denote by c0,
c∞.
• The three cusps in c0 map to a0, and the three cusps in c∞ map to a∞ on X(b5).
• The divisor of x1/x2 interpreted as a function on X is 7·(c0− c∞). In particular, the class[c0− c∞]
is an element of order 1 or 7. There are several ways to show that the divisor c0−c∞ is not principal,
and so its class has order 7. One way is by direct computation using Magma, working with the model
D introduced below. Here is another way: we shall show below that X has gonality 4. As c0, c∞
have degree 3 they cannot be linearly equivalent.
A plane degree 6 model for X = X(b5, ns7). We used Magma to compute, starting with the model C,
the canonical map and its image. The latter is indeed a smooth genus 6 curve cut out in P5 by six
homogeneous degree 2 polynomials. By the Enriques–Babbage theorem [Arbarello et al. 1985, page 124],
we know that X is neither trigonal, nor isomorphic to a plane quintic. Moreover, as the factors Ai of the
Jacobian are 2-dimensional and absolutely simple, we see that the curve is not bielliptic. It follows (see
[loc. cit., pages 209–210]) that X has gonality 4 and a degree 6 planar model, with four ordinary double
points as singularities. We used the inbuilt Magma implementation for writing down this model, and found
that two of the four double points are deﬁned over Q(i) and the other two over Q(
√
5). After applying
a Q-rational automorphism of P2 to slightly simplify this degree 6 model, it is given by the following
equation:
D: 5u6− 50u5v+ 206u4v2− 408u3v3+ 321u2v4+ 10uv5− 100v6+ 9u4w2
− 60u3vw2+ 80u2v2w2+ 48uv3w2+ 15v4w2+ 3u2w4− 10uvw4+ 6v2w4−w6= 0.
Elliptic curves over totally real cubic ﬁelds are modular 1797
On this model D the double points are
p1=(i: 0: 1), p2=(−i: 0: 1), p3=
(
0: 1√
5
: 1
)
, p4=
(
0:− 1√
5
: 1
)
.
It is clear that D has an automorphism (u:v:w)↦→(−u:−v:w). The curve X has an obvious
modular involution which isw5. The following lemma proves that w5 coincides with the automorphism
(u:v:w)↦→(−u:−v:w).
Lemma 6.2. The Q-rational automorphism group of X(b5, ns7) is generated byw5, i.e., AutQ(X)=
⟨w5⟩∼= Z/2Z.
Proof. As described in [Arbarello et al. 1985, pages 210–211] a degree 6 planar curve with four ordinary
double points such as D has exactly ﬁve different g1
4. Namely, one given by the pencil of quadrics going
through all four points, and the other four coming from the pencil of lines through each of the pi. Since
none of the pi are Q-rational, only the ﬁrst g1
4 is deﬁned over Q. Now every g2
6 on such a curve is residual
to a g1
4. This means that there is only one Q-rational g2
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
7. Proof of Theorem 7
In this section we prove Theorem 7 thereby completing the proof of Theorem 2. Recall X= X(b5, ns7).
Write X(3) for the third symmetric power of X. We shall prove the following result which immediately
implies Theorem 7.
Proposition 7.1. X(3)(Q)={ c0, c∞}.
Proof. Let x∈ X(3)(Q). By Lemma 6.3 we have (1−w5)[x− c∞]= 𝓁·[ c0− c∞] for some𝓁∈ Z/7Z.
Asw5(c∞)= c0 we may rewrite this as
(x−w5(x))∼ k·(c0− c∞)
for some k∈{− 3,..., 3}. We write xF3, c0,F3, c∞,F3∈ X(3)(F3) for the reductions of x, c0, c∞ modulo 3
respectively. It follows that
(y−w5(y))∼ k·(c0,F3− c∞,F3) (3)
where y= xF3. Using our model D we enumerated X(3)(F3); this has precisely 40 elements. For each
y∈ X(3)(F3) and for each k=− 3,..., 3 we tested the relation (3) and found that it holds only fory= c0,F3
and k= 1 and for y= c∞,F3 and k=− 1. We therefore deduce that xF3= c0,F3 or c∞,F3. We would like to
conclude that x= c0 or c∞. As w5 swaps c0 and c∞ and also their mod 3 reductions, we may suppose
that xF3= c∞. Letµ: X(3)→ J be given by z↦→[ z− c∞] and t: J→ A be simply t=w5− 1. Since
xF3= c∞,F3, the point (t◦µ)(x)∈ A(Q) belongs to the kernel of reduction A(Q)→ A(F3). However
as A(Q) is torsion, this kernel of reduction is trivial [Katz 1981, Appendix]. Thus (t◦µ)(x)= 0. To
conclude that x= c∞ it is now enough to check that t◦µ is a formal immersion at c∞,F3, and for this we
shall use the formal immersion criterion due to Derickx, Kamienny, Stein and Stoll [Derickx et al. 2017,
Proposition 3.7].
WriteX∼=J for the 6-dimensional space of 1-forms on X/F3. We would like to write down the
4-dimensional subspace t∗(A). We easily do this since it is precisely that−1-eigenspace ofw∗
5 acting
onX, and we know the action of w5 on our model D from which can write down the corresponding
action on the 1-forms. Let ω1,...,ω 4 be an F3-basis for t∗(A). To check the formal immersion
criterion of Derickx et al. at c∞,F3 we need to check that a certain 4× 3 matrix deﬁned in [Derickx
et al. 2017, Proposition 3.7], which we denote by M, has rank 3. As 3 is inert in Q(ζ7)+, we have
c∞,F3= P1+ P2+ P3, where Pi∈ X(F27) are distinct. This slightly simpliﬁes the description of the
matrix M. Let u j∈ F27(X) be a uniformizing element for Pj. Thenωi/du j is a regular function at Pj
and we may evaluate(ωi/du j)(Pj)∈ F27. That matrix is simply
M=((ωi/du j)(Pj))i=1,2,3,4; j=1,2,3.
We computed M and checked that it has rank 3 as required. This completes the proof. □
Elliptic curves over totally real cubic ﬁelds are modular 1799
