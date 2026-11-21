---
doc_id: fulltext
doc_title: "The Dilogarithm Function"
section_id: sec-008-1-variants-of-the-dilogarithm-function
section_title: "Variants of the dilogarithm function"
section_number: 1
pages: 20-31
source_pdf: fulltext.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
As explained in Chapter I, one of the disadvantages of the classical dilogarithm
function Li2(z) is that, although it has a holomorphic extension beyond the
region of convergence |z| < 1 of the deﬁning power series 
∞
n=1 zn/n2, this
extension is many-valued. This complicates all aspects of the analysis of the
dilogarithm function. One way to circumvent the diﬃculty, discussed in detail
in §§3–4 of Chapter I, is to introduce the Bloch-Wigner dilogarithm function
D(z) = ℑ

Li2(z) −log |z| Li1(z)

, which extends from the original region of
deﬁnition 0 < |z| < 1 to a continuous function D : P1(C) →R which is (real-)
analytic on P1(C)∖{0, 1, ∞} ; this function has an appealing interpretation as
the volume of an ideal hyperbolic tetrahedron and satisﬁes “clean” functional
equations which do not involve products of ordinary logarithms.
It turns out, however, that there are other natural dilogarithm functions
besides Li2 and D which have interesting properties. In this section we shall
discuss six of these: the Rogers dilogarithm L, which is similar to D but is
deﬁned on P1(R) (where D vanishes); the “enhanced” dilogarithm D, which
takes values in C/π2Q and is in some sense a combination of the Rogers
and Bloch-Wigner dilogarithms, but is only deﬁned on the Bloch group of
The Dilogarithm Function
23
C rather than for individual complex arguments; the double logarithm Li1,1,
the simplest of the multiple polylogarithms, which has two arguments but
can be expressed in terms of ordinary dilogarithms; the quantum dilogarithm
of Faddeev and Kashaev, which will play a role in the discussion of Nahm’s
conjecture in §3; and, very brieﬂy, the p-adic and the modulo p analogues of
the dilogarithm.
A. The Rogers dilogarithm. This function is deﬁned in the interval (0, 1)
by
L(x) = Li2(x) + 1
2 log(x) log(1 −x)
if 0 < x < 1
and then extended to the rest of R by setting L(0) = 0, L(1) = π2/6, and
L(x) =

2 L(1) −L(1/x)
if x > 1,
−L(x/(x −1))
if x < 0.
The resulting function is then a monotone increasing continuous real-valued
function on R and is (real-)analytic except at 0 and 1, where its derivative
becomes inﬁnite. At inﬁnity it is not continuous, since one has
lim
x →+∞L(x) = 2L(1) = π2
3 ,
lim
x →−∞L(x) = −L(1) = −π2
6 ,
but it is continuous if we consider it modulo π2/2. Moreover, the new function
L(x) := L(x) (mod π2/2) from P1(R) to R/ π2
2 Z, just like its complex ana-
logue D(z), satisﬁes “clean” functional equations with no logarithm terms, in
particular the reﬂection properties
L(x) + L(1 −x) = L(1),
L(x) + L(1/x) = −L(1)
and the 5-term functional equation
L(x) + L(y) + L
 1 −x
1 −xy

+ L(1 −xy) + L
 1 −y
1 −xy

= 0.
If we replace L by L in the left-hand sides of these three equations, then
their right-hand sides must be replaced by piecewise continuous functions
whose values depend on the positions of the arguments: L(1) in the ﬁrst
equation, 2L(1) for x > 0 or −L(1) for x < 0 in the second, and −3L(1) for
x, y < 0, xy > 1 and +3L(1) otherwise in the third. The proofs of these and
all other functional equations result from the elementary formula
L′(x) = −1
2x log(1 −x) −
1
2(1 −x) log(x) .
The special values of the dilogarithm function listed in §1 of Chapter I
become simpler when expressed in terms of the Rogers dilogarithm (e.g. one
24
Don Zagier
has simply L(1/2) = π2/12, L((3 −
√
5)/2) = π2/15 instead of the previous
expressions involving log2(2) and log2((1 +
√
5)/2)) and the same holds also
for more complicated identities involving several values of the dilogarithm
at algebraic arguments. Such identities, of which several will be discussed
in §2, reﬂect the fact that the corresponding linear combination of arguments
represents a torsion element in the Bloch group of Q. They play a role in
quantum ﬁeld theory, where the constants appearing on the right-hand sides
of the identities, renormalized by dividing by L(1), occur as central charges
of certain rational conformal ﬁeld theories.
B. The enhanced dilogarithm. The Bloch-Wigner dilogarithm is the imag-
inary part of Li2(z) (corrected by a multiple of log |z| Li1(z) to make its ana-
lytic properties better) and hence vanishes on P1(R), while the Rogers dilog-
arithm is the restriction of Li2(z) (corrected by a multiple of log |z| Li1(z) to
make its analytic properties better) to P1(R) and takes its values most nat-
urally in the circle group R/(π2/2)Z. It is reasonable to ask whether there
is then a function D(z) with values in C/(π2/2)Z or at least C/π2Q whose
imaginary part is D(z) and whose restriction to P1(R) is L(z). In fact such a
function does not exist if we demand that the argument belongs to P1(C), but
it does exist if we either pass to a suitable inﬁnite covering of P1(C)∖{0, 1, ∞}
or else consider only combinations 
 nj D(zj) where 
 nj[zj] belongs to the
Bloch group BC deﬁned in §4 of Chapter I. This extended function, which
following [47] we call the “enhanced dilogarithm,” plays an important role in
W. Nahm’s article in this volume and is discussed in some detail there, so we
will be relatively brief here.
We begin with the extension of Li2 and D to covers of punctured projective
space. Let X = P1(C) ∖{0, 1, ∞}. Its fundamental group is the free group
on two generators and its universal cover 
X is isomorphic to the complex
upper half-plane H (with covering map given by the classical Legendre mod-
ular function λ : H/Γ(2) →X), and naturally Li2 becomes a single-valued
holomorphic function on this universal cover, but we do not have to go this
far if we only want the values of Li2(z) modulo π2Q. Instead, it suﬃces to
take the universal abelian cover 
X : the abelianization of π1(X) is Z⊕Z, with
generators corresponding to the monodromy around 0 and 1 and hence to the
multi-valuedness of log(z) and log(1 −z), so 
X is given by choosing branches
of these two logarithms, i.e.,

X =

(u, v) ∈C2 | eu + ev = 1

,
with covering map π : 
X →X given by (u, v) →z = eu = 1 −ev. It is on
this space that we will deﬁne D.
Actually, to get a C/4π2Z-valued version of Li2, we do not even need to
pass to 
X, but only to the smaller abelian cover corresponding to choosing a
branch of log(1 −z) only, i.e., the cover X′ = C −2πiZ, with covering map
The Dilogarithm Function
25
X′ →X given by v →1 −ev. Indeed, from the formula Li′
2(z) = 1
z log
1
1−z we
see that the function
F(v) = Li2(1 −ev)
(v ∈X′)
has derivative given by F ′(v) =
−v
1 −e−v , which is a one-valued meromorphic
function on C with simple poles at v ∈2πiZ whose residues all belong to
2πiZ. It follows that F itself is a single-valued function on X′ with values in
C/(2πi)2Z. This function satisﬁes F(v + 2πis) = F(v) −2πis log(1 −ev). We
now deﬁne D on 
X by
D(ˆz) = F(v) + uv
2
for ˆz = (u, v) ∈
X .
This is a holomorphic function from 
X to C/(2πi)2Z whose behavior under
the covering transformations of 
X →X is given by
D((u + 2πir, v + 2πis)) = D((u, v)) + πi(rv −su) + 2π2rs
(r, s ∈Z)
and whose relation to the Bloch-Wigner function D(z) is given by
ℑ( D(ˆz)) = D(z) + 1
2 ℑ(¯uv)
(ˆz = (u, v),
π(ˆz) = z).
(1)
(For more details, see [47], pp. 578–579, where the deﬁnition of D is given
somewhat diﬀerently.)
Now let ξ = 
 nj[zj] be an element of the Bloch group BC. This means,
ﬁrst of all, that the numbers zj ∈X and nj ∈Z satisfy 
 nj(zj)∧(1−zj) = 0
in Λ2(C∗) and, secondly, that ξ is considered only up to the addition of ﬁve-
term relations [x]+[y]+

 1−x
1−xy

+[1−xy]+

 1−y
1−xy

with x, y ∈X, xy̸ = 1. If we
lift each zj to some ˆzj = (uj, vj) in 
X, then the relation 
 nj(zj)∧(1−zj) = 0
in Λ2(C∗) says that the sum 
 nj (uj) ∧(vj) ∈Λ2(C) has the form 2πi ∧A
for some A ∈C depending on the liftings ˆzj = (uj, vj). If we change these lifts
to ˆz′
j = (u′
j, v′
j) with u′
j = uj + 2πirj, v′
j = vj + 2πisj with rj and sj in Z,
then A changes to A′ = A+
 nj(rjvj −sjuj +2πirjsj), so the formula given
above for the behavior of D under covering transformations of 
X implies that
the expression (“enhanced dilogarithm”)
Denh(ξ) =

j
nj D(ˆzj) −πiA ∈C/π2Q
is independent of the choice of lifts ˆzj. (This independence is true only modulo
π2Q, and not in general modulo 2π2Z, as asserted in [47], because the group
generated by the zj and 1−zj may contain torsion of arbitrary order.) Any 5-
term relation is in the kernel of Denh, so Denh does indeed give a well-deﬁned
map from the Bloch group BC to C/π2Q. (The treatment in [30] is more
26
Don Zagier
precise since Nahm works with an extension BC of BC on which the value of
Denh makes sense modulo 2π2Z.) Furthermore, the relation 
 nj(zj) ∧(1 −
zj) = 0 implies that 
 ℑ(¯ujvj) belongs to π2Q, so formula (1) implies that
ℑDenh(ξ) = D(ξ) for any ξ ∈BC .
In §4 of Chapter I we explained the relation of D to hyperbolic volumes. In
particular, if M is any oriented compact hyperbolic 3-manifold (or complete
hyperbolic 3-manifold with cusps), and if we triangulate M into oriented ideal
hyperbolic tetrahedra ∆j, then the expression ξM = 
[zj], where zj is the
cross-ratio of the vertices of ∆j, lies in BC and the interpretation of D(zj) as
Vol(∆j) implies that the imaginary part of Denh(ξM) is the hyperbolic volume
of M. The corresponding interpretation of the real part ℜDenh(ξM) ∈R/π2Q
is that it is equal (up to a normalizing factor) to the Chern-Simons invariant
of M. For further discussion of this, see Neumann [33] as well as [32] and [42].
We refer the reader to §7 of [47] for an interesting number-theoretic ap-
plication of the enhanced dilogarithm related to a conjectural formula which
is both a generalization of the classical Kronecker limit formula and a re-
ﬁnement of (a special case of) the Gross-Stark conjecture on special values
of Artin L-functions. Very roughly, if A is an ideal class of an imaginary
quadratic ﬁeld K = Q(
√
d), d < 0, then the value at s = 2 of the partial zeta
function ζK,A(s) = 
a∈A N(a)−s is known by results of Deninger [13] and
Levin [25] to be of the form π2d−3/2D(ξK,A) for some ξK,A ∈BQ, and in [47]
an “enhanced” partial zeta value ζenh
K,A(2) ∈C/π2d1/2Q is deﬁned for which
the formula ζenh
K,A(2) = π2d−3/2Denh(ξK,A) can be conjectured and tested nu-
merically in many examples.
C. The double logarithm. In recent years there has been a resurgence of
interest in the “multiple zeta values”
ζ(k1, . . . , km) =

n1,...,nm∈Z
0<n1<···<nm
1
nk1
1
· · · nkm
m
originally deﬁned (for m = 2) by Euler; these numbers turn up in particular
in connection with quantum invariants of knots and with the calculation of
certain Feynman diagram integrals. The multiple zeta values are simply the
specializations to x1 = · · · = xm = 1 of the multiple polylogarithm functions
Lik1,...,km(x1, . . . , xm) =

n1,...,nm∈Z
0<n1<···<nm
xn1
1
· · · xnm
m
nk1
1
· · · nkm
m
which for m = 1 is the ordinary polylogarithm function.
In the hierarchy of multiple polylogarithm functions, the key invariant is
the total weight k1 + · · · + km. The only multiple polylogarithm of weight 1
is the ordinary logarithm Li1(x) = −log(1 −x), but there are two multiple
polylogarithms of weight 2, the dilogarithm function Li2(x) and the double
logarithm function [21]
The Dilogarithm Function
27
Li1,1(x, y) =

0<m<n
xmyn
m n
(x, y ∈C, |y| < 1, |xy| < 1).
The remarkable fact here is that the function Li1,1, which has two arguments
and hence is a priori a more complicated type of object than the one-argument
function Li2, can in fact be expressed in terms only of the latter:
Proposition 1. For x, y ∈C with |xy| < 1, |y| < 1 we have
Li1,1(x, y) = Li2
xy −y
1 −y

−Li2
 −y
1 −y

−Li2(xy) .
(2)
Before proving this identity, we mention some equivalent formulas and con-
sequences. First of all, the double logarithm function satisﬁes the identity—the
simplest case of the “shuﬄe relations” satisﬁed by all multiple zeta values and
multiple polylogarithms—
Li1,1(x, y) + Li1,1(y, x) + Li2(xy) = Li1(x) Li1(y) ,
(3)
which is an immediate consequence of the fact that any pair of positive integers
(m, n) must satisfy exactly one of the three conditions 0 < m < n, 0 < n < m,
or 0 < m = n. Combining this with (2) and interchanging the roles of x and
y, we can rewrite (2) in the equivalent form
Li1,1(x, y) = Li1(x) Li1(y) + Li2
 −x
1 −x

−Li2
xy −x
1 −x

,
(4)
which is slightly less pretty than (2) in that it involves products of logarithms
as well as dilogarithms, but has the advantage of containing only two rather
than three dilogarithms. And if we use (4) to express both Li1,1(x, y) and
Li1,1(y, x) in (3) in terms of dilogarithms, we obtain what is perhaps the most
natural proof of the ﬁve-term relation.
We now give the proof of Proposition 1 (in the form (4) or (2)). In fact,
just for fun we give three proofs.
(i) We have
∂
∂y Li1,1(x, y) =

0<m<n
xm
m yn−1 =
∞

m=1
xm
m
ym
1 −y
=
1
1 −y log
1
1 −xy .
The derivative with respect to y of the right-hand side of (4) (or of (2)) has
the same value and both sides of (4) (or of (2)) vanish at y = 0.
(ii) We have
∂
∂x Li1,1(x, y) =

0<m<n
xm−1 yn
n
=
∞

n=1
1 −xn−1
1 −x
yn
n
=
1
1 −x log
1
1 −y −
1
x(1 −x) log
1
1 −xy .
28
Don Zagier
The derivative with respect to x of the right-hand side of (4) (or of (2)) has
the same value and both sides of (4) (or of (2)) vanish at x = 0.
(iii) Write the right-hand side of (4) as

m, n≥1
xm
m
yn
n
+
∞

k=1
 −x
1 −x
k 1 −(1 −y)k
k2
=

m, n≥1
xmyn
 1
mn −

n≤k≤m
(−1)k−1
k2
m −1
k −1
k
n

and then verify as an elementary combinatorial exercise that the expression
in square brackets, which clearly equals
1
mn if m < n, vanishes if m ≥n.
It seems very surprising that the beautiful identities (2) and (4) are not
better known.
D. The quantum dilogarithm The “quantum dilogarithm,” studied by
Faddeev-Kashaev [15], Kirillov [22] and other authors, is the function of two
variables deﬁned by the series
Li2(x; q) =
∞

n=1
xn
n (1 −qn) .
(5)
It is a q-deformation of the ordinary dilogarithm in the sense that
lim
ε→0

ε Li2(x; e−ε)

= Li2(x)
(|x| < 1) ;
(6)
indeed, using the expansion
1
1−e−t
=
1
t + 1
2 +
t
12 −
t3
720 + · · · we obtain a
complete asymptotic expansion
Li2(x; e−ε) = Li2(x) ε−1 + 1
2 log

1
1 −x

+
x
1 −x
ε
12 −
x + x2
(1 −x)3
ε3
720 + · · ·
as ε →0 with x ﬁxed, |x| < 1.
The function (5) belongs to the world of “q-series.” These series, about
which there is a very extensive literature—with the letter “q” having been
the traditional choice long before it was realized that there was any connec-
tion with the “q” of “quantum”—are functions of a formal (or small complex)
variable q which are given by convergent inﬁnite series whose terms are ratio-
nal functions of q with rational coeﬃcients. For instance, the q-hypergeometric
functions, a very important subclass which includes some classical modular
forms and related functions like Ramanujan’s “mock theta functions” (which
have occurred in connection with quantum invariants of 3-manifolds [24]) are
given by series whose nth term has the form n
i=1 R(q, qi) for some rational
function R(x, y) of two variables. The classical aspects of q-series are those
having to do with the behavior as q tends to 0 and typically are concerned
The Dilogarithm Function
29
with proving identities F(q) = G(q) between two given q-series considered
as elements of Q[[q]]. This is usually done either by purely combinatorial ar-
guments (such as interpreting the coeﬃcients of qn in F(q) and G(q) as the
numbers of partitions of n of two diﬀerent types and then giving a bijection
between these) or else via algebraic tricks such as introducing an extra para-
meter x and showing that both F(x, q) and G(x, q) satisfy the same functional
equations under x →qx (as in the proof of Proposition 2 below). The quan-
tum aspects, on the other hand, are the ones that emerge when one studies
the asymptotic behavior of the q-series as q tends to 1 (or more generally to
a root of unity) rather than to 0, an example being the asymptotic expansion
of Li2(x; e−ε) as ε →0 given above.
In the study of q-hypergeometric functions and other q-series, an important
role is played by the q-analogues
(q)n :=
n
	
m=1
(1 −qm) ,
(x; q)n :=
n−1
	
i=0
(1 −qix)
of the classical factorial function and Pochhammer symbol, respectively. One
can also allow n = ∞and set
(q)∞:=
∞
	
m=1
(1 −qm) ,
(x; q)∞:=
∞
	
i=0
(1 −qi x),
the q-analogues of the classical gamma function; the function (q)∞is up to a
factor q1/24 the modular form η(τ) (Dedekind eta-function), where q = e2πiτ.
Observe that the ﬁnite products can be expressed in terms of the inﬁnite
ones by (q)n = (q)∞/(qn+1; q)∞and (x; q)n = (x; q)∞/(qnx; q)∞. Following a
much-practised abuse of notation we will consider q as given and omit it from
the notations, writing simply (x)n and (x)∞instead of (x; q)n and (x; q)∞.
This causes no confusion with the notations (q)n and (q)∞since (q)n = (q; q)n
and (q)∞= (q; q)∞, but is an abuse of notation because, for instance, (q)2
means (1−q)(1−q2) but (x)2 means (1−x)(1−qx) rather than (1−x)(1−x2).
The ﬁrst surprise is now that the quantum dilogarithm Li2(x; q) is essen-
tially equivalent to the q-gamma function (x)∞! This is the third part of the
following simple (and well-known) result which gives the expansions of the
functions (x)∞, 1/(x)∞and log(x)∞as power series in x . All three formulas
will play a role in §3 in connection with Nahm’s conjecture.
Proposition 2. For x, q ∈C with |x| < 1, |q| < 1 we have the power series
expansions
(x; q)∞=
∞

n=0
(−1)n q(
n
2)
(q)n
xn ,
(7)
1
(x; q)∞
=
∞

n=0
xn
(q)n
,
(8)
−log(x; q)∞= Li2(x; q) .
(9)
30
Don Zagier
Proof. All three of these identities can be proved in essentially the same way.
To emphasize this, we present the three proofs simultaneously. Since (x)∞is
obviously a power series in x with constant term 1, we can write
(x)∞=
∞

n=0
an xn ,
1
(x)∞
=
∞

n=0
bn xn ,
−log(x)∞=
∞

n=1
cn xn
for some coeﬃcients an, bn and cn depending on q, a0 = b0 = 1. Combining
each of these expansions with the functional equation (x)∞= (1 −x) (qx)∞
and comparing the coeﬃcients of xn on both sides, we ﬁnd
(1 −qn) an = −qn−1 an−1 ,
(1 −qn) bn = bn−1 ,
(1 −qn) cn = 1
n ,
from which the desired formulas
an = (−1)n q(
n
2)
(q)n
,
bn =
1
(q)n
cn = 1
n ·
1
1 −qn
(10)
follow immediately or by induction. Note that the third identity of the propo-
sition can also be proved directly, without using the functional equation of
(x)∞, by the calculation
−log(x)∞=
∞

i=0
−log(1 −qix) =
∞

i=0
∞

n=1
1
n qin xn =
∞

n=1
xn
n (1 −qn) ,
i.e., Li2(x; q) = 
∞
i=0 Li1(qix).
The second surprise is the discovery by Faddeev and Kashaev [15] that the
q-dilogarithm satisﬁes a non-commutative 5-term functional equation which
degenerates in the limit q →1 to the classical 5-term functional equation
of the classical dilogarithm. We content ourselves with stating and proving
the ﬁrst statement only, referring the reader for the second statement (which
involves the use of the Baker-Campbell-Hausdorﬀformula) to the original
paper, or to the more recent survey paper by Zudilin [48].
Proposition 3 ([38], [15], [22]). Let u and v be non-commuting variables
satisfying the commutation relation
u v = q v u .
(11)
Then
(v)∞(u)∞= (u)∞(−vu)∞(v)∞.
(12)
Proof. Expanding each factor (x)∞in (12) by equation (7) and observing that
vnum = q−mnumvn and (vu)s = q−(
s+1
2 )usvs, we ﬁnd that (12) is equivalent
to the generating series identity
The Dilogarithm Function
31

m, n≥0
q−mn am an um vn =

r, s, t≥0
(−1)sq−(
s+1
2 ) ar as at ur+s vs+t
with an as in (10) or, comparing coeﬃcients of like monomials, to the combi-
natorial identity

r, s, t≥0
r+s=m, s+t=n
qrt
(q)r (q)s (q)t
=
1
(q)m (q)n
(m, n ≥0) .
(13)
(Amusingly, if we write (12) in the equivalent form (v)−1
∞(−vu)−1
∞(u)−1
∞=
(u)−1
∞(v)−1
∞and expand each term (x)−1
∞using (8) instead of (7), then the
combinatorial identity to be proved turns out to exactly the same formula
(13), but with q replaced by q−1.) Identity (13) can be proved either using
generating functions (now commutative!) by multiplying both sides by xmyn,
summing over m, n ≥0, and applying (8) and the easy identity 
∞
r=0
(y)r
(q)r xr =
(xy)∞
(x)∞, or else by using the standard recursion property

 m+1
s

= qs
 m
s

+

 m
s−1

of the q-binomial coeﬃcient

 m
s

=
(q)m
(q)s(q)m−s to show that the numbers
Cm,n := 
s

 m
s

q(m−s)(n−s)
(q)n
(q)n−s satisfy Cm+1,n = qnCm,n + (1 −qn)Cm,n−1
and hence by induction Cm,n = 1 for all m, n ≥0.
E. The p-adic dilogarithm and the dianalog.
The next dilogarithm
variant we mention is the p-adic dilogarithm, studied by R. Coleman and
other authors. We ﬁx a prime number p and deﬁne
Li(p)
2 (x) =

n>0, p∤n
xn
n2 .
(14)
This function can be written as Li2(x)−p−2Li2(xp), so in the complex domain
it is simply a combination of ordinary dilogarithms and of no independent
interest, but because we have omitted the terms in (14) with p’s in the de-
nominator, the power series converges p-adically for all p-adic numbers x with
valuation |x|p < 1. The function Li(p)
2 (x), and the corresponding higher p-adic
polylogarithms Li(p)
m (x), have good properties of analytic continuation and are
related to p-adic L-functions [11]. Furthermore, the p-adic dilogarithm and p-
adic polylogarithms have modiﬁed versions analogous to the Bloch-Wigner
dilogarithm and Bloch-Wigner-Ramakrishnan polylogarithms which satisfy
the same “clean” functional equations as their complex counterparts [41].
Finally, instead of working over the p-adic numbers we can work over the
ﬁnite ﬁeld Fp and consider the ﬁnite sum
£2(x) = £(p)
2 (x) =

0<n<p
xn
n2 ,
(15)
32
Don Zagier
a polynomial with coeﬃcients in Fp. The corresponding analogue £1(x) =

p−1
n=1 xn/n of the 1-logarithm was ﬁrst proposed (under the name “The 1 1
2-
logarithm”) by M. Kontsevich in a note in the informal Festschrift prepared
on the occasion of F. Hirzebruch’s retirement as director of the Max Planck
Institute for Mathematics in Bonn [23]. Kontsevich showed that this function,
as a function from Fp to Fp, satisﬁes the 4-term functional equation
£1(x + y) = £1(y) + (1 −y)£1

x
1 −y

+ y £1

−x
y

(16)
(the mod p analogue of the “fundamental equation of information theory”
satisﬁed by the classical entropy function −x log x −(1 −x) log(1 −x)), mid-
way between the 3-term functional equation of log(xy) −log(x) −log(y) = 0
of the classical logarithm function and the 5-term functional equation of
the classical dilogarithm, and also that £1 is characterized uniquely by this
functional equation together with the two one-variable functional equations
£1(x) = £1(1 −x) and x£1(1/x) = −£1(x). Kontsevich’s question whether
the higher polylogarithm analogues £m(x) = 
p−1
n=1 xn/nm satisﬁed similar
equations was taken up and answered positively by Ph. Elbaz-Vincent and
H. Gangl [14]. They called these functions “polyanalogs”, an amalgam of the
words “analogue,” “polylog,” and “pollyanna” (an American term suggesting
exaggerated or unwarranted optimism). Presumably the correct term for the
case m = 2 would then be “dianalog”, which has a pleasing British ﬂavo(u)r.
The main property of the dianalog and its higher-order generalizations,
generalizing the identities found by Kontsevich for m = 1, is that if we con-
sider them as functions from Fp to Fp (rather than as polynomials with co-
eﬃcients in Fp) they satisfy functional equations which are reminiscent of,
but of a somewhat diﬀerent type than, the functional equations of the clas-
sical polylogarithms. In particular, Elbaz-Vincent and Gangl proved that the
dianalog function satisﬁes several functional equations: the easy symmetry
property £2(x) = x£2(1/x), the somewhat less obvious three-term relation
£2(1 −x) −£2(x) + x£2(1 −1/x) = 0, and the “Kummer-Spence analogue”
£2(xy) + y £2
x
y

−(1 + y) £2(x) −(1 + x) £2(y)
−(1 −y)

£2
y(x −1)
1 −y

−£2
1 −x
1 −y

−x(1 −y)

£2
y(1 −x)
x(1 −y)

−£2
 x −1
x(1 −y)

= 0 ,
each of which is the analogue of a classical functional equation of the trilog-
arithm. There is also a 22-term functional equation based on Cathelineau’s
diﬀerential version of the trilogarithm. Moreover, in each of the functional
equations for £1 and £2, if one replaces the polynomial factors preceding the
polyanalogs (for instance, the factors 1−y and y preceding £1(x/(1−y)) and
£1(−x/y) in (16)) by their pth powers, then the functional equation becomes
The Dilogarithm Function
33
true as an identity between polynomials in Fp[x, y] and not merely as an equal-
ity between functions from Fp × Fp to Fp. Finally, by passing via the p-adics
and using a recent result of Besser [4] expressing the polyanalogs (now again
considered as functions rather than polynomials) as the mod p reductions
of certain derivatives of modiﬁed p-adic polylogarithm functions, the authors
show how functional equations of the mth classical complex polylogarithm
induce by a process of diﬀerentiation corresponding functional equations of
the (m −1)-st polyanalog. The whole story is intimately related to Cathelin-
eau’s theory of inﬁnitesimal polylogarithms (inﬁnitesimal or Lie version of the
Bloch group), which is yet another and even more subtle manifestation of the
world of polylogarithms.
We do not give any further details, referring the reader to the original
papers [8] and [14].
