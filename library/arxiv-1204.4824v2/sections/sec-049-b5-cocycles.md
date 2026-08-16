---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-049-b5-cocycles
section_title: "B.5 Cocycles"
section_number: null
pages: 80-82
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
We would now like to relate the formalism of this paper to the formalism using the Xγij′
used in our previous paper [5]. The essential problem here is one of signs. In this section we
explain how one can construct a twisted ring, which allows us to work directly with paths
onC and Σ, at the cost of introducing some subtle cocycles in the multiplication rules. The
precise statement is equation (B.18) below. What we actually prove is the closely related
statement (B.16), but to pass to (B.18) we rely on a conjecture stated below (B.17).
In order to deﬁne the framed 2d-4d degeneracies in terms of paths on C rather than on
˜C, we will need a way of lifting fromC to ˜C. To do this we introduceI(C), the immersion
– 78 –
category of C. The objects are points on C together with tangent directions, i.e. points
of ˜C, and the morphisms are immersions of intervals [ T1,T 2] into C. Note that there is
no identity morphism so this “category” is a category without identity morphisms, i.e., a
semicategory. We can view it as a subsemicategory of P( ˜C). If we mod out by regular
homotopy (i.e. homotopy through immersions) we obtain a semicategoryπReg
≤1 (C). We also
have an obvious functor πReg
≤1 (C)→P ( ˜C), hence a ring homomorphism
Lift :R(πReg
≤1 (C))→R(π≤1( ˜C)). (B.11)
Composing with the projection R(π≤1( ˜C))→R(π≤1( ˜C))/I we get
R(πReg
≤1 (C))→R(π≤1( ˜C))/I. (B.12)
Recall that the objects of πReg
≤1 (C) are points of ˜C. Thus, a point z∈ C with tangent
vector corresponds to a point ˜z∈ ˜C. A little closed loop beginning at ˜ z and wrapping
around the ﬁber of ˜C overz maps to to−1˜z.
The statement we are aiming for, (B.18) below, concerns homotopy classes of paths,
rather than regular homotopy classes. Therefore, the ﬁrst step is to ﬁnd a homomorphism
R(π≤1(C))→R(πReg
≤1 (C)). We could attempt to ﬁnd such a homomorphism by choosing,
for each homotopy class, an immersion in the same homotopy class. In general this will not
produce anything like a homomorphism into R(πReg
≤1 (C)). First of all, composable paths
in π≤1(C) will, in general, not map to composable immersions in πReg
≤1 (C). Thus, the ﬁrst
thing we should do is choose a nowhere-zero vector ﬁeld on C and, for each homotopy
class in π≤1(C), choose an immersion whose initial and ﬁnal tangent vectors match the
tangent vector at a point. However, even once we have done this, if we lift two composable
homotopy classes [ ¯℘1] and [ ¯℘2] to regular homotopy classes of immersions [ι1] and [ι2] there
is no guarantee that the lift [ι12] of [ ¯℘1◦ ¯℘2] is the same as [ι1◦ι2]. That is,
[ι12]⁄= [ι1◦ι2] := [ι1]· [ι2] (B.13)
so we still do not get a homomorphism. However, if we compose our non-canonical non-
homomorphism with the map to the quotient (B.12) then we will get a homomorphism
from a twisted ring:
R(π≤1(C),σ )→ Lift
(
R(πReg
≤1 (C))
)
/I (B.14)
The cocycle in question is
σ([℘1], [℘2]) = (−1)w[ι1◦ι2◦ι−1,a
12 ] (B.15)
whereι−1,a
12 is the anti-lift of the inverse immersionι−1
12 . (Given an immersion, we can lift it
in the usual way, but then we can compose with the antipodal map in the ﬁber. Call that
the anti-lift. Given an immersion ¯℘ in C with canonical lift ℘ in ˜C, ℘−1 is the antilift of
¯℘−1.) It would be nice to have a more conceptual and invariant description of this cocycle.
Now let us reconsider the framed 2d-4d BPS degeneracies. We can compose the map
(B.14) with the formal monodromy and ﬁnally project to the homology groupoid to get a
homomorphism of the form
¯F :R(π≤1(C),σ )→R(H≤1(˜Σ))/I (B.16)
– 79 –
The whole discussion above for the curve C can be repeated for Σ to construct a map
R(H≤1(Σ),σ ir)→R(H≤1(˜Σ))/I (B.17)
where the cocycle σir is analogous to that appearing in (B.16). It is natural to conjecture
that (B.16) in fact factors through a homomorphism
¯F :R(π≤1(C),σ uv)→R(H≤1(Σ),σ ir) (B.18)
where σuv is the cocycle (B.15) appearing in (B.16). This would be a gauge-invariant
formulation of the 2d-4d degeneracies directly involving paths on C and Σ.
