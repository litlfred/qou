---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-018-5-volume-maximization
section_title: "Volume maximization"
section_number: 5
pages: 16-18
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
In this section, we show how volume considerations give a way to turn an angle
structure into a genuine hyperbolic metric onM. To compute the volume of an
ideal hyperbolic tetrahedron, recall the Lobachevsky function L : R → R.I t s
deﬁnition is
(5.1) L(x)= −
∫x
0
log|2sin t|dt.
Lemma 5.1. The Lobachevsky function L(x) is well deﬁned and continuous
on R (even though the deﬁning integral is improper), and periodic with periodπ.
Furthermore, ifT is a hyperbolic ideal tetrahedron with dihedral anglesα,β,γ ,i t s
volume satisﬁes
vol(T)= L(α)+ L(β)+ L(γ).
Proof. See, for example, Milnor [19]. □
Following Lemma 5.1, we may deﬁne the volume of an angle structure in a
natural way.
Definition 5.2. Let τ be an ideal triangulation ofM, containingn tetrahedra.
Let A(τ) ⊂ R3n be the polytope of angle structures onM. Then we deﬁne avolume
functional V : A(τ) → R, by assigning to a pointp =( p1,...,p 3n)t h er e a ln u m b e r
V(p)= L(p1)+ ... +L(p3n).
By Lemma 5.1,V(p) is equal to the sum of the volumes of the hyperbolic tetrahedra
associated to the angle structurep.
174
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES 17
Lemma 5.3. Let p =( p1,...,p 3n) ∈A (τ) be an angle structure onτ,a n dl e t
w =( w1,...,w 3n) ∈ TpA(τ) be a nonzero tangent vector atp. Then the ﬁrst two
derivatives ofV(p) satisfy
∂V
∂w =
3n∑
i=1
−wi logsin pi and ∂2V
∂w2 < 0.
In particular,V is strictly concave down onA(τ).
Proof. Since the deﬁnition ofV is linear over the tetrahedra inτ, it suﬃces
to consider the volume of one tetrahedron. Thus, suppose that a tetrahedronT
has anglesp1,p2,p3 > 0, which are changing at ratesw1,w2,w3. Note that, since
the tangent vectorw must preserve the angle sum in each tetrahedron, we have
w1 +w2 +w3 = 0. We may also assume that at least one (hence, at least two) of
the wi are nonzero. Then, by equation (5.1) and Lemma 5.1,
∂vol(T)
∂w =
3∑
i=1
−wi log|2sin pi| =
3∑
i=1
−wi logsin pi,
because all sines are positive and∑wi log2 = 0. This completes the computation
of the ﬁrst derivative.
To compute the second derivative, assume by symmetry thatp1,p2 <π /2.
Diﬀerentiating vol(T) a second time, we get
− ∂2vol(T)
∂w2 = w2
1 cotp1 +w2
2 cotp2 +w2
3 cotp3
= w2
1 cotp1 +w2
2 cotp2 +(w1 +w2)21−cotp1 cotp2
cotp1 +cot p2
= (w1 +w2)2 +(w1 cotp1 −w2 cotp2)2
cotp1 +cot p2
≥ 0.
In fact, the numerator in the next-to-last line must be strictly positive. For the
n u m e r a t o rt ob e0 ,w em u s th a v ew1 = −w2, hence cotp1 = −cotp2, which is im-
possible whenp1,p2 ∈ (0,π/2). Thus∂2vol(T)/∂w2 < 0, and the volume functional
V is also strictly concave down. □
By Lemma 5.3, the only potential critical point ofV is a global maximum. As
the next proposition shows, derivatives ofV are closely connected to the holonomy
of curves on∂M.
Proposition 5.4. Let C b eac u s pt o r u so fM, with a tessellation by boundary
triangles coming fromτ.L e tσ ⊂ C be an oriented normal closed curve. Recall the
holonomy H(σ) from Deﬁnition 2.3 and the tangent vectorw(σ) ∈ TpA(τ) from
Deﬁnition 4.1.
Then for every pointp ∈A (τ), we have
∂V
∂w(σ) = Re(H(σ)).
Proof. Let σ1,...,σ k be the segments ofσ, with σi contained in boundary
triangle Δi.F o re a c hi,l a b e lt h ea n g l e so fΔi as αi,βi,γi, in clockwise order, such
175
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
