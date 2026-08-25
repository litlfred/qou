---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-021-4-torsion-on-the-character-variety
section_title: "Torsion on the character variety"
section_number: 4
pages: 22-23
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
Having given a putative formula for the non-abelian torsion of a cusp ed hyperbolic man-
ifold M at the discrete faithful representation ρ0, it is natural to ask whether the formula
generalizes to other settings. In this section, we extend the tors ion formula to general rep-
resentationsρ :π1(M)−→ (P)SL(2, C) for manifolds M with torus boundary, essentially by
letting the shapes z be functions of ρ. We also ﬁnd that some special results hold when M
is hyperbolic and the representations lie on the geometric componen tX geom
M of the SL(2, C)
character variety.
We will begin with a short review of what it means for a combinatorial ide al triangulation
to be regular with respect to a general representation ρ. We will also ﬁnally prove Proposition
1.7 from the Introduction. Recall that Proposition 1.7 identiﬁed a canonical connected subset
X EP
M of the set of regular triangulationsXρ0 of a hyperbolic 3-manifold M. This result allowed
us to construct the topological invariant τM .
We then proceed to deﬁne an enhanced Neumann-Zagier datum ˆβT = (z, A, B,f ) suitable
for a general representation ρ, and propose a generalization of the torsion formula:
(4.1) τT (ρ) :=±1
2 det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f.
This formula looks identical to ( 1.8). However, the shape parameters here are promoted to
functions z→ z(ρ) of the representation ρ, which satisfy a well known deformed version
of the gluing equations. Moreover, the ﬂattening f is slightly more restricted than it was
previously. We will prove in Section 4.5 that
Theorem 4.1. The formula for τT (ρ) is independent of the choice of enhanced Neumann-
Zagier datum, and is invariant under 2–3 moves connecting ρ-regular triangulations.
When M is hyperbolic, it turns out that ρ0-regular triangulations are ρ-regular for all but
ﬁnitely many representations ρ∈X geom
M . Then we can create a topological invariant τM that
is a function on X geom
M just as in Proposition 1.7, by evaluating τT (ρ) on any triangulation
in the canonical subset X EP
M ⊆X ρ0.
In general, there is a rational map from the character variety XM to the zero-locus YM
of the A-polynomial AM (ℓ,m ) = 0 [ CCG+94], for any M with torus boundary. Therefore,
the shapes z and the torsion τT are algebraic functions on components of the A-polynomial
curve YM . When M is hyperbolic and ρ∈ X geom
M , somewhat more is true: the shapes are
rational function on the geometric component Y geom
M (Proposition B.1). Then
(4.2) τM ∈ C(Y geom
M ) = Q(m)[ℓ]/
(
Ageom
M (ℓ,m )
)
,
whereAgeom
M (ℓ,m ) is the geometric factor of the A-polynomial. We will give a simple examp le
of the function τM for the ﬁgure-eight knot in Section
4.6.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 23
4.1. A review of ρ-regular ideal triangulations. In this section we discuss the ρ-regular
ideal triangulations that are needed to generalize our torsion invar iant. Let M denote a
3-manifold with nonempty boundary and let ρ :π1(M)−→ PSL(2, C) be a PSL(2 , C) repre-
sentation of its fundamental group. Let X denote the set of combinatorial ideal triangulations
T of M. Matveev and Piergallini independently showed that every two eleme nts ofX with
at least two ideal tetrahedra are connected by a sequence of 2-3 moves (and their inverses)
[Mat87, Pie88]. For a detailed exposition, see [ Mat07, BP97].
Given an ideal triangulationT , let VT denote the aﬃne variety of non-degenerate solutions
(i.e., solutions in C\{ 0, 1}) of the gluing equations of T corresponding to its edges. There
is a developing map
(4.3) VT−→XM,
where XM := Hom(π1(M), PSL(2, C))/PSL(2, C) denotes the aﬃne variety of all PSL(2 , C)
representations of π1(M).
Deﬁnition 4.2. Fix a PSL(2, C)-representation of M. We say that T ∈X is ρ-regular if ρ
is in the image of the developing map (
4.3).
LetXρ⊂X denote the set of all ρ-regular ideal triangulations of M. When M is hyper-
bolic, let ρ0 denote its discrete faithful representation ρ0 and let X geom
M ⊂ XM denote the
geometric component of its character variety [ Thu77, NZ85]. We then have the following
result.
Lemma 4.3. (a)T ∈Xρ0 if and only if T has no homotopically peripheral ( i.e., univalent)
edges.
(b) IfT ∈Xρ0, thenT ∈Xρ for all but ﬁnitely many ρ∈X geom
M .
Proof. Part (a) has been observed several times; see [
Cha03], [BDR V, Sec.10.3], [Til, Thm.2.3]
and also [ DG11, Rem.3.4]. For part (b), ﬁx T ∈Xρ0. Observe that T is ρ-regular if the
image of every edge 3 ofT under ρ does not commute with the image under ρ of the periph-
eral subgroup of M. This is an algebraic condition on ρ, and moreover, when ρ∈X geom
M is
analytically nearby ρ0, the condition is satisﬁed. It follows that the set of points of X geom
M
that satisfy the above condition is Zariski open. On the other hand ,X geom
M is an aﬃne curve
[Thu77, NZ85]. It follows that T is ρ-regular for all but ﬁnitely many ρ∈X geom
M . □
