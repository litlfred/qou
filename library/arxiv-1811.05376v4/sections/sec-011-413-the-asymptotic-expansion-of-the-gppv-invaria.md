---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-011-413-the-asymptotic-expansion-of-the-gppv-invaria
section_title: "The asymptotic expansion of the GPPV invariant"
section_number: 4.1.3
pages: 33-36
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
Recall the deﬁnition the functionsF and g given in (15). Letm∈ N. Fory close to 2πim we use
the notation of Propositon 14 and write
F (y) =
n−2∑
j=1
fj(m)(y− 2πim)−j + reg.,
whereeach fj : Z→ Cis 2P-periodic. Foreach l∈ Nthereexistsauniquelydeterminedpolynomial
Pl(x,y )∈Q[πi,x,y ]
such that
1
l!
∂leg(y)/τ
∂yl (2πim) =eg(2πim)/τPl(τ−1,m ). (79)
There exists uniquely determined complex coeﬃcientspl,u,v, with
Pl(τ−1,m ) =
∑
u,v
pl,u,vτ−umv.
Recall thatBm(x) denotes them’th Bernoulli polynomial and is deﬁned by (74). Deﬁne for each
θ∈ CSC(X) the following polynomials with coeﬃcients in power series
Rθ(k,t ) =
∑
m=1,...,2P,
g(2πim)≡2πiθ
∑
j,u,v
fj(m)kupj−1,u,v
∞∑
r=0
(2P )2r+v
2r +v + 1B2r+v+1
(m
2P
) (−t)r
r! ,
ˇZθ(k,t ) =
∑
m=1,...,2P,
g(2πim)≡2πiθ
∑
j,u,v
fj(m)kupj−1,u,v
∞∑
r=1
(2P )2r+v
2r +v + 1B2r+v+1
(m
2P
) (−t)r
r!
(80)
Observe
ˇZθ(k,t ) =Rθ(k,t )−Rθ(k, 0),
i.e. ˇZθ is equal toRθ minus the constant in the parametert.
We can now prove Theorem 4.
Proof of Theorem 4.Recall the decompsition
√τ
λ q∆ˆZ =L(τ) +R(τ)
given in Equation (61) in Lemma 1. Recall the decomposition of the normalized quantum invariant
Zk(X) = ZI(k) + ZR(k)
given in (16). This decomposition together with equation (1), which relates the normalized quan-
tum invariant˜Zk(X) to the WRT invariantτk(X), shows the radial limit idenity can be proved by
proving the following two limits.
ZI(k) = lim
τ↑1/k
√τ
2λL(τ), ZR(k) = lim
τ↑1/k
,
√τ
2λR(τ).
Observe that asX is an integral homology sphere, the onlySpinc structure isa = 0, and therefore
the radial limit conjecture reduces (up to a scalar factor) to equation (8). We ﬁrst focus on the
integral partL(τ). For everyk∈ N∗ the integral partL(τ) extends continuosly toτ = 1/k and it
follows from Equations (16), (39) and (62) that
(2λ
√
k)−1L(1/k) =LR+(B(Z0))(k) = ZI(k).
Resurgence Analysis of Quantum Invariants 34
Now recalling thatτk,t = (k−i 2Pt
π )−1, we see that the non-trivial parts left in order to prove the
asymptotic expansion (7) stated in Theorem 4 are the asymptotic expansion
√τk,t
2λ R(τk,t) ∼
t→0
∑
θ∈CSC(X)
e2πikθRθ(k,t ), (81)
and the identity ∑
θ∈CSC(X)
e2πikθRθ(k, 0) = ZR(k). (82)
We start with the expansion (81). To ease notation we set
g(2πim) =θm.
We have
Res(F (y)eg(y)/τ, 2πim) =eθm/τ
n−3∑
j=1
fj(m)Pj−1(τ−1,m ).
and accordingly √τ
2λR(τ) =−
∞∑
m=0
eθm/τ
n−3∑
j=1
fj(m)Pj−1(τ−1,m ),
Note thatτk,t∈ h for t∈ (0, 1). The functiong has the following transformation property
g(y + 4πimP ) = i(y + 4πimP )2
8πP =g(y)−my− 2πim2P.
Because of this, and the2P periodicity of thefj’s, we can write
√τ
2λR(τ) =−
∞∑
m=0
e−tm2
ekg(2πim)
n−3∑
j=1
fj(m)Pj−1(τ−1,m )
=−
n−2∑
j=1
∑
u,v
∞∑
m=0
e−tm2
ekθmfj(m)pj−1,u,vτ−umv.
Now for eachj,u = 0,...,n − 3 we can apply Proposition 13 to the2P-periodic function of mean
value zero given by
Cj(m) =ekθmfj(m)
and the polynomial
Qj,u(m) =
∑
v
pj−1,u,vmv.
The fact that eachCj is of mean value equal to zero follows from Proposition 14. The result of
applying Proposition 13 is
√τ
2λR(τ) ∼
t→0
−
∑
j,u,v
∞∑
r=0
kupj−1,u,vL(−2r−v,Cj)(−t)r
r!
=
∑
j,u,v
∞∑
r=0
kupj−1,u,v
(2P )2r+v
2r +v + 1
2P∑
m=1
Cj(m)B2r+v+1
(m
2P
) (−t)r
r!
=
2P∑
m=1
∑
j,u,v
ekθmfj(m)kupj−1,u,v
∞∑
r=0
(2P )2r+v
2r +v + 1B2r+v+1
(m
2P
) (−t)r
r! .
This establishes the asymptotic expansion (81).
We now turn to the identity (82). Set
R0(k) =
∑
θ∈CSC(X)
e2πikθRθ(k, 0) =
2P∑
m=1
∑
j,u,v
ekθmfj(m)pj−1,u,vku (2P )v
v + 1Bv+1
(m
2P
)
. (83)
Resurgence Analysis of Quantum Invariants 35
Let x be a complex coordinate near0 and setym =x + 2πim for m = 1, 2,..., 2P. Recall that
ZR(k) =−
2P−1∑
m=1
Res
(F (y) exp (kg(y))
1− exp(−ky) ,y = 2πim
)
.
We have that
g(ym) =g(x + 2πim) = i(x + 2πim)2
8πP =g(2πim) +g(x)− xm
2P ,
and accordingly
exp(kg(ym)) = exp (kθm +kg(x))· exp
(
−kxm
2P
)
. (84)
Recall that the polynomialsPl deﬁned in (79) as the coeﬃcients of the Taylor series ofekg(y).
Therefore it follows from Cauchy’s formula for multiplication of power series, the formula for the
Taylor expansion of the exponential and the identity (84) that the following holds for allk,m
Pc(k,m ) =
∑
a+b=c
Pa(k, 0)
(−mk
2P
)b 1
b!.
Writing this out in terms of coeﬃcients gives
∑
c,u,v
pc,u,vkumv =
∑
a+b=c
∑
s
pa,s,0
((−1)
2P
)b 1
b!ks+bmb.
This is equivalent to the identities
pj,u,0
(−1
2P
)v 1
v! =pj+v,u+v,v. (85)
Recall the deﬁnition (74) of the Bernoulli polynomialsBm. Write
− F (ym) exp (kg(ym))
1− exp(−kym) =F (ym) exp (k(g(x) +θm) exp
(−kxm
2P
)
exp(−kx)− 1 =


n−3∑
j=1
fj(m)x−j + reg.


(
ekθm
∞∑
a=0
Pa(k, 0)xa
)( ∞∑
b=0
Bb
( m
2P
)
b! (−kx)b−1
)
.
By comparing with Equation (83) and using the facts thatF has a multiple order zero at multiples
of 4πiP and that we know that thek−1 term cancels inZR(k), we obtain the desired identity
ZR(k) =
2P∑
m=1
n−2∑
j=1
∑
a+b=j,
a≥0,b≥1
ekθmfj(m)Pa(k, 0)Bb
( m
2P
)
b! (−k)b−1
=
2P∑
m=1
n−2∑
j=1
∑
a+b=j,
a≥0,b≥1
ekθmfj(m)Pa(k, 0)
(−1
2P
)b−1 kb−1
(b− 1)!
(2P )b−1
b Bb
(m
2P
)
=
2P∑
m=1
n−2∑
j=1
∑
a+b=j,
a≥0,b≥1
∑
s
ekθmfj(m)pa,s,0
(−1
2P
)b−1 ks+b−1
(b− 1)!
(2P )b−1
b Bb
(m
2P
)
=
2P∑
m=1
n−2∑
j=1
∑
s,a+b=j,
a≥0,b≥1
∑
s
ekθmfj(m)pa+b−1,s+b−1,b−1ks+b−1 (2P )b−1
b Bb
(m
2P
)
(86)
=
2P∑
m=1
n−2∑
j=1
∑
u,v
ekθmfj(m)pj−1,u,vku (2P )v
v + 1Bv+1
(m
2P
)
(87)
=R0(k).
In (86) we used the identity (85), and in (87) we setu =s +b− 1 andv =b− 1. This ﬁnishes the
proof.
Resurgence Analysis of Quantum Invariants 36
