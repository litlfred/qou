---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-005-32-cocycle-parameters
section_title: "Cocycle parameters"
section_number: 3.2
pages: 14-16
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
respective fundamental groups.
Fix an e-triangulation (T,b ) of F . Denote by Z(T,b ) the space of PSL (2, C)-valued 1-cocycles on
(T,b ); we stipulate that on a triangle with ordered b-oriented edges e0,e 1,e 2 the cocycle relation is
z(e0)z(e1)z(e2)−1 = 1. In this section we construct a parametrization of R(g,r ) based on cocycle
coeﬃcients by specifying subsets of Z(T,b ) with small ‘residual gauge groups’, that make principal
algebraic bundles over the “strata” of a suitable partition of R(g,r ). These strata are determined by
the holonomies around the boundary components of F .
Write C(T,b ) for the space of PSL (2, C)-valued 0-cochains on ( T,b ), that is the PSL (2, C)-valued
functions deﬁned on the set of vertices of T . Two 1-cocycles z and z′ are said equivalent up to gauge
transformation if there is a 0-cochain λ such that, for every oriented edge e = [x0,x 1], we have
z′(e) = λ(x0)−1z(e)λ(x1) .
It is well known that the quotient set H(T,b ) = Z(T,b )/C(T,b ) is in one-one correspondence with
R(g,r ). Indeed, for any ﬁxed x0 ∈T we have a natural surjective map
fx0 :Z(T,b ) → Hom(π,PSL (2, C)),
where π = π1(F,x 0), and two representations fx0(z) and fx0(z′) deﬁne the same point in R(g,r ) if
and only if z and z′ are equivalent up to gauge transformation. Note that the complex dimension of
H(T,b ) is 3( |E(T )| − (p + 2r) − 2r) = −3χ(F ), which is the dimension of R(g,r ). This is because the
complex dimension of C(T,b ) is equal to 6r, the set Z(T,b ) is deﬁned by 3(p+2r) polynomial relations
QUANTUM HYPERBOLIC GEOMETRY 15
on 3 |E(T )| variables, and PSL (2, C) has trivial centre. (Recall that p is the number of triangles of
the initial triangulation T ′ of S with r vertices.)
Denote by B+(2, C) (respectively B−(2, C)) the Borel subgroup of SL(2, C) of upper (respectively
lower) triangular matrices. Let PB ±(2, C) = B±(2, C)/ ±I and put
P =
( 0 1
1 0
)
.
Deﬁne a map
(15) Ψ : SL(2, C) →SL(2, C), Ψ(A) = PAP
and denote by Ψ the induced automorphism of PSL (2, C). We have Ψ( B±(2, C)) = B∓(2, C). For
any g ∈ PSL (2, C) we distinguish the type of g as trivial, parabolic or generic (the latter for elliptic
or loxodromic) with the obvious meaning. We denote
C+(g) ∈PB +(2, C)
the canonical upper triangular matrix (up to sign) representative of the conjugacy class of g (for
generic g we normalize C+(g) by stipulating that the top diagonal entry has absolute value > 1), and
we set
C−(g) = Ψ( C+(g)).
We deﬁne the type of ρ ∈ R(g,r ) as the n-uple of types of the ρ-holonomies of the oriented boundary
components γ1,...,γ r of F . Put:
R(g,r,t ) = {ρ ∈ R(g,r ) |ρ has type t}
R(g,r, C±) = {ρ ∈ R(g,r,t ) | C ±(ρ(γi)) = C±
i }
where C± = (C±
1 ,..., C±
r ), C±
i is an arbitrary diagonal or unipotent element in PB ±(2, C), and C± has
typet. For any g ∈PB ±(2, C) let us write g = [a,b ]±, where a is the top diagonal entry of g andb is
the non diagonal one (we do the abuse of confusing g with its projective class). For every vertex vi of
(T,b ), let ei
1 be the boundary edge of the preferred inner triangle τvi (see Deﬁnition 3.2), and γi the
oriented boundary loop of F based at vi. Recall the projections fvi :Z(T,b ) → Hom(π,PSL (2, C)).
Deﬁnition 3.3. The set of ( ±)-cocycle parameters for R(g,r, C±) is
Z(T,b, C±) = {z ∈Z(T,b ) | ∀i = 1,...,r, f vi(z)(γi) = C±
i , z(ei
1) = [1, 1/2]±}.
Clearly Z(T,b, C±) is non empty. In fact, any z ∈Z(T,b ) with conj ◦f (z) ∈ R(g,r, C±) is equivalent
to one in Z(T,b, C±) via some gauge transformation. Moreover, given a vertex vi and a 0-cochain s
with support at vi and v′
i, s maps Z(T,b, C±) onto itself if and only if
s(vi) ∈ Stab(C±
i )
and
s(v′
i)−1[1, 1/2]±s(vi) = [1, 1/2]±.
As the triangles τvi are in one-one correspondence with the vi, we deduce that there is a projection
(16) p±
C : Z(T,b, C±) → R(g,r, C±)
with ﬁber isomorphic to the group
G(T,b, C±) := Stab( C±
1 ) × · · · × Stab(C±
r )
that we call the residual gauge transformations . Denote by Z(T,b,t )± (respectively p±
t ) the union of
the Z(T,b, C±) (respectively p±
C ) over all C± with type t, and put
Z(T,b )± = ∐
t Z(T,b,t )±, p ± = ∐
tp±
t ).
For futur reference, we summarize the above constructions in th e following proposition.
16 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Proposition 3.4. For every C±, the projection p± : Z(T,b )± → R(g,r ) restricts to a complex aﬃne
algebraic principal G(T,b, C±)-bundle
Z(T,b, C±) → R(g,r, C).
The map Ψ in (15) yields an isomorphism Z(T,b, C±) ∼
= Z(T,b, C∓). Moreover we have:
dim(Z(T,b, C±) = −3χ(F )
dim(R(g,r, C)) = −3χ(F ) − dim(G(T,b,t C))
dim(R(g,r,t C)) = dim( R(g,r, C)) +α(tC)
wheretC is the type of C and α(tC) is the number of generic entries of tC.
Observe that: if tgen is the purely generic type, then dim( R(g,r,t gen)) = −3χ(F ); if tpar is purely
parabolic, then dim( R(g,r,t par)) = −3χ(F ) − r; if tI is purely trivial, then dim( R(g,r,t I )) =
−3χ(F ) − 3r = −3χ(S) = 6 g − 6. Hence R(g,r,t gen) is a dense open subset of R(g,r ). More-
over, via the inclusion of closures, we have a ﬁltration of R(g,r ) for which R(g,r,t I ) is the ‘deepest’
part. It would be interesting to study the singularities of the closur e of each R(g,r,t ) in R(g,r ), in
order to check if this ﬁltration induces a “stratiﬁcation” of R(g,r ).
Remark 3.5. For parabolic elements g ∈ PSL (2, R) we have two conjugacy classes, that can be
distinguished by a sign. So, replacing PSL (2, C) withPSL (2, R), the constructions of this section still
work by associating a sign to each parabolic end of the surface S \V . Note that for PSL (2, R)-valued
cocycles the idealization procedure described in Section 3.3 below give s only degenerate triangles and
tetrahedra (with real shapes or cross-ratio moduli).
Example: the F ricke space. Suppose that S has a unique marked point v. Choose a standard
curve system S = {ai,bi}g
i=1 based at v, so that
π1(S,v ) =<a 1,b 1,...,a g,bg | [a1,b 1]... [ag,bg] = 1 >.
Cutting open S along S we get a 4g-gonP with oriented boundary edges. Taking the cone to a vertex
it is easy to construct a branched triangulation of P , which induces one, say ( T ′,b ′), for (S,v ). Denote
by (T,b ) any e-triangulation obtained from ( T ′,b ′).
Recall that the Teichm¨ uller spaceT (S) can be identiﬁed with the set of conjugacy classes of PSL (2, R)-
valued discrete faithful representations ofπ1(S), and that we have the well-known (real-analytic) Fricke
parametrization T (S) ∼
= R6g−6 (see e.g. [1]). For each z ∈ T (S) the Fricke coordinates of z are matrix
entries of the ˆz(γ) for all γ ∈ S , where ˆz is a representative of z speciﬁed by ﬁxing once and for all
three of the ﬁxed points of z(ag) and z(bg). So T (S) embeds in the space of real cocycle parameters
for F with trivial type tI . This embedding is generalized easily to the Teichm¨ uller space of arbit rary
bordered Riemann surfaces, by considering the spaces Z(T,b,t ) for all types t ande-triangulations of
(S,V ) with arbitrary V (see Remark 3.5).
