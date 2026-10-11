---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-003-5-and-values-of-dedekind-zeta-functions
section_title: ". . . and values of Dedekind zeta functions"
section_number: 5
pages: 14-18
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
---
Let F be an algebraic number ﬁeld, say of degree N over Q. Among its most
important invariants are the discriminant d, the numbers r1 and r2 of real and
imaginary archimedean valuations, and the Dedekind zeta-function ζF (s). For
the non-number-theorist we recall the (approximate) deﬁnitions. The ﬁeld
F can be represented as Q(α) where α is a root of an irreducible monic
polynomial f ∈Z[x] of degree N. The discriminant of f is an integer df and
d is given by c−2df for some natural number c with c2 | df. The polynomial f,
which is irreducible over Q, in general becomes reducible over R, where it splits
into r1 linear and r2 quadratic factors (thus r1 ≥0, r2 ≥0, r1 + 2r2 = N). It
also in general becomes reducible when it is reduced modulo a prime p, but
if p ∤df then its irreducible factors modulo p are all distinct, say r1,p linear
factors, r2,p quadratic ones, etc. (so r1,p + 2r2,p + · · · = N). Then ζF (s) is
the Dirichlet series given by an Euler product 
p Zp(p−s)−1 where Zp(t) for
p ∤df is the monic polynomial (1 −t)r1,p(1 −t2)r2,p · · · of degree N and Zp(t)
for p | df is a certain monic polynomial of degree ≤N. Thus (r1, r2) and ζF (s)
encode the information about the behaviour of f (and hence F) over the real
and p-adic numbers, respectively.
As an example, let F be an imaginary quadratic ﬁeld Q(√−a) with a ≥1
squarefree. Here N = 2, d = −a or −4a, r1 = 0, r2 = 1. The Dedekind
zeta function has the form 
n≥1 r(n)n−s where r(n) counts representations
of n by certain quadratic forms of discriminant d; it can also be represented
as the product of the Riemann zeta function ζ(s) = ζQ(s) with an L-series
L(s) = 
n≥1
 d
n

n−s where
 d
n

is a symbol taking the values ±1 or 0 and
which is periodic of period |d| in n. Thus for a = 7
The Dilogarithm Function
17
ζQ(√−7)(s) = 1
2

(x,y)̸=(0,0)
1
(x2 + xy + 2y2)s
=
 ∞

n=1
n−s
  ∞

n=1
−7
n

n−s

where
−7
n

is +1 for n ≡1, 2, 4 (mod 7), −1 for n ≡3, 5, 6 (mod 7), and 0
for n ≡0 (mod 7).
One of the questions of interest is the evaluation of the Dedekind zeta
function at suitable integer arguments. For the Riemann zeta function we have
the special values cited at the beginning of this paper. More generally, if F is
totally real (i.e., r1 = N, r2 = 0), then a theorem of Siegel and Klingen implies
that ζF (m) for m = 2, 4, . . . equals πmN/

|d| times a rational number. If
r2 > 0, then no such simple result holds. However, in the case F = Q(√−a),
by using the representation ζF (s) = ζ(s)L(s) and the formula ζ(2) = π2/6
and writing the periodic function
 d
n

as a ﬁnite linear combination of terms
e2πikn/|d| we obtain
ζF (2) =
π2
6

|d|
|d|−1

n=1
 d
n

D(e2πin/|d|)
(F imaginary quadratic),
e.g.,
ζQ(√−7)(2) = π2
3
√
7

D

e2πi/7
+ D

e4πi/7
−D

e6πi/7
.
Thus the values of ζF (2) for imaginary quadratic ﬁelds can be expressed in
closed form in terms of values of the Bloch-Wigner function D(z) at algebraic
arguments z.
By using the ideas of the last section we can prove a much stronger state-
ment. Let O denote the ring of integers of F (this is the Z-lattice in C spanned
by 1 and √−a or (1+√−a)/2, depending whether d = −4a or d = −a). Then
the group Γ = SL2(O) is a discrete subgroup of SL2(C) and therefore acts
on hyperbolic space H3 by isometries. A classical result of Humbert gives the
volume of the quotient space H3/Γ as |d|3/2 ζF (2)/4π2. On the other hand,
H3/Γ (or, more precisely, a certain covering of it of low degree) can be trian-
gulated into ideal tetrahedra with vertices belonging to P1(F) ⊂P1(C), and
this leads to a representation
ζF (2) =
π2
3|d|3/2

ν
nν D(zν)
with nν in Z and zν in F itself rather than in the much larger ﬁeld Q(e2πin/|d|)
([8], Theorem 3). For instance, in our example F = Q(√−7) we ﬁnd
ζF (2) =
4π2
21
√
7

2D
1 + √−7
2

+ D
−1 + √−7
4

.
18
Don Zagier
This equation together with the fact that ζF (2) = 1.89484144897 · · ·̸ = 0
implies that the element (13) has inﬁnite order in BC.
In [8], it was pointed out that the same kind of argument works for all
number ﬁelds, not just imaginary quadratic ones. If r2 = 1 but N > 2 then
one can again associate to F (in many diﬀerent ways) a discrete subgroup Γ ⊂
SL2(C) such that Vol(H3/Γ) is a rational multiple of |d|1/2ζF (2)/π2N−2. This
manifold H3/Γ is now compact, so the decomposition into ideal tetrahedra
is a little less obvious than in the case of imaginary quadratic F, but by
decomposing into non-ideal tetrahedra (tetrahedra with vertices in the interior
of H3) and writing these as diﬀerences of ideal ones, it was shown that the
volume is an integral linear combination of values of D(z) with z of degree at
most 4 over F. For F completely arbitrary there is still a similar statement,
except that now one gets discrete groups Γ acting on Hr2
3 ; the ﬁnal result ([8],
Theorem 1) is that |d|1/2 × ζF (2)/π2(r1+r2) is a rational linear combination
of r2-fold products D(z(1)) · · · D(z(r2)) with each z(i) of degree ≤4 over F
(more precisely, over the ith complex embedding F (i) of F, i.e. over the subﬁeld
Q(α(i)) of C, where α(i) is one of the two roots of the ith quadratic factor of
f(x) over R).
But in fact much more is true: the z(i) can be chosen in F (i) itself (rather
than of degree 4 over this ﬁeld), and the phrase “rational linear combination
of r2-fold products” can be replaced by “rational multiple of an r2 × r2 de-
terminant.” We will not attempt to give more than a very sketchy account
of why this is true, lumping together work of Wigner, Bloch, Dupont, Sah,
Levine, Merkuriev, Suslin, . . . for the purpose (references are [1], [3], and the
survey paper [7]). This work connects the Bloch group deﬁned in the last
section with the algebraic K-theory of the underlying ﬁeld; speciﬁcally, the
group2 BF is equal, at least after tensoring it with Q, to a certain quotient
Kind
3
(F) of K3(F). The exact deﬁnition of Kind
3
(F) is not relevant here. What
is relevant is that this group has been studied by Borel [2], who showed that
it is isomorphic (modulo torsion) to Zr2 and that there is a canonical homo-
morphism, the “regulator mapping,” from it into Rr2 such that the co-volume
of the image is a non-zero rational multiple of |d|1/2ζF (2)/π2r1+2r2; moreover,
it is known that under the identiﬁcation of Kind
3
(F) with BF this mapping
corresponds to the composition BF →(BC)r2
D
→Rr2, where the ﬁrst arrow
comes from using the r2 embeddings F ⊂C (α →α(i)). Putting all this
together gives the following beautiful picture. The group BF /{torsion} is iso-
morphic to Zr2. Let ξ1, . . . , ξr2 be any r2 linearly independent elements of it,
and form the matrix with entries D(ξ(i)
j ), (i, j = 1, . . . , r2). Then the deter-
minant of this matrix is a non-zero rational multiple of |d|1/2ζF (2)/π2r1+2r2.
If instead of taking any r2 linearly independent elements we choose the ξj to
2 It should be mentioned that the deﬁnition of BF which we gave for F = C or
Q must be modiﬁed slightly when F is a number ﬁeld because F × is no longer
divisible; however, this is a minor point, aﬀecting only the torsion in the Bloch
group, and will be ignored here.
The Dilogarithm Function
19
be a basis of BF /{torsion}, then this rational multiple (chosen positively) is
an invariant of F, independent of the choice of ξj. This rational multiple is
then conjecturally related to the quotient of the order of K3(F)torsion by the
order of the ﬁnite group K2(OF ), where OF denotes the ring of integers of F
(Lichtenbaum conjectures).
This all sounds very abstract, but is in fact not. There is a reasonably
eﬃcient algorithm to produce many elements in BF for any number ﬁeld F.
If we do this, for instance, for F an imaginary quadratic ﬁeld, and compute
D(ξ) for each element ξ ∈BF which we ﬁnd, then after a while we are
at least morally certain of having identiﬁed the lattice D(BF ) ⊂R exactly
(after ﬁnding k elements at random, we have only about one chance in 2k of
having landed in the same non-trivial sublattice each time). By the results
just quoted, this lattice is generated by a number of the form κ|d|3/2ζF (2)/π2
with κ rational, and the conjecture referred to above says that κ should have
the form 3/2T where T is the order of the ﬁnite group K2(OF ), at least for
d < −4 (in this case the order of K3(F)torsion is always 24). Calculations done
by H. Gangl in Bonn for several hundred imaginary quadratic ﬁelds support
this; the κ he found all have the form 3/2T for some integer T and this integer
agrees with the order of K2(OF ) in the few cases where the latter is known.
E
Here is a small excerpt from his tables:
|d|
7 8 11 15 19 20 23 24 31 35 39 40 · · · 303 472 479 491 555 583
T
2 1 1
2
1
1
2
1
2
2
6
1 · · · 22
5
14
13
28
34
(the omitted values contain only the primes 2 and 3; 3 occurs whenever d ≡3
mod 9 and there is also some regularity in the powers of 2 occurring). Thus
one of the many virtues of the mysterious dilogarithm is that it gives, at least
conjecturally, an eﬀective way of calculating the orders of certain groups in
algebraic K-theory!
To conclude, we mention that Borel’s work connects not only Kind
3
(F) and
ζF (2) but more generally Kind
2m−1(F) and ζF (m) for any integer m > 1. No
elementary description of the higher K-groups analogous to the description of
K3 in terms of B is known, but one can at least speculate that these groups
and their regulator mappings may be related to the higher polylogarithms
and that, more speciﬁcally, the value of ζF (m) is always a simple multiple
of a determinant (r2 × r2 or (r1 + r2) × (r1 + r2) depending whether m is
even or odd) whose entries are linear combinations of values of the Bloch-
Wigner-Ramakrishnan function Dm(z) with arguments z ∈F. As the simplest
case, one can guess that for a real quadratic ﬁeld F the value of ζF (3)/ζ(3)
(= L(3), where L(s) is the Dirichlet L-function of a real quadratic character
of period d) is equal to d5/2 times a simple rational linear combination of
diﬀerences D3(x) −D3(x′) with x ∈F, where x′ denotes the conjugate of x
over Q. Here is one (numerical) example of this:
20
Don Zagier
2−555/2ζQ(
√
5)(3)/ζ(3) = D3
1 +
√
5
2

−D3
1 −
√
5
2

−1
3

D3(2 +
√
5) −D3(2 −
√
5)

(both sides are equal approximately to 1.493317411778544726). I have found
many other examples, but the general picture is not yet clear.
F
