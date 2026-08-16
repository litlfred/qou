---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-014-26-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 26
pages: 26-28
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
and so on. In terms of this basis, one checks by an easy inducti on argument that
pn =tn − Σ n
k=2(−1)k(k − 1)
(
n
k
)
xktn−k,
so the ﬁrst few polynomials are:
1
t
t2 −x
t3 − 3xt + 2y
t4 − 6xt2 + 8yt − 3x2
t5 − 10xt3 + 20yt2 − 15x2t + 4xy
t6 − 15xt4 + 40yt3 − 45x2t2 + 24xyt − 5x3
t7 − 21xt5 + 70yt4 − 105x2t3 + 84xyt2 − 35x3t + 6(x2y − b
2y).
This is a bit cleaner than the formulas in [ DW], mostly because we set the sum of
the roots in the Weierstrass equation of E to 0. A more-or-less equivalent solution
was given already in [ T], where the generating function for the pn was written in
terms of theta functions and exponentials on E. A slightly diﬀerent (but equivalent)
set of polynomials was given in [ IM1].
Elliptic solitons
It is curious to note that the same system arises in several ra ther diﬀerent
contexts. Here is a brief outline of one of these, following t he work of Treibich and
Verdier [T], [ TV].
Finite dimensional solutions of the KP hierarchy (= inﬁnite dimensional in-
tegrable system) are well understood. They are parametrize d by Krichever data,
consisting of a curve C, a point p ∈ C, a line bundle L, and local trivializations.
Such data determine a point in the total space of the hierarch y with the property
that the inﬁnite collection of commuting KP ﬂows emanating f rom the point sweep
out only a ﬁnite dimensional space, isomorphic to J(C). The curve C, the point p
and the trivializations remain ﬁxed, while L moves freely in J(C).
An elliptic soliton is a ﬁnite dimensional solution of KP in w hich the ﬁrst ﬂow,
KP 1, already closes up, i.e. evolves on an elliptic curve inside the possibly larger
Jacobian J(C). The direction of KP 1, for points coming from Krichever data, is
the tangent vector at p to the Abel-Jacobi image of C in J(C). So the condition
is that J(C) should contain an elliptic curve E which is tangent at AJ(p) to the
Abel-Jacobi image AJ(C).
Start with an n-sheeted branched cover π : C → E and a point p ∈ E with
local coordinate ξ. Let π∗(p) = q0 + · · · +qn−1, and let ξi := ξ ◦π near qi. The
tangent vector ti :=∂/∂ξ i lives naturally in Γ( Oqi (qi)). Its image
(AJ)∗ti ∈TAJ(qi)J(C)
can then be identiﬁed with the image of ti under the coboundary map δ for the
sequence
0 → OC → OC(qi) → Oqi(qi) → 0.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 27
Similarly, the tangent atπ∗p to the image π∗E ofE inJ(C) is given by Σ n−1
i=0δ(ti) =
δ(Σ n−1
i=0ti). The tangency condition then says that δ(Σ n−1
i=0ti) is proportional toδ(t0),
and therefore equal (by the residue theorem) to δ(nt0). This happens if and only
if there is some f ∈ Γ( O(π∗p)) with
Resqi (fπ ∗dz) =
{ 1 1 ≤i ≤n − 1
1 −n i = 0,
where dz is a non-zero closed 1-form on E. This is equivalent to saying that
π : C → E is one of our spectral curves, and fπ ∗dz becomes the Seiberg-Witten
diﬀerential.
T ests
What makes this description of SYM with adjoint matter convi ncing for a
physicist, is that it can be “tested” by working out various l imits and special cases,
and that it yields results consistent with the “predictions ” based on the expected
behavior of the physical system. We outline some of these tes ts.
Consistency with Seiberg-Witten
Forn = 2, with given E and m, our system produces a 1-parameter family of
double coversCu →E. Each Cu has genus 2, and the integrable system is the family
of 1-dimensional Pryms. Write the equation of E asy2 = Π 3
i=1(x−ei) = x3 +bx−c,
with∑ ei = 0 as before. The cover Cu is given explicitly in terms of our polynomials
pi as:
0 = p2 +up0 =t2 −x +u.
Its Galois group over the P1 with coordinate x is Z2 × Z2, with involutions α :y ↦→
−y, ,β :t ↦→ −t, and αβ. The quotients are a rational curve (with coordinate t);
the original E; and another elliptic curve Eu, respectively.
P I1:(x)
α β
:(x,t)/(x=tP I1 2+u)
α β
C  :(x,y,t)/(y  =  (x-e  ),t  =x-u)u
2
E  :(x,z=yt)/(z  =(x-u)   (x-e  ))2u
i
E:(x,y)/(y  =   (x-e  ))Π2
Π
Π
2
i i
The Prym can then be identiﬁed with Eu.
The original Seiberg-Witten solution is given directly as t he family of elliptic
curvesE′
u, double covers of P1 branched at eiu +e2
i (i = 1, 2, 3) and ∞ ([SW2],
eq. (16.17)). These are indeed isomorphic to our Eu: the transformation
x ↦→(u2 +b)x −c
u −x
takes the ei and u to eiu +e2
i and ∞, respectively.
Mass to zero: the N=4 limit
The limit m → 0 of N = 2 SYM with gauge group G and adjoint matter is
known to acquire a higher form of supersymmetry: it is the N = 4 SYM theory,
with the same gauge group. (A physicist might rather say that two of the four
