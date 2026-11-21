---
doc_id: ant-v14-n7-s-p04
doc_title: "Elliptic curves over totally real cubic fields are modular"
section_id: sec-003-5-proof-of-theorem-6
section_title: "Proof of Theorem 6"
section_number: 5
pages: 4-8
source_pdf: ant-v14-n7-s-p04.pdf
source_sha256: 6abd838a4c933311
toc_source: inferred
doc_brief: "Elliptic curves over totally real cubic fields are modular — 7 sections: Front matter; Introduction; Images mod 3, 5, 7 and modularity"
---
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
6. The modular curve X(b5, ns7)
We shall henceforth restrict our attention to X(b5, ns7). To simplify the notation we write X = X(b5, ns7).
We denote the Jacobian of X by J = J(b5, ns7). The curve X and its Jacobian J are studied in Le
Hung’s thesis [2014, Section 6.4] and we make extensive use of his results. In particular, this curve is
nonhyperelliptic and has genus 6.
The Jacobian J = J(b5, ns7). Le Hung shows that
J ∼A1 × A2 × A3
where ∼here denotes isogeny over Q, and A1, A2, A3 are modular abelian surfaces deﬁned over Q.
Moreover the Ai are absolutely simple. The involution w5 on J is compatible with the isogeny and
acts by multiplication by 1, −1, −1 respectively on A1, A2, A3. The analytic ranks of A1, A2, A3 are
respectively 2, 0, 0. In particular, by the work of Kolyvagin and Logachëv [1989], the Mordell–Weil
groups A2(Q) and A3(Q) are torsion. We immediately deduce the following.
Lemma 6.1. Let A/Q be the abelian subvariety of J that is the image of w5 −1. Then A ∼A2 × A3 has
dimension 4. Moreover, the Mordell–Weil group A(Q) is torsion.
Le Hung’s model for X = X(b5, ns7). We need a good model for X(b5, ns7). Le Hung [2014, page 47]
gives a model which will be a good starting point for us. We brieﬂy sketch Le Hung’s derivation of his
model, but work with projective rather than afﬁne coordinates. Later we explain how to derive a better
model. The curves X(b5) and X(ns7) are both isomorphic to P1 over Q. Let
F1(x1, x2) = (x2
1 + 10x1x2 + 5x2
2)3,
F2(x1, x2) = x1x5
2,
G1(y1, y2) = 64 · (y1 · (y2
1 + 7y2
2) · (y2
1 −7y1y2 + 14y2
2) · (5y2
1 −14y1y2 −7y2
2))3, and
G2(y1, y2) = (y3
1 −7y2
1 y2 + 7y1y2
2 + 7y3
2)7.
1796
Maarten Derickx, Filip Najman and Samir Siksek
For appropriate choices of projective coordinates (x1 : x2) for X(b5) and (y1 : y2) on X(ns7), the j-maps
are given by
j : X(b5) →X(1),
(x1 : x2) 7→(F1(x1, x2) : F2(x1, x2)),
and
j : X(ns7) →X(1),
(y1, y2) 7→(G1(y1, y2) : G2(y1, y2)).
As X is the normalization of X(b5) ×X(1) X(ns7) we immediately deduce the following model for X in
P1 × P1:
C : F1(x1, x2)G2(y1, y2) = F2(x1, x2)G1(y1, y2).
The curve X is the normalization of this model. The parametrization (x1 : x2) on X(b5) is chosen so that
the 0 and ∞cusps are (x1 : x2) = (0 : 1) and (x1 : x2) = (1 : 0), respectively. We shall denote these by a0,
and a∞. Let ζ7 be a primitive 7-th root of unity. Let η = 2(ζ7+ζ7)+3 ∈Q(ζ7)+. Then G2(η : 1) = 0. The
three cusps of X(ns7) are (η : 1) and its Galois conjugates. It follows that the cusps of X are the points
belonging to the normalization of C lying above the points (x1 : x2, y1 : y2) = (0 : 1, η : 1), (1 : 0, η : 1)
and their Galois conjugates. Although these points on C are singular, it is easy to check (see [Freitas et al.
2015, Section 5.5.1]) that there is only one point on the normalization above each, and to deduce:
• X has two Galois orbits of cusps, both of degree 3 and deﬁned over Q(ζ7)+, which we denote by c0,
c∞.
• The three cusps in c0 map to a0, and the three cusps in c∞map to a∞on X(b5).
• The divisor of x1/x2 interpreted as a function on X is 7·(c0 −c∞). In particular, the class [c0 −c∞]
is an element of order 1 or 7. There are several ways to show that the divisor c0 −c∞is not principal,
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
D : 5u6 −50u5v + 206u4v2 −408u3v3 + 321u2v4 + 10uv5 −100v6 + 9u4w2
−60u3vw2 + 80u2v2w2 + 48uv3w2 + 15v4w2 + 3u2w4 −10uvw4 + 6v2w4 −w6 = 0.
Elliptic curves over totally real cubic ﬁelds are modular
1797
On this model D the double points are
p1 = (i : 0 : 1),
p2 = (−i : 0 : 1),
p3 =

0 : 1
√
5
: 1

,
p4 =

0 : −1
√
5
: 1

.
It is clear that D has an automorphism (u : v : w) 7→(−u : −v : w). The curve X has an obvious
modular involution which is w5. The following lemma proves that w5 coincides with the automorphism
(u : v : w) 7→(−u : −v : w).
Lemma 6.2. The Q-rational automorphism group of X(b5, ns7) is generated by w5, i.e., AutQ(X) =
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
6 model given by u, w, v above. In particular every Q-rational automorphism has to come from an
automorphism h : P2
Q →P2
Q in the degree 6 model. Such an automorphism h has to preserve the singular
locus {p1, p2, p3, p4} and is in fact uniquely determined by what it does on this singular locus. Of the 24
automorphisms of P2
Q preserving {p1, p2, p3, p4}, only the ones of the form (u : v : w) 7→(±u : ±v : w)
are Q-rational. One easily sees that of these four only the identity and (u : v : w) 7→(−u : −v : w) are
actually automorphisms of the curve.
□
Transferring c0 and c∞to our new model D, we ﬁnd that they respectively are the Galois orbits of the
following two points deﬁned over Q(η) = Q(ζ7)+ by
(−4η2 + 21η + 7 : −η2 + 7η : 14),
(4η2 −21η −7 : η2 −7η : 14).
We note that these are interchanged by w5 : (u : v : w) 7→(−u : −v : w) as expected.
The Mordell–Weil group A(Q). In Lemma 6.1 we deﬁned the abelian subvariety A of J as the image of
w5 −1 and observed that A(Q) is torsion. We can now pin down A(Q) precisely. In particular, applying
the function ﬁeld class group algorithm of Hess [2002] (implemented in Magma) to our model D, we
obtain
J(F3) ∼= Z/7Z × Z/(7 · 23)Z,
and
J(F17) ∼= Z/2Z × Z/(22 · 73 · 31 · 271)Z.
Hence J(Q)tors is isomorphic to a subgroup of Z/7Z. Recall that the class [c0 −c∞] has order 7. Thus
[c0 −c∞] generates J(Q)tors. Now since w5 interchanges c0 and c∞,
(w5 −1)([3c0 −3c∞]) = 6[c∞−c0] = [c0 −c∞].
Therefore [c0 −c∞] ∈A(Q). As A(Q) = A(Q)tors ⊆J(Q)tors = Z/7Z we have now proved the following.
Lemma 6.3. A(Q) = (Z/7Z) · [c0 −c∞].
1798
Maarten Derickx, Filip Najman and Samir Siksek
