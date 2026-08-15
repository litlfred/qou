---
doc_id: angled-survey
doc_title: "Contemporary Mathematics From angled triangulations to hyperbolic structures"
section_id: sec-019-18-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 18
pages: 18-19
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "Contemporary Mathematics From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on"
---
that αi is the angle cut oﬀ byσi. Recall that, in Deﬁnition 2.3, we deﬁned
ϵi =
{
1, if αi is to the left ofσi,
−1, if αi is to the right ofσi.
Comparing this with Deﬁnition 4.1 and Figure 3, we see that the vectorw(σi)
increases angleβi at rateϵi, and increasesγi at rate−ϵi. By Lemma 5.3,
∂V
∂w(σ) =
k∑
i=1
∂V
∂w(σi)
=
k∑
i=1
(−ϵi logsin βi +ϵi logsin γi)
=
k∑
i=1
ϵi log
( sinγi
sinβi
)
=
k∑
i=1
ϵi log|zi| by equation (3.1)
= Re
k∑
i=1
ϵi logzi,
as desired. □
Recall, from Section 3, that an angle structure onτ corresponds to solving the
imaginary part of the edge gluing equations. By Proposition 5.4, solving the real
part of each edge equation amounts to having vanishing derivative in the direction
of the corresponding deformation. This turns out to be the crucial step in the proof
of Theorem 1.2.
Theorem 1.2. Let M be an orientable3–manifold with boundary consisting of
tori, and letτ be an ideal triangulation ofM.T h e nap o i n tp ∈A (τ) corresponds
to a complete hyperbolic metric on the interior ofM if and only ifp is a critical
point of the functionalV : A(τ) → R.
Proof. For one direction of the theorem, suppose thatp ∈A (τ) is a critical
point of V. This angle structure deﬁnes a shape parameter on each tetrahedron
of τ. By Proposition 2.5, proving that these shape parameters give a complete
hyperbolic metric onM amounts to checking the edge and completeness equations
of Deﬁnition 2.4.
First, consider the edge equation about an edgee. Notethat the imaginary part
ofthegluing equationaboutedge eisautomaticallysatisﬁedforanyanglestructure.
To check the real part of the gluing equation, letσ ⊂ ∂M be a normal closed curve
encircling one endpoint ofe.S i n c ep is a critical point ofV, Proposition 5.4 implies
that Re(H(σ)) = 0, as desired. Thus the edge gluing equations are satisﬁed.
To check completeness, letC be a boundary torus ofM, and letσ
1,σ2 beapair
of simple closed normal curves that spanπ1(C)= H1(C). Recall thatC is tiled by
boundary triangles that truncate the tips of ideal tetrahedra. The angle structurep
gives each of these triangles a Euclidean shape, well-deﬁned up to similarity. If Δ is
a triangle in whichσ
1 and σ2 intersect, we may place the corners of Δ at 0,1,z ∈ C,
and develop the other triangles ofC from there. Note that, since the edge gluing
176
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 19
equations are satisﬁed, the boundary triangles ﬁt together correctly around every
vertex ofC.
Let d1 and d2 be the deck transformations of~C corresponding to σ1 and σ2.
Consider the complex numbers
q = d1(0),r = d2(0),s = d1(r)= d2(q).
The four points 0,q,r,s form four corners of a fundamental domain forC.B yt h e
deﬁnition of holonomy (Deﬁnition 2.3) and the solution to the edge equations,
H(σ1) = logs−q
r−0 ,H (σ2) = logs−r
q −0 .
By Proposition 5.4, the real part of each of these holonomies is 0. Thus we have
|s−q| = |r| and |s−r| = |q|, hence the fundamental domain ofC is a parallelo-
gram. Therefore,H(σ1)= H(σ2) = 0, and the completeness equations are satisﬁed
for cuspC.
For the converse implication of the theorem, suppose thatp ∈A (τ) deﬁnes a
complete metric. Then the tetrahedron shapes corresponding top must satisfy all
the edge and completeness equations of Deﬁnition 2.4: we must haveH(σ)=2 πi
for every closed curve σ encircling an endpoint of an edge, and H(σj)=0f o r
a collection of simple closed curvesσ1,...,σ 2k that form a basis ofH1(∂M). In
particular, the real part of each of these holonomies is 0. But, by Proposition
4.6, the leading–trailing deformations that correspond to these closed curves span
T
pA(τ). Thusp is a critical point ofV, as desired. □
