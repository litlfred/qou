---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
toc_source: outline
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — 9 sections: Front matter; Quantum Dilogarithm Function; Examples"
---
arXiv:math/0604094v1  [math.QA]  5 Apr 2006
GENERALIZED VOLUME CONJECTURE AND THE A-POLYNOMIALS:
THE NEUMANN–ZAGIER POTENTIAL FUNCTION AS A CLASSICAL LIMIT OF
QUANTUM INVARIANT
KAZUHIRO HIKAMI
A. We study quantum invariant Zγ(M) for cusped hyperbolic3-manifold M. We construct
this invariant based on oriented ideal triangulation of M by assigning to each tetrahedron the
quantum dilogarithm function, which is introduced by Faddeev in studies of the modular double of
the quantum group. Following Thurston and Neumann–Zagier, we deform a complete hyperbolic
structure of M, and correspondingly we deﬁne quantum invariant Zγ(Mu). This quantum invariant
is shown to give the Neumann–Zagier potential function in the classical limit γ →0, and the A-
polynomial can be derived from the potential function. We explain our construction by taking
examples of 3-manifolds such as complements of hyperbolic knots and punctured torus bundle
over the circle.
1. I
Since the quantum invariant of knots/links and 3-manifolds as a generalization of the Jones
polynomial [25] is constructed by Witten [53] by use of the Chern–Simons path integral, stud-
ies on quantum invariants have been much developed. Recently geometrical interpretations of
the quantum invariants have received interests since Kashaev observed an intriguing relation-
ship [29] between the hyperbolic volume and his knot invariant, which is later identiﬁed with a
speciﬁc value of the N-colored Jones polynomial JK

N; e2πi/N
[41] (here the N-colored Jones
polynomial is normalized to be Junknot(N; q) = 1). Namely the hyperbolic volume of the knot
complement S 3 \ K is conjectured to dominate the asymptotics of the invariant JK

N; e2πi/N
in
the large-N limit N →∞,
lim
N→∞
2 π
N log

JK

N; e2πi/N

 = Vol(S 3 \ K)
(1.1)
This “volume conjecture” is generalized for other values (near the N-th root of unity) of the N-
colored Jones polynomial [18] (see also Refs. 39,40), and a relationship with the A-polynomial
is conjectured; when we deﬁne b by
b = −d
da
lim
N,k→∞
N/k=a
1
k log JK

N; e2πi/k
(1.2)
Date: April 4, 2006.
1
2
K. HIKAMI
the pair

eb, −eia
is a zero locus of the A-polynomial for knot K. This is checked numerically
for twist knots [22].
The A-polynomial is deﬁned as an algebraic curve of eigenvalues of the S L(2; C) representa-
tion of the boundary torus of knot K [9] (see also Ref. 10). This can be computed from triangu-
lation of the knot complement M = S 3 \ K into ideal tetrahedra in the hyperbolic space H3 once
the fundamental group has a irreducible representation ρ into PS L(2; C) which is identiﬁed with
the orientation-preserving isometries of H3;
ρ : π1(M) →PS L(2; C) ≃Isom+(H3)
Up to conjugation, the meridian µ and the longitude of the boundary torus of K have
ρ(µ) =
 
m
∗
0
1/m
!
ρ(λ) =
 
ℓ
∗
0
1/ℓ
!
Another geometrical aspect of the N-colored Jones polynomial JK(N; q) as a relationship with
the A-polynomial is proposed as “AJ conjecture” [17]; recursion relation of the colored Jones
polynomial with respect to N is conjectured to be related to the A-polynomial AK(ℓ, m). This
conjecture is proved for the torus knots [23] and the 2-bridge knots [35].
In this paper, we introduce quantum invariant for cusped hyperbolic manifold M and its defor-
mation Mu `a la Thurston [50] following Refs. 19–21, and study a classical limit thereof. Based
on a triangulation of cusped 3-manifold M, we deﬁne quantum invariant Zγ(Mu) by assigning
Faddeev’s quantum dilogarithm function to each oriented ideal tetrahedron. Originally Kashaev
introduced his invariant JK

N; e2πi/N
for triangulated 3-manifolds, although the R-matrix con-
struction is developed subsequently [28]. He studied Faddeev’s quantum dilogarithm function
when q is a root of unity [13,26] (see also Ref. 2), and assigning the quantum dilogarithm func-
tion to ideal tetrahedron he deﬁned invariant [27, 28]. In this sense, our invariant Zγ(M) for
M with complete hyperbolic structure can be regarded as a non-compact Uq(sl(2; R)) analogue
of the Kashaev invariant, and an asymptotic behavior of Zγ(S 3 \ K) in the limit γ →0 should
coincide with that of the Kashaev invariant JK

N; e2πi/N
in the limit N →∞.
This paper is organized as follows. In Section 2 we recall deﬁnitions of quantum dilogarithm
function, and we discuss properties of this function. In Section 3, we shall reveal that the three-
dimensional hyperbolic geometry naturally arises from the quantum dilogarithm function in the
classical limit γ →0 as was clariﬁed in Ref. 19. Then we deﬁne the quantum invariant Zγ(Mu)
for a deformation of complete hyperbolic cusped 3-manifold M. Based on a triangulation of
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS
