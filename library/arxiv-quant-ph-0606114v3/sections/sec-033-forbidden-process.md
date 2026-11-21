---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-033-forbidden-process
section_title: "Forbidden Process"
section_number: null
pages: 70-80
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Process
Figure 47 - Fibonacci Particle as 2-Projector
Note that in Figure 47 we have adopted a single strand notation for the particle
interactions, with a solid strand corresponding to the marked particle, a dotted
strand (or nothing) corresponding to the unmarked particle. A dark vertex
indicates either an interaction point, or it may be used to indicate the single
strand is shorthand for two ordinary strands. Remember that these are all
shorthand expressions for underlying bracket polynomial calculations.
In Figures 48, 49, 50, 51, 52 and 53 we have provided complete diagram-
matic calculations of all of the relevant small nets and evaluations that are
useful in the two-strand theory that is being used here. The reader may wish
to skip directly to Figure 54 where we determine the form of the recoupling
coeﬃcients for this theory. We will discuss the resulting algebra below.
For the reader who does not want to skip the next collection of Figures,
here is a guided tour. Figure 48 illustrates three three basic nets in case of
two strands. These are the theta, delta and tetrahedron nets. In this Figure
we have shown the decomposition on the theta and delta nets in terms of 2-
projectors. The Tetrahedron net will be similarly decomposed in Figures 52
and 53. The theta net is denoted Θ, the delta by ∆, and the tetrahedron by T.
In Figure 49 we illustrate how a pedant loop has a zero evaluation. In Figure
50 we use the identity in Figure 49 to show how an interior loop (formed by
two trivalent vertices) can be removed and replaced by a factor of Θ/∆. Note
how, in this ﬁgure, line two proves that one network is a multiple of the other,
while line three determines the value of the multiple by closing both nets.
Figure 51 illustrates the explicit calculation of the delta and theta nets. The
ﬁgure begins with a calculation of the result of closing a single strand of the
2-projector. The result is a single stand multiplied by (δ −1/δ) where δ =
−A2 −A−2, and A is the bracket polynomial parameter. We then ﬁnd that
∆= δ2 −1
and
Θ = (δ −1/δ)2δ −∆/δ = (δ −1/δ)(δ2 −2).
Figures 52 and 53 illustrate the calculation of the value of the tetrahedral
network T. The reader should note the ﬁrst line of Figure 52 where the tetrad-
edral net is translated into a pattern of 2-projectors, and simpliﬁed. The rest
of these two ﬁgures are a diagrammatic calculation, using the expansion for-
mula for the 2-projector. At the end of Figure 53 we obtain the formula for
the tetrahedron
T = (δ −1/δ)2(δ2 −2) −2Θ/δ.
=
=
Θ =
=
=
=
∆
Τ
Figure 48 - Theta, Delta and Tetrahedron
=
=
=
=
0
−1/δ
Figure 49 - LoopEvaluation–1
=
=
=
=
=
=
Θ
∆
=
Θ ∆
=
/
x
y
+
x
x
x
x
Θ ∆
=
/
x
Figure 50 - LoopEvaluation–2
=
Θ
=
=
=
∆
=
− 1/δ
=
(δ − 1/δ)
(δ − 1/δ)
(δ − 1/δ) δ
=
∆
δ    − 1
2
=
− 1/δ
= (δ − 1/δ)
δ
2
− ∆/δ
Θ
Figure 51 - Calculate Theta, Delta
=
=
Τ
=
=
− 1/δ
=
− Θ/δ =
− 1/δ
− Θ/δ
=
− (1/δ)
− Θ/δ
(δ − 1/δ)    δ
2
Figure 52 - Calculate Tetrahedron – 1
=
− (1/δ)
− Θ/δ
(δ − 1/δ)    δ
2
=
− 1/δ
− Θ/δ
− (δ − 1/δ)    
2
Τ
=
(δ − 1/δ)    δ
3
− (1/δ)Θ 
− Θ/δ
− (δ − 1/δ)    
2
=
(δ − 1/δ)    (δ    − 2)    −  2Θ/δ
2
2
Figure 53 - Calculate Tetrahedron – 2
Figure 54 is the key calculation for this model. In this ﬁgure we assume that
the recoupling formulas involve only 0 and 2 strands, with 0 corresponding to
the null particle and 2 corresponding to the 2-projector. (2+2 = 4 is forbidden
as in Figure 47.) From this assumption we calculate that the recoupling matrix
is given by
F =
 
a
b
c
d
!
=
 
1/∆
∆/Θ
Θ/∆2
T∆/Θ2
!
a
b
c
d
+
+
=
=
a
=
a = 1/∆
b
=
Θ 
Θ    /∆
2
= b
b = ∆/Θ
= c
c =
2
= d
=
d
Τ ∆/Θ 2
Θ/∆
Figure 54 - Recoupling for 2-Projectors
-
+
+
-
=
+
+
=
=
A-1
=
A-1
= -A3
= -A-4
−1/δ
2
+(2/δ    )
Figure 55 - Braiding at the Three-Vertex
=
=
=
− 1/δ
=
− 1/δ
-A3
=
− 1/δ
-A3
=
= -A3
=
− 1/δ
A6
= A
1 - A
2
-4
 + (            )
=
− 1/δ
A8(
)
= A8
Figure 56 - Braiding at the Null-Three-Vertex
Figures 55 and 56 work out the exact formulas for the braiding at a three-vertex
in this theory. When the 3-vertex has three marked lines, then the braiding
operator is multiplication by −A4, as in Figure 55. When the 3-vertex has two
marked lines, then the braiding operator is multiplication by A8, as shown in
Figure 56.
Notice that it follows from the symmetry of the diagrammatic recoupling for-
mulas of Figure 54 that the square of the recoupling matrix F is equal to the
identity. That is,
 
1
0
0
1
!
= F 2 =
 
1/∆
∆/Θ
Θ/∆2
T∆/Θ2
! 
1/∆
∆/Θ
Θ/∆2
T∆/Θ2
!
=
 
1/∆2 + 1/∆
1/Θ + T∆2/Θ3
Θ/∆3 + T/(∆Θ)
1/∆+ ∆2T 2/Θ4
!
.
Thus we need the relation
1/∆+ 1/∆2 = 1.
This is equivalent to saying that
∆2 = 1 + ∆,
a quadratic equation whose solutions are
∆= (1 ±
√
5)/2.
Furthermore, we know that
∆= δ2 −1
from Figure 51. Hence
∆2 = ∆+ 1 = δ2.
We shall now specialize to the case where
∆= δ = (1 +
√
5)/2,
leaving the other cases for the exploration of the reader. We then take
A = e3πi/5
so that
δ = −A2 −A−2 = −2cos(6π/5) = (1 +
√
5)/2.
Note that δ −1/δ = 1. Thus
Θ = (δ −1/δ)2δ −∆/δ = δ −1.
and
T = (δ −1/δ)2(δ2 −2) −2Θ/δ = (δ2 −2) −2(δ −1)/δ
= (δ −1)(δ −2)/δ = 3δ −5.
Note that
T = −Θ2/∆2,
from which it follows immediately that
F 2 = I.
This proves that we can satisfy this model when ∆= δ = (1 +
√
5)/2.
For this specialization we see that the matrix F becomes
F =
 
1/∆
∆/Θ
Θ/∆2
T∆/Θ2
!
=
 
1/∆
∆/Θ
Θ/∆2
(−Θ2/∆2)∆/Θ2
!
=
 
1/∆
∆/Θ
Θ/∆2
−1/∆
!
This version of F has square equal to the identity independent of the value of
Θ, so long as ∆2 = ∆+ 1.
The Final Adjustment. Our last version of F suﬀers from a lack of symme-
try. It is not a symmetric matrix, and hence not unitary. A ﬁnal adjustment
of the model gives this desired symmetry. Consider the result of replacing each
trivalent vertex (with three 2-projector strands) by a multiple by a given quan-
tity α. Since the Θ has two vertices, it will be multiplied by α2. Similarly, the
tetradhedron T will be multiplied by α4. The ∆and the δ will be unchanged.
Other properties of the model will remain unchanged. The new recoupling
matrix, after such an adjustment is made, becomes
 
1/∆
∆/α2Θ
α2Θ/∆2
−1/∆
!
For symmetry we require
∆/(α2Θ) = α2Θ/∆2.
We take
α2 =
√
∆3/Θ.
With this choice of α we have
∆/(α2Θ) = ∆Θ/(Θ
√
∆3) = 1/
√
∆.
Hence the new symmetric F is given by the equation
F =
 
1/∆
1/
√
∆
1/
√
∆
−1/∆
!
=
 
τ
√τ
√τ
−τ
!
where ∆is the golden ratio and τ = 1/∆. This gives the Fibonacci model.
Using Figures 55 and 56, we have that the local braiding matrix for the model
is given by the formula below with A = e3πi/5.
R =
 
−A4
0
0
A8
!
=
 
e4πi/5
0
0
−e2πi/5
!
.
The simplest example of a braid group representation arising from this
theory is the representation of the three strand braid group generated by S1 =
R and S2 = FRF (Remember that F = F T = F −1.). The matrices S1 and S2
are both unitary, and they generate a dense subset of the unitary group U(2),
supplying the ﬁrst part of the transformations needed for quantum computing.
10
