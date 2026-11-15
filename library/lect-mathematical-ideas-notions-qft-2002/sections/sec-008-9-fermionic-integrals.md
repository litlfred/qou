---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-008-9-fermionic-integrals
section_title: "Fermionic integrals"
section_number: "9"
pages: 61-67
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
9. Fermionic integrals
9.1. Bosons and fermions. In physics there exist two kinds of particles – bosons
and fermions. So far we have dealt with bosons only, but many important par-
ticles are fermions: e.g., electron, proton, etc. Thus it is important to adapt our
techniques to the fermionic case.
In quantum theory, the difference between bosons and fermions is as follows: if
the space of states of a single particle is H then the space of states of the system of
k k
k such particles is S H for bosons and  H for fermions. In classical theory, this
means that the space of states of a bosonic particle is a usual real vector space (or
more generally a manifold), while for a fermionic particle it is an odd vector space.
Mathematically “odd” means that the ring of smooth functions on this space (i.e.
the ring of classical observables) is an exterior algebra (unlike the case of a usual,
even space, for which the ring of polynomial functions is a symmeteric algebra).
More generally, one may consider systems of classical particles or fields some
of which are bosonic and some fermionic. In this case, the space of states will be
a supervector space, i.e. the direct sum of an even and an odd space (or, more
generally, a supermanifold – a notion we will define below).
When such a theory is quantized using the path integral approach, one has to
integrate functions over supermanifolds. Thus, we should learn to integrate over
supermanifolds and then generalize to this case our Feynman diagram techniques.
This is what we do in this section.
9.2. Supervector spaces. Let k be a field of characteristic zero. A supervector
space (or shortly, superspace) over k is just a Z=2-graded vector space: V = V0 
n m njm
V1. If V0 = k and V1 = k then V is denoted by k . The notions of a
homomorphism, direct sum, tensor product, dual space for supervector spaces are
defined in the same way as for Z=2-graded vector spaces. In other words, the tensor
category of supervector spaces is the same as that of Z=2-graded vector spaces.
However, the notions of a supervector space and a Z=2-graded vector space are
not the same. The difference is as follows. The category of vector (and hence Z=2-
graded vector) spaces has an additional symmetry structure, which is the standard
isomorphism V 
 W ! W 
 V (given by v 
 w ! w 
 v). This isomorphism allows
m m
one to define symmetric powers S V , exterior powers  V , etc. For supervector
spaces, there is also a symmetry V 
 W ! W 
 V , but it is defined differently.
mn
Namely, v 
 w goes to (−1) w 
 v, v 2 Vm; w 2 Vn (m; n 2 f0; 1g). In other
words, it is the same as usual except that if v; w are odd then v 
 w ! −w 
 v.
m m
As a result, we can define the superspaces S V and  V for a superspace V , but
they are not the same as the symmetric and exterior powers in the usual sense. For
m
example, if V is purely odd (V = V1), then S V is the exterior m-th power of V ,
m
and  V is the m-th symmetric power of V (purely even for even m and purely
odd for odd m).
For a superspace V , let V be the same space with opposite parity, i.e. (V )i =
V1−i, i = 0; 1. With this notation, the equalities explained in the previous para-
m m m m m m
graph can be written as: S V =  ( V ),  V =  (S V ).
Let V = V0  V1 be a finite dimensional superspace. Define the algebra of

polynomial functions on V , O(V ), to be the algebra SV (where symmetric powers
 
are taken in the super sense). Thus, O(V ) = SV0 
 V1 , where V0 and V1 are
regarded as usual spaces. More explicitly, if x1; :::; xn are linear coordinates on V0,
62 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
and 1; :::; m are linear coordinates on V1, then O(V ) = k[x1; :::; xn; 1; :::; m], with
defining relations
xixj = xjxi; xir = rxi; rs = −sr
Note that this algebra is itself a (generally, infinite dimensional) supervector space,
and is commutative in the supersense. Also, if V; W are two superspaces, then
O(V  W ) = O(V ) 
 O(W ), where the tensor product of algebras is understood in
p(b)p(c)
the supersense (i.e. (a 
 b)(c 
 d) = (−1) (ac 
 bd), where p(x) is the parity
of x).
9.3. Supermanifolds. Now assume that k = R. Then by analogy with the
above for any supervector space V we can define the algebra of smooth functions,
1 1 
C (V ) := C (V0) 
 V1 . In fact, this is a special case of the following more
general setting.
1
Definition 9.1. A supermanifold M is a usual manifold M0 with a sheaf CM of
Z=2Z graded algebras (called the structure sheaf), which is locally isomorphic to
1
CM0 
 (1; :::; m).
The manifold M0 is called the reduced manifold of M. The dimension of M is
the pair of integers dim M0jm.
For example, a supervector space V is a supermanifold of dimension dim V0j dim V1.
Another (more general) example of a supermanifold is a superdomain U := U0 V1,
1 
i.e. a domain U0  V0 together with the sheaf CU 
 V1 . Moreover, the defini-
tion of a supermanifold implies that any supermanifold is “locally isomorphic” to
a superdomain.
Let M be a supermanifold. An open set U in M is the supermanifold (U0,
1
CM jU0), where U0 is an open subset in M0.
By the definition, supermanifolds form a category SMAN . Let us describe ex-
plicitly morphisms in this category, i.e. maps F : M ! N between supermanifolds
M and N. By the definition, it suÆces to assume that M; N are superdomains, with
global coordinates x1; :::; xn; 1; :::; m, and y1; :::; yp; 1; :::; q, respectively (here xi,
yi are even variables, and i; i are odd variables). Then the map F is defined by
the formulas:
j1j2
yi = f0;i(x1; :::; xn) + f2;i (x1; :::; xn)j1j2 + :::;
j j1j2j3
i = a1;i(x1; :::; xn)j + a3;i (x1; :::; xn)j1 j2j3 + :::;
j1j2 j j1;j2;j3
where f0;i; f2;i ; a1;i; a3;i ; ::: are usual smooth functions, and we assume sum-
mation over repeated indices. These formulas, determine F completely, since for
1 1
any g 2 C (N) one can find g Æ F 2 C (M) by Taylor's formula. For exam-
1j2
ple, if M = N = R and F (x; 1; 2) = (x + 12; 1; 2), and if g = g(x), then
0
g Æ F (x; 1; 2) = g(x + 12) = g(x) + g (x)12.
1 r
Remark. For this reason, one may consider only C (and not C ) functions on
r
supermanifolds. Indeed, if for example g(x) is a C function of one variable which
Pr+1
is not differentiable r+1 times, then the expression g(x+ i=1 2i−12i) will not be
(r+1)
defined, because the coeÆcient of 1:::2r+2 in this expression should be g (x),
but this derivative does not exist.
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 63
9.4. Supermanifolds and vector bundles. Let M0 be a manifold, and E be a
vector bundle on M0. Then we can define the supermanifold M := Tot(E), the
total space of E with changed parity. Namely, the reduced manifold of M is M0,
1 
and the structure sheaf C is the sheaf of sections of E . This defines a functor
M
S : BUN ! SMAN , from the category of manifolds with vector bundles to the
category of supermanifolds. We also have a functor S in the opposite direction:
2 
namely, S(M) is the manifold M0 with the vector bundle (R=R ) , where R is the
1
nilpotent radical of C .
M
The following proposition (whose proof we leave as an exercise) gives a classifi-
cation of supermanifolds.
Proposition 9.2. SS = Id, and SS = Id on isomorphism classes of objects.
The usefulness of this proposition is limited by the fact that, as one can see from
the above description of maps between supermanifolds, SS is not the identity on
1j2
morphisms (e.g. it maps the automorphism x ! x + 12 of R to Id), and hence,
S is not an equivalence of categories. In fact, the category of supermanifolds is not
equivalent to the category of manifolds with vector bundles (namely, the category
of supermanifolds “has more morphisms”).
Remark. The relationship between these two categories is quite similar to the
relationship between the categories of (finite dimensional) filtered and graded vector
spaces, respectively (namely, for them we also have functors S, S with the same
properties – check it!). Therefore in supergeometry, it is better to avoid using
realizations of supermanifolds as S(M0; E), similarly to how in linear algebra it is
better to avoid choosing a grading on a filtered space.
9.5. Integration on superdomains. We would now like to develop integration
theory on supermanifolds. Before doing so, let us recall how it is done for usual
manifolds. In this case, one proceeds as follows.
1. Define integration of compactly supported (say, smooth) functions on a do-
n
main in R .
2. Find the transformation formula for the integral under change of coordinates
(i.e. discover the factor jJj, where J is the Jacobian).
3. Define a density on a manifold to be a quantity which is locally the same as
a function, but multiplies by jJj under coordinate change (unlike true functions,
which don't multiply by anything). Then define integral of compactly supported
functions on the manifold using partitions of unity. The independence of the integral
on the choices is guaranteed by the change of variable formula and the definition
of a density.
We will now realize this program for supermanifolds. We start with defining
integration over superdomains.
Let V = V0  V1 be a supervector space. The Berezinian of V is the line
top top 
 V0 
  V1 . Suppose that V is equipped with a nonzero element dv of the
Berezinian (called a supervolume element).
1 
Let U0 be an open set in V0, and f 2 C (U) 
 V1 be Pa compactly supported
1
smooth function on the superdomain U := U0 V1 (i.e. f = fi 
!i, fi 2 C (U),

!i 2 V1 , and fi are compactly supported). Let dv0; dv1 be volume forms on V0; V1
such that dv = dv0=dv1.
R R
−1
Definition 9.3. The integral U f(v)dv is U0(f(v); (dv1) )dv0.
64 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
It is clear that this quantity depends only on dv and not on dv0 and dv1 sepa-
rately.
R
Thus, f(v)dv is defined as the integral of the suitably normalized top coeÆcient

of f (expanded with respect to some homogeneous basis of V ). To write it in
1
coordinates, let 1; :::; m be a linear system of coordinates on V such that dv =
dx1:::dxn
(such coordinate systems will be called unimodular with respect to dv).
d1:::dRm R
Then f(v)dv equals ftop(x1; :::; xn)dx1:::dxn, where ftop is the coeÆcient of
1:::n in the expansion of f.
9.6. The Berezinian of a matrix. Now we generalize to the supercase the defini-
tion of determinant (since we need to generalize Jacobian, which is a determinant).
Let R be a supercommutative ring. Fixt two nonnegative integers m; n. Let A
be a n + m by n + m matrix over R. Split A in the blocks A11; A12; A21; A22 so that
A11 is n by n, and A22 is m by m. Assume that the matrices A11; A22 have even
elements, while A21 and A12 have odd elements. Assume also that A22 is invertible.
Definition 9.4. The Berezinian of A is the element
−1
det(A11 − A12A22 A21)
Ber(A) := 2 R
det(A22)
(where the determinant of the empty matrix is agreed to be 1; so for m = 0 one
−1
has BerA = det A, and for n = 0 one has BerA = (det A) ).
Remark. Recall for comparison that if A is purely even then
−1
det(A) := det(A11 − A12A22 A21) det(A22):
The Berezinian has the following simpler description. Any matrix A as above
admits a unique factorization A = A+A0A−, where A+, A0, A− are as above, and
in addition A+; A− are block upper (respectively, lower) triangular with 1 on the
diagonal, while A0 is block diagonal. Then Ber(A) = det((A0)11)= det((A0)22).
Proposition 9.5. If A; B be matrices as above, then Ber(AB) = Ber(A)Ber(B).
Proof. From the definition using triangular factorization, it is clear that it suÆces
to consider the case A = A−, B = B+. Let X = (A−)21, Y = (B+)12 (matrices
with odd elements). Then the required identity is
−1
det(1 − Y (1 + XY ) X) = det(1 + XY ):
To prove this relation, let us take the logarithm of both sides and expand using
Taylor's formula. Then the left hand side gives
X
k k−1
− Tr(Y (1 + XY ) (XY ) X)=k
k1
Using the cyclic property of the trace, we transform this to
X
k k
Tr((1 + XY ) (XY ) )=k
k1
(the minus disappears since X; Y have odd elements). Summing the series, we find
that the last expression equals
−1
−Tr ln(1 − (1 + XY ) XY ) = Tr ln(1 + XY );
as desired. 
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 65
The additive analog of Berezinian is supertrace. Namely, for A as above, sTrA =
TrA11 − TrA22. It is the correct superanalogue of the usual trace, as it satisfies
the equation sTr(AB) = sTr(BA) (while the usual trace does not). The connection
between the supertrace and the Berezinian is given by the formula
A sTr(A)
Ber(e ) = e :
Exercise. Prove this formula.

9.7. Berezin's change of variable formula. Let V be a vector space, f 2 V ,
cf
v 2 V . Denote by the result of contraction of f with v.
cv
0 0
Let U; U be superdomains, and F : U ! U be a morphism. As explained above,
0
given linear coordinates x1; :::; xn; 1; :::; m on U and y1; :::; yp; 1; :::; q on U , we
can describe f by expressing yi and i as functions of xj and j. Define the Berezin
matrix of F , A := DF (x; ) by the formulas:
cyi cyi ci ci
A11 = ( ); A12 = ( ); A21 = ( ); A22 = ( ):
cxj cj cxj cj
Clearly, this is a superanalog of the Jacobi matrix.
The main theorem of supercalculus is the following theorem.
0
Theorem 9.6. (Berezin) Let g be a smooth function with compact support on U ,
0 0 0
and F : U ! U be an isomorphism. Let dv; dv be supervolume elements on U; U .
Then Z Z
0 0
g(v )dv = g(F (v))jBerDF (v)jdv;
U0 U
where the Berezinian is computed with respect to unimodular coordinate systems.
Remark. If f() = a+terms containing j then by definition jf()j := f() is
a > 0 and −f() if a < 0.
Proof. The chain rule of the usual calculus extends verbatim to supercalculus. Also,
we have shown that Ber(AB) = Ber(A)BerB. Therefore, if we know the statement
of the theorem for two isomorphisms F1 : U2 ! U1 and F2 : U3 ! U2, then we
know it for the composition F1 Æ F2.
0 0 0 0
Let F (x1; :::; xn; 1; :::; m) = (x1; :::; xn; 1; :::; m). From what we just explained
it follows that it suÆces to consider the following cases.
0 0
1. xi depend only on xj, j = 1; :::; n, and i = i.
0 0
2. xi = xi + zi, where zi lie in the ideal generated by j, and i = i.
0
3. xi = xi.
Indeed, it is clear that any isomorphism F is a composition of isomorphisms of
the type 1; 2; 3.
In case 1, the statement of the theorem follows from the usual change of variable
formula. Thus it suÆces to consider cases 2 and 3.
In case 2, it is suÆcient to consider the case when only one coordinate is changed
0 0
by F , i.e. x1 = x1 + z, and xi = xi for i  2. In this case we have to show that the
integral of
cz
g(x1 + z; x2; :::; xn; )(1 + ) − g(x; )
cx1
is zero. But this follows easily upon expansion in powers of z, since all the terms
are manifestly total derivatives with respect to x1.
0
In case 3, we can also assume i = i, i  2, and a similar (actually, even simpler)
argument proves the result. 
66 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
9.8. Integration on supermanifolds. Now we will define densities on super-
manifolds. Let M be a supermanifold, and fUffg be an open cover of M together
0 0 njm
with isomorphisms fff : Uff ! Uff , where Uff is a superdomain in R . Let
−1
gfffi : ffi(Uff “ Ufi) ! fff(Uff “ Ufi) be the transition map fffffi . Then a density s
1
on M is a choice of an element sff 2 CM (Uff) for each ff, such that on Uff “ Ufi one
has sfi(z) = sff(z)jBer(gfffi)(ffi(z))j.
Remark. It is clear that a density on M is a global section of a certain sheaf
on M, called the sheaf of densities.
R
Now, for any (compactly supported) density ! on M, the integral ! is well
M
defined. Namely, it is defined as is usual calculus: one uses partition of unity 
ff
R P R
such that Supp
ff  (Uff)0 are compact subsets, and sets M ! := ff M 
ff!
(where the summands can be defined using fff). Berezin's theorem guarantees then
that the final answer will be independent on the choices made.
9.9. Gaussian integrals in an odd space. Now let us generalize to the odd case
the theory of Gaussian integrals, which was, in the even case, the basis for the path
integral approach to quantum mechanics and field theory.
Recall first the notion of PfaÆan. Let A be a skew-symmetric matrix of even
size. Then the determinant of A is the square of a polynomial in the entries of A.
This polynomial is determined by this condition up to sign. The sign is usually
fixed by requiring that the polynomial should be 1 for the direct sum of matrices
 
0 1
. With this convention, this polynomial is called the PfaÆan of A and
−1 0
T
denoted PfA. The PfaÆan obviously has the property Pf(X AX) = Pf(A) det(X)
for any matrix X.
Let now V be an 2m-dimensional vector space with a volume element dv, and B
a skew-symmetric bilinear form on V . We define the PfaÆan PfB of B to be the
PfaÆan of the matrix of B in any unimodular basis by the above transfoamtion
formula, it does not depend on the choice of the basis). It is easy to see (by reducing
B to canonical form) that
m
^ B
= Pf(B)dv:
m!
In terms of matrices, this translates into the following (well known) formula for the
PfaÆan of a skew symmetric matrix of size 2m:
X Y
Pf(A) = ” ai(i);
2m i2f1;:::;2mg;i<(i)
where m is the set of pairings of f1; :::; 2mg, and ” is the sign of the permutation
sending 1; :::; 2m to i1; (i1); :::; im; (im) (where ir < (ir) for all r). For example,
for m = 2 (i.e. a 4 by 4 matrix),
Pf(A) = a12a34 + a14a23 − a13a24:
Now consider an odd vector space V of dimension 2m with a volume element d.
Let B be a symmetric bilinear form on V (i.e. a skewsymmetric form on V ). Let
1; :::; 2m be unimodular linear coordinates on V (i.e. d = d1 ^ ::: ^ dm). Then
P
if  = (1; :::; n) then B(; ) = i;j bijij, where bij is a skewsymmetric matrix.
Proposition 9.7.
Z
1
e2 B(;)(d)−1 = Pf(B):
V
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 67
m
^ B
Proof. The integral equals , which is Pf(B). 
m!d

Example. Let V is a finite dimensional odd vector space, and Y = V  V .

The space Y has a canonical volume element dvdv , defined as follows: if e1; :::; em
     
be a basis of V and e1; :::; en is the dual basis of V then dvdv = e1 ^e1:::^en ^en.
 −1
Let dy = (dvdv ) be the corresponding supervolume element.
Let A : V ! V be a linear operator. Then we can define an even smooth
 
function S on the odd space Y as follows: S(v; v ) = (Av; v ). More explicitly, if
i be coordinates on V corresponding to the basis ei, and i the dual system of

coordinates on V , then
X
S(1; :::; m; 1; :::; m) = aijji;
where (aij) is the matrix of A in the basis ei.
Proposition 9.8.
Z
S
e dy = det A
Y
1
Proof. We have S(v; v) = 2B((v; v); (v; v)), where B is the skew form on Y ,
   
which is given by the formula B((v; v ); (w; w )) = (Av; w ) − (Aw; v ). It is easy
to see that Pf(B) = det(A), so Proposition 9.8 follows from Proposition 9.7.
Another proof can be obtained by direct evaluation of the top coeÆcient. 
9.10. The Wick formula in the odd case. Let V be a 2m-dimensional odd
2
space with a volume form d, and B 2 S V a nondegenerate form (symmetric
in the supersense and antisymmetric in the usual sense). Let 1; :::; n be linear
functions on V (regarded as the usual space). Then 1; :::; n can be regarded as
odd smooth functions on the superspace V .
Theorem 9.9.
Z
1
1():::n()e− 2 B(;)(d)−1 = Pf(−B)Pf(B−1(i; j)):
V
(By definition, this is zero if n is odd). In other words, we have:
Z
X Y
1
1():::n()e− 2 B(;)(d)−1 = Pf(−B) ” (B−1(i; (i))):
V
2m i2f1;:::;2mg;i<(i)
Proof. We prove the second formula. Choose a basis ei of V with respect to which
the form B is standard: B(ej; el) = 1 if j = 2i − 1; l = 2i, and B(ej; el) = 0
for other pairs j < l. Since both sides of the formula are polylinear with respect
 
to 1; :::; n, it suÆces to check it if 1 = ei1,..., n = ein. This is easily done
by direct computation (in the sum on the right hand side, only one term may be
nonzero). 
