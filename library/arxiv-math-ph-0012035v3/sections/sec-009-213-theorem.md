---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-009-213-theorem
section_title: "Theorem"
section_number: 2.1.3
pages: 11-16
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
The non-Abelian Stokes theorem in its original operator form rough ly claims
that the holonomy round a closed curve C = ∂S equals a surface-ordered expo-
nent of the twisted curvature, namely
P exp
(
i
∮
C
A
)
= P exp
(
i
∫
S
F
)
, (14)
11
✲
✻
✛
❄
(0,0)
(0,1) (1,1)
(1,0)
Figure 6: The parametrized loop C as a boundary of the “big” square S with
the coordinates {(0, 0), (1, 0), (1, 1), (0, 1)}.
where F is the twisted curvature
F ≡ U −1F U.
A more precise form of the non-Abelian Stokes theorem as well as an exact
meaning of the notions appearing in the theorem will be given in the cou rse of
the proof.
Proof Following [Are80] and [Men83] we will present a short, direct proof of
the non-Abelian Stokes theorem.
In our parametrization, the ﬁrst step consists of the decomposit ion of the
initial loop (see, Fig.6) into small lassos according to the rules given in t he
section 2.1.1
P exp
(
i
∮
C
A
)
= lim
N →∞
(Ps,t)
N∏
m,n=1
U −1
m,nWm,nUm,n,
where the objects involved are deﬁned as follows: parallel-transpo rt operators
from the reference point (0 , 0) to the point with coordinates ( m
N , n
N ) consists of
12
✻
✲
Figure 7: Approaching the “small” plaquette inside the “big” square.
two segments (see, Fig.7)
Um,n
def
= P exp
(
i
∫ ( m
N , n
N )
(0, n
N )
A
)
P exp
(
i
∫ (0, n
N )
(0,0)
A
)
,
parallel-transport operator round a small plaquette Sm,n
Wm,n
def
= Tr P exp
(
i
∮
Sm,n
A
)
,
where Sm,n is a boundary of a (small) square with coordinates
Sm,n :
{(m
N , n
N
)
,
(m − 1
N , n
N
)
,
(m − 1
N , n − 1
N
)
,
(m
N , n − 1
N
)}
.
Now
U −1
m,nWm,nUm,n = U −1
m,n
[
1 + i
N 2 Fm,n + O
( 1
N 3
)]
Um,n
= 1 + i
N 2 U −1
m,nFm,nUm,n + O
( 1
N 3
)
= 1 + i
N 2 Fm,n + O
( 1
N 3
)
= Wm,n + O
( 1
N 3
)
,
where Wm,n has been calculated in the Appendix to this section (see, Eq.15),
Fm,n
def
= U −1
m,nFm,nUm,n,
13
✲
✻
✛
❄
... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ...... . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..
Figure 8: The small plaquette.
and
Wm,n
def
= exp
( i
N 2 Fm,n
)
.
Then
P exp
(
i
∮
C
A
)
= lim
N →∞
(Ps,t)
N∏
m,n=1
[
Wm,n + O
( 1
N 3
)]
= lim
N →∞
(Ps,t)
N∏
m,n=1
exp
[ i
N 2 Fm,n + O
( 1
N 3
)]
= lim
N →∞
(Pt)
N∏
m,n=1
exp
[ i
N 2 Fm,n + O
( 1
N 3
)]
.
The last equality follows from the fact that operations correspond ing to the
change of the order of the operators yield the commutator
[ 1
N 2 Fm′,n′, 1
N 2 Fm′′,n′′
]
= O
( 1
N 4
)
,
and there is maximum N − 1 transpositions possible in the framework of s-
ordering, so
(N − 1) O
( 1
N 4
)
= O
( 1
N 3
)
.
14
Thus, we arive at the ﬁnal form of the non-Abelian Stokes theorem ,
P exp
(
i
∮
C
A
)
= lim
N →∞
(Pt)
N∏
m,n=1
exp
[ i
N 2 Fm,n
]
= P exp
(
i
∫
S
F
)
.
Appendix In this paragraph we will perform a fairly standard calculus and
derive the contribution coming from a small loop Wm,n. Namely,
Wm,n = P exp
(
i
∫ ( m
N , n
N )
( m
N , n−1
N )
A
)
P exp
(
i
∫ ( m
N , n−1
N )
( m−1
N , n−1
N )
A
)
P exp
(
i
∫ ( m−1
N , n−1
N )
( m
N , n−1
N )
A
)
P exp
(
i
∫ ( m
N , n−1
N )
( m
N , n
N )
A
)
=
[
1 + i
N Ay
m,n + 1
2
( i
N Ay
m,n
)2
+ O
( 1
N 3
)]
·
[
1 + i
N Ax
m,n−1 + 1
2
( i
N Ax
m,n−1
)2
+ O
( 1
N 3
)]
·
[
1 − i
N Ay
m−1,n + 1
2
( i
N Ay
m−1,n
)2
+ O
( 1
N 3
)]
·
[
1 − i
N Ax
m,n + 1
2
( i
N Ax
m,n
)2
+ O
( 1
N 3
)]
= 1 + i
N
(
Ay
m,n − Ay
m−1,n
)
− i
N
(
Ax
m,n − Ax
m,n−1
)
+
( i
N
)2(
Ay
m,n
)2
+
( i
N
)2(
Ax
m,n
)2
+
( i
N
)2
Ay
m,nAx
m,n
−
( i
N
)2(
Ay
m,n
)2
−
( i
N
)2
Ay
m,nAx
m,n −
( i
N
)2
Ax
m,nAy
m,n
−
( i
N
)2(
Ax
m,n
)2
+
(
− i
N
)2
Ay
m,nAx
m,n + O
( 1
N 3
)
= 1 + i
N 2 (∂xAy − ∂yAx) − i2
N 2 (AxAy − AyAx) + O
( 1
N 3
)
= 1 + i
N 2 Fm,n + O
( 1
N 3
)
, (15)
where
F = ∂xAy − ∂yAx − i [Ax, Ay]
(ocassionally, we put x and y in the upper position), and
A = Am,n + O
( 1
N
)
.
15
Then
Wm,n = exp
[ i
N 2 Fm,n + O
( 1
N 3
)]
.
Other approaches There is a lot of other approaches to the (operator) non-
Abelian Stokes theorem, more or less interrelated. The analytic app roach ad-
vocated in [Bra80] and [HM98]. The approach using the, so-called, pr oduct
integration [KMR99] and [KMR00]. And last, but not least, a (very interesting)
coordinate-gauge approach [SS98], and [Hal79] as well as its lattice f ormulation
[Bat82].
