---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-026-2-the-adjoint-torsion
section_title: "The adjoint torsion"
section_number: 2
pages: 46-48
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Let ¯X be a component of irreducible type of the augmented character variety ¯X(M)
and k( ¯X) its function ﬁeld. In this chapter we will study the action of the funda-
mental group π1(M) on the Lie algebra sl2(k( ¯X)), and the Reidemeister torsion of
the twisted complex C∗(M, Ad ◦ρ) for this action. It is what we will call the adjoint
torsion. First we will deﬁne it as a rational diﬀerential form over Y , the smooth
projective model of ¯X, and then we will study its poles and zeros, in particular we
will observe that the torsion is regular on the aﬃne part ¯X of the Riemann surface
Y . We will deduce a "genus formula" that gives a relation between the topology
of the augmented character variety and the Euler characteristic of incompressible
surfaces in M produced through the Culler-Shalen theory. This chapter contains the
results of the article [Ben16].
Notation. The convention that we follow here for the torsion is convenient to ex-
press it as a diﬀerential form on the character variety. Many authors use the opposite
convention, for instance in Section 2.2.3 we use some computations of Jerome Du-
bois with the other convention. On the other hand, it is the convention taken in
[GKZ94, Appendix A].
The results of this chapter are summarized in the following theorems :
Theorem 2.0.1. Let ¯X be a component of irreducible type of the augmented cha-
racter variety, and let x be a point in ¯X, with corresponding valuation v. Then the
adjoint torsion tor(M, Ad ◦ρ) vanishes at v with order given by the length of the
torsion part of the Ov-module H1(M, Ad ◦ρ)v. In particular tor(M, Ad ◦ρ) is regular
on ¯X, and does not vanish if v projects onto a smooth point of X(M).
The striking point of this theorem, and the more simple to state, is that the torsion
deﬁnes a regular diﬀerential form on ¯X, which was not expected from the deﬁnition.
45
On the other hand, its zeros are included in pre-image S of the singular locus of
X(M) through the covering map ¯X →X, but not every point x ∈S will be a
zero of the torsion. For instance, the pre-image of an intersection point with normal
crossing between two components of irreducible type in X(M) will not, neither
will generically be the pre-image of an intersection point between a component of
irreducible type and the component of reducible type. We do not know any example
of such a zero, and it is related with the fact that we do not know any component
of irreducible type with an intrinsic singularity, like a cusp or a self-crossing.
Theorem 2.0.2. Let y ∈Y be an ideal point of the smooth projective model of a
component of irreducible type ¯X of the augmented character variety, and let v be the
corresponding valuation on k(Y ). Assume that y detects an incompressible surface
Σ ⊂M, such that Σ is connected or is the union of n parallel homeomorphic copies,
that the restriction ρΣ is not abelian and that the complement of any connected
component of Σ in M is the disjoint union of two handlebodies. Then we have the
following bound on the order of tor(M, Ad ◦ρ) at y :
v(tor(M, Ad ◦ρ)) ≤−nχ(Σ) −m
where m = n whence ρΣ is not residually abelian, and else m = length(H1(Σ, Ad ◦ρΣ).
Unless χ is an annulus (see the example of the trefoil knot Section 2.1, which remains
true for torus knots in general), there is no reason for the order of tor(M, Ad ◦ρ) at
y to be negative. In fact, it is not the case for the four non-torus examples we have
computed. From this observations we adress the following question :
Question 2.0.3. Is there a hyperbolic knot such that the adjoint torsion form has
a pole on the augmented covering of a geometric component ?
A somehow related question is the following, which comes naturally after considering
the examples at the end of this chapter :
Question 2.0.4. Is the inequality of Theorem 2.0.2 an equality ?
We deduce from Theorem 2.0.2 the following corollary :
Corollary 2.0.5. Assume that X(M) holds a one-dimensional component X such
that every irreducible characters χ ∈X are smooth points, and that for each ideal
point y in its smooth projective model of the augmented variety Y one can produce
an incompressible surface Σy with ny connected components and which veriﬁes the
46
hypothesis of Theorem 2.0.2. Futhermore, assume that the Alexander polynomial of
M has simple roots. Then
−χ(Y ) ≤
X
y
−nyχ(Σy) −my
where my is deﬁned as in Theorem 2.0.2.
The two ﬁrst sections of this chapter are devoted to the deﬁnition of the adjoint
torsion as a diﬀerential form on the augmented character variety, and we detail
several computations of this form. In the third section we give a proof of Theorem
2.0.1, and some interpretation of those results in terms of torsion in the Kähler
diﬀerential’s module and of Alexander invariants. In the fourth section we begin
with an explicit topological computation of the torsion form of the trefoil knot,
which has inspired the general proof of Theorem 2.0.2 that follows, and we conclude
by checking our results on a series of examples.
