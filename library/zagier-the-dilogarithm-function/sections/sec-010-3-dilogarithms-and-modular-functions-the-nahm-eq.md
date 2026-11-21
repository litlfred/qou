---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-010-3-dilogarithms-and-modular-functions-the-nahm-eq
section_title: "Dilogarithms and modular functions: the Nahm equation"
section_number: 3
pages: 39-56
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
A fascinating and almost completely unsolved problem is to understand
the overlap between the classes of q-hypergeometric functions and modular
forms or functions, the prototypical case being given by the famous Rogers-
Ramanujan identities. Nahm’s conjecture gives us a ﬁrst glimpse of an an-
swer, which surprisingly involves dilogarithms and the Bloch group. In sub-
sections A and B we describe the conjecture and some of the examples which
motivate it, while subsection C contains an asymptotic analysis of the q-series
involved and the proof that the conjecture is true in the simplest case.
A. q-hypergeometric series and Nahm’s conjecture. Consider the two
power series G(q) and H(q) by
G(q) =
∞

n=0
qn2
(q)n
,
H(q) =
∞

n=0
qn2+n
(q)n
(|q| < 1),
where (q)n as in §1 denotes the product (1−q)(1−q2) · · · (1−qn). The classical
Rogers-Ramanujan identities—discovered by Rogers in 1897, rediscovered by
Ramanujan in 1915 and then given a third proof by both authors jointly
and many further proofs in subsequent years—says that these two series have
product developments
G(q) =
	
n ≡±1 (mod 5)
1
1 −qn ,
H(q) =
	
n≡±2 (mod 5)
1
1 −qn .
The important thing here is not so much that these functions have product ex-
pansions as that, up to rational powers of q, they are both modular functions.
Indeed, by the Jacobi triple product formula, we can rewrite the identities as
G(q) =
1
(q)∞

n∈Z
(−1)n q(5n2+n)/2,
H(q) =
1
(q)∞

n∈Z
(−1)n q(5n2+3n)/2
or, even more intelligently, as
q−1/60 G(q) = θ5,1(z)
η(z) ,
q11/60 H(q) = θ5,2(z)
η(z) ,
(23)
42
Don Zagier
where q = e2πiz with z ∈H (upper half-plane) and
η(z) = q1/24
∞
	
n=1
(1 −qn),
θ5,j(z) =

n ≡2j−1 (mod 10)
(−1)[n/10] qn2/40 .
The point is that η(z), θ5,1(z) and θ5,2(z) are all modular forms of weight 1/2
and therefore that the functions on the right-hand side of (23) are modular
functions, i.e., they are invariant under z →az+b
cz+d for all
 a b
c d

belonging to
some subgroup of ﬁnite index of SL(2, Z). Indeed, if we combine them into a
single vector-valued function
g(z) =

q−1/60G(q)
q11/60H(q)


z ∈H, qα := e2πiαz
,
then we have transformation formulas with respect to the full modular group:
g(z + 1) =
ζ−1
60
0
0
ζ11
60

g(z),
g

−1
z

=
2
√
5
sin 2π
5
sin π
5
sin π
5 −sin 2π
5

g(z)
(24)
(with ζN := e2πi/N) and hence g(γ(z)) = ρ(γ)g(z) for all γ ∈SL(2, Z) and
some representation ρ : SL(2, Z) →GL(2, C).
The functions G(q) and H(q) are special examples of what are called q-
hypergeometric series, i.e., series of the form 
∞
n=0 An(q) where A0(q) is a
rational function and An(q) = R(q, qn)An−1(q) for all n ≥1 for some rational
function R(x, y) with lim
x→0 lim
y→0 R(x, y) = 0. (For G and H one has A0 = 1
and R(x, y) = x−1y2/(1 −y) or y2/(1 −y), respectively.) There are only a
handful of examples known of q-hypergeometric series which are also modular,
and, as already mentioned in the introduction to this section, the problem
of describing when this happens in general is an important and fascinating
question, but totally out of reach for the moment. A remarkable conjecture
of Werner Nahm, discussed in more detail in his paper [30] in this volume as
well as in his earlier articles [28], [29], relates the answer to this question in
a very special case to dilogarithms and Bloch groups on the one hand and to
rational conformal ﬁeld theory on the other.
Nahm’s conjecture actually concerns certain r-fold hypergeometric series
(deﬁned as above but with n running over (Z≥0)r rather than just Z≥0). Let
A be a positive deﬁnite symmetric r × r matrix, B a vector of length r, and
C a scalar, all three with rational coeﬃcients. We deﬁne a function fA,B,C(z)
by the r-fold q-hypergeometric series
fA,B,C(z) =

n=(n1,...,nr) ∈(Z≥0)r
q
1
2 ntAn+Btn+C
(q)n1 · · · (q)nr
(z ∈H)
and ask when fA,B,C is a modular function. Nahm’s conjecture does not an-
swer this question completely, but predicts which A can occur. If A = (aij)
The Dilogarithm Function
43
is any positive deﬁnite symmetric r × r matrix with rational entries, we can
consider the system
1 −Qi =
r
	
j=1
Qaij
j
(i = 1, . . . , r)
(25)
of r equations in r unknowns, which we can write in abbreviated notation as
1 −Q = QA, Q = (Q1, . . . , Qr). We suppose ﬁrst that A has integral coeﬃ-
cients, so that the equations in (25) are polynomial. Since there are as many
equations as unknowns, we expect that the solutions form a 0-dimensional
variety, i.e., there are only ﬁnitely many solutions and (hence) all lie in Q, but
in any case, the system certainly has solutions in Q
r. For any such a solution
Q = (Q1, . . . , Qr) we can consider the element
ξQ = [Q1] + · · · + [Qr]
∈Z[F] ,
where F is the number ﬁeld Q(Q1, . . . , Qr). Then in Λ2(F ×) we ﬁnd
∂

ξQ

=
r

i=1
(Qi) ∧(1 −Qi) =
r

i=1
(Qi) ∧
 r
	
j=1
Qaij
j

=
r

i=1
(Qi) ∧
 r

j=1
aij(Qj)

=
r

i=1
r

j=1
aij (Qi) ∧(Qj) ,
and this is 0 since aij is symmetric and (Qi)∧(Qj) antisymmetric in i and j.
Hence ξA belongs to the Bloch group of F. If A is not integral, then we
have to be careful about the choice of determinations of the rational powers
Qaij
j
in (25). We require them to be consistent, i.e., we must have Qi = eui,
1 −Qi = evi for some vectors u, v ∈Cr such that v = Au. This deﬁnes the
minimal number ﬁeld F in which the equations (25) make sense. For instance,
if A =
 8/3 1/3
1/3 2/3

, we set (Q1, Q2) = (α, αβ3) where α, β ∈Q are solutions of
the system 1−α = α3β, 1−αβ3 = αβ2; then F = Q(α, β), and ξQ = [α]+[αβ3]
is an element of B(F). Nahm’s conjecture is then
Conjecture. Let A be a positive deﬁnite symmetric r×r matrix with rational
coeﬃcients. Then the following are equivalent:
(i) The element ξQ is a torsion element of B(F) for every solution Q of (25).
(ii) There exist B ∈Qr and C ∈Q such that fA,B,C(z) is a modular function.
The main motivation for this conjecture comes from physics, and in fact one
expects that all the modular functions fA,B,C which are obtained this way
are characters of rational conformal ﬁeld theories. (We will not discuss these
aspects at all, referring the reader for this to Nahm’s paper.) A further ex-
pectation, again predicted by the physics, is that if a matrix A satisﬁes the
conditions of the conjecture, then the collection of modular functions occur-
ring in statement (ii) span a vector space which is invariant under the action of
44
Don Zagier
SL(2, Z) (bosonic case) or at least Γ(2) (fermionic case), even though the indi-
vidual functions fA,B,C will in general have level greater than 2. For instance,
in the Rogers-Ramanujan identities given above, each of the two functions
(23) is modular (up to multiplication by a root of unity) only on the modular
group Γ0(5) of level 5 (and on a yet much smaller group if we do not allow
scalar multiples), but the vector space which they span is invariant under all
of SL(2, Z) by eq. (24). From a purely mathematical point of view, the mo-
tivation for the conjecture comes from the asymptotic analysis, discussed in
subsection B, and from the known examples, some of which we now describe.
B. Examples and discussion. In this subsection we describe a number of
examples which give numerical support for Nahm’s conjecture and which show
that two plausible alternative versions of the conjecture—one with a stronger
and one with a weaker hypothesis on the matrix A —are not tenable.
(a) Rank one examples. If r = 1, then the parameters A, B and C are
simply rational numbers and exactly seven cases are known where fA,B,C(z)
is a modular function, given by the following table:
Table 1. The modular functions fA,B,C for r = 1
A
B
C
fA,B,C(z)
2
0
−1/60
θ5,1(z)/η(z)
1
11/60
θ5,2(z)/η(z)
1
0
−1/48
η(z)2/η(z/2)η(2z)
1/2
1/24
η(2z)/η(z)
−1/2
1/24
2η(2z)/η(z)
1/2
0
−1/40
θ5,1(z/4)/θ8(z)
1/2
1/40
θ5,2(z/4)/θ8(z)
with θ5,j(z) and η(z) as in (23) and θ8(z) = 
n>0
 8
n

qn2/8 = η(z)η(4z)/η(2z) .
The ﬁrst two entries in this table are just the Rogers-Ramanujan identities
with which we began the discussion, and the product η(z)fA,B,C(z) in all
seven cases is a unary theta series (i.e., a function 
 ε(n)qλn2 with ε(n) an
even periodic function and λ a positive rational number). We will see in sub-
section B that these are the only triples (A, B, C) ∈Q+×Q2 for which fA,B,C
is modular. On the other hand, the element ξA when r = 1 consists of a single
element [Q1], where 1 −Q1 = QA
1 , so by the discussion in example (c) of §2B
we know that the only values of A > 0 for which condition (i) of the conjecture
is satisﬁed are A = 1/2, 1 or 2 (corresponding to Q1 = (−1 +
√
5)/2, 1/2 and
(3 −
√
5)/2, respectively). Thus Nahm’s conjecture holds for r = 1.
(b) Totally real, or torsion in the Bloch group? In the above examples,
the element Q1 was a totally real algebraic number. It is reasonable to ask
whether the requirement for modularity is really condition (i) of the conjecture
or merely the more elementary (but stronger) condition that equation (25) has
The Dilogarithm Function
45
only real solutions. To see that (i) really is the right condition, we consider the
matrix A =
 4 1
1 1

. In this case (25) specializes to the system of equations (19)
studied in example (b) of §2B, and by the discussion given there we know
that the corresponding element ξA ∈B(Q(ξA)) is torsion (of order 10) but is
not totally real. So if (i) rather than total reality is the correct condition in
the conjecture, then there should be pairs (B, C) ∈Q2 ×Q for which fA,B,C is
modular. After some experimentation, using a method which will be explained
brieﬂy at the end of subsection C, we ﬁnd that there are indeed at least two
such pairs, the corresponding identities being
f( 4 1
1 1 ), ( 0
1/2 ),
1
120
(z) = θ5,1(2z)
η(z)
,
f( 4 1
1 1 ), ( 2
1/2 ), 49
120
(z) = θ5,2(2z)
η(z)
,
where θ5,1(z) and θ5,2(z) are the same theta series as those occurring in (23).
(These equations were not proved, but only veriﬁed to a high order in the
power series in q.)
(c) Must all solutions be torsion? If A is any positive deﬁnite matrix,
even with real coeﬃcients, then the system of equations (25) has exactly one
solution with all Qi real and between 0 and 1. (To see this, one shows by
induction on r the more general assertion that the system 1−Qi = λi

j Qaij
j
has a unique solution in (0, 1)r for any real numbers λ1, . . . , λr > 0.) Denote
this solution by Q0 = (Q0
1, . . . , Q0
r). If the coeﬃcients of A are rational, the
Q0
i are real algebraic numbers (though not necessarily totally real—see (b))
and we obtain a speciﬁc element ξA = ξQ0 ∈B(Q ∩R). If condition (i) of
the conjecture is satisﬁed, then this must be a torsion element and hence
the corresponding Rogers dilogarithm value L(ξA) = 
 L(Q0
i ) must be a
rational multiple of π2. This criterion is numerically eﬀective (one can ﬁnd Q0
numerically to high precision by an iterative procedure and then test L(ξA)/π2
for rationality) and is the one used for the computer searches described in (d)
and (e) below. One can reasonably ask whether it is in fact suﬃcient, i.e.,
whether it is suﬃcient in (i) to assume only that ξA is torsion. An example
showing that this is not the case—we will see many others in (d) and (e)—is
given by the matrix A = ( 8
5
5
4). Here Q0 is equal to

φ−1 ψ, φ4 −φ3ψ

, with
φ = (
√
5 + 1)/2 and ψ = (1 +

2
√
5 −1)/2, and this is torsion, as we can
see numerically from the dilogarithm values ( L(ξ) = 8
5 L(1) for both ξQ0 and
its real conjugate and D(ξ) = 0 for both non-real conjugates of ξQ0) and
could verify algebraically as in section 2B. But the equations 1−Q1 = Q8
1Q5
2,
1 −Q2 = Q5
1Q4
2 have another Galois orbit of four solutions where (Q1, Q2)
belong to a diﬀerent quartic ﬁeld and where D(ξ)̸ = 0, so condition (i) of the
conjecture is not satisﬁed. Here a computer search ﬁnds no B and C making
fA,B,C modular.
(d) Rank two examples. An extensive search for positive deﬁnite matrices
A ∈M2(Q) for which L(ξA)/L(1) ∈Q (speciﬁcally, a search over A = 1
m
a b
b c

with integers a, b, c, m less than or equal to 100) found three inﬁnite families
46
Don Zagier
A =
 λα
1 −α
1 −α λ−1 α

,
ξA =

x, xλ = 1 −x

,
L(ξA) = L(1),
A =

α
2 −α
2 −α
α

,
ξA =
 √
5−1
2
,
√
5−1
2

,
L(ξA) =
6
5 L(1),
A =

α
1
2 −α
1
2 −α
α

,
ξA =
 3−
√
5
2
, 3−
√
5
2

,
L(ξA) =
4
5 L(1),
and 22 individual solutions (excluding split ones), namely the matrices
A
 2 1
1 1

 4 1
1 1

 4 2
2 2

 4 3
3 3
  8 3
3 2
  8 5
5 4

L(ξA)/L(1)
5/4
13/10
10/7
3/2
3/2
8/5
A
 11 9
9 8
  24 19
19 16
  2
1
1 3/2
  5/2 2
2
2
  8/3 1/3
1/3 2/3

L(ξA)/L(1)
17/10
9/5
9/7
7/5
8/7
and their inverses with L(ξA−1)/L(1) = 2−L(ξA)/L(1). (All of these examples
except for
 24 19
19 16

were already given in 1995 by Nahm’s student M. Terhoeven
in his thesis ([37], pp. 48–49), based on a search in the smaller domain with
“100” replaced by “11”.) Of these, the only ones that satisfy the stronger
condition that all solutions of (25) are torsion are

α
1 −α
1 −α
α

,
2 1
1 1

,
4 1
1 1

,
4 2
2 2

,
2
1
1 3/2

,
4/3 2/3
2/3 4/3

and their inverses, and indeed for each of these we ﬁnd several values of
B, C for which the function fA,B,C is (or appears to be) modular, while for
the others we never ﬁnd any. The list of these values is given in Table 2. The
formulas for the corresponding modular forms for A =
 4 1
1 1

were given in (b),
and the ones for A =

α
1−α
1−α
α

are given by the formula
f
α
1−α
1−α
α

,
 αν
−αν

, α
2 ν2 −1
24
(z) =
1
η(z)

n∈Z+ν
qαn2/2
(∀ν ∈Q),
(26)
which is easily proved using the identity

m,n≥0
m−n=r
qmn
(q)m(q)n
=
1
(q)∞
for any r ∈Z
(27)
(itself an easy consequence of eq. (7) and the Jacobi triple product formula).
For reasons of space we do not give the other modular forms explicitly in
Table 2, but only the numbers c = c(A) and K = K(A, B) deﬁned—if fA,B,C
is modular—by
fA,B,C

e−ε
= K ecπ2/6ε + O

ec′π2/6ε
(ε →0, c′ < c) .
(28)
The Dilogarithm Function
47
Table 2. Rank 2 examples for Nahm’s conjecture. Here αk = sin(πk/8), βk = 2/
√
5 sin(πk/5) and γk = 2/
√
7 sin(πk/7).
48
Don Zagier
According to the analysis in C below, these numbers—of which c corresponds
in conformal ﬁeld theory to the eﬀective central charge—are given by
c =
r

i=1

1 −L(Q0
i )
L(1)

= r −L(ξA)
L(1) ,
K =
1

det A
r
	
i=1
(Q0
i )bi

1 −Q0
i
,
(29)
where Q0 = (Q0
1, . . . , Q0
r) ∈(0, 1)r as above, B = (b1, . . . , br), and
A = A + diag

Q0
1
1 −Q0
1
, . . . ,
Q0
r
1 −Q0r

.
(30)
(e) Rank three examples. We conducted similar experiments for 3×3 matri-
ces, restricting the search to matrices with coeﬃcients which are integral and
≤10. In this range we found over 100 matrices A satisfying L(ξA)/L(1) ∈Q,
of which about one-third satisﬁed the stronger condition (i) of the conjecture.
These consisted of members of a three-parameter inﬁnite family
A = α


h2
h −h
h
1 −1
−h −1 1

+


A1 0 0
0 0 1
0 1 0


(α ∈Q, h ∈Z, A1 ∈{ 1
2, 1, 2})
(31)
together with eight sporadic solutions, and in all cases the computer found
pairs (B, C) making fA,B,C apparently modular. The pairs found for the eight
sporadic solutions (and for one member of the family (31) which had extra
solutions) are given in Table 3, while those for the family (31) are given by
B = αν


h
1
−1

+


B1
0
0

,
C = αν2
2
−1
24 + C1
(32)
where ν ∈Q and (A1, B1, C1) is one of the 7 rank one solutions given in
Table 1. Let us check that the matrices A in (31) indeed satisfy Nahm’s
criterion (i) and that the functions fA,B,C) for (B, C) as in (32) are indeed
modular. For the ﬁrst, we note that for this A Nahm’s equations (25) take the
form 1−Q1 = QA1
1 Rh, 1−Q2 = Q3R, 1−Q3 = Q2R−1 with R = (Qh
1Q2/Q3)α.
The last two give (1 −Q2)(1 −Q3) = Q2Q3 or Q2 + Q3 = 1, which implies
ﬁrst of all that [Q2] + [Q3] is torsion in the Bloch group and secondly that
R = 1 and hence (since h is integral!) that 1−Q1 = QA1
1 , which because of the
choice of A1 implies that [Q1] is also torsion. For the modularity, we note that
fA,B,C for (A, B, C) as in (31) and (32) is equal to 
 qQ(l,m,n)/(q)l(q)m(q)n
where the sum is over all l, m, n ≥0 and Q(l, m, n) is the quadratic form
Q(l, m, n) = α
2

hl + m −n −ν)2 + mn + A1
2 l2 + B1l + C1 −1
24 .
The identity (27) then gives
49

The Dilogarithm Function

or/6 on/T o/h sp/o U/T T/T 9/t  o@t/tt—9/T 0 0 )
2/T Z/T 0 0 z/T 0 T 0 0 T /T- i)
Z/T Z/t I 0 0 0 I I G/L 0 0 Z/T a
z 0 z if 0 0 z if if if 0 0
TOT To i
or z g
o7? oe F e° I- @ @ 7? Vv
° TPpe I- @ FP
ge/tt at/t og/T ve/ TL e/T 0 Pe/T 8p/T a1/T 8p/T 8P/T pe/s — ve/e SP/h sp/h  be/tT- 4 | 0
0 0 0 I o/T Z/t 0 G/L Z/t Z/t 0 0 I 0 I %
if 0 0 if if 0 0 @/I- I- @/I- 0 if 0 if 0 % a
z T 0 z z 0 0 0 I- I- @/T- T T Z/T /T 0
¢ aad TO z 10
Zz? art T=? 0% T=0 oat Vv
aro LZ Te
or/6 —os/et oF /6 or/t — os/e— ——OF/T p/tt pe/tt ops/g pg /gP8/T- B/T- JO
G/L 0 Z/T Z/T 0 Z/T G/L I 0 z/t 0 G/L
I T T 0 0 i) T S/T /T 0 JT 0 a
ale I o/T o/T 0 z/t I I I I 0 0
T Tt L Tot
=o Lae 2° ort v
Tae TLa@
ove 8/L F@/T>—8B/T 8/T 09/1 —2/,? ST/L— 2/24” O/T + 2/2? OBT/L- 2/200 3/00 @/ 0 9/1 -2/ | 0
ge 0 0 g a a0 a0 a0 0 a0 a0 a0
T z z } ib a0 a0 a0 a0 a0 a0 a0 a
T T 0 0 0 z/T + yan yao T+ yan yao 2/T— yan 2/T+ yao yao
z T 0 1- ¢ >” U-T yor ¢ >” U-T yoo z >” UT yor
faa ott 2 so v-[T » yo Sao v-—T yo fa5 v-—T » yo Vv
& I- - @ 8 yor yo Z/t+ zy 4 yor yo Z+ {yo & yor yo T+ zy

“TeuoryeT St 7 out] py? oY UT *

TeiZoqUr sty pue [eUOTPeI ore 1 puUR O OUT] YSIY oY} UT ‘aMyoofuoo s,wIYeN Joy soydurexe E yueY “gE eTqey,
50
Don Zagier
fA,B,C(z) =
1
η(z)

l≥0

r∈Z
qα(r+hl−ν)2/2

qA1l2/2+B1l+C1 ,
and (since h is integral!) we can now shift r by −hl in the inner sum to see
that fA,B,C is the product of fA1,B1,C1 and the function (26). We also remark
that one of the eight sporadic values of A also has an inﬁnite family of (B, C)
making fA,B,C modular (checked only numerically):
f 2 1 1
1 2 0
1 0 2

,

0
2ν
−2ν

, ν2−1
24
(z) =
1
η(z)

n∈Z+ν
qn2
(∀ν ∈Q).
(33)
(f) Duality. Finally, we remark that the conditions on A in the conjecture
are invariant under A →A−1. For (i) this is clear, since if Q is a solution of
(25) for some A then the vector Q⋆= (1 −Q1, . . . , 1 −Qr) is a solution for
A⋆= A−1 and ξQ⋆equals −ξQ modulo torsion in B(Q). On the modular side,
the analysis in C (speciﬁcally, eq. (38) below) suggests, though it does not
prove, that if fA,B,C is modular then fA⋆,B⋆,C⋆is also modular and has an
asymptotic expression as in (28) with (c, K) replaced by (c⋆, K⋆), where
(A⋆, B⋆, C⋆, c⋆, K⋆) =

A−1, A−1B, 1
2BtA−1B −r
24 −C, r −c, K
√
det A

.
These formulas, which one can verify in the examples in Table 2, were given
by Nahm in [28], p. 663–4 and [29], p. 164. On the conformal ﬁeld theory side,
the involution A ↔A−1 is related to a duality found by Goddard-Kent-Olive
[19] and to the so-called level-rank duality.
C. Asymptotic calculations. In this subsection we study the asymptotic
behavior of fA,B,C(z) as z →0 (q →1), concentrating for simplicity on the
case r = 1, and use it to verify that the table of rank one solutions given
in (a) of subsection B is complete. The analysis could in principle be carried
out for larger values of r, but this would require a considerable eﬀort and it
is not clear whether one could use the method to complete the classiﬁcation
even in the next case r = 2.
We consider real variables A > 0, B and C and write FA,B,C(q) instead of
fA,B,C(z), so that the deﬁnition (for r = 1) becomes
FA,B,C(q) =
∞

n=0
q
1
2 An2+Bn+C
(q)n
(A, B, C ∈R, A > 0).
(34)
Since FA,B,C(q) = qCFA,B,0(q), it is enough to study the case C = 0, in which
case we omit the index C from the notation.
Proposition 5. For any A, B ∈R, A > 0, we have the asymptotic expansion
log FA,B

e−ε
∼
∞

j=−1
cj(A, B) εj

ε ↘0

,
(35)
The Dilogarithm Function
51
with coeﬃcients cj(A, B) ∈R. The ﬁrst two coeﬃcients are given by
c−1(A, B) = L(1) −L(Q) ,
c0(A, B) = B log Q −1
2 log ∆,
(36)
where Q is the unique positive solution of Q + QA = 1, L(x) is the Rogers
dilogarithm, and ∆= A + Q −AQ, while cj(A, B) for j ≥1 is a polynomial
of degree j + 1 in B with coeﬃcients in Q[Q, A, ∆−1], e.g.
c1(A, B) = 1 −Q
2∆
B2 −Q(1 −Q)(1 −A)
2∆2
B
−(1 −Q)((1 −Q2)A3 −3QA2 + 3Q(1 + Q)A −2Q2)
24∆3
.
Before proving the proposition, we say a little bit more about the coef-
ﬁcients cj. The polynomial cj = cj(A, B) belongs to ∆−3jQ[A, Q, B∆]. Its
leading term is αjBj+1/(j + 1) where 
 αjxj is the Taylor expansion of
log Q(x), Q(x) + e−xQ(x)A = 1, e.g.
c2 = −Q(1 −Q)
6∆3
B3 + · · · ,
c3 = Q(1 −Q)(3Q −(1 + Q)∆)
24∆5
B4 + · · · .
We omit the other coeﬃcients, giving only the constant term of c2:
c2(A, 0) = Q(1 −Q)(A −1)
48 ∆6

−4A(A + 1)(A −1)2Q3
+ 3A(A −1)(A −2)(2A + 1)Q2 + 2A2(5A −4)Q −A3(2A −1)

.
We will describe three diﬀerent approaches for obtaining the asymptotics
of log FA,B(e−ε) as ε →0. The ﬁrst, based on a functional equation for
FA,B, is short and elementary, but gives the coeﬃcients cj(A, B) only up
to a term depending on A. The second is also elementary—essentially based
on the Euler-Maclaurin summation formula—and gives the entire asymptotic
expansion, but requires more work. The third, which is the one used by Nahm
and his collaborators, is based on Cauchy’s theorem together with formula (8)
for the quantum dilogarithm, and also leads to a full expansion; this method
also has a variant, using (7) rather than (8) for the quantum dilogarithm,
which has apparently not been noticed before. It seemed worth presenting all
three approaches, at least brieﬂy, since the information they give is somewhat
diﬀerent and since each of them is applicable (at least in principle) to the
general case of Nahm’s conjecture and to many other problems of this type.
(a) For the ﬁrst approach we set
FA,B

e−ε
FA,0

e−ε = QB HA,B(ε)
52
Don Zagier
where HA,B(ε) =
∞

n=0
hn(A, B) εn is a power series in ε satisfying HA,B(0) ≡1,
HA,0(ε) ≡1. Knowing HA,B(ε) is tantamount to knowing cj(A, B) −cj(A, 0)
for all j ≥1. The functional equation
FA,B(q) −FA,B+1(q) =
∞

n=1
q
1
2 An2+Bn
(q)n−1
= q
1
2 A+B FA,B+A(q)
(37)
of FA,B(q) gives a functional equation
HA,B(ε) = Q HA,B+1(ε) + (1 −Q) e−( 1
2 A+B)ε HA,B+A(ε)
for HA,B(ε). Write HA,B(ε) =
∞

n=0
hn(A, B) εn where h0 ≡1 and hn(A, B) is
a polynomial of degree 2n in B without constant term for n ≥1. Substituting
this into the functional equation and replacing B by B −A, we obtain
hn(A, B−A) = Q hn(A, B+1−A) + (1 −Q)
n

s=0
(A/2 −B)s
s!
hn−s(A, B) ,
and this equation gives the coeﬃcient hn,m of Bm in hn(A, B) recursively in
terms of earlier coeﬃcients hn′,m′ with n′ < n or with n′ = n, m′ < m.
Remark. The functional equation (37) remains true formally if one re-
places FA,B(q) by F ⋆
A,B(q) = qB2/2AF1/A,B/A(q−1), so the formal power se-
ries HA,B(ε) satisﬁes a second functional equation H1/A,B/A(−ε) = eεB2/2A
HA,B(ε). (Note that the change (A, B) →(1/A, B/A) changes Q to 1 −Q =
QA and does not change B2/A or QA.) It follows that the coeﬃcients cj(A, B)
in (35) satisfy the functional equations
cj(A, B) −(−1)j cj(1/A, B/A) = γj(A) +

B2/2A
if j = 1,
0
otherwise
for some constants γj = γj(A) independent of B. Using the explicit formulas
for cj which will be computed below, we ﬁnd that γ−1 = L(1), γ0 = −1
2 log A,
γ1 = −1
24, γ2 = γ3 = γ4 = 0. This suggests the conjecture that γj = 0 for
all j ≥2. Assuming this, we have the formal functional equation
F ⋆
A,B

e−ε
=
√
A exp

−π2
6ε + ε
24 + O

εN
FA,B

e−ε
(∀N > 0).
(38)
(b) The second method is based on the asymptotics of the individual terms
in the series (34). Denote the nth term in this series by un. Then the ratio
un/un−1 = qAn+B−A/2/(1−qn) is small for q small and large for q very near 1,
and becomes equal to 1 when qn is near to the unique root Q ∈(0, 1) of the
equation Q + QA = 1. The terms that contribute are therefore those of the
The Dilogarithm Function
53
form qn = Qq−ν with ν ∈ν0 + Z of order much less than n, where ν0 denotes
the fractional part of −log(Q)/ log(q). To know the size of un in this range we
ﬁrst have to know the behavior of (q)n as q →1 and n →∞with qn tending
to a ﬁxed number Q. It is given by:
Lemma. For ﬁxed Q ∈(0, 1) and q = e−ε →1 with qn = Qq−ν with n →∞,
ν = o(n), we have
log
 1
(q)n

∼
π2
6 −Li2(Q)

ε−1 −

(ν −1
2) log

1
1 −Q

+ 1
2 log
2π
ε

−
 1
24 + 1
2

ν2 −ν + 1
6)
Q
1 −Q

ε −
∞

r=3
Br(ν) Li2−r(Q) εr−1
r!
as ε →0, where Br(ν) denotes the rth Bernoulli polynomial and Li−j(Q) is
the negative-index polylogarithm Li−j(Q) =
∞

m=1
mjQm =

Q d
dQ
j
1
1 −Q.
Proof. The Euler-Maclaurin formula or the modularity of η(z) gives
log

1
(q)∞

= π2
6ε −1
2 log
2π
ε

−ε
24 + O

εN
for all N as ε →0. On the other hand, we have
log
 (q)n
(q)∞

=
∞

s=1
log

1
1 −qn+s

=
∞

s=1
log

1
1 −Qqs−ν

=
∞

s=1
∞

k=1
Qk
k qk(s−ν) =
∞

k=1
Qk
k
eνkε
ekε −1
=
∞

k=1
Qk
k
∞

r=0
Br(ν)
r!
(kε)r−1 =
∞

r=0
Br(ν)
r!
Li2−r(Q) εr−1 .
Subtracting these two formulas gives the desired result.
□
With the same conventions (q = e−ε, qn = Qq−ν), we also have
log

q
1
2 An2+Bn+C
= −Aε
2
log(1/Q)
ε
−ν
2
−Bε
log(1/Q)
ε
−ν

= −log(Q) log(1 −Q)
2ε
+

B −νA) log Q +

−Aν2
2
+ Bν

ε ,
where we have used A log(Q) = log(1 −Q). Together with the lemma this
gives
log
q
1
2 An2+Bn+C
(q)n

= L(1) −L(Q)
ε
−1
2 log 2π
ε
+ log
QB
√1 −Q
−

∆
1 −Q
ν2
2 −

B + 1
2
Q
1 −Q

ν + 1
24
1 + Q
1 −Q

ε −
∞

r=3
Br(ν) Li2−r(Q) εr−1
r!
54
Don Zagier
with ∆= A + Q −AQ as before. If we write this as log ϕ(ν) where ϕ is
a smooth function of rapid decay, then FA,B(q) equals 
ν≡ν0 (mod 1) ϕ(ν),
which by the Poisson summation formula can be written as 
r∈Z ϕ(r)e2πirν0
where ϕ is the Fourier transform of ϕ. The smoothness of ϕ implies that all
terms except r = 0 give contributions which are O(εN) for all N > 0 as
ε →0. We therefore obtain the asymptotic expansion
FA,B

e−ε
= QB
√
∆
· exp
L(1) −L(Q)
ε
−1 + Q
1 −Q
ε
24

· I

exp

B + 1
2
Q
1 −Q

uε −
∞

r=3
Br(u) Li2−r(Q) εr−1
r!
1 −Q
∆ε

,
where I

 
is the functional deﬁned formally by the integral transform
I

H(u)


t

=
1
√
2πt
 ∞
−∞
e−u2/2t H(u) du ,
(39)
and explicitly at the level of power series by
I
 ∞

n=0
cn un

t

∼
∞

n=0
(2n −1)!! c2n tn ,
(40)
where (2n−1)!! = (2n)!/2nn! as usual. It is not immediately obvious why this
expansion makes sense, since the argument of the functional grows like 1/ε as
ε →0, but the power series to which it is applied has the property that the
coeﬃcient of un is O(ε2n/3) for every n ≥0, and since the functional I

 
has
the scaling property I

H(λu)

(t) = I

H(u)

(λ2t), the ﬁnal expression does
indeed involve only positive powers of ε. (Choose λ = εc with 1
2 < c < 2
3.)
(c) The third method, which is based on a clever application of Cauchy’s
theorem going back originally to an old paper of Meinardus [26], was ﬁrst
used in this context by Nahm, Recknagel and Terhoeven [31] and is also the
one used in Nahm’s paper [30] in this volume, so that we will only indicate
the main idea of the method here. We write Fa,b(q) as
FA,B(q) = Cx0

∞

n=−∞
q
1
2 An2+Bn x−n
  ∞

n=0
1
(q)n
xn

where Cx0[ · ] denotes the constant term of a Laurent series. The ﬁrst factor is
a theta series with a well-understood asymptotic behavior as q →1 and the
second equals (x; q)−1
∞by equation (8) and hence also has known asymptotics.
Speciﬁcally, the Poisson summation formula (or the Jacobi transformation
formula for theta series) shows that
θA,B(z, u) :=
∞

n=−∞
q
1
2 An2+Bn x−n =
 
i
Az
∞

n=−∞
e

−(u −Bz + n)2
2Az

,
The Dilogarithm Function
55
where q = e(z) := e2πiz, x = e(u). Hence we ﬁnd, for any u0 ∈C,
FA,B(q) =
 u0+1
u0
θA,B(z, u)

e(u); q
−1
∞du
=
 
i
Az

ℑ(u)=ℑ(u0)
e

−(u −Bz)2
2Az
 
e(u); q
−1
∞du
=
1
√
2πAε

ℑ(t)=const
exp

−t2
2Aε + Li2(qBeit; q)

dt .
where in the last line we have substituted u = Bz +t/2π. The derivative with
respect to t of the argument of exp equals [A log(1 −eit) −it]/iAε + O(1),
which vanishes at it = log(1 −Q) + O(ε), where Q is the solution between 0
and 1 (or, of course, any other solution) of Nahm’s equation 1−Q = QA. Now
moving the path of integration to a neighbourhood of this point and applying
the method of stationary phase (saddle point method), we obtain the desired
asymptotic expansion for FA,B

e−ε
. This method has the further advantage,
as explained in Nahm’s paper, that the contributions from the further saddle
points could in principle be used to describe all the terms of the q-expansion
of fA,B,C(−1/z) in the cases when fA,B,C is a modular function.
As already mentioned, one can also do an almost exactly similar calculation
using the power series expansion (7) rather than (8), at least if A > 1: we now
write
FA,B(q) = Cx0

∞

n=−∞
(−1)n q
A−1
2
n2+(B+ 1
2 )n x−n
  ∞

n=0
(−1)n q
n2−n
2
(q)n
xn

=
 u0+1
u0
!
i
(A −1)z

n∈Z
e
(u −(B + 1
2)z + n + 1
2)2
2(A −1)z
 
e(u); q

∞du
=
1

2π(A −1)ε

ℑ(t)=const
exp

−
t2
2(A −1)ε −Li2(−qB+ 1
2 eit; q)

dt ,
and again an asymptotic expansion could now be obtained by the saddle point
method. I have not carried out the details.
This completes our discussion and proof of Proposition 5. We remark that
each of the methods described applies also to r > 1, and we again ﬁnd an
expansion of log FA,B(q) of the form (35), with leading coeﬃcient given by
c−1(A, B) =
r

i=1

L(1) −L(Qi)

= rL(1) −L(ξA) = c(A)L(1) .
In particular, the modularity of fA,B,C(z) for any B ∈Qr and C ∈Q requires
that L(ξA) be a rational multiple of π2 and hence suggests very strongly that
ξA has to be a torsion element of B(Q(ξA)), as required by Nahm’s conjecture.
56
Don Zagier
The higher coeﬃcients are given by a formula essentially the same as in the
case r = 1, except that the previous expression of the form I

H(u)

 1−Q
∆ε

with I

 
deﬁned by equation (30) or (31) must now be replaced by its multi -
dimensional generalization

det A
(2π)r/2

Rr exp

−ε
2u Aut
H(u) du
∼
∞

n=0
(2ε)−n
n!
∆n

AH(0),
where A is given by (30) and ∆
A denotes the Laplacian with respect to the
quadratic form u Aut.
We now use the proposition to classify the modular fA,B,C when r = 1.
Theorem. The only (A, B, C) ∈Q+×Q×Q for which fA,B,C(z) is a modular
form are those given in Table 1.
The basic idea of the proof is that, if f(z) = F(q) is a modular form
of weight k on some group Γ, then the function g(z) = z−kf(−1/z) is also
a modular form (on the group SΓS, where S =
 0 −1
1
0

) and hence has an
expansion as z →0 of the form a0qn0 +a1qn1 +· · · for some rational exponents
n0 < n1 < · · · and non-zero algebraic coeﬃcients a0, a1, . . . . In particular
we have F

e−ε
= f(iε/2π) = (2πi/ε)k a0 e−4π2n0/ε + O

ε−ke−4π2n1/ε
and
hence log F

e−ε
= −4π2n0ε−1 −k log ε + c + O(εN) for all N > 0 as ε
tends to 0, where c = log((2πi)ka0). Comparing this with the expansion of
log FA,B,C

e−ε
= log FA,B

e−ε
−Cε as given in equation (35), we see that
if fA,B,C(z) is a modular form of weight k then
(i)
the weight k must be 0 (i.e. fA,B,C(z) must be a modular function);
(ii) the number c−1(A, B) must be π2 times a rational number;
(iii) the number c0(A, B) must be the logarithm of an algebraic number;
(iv) the number c1(A, B) must be a rational number (namely, C); and
(v)
the numbers cj(A, B) must vanish for all j ≥2.
The conditions (ii)–(iv) are useless for numerical work, since the rationals lie
dense in R, but condition (v) gives inﬁnitely many constraints on the two real
numbers A and B and can be used to determine their possible values. This
approach was already used by Terhoeven in 1994 to prove a weaker version
of the theorem, namely, that the only values of A ∈Q+ for which fA,0,C is
modular for some C ∈Q are 1/2, 1 and 2. (See [36], where, however, the details
of the calculation are not given.) To do this, Terhoeven computed cj(A, B) up
to j = 2 using the method (c) above, as developed in his earlier joint paper [31].
If fA,0,C is to be modular for some C, then the number c2(A, 0) must vanish.
We have c2(A, 0) = P(A, Q)/(A+Q−AQ)6 for a certain polynomial P(A, Q)
with rational coeﬃcients (given after Proposition 5), where Q is the root
of Q + QA = 1 in (0,1). By looking at the graph of the function Φ(Q) =
P
 log(1−Q)
log Q) , Q) on the interval (0,1), we ﬁnd numerically that it has a simple
zero at Q1 = (3 −
√
5)/2, a double zero at Q2 = 1/2, a simple zero at Q3 =
The Dilogarithm Function
57
(
√
5 −1)/2, and no other zeros. Since P(Q1, 1
2) = P(Q2, 1) = P(Q3, 2) = 0
and since Φ(Q) = Φ(1−Q), we know that there really are zeros of the speciﬁed
multiplicities at Q1, Q2 and Q3. It follows that they are the only zeros in this
interval and hence that fA,0,C can only be modular for the three values given
in Table 1.
To prove the full theorem we proceed in the same way, but since we now
have two variables A and B to determine we must use at least two coeﬃcients
cj(A, B). The functions c2(A, B) and c3(A, B) are polynomials in B of degree 3
and 4, respectively, whose coeﬃcients are known elements of Q(A, Q). For ﬁxed
A ∈R+ the condition that the two polynomials c2(A, · ) and c3(A, · ) have a
common zero is that their resultant vanishes. From the explicit formulas for c2
and c3 we ﬁnd that this resultant has the form R(A, Q)/(A+Q−AQ)39 where
R(A, Q) is a (very complicated) polynomial in A and Q with rational coeﬃ-
cients. Now a graphical representation of the function Ψ(Q) = R
 log(1−Q)
log Q) , Q)
on the interval (0,1) (which we can unfortunately not show here since this
function varies by many orders of magnitude in this range and hence has to
be looked at at several diﬀerent scales on appropriate subintervals) shows that
it has nine zeros (counting multiplicities), namely:
a simple zero at Q0 = 0.196003534545184447085746160093577 · · ·
a double zero at Q1 = 0.3819660 · · · = (3 −
√
5)/2
a triple zero at Q2 = 0.5000000 · · · = 1/2
a double zero at Q3 = 0.6180339 · · · = (
√
5 −1)/2
a simple zero at Q4 = 0.803996465454815552914253 · · · = 1 −Q0
and no other zeros. Since Ψ(1−Q) = −Ψ(Q) and since we know from Table 1
that Ψ(Q) has to have at least a double zero at Q = Q1 and at Q = Q3
and a triple one at Q = Q2, we deduce that the numerically found zeros at
these places are really there and correspond to the known cases of modularity.
As to the new value Q0 and Q4 = 1 −Q0 and the corresponding A-values
A0 = 0.133871736816761609695060406707385 · · · and A4 = A−1
0 , we ﬁnd that
indeed c2(A0, B) and c3(A0, B) have a (simple) common root at B = B0 =
−0.397053221675466369 . . . , as they must since their resultant vanishes. But
for the pair (A0, B0) we ﬁnd numerically
c−1(A0, B0)/π2 = 0.1277279468293881629887898 · · ·
which is (apparently) not a rational number,
exp(c0(A0, B0)) = 3.4660299497719132664077586 · · ·
which is (apparently) not algebraic,
c1(A0, B0) = 0.4917635587907976876492549 · · ·
which is (apparently) not rational, and ﬁnally
c4(A0, B0) = 0.0175273497972616555765902 · · ·
which is (deﬁnitely) not zero. It follows that the function fA0,B0,c1(A0,B0)(z)
is not modular and thus that the list given in Table 1 is complete.
□
This analysis was quite tedious and would become prohibitively so for
r ≥2 (although the method applies in principle) because we would need
58
Don Zagier
explicit formulas for many more of the coeﬃcients cj(A, B). An alternative
approach might be to reﬁne Proposition 5 by showing that
log FA,B

ζ e−ε
∼
∞

j=−1
cj,ζ(A, B) εj

ε ↘0

for every root of unity ζ. If fA,B,C(z) is modular for some C ∈Q, then the
logarithm of FA,B,C

ζ e−ε
= ζCe−CεFA,B

ζ e−ε
has vanishing coeﬃcient
of εj in its expansion at ε = 0 for every j ≥1. In particular we must have
c1,ζ(A, B) = C for all roots of unity ζ with the same constant C, so we get
inﬁnitely many constraints on A and B without having to calculate any of the
Taylor expansions further than their O(ε) term. I have not yet tried to carry
this out, but it seems to hold out good prospects for an easier proof of the
r = 1 case and perhaps a reasonable attack on the higher rank cases of the
conjecture as well.
Finally, we remark that Proposition 5 (or its generalization to r > 1) can
be used to search eﬃciently for values of B for a given A for which fA,B,C may
be modular for some C. Indeed, since the function φ(ε) = log(FA,B(e−ε) must
have a terminating asymptotic expansion of the form c−1ε−1+c0+c1ε with an
error term that is exponentially small in 1/ε, we can simply check whether four
successive values of nφ(α/n) (say, those with α = 1 and n = 20, 21, 22, 23) are
approximated to high precision by a quadratic polynomial in n (i.e., whether
the third diﬀerence of this 4-tuple is extremely small). In fact, since we know
c−1 by (30), we can look instead at three sucessive values of nφ(α/n)−c−1n2/α
and check whether they lie on a line (i.e., whether their second diﬀerence
vanishes) to high precision. This can be done very rapidly and therefore we
can search through a large collection of candidate vectors B ∈Qr for those
which can correspond to some modular fA,B,C. This is the method which was
used to ﬁnd the modular solutions for r = 2 amd 3 given in (d) and (e) of
subsection B.
