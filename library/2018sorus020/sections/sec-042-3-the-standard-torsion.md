---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-042-3-the-standard-torsion
section_title: "The standard torsion"
section_number: 3
pages: 84-86
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Here M is a compact connected orientable 3-manifold, whose boundary is a torus.
In this chapter we pick X a one-dimensional component of irreducible type of the
character variety X(M), and denote by k(X) its function ﬁeld. Here we consider the
action of the fundamental group π1(M) on the 2-dimensional vector space k(X)2
through the tautological representation ρ : π1(M) →SL2(k(X)), and the correspon-
ding cohomological complex C∗(M, ρ). When this complex is acyclic (for instance
when X is a component of the character variety of a hyperbolic manifold that carries
the holonomy character, say a geometric component), the Reidemeister torsion of
this complex deﬁnes a rational function on the complex curve X. We prove that
this function’s zeros are precisely characters χ¯ρ ∈X where the residual cohomology
group H1(M, ¯ρ) are not trivial, and that this function is regular (it has no poles on
X). Moreover, we consider ¯X a smooth projective model, and show that an ideal
point of ¯X is a pole of the torsion function if it detects an incompressible surface
that splits M into two handlebodies and which satisﬁes the following condition : the
boundary slope γ is known (see [CCG+94]) to be mapped by the limit representa-
tion on a matrix with eigenvalue a root of unity. Moreover the order of this root
of unity divides the minimal number of boundary components of any component of
the incompressible surface Σ associated to this ideal point by the construction of
Section 1.3. We assume that the root of unity is 1, and we will say that the boun-
dary curve has trivial eigenvalues. Such an assumption is motivated by numerical
computations, and by the fact that it occurs in many known examples. In fact it has
been a diﬃcult task to ﬁnd roots of unity diﬀerent of ±1 with this construction, see
[Dun99] for the ﬁrst known example. The results of this chapter will be the core of
the upcoming paper [Ben17], we summarize them in the following theorems :
83
Theorem 3.0.1. Let X be a one dimensional component of the character variety
X(M) and ρ : π1(M) →SL2(k(X)) the tautological representation. Assume that the
complex C∗(M, ρ) is acyclic. Then tor(M, ρ) is a regular function on X. Moreover
its order at a point χ ∈X is given by the length of the torsion module H2(M, ρ)v,
where v is the valuation associated to χ on the function ﬁeld k(X). In particular it
vanishes if and only if H1(M, ¯ρ) is non trivial, where ¯ρ is the residual representation
¯ρ : π1(M)
ρ−→SL2(Ov)
mod t
−−−→SL2(k) whose character is χ.
Theorem 3.0.2. Let x ∈ˆX be an ideal point in the smooth projective model of
X, and assume that an associated incompressible surface Σ is a union of parallel
homeomorphic copies Σi such that M \ Si is a (union of) handlebodie(s). If the
curve γ = ∂Σ ∈π1(M) has trivial eigenvalues, then the torsion function tor(M, ρ)
has a pole at x.
The proof of this theorem recovers two cases, treated separately in Section 3.3.1,
where the components of the incompressible surface split M, and Section 3.3.2,
where they do not. The hypothesis on the boundary eigenvalues is discussed in the
beginning of Section 3.3.1, on the other hand it is automatically satisﬁed in Section
3.3.2.
If M is hyperbolic, the question whether the torsion deﬁnes a non-constant func-
tion on a geometric component has been addressed in [DFJ12, Section 1.7]. It is
motivated by the following observation and conjecture : this article of Nathan Dun-
ﬁeld, Stefan Friedl and Nicholas Jackson studies twisted Alexander polynomial of
hyperbolic knots. It is a Laurent polynomial ∆ρ(t) associated to a representation of
the fundamental group ρ : π1(M) →SL2(C), and it follows from its deﬁnition that
∆ρ(1) = tor(M, ρ)(χρ), for χρ the character corresponding to ρ. It is conjectured
from numerical evidences that this polynomial considered at the holonomy repre-
sentation carries a lot of topological information on the manifold M, as ﬁberness,
chirality, genus and volume. If the torsion was constant, it would suggest a disproof
of this conjecture . This question is motivated by the fact that the torsion is known
to be locally constant on the character variety of torus knots. The ﬁrst computation
of non constant torsion function has been performed by Teruaki Kitano in [Kit94]
for the ﬁgure-eight knot. We deduce the following corollary of Theorem 3.0.2, which
answer partially to this question. Recall that a connected surface Σ ∈M is free if
M \ S is a union of handlebodies.
Corollary 3.0.3. Let M be a hyperbolic manifold and X be a geometric component
of its SL2(C) character variety. Assume that an ideal point of X detects an incom-
84
pressible surface which is connected or union of parallel free copies, and such that
