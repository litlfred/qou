---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-009-2-z-we-deﬁne
section_title: "Z we deﬁne"
section_number: 2
pages: 3-5
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
---
Y (0)
(I,J,K ) =
{
1 if I +J −K, J+K −I, K+I −J ∈ Z+
0 otherwise (2)
Y (1)
(I,m) =
{ 1 if I +m, I−m ∈ Z+
0 otherwise. (3)
3
Let us now recall some properties about braiding matrices, 3 j and 6j symbols of the ﬁnite
dimensional representations of Uq(su(2)). We will always refer to conventions as well as explicit
expressions given in [1], see also [15, 16, 17]. The group-like element
K
µ, the square root of
the ribbon element v1/2
K , the quantum Weyl element
K
w, the braiding matrices
I J
R(±), and the
Clebsch-Gordan coeﬃcients satisfy the following relations:
∑
m,n
(
r
L
I J
m n
)(
m n
I J
K
p
)
=Y (0)
(I,J,K )δK,Lδr
pY (1)
(K,p),
∑
K,p
(
m n
I J
K
p
)(
p
K
I J
i j
)
=δm
i δn
jY (1)
(I,m)Y (1)
(J,n), (4)
∑
k,l
( p
K
I J
k l
)
J I
R (±)lk
ji = (v1/2
I v1/2
J
v1/2
K
)±1
( p
K
J I
j i
)
, (5)
∑
i′j′m
( k
C
A B
i′ j′
)
A D
R (±)i′l
im
B D
R (±)j′m
jn =
∑
p
C D
R (±)kl
pn
( p
C
A B
i j
)
, (6)
∑
a′
v1/2
I
I
waa′
( a′ b
I J
K
k
)
=eiπ(J−K)( [dK]
[dJ ] )1/2
( b
J
I K
a k
)
=
∑
k′
v1/2
I
K
wk′k
( b k ′
J K
I
a
)
,
∑
i′,k′
J
wii′
J I
R(±)lk′
ji′
J
w k′k =
I J
R (∓)il
kj , v J
∑
k
J
w ik J
wkj =δi
jY (1)
(J,j), (7)
( 0
0
I J
a b
)
=δI,J
J
wabeiπJ
√
[dI ]
, v J
∑
b
J
w
ab J
wkb=e2iπJ J
µ a
k, [dK] =
∑
a
K
µ a
a, (8)
( k
C
A B
i j
)
=
( i j
A B
C
k
)
∈ R. (9)
The Clebsch-Gordan coeﬃcients also satisfy the relations [17]:
( k
C
A B
i j
)
(q) =
( −k
C
B A
−j −i
)
(q) = ( −1)A+B−C
( −k
C
A B
−i −j
)
(q−1). (10)
Let us now recall basic facts about 6 j(0) that we will use extensively in our work.
6j(0) of Uq(su(2)) are deﬁned as follows:
{ A B
C F
E
D
}
(0)
δF,Hδp
nY (1)
(H,p) =
∑
i,j,k,l,m
( m
E
A B
i j
)( p
H
E C
m k
)( j k
B C
D
l
)( i l
A D
F
n
)
.
The properties of the Clebsch-Gordan coeﬃcients, recalled above , imply the following rela-
tions on 6j(0):
{
A B
C D
E
F
}
(0)
=
{
B A
D C
E
F
}
(0)
=
{
C D
A B
E
F
}
(0)
=
{
A D
C B
F
E
}
(0)
(Symmetries), (11)
{
A C
B E
F
D
}
(0)
=eiπ(C−F +E−D)( [dF ][dD]
[dC ][dE] )1/2
{
A F
B D
C
E
}
(0)
(Racah-Wigner), (12)
4
∑
C
{
A B
G H
C
I
}
(0)
{
A B
G H
C
J
}
(0)
=δI,JY (0)
(A,H,I )Y (0)
(B,G,I )(Orthogonality), (13)
∑
C
{
A B
H G
C
I
}
(0)
{
A B
G H
C
J
}
(0)
( v1/2
J v1/2
I v1/2
C
v1/2
G v1/2
H v1/2
A v1/2
B
)±1 =
{
A G
B H
I
J
}
(0)
, (14)
∑
A
{ D F
I G
A
J
}
(0)
{ D F
E B
A
C
}
(0)
{ E A
G H
B
I
}
(0)
=
{ E F
J H
C
I
}
(0)
{ D C
H G
B
J
}
(0)
. (15)
The relation (14) is called the “Racah-relation”, whereas the relatio n (15) is usually referred to
as the “Pentagonal equation” or the “Biedenharn-Elliot”equation . The relations (14)(15) imply
the Yang-Baxter equation on 6 j(0), also called “Hexagonal relation”.
Explicit expressions, as well as special values for low spins, of 6 j(0) symbols are given in [1],
but we want to add here the following asymptotic formulae which will be of importance in the
rest of this paper (for details see [17]):
lim
K→+∞
{
A B
K K+m+n
C
K +n
}
(0)
=eiπ(A+B−C)
(
m+n
C
A B
m n
)
, (16)
lim
K→+∞
{
A K+n1+n2
D K
K +n2
K +n′
1
}
(0)
(
v1/2
K+n2v1/2
K+n′
1
v1/2
K v1/2
K+n1+n2
)±1δn1+n2,n′
1+n′
2 =
A D
R (±)n′
1n′
2
n1n2. (17)
