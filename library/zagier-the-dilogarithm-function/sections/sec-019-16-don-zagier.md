---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-019-16-don-zagier
section_title: "Don Zagier"
section_number: 16
pages: 14-16
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
We give an example of a non-trivial element of the Bloch group. For con-
venience, setα = 1−√−7
2 , β =−1−√−7
2 . Then
2 ·
(1+ √−7
2
)
∧
(1−√−7
2
)
+
(−1+ √−7
4
)
∧
(5−√−7
4
)
=2 · (−β)∧α +
( 1
β
)
∧
(α2
β
)
=β2∧α−β∧α2 =2 ·β∧α− 2·β∧α =0 ,
so
2
[ 1+ √−7
2
]
+
[−1+ √−7
4
]
∈ BC. (13)
This example should make it clear why non-trivial elements of BC can only
arise from algebraic numbers: the key relations 1+β =α and 1−β−1 =α2/β
in the calculation above forcedα and β to be algebraic.
5 ... and values of Dedekind zeta functions
Let F be an algebraic number ﬁeld, say of degreeN over Q. Among its most
important invariants are the discriminantd, the numbersr1 andr2 of real and
imaginary archimedean valuations, and the Dedekind zeta-functionζF (s). For
the non-number-theorist we recall the (approximate) deﬁnitions. The ﬁeld
F can be represented as Q(α) where α is a root of an irreducible monic
polynomial f∈ Z[x] of degree N. The discriminant of f is an integer df and
d is given byc−2df for some natural numberc withc2|df . The polynomialf,
which is irreducible overQ, in general becomes reducible overR, where it splits
intor1 linear and r2 quadratic factors (thusr1 ≥ 0, r2 ≥ 0, r1 +2r2 =N). It
also in general becomes reducible when it is reduced modulo a prime p, but
if p ∤df then its irreducible factors modulo p are all distinct, say r1,p linear
factors, r2,p quadratic ones, etc. (so r1,p +2r2,p +··· = N). Then ζF (s)i s
the Dirichlet series given by an Euler product∏
pZp(p−s)−1 where Zp(t)f o r
p ∤df is the monic polynomial (1−t)r1,p (1−t2)r2,p ··· of degreeN andZp(t)
forp|df is a certain monic polynomial of degree≤N.T h u s(r1,r2)a n dζF (s)
encode the information about the behaviour off (and henceF)o v e rt h er e a l
and p-adic numbers, respectively.
As an example, letF be an imaginary quadratic ﬁeld Q(√−a) witha≥ 1
squarefree. Here N =2 , d = −a or −4a, r1 =0 , r2 = 1. The Dedekind
zeta function has the form∑
n≥1r(n)n−s where r(n) counts representations
of n by certain quadratic forms of discriminant d; it can also be represented
as the product of the Riemann zeta function ζ(s)=ζ Q(s) with an L-series
L(s)= ∑
n≥1
(d
n
)
n−s where
(d
n
)
is a symbol taking the values ±1o r0a n d
which is periodic of period|d| in n.T h u sf o ra =7
The Dilogarithm Function 17
ζQ(√−7)(s)= 1
2
∑
(x,y)⁄=(0,0)
1
(x2 +xy +2y2)s
=
( ∞∑
n=1
n−s
)( ∞∑
n=1
(−7
n
)
n−s
)
where
(−7
n
)
is +1 forn≡ 1, 2, 4 (mod 7), −1f o rn≡ 3, 5, 6 (mod 7), and 0
for n≡ 0 (mod 7).
One of the questions of interest is the evaluation of the Dedekind zeta
function at suitable integer arguments. For the Riemann zeta function we have
the special values cited at the beginning of this paper. More generally, ifF is
totally real (i.e.,r1 =N,r2 = 0), then a theorem of Siegel and Klingen implies
that ζF (m)f o rm =2 ,4,... equals πmN/
√
|d| times a rational number. If
r2 > 0, then no such simple result holds. However, in the caseF = Q(√−a),
by using the representation ζF (s)= ζ(s)L(s) and the formula ζ(2) = π2/6
and writing the periodic function
(d
n
)
as a ﬁnite linear combination of terms
e2πikn/|d| we obtain
ζF (2) = π2
6
√
|d|
|d|−1∑
n=1
(d
n
)
D(e2πin/|d|)( F imaginary quadratic),
e.g.,
ζQ(√−7)(2) = π2
3
√
7
(
D
(
e2πi/7)
+D
(
e4πi/7)
−D
(
e6πi/7))
.
Thus the values of ζF (2) for imaginary quadratic ﬁelds can be expressed in
closed form in terms of values of the Bloch-Wigner functionD(z) at algebraic
argumentsz.
By using the ideas of the last section we can prove a much stronger state-
ment. Let O denote the ring of integers ofF (this is theZ-lattice in C spanned
by 1 and√−a or (1+√−a)/2, depending whetherd =−4a ord =−a). Then
the group Γ = SL2(O) is a discrete subgroup of SL2(C) and therefore acts
on hyperbolic space H3 by isometries. A classical result of Humbert gives the
volume of the quotient space H3/Γ as|d|3/2 ζF (2)/4π2. On the other hand,
H3/Γ (or, more precisely, a certain covering of it of low degree) can be trian-
gulated into ideal tetrahedra with vertices belonging to P1(F)⊂ P1(C), and
this leads to a representation
ζF (2) = π2
3|d|3/2
∑
ν
nν D(zν)
withnν in Z andzν inF itself rather than in the much larger ﬁeldQ(e2πin/|d|)
([8], Theorem 3). For instance, in our exampleF = Q(√−7) we ﬁnd
ζF (2) = 4π2
21
√
7
(
2D
(1+ √−7
2
)
+D
(−1+ √−7
4
))
.
