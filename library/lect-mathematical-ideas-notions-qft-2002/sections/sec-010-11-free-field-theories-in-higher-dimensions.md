---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-010-11-free-field-theories-in-higher-dimensions
section_title: "Free field theories in higher dimensions"
section_number: "11"
pages: 73-78
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
11. Free field theories in higher dimensions
11.1. Minkowski and Euclidean space. Now we pass from quantum mechanics
to quantum field theory in dimensions d  1. As we explained above, we have two
main settings.
1. Minkowski space. Fields are functions on a spacetime VM , which is a real
inner product space of signature (1; d−1). This is where physical processes actually
“take place”. The symmetry group of V , G = SO(1; d − 1), is called the Lorenz
group; it is the group of transformation of spacetime in special relativity. Therefore,
field theories in Minkowski space which are in an approariate sense “compatible”
with the action of G are called relativistic.
Recall some standard facts and definitions. The light cone in V is the cone
2 2
described by the equation jvj = 0, where jvj := (v; v). Vectors belonging to the
light cone are called lightlike. The light cone divides the space V into spacelike
2 2
vectors jvj < 0 (the outside of the cone), and timelike vectors jvj > 0 (inside
the cone). We will choose one of the two components of the interior of the cone
and call it positive; it will be denoted by V+. The opposite (negative) component
is denoted by V−. The group of g 2 SO(V ) = SO(1; d − 1) which preserve V+
74 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
is denoted by SO+(1; d − 1); it is the connected component of the identity of the
group SO(1; d − 1) (which has two connected components).
Often (e.g. when doing Hamiltonian field theory) it is necessary to split V in an
orthogonal direct sum V = Vs  R of space and time. In this decomposition, the
space Vs is required to be spacelike (i.e. negative definite), which implies that the
time axis R has to be timelike (positive definite). Note that such a splitting is not
unique, and that fixing it breaks the Lorenz symmetry SO+(1; d − 1) down to the
usual rotation group SO(d − 1). To do explicit calculations, one further chooses
Cartesian coordinates x1; :::; xd−1 on Vs and t on the time axis R.
2. Euclidean space. Fields are functions on a spacetime VE, which is a positive
definite inner product space. It plays an auxiliary role and has no direct physical
meaning, although path integrals computed in this space are similar to expectation
values in statistical mechanics.
The two settings are related by the “Wick rotation”. Namely the Euclidean
space VE corresponding to the Minkowski space VM is the real subspace in (VM )C
consisting of vectors (it; x1; :::; xd−1, where t and xj are real. In other words, to
pass to the Euclidean space one needs to make a change of variable t ! it. Note
P
2 2
that under this change, the standard metric on the Minkowski space, dt − dx ,
P i
2 2
goes into a negative definite metric −dt − dx . However, the minus sign is
i P
2 2
traditionally dropped and one considers instead the positive metric dt + dx on
i
VE.
11.2. Free scalar bosons. Consider the theory of a free scalar bosonic field 
 of
mass m. The procedure of quantization of this theory in the Lagrangian setting
is a straightforward generalization from the case of quantum mechanics. Namely,
1 2 2 2
the Lagrangian for this theory in Minkowski space is L = ((d
) − m 
 ), and
2
2
the Euler-Lagrange equation is 
 = −m 
, where  is the D'Alambertian,  =
2 P 2
c c
ct2 − i cx2i . Thus to define the corresponding quantum theory, we should invert
2
the operator  + m . As in the quantum mechanics case, this operator is not
invertible (0 is in the spectrum), so we should proceed using the Wick rotation.
After the Wick rotation (i.e. transformation t ! it), we arrive at the following
1 2 2 2
Euclidean Lagrangian: LE = 2 ((d
) + m 
 ), and the Euler-Lagrange equation is
2

 = m 
. So to define the quantum theory, i.e. the path integral
Z
−S(
)

(x1):::
(xn)e D

R
2
(where S = L), we now need to invert the operator A = − + m . The operator
−1
A is an integral operator, whose kernel is G(x − y), where G(x) is the Green's
function, i.e. the fundamental solution of the differential equation
2
−G + m G = Æ
To solve this equation, note that the solution is rotationally invariant. Therefore,
outside of the origin, G(x) = g(jxj), where g is a function on (0; 1) such that
d − 1
00 0 2
−g − g + m g = 0
r
(where the left hand side is the radial part of the operator A). This is a version of
2−d
the Bessel equation. If m > 0, the basis of solutions is r 2 J 2−d (imr). (Actually,
 2
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 75
these functions are elementary for odd d). There exists a unique up to scaling
solution, which decays at infinity, namely,
2−d
g = Cr 2 (J2−d (imr) + idJ 2−d (imr)); (d 6= 2):
2 − 2
For d = 2, this expression is zero, and one should instead take the limit of the right
hand side divided by d − 2 as d ! 2 (which will generate a logarithmic factor ln r).
The normalizing constant C can be found from the condition that AG = Æ.
Remark. It is easy to check that for d = 1 this function equals the familiar
−mr
Green's function for quantum mechanics, e =2m.
If m = 0 (massless case), the basis of solutions is: 1; r for d = 1, 1; ln r for d = 2,
2−d
and 1; r for d > 2. Thus, if d ≤ 2, we don't have a decaying solution and thus
the corresponding quantum theory will be deficient: it will not satisfy the clustering
property. On the other hand, for d > 2 we have a unique up to scaling decaying
1−d
solution g = Cr . The constant C is found as in the massive case.
The higher correlation founctions are found from the 2-point function via the
Wick formula, as usual.
We should now note a fundamental difference between quantum mechanics and
quantum field theory in d > 1 dimensions. This difference comes from the fact that
while for d = 1, the Green's function G(x) is continuous at x = 0, for d > 1 it is
2−d
singular at x = 0. Namely, G(x) behaves like Cjxj as x ! 0 for d > 2, and as
C ln jxj as d = 2. Thus for d > 1, unlike the case d = 1, the path integral
Z
−S(
)

(x1):::
(xn)e D

(as defined above) makes sense only if xi 6= xj. In other words, this path integral
should be regarded not as a function but rather as a distribution. Luckily, there is
1
a canonical way to do it, since the Green's function G(x) is locally L .
Now we can Wick rotate this theory back into the Minkowski space. It is clear
p
2
that the Green's function will then turn into GM (x) = g( jxj + i”), The higher
correlation functions, as before, are determined from this by the Wick formula.
Actually, it is more convenient to describe this theory “in momentum space”,
where the Green's function can be written more explicitly. Namely, the Fourier
^
transform G(p) of the distribution G(x) is a solution of the equation
2 ^ 2 ^
p G + m G = 1;
obtained by Fourier transforming the differential equation for G. Thus,
1
^
G(p) = ;
2 2
p + m
as in the quantum mechanics case. Therefore, like in quantum mechanics, the Wick
rotation produces the distribution
i
^
GM (p) = ;
2 2
p − m + i”
which is the Fourier transform of GM (x).
11.3. Spinors. To consider field theory for fermions, we must generalize to the
1 dc
case of d > 1 the basic fermionic Lagrangian c . To do this, we must replace
2 dt
d
by some differential operator on V . This operator should be of first order, since
dt
in fermionic quantum mechanics it was important that the equations of motion are
76 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
first order equations. Clearly, it is impossible to define such an operator so that
the Lagrangian is SO+(V )-invariant, if c is a scalar valued (odd) function on V .
Thus, a fermionic field in field theory of dimension d > 1 cannot be scalar valued,
but rather must take values in a real representation S of SO+(V ), such that there
2 
exists a nonzero intertwining operator V ! Sym S . This property is satisfied by
spinor representations. They are indeed basic in fermionic field theory, and we will
now briefly discuss them (for more detail see “Spinors” by P.Deligne, in “QFT and
string theory: a course for mathematicians”).
First consider the complex case. Let V be a complex inner product space of
dimension d > 1. Let Cl(V ) be the Clifford algebra of V , defined by the relation
 +  = 2(; ), ;  2 V . As we discussed, for even d it is simple and has a
d=2
unique irreducible representation S of dimension 2 , while for odd d it has two
0 00 (d−1)=2
such representations S ; S of dimension 2 . It is easy to show that the space
CL2(V ) of quadratic elements of CL(V ) (i.e. the subspace spanned elements of the
form  − ; ;  2 V ) is closed under bracket, and coonstitutes the Lie algebra
0 00
o(V ). Thus o(V ) acts on S (respectively, S ; S ). This action does not integrate to
an action of SO(V ), but integrates to an action of its double cover Spin(V ).
If d is even, the representation S of Spin(V ) is not irreducible. Namely, recall that
S is the exterior algebra of a Lagrangian subspace of V . Thus is splits in a direct sum
S = S+S− (odd and even elements). The subspaces S+; S− are subrepresentations
of S, which are irreducible. They are called half-spin representations.
0 00
If d is odd, the representations S and S of Spin(V ) are irreducible and iso-
morphic. Any of them will be denoted by S and called the spinor representation.
Thus, we have the spinor representation S for both odd and even d, but for even d
it is reducible.
An important structure attached to the spinor representation S is the inter-
twining operator − : V ! EndS, given by the action of V  Cl(V ) in S. This
intertwiner allows us to define the Dirac operator
X
c
D = −i
cxi
where xi are coordinates on V associated to an orthornormal basis ei, and −i =
2
−(ei). This operator acts on functions form V to S, and D = , so D is a square
root of the Laplacian. The matrices −i are called − matrices.
Note that for even d, one has −(v) : S ! S, so D acts from functions with
values in S to functions with values in S.
By a spinor representation of Spin(V ) we will mean any linear combination
of S+; S− for even d, and any multiple of S for odd d. Thus, for every spinor
0 0 0
representation we have −(v) : Y ! Y , where S+ := S− and S− := S+, and
0
S := S.
Now assume that V is a real inner product space with Minkowski metric. In this
case we can define the group Spin+(V ) to be the preimage of SO+(V ) under the
map Spin(VC ) ! SO(VC ). It a double cover of SO+(V ) (if d = 2, this double cover
is disconnenced and actually a direct product by Z=2).
By a real spinor representation of SO+(V ) we will mean a real representation Y
such that YC is a spinor representation of Spin(VC ).
11.4. Fermionic Lagrangians. Now let us consider Lagrangians for a spinor field
c with values in a spinor representation Y . As the Lagrangian is supposed to be real
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 77
in the Minkowski setting, we will require in that case that Y is real. First of all, let
us see what we need in order to write the “kinetic term” (c; Dc). Clearly, to define
such a term (so that it is nonzero), we need an invariant nondegenerate pairing (; )
0
between Y and Y such that the for any v 2 V , the bilinear form (x; −(v)y) on Y
is symmetric.
Let us find for which Y this is possible (for complex V ). The behavior of Spin
groups depends on d modulo 8. Thus we will list the answers labeling them by d
mod 8 (they are easily extracted from the tables given in Deligne's text).
0. n(S+  S−).
1. nS.
2. nS+  kS−.
3. nS.
4. n(S+  S−).
5. 2nS.
6. 2nS+  2kS−.
7. 2S.
Let us now find when we can also add a mass term. Recall that the mass term
has the form (c; Mc), so it corresponds to an invariant skew-symmetric operator

M : Y ! Y . Let us list those Y from the above list, for which such nondegenerate
operator exists.
0. 2n(S+  S−).
1. 2nS.
2. n(S+  S−).
3. nS.
4. n(S+  S−).
5. 2nS.
6. 2n(S+  S−).
7. 2S.
To pass to the real Minkowski space (in both massless and massive case), one
should put the additional requirement that Y should be a real representation.
We note that upon Wick rotation to Minkowski space, it may turn out that a
real spinor representation Y will turn into a complex representation which has no
real structure. Namely, this happens for massless spinors that take values in S if
d = 2 mod 8. These representations have a real structure for Minkowskian V (i.e.
for SO+(1; d − 1)), but no real structure for Euclidean V (i.e. for SO(d)). This is
quite obvious, for example, when d = 2 (check!).
One may think that this causes a problem in quantum field theory, where we
would be puzzled what to integrate over – real or complex space. However, the
problem in fact does not arise, since we have to integrate over fermions, and inte-
gration over fermions (say, in the finite dimensional case) is purely algebraic and
does not make a distinction between real and complex.
11.5. Free fermions. Let us now consider a free theory for a spinor c : V ! Y ,
1
where Y is a spinor representation, defined by a Lagrangian L = ((c; Dc) −
2
(c; Mc)), where M is allowed to be degenerate (we assume that Y is such that this
expression makes sense). The equation of motion in Minkowski space is Dc = Mc.
0  0
where we have identified Y and Y using the pairing Y  Y ! R used to define
the kinetic term. Thus, to define the corresponding quantum theory, we need to
78 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
invert the operator D − M. As usual, this cannot be done because of a singularity,
and we have to consider the Wick rotation.
1
The Wick rotation produces the Euclidean Lagrangian L = 2((c; DEc)+(c; Mc))
(note that the i in the kinetic term is hidden in the definition of the Euclidean Dirac
operator). We invert DE + M, to obtain the Euclidean Green's function. To do
this, it is convenient to go to momentum space, i.e. perform a Fourier transform.
P
Namely, after Fourier transform DE turns into the operator ip, where p = pj−j,
and pj are the operators of multiplication by the coordinates pj. Thus, the Green's
0
function (i.e. the 2-point function) G(x) 2 Hom(Y ; Y ) is the Fourier transform
1 y 0
of the matrix-valued function . Let M : Y ! Y be the operator such that
ip+M
y y 2 y
−iM = M −i. Then, (−ip + M )(ip + M) = p + M M, so that
^ 2 y −1 y
G(p) = (p + M M) (−ip + M ):
This shows that G(x) is expressed through the Green's function in the bosonic case
by differentiations (how?). After Wick rotation back to the Minkowski space, we
get
^ 2 y −1 y
GM (p) = (p − M M + i”) (p + iM ):
Finally, the higher correlation functions, as usual, are found from the Wick formula.
