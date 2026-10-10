---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-009-10-quantum-mechanics-for-fermions
section_title: "Quantum mechanics for fermions"
section_number: "10"
pages: 67-73
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
10. Quantum mechanics for fermions
10.1. Feynman calculus in the supercase. Wick's theorem allows us to extend
Feynman calculus to the supercase. Namely, let V = V0 V1 be a finite dimensional
real superspace with a supervolume element dv, equipped with a symmetric nonde-
P
1 Br(v;v;:::;v)
generate form B = B0  B1 (B0 > 0). Let S(v) = 2 B(v; v) + r3 r! be
an even function on V (the action). Note that Br, r  3 can contain mixed terms
68 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
involving both odd and even variables, e.g. x12 (the so called “Yukawa term”).
We will consider the integral
Z
−S(v)=~
I(~) = `1(v0):::`n(v0)1(v1):::p(v1)e dv:
V
(where v0; v1 are the even and odd components of v). Then this integral has an
expansion in ~ written in terms of Feynman diagrams. Since v has both odd and
even part, these diagrams will contain “odd” and “even” edges (which could be
depicted by straight and wiggly lines respectively). More precisely, let us write
r  
X
r
Br(v; v; :::; v) = Bs;r−s(v1; :::; v1; v0; :::; v0);
s
s=0
where Bs;r−s has homogeneity degree s with respect to v1 and r − s with respect to
v0 (i.e. it will be nonzero only for even s). Then to each term Bs;r−s we assign an
(s; r − s)-valent flower, i.e. a flower with s odd and r − s even outgoing edges, and
for the set of odd outgoing edges, it has been specified which orderings are even.
Then, given an arrangement of flowers, for every pairing  of outgoing edges, we
can define an amplitude F by contracting the tensors −Bs;r−s (and being careful
with the signs). It is easy to check that all pairings giving the same graph will
contribute to I(~) with the same sign, and this we have almost the same formula
as in the bosonic case:
I(~) = (2)dim V0=2~ dimV0−2dimV1 Ppf(−B1) X ~b(−) F−;
det B0 jAut(−)j
−
where the summation is taken over graphs with n even and p odd outgoing edges.
Remark. More precisely, we can define the sign ” of a pairing  as follows:
label outgoing edges by 1; :::, starting from the fisrt flower, then second, etc., so
that the labeling is even on each flower. Then write the labels in a sequence,
enumerating (in any order) the pairs defined by  (the element with the smaller of
the two labels goes first). The sign ” is by definition the sign of this ordering (as a
permutation of 1; :::). Then F− is F for any pairing  yielding − which is positive,
i.e. such that ” = 1. For negative pairing, F− = −F.
In most (but not all) situations considered in physics, the action is quadratic
in the fermionic variables, i.e. S(v) = Sb(v0) − Sf (v0)(v1; v1), where Sf (v0) is a
skew-symmetric bilinear form on V1. In this case, using fermionic Wick's theorem,
we can perform exact integration with respect to v1, and reduce I(~) to a purely
bosonic integral. For example, if we have only `i and no i, we have
Z
−Sb(v0)=~
I(~) = `1(v0):::`n(v0)e Pf(Sf (v0))dv0:
V0
In this situation, all vertices which have odd outgoing edges, will have only two of
them, and therefore in any Feynman diagram with even outgoing edges, odd lines
form nonintersecting simple curves, called fermionic loops (in fact, the last formula
is nothing but the result of regarding these lopps as a new kind of vertices – convince
yourself of this). In this case, there is the following simple way of assigning signs to
Feynman diagrams. For each vertex with two odd outgoing edges, we orient the first
edge inward and the second one outward. We allow only connections (pairings) that
preserve orientations (so the fermionic loops become oriented). Then the sign is
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 69
r
(−1) , where r is the number of fermionic loops (i.e. each fermionic loop contributes
a minus sign).
10.2. Fermionic quantum mechanics. Let us now pass from finite dimensional
fermionic integrals to quantum mechanics, i.e. integrals over fermionic functions of
one (even) real variable t.
Let us first discuss fermionic classical mechanics, in the Lagrangian setting. Its
difference with the bosonic case is that the “trajectory” of the particle is described
by an odd, rather than even, function of one varible, i.e. c : R ! V , where V is a
vector space. Mathematically this means that the space of fields (=trajectories) is
1
an odd vector space C (R; V ). A Lagrangian L(c) is a local expression in such
R
_
a field (i.e. a polynomial in c; c; :::), and an action is the integral S = Ldt. This
R
1 
means that the action is an element of the space C0 (R; V ) .
Consider for example the theory of a single scalar-valued free fermion c(t). By
1 _
definition, the Lagrangian for such a theory is L = cc, i.e. the action is S =
R 2
1 _
ccdt.
2
2
This Lagrangian is the odd analog of the Lagrangian of a free particle, q_ =2.
_ d 2 _ _
Remark. Note that cc 6= (c =2) = 0, since cc = −cc, so this Lagrangian
dt
is “reasonable”. On the other hand, the same Lagrangian would be unreasonable
in the bosonic case, as it would be a total derivative, and hence the action would
be zero. Finally, note that it would be equally unreasonable to use in the fermionic
1 2 2 2
case the usual bosonic Lagrangian (q_ − m q ); it would identically vanish if q
2
were odd-valued.
The Lagrangian L is invariant under the group of reparametrizations Diff+(R),
_
and the Euler-Lagrange equation for this Lagrangian is c = 0 (i.e. no dynamics).
Theories with such properties are called topological field theories.
Let us now turn to quantum theory in the Lagrangian setting, i.e. the theory
R
iS(c)
given by the Feynman integral c(t1):::c(tn)e Dc. In the bosonic case, we
1
“integrated” such expressions over the space C0 (R). This integration did not make
immediate sense because of failure of measure theory in infinite dimensions. So we
had to make sense of this integration in terms of ~-expansion, using Wick's formula
and Feynman diagrams. In the fermionic case, the situation is analogous. Namely,
1
now we must integrate functions over C (R), which are elements of D(R), where
0
D(R) is the space of distributions on R. Although in the fermionic case we don't
need measure theory (as integration is completely algebraic), we still have trouble
defining the integral: recall that by definition the integral should the top coeÆcient
of the integrand as the element of D(R), which makes no sense since in the exterior
algebra of an infinite dimensional space there is no top component. Thus we have
to use the same strategy as in the bosonic case, i.e. Feynman diagrams.
Let us, for instance, define the quantum theory for a free scalar valued fermion,
1 _
i.e one described by the Lagrangian L = cc. According to the yoga we used in
2
the bosonic case, the two point function of this theory < c(t1)c(t2) > should be the
dG
function G(t1 −t2), where G is the solution of the differential equation −i dt = Æ(t).
1
The general solution of this equation has the form G(t) = − sign(t) + C. Be-
2i
cause of the fermionic nature of the field c(t), it is natural to impose the requirement
that G(−t) = −G(t), i.e that the correlation functions are antisymmetric; this sin-
1
gles out the solution G(t) = − sign(t) (we also see from this condition that we
2i
should set G(0) = 0). As usual, the 2n-point correlation functions are defined by
70 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
the Wick formula. That is, for distinct ti,
n
< c(t1):::c(t2n) >= (2n − 1)!!(i=2) sign();
where  is the permutation that orders ti in the decreasing order. If at least two
points coincide, the correlation function is zero.
Thus we see that the correlation functions are invariant under Diff+(R). In other
words, using physical terminology, we have a topological quantum field theory.
Note that the correlation functions in the Euclidian setting for this model are
the same as in the Minkowski setting, since they are (piecewise) constant in ti. In
particular, they don't decay at infinity, and hence our theory does not have the
clustering property.
We have considered the theory of a massless fermionic field. Consider now the
massive case. This means, we want to add to the Lagrangian a quadratic term in
c which does not contain derivatives. If we have only one field c, the only choice
2
for such term is c , which is zero. So in the massive case we must have at least
two fields. Let us therefore consider the theory of two fermionic fields c1; c2 with
Lagrangian
1
_ _
L = (c1c1 + c2c2 − mc1c2);
2
where m > 0 is a mass parameter. The Green's function for this model satisfies the
differential equation
0
G − MG = iÆ;
 
0 m
where M = (and G is a 2 by 2 matrix valued function). The general
−m 0
T
solution of this equation that satisfies the antisymmetry condition G (−t) = −G(t)
(which we will impose as in the massless case) has the form
1
Mt
G(t) = −( sign(t)I + aM)e ;
2i
where I is the identity matrix, and a is a number. Furthermore, it is natural to
require that the theory at hand satisfies the clustering property (after being Wick-
rotated). This means, G(−it) decays at infinity for real t. It is easy to compute
that this condition is satisfied for only one value of a, namely a = 1=2m. For this
−iMt
value of a, the solution has the form G(t) = iPe for t > 0, where P is
the projector to the eigenspace of M with eigenvalue im (and G(0) = 0).
Remark. It is easy to generalize this analysis to the case when c takes values
in a positive definite inner product space V , and M : V ! V is a skewsymmetric
operator, since such a situation is a direct sum of the situations considered above.
In the case when M is nondegenerate, one can define the corresponding theory
with interactions, i.e. with higher than quadratic terms in c. Namely, one defines
the correlators as sums of amplitudes of appropriate Feynman diagrams. We leave
it to the reader to work out this definition, by analogy with the finite dimensional
case which we have discussed above.
10.3. Super Hilbert spaces. The space of states of a quantum system is a Hilbert
space. As we plan to do Hamiltonian quantum mechanics for fermions, we must
define a superanalog of this notion.
Recall that a sesquilinear form on a complex vector space is a form (; ) which
is additive in each variable, and satisfies the conditions (ax; y) = a(x; y), (x; ay) =
a(x; y) for a 2 C .
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 71
Now suppose H = H0  H1 is a Z=2-graded complex vector space.
Definition 10.1. (i) A Hermitian form on H is an even sesquilinear form (; ), such
that (x; y) = (y; x) for even x; y, and (x; y) = −(y; x) for odd x; y.
(ii) A Hermitian form is positive definite if (x; x) > 0 for even x 6= 0, and
−i(x; x) > 0 for odd x 6= 0. A super Hilbert space is a superspace with a positive
definite Hermitian form (; ), which is complete in the corresponding norm.
(iii) Let H be a super Hilbert space, and T : H0  H1 ! H0  H1 be a
linear operator between the underlying purely even spaces. The Hermitian adjoint
 p(x)p(T) 
operator T is defined by the equation (x; T y) = (−1) (T x; y), where p
denotes the parity.
10.4. The Hamiltonian setting for fermionic quantum mechanics. Let us
now discuss what should be the Hamiltonian picture for the theory of a free fermion.
More precisely, let V be a positive definite finite dimensional real inner product
1 _
space, and consider the Lagrangian L = ((c; c) − (c; Mc)), where c : R ! V ,
2
and M : V ! V is a skew-symmetric operator.
To understand what the Hamiltonian picture should be, let us compare with
1 2 2 2
the bosonic case. Namely, consider the Lagrangian Lb = 2(q_ − m q ), where
 
q : R ! V . In this case, the classical space of states is Y := T V = V  V .
2
The equations of motion are Newton's equations q¨ = −m q, which can be reduced
2
to Hamilton's equations q_ = p, p_ = −m q. The algebra of classical observables is
1 
C (Y ), with Poisson bracket defined by fa; bg = (a; b), a; b 2 Y , where (; ) is the

form on Y inverse to the natural symplectic form on Y . The hamiltonian H is
determined (up to adding a constant) by the condition that the equations of motion
_ 2 2 2
are f = ff; Hg; in this case it is H = (p + m q )=2.
The situation in the fermionic case is analogous, with some important differences
which we will explain below. Namely, it is easy to compute that the equation of
_
motion (i.e. the Euler-Lagrange equation) is c = Mc. The main difference with
the bosonic case is that this equation is of first and not of second order, so the space
of classical states is just V (no momentum or velocity variables are introduced).
1 
Hence the algebra of classical observables is C (V ) = V . To define a Poisson
bracket on this algebra, recall that V has a natural “symplectic structure”, defined

by the symmetric form (; ) on V . Thus we can define a Poisson bracket on V by
the same formula as above: fa; bg = (a; b). More precisely, f; g is a unique skew

symmetric (in the supersense) bilinear operation on V which restricts to (a; b)

for a; b 2 V , and is a derivation with respect to each variable:
p(a)p(b)
fa; bcg = fa; bgc + (−1) bfa; cg;
where p(a) denotes the parity of a.
Now it is easy to see what should play the role of the Hamiltonian. More pre-
cisely, the definition with Legendre transform is not valid in our situation, since the
Legendre transform was done with respect to the velocity variables, which we don't
have in the fermionic case. On the other hand, as we discussed in x8, in the bosonic
_
case the equation of motion f = ff; Hg determines H uniquely, up to a constant.
The situation is the same in the fermionic case. Namely, by looking at the equation
_ 1
of motion c = Mc, it is easy to see that the Hamiltonian equals H = (c; Mc).
2
In particular, if M = 0 (massless case), the Hamiltonian is zero (a characteristic
property of topological field theories).
72 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
Now let us turn to quantum theory. In the bosonic case the algebra of quantum
1
observables is a noncommutative deformation of the algebra C (Y ) in which the
relation fa; bg = (a; b) is replaced with its quantum analog ab − ba = i(a; b) (up to
the Planck constant factor which we will now ignore). In particular, the subalgebra

of polynomial observables is the Weyl algebra W (Y ), generated by Y with this
defining relation. By analogy with this, we must define the algebra of quantum

observables in the fermionic case to be generated by V with the relation ab + ba =

i(a; b) (it deforms the relation ab + ba = 0 which defines V ). So we recall the
following definition.
Definition 10.2. Let V be a vector space over a field k with a symmetric bilinear
form Q. The Clifford algebra Cl(V; Q) is generated by V with defining relations
ab + ba = Q(a; b), a; b 2 V .

We see that the algebra of quantum observables should be Cl(V ; i(; )). Note
C
that like in the classical case, this algebra is naturally Z=2 graded, so that we have
even and odd quantum observables.
Now let us see what should be the Hilbert space of quantum states. In the bosonic
2
case it was L (V ), which is, by the well known Stone-von Neumann theorem, the
unique irreducible unitary representation of W (Y ). By analogy with this, in the
fermionic case the Hilbert space of states should be an irreducible even unitary
representation of Cl(V ) on a supervector space H.

The structure of the Clifford algebra Cl(V ) is well known. Namely, consider
separately the cases when dim V is odd and even.

In the even case, dim V = 2d, Cl(V ) is simple, and has a unique irreducible
d
representation H, of dimension 2 . It is constructed as follows: choose a decompo-
 
sition VC = L  L , where L; L are Lagrangian subspaces. Then H = L, where
 
L  V acts by multiplication and L by differentiation (multiplied by −i). The
C
structure of the superspace on H is the standard one on the exterior algebra.

In the odd case, dim V = 2d+1, choose a decomposition VC = LL K, where

L; L are maximal isotropic, and K is a nondegenerate 1-dimensional subspace

orthogonal to L and L . Let H = (L  K), where L; K act by multiplication and
 
L by (−i times) differentiation. This is a representation of Cl(V ) with a Z=2
grading. This representation is not irreducible, and decomposes in a direct sum of
two non-isomorphic irreducible representations H+  H− (this is related to the fact
that the Clifford algebra for odd dim V is not simple but is a sum of two simple
algebras). However, this decomposition is not consistent with the Z=2-grading, and
therefore as superrepresentation, H is irreducible.
Now, it is easy to show that both in the odd and in the even case the space H
 
carries a unique up to scaling Hermitian form, such that V  V acts by selfadjoint
C
operators. This form is positive definite. So the situation is similar to the bosonic
case for any dim V .
Let us now see which operator on H should play the role of the Hamiltonian of
the system. The most natural choice is to define the quantum Hamiltonian to be the
1
obvious quantization of the classical Hamiltonian H = 2(c; Mc). Namely, if ”i is a
P
 ^ 1
basis of V and aij is the matrix of M in this basis, then one sets H = 2 i;j aij”i”j.
To compute this operator more explicitly, we will assume (without loss of generality)
that the decomposition of VC that we chose is stable under M. Let j be an
eigenbasis of M in L (with eigenvalues imj), and cj be differentiations along the
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 73
vectors of this basis. Then
X X
^
H = mj(jcj − cjj) = mj(2jcj − 1):
j j
This shows that if dim V is even then the partition function on the circle of
length L for our theory is
Y
−LH^ mjL −mjL
Z = sTr(e ) = (e − e )
j
If the dimension of V is odd then the partition function is zero.
Now we would like to consider the fermionic analog of the Feynman-Kac formula.
For simplicity consider the fully massive case, when dim V is even and mj 6= 0 (i.e.
M is nondegenerate). In this case, we have a unique up to scaling lowest eigenvector
^
of H, namely 
 = 1.

Let c(0) 2 V 
 End(H) be the element corresponding to the action map V !
itH^ −itH^
End(H), and c(t) = e c(0)e . Also, let < c(t1):::c(tn) >, t1  :::  tn, be
the correlation function for the free theory in the Lagrangian setting, taking values

n
in V , so in this expression c(ti) is a formal symbol and not an operator.
Theorem 10.3. (i) For the free theory on the line we have
< c(t1):::c(tn) >= (
; c(t1):::c(tn)
):
(ii) For the free theory on the circle of length L we have
−LH^
sTr(c(t1):::c(tn)e )
< c(t1):::c(tn) >= −LH^
sTr(e )
Exercise. Prove this theorem. (The proof is analogous to Theorem 8.3 in the
free case).
It should now be straightforward for the reader to formulate and prove the
Feynman-Kac formula for an interacting theory which includes both bosonic and
Fermionic massive fields. We leave this as an instructive exercise.
