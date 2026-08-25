---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-041-3-dilogarithms-and-modular-functions
section_title: "Dilogarithms and modular functions"
section_number: 3
pages: 39-43
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
A fascinating and almost completely unsolved problem is to understand
the overlap between the classes of q-hypergeometric functions and modular
forms or functions, the prototypical case being given by the famous Rogers -
Ramanujan identities. Nahm’s conjecture gives us a ﬁrst glimpse of an an-
swer, which surprisingly involves dilogarithms and the Bloch group. In sub-
sections A and B we describe the conjecture and some of the examples which
motivate it, while subsection C contains an asymptotic analysis of the q-series
involved and the proof that the conjecture is true in the simplest c ase.
A. q-hypergeometric series and Nahm’s conjecture. Consider the two
power series G(q)a n d H(q)b y
G(q)=
∞∑
n=0
qn2
(q)n
,H (q)=
∞∑
n=0
qn2+n
(q)n
(|q| < 1),
where (q)n as in §1 denotes the product (1 −q)(1−q2) ··· (1−qn). The classical
Rogers-Ramanujan identities—discovered by Rogers in 1897, rediscovere d by
Ramanujan in 1915 and then given a third proof by both authors jointly
and many further proofs in subsequent years—says that these two ser ies have
product developments
G(q)=
∏
n ≡± 1( m o d5 )
1
1 − qn ,H (q)=
∏
n≡± 2( m o d5 )
1
1 − qn .
The important thing here is not so much that these functions have pr oduct ex-
pansions as that, up to rational powers of q, they are both modular functions.
Indeed, by the Jacobi triple product formula, we can rewrite the id entities as
G(q)= 1
(q)∞
∑
n∈Z
(−1)n q(5n2+n)/2,H (q)= 1
(q)∞
∑
n∈Z
(−1)n q(5n2+3n)/2
or, even more intelligently, as
q−1/60 G(q)= θ5,1(z)
η(z) ,q 11/60 H(q)= θ5,2(z)
η(z) , (23)
42 Don Zagier
where q = e2πiz with z ∈ H (upper half-plane) and
η(z)= q1/24
∞∏
n=1
(1 − qn),θ 5,j(z)=
∑
n ≡ 2j−1 (mod 10)
(−1)[n/10] qn2/40 .
The point is that η(z), θ5,1(z)a n d θ5,2(z) are all modular forms of weight 1/2
and therefore that the functions on the right-hand side of (23) are modular
functions, i.e., they are invariant under z ↦→az+b
cz+d for all
( ab
cd
)
belonging to
some subgroup of ﬁnite index of SL(2, Z). Indeed, if we combine them into a
single vector-valued function
g(z)=
(
q−1/60G(q)
q11/60H(q)
) (
z ∈ H,q α := e2πiαz)
,
then we have transformation formulas with respect to the full modul ar group:
g(z +1 )=
( ζ −1
60 0
0 ζ 11
60
)
g(z),g
(
− 1
z
)
= 2√
5
( sin 2π
5 sin π
5
sin π
5 − sin 2π
5
)
g(z) (24)
(with ζN := e2πi/ N) and hence g(γ(z)) = ρ(γ)g(z) for all γ ∈ SL(2, Z)a n d
some representation ρ : SL(2, Z) → GL(2, C).
The functions G(q)a n d H(q) are special examples of what are called q-
hypergeometric series, i.e., series of the form ∑ ∞
n=0 An(q) where A0(q)i sa
rational function and An(q)= R(q, qn)An−1(q) for all n ≥ 1 for some rational
function R(x, y) with lim
x→0
lim
y→0
R(x, y) = 0. (For G and H one has A0 =1
and R(x, y)= x−1y2/(1 − y)o r y2/(1 − y), respectively.) There are only a
handful of examples known of q-hypergeometric series which are also modular,
and, as already mentioned in the introduction to this section, the pr oblem
of describing when this happens in general is an important and fascinati ng
question, but totally out of reach for the moment. A remarkable conjectur e
of Werner Nahm, discussed in more detail in his paper [30] in this volume as
well as in his earlier articles [28], [29], relates the answer to this qu estion in
a very special case to dilogarithms and Bloch groups on the one hand and to
rational conformal ﬁeld theory on the other.
Nahm’s conjecture actually concerns certain r-fold hypergeometric series
(deﬁned as above but with n running over ( Z≥0)r rather than just Z≥0). Let
A be a positive deﬁnite symmetric r × r matrix, B a vector of length r,a n d
C a scalar, all three with rational coeﬃcients. We deﬁne a function fA,B,C (z)
by the r-fold q-hypergeometric series
fA,B,C (z)=
∑
n=(n1,...,nr) ∈ (Z≥0)r
q
1
2 ntAn+Btn+C
(q)n1 ··· (q)nr
(z ∈ H)
and ask when fA,B,C is a modular function. Nahm’s conjecture does not an-
swer this question completely, but predicts which A can occur. If A =( aij)
The Dilogarithm Function 43
is any positive deﬁnite symmetric r × r matrix with rational entries, we can
consider the system
1 − Qi =
r∏
j=1
Qaij
j (i =1 ,...,r ) (25)
of r equations in r unknowns, which we can write in abbreviated notation as
1 − Q = QA, Q =( Q1,...,Q r). We suppose ﬁrst that A has integral coeﬃ-
cients, so that the equations in (25) are polynomial. Since there are as man y
equations as unknowns, we expect that the solutions form a 0-dimension al
variety, i.e., there are only ﬁnitely many solutions and (hence) all l ie in Q, but
in any case, the system certainly has solutions in Q
r
. For any such a solution
Q =( Q1,...,Q r) we can consider the element
ξQ =[ Q1]+ ··· +[ Qr] ∈ Z[F ] ,
where F is the number ﬁeld Q(Q1,...,Q r). Then in Λ2(F ×) we ﬁnd
∂
(
ξQ
)
=
r∑
i=1
(Qi) ∧ (1 − Qi)=
r∑
i=1
(Qi) ∧
( r∏
j=1
Qaij
j
)
=
r∑
i=1
(Qi) ∧
( r∑
j=1
aij(Qj)
)
=
r∑
i=1
r∑
j=1
aij (Qi) ∧ (Qj) ,
and this is 0 since aij is symmetric and ( Qi) ∧ (Qj) antisymmetric in i and j.
Hence ξA belongs to the Bloch group of F .I f A is not integral, then we
have to be careful about the choice of determinations of the rational powe rs
Qaij
j in (25). We require them to be consistent, i.e., we must have Qi = eui ,
1 − Qi = evi for some vectors u, v ∈ Cr such that v = Au. This deﬁnes the
minimal number ﬁeld F in which the equations (25) make sense. For instance,
if A =
( 8/31 /3
1/32 /3
)
, we set ( Q1,Q 2)=( α, αβ3) where α, β ∈ Q are solutions of
the system 1−α = α3β,1 −αβ3 = αβ2; then F = Q(α, β), and ξQ =[ α]+[αβ3]
is an element of B(F ). Nahm’s conjecture is then
Conjecture. Let A be a positive deﬁnite symmetric r×r matrix with rational
coeﬃcients. Then the following are equivalent:
(i) The element ξQ is a torsion element of B(F ) for every solution Q of (25).
(ii) There exist B ∈ Qr and C ∈ Q such that fA,B,C (z) is a modular function.
The main motivation for this conjecture comes from physics, and in fact on e
expects that all the modular functions fA,B,C which are obtained this way
are characters of rational conformal ﬁeld theories. (We will not discuss t hese
aspects at all, referring the reader for this to Nahm’s paper.) A furth er ex-
pectation, again predicted by the physics, is that if a matrix A satisﬁes the
conditions of the conjecture, then the collection of modular function s occur-
ring in statement (ii) span a vector space which is invariant under t he action of
44 Don Zagier
SL(2, Z) (bosonic case) or at least Γ (2) (fermionic case), even though the indi-
vidual functions fA,B,C will in general have level greater than 2. For instance,
in the Rogers-Ramanujan identities given above, each of the two functi ons
(23) is modular (up to multiplication by a root of unity) only on the modu lar
group Γ0(5) of level 5 (and on a yet much smaller group if we do not allow
scalar multiples), but the vector space which they span is invariant under all
of SL(2, Z) by eq. (24). From a purely mathematical point of view, the mo-
tivation for the conjecture comes from the asymptotic analysis, discus sed in
subsection B, and from the known examples, some of which we now describe.
B. Examples and discussion. In this subsection we describe a number of
examples which give numerical support for Nahm’s conjecture and which show
that two plausible alternative versions of the conjecture—one with a s tronger
and one with a weaker hypothesis on the matrix A —are not tenable.
(a) Rank one examples. If r = 1, then the parameters A, B and C are
simply rational numbers and exactly seven cases are known where fA,B,C (z)
is a modular function, given by the following table:
T able 1. The modular functions fA,B,C for r =1
AB C fA,B,C (z)
20 −1/60 θ 5,1(z)/η (z)
11 1 /60 θ 5,2(z)/η (z)
10 −1/48 η (z)2/η (z/2)η (2z)
1/21 /24 η (2z)/η (z)
−1/21 /24 2η (2z)/η (z)
1/20 −1/40 θ 5,1(z/4)/θ 8(z)
1/21 /40 θ 5,2(z/4)/θ 8(z)
with θ5,j(z)a n dη(z) as in (23) and θ8(z)= ∑
n>0
( 8
n
)
qn2/8 = η(z)η(4z)/η(2z).
The ﬁrst two entries in this table are just the Rogers-Ramanujan iden tities
with which we began the discussion, and the product η(z)fA,B,C (z) in all
seven cases is a unary theta series (i.e., a function ∑ ε(n)qλn2
with ε(n)a n
even periodic function and λ a positive rational number). We will see in sub-
section B that these are the only triples ( A, B, C) ∈ Q+ ×Q2 for which fA,B,C
is modular. On the other hand, the element ξA when r = 1 consists of a single
element [Q1], where 1 − Q1 = QA
1 , so by the discussion in example (c) of §2B
we know that the only values of A> 0 for which condition (i) of the conjecture
is satisﬁed are A =1 /2, 1 or 2 (corresponding to Q1 =( −1+
√
5)/2, 1 /2a n d
(3 −
√
5)/2, respectively). Thus Nahm’s conjecture holds for r =1 .
(b) Totally real, or torsion in the Bloch group? In the above examples,
the element Q1 was a totally real algebraic number. It is reasonable to ask
whether the requirement for modularity is really condition (i) of t he conjecture
or merely the more elementary (but stronger) condition that equation (25) has
The Dilogarithm Function 45
only real solutions. To see that (i) really is the right condition, we con sider the
matrix A =
( 41
11
)
. In this case (25) specializes to the system of equations (19)
studied in example (b) of §2B, and by the discussion given there we know
that the corresponding element ξA ∈ B(Q(ξA)) is torsion (of order 10) but is
not totally real. So if (i) rather than total reality is the correct condit ion in
the conjecture, then there should be pairs ( B, C) ∈ Q2 × Q for which fA,B,C is
modular. After some experimentation, using a method which will be explained
brieﬂy at the end of subsection C, we ﬁnd that there are indeed at least two
such pairs, the corresponding identities being
f( 41
11 ), ( 0
1/2 ), 1
120
(z)= θ5,1(2z)
η(z) ,f ( 41
11 ), ( 2
1/2 ), 49
120
(z)= θ5,2(2z)
η(z) ,
where θ5,1(z)a n d θ5,2(z) are the same theta series as those occurring in (23).
(These equations were not proved, but only veriﬁed to a high order in the
power series in q.)
(c) Must all solutions be torsion? If A is any positive deﬁnite matrix,
even with real coeﬃcients, then the system of equations (25) has exact ly one
solution with all Qi real and between 0 and 1. (To see this, one shows by
induction on r the more general assertion that the system 1 − Qi = λi
∏
j Qaij
j
has a unique solution in (0 , 1)r for any real numbers λ1,...,λ r > 0.) Denote
this solution by Q0 =( Q0
1,...,Q 0
r). If the coeﬃcients of A are rational, the
Q0
i are real algebraic numbers (though not necessarily totally real—see (b))
and we obtain a speciﬁc element ξA = ξQ0 ∈ B(
Q ∩ R). If condition (i) of
the conjecture is satisﬁed, then this must be a torsion element and hence
the corresponding Rogers dilogarithm value L(ξA)= ∑ L(Q0
i )m u s tb ea
rational multiple of π2. This criterion is numerically eﬀective (one can ﬁnd Q0
numerically to high precision by an iterative procedure and then te st L(ξA)/π2
for rationality) and is the one used for the computer searches describe d in (d)
and (e) below. One can reasonably ask whether it is in fact suﬃcient, i .e.,
whether it is suﬃcient in (i) to assume only that ξA is torsion. An example
showing that this is not the case—we will see many others in (d) and (e) —is
given by the matrix A =( 8
5
5
4 ). Here Q0 is equal to
(
φ−1 ψ, φ 4 − φ3ψ
)
, with
φ =(
√
5+1 ) /2a n d ψ =( 1 +
√
2
√
5 − 1)/2, and this is torsion, as we can
see numerically from the dilogarithm values ( L(ξ)= 8
