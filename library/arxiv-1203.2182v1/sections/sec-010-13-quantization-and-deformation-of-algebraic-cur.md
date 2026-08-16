---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-010-13-quantization-and-deformation-of-algebraic-cur
section_title: "Quantization and deformation of algebraic curves"
section_number: 1.3
pages: 4-6
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
The above structure – and its “reﬁnement” that we are going to construct – is not limited
to applications in knot theory. Similar mathematical struc ture appears in matrix models
[8, 9, 10], in four-dimensional N = 2 supersymmetric gauge theories [11, 12, 13, 14], and in
topological string theory [15, 16, 17, 18].
1Although diﬀerent choices of polarization will not play an i mportant role in the present paper, the interested
reader may consult e.g. [6, 7] for further details.
– 3 –
In all of these problems, the semiclassical limit is describ ed by a certain “spectral curve”
(1.4) deﬁned by the zero locus of A(x,y ). Motivated by application to knots, we shall refer
to the function A(x,y ) as the A-polynomial even in situations where its form is not at all
polynomial.
ref
A  (x,y;t)
A(x,y;q) A  (x,y;q,t)
ref
quantization
deformation ("categorification")
q=1
t=−1
t=−1
deformation ("categorification")
A(x,y)
quantization
q=1
Figure 1: Deformation and quantization of the A-polynomial. The horizontal arrows describe a
deformation / reﬁnement, such that the unreﬁned case corresp onds to t = −1. The vertical arrows
represent quantization, i.e. a lift of classical polynomials A(x,y ) and A(x,y ;t) to quantum operators.
Furthermore, in most of these problems the classical curve ( 1.4) admits two canonical
deformations with the corresponding parameters q and t. The ﬁrst one is the deformation
quantization in whichx andy turn into non-commutative generators of the Weyl algebra, cf.
(1.7). The second deformation, parametrized by t, does not aﬀect commutativity of x andy,
i.e. it is an ordinary deformation. How these deformations aﬀect t he classical curve deﬁned
by the zero locus of A(x,y ) is illustrated in Figure 1.
A systematic procedure for lifting the polynomial A(x,y ) to the quantum operator
ˆA(ˆx,ˆy;q) is described in [7] for curves coming from triangulated 3-manifolds and, more gener-
ally, in [19] for abstract curves deﬁned by the equation A(x,y ) = 0. The general approach of
[19] is based on the topological recursion, which allows to c ompute ˆA(ˆx,ˆy;q) order by order
in the q-expansion following the steps of [20, 21, 22, 23, 24] where s imilar computations of
the partition function were discussed. Thus, under favorab le conditions described in [19], the
quantum operator
ˆA(ˆx,ˆy;q) =
∑
m,n
am,nqcm,nˆxmˆyn (1.8)
can be obtained simply from the data{am,n} of the original polynomialA(x,y ) =∑ am,nxmyn
and from the data {cm,n} of the Bergman kernelB(u1,u 2) which, for curves of arbitrary genus,
is given by a derivative of the logarithm of the odd characteristic theta function. Speciﬁcally,
given the Bergman kernel B(u1,u 2) for the classical curve (1.4), one can ﬁrst compute the
– 4 –
“torsion” T (u),
logT (u) = lim
u1→u2=u
∫ ( du1du2
(u1 −u2)2 −B(u1,u 2)
)
, (1.9)
and then ﬁnd the exponents {cm,n} by solving
∑
m,n
am,ncm,nxmyn = 1
2
(∂uA
∂vA∂2
v + ∂uT
T ∂v
)
A (1.10)
together with A(x,y ) = 0. Substituting the resulting data {cm,n} into (1.8) gives the quanti-
zation of A(x,y ). In the above equations we used the relations
x =eu, y =ev. (1.11)
In this paper, our main focus will be the deformation in the ot her direction, associated
with the parameter t. Some prominent examples of classical A-polynomials and their t-
deformations which we ﬁnd are given in table 1. Important exa mples of quantum reﬁned
A-polynomials, which we will derive in this paper, are reveal ed in table 2.
⏐
⏐
⏐ Model
A(x,y )
⏐
⏐
⏐ Aref(x,y ;t)
⏐
⏐
⏐ unknot
(1 −x)(1 −y)
⏐
⏐
⏐ (1 +t3x)(−t−3)1/2 − (1 −x)y
⏐
⏐
⏐ trefoil
(y − 1)(y +x3)
⏐
⏐
⏐ y2 − 1−xt2+x3t5+x4t6+2x2t2(t+1)
1+xt3 y + (x−1)x3t4
1+xt3
⏐
⏐
⏐ tetrahedron
1 −y +x(−y)f
⏐
⏐
⏐ 1 +ty −tx(−y)f
⏐
⏐
⏐ conifold
1 −y +x(−y)f +Qx(−y)f +1
⏐
⏐
⏐ 1 +ty −tx(−y)f +Q√
−tx (−y)f +1
T able 1: Classical curves in prominent examples, in unreﬁned limit (which are we ll known, left
column) and for general t (derived in this paper, right column). In this paper we also derive reﬁ ned
A-polynomials for general T 2,2p+1 torus knots; for explicit examples for low values of p see table 3.
Note that in section 4 the deformation parameter t is identiﬁed with −q1 (when q2 =q = 1).
