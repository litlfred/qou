---
doc_id: arxiv-2507.12454v1
doc_title: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT"
section_id: sec-001-2-fricke-klein-example
section_title: "Fricke-Klein example"
section_number: 2
pages: 3-8
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
doc_brief: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of"
---
2.1. Equations. This example was essentially worked out in [FK65]. Let k = 4, n = 2.
Let a1,...,a 4∈ C\{− 2, 2}. Let us try to parameterize all 4-tuples of 2 × 2 matrices
M1,M 2,M 3,M 4∈ GL2(C), up to conjugation, satisfying
4Y
i=1
Mi =I2, detMi = 1, trMi =ai.
Let x = tr(M1M2), y = tr(M1M3), z = tr(M2M3). The following code computes the ideal
of relations between x,y,z :
R.<m111,m112,m121,a1,m211,m212,m221,a2,m311,m312,m321,a3,x,y,z,a4>=QQ[]
M1=matrix(2,2,[m111,m112,m121,a1-m111])
M2=matrix(2,2,[m211,m212,m221,a2-m211])
M3=matrix(2,2,[m311,m312,m321,a3-m311])
eqns=[M1.det()-1,M2.det()-1,M3.det()-1,(M1*M2*M3).trace()-a4,(M1*M2).trace()-x, \
(M1*M3).trace()-y,(M2*M3).trace()-z]
J=R.ideal(eqns)
J.elimination_ideal([m111,m112,m121,m211,m212,m221,m311,m312,m321])
The output is
Ideal (a1*a2*a3*a4 - a1*a2*x - a1*a3*y - a2*a3*z + x*y*z - a3*x*a4 - a2*y*a4 - a1*z*a4
+ a1^2 + a2^2 + a3^2 + x^2 + y^2 + z^2 + a4^2 - 4) of Multivariate Polynomial Ring in
m111, m112, m121, a1, m211, m212, m221, a2, m311, m312, m321, a3, x, y, z, a4 over
Rational Field
So for each 4-tuple of matrices satisfying the conditions, the corresponding x,y,z ∈ C as
above produce a solution to the so called Markov equation with parameters a1,a 2,a 3,a 4:
(2.1) xyz +x2 +y2 +z2− (a1a2 +a3a4)x− (a1a3 +a2a4)y− (a1a4 +a2a3)z
+a1a2a3a4 +a2
1 +a2
2 +a2
3 +a2
4− 4 = 0.
Conversely, supposex,y,z ∈ C is a solution to the Markov equation. Let us see that for
generically chosen valuesa1,a 2,a 3,a 4 we can always uniquely recover the tuple of matrices,
up to conjugation.
4 ANTON MELLIT
First, we observe that knowing the traces x,y,z,a 1,a 2,a 3,a 4 we can compute the trace
of an arbitrary product of matrices M1,...,M 4 and their inverses. Indeed, given such a
product, we first replace any occurrence of M4 byM−1
3 M−1
2 M−1
1 . Then using
A−1 = tr(A)I2−A (A∈ SL2(C))
we can reduce to the situation when no inverses appear. So we have an arbitrary product
of M1,M 2,M 3. Using
BA = tr(BA)I2−A−1B−1 (A,B∈ SL2(C))
and getting rid of the inverses we rearrange terms modulo products of shorter length until
we get to a linear combination ofI2,M1,M2,M3,M1M2,M1M3,M2M3,M1M2M3 =M−1
4 ,
all of whose traces are explicitly computed in terms of x,y,z and the parameters.
Knowing the traces of arbitrary products lets us find out if any 4 products form a basis
of the space of 2×2 matrices. Indeed, because the trace pairing is non-degenerate, matrices
A1,...,A n2 form a basis of the space of n×n matrices if and only if the n2×n2 matrix of
traces tr(AiAj) is non-degenerate.
Suppose products of M1,...,M 4 do span the space of matrices, i.e. the monodromy rep-
resentation is irreducible, and we choose a basis A1,...,A 4. Knowing the traces allows us
to express any other product as a linear combination ofA1,...,A 4. In particular we recover
the ring structure on the 4-dimensional space of linear combinations of A1,...,A 4 and any
monodromy representation provides an isomorphism of this ring with the matrix ring. Any
other monodromy representation with the same traces would produce an automorphism of
the matrix ring. All automorphisms of the matrix ring are inner, i.e. related by a change
of basis transformation, and so we conclude that the monodromy representations with the
same traces are equivalent.
This was under the assumption that the monodromy representation is irreducible. If it
is not, then in some basis the matrices M1,...,M 4 are upper triangular. In this situation
we cannot determine the matrices only from the trace information. Denoting the top-left
diagonal entry of Mi by λi we must haveQ4
i=1λi = 1. On the other hand, λi is a root of
the polynomial t2−ait + 1 which has 2 roots. So this kind of situation is possible only for
special values of the parameters a1,a 2,a 3,a 4.
More precisely, we call a1,a 2,a 3,a 4 generic if none of the 16 products of the roots of
t2−ait + 1 (we pick one root from each quadratic equation) equals 1. We have seen, that
if the parameters are generic then all monodromy representations are irreducible and in
one-to-one correspondence with the solutions of the Markov equation.
COHOMOLOGY RINGS OF CHARACTER V ARIETIES 5
Figure 2. Markov’s cubic as the complement of a triangle in the projective
plane blown up at six points
2.2. Geometry of the Markov cubic. In algebraic geometry, given an algebraic variety
X, i.e. a set of solutions to a system of polynomial equations, we are usually interested
in its cohomology ring H∗(X, C). Hodge theory extended by Deligne to non-compact and
singular spaces [Del71, Del74] endows the cohomology with mixed Hodge structure. Struc-
ture constants of the ring typically encode interesting enumerative information. Sometimes
the cohomology ring as a ring itself can be an interesting object of study, perhaps making
a connection with a ring constructed in some other way in a completely different field of
mathematics.
Although the ring structure in the Fricke-Klein situation turns out to be trivial, the
cohomology already has a non-trivial mixed Hodge structure. We explain how to compute
it.
Assuming the parameters a1,a 2,a 3,a 4 ∈ C\{− 2, 2} are generic, the cubic X given
by the Markov equation (2.1) is nonsingular. Let X ⊂ CP3 be the solution set of the
homogenization of (2.1). Its affine part is X⊂ X, and the complement X\X is given
in CP2 as the solution set of the homogeneous equation xyz = 0, thus it is a union of
three lines forming a triangle. Denote this triangle by ∆. We refer to Figure 2. It is
straightforward to check that homogenization of any cubic of the form
xyz +x2 +y2 +z2 + lower degree terms
does not have any singularities at infinity. So X is a smooth cubic surface, and therefore
can be obtained as a blowup of CP2 at 6 points (for background see [Har77]). The cubic
6 ANTON MELLIT
X, as any other smooth cubic surface contains 27 projective lines. Three of them form ∆.
The intersection graph of the 27 lines is well-known and one can see that for any triangle
one can choose 6 lines which do not intersect pairwise and do not contain any of the lines
of the triangle. Each side of the triangle intersects 2 of the 6 lines. Blowing down these 6
lines we obtain a mapX→ CP2. The 3 lines of ∆ are isomorphically mapped to 3 lines on
CP2. Choosing coordinates appropriately, one can assume that f(∆) is the complement of
C∗× C∗⊂ CP2. So we have
U =f−1(C∗× C∗) = C∗× C∗⊂X,
an open subset, and the complement X\U is a disjoint union of 6 copies of C:
X = C∗× C∗⊔ C⊔···⊔ C| {z }
6 copies
.
The 6 copies of C are divided into 3 pairs according to which of the three lines of ∆ they
intersect.
2.3. Cohomology. With this picture in mind, we have several ways to compute the coho-
mology. All cohomology groups we consider have complex coefficients. From the relative
cohomology sequence for the pair C∗× C∗ =U⊂X we obtain an exact sequence
0→H1(X)→H1(U)→H2(X,U )→H2(X)→H2(U)→ 0.
Since both C and X are non-singular, by excision we have that the only non-vanishing
relative cohomology group is H2(X,U )∼= C6. So the remaining part of the long exact
sequence vanishes, except for the isomorphism H0(X)∼= H0(U)∼= C. The map C2 =
H1(U)→ H2(X,U ) = C6 is dual to the map H2(X,U )→ H1(U). Here a point class on
C corresponds to a disc class in H2(X,U ) whose boundary is a 1-cycle in U which gets
contractible inU∪ C. From the picture we see that all 1-cycles become contractible, so the
map H2(X,U )→H1(U) is surjective, the dual map is injective and we have H1(X) = 0,
H2(X) is an extension of H2(U) = C byH2(X,U )/H1(U)∼= C4.
This is reflected by the weight filtration onH2(X). The cohomology H2(X,U )/H1(U)⊂
H2(X) as a mixed Hodge structure is pure of weight 2, while H2(U) has weight 4. Thus
we have W2 =H2(X,U )/H1(U)⊂H2(X) with dimW2 = 4, W3 =W2, and W4 =H2(X)
with dimW4/W2 = 1.
Another way to compute the cohomology is to use the compactification. Let us denote
X0 =X, X1 =X0\ CP1, X2 =X0\ (CP1∪ CP1), X3 =X0\ ∆, so that we pass from Xi
COHOMOLOGY RINGS OF CHARACTER V ARIETIES 7
H∗ WiHi Wi+2Hi/WiHi
H2 C4 =⟨c1(Li)|i = 1, 2, 3, 4⟩ C =⟨ω = symplectic form⟩
H0 C =⟨1⟩
Figure 3. Cohomology of the Markov cubic
to Xi+1 by removing a line. This leads to exact sequences for each i:
0→H1(Xi+1)→H2(Xi,Xi+1)→H2(Xi)→H2(Xi+1)→H3(Xi,Xi+1)→ 0
0→H3(Xi+1)→H4(Xi,Xi+1)→H4(Xi)→H4(Xi+1)→ 0,
as we will see that the even cohomologies of Xi vanish at each step. At each step we will
use thatHk(Xi,Xi+1) =Hk−2(Xi\Xi+1) by excision, which is non-zero only fork = 0, 1, 2.
Initially we haveH0(X0) = C,H2(X0) = C7 (represented by 7 algebraic cycles: the line in
CP2 and the 6 exceptional curves), H4(X0) = C, all other cohomologies vanish.
Fori = 0 we have X0\X1 = CP1, which has H0 = C andH2 = C. These coincide with
H2(X0,X 1) andH4(X0,X 1) respectively and we see that inH2(X1) and inH4(X1) we have
one less dimension than in H2(X0), respectively H4(X0). So H4(X1) = 0, H2(X1) = C6.
Fori = 1 we have X1\X2 = C, which only has H0 = C. So we have that X2 has one
dimension less in H2(X2), nothing else changes: H2(X1) = C5.
Finally, for i = 2 we have X2\X3 = C∗, which has H0 = C and H1 = C, contributing
to H2(X2,X 3) and H3(X2,X 3) correspondingly. Thus two things happen. First, only 4
dimensions from H2(X2) out of 5 contribute to H2(X3). On the other hand, one extra
dimension comes from H3(X3,X 2). The net total is H2(X3) = C5, as in X2, but the
nature of the 5 dimensions is different, and correspondingly the weights are different. The
4 dimensions coming from H2(X2) have weight 2, and this is reflected by the fact that
they are represented by algebraic cycles. The remaining class has weight 4 as it comes
from H3(X3,X 2). The weight of H1(C∗) is 2, but it gets increased by 2 when we pass to
H3(X3,X 2).
These findings can be summarized in the table on Figure 3.
The 4 algebraic classes in H2(X) can be represented by characteristic classes of line
bundles. The extra class can be represented by an explicit holomorphic symplectic form
as explained below. Using the natural coordinates on C∗× C∗, the form is written as
ω = dx
x ∧ dy
y ,
and one can verify that the form extends to the whole of X.
8 ANTON MELLIT
2.4. Mixed Hodge Polynomial. From Figure 3 we obtain that the Poincar´ e polynomial
of X is 1 + 5q2 and the mixed Hodge polynomial is P (q,t ) = 1 + 4q2t2 +q2t4. We prefer
to consider a slightly different version of the mixed Hodge polynomial, without losing any
information. Let
MH(X;q,t ) :=q
1
2 dimCXP (X;q− 1
2t− 1
2,t
1
2 ).
For instance, in our running example we obtain
MH(X;q,t ) =q +t + 4.
We should also compare our calculations with the number of points on our variety over
Fq. Assuming all the lines are defined over the base field, we see that the first computation
produces
(q− 1)2 + 6q =q2 + 4q + 1.
The second computation produces
q2 + 7q + 1− (q + 1)−q− (q− 1) =q2 + 4q + 1.
In each case, one can track how the different powers of q contribute to the cohomology so
that q2 corresponds to H0 and 4q + 1 corresponds to H2.
In any case, for a general algebraic variety X, if the number of points is a polynomial of
q, we have
(2.2) |X(Fq)| =qdimCXP (X;−1,q− 1
2 ) =q
1
2 dimCXMH(X;q,q−1),
assuming MH is indeed a polynomial in q, t, which means that all the weights are even
and the cohomology is concentrated in even degrees.
