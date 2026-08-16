---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-007-2-suppose-thatm-is-a-knot-complement-andm-is-a-m
section_title: "Suppose thatM is a knot complement andm is a meridian. Ifv projects to"
section_number: 2
pages: 11-16
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
a reducible characterλ +λ−1 in X(M) then λ(m)2 is a root of the Alexander
polynomial of M of orderr≥ 1. Under some technical hypothesis detailed
in Section 2.3, tor(M, Ad◦ρ) vanishes at v at order bounded by2r− 2. In
particular it does not vanishes ifλ2 is a simple root.
If v is an ideal point ofY, then the Culler-Shalen theory associates tov an action
ofπ1(M) on the Bass-Serre tree ofSL2(Ov) which itself produces an incompressible
surface Σ in M. We say thatΣ is associated to the ideal pointv.
Theorem (Theorem 2.0.2). Letv be an ideal point ofY and Σ be an incompressible
non-Seifert surface associated tov. We suppose thatΣ is a union of parallel connec-
ted copiesΣ1∪... Σn and that both components ofM\ Σi are handlebodies. Let us
also assume thatY contains the character of a representation whose restriction to
Σ is irreducible. Then the torsiontor(M, Ad◦ρ) has vanishing order atv bounded
by−n(χ(Σ) + 1)if the ideal point does not correspond to the character of an abelian
representation ofπ1(Σ), and by−nχ(Σ)−m else, where m depends only on the
restriction ofρ to π1(Σ).
We say that a surfaceS⊂ M is free if its complement is a union of handlebodies.
Many natural constructions yield such surfaces. For example take a knot diagram
and consider the checkerboard surfaces (on Figure 1 on the left is an example of
such a surface). If one of them, sayΣ, is an incompressible non orientable surface
in M, then the boundary of a neighborhood ofΣ is orientable, and does splitM
into two handlebodies, as can be easily seen (both part of its complement retract
onto a graph). In fact, it is the case for every incompressible surfaces as soon as
M is small. On the other hand, every incompressible non Seifert surface will be
10
splitting M. The distinction with the abelian case at the end of the theorem comes
from the fact that this situation appears naturally in basic examples as the ﬁgure
eight knot. We deduce from this theorem an unexpected relation between the genus
of the character variety ofM and the genus of the incompressible surfaces inM.
More precisely, suppose thatM is a knot complement whose character variety is one
dimensional. Then, let us pick a smooth component of the variety, and assume that
each ideal pointy∈Y corresponds to an incompressible surfaceΣy that veriﬁes the
hypothesis of the theorem. Let us further assume that the Alexander polynomial of
M has only simple roots. Then
−χ(Y )≤
∑
y
−nyχ(Σy)−my
where my is deﬁned as in Theorem 2.0.2. In the simple case where the surfacesΣ
are connected, it turns into
−χ(Y )≤
∑
y
(−χ(Σy)− 1).
Example 0.0.1. We know from [HT85] that the knot5.2 has two incompressible
surfaces in its complement :Σ1 whose Euler characteristic is−4, andΣ2 whose Euler
characteristic is−2 (see ﬁgure 1).
The (geometric component of the) character variety has 3 ideal points, two of them
corresponding to Σ2, and the third toΣ1. The torsion vanishes at order1 on the
Σ2’s ideal points, and at order3 at the other. Hence on the augmented varietyY,
one obtains−χ(Y ) = 4× 1 + 2× 3 = 10. The covering mapY→X(M) ramiﬁes on
six points, hence−χ(X) = 1
2(−χ(Y )− 6) = 2, and the genus ofX is 2, as it can be
computed directly.
Question 0.0.2.Is the inequality of Theorem 2.0.2 an equality?
In all the examples we have listed in Section 2.2.3 for connected incompressible
surfaces, it happens to be an equality. A careful examination of the proof shows
that it has to be generically the case. The lack of equality should be interpreted as
a non-transversal situation.
Furthermore, it also seems reasonable that the vanishing order of the torsion is
always positive, and one may wonder :
Question 0.0.3. For which knot complements is the torsion a regular diﬀerential
form on a component of the character variety?
11
ˇΣ1
ˇΣ2
Figure 1 – Incompressible surfaces in the complement of the knot5.2. The surface
Σ1 is the orientation covering of the non oriented surface here colored on the left,
thatcanbethoughtastheboundaryofatubularneighborhoodofthisnonorientable
surface. The surfaceΣ2 is again the orientation covering of the surface colored on the
right, that can be obtained as follows : consider two parallel copies of each twisted
bands above and below the square in the middle, and plumb them along this square.
The result is connected because the bands below have an odd number of twists, and
this is our surfaceΣ2
From Theorem 2.0.1, it is so on the aﬃne part of¯X(M). Yet the torsion could
have a pole at inﬁnity. In fact, examples of torus knots(p,q ) provide such a case :
each component of the character variety is isomorphic toC with an unique ideal
point, which corresponds to an essential annulus in the knot complement. Although
Theorem 2.0.2 cannot apply since the fundamental group of an annulus have no
non abelian representations, one can compute directly that the torsion has a pole of
order one at those points.
Further work could concern reducible characters that are limits of irreducible cha-
racters, such as in Theorem 2.0.1, item 2. It is most likely that one could eventually
weaken the hypothesis of this theorem. But this requires a better understanding of
the relation between the ﬁrst twisted cohomology group and the tangent space at
this point. This complex problem is partially answered in [FK91, HPSP01].
The standard torsion
In Chapter 3, we focus on the standard torsion, and present the results of the
upcoming article [Ben17]. The standard torsiontor(M,ρ ) is deﬁned as a non zero
12
rational function on the character variety. More precisely, we takeX to be a one
dimensional component of the character variety, and the torsion function is seen as
an element of the function ﬁeldk(X)∗. While it is not usually deﬁned in the way it
is here, the torsion function has been long established as such. The question of how
to compute this function and whether it has some zeros is still under investigation.
It is known to be a constant function on the character varieties of torus knots.
The ﬁrst non constant computation was done by Kitano in [Kit94]. Since then,
because of its proximity with the twisted Alexander polynomial, there has been
many more studies of this torsion. In [DFJ12], the authors address several questions
on the twisted Alexander polynomial, and in particular if its evaluation att = 1,
namelythestandardtorsion,canbeconstantonacomponentofthecharactervariety
of a hyperbolic knot that carries the character of the holonomy representation (a
geometric component). In chapter 3, we partially answer this question, and conclude
to the negative. See Theorem 3.0.2 and the corollary below.
The ﬁrst result of this chapter is the following :
Theorem (Theorem3.0.1). LetX be a geometric component of the character variety
X(M) of a hyperbolic manifoldM. Then tor(M,ρ ) is a regular function onX, that
vanishes at a characterχ if and only if the vector spaceH1(M, ¯ρ) is non trivial,
where ¯ρ is a representation¯ρ :π1(M)→ SL2(C) whose character isχ.
The fact that the torsion has no poles onX was expected. Yet, to our knowledge,
there has been no such formal statement to date, and it is interesting in and by itself.
The characterization in terms of jump of dimension of the vector spaceH1(M, ¯ρ)
is also notalbe, because it relates the torsion with the deformation theory of semi-
simple representations inSL3(C). We provide more detailed explanations about this
at the beginning of Chapter 3. Similarly to Chapter 2, we treat separately the case
of ideal points inX. When saying that a curveγ∈π1(Σ) has trivial eigenvalue, we
mean that the representation corresponding to the ideal points¯ρΣ :π1(Σ)→ SL2(C)
maps γ on a matrix with eigenvalues equal to 1.
Theorem (Theorem 3.0.2). Let x∈ ˆX be an ideal point in the smooth projective
model ofX, and assume that an associated incompressible surfaceΣ is a union of
parallel homeomorphic copiesΣi such that M\ Σi is a (union of) handlebodie(s).
If the curve γ = ∂Σ ∈ π1(M) has trivial eigenvalues, then the torsion function
tor(M,ρ ) has a pole atx.
We deduce the following corollary :
13
Corollary 0.0.4.LetM be a hyperbolic manifold andX be a geometric component
of its SL2(C) character variety. Assume that an ideal point ofX detects an incom-
pressible surface which is connected or union of parallel free copies, and such that
the eigenvalue of its boundary curve is 1. Then the torsion function is not constant
on the componentX.
Here again, the hypothesis that the complement of any connected component ofΣ
is union of handlebodies is automatically satisﬁed if the manifoldM is small. The
hypothesis on the eigenvalue of the boundary curve is automatically satisﬁed forΣ
a Seifert surface, and we discuss it more generally in Chapter 3.
Since we expect the torsion to be non constant on the geometric component of any
small hyperbolic three manifold, we adress the following question :
Question 0.0.5.Is it true that a geometric component of a small hyperbolic three
manifold detects necessarily an incompressible surface whose boundary curve has
eigenvalue 1?
Two-bridge knots are known to have non-Seifert incompressible surfaces with only
2 boundary components, in case which the eigenvalue of the boundary curve is±1.
Yet, as mentioned above, any Seifert surface’s boundary curve has eigenvalue 1. It
thus seems reasonable to consider this question.
14
Chapitre 1
