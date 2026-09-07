---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-016-7-application-to-the-differential-transcendence
section_title: "Application to the differential transcendence"
section_number: 7
pages: 34-35
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
Let k be a ﬁeld of characteristic zero and ( k, φ, ∂) be a C1-ﬁeld with no proper ﬁnite
diﬀerence ﬁeld extension, equipped with an automorphism φ, and a derivation ∂, that is an
additive morphism satisfying the Leibnitz rule ∂(f g) = ∂(f )g + f ∂(g). Let us assume that
φ and ∂ commute. In our examples, we may take ∂ = ∂z (case S and E), and ∂ = z∂z (case
Q). In the Mahler case, we could adapt as in [ DHR18] the framework with the derivation
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 35
∂ = z∂z log(z) but this will complicate the exposition of a general criter ion, so let us drop
the Mahler case in what follows.
Let us consider R, a ring extension of k such that φ and ∂ extend on R. We say that
f ∈ R is ∂-algebraic over k if there exists n ∈ N and a nonzero P ∈ k[X0, . . . , Xn] such that
P (f, . . . , ∂nf ) = 0. We say that f is ∂-transcendent over k otherwise. In our examples, f
is ∂-algebraic over k if and only if it is ∂z-algebraic over k. Many proof of ∂-transcendence
of solutions of φ-equation are based on the diﬀerence Galois theory. Roughly s peaking,
this kind of theorem says that if the diﬀerence Galois group is suﬃciently big, then the
nonzero solutions of the linear equation are ∂-transcendent. Let f ∈ R∗ be a solution of
a3φ3(y) + a2φ2(y) + a1φ(y) + a0y = 0, where ai ∈ k and a0a3 ⁄= 0.
Consider the dual ∑ 3
i=0 φ−i(ai)φ−i that is equivalent to
φ3(a0)φ3(y) + φ2(a1)φ2(y) + φ(a2)φ(y) + a3y = 0, where ai ∈ k.
Theorem 7.1. Let us assume that
• there is no u ∈ k such that
a3uφ(u)φ2(u) + a2uφ(u) + a1u + a0 = 0.
• there is no u ∈ k such that
φ3(a0)uφ(u)φ2(u) + φ2(a1)uφ(u) + φ(a2)u + a3 = 0.
• there is no g ∈ k and nonzero linear diﬀerential operator L ∈ C[∂], such that
L(∂(a0/a3)/(a0/a3)) = φ(g) − g.
Then, f is ∂-transcendent over k.
Proof. Let G be the diﬀerence Galois group of the equation of order three sa tisﬁed by
f . The ﬁrst assumption ensures that the operator has no right f actor of order one and
the second assumption ensures that the operator has no left f actor of order one. So the
operator is irreducible and then the diﬀerence Galois group i s irreducible. When G is
imprimitive, this is the same reasoning as [ ADR21, Theorem 3.5]. When G is primitive,
it contains SO 3(C) and we now follow the proof of [ ADR21, Theorem 3.5]. □
