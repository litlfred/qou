---
doc_id: raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials
doc_title: "On 2-variable q-Legendre polynomials: the view point of the q-operational technique"
section_id: sec-004-18-raza-n-fadel-m-c-cesarano
section_title: "Raza N., Fadel M., C. Cesarano"
section_number: 18
pages: 5-7
source_pdf: raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf
source_sha256: da8c1204e84d019c
doc_brief: "On 2-variable q-Legendre polynomials: the view point of the q-operational technique — 12 sections: Aligarh Muslim University , Aligar; University of Lahej, 73560 Lahej, ; Introduction"
---
1 2-variable q-Legendre polynomials
In this section, we introduce the 2-variable q-Legendre polynomials 2V qLP Sn,q(x, y) and
Rn,q(x, y)/[n]q! by means of generating function involving 0th order q-Bessel Tricomi functions
and obtain their series deﬁnitions, q-differential equations and operational identities.
In view of equations (1), (2) and (11), we deﬁne the 2-variabl e q-Legendre polynomials
2VqLP Sn,q(x, y) and Rn,q(x, y)/[n]q! by means of the following generating functions
eq(yt) C0,q(− xt2) =
∞
∑
n=0
Sn,q(x, y) tn
[n]q! (24)
and
C0,q(xt) C0,q(− yt) =
∞
∑
n=0
Rn,q(x, y)
[n]q!
tn
[n]q! , (25)
where C0,q(xt) denotes the 0 th order q-Bessel Tricomi functions, deﬁned by equation (11).
Expanding the left hand side of equation (24), using equatio ns (3) and (11) and then using
the series rearrangement technique, we get
∞
∑
n=0
[n/2]
∑
k=0
xkyn− 2ktn
([k]q!)2[n − 2k]q! =
∞
∑
n=0
Sn,q(x, y) tn
[n]q! .
Comparing the coefﬁcients of equal powers of t from both sides of the above equation, we get
the following explicit form
Sn,q(x, y) = [ n]q!
[n/2]
∑
k=0
xkyn− 2k
([k]q!)2[n − 2k]q! (26)
of Sn,q(x, y) polynomials.
Similarly , expanding the left hand side of equation (25) and using the same approaches in
acquiring (26), we obtain the following explicit form
Rn,q(x, y)
[n]q! = [ n]q!
n
∑
k=0
(− 1)k xkyn− k
([k]q!)2([n − k]q!)2 (27)
of Rn,q(x, y)/[n]q!.
From equations (26) and (27), we get
Sn,q(x, − y) = ( − 1)nSn,q(x, y) and Rn,q(− x, − y) = ( − 1)nRn,q(x, y),
respectively. Moreover, taking x = 0 and y = 0 one by one in equations (26) and (27), we get
the following boundary conditions
Sn,q(0, y) = yn, Sn,q(x, 0) =
{
[n]q!(x)[n/2]
q /([n/2]q!)2, if n is even,
0, if n is odd,
and
Rn,q(x, 0) = ( − x)n, Rn,q(0, y) = yn,
respectively.
On 2-variable q-Legendre polynomials: the view point of the q-operational technique 19
The operational identity allows the representation of Sn,q(x, y) as q-Laguerre and q-Hermite
polynomials of two variables by using equations (20) and (24 ), equation (23), for m = 2, as
follows
Sn,q(x, y) = [2]Ln,q(x, y) = Hn,q(y, D− 1
q,x ){1}.
Similarly , the polynomialsRn,q(x, y)/[n]q! can be represented as 2-variable q-Laguerre poly-
nomials by using the operational identity and equations (12 ) and (25) as follows
Rn,q(x, y)
[n]q! = Ln,q(x, D− 1
q,y ){1}.
As we noted earlier, the partial differential equations of ordinary 2-variable Legendre poly-
nomials give rise to real applied problems in areas such as he at condition equations and other
kinds of heat diffusion equations. T o this end, we demonstra te the q-partial differential equa-
tions of 2V qLP Sn,q(x, y) and Rn,q(x, y)/[n]q!.
Theorem 1. The 2VqLP Sn,q(x, y) and Rn,q(x, y)/[n]q! satisfy the following q-partial differential
equations:
L ˆDq,xSn,q(x, y) = ˆD2
q,ySn,q(x, y), (28)
or, alternatively ,
(qx ˆD2
q,x − ˆD2
q,y + ˆDq,x)Sn,q(x, y) = 0 (29)
and
L ˆDq,xRn,q(x, y) = − L ˆDq,yRn,q(x, y), (30)
or, alternatively ,
(q(x ˆD2
q,x + y ˆD2
q,y) + ˆDq,x + ˆDq,y)Rn,q(x, y) = 0, (31)
where
L ˆDq,x := ˆDq,xx ˆDq,x. (32)
Proof. Operating L ˆDq,x on both sides of equation (24) and using equations (32) and (1 5) in the
left hand side, we get
t2eq(yt)C0,q(− xt2) =
∞
∑
k=0
L ˆDq,xSn,q(x, y) tn
[n]q! . (33)
Furthermore, operating ˆDq,y on both sides of equation (24), by using equation (6), we rece ive
teq(yt)C0,q(− xt2) =
∞
∑
n=0
ˆDq,ySn,q(x, y) tn
[n]q! . (34)
Using equation (24) in the left hand side of equations (33) an d (34), then comparing the
coefﬁcients of equal powers of t from both sides of the resultant equation, we get
L ˆDq,xSn,q(x, y) = [ n]q[n − 1]qSn− 2,q(x, y), n ≥ 2, (35)
and
ˆDq,ySn,q(x, y) = [ n]qSn− 1,q(x, y), n ≥ 1. (36)
