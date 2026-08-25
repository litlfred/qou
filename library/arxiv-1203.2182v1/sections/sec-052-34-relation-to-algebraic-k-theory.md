---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-052-34-relation-to-algebraic-k-theory
section_title: "Relation to algebraic K-theory"
section_number: 3.4
pages: 50-52
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
So far in this section we have discovered a number of reﬁned A-polynomials Aref(x,y ;t)
for various knots, including the unknot (3.105), the trefoi l knot (3.160), and more general
(2, 2p + 1) torus knots discussed in section 3.3.3. For the unknot an d for the trefoil knot we
also found an explicit form of the quantum A-polynomial, given respectively in (3.104) and
(3.134).
There is no doubt that such reﬁned and quantum A-polynomials exist for other knots
as well, and can be determined either by (generalizations of ) the techniques we used here
or via some other methods. In any case, when lifting the class ical t-deformed A-polynomial
to a quantum operator, one encounters an important subtlety : not all classical curves are
quantizable, and the existence of a consistent quantum curv e depends in a delicate way on
the complex structure 12 (i.e. on the coeﬃcients in the deﬁning equation) of the classical
polynomial Aref(x,y ;t). Therefore, one should always verify whether a classical t-deformed
curve actually admits a consistent quantization.
We should stress that this issue of quantizability is much mo re delicate for reﬁned A-
polynomials compared to the ordinary ones. The coeﬃcients o f ordinary A-polynomials are
merely integer numbers, and quantizability imposes non-trivial constraints on these numbers.
Magically, all A-polynomials of knots and 3-manifolds automatically meet t hese conditions.
In retrospect, this is not too surprising, for otherwise SL(2, C) Chern-Simons would simply
make no sense on 3-manifolds whose A-polynomials fail to meet these constraints [3].
The coeﬃcients of reﬁnedA-polynomials, on the other hand, are functions of an arbitrary
continuous parameter t. Hence, at ﬁrst it may not be entirely obvious how to reconcil e
arbitrariness of t with the fact that certain functions of this parameter shoul d satisfy rather
strong constraints. In all examples that we have analyzed, s omething beautiful happens: as
we explain below, it turns out that t can be any root of unity. Therefore, it is also natural
to think of ℏ = logq as a purely imaginary number, valued in iQ. We conjecture that this is
12At ﬁrst, this may seem a little surprising, because the quant ization problem is about symplectic geometry
and not about complex geometry of C. (Figuratively speaking, quantization aims to replace all classical objects
in symplectic geometry by the corresponding quantum analog s.) However, our phase space C∗ × C∗ is very
special in a sense that it comes equipped with a whole CP1 worth of complex and symplectic structures, so
that each aspect of the geometry can be looked at in several di ﬀerent ways, depending on which complex or
symplectic structure we choose. This hyper-K¨ ahler nature of our geometry is responsible, for example, for the
fact that a curve C “appears” to be holomorphic (or algebraic). We put the word “ appears” in quotes because
this property of C is merely an accident, caused by the hyper-K¨ ahler structur e on the ambient space, and is
completely irrelevant from the viewpoint of quantization. What is important to the quantization problem is
that C is Lagrangian with respect to the symplectic form Ω = i
ℏ
dx
x ∧ dy
y .
– 49 –
a general phenomenon: for any knot, quantizability of the re ﬁned A-polynomial Aref(x,y ;t)
requires t to be a root of unity. This statement could be veriﬁed if new ex amples of reﬁned
A-polynomials are found or, conversely, this property could help in ﬁnding new examples of
reﬁned A-polynomials.
Before we explain the condition ont, let us recall in more detail the general quantizability
criteria for curves [3]. Let us consider a curve (1.4):
C :
{
(x,y ) ∈ C∗ × C∗
⏐
⏐
⏐A(x,y ) = 0
}
, (3.197)
and the corresponding partition function Z = exp( 1
ℏS0 +... ) = exp( 1
ℏ
∫
logy dx
x +... ), as in
(2.6). One has to make sure that this partition function is we ll deﬁned, which means that all
periods of the 1-form Im log y dx
x on the curve C are trivial,
∮
γ
(
log |x|d(argy) − log |y|d(argx)
)
= 0 , (3.198)
and that the periods of the 1-form Re log y dx
x are rational multiples of 2 πi, so that for all
closed paths γ on the curve C
1
4π2
∮
γ
(
log |x|d log |y| + (argy)d(argx)
)
∈ Q. (3.199)
The above conditions can be nicely reformulated in terms of a lgebraic K-theory [19]. Thus,
the integrand η(x,y ) = log |x|d(argy) − log |y|d(argx) in (3.198) is the image of the symbol
{x,y } ∈ K2(C) under the regulator map [69, 70]. For curves it is not hard to see that η(x,y )
is closed, dη = 0. However, the condition (3.198) means that η(x,y ) must actually be exact.
In the language of algebraic K-theory, this means that the sy mbol {x,y } = 0 must be trivial
in K2(C(C)) ⊗ Q. This led two of the authors of the present paper to propose th e following
criterion for quantizability [19]:
C is quantizable ⇐ ⇒ { x,y } ∈ K2(C(C)) is a torsion class. (3.200)
Moreover, it is known that the above condition is equivalent to the existence of a decompo-
sition [71]
x ∧y =
∑
i
rizi ∧ (1 −zi) in ∧2 (C(C)∗) ⊗ Q (3.201)
for some zi ∈ C(C)∗ and ri ∈ Q. In turn, this also means that [71]:
A(x,y ) is tempered, i.e. the roots of all its face polynomials are roots of unity. (3.2 02)
By face polynomials we mean the following. We construct a New ton polygon corresponding
toA(x,y ) =∑
i,jc(i,j)xiyj, and to each point (i,j ) of this polygon we associate the coeﬃcient
c(i,j). Then, each face of the polygon consists of several points la beled, in order, by k =
0, 1, 2,... , so that the corresponding monomial coeﬃcients for a given f ace can be relabeled
asck =c(i,j). The face polynomial is deﬁned, then, as f(z) =∑
kckzk. The condition (3.202)
states that all roots of face polynomials f(z), constructed for all boundaries of the Newton
polygon, must be roots of unity. It is this latter condition t hat we shall consider below in
order to test quantizability of the reﬁned A-polynomials.
– 50 –
