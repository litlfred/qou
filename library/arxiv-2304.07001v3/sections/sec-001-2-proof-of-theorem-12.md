---
doc_id: arxiv-2304.07001v3
doc_title: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES"
section_id: sec-001-2-proof-of-theorem-12
section_title: "Proof of Theorem 1.2"
section_number: 2
pages: 7-13
source_pdf: 2304.07001v3.pdf
source_sha256: b6c0d7f50b6407f1
doc_brief: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES — We prove resurgence properties for the Borel transform of a f ormal power series associated to elements in the Habiro ring that come from radi al"
---
Proof of Theorem 1.2. The Borel transform of Ff (1/x) from ( 1.16) is given by
B[Ff ](p) = CM δ + Gf (p)
where
CM =− M
2
M∑
m=1
f (m)B2
(m
M
)
and
Gf (p) =
∞∑
n=1
(−1)n+1M 2n+1
(2n + 2)n!
M∑
m=1
f (m)B2n+2
(m
M
) pn−1
(n− 1)!bn
= M
∞∑
n=0
M∑
m=1
(−1)nf (m)B2n+4
(m
M
)
(2n + 4)!
(2n + 3)!
n!(n + 1)!
(M 2
b
) n+1
pn.
(2.1)
From the generating function
xext
ex− 1 =
∞∑
n=0
Bn(t)
n! xn,
where|x| < 2π, we deduce
∞∑
n=0
B2n(t)
(2n)! x2n = x
2
( ext
ex− 1− e−xt
e−x− 1
)
= x(ext + e−(t−1)x)
2(ex− 1) . (2.2)
Assuming|y| < 2π
M , x = iM y, and taking t = m
M , where 1 ≤ m≤ M , we use ( 2.2) to obtain
1
M y
M∑
m=1
f (m)
∞∑
n=0
B2n+2
(m
M
)
(2n + 2)! (iM y)2n+2 = i
2(eiM y− 1)
M∑
m=1
f (m)
(
eimy + e−i(m−M )y
)
=−2c·
sin
(
(k2−k1)y
2
)
sin
(
(M −k1−k2)y
2
)
sin
(
M y
2
) . (2.3)
If we let y =√p in ( 2.3), then
g1,f (p) := M 3
∞∑
n=0
M∑
m=1
f (m) B2n+4
(m
M
)
(2n + 4)! (−M 2p)n
= 1
M p2
∞∑
n=0
M∑
m=1
f (m) B2n+2
(m
M
)
(2n + 2)! (−M 2p)n+1− CM
p
=− 1
p3/2

2c·
sin
((k2−k1)√
p
2
)
sin
((M −k1−k2)√p
2
)
sin
(M √p
2
) + CM
√p

 . (2.4)
We conclude
Gf (p) = ( g1,f ⊛ g2,f )(p)
8 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
where g1,f was computed in (
2.4) and
g2,f (p) :=
∞∑
n=0
(2n + 3)!
n!(n + 1)!
(1
b
) n+1
pn = 1
b
6
(
1− 4 p
b
) 5/2
and ⊛ denotes the Hadamard product of two formal power series
( ∞∑
n=0
anpn
)
⊛
( ∞∑
n=0
bnpn
)
:=
∞∑
n=0
anbnpn.
It now follows that
Gf (p) = 1
2πi
∫
−γ
g1,f (s)g2,f
(p
s
) ds
s (2.5)
where γ is a circle with center at the origin and a small radius orient ed clockwise (see Figure
2).
γR
γ
Figure 2. Contour deformation of γR− γ
Now, we consider the poles of g1,f (s). Note that there is no pole at s = 0. By ( 2.4), they are
supported where p = 4ℓ2π2
M 2 , ℓ∈ Z. However,
sin
((k2− k1)√p
2
)
sin
((M− k1− k2)√p
2
)
= 0
when p = 4k2π2
(k2− k1)2 or p = 4k2π2
(M− k2− k1)2 for k∈ Z. Thus, if for some k, ℓ∈ Z
ℓ = M k
k2− k1
or ℓ = M k
M− k2− k1
which is true if and only if
ℓ =
M
gcd(M, k2−k1) k
(k2−k1)
gcd(M, k2−k1)
or ℓ =
M
gcd(M, M −k2−k1) k
(M −k2−k1)
gcd(M, M −k2−k1)
,
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 9
then g1,f (s) does not have poles at p = 4ℓ2π2
M 2 . Thus, the set of poles of g1,f (s) is given by
N1,f =
{ 4ℓ2π2
M 2 : ℓ∈ N, M
gcd(M, k2− k1) ∤ ℓ or M
gcd(M, M− k2− k1) ∤ ℓ
}
. (2.6)
We next carefully calculate the residues of the poles of the i ntegrand ( 2.5) which are given by
(2.6). Take a circle γR with center at the origin and of large radius R which encloses a ﬁnite
number of points N inN1,f . Thus,
1
2πi
∫
γR ∪ γ
g1,f (s)g2,f
(p
s
) ds
s =
∑
pi∈N1,f
1≤i≤N
Ress→pi
(g1,f (s)g2,f ( p
s )
s
)
=
∑ N
ℓ∈N
g2,f
(
pM 2
4ℓ2π2
)
(
4ℓ2π2
M 2
)
× lim
s→ 4ℓ2π2
M 2
(
s− 4ℓ2π2
M 2
) 
− 1
s3/2

2c·
sin
(
(k2−k1)√
s
2
)
sin
(
(M −k1−k2)√s
2
)
sin
(
M √s
2
) + CM
√s




=− 3πc
bM 2
∑ N
ℓ∈N
ℓ ˜f (ℓ)
(
ℓ2π2
M 2 − p
b
) 5/2 (2.7)
where
∑ N
means that ℓ runs over the ﬁrst N elements 4ℓ2π2
M 2 ofN1,f and ˜f (ℓ) is given by ( 1.12).
It follows that ⏐
⏐
⏐
⏐
∫
γR
g1,f (s)g2,f
(p
s
) ds
s
⏐
⏐
⏐
⏐→ 0 (2.8)
as R→∞ . Thus, (
2.5), ( 2.7), ( 2.8) and the contour deformation given in Figure 2 imply that
Gf (p) = 3πc
M 2b
∞∑
ℓ=1
ℓ ˜f (ℓ)
(
ℓ2π2
M 2 − p
b
) 5/2 . (2.9)
The set of poles of Gf (p) is then
N :=
{ bℓ2π2
M 2 : ℓ∈ N, M
gcd(M, k2− k1) ∤ ℓ or M
gcd(M, M− k2− k1) ∤ ℓ
}
.
Since Gf (p) has two branches, by considering the cut complex plane C\N , it can be made
analytic in this region. This implies (1). We now compute S±[Ff ](x):
S±[Ff ](x) =
∫ e±iθ∞
0
e−pxB[Ff ](p) dp = CM + 3πc
M 2b
∞∑
ℓ=1
ℓ ˜f (ℓ)
∫ e±iθ∞
0
e−px
(
ℓ2π2
M 2 − p
b
) 5/2 dp (2.10)
where the integral
∫ e+iθ∞
0 agrees with
∫ +i∞
0 ifℑ(x) > 0 and the integral
∫ e−iθ∞
0 agrees with∫ −i∞
0 ifℑ(x) < 0. To prove the ﬁrst part of (2), we start with the following fo rmula, valid for
10 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
ℜ(x) > 0: ∫
γ
e−px
(1− p)
5
2
dp =− 4
3 + 8
3
√πE(√x) (2.11)
where γ = [0, eiθ∞)∪ [0, e−iθ∞) and
E(y) := 2y3e−y2
√π
∫ y
0
et2
dt− y2
√π .
From (1.3) and ( 2.10), we have
Smed
f (x) = CM + 1
2
3πc
M 2b
∞∑
ℓ=1
ℓ ˜f (ℓ)
∫
γ
e−px
(
ℓ2π2
M 2 − p
b
) 5/2 dp
= CM + b
(M
π
) 3 3πc
2M 2b
∞∑
ℓ=1
˜f (ℓ)
ℓ
∫
γ
e− bpℓ2π2x
M 2
(1− p)5/2 dp (2.12)
where we have made the change of variable p→ bpℓ2π2
M 2 . Thus, ( 2.11) and ( 2.12) imply
Smed
f (x) = CM + 3M c
2π2
∞∑
ℓ=1
˜f (ℓ)
ℓ
{
− 4
3 + 8
3
√πE
(ℓπ
M
√
bx
)}
= 4M c
π3/2
∞∑
ℓ=1
˜f (ℓ)
ℓ E
(ℓπ
M
√
bx
)
where one can check that
CM = 2M c
π2
∞∑
ℓ=1
˜f (ℓ)
ℓ2 . (2.13)
This implies that Smed
f (x) is analytic on ℜ(x) > 0.
To prove the existence of the radial limit and part (3), we beg in with rewriting the integral on
the right-hand side of ( 2.10) as an integral of the partial theta function θ(0)
0,4M 2, ˜f (x). This requires
some attention due to the branch cut singularity of the resul ting square root. Integration by
parts yields
∫ e±iθ∞
0
e−px
(
ℓ2π2
M 2 − p
b
) 5/2 dp =


 2b
3
e−px
(
ℓ2π2
M 2 − p
b
) 3/2



e±iθ∞
0
+ 2bx
3
∫ e±iθ∞
0
e−px
(
ℓ2π2
M 2 − p
b
) 3/2 dp
= 2b
3


− M 3
ℓ3π3 + x
∫ xe±iθ∞
0
e− ℓ2π2b
M 2 p
(
ℓ2π2
M 2 − ℓ2π2
M 2x p
) 3/2 d
(ℓ2π2b
M 2x p
)



=− 2bM 3
3ℓ3π3 + 2b2M
3ℓπ
∫ xe±iθ∞
0
e− ℓ2π2b
M 2 p
(
1− p
x
) 3/2 dp. (2.14)
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 11
The change of coordinate x→− 1
2πiα where 0⁄= α∈ C to ( 2.14) yields
− 2bM 3
3ℓ3π3 + 2b2M
3ℓπ
∫ xe±iθ∞
0
e− ℓ2π2b
M 2 p
(
1− p
x
) 3/2 dp =− 2bM 3
3ℓ3π3 + 2b2M
3ℓπ
∫ − 1
2πiα e±iθ∞
0
e2πi ℓ22πib
4M 2 p
(
1 + 2πipα
) 3/2 dp
=− 2bM 3
3ℓ3π3 + b2M
3iℓπ2
∫ − 1
α e±iθ∞
0
e2πi ℓ2b
4M 2 p
(
1 + pα
) 3/2 dp. (2.15)
Now (1 + pα)3/2 has a branch cut at p =−1/α, hence we distinguish between ℜ(α) > 0 and
ℜ(α) < 0 (see Figure 3). If ℜ(α) > 0, then (1 + pα)3/2 = α3/2(1/α + p)3/2, and the integral at
angle−iθ will not change sign as the path is not crossing the branch cut , i.e.,
∫ − 1
α e−iθ∞
0 =
∫ +i∞
0 .
Ifℜ(α) < 0, then (1 + pα)3/2 = α3/2(1/α + p)3/2, but the integral at angle + iθ will change sign
as the path is crossing the branch cut, i.e.,
∫ − 1
α e+iθ∞
0 =−
∫ +i∞
0 .
◭
◭
− 1
α• ◮
◮
− 1
α•
Figure 3. Branch cut of (1 + pα)3/2. On the left for ℜ(α) < 0 and on the right
forℜ(α) > 0.
By ( 2.10), ( 2.13) and ( 2.15), we have for α∈ Q>0
∫ e−iθ∞
0
e
p
2πiαB[Ff ](p) dp =−i cb
M π
∞∑
ℓ=1
˜f (ℓ)
∫ − 1
α e−iθ∞
0
e2πi ℓ2b
4M 2 p
(
1 + pα
) 3/2 dp
=−i cb
M πα3/2
∞∑
ℓ=1
˜f (ℓ)
∫ +i∞
0
e2πi ℓ2b
4M 2 p
(
1/α + p
) 3/2 dp
=−i cb
M πα3/2
∫ +i∞
0
θ(0)
0,4M 2, ˜f (bp)
(
1/α + p
) 3/2 dp
while for α∈ Q<0, we obtain
∫ e+iθ∞
0
e
p
2πiαB[Ff ](p) dp =−i cb
M π
∞∑
ℓ=1
˜f (ℓ)
∫ − 1
α e+iθ∞
0
e2πi ℓ2b
4M 2 p
(
1 + pα
) 3/2 dp
12 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
= i cb
M πα3/2
∞∑
ℓ=1
˜f (ℓ)
∫ +i∞
0
e2πi ℓ2b
4M 2 p
(
1/α + p
) 3/2 dp
= i cb
M πα3/2
∫ +i∞
0
θ(0)
0,4M 2, ˜f (bp)
(
1/α + p
) 3/2 dp.
We now compute the discontinuity disc 0(x) across the positive real axis:
disc0(x) := S+[Ff ](x)− S−[Ff ](x)
= 3πc
M 2b
∞∑
ℓ=1
ℓ ˜f (ℓ)
[ ∫ e+iθ∞
0
e−px
(ℓ2π2
M 2 − p
b
) 5/2 dp−
∫ e−iθ∞
0
e−px
(ℓ2π2
M 2 − p
b
) 5/2 dp
]
= 3πc
M 2b
∞∑
ℓ=1
ℓ ˜f (ℓ)
∫
C
e−px
(ℓ2π2
M 2 − p
b
) 5/2 dp
= 3πcb3/2
M 2
∞∑
ℓ=1
ℓ ˜f (ℓ)e− ℓ2 π2b
M 2 x
∫
Cℓ
e−px
(−p)5/2 dp
= 3πcb3/2
M 2
∞∑
ℓ=1
ℓ ˜f (ℓ)e− ℓ2π2b
M 2 x
∫
Cℓ
e−px
(−xp)5/2 d(xp)x3/2
= 2πi
Γ
(5
2
) x3/2 3πcb3/2
M 2
∞∑
ℓ=1
ℓ ˜f (ℓ)e− ℓ2π2b
M 2 x
= 2i (2bπx)3/2
√
2c
M 2
∞∑
ℓ=1
ℓ ˜f (ℓ)e− ℓ2π2b
M 2 x
= 2i (2bπx)3/2
√
2c
M 2 θ(1)
0,4M 2, ˜f (2πix).
(2.16)
Here,Cℓ =C− ℓ2π2b
M 2 whereC is the Hankel contour enclosing the branch point singularit y arising
from the second line in ( 2.16), as in Figure 4. The radial limit x→− 1
2πiα of the partial theta
series appearing in the last line of ( 2.16) exists by [ 2, Proposition 3.1] and so
disc0
(
− 1
2πiα
)
= 2i
(ib
α
) 3/2
√
2c
M 2 θ(1)
0,4M 2, ˜f
(
− b
α
)
.
In addition, the radial limit x→− 1
2πiα also exists for S±[Ff ](x) since they are analytic functions
on the half-planes ℜ(e±iθx) > 0, respectively (see the change of coordinates after ( 2.14)). Thus,
the second part of (2) follows. Summarizing, we ﬁnd that
Smed
f
(
− 1
2πiα
)
=













S+
(
− 1
2πiα
)
+
(b
α
) 3/2
eπi/4
√
2c
M 2 θ(1)
0,4M 2, ˜f
(
− b
α
)
if α∈ Q>0,
S−
(
− 1
2πiα
)
−
(b
α
) 3/2
eπi/4
√
2c
M 2 θ(1)
0,4M 2, ˜f
(
− b
α
)
if α∈ Q<0
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 13
• • •<
<
S+[Ff ]
S− [Ff ]
• • •
<
>
C
Figure 4. The Hankel contour C for the discontinuity disc 0(x).
with
S±
(
− 1
2πiα
)
=∓i cb
M πα3/2
∫ +i∞
0
θ(0)
0,4M 2, ˜f (bp)
(
1/α + p
) 3/2 dp.
Finally, noticing that ( iα)−3/2 =∓eπi/4α−3/2 depending on the sign of α and on our choice of
the branch of the square root, part (3) follows. □
