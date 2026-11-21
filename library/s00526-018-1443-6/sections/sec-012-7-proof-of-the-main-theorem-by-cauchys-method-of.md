---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-012-7-proof-of-the-main-theorem-by-cauchys-method-of
section_title: "Proof of the main theorem by Cauchy's method of majorants"
section_number: 7
pages: 20-27
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
In order to prove the main result, Theorem 1.2, we deduce a recursive estimate for ∥∂lγ ∥H1
by putting together the results of the previous sections. We then apply Cauchy’s method of
majorants to the recursive formula to achieve the analyticity of γ .
Let m := 1 > 1
2 and γ : R/Z →Rn, γ = (γ1, . . . , γn), be a simple, closed, and by
arc-length parametrized curve with γ ∈C∞(R/Z, Rn) and γ a critical point of the Möbius
energy E. Then (3.1) tells us that γ solves the Euler–Lagrange equation
(Hγ, h)L2([0,1],Rn) = 0
for all h ∈H2(R/Z, Rn) and therefore
Hγ = P⊥
˙γ Qγ + P⊥
˙γ R1γ + P⊥
˙γ R2γ ≡0
(7.1)
on R/Z by (3.2) and (3.3). Let l ∈N0. Then by Corollary 4.2 (7.1), the deﬁnition of the
orthogonal projection, and the triangle inequality
∥∂l+3γ ∥H1 ≤
C∥∂l Qγ ∥H1
= 
C

)))∂l 
PT
˙γ Qγ −P⊥
˙γ R1γ −P⊥
˙γ R2γ

)))
H1

≤
C

∥∂l PT
˙γ Qγ ∥H1 + ∥∂l P⊥
˙γ R1γ ∥H1 + ∥∂l P⊥
˙γ R2γ ∥H1

.
(7.2)
For the next estimates we assume 1
2 ≥ε > 0. Then the estimates of the Sects. 2.1 and 5
imply the following estimate for the tangential part of Q.
Lemma 7.1 Let l ∈N0. There exists a positive constant CQ < ∞which is independent of ε
and l such that the following estimate holds:
∥∂l PT
˙γ Qεγ ∥H1 ≤CQ
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

∥∂l−k1+2γ ∥H1∥∂k1−k2+2γ ∥H1∥∂k2+1γ ∥H1.
Proof Applying the Leibniz rule twice, we obtain
∂l 
PT
˙γ Qεγ (x)

= ∂l
⎛
⎝4

|w|∈

ε, 1
2


[0,1]2(1 −t)(−t)⟨¨γ (x + tw), ¨γ (x + stw)⟩Rn
w
˙γ (x)dsdtdw
⎞
⎠
= 4

|w|∈

ε, 1
2


[0,1]2(1 −t)(−t)∂l
⟨¨γ (x + tw), ¨γ (x + stw)⟩Rn
w
˙γ (x)

dsdtdw
= 4

|w|∈

ε, 1
2


[0,1]2(1 −t)(−t)·
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2
*
∂l−k1+2γ (x + tw), ∂k1−k2+2γ (x + stw)
+
Rn
w
∂k2+1γ (x)dsdtdw
= 4

[0,1]2(1 −t)(−t)·
On the analyticity of critical points of the Möbius energy
Page 21 of 28
16
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

n
	
k=1
Hε
t,st(∂l−k1+2γk, ∂k1−k2+2γk)(x)∂k2+1γ (x)dsdt
where interchanging integrals and derivative are permitted due to the smoothness of the
integrand. Hence, by using the Banach algebra property of H1 (2.1), the estimate of the
approximation of the bilinear Hilbert transform (Theorem 5.3) for each of the components, the
equivalence of the Sobolev norms and the inequality of Cauchy-Schwarz we get component-
wise for all 1 ≤m ≤n
∥∂l(PT
˙γ Qεγ )m∥H1
≤4

[0,1]2 |1 −t||t|·
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

n
	
k=1
C1∥Hε
t,st(∂l−k1+2γk, ∂k1−k2+2γk)∥H1∥∂k2+1γm∥H1dsdt
≤4C1

[0,1]2 |1 −t||t|·
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2
  n
	
k=1
CH∥∂l−k1+2γk∥H1∥∂k1−k2+2γk∥H1

∥∂k2+1γm∥H1dsdt
≤4C1CH
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

∥∂l−k1+2γ ∥H1∥∂k1−k2+2γ ∥H1∥∂k2+1γm∥H1 < ∞.
We ﬁnally get by the deﬁnition of the H1-norm and the inequality of Cauchy-Schwarz
∥∂l PT
˙γ Qεγ ∥H1
≤4C1CH
√n
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

∥∂l−k1+2γ ∥H1∥∂k1−k2+2γ ∥H1∥∂k2+1γm∥H1 < ∞.
where CQ := 4C1CH
√n < ∞is a positive constant which is independent of ε and l.
⊓⊔
Let us now estimate the remaining parts of the decomposition of the gradient by using
the form of P⊥
˙γ Rε
1γ (respectively, P⊥
˙γ Rε
2γ ), Faà di Bruno’s formula and the Banach algebra
property of H1.
Lemma 7.2 Let us consider the mapping f : R/Z →Rn \ {0} × R3n, f = ( f1, . . . , f4n),
f (x) :=
⎛
⎜⎜⎝
˙γ (x)
¨γ (x)
¨γ (x)
¨γ (x)
⎞
⎟⎟⎠
and let l ∈N0. Then we obtain positive constants CR1,r < ∞which are independent of ε
and l such that the universal polynomial p(4n)
l
from the multivariate form of Faa di Bruno’s
formula Remark 2.7 satisfy
∥∂l P⊥
˙γ Rε
1γ ∥H1 ≤CR1 p(4n)
l
.(|α| + 1)!
r|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

where C1 is the constant from the estimate (2.1) with m = 1.
16
Page 22 of 28
S. Blatt, N. Vorderobermeier
Proof We start by recalling the formula of P⊥
˙γ Rε
1γ computed in the previous section,

P⊥
˙γ Rε
1γ

(x) =

|w|∈
'
ε, 1
2
(

[0,1]4(r1 −r2)2G1( f1(x))dψ1dψ2dr1dr2dw
where G1 : Rn \ {0} × R3n →Rn is an analytic function as deﬁned in (6.3) and (6.4) and
f1(x) :=
⎛
⎜⎜⎝
 1
0 ˙γ (x + sw)ds
¨γ (x + r2w + (r1 −r2)ψ1w)
¨γ (x + r2w + (r1 −r2)ψ2w))
 1
0 ¨γ (x + tw)dt
⎞
⎟⎟⎠.
By interchanging derivative and integral due to the smoothness of the integrand and
by applying the generalized Faà di Bruno’s formula as stated in Remark 2.7 we obtain
component-wise for all 1 ≤k ≤4n
∂l 
P⊥
˙γ Rε
1γ

k (x)
= ∂l

|w|∈

ε, 1
2


[0,1]4(r1 −r2)2G1,k( f1(x))dψ1dψ2dr1dr2dw
=

|w|∈

ε, 1
2


[0,1]4(r1 −r2)2∂lG1,k( f1(x))dψ1dψ2dr1dr2dw
=

|w|∈

ε, 1
2


[0,1]4(r1 −r2)2·
p(4n)
l

{(∂αG1)k( f1(x))}|α|≤l, { f ( j)
1,i (x)}1≤j≤l,1≤i≤4n

dψ1dψ2dr1dr2dw.
Applying the H1-norm on ∂l(P⊥
˙γ Rε
1γ ) component-wise, we yield for any 1 ≤k ≤4n by
the deﬁnition of the H1-norm, triangle inequality and the Banach algebra property of H1
∥∂l 
P⊥
˙γ Rε
1γ

k ∥H1
≤

|w|∈

ε, 1
2


[0,1]4 |r1 −r2|2·
)))p(4n)
l

{(∂αG1)k( f1)}|α|≤l, { f ( j)
1,i }1≤j≤l,1≤i≤4n

)))
H1 dψ1dψ2dr1dr2dw
≤

|w|∈

ε, 1
2


[0,1]4 |r1 −r2|2·
p(4n)
l

{
))(∂αG1)k( f1)
))
H1}|α|≤l, {C1∥f ( j)
1,i ∥H1}1≤j≤l,1≤i≤4n

dψ1dψ2dr1dr2dw
where p(4n)
l
is the polynomial coming from Remark 2.7. The constant C1 does not appear in
front of ∥(∂αG1)k( f1)∥H1 because p(4n)
l
is one-homogeneous in the ﬁrst components.
Note that for any 1 ≤j ≤l
∥f ( j)
1,k ∥H1 ≤∥f ( j)
k
∥H1
∀1 ≤k ≤n, 3n + 1 ≤k ≤4n,
∥f ( j)
1,k ∥H1 = ∥f ( j)
k
∥H1
∀n + 1 ≤k ≤3n,
On the analyticity of critical points of the Möbius energy
Page 23 of 28
16
and ∥f ( j)
k
∥H1 does not depend on any of the parameters w, ψi,ri, s, t for all 1 ≤k ≤4n,
1 ≤j ≤l. Now, since f1 is a continuous function on R/Z and due to γ ∈C∞(R/Z, Rn),
f1([0, 1]) is a compact set K of Rn \ {0} × R3n. By the analyticity of G1, there hence are
constants CG1 < ∞,r > 0, such that
∂αG1(x)
 ≤CG1
|α|!
r|α|
(7.3)
for all α ∈Nk0
0 , k0 ∈N0, and x ∈K. Without loss of generality, we assume r < 1. By
deﬁning the constant C f1 := 1 + ∥f1∥H1 ≤1 + ∥f ∥H1 < ∞, using Lemma 2.1 and (7.3)
we can estimate
))(∂αG1)k( f1)
))
H1
=
))(∂αG1,k|K )( f1)
))
H1
≤Cc
))∂αG1,k|K
))
C1 (1 + ∥f1∥H1)
≤CcC f1
))∂αG1,k|K
))
C1
= CcC f1
max
|β|=|α|+1{
))∂αG1,k|K
))
∞,
))∂βG1,k|K
))
∞}
≤CcC f1CG1
max
|β|=|α|+1
.|α|!
r|α| , |β|!
r|β|
/
≤CcC f1CG1
(|α| + 1)!
r|α|+1
max
. r|α|+1
|α| + 1, 1
/
Hence
))(∂αG1)k( f1)
))
H1 ≤
CR1
(|α| + 1)!
r|α|+1
for all α ∈Nk0
0 , k0 ∈N0, and
CR1 := CcC f1CG1 supα max
0
r|α|+1
|α|+1
1
< ∞and with CR1 :=
√
4n 
CR1 we get
))(∂αG1)( f1)
))
H1 ≤CR1
(|α| + 1)!
r|α|+1
In the end we arrive at
∥∂l 
P⊥
˙γ Rε
1γ

∥H1
≤p(4n)
l
.
CR1
(|α| + 1)!
r|α|+1
/
|α|≤l
, {∥C1 f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

which is independent of ε. Using that p(4n)
l
is one-homogeneous in the ﬁrst components, we
get the claim.
⊓⊔
The term P⊥
˙γ Rε
2γ can be estimated analogously:
Lemma 7.3 Let l ∈N0 and f = ( ˙γ , ¨γ , ¨γ , ¨γ ) as in Lemma 7.2. Then there are positive
constants CR2, s < ∞which are independent of ε and l and the same universal polynomial
p(4n)
l
as in Lemma 7.2 such that
∥∂l P⊥
˙γ Rε
2γ ∥H1 ≤CR2 p(4n)
l
.(|α| + 1)!
s|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

.
16
Page 24 of 28
S. Blatt, N. Vorderobermeier
Proof Completely similar to Lemma 7.2.
⊓⊔
The estimates of the Lemmata 7.1, 7.2 and 7.3 are also valid for the limit ε ↓0 on the
left-hand sides, what can be proved as below.
Theorem 7.4 Let l ∈N0 and f = ( ˙γ , ¨γ , ¨γ , ¨γ ) as in Lemma 7.2. Then there are posi-
tive constants CQ, CR1, CR2,r, s < ∞which are independent of l and the same universal
polynomial p(4n)
l
as in Lemma 7.2 such that
∥∂l PT
˙γ Qγ ∥H1 ≤CQ
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

∥∂l−k1+2γ ∥H1∥∂k1−k2+2γ ∥H1∥∂k2+1γ ∥H1,
∥∂l P⊥
˙γ R1γ ∥H1 ≤CR1 p(4n)
l
.(|α| + 1)!
r|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

,
∥∂l P⊥
˙γ R2γ ∥H1 ≤CR2 p(4n)
l
.(|α| + 1)!
s|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

.
Proof Let l ∈N0 and { fε}ε>0 be a set of functions fε : R/Z →Rn such that there exist
positive constants Ci < ∞with ∥∂i fε∥H1 ≤Ci for all ε > 0 and 0 ≤i ≤l. Furthermore,
let us assume that ∂i fε
ε↓0
−→fi point-wise on [0, 1] with fi : R/Z →Rn, 0 ≤i ≤l. Our
aim is to show that ∂l fε
ε↓0
−→∂l f0 ∈H1(R/Z, Rn) weakly in H1 and hence especially
∥∂l f0∥H1 ≤lim inf
ε↓0
∥∂l fε∥H1 ≤Cl.
Then the statement of the theorem follows directly from applying this abstract argument
to fε = ∂l PT
˙γ Qεγ , fε = ∂l P⊥
˙γ Rε
1γ and fε = ∂l P⊥
˙γ Rε
2γ and using the previous Lem-
mata 7.1, 7.2 and 7.3.
Since H1(R/Z, Rn) is a Hilbert space, there exists a subsequence { fεk}k∈N of { fε}ε>0
which converges weakly to a unique function f ∈H1(R/Z, Rn) in H1(R/Z, Rn) and
by the compact embedding H1(R/Z, Rn) ⊂⊂C(R/Z, Rn) strongly to f with respect to
the uniform norm. Due to the point-wise convergence of fεk
k→∞
−→
f0 and the uniform
boundedness of { fεk}k∈N, { fεk}k∈N converges to f0 in C(R/Z, Rn) as well. By the uniqueness
of limits of weak convergent series we get f = f0 and since every weakly convergent
subsequence of { fε}ε>0 has the same limit, { fε}ε>0 converges weakly to f0 ∈H1(R/Z, Rn)
with respect to the H1-norm and strongly to f0 with respect to the L2-norm. By the same
argument, {∂l fε}ε>0 converges weakly to fl ∈H1(R/Z, Rn) with respect to the H1-norm
and strongly to fl with respect to the uniform norm.
It remains to show ∂l f0 = fl which follows by
On the analyticity of critical points of the Möbius energy
Page 25 of 28
16
0 = lim
ε↓0
 1
0
∂l fε(x)φ(x)dx −(−1)l
 1
0
fε(x)∂lφ(x)dx

=
 1
0
fl(x)φ(x)dx −(−1)l
 1
0
f0(x)∂lφ(x)dx
for all φ ∈C∞([0, 1], Rn) where we used Lebesgue’s theorem.
⊓⊔
Proof of Theorem 1.2 Let γ : R/Z →Rn, γ = (γ1, . . . , γn), be a closed, simple, and by
arc-length parametrized curve in H
3
2 (R/Z, Rn) that is a critical point of the Möbius energy
E. We deduce by Theorem 1.1 that γ ∈C∞(R/Z, Rn). Moreover, we set f : R/Z →R4n,
f (x) :=
⎛
⎜⎜⎝
˙γ (x)
¨γ (x)
¨γ (x)
¨γ (x)
⎞
⎟⎟⎠
and al := C1∥∂l f ∥H1 for all l ∈N0. Our main goal is to determine positive constants
δ, Cγ < ∞such that
al ≤Cγ
l!
δl
from which we can directly conclude the analyticity of γ on R/Z by Corollary 2.4.
As explained above in the beginning of the section, (7.1) and therefore (7.2) hold for any
l ∈N0, more precisely
∥∂l+3γ ∥H1 ≤
C

∥∂l PT
˙γ Qγ ∥H1 + ∥∂l P⊥
˙γ R1γ ∥H1 + ∥∂l P⊥
˙γ R2γ ∥H1

.
Due to the deﬁnition of the Sobolev norm and the previous Theorem 7.4 we may conclude
that
al+1 =C1∥∂l+1 f ∥H1 ≤C1(3∥∂l+3γ ∥H1 + ∥∂l+2γ ∥H1)
≤3
CC1

∥∂l PT
˙γ Qγ ∥H1 + ∥∂l P⊥
˙γ R1γ ∥H1 + ∥∂l P⊥
˙γ R2γ ∥H1

+ al
≤3
CC1
⎛
⎝CQ
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

∥∂l−k1+2γ ∥H1∥∂k1−k2+2γ ∥H1∥∂k2+1γ ∥H1
+CR1 p(4n)
l
.(|α| + 1)!
r|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

+CR2 p(4n)
l
.(|α| + 1)!
s|α|+1
/
|α|≤l
, {C1∥f ( j)
i
∥H1}1≤j≤l,1≤i≤4n

+ al.
Hence, there are constants C < ∞and rγ > 0 such that
al+1 ≤C
⎛
⎝
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

al−k1ak1−k2ak2
+p(4n)
l
⎛
⎝

(|α| + 1)!
r|α|+1
γ
2
|α|≤l
, {a j}1≤j≤l
⎞
⎠
⎞
⎠
+al.
(7.4)
16
Page 26 of 28
S. Blatt, N. Vorderobermeier
For any y ∈R4n, y = (y1, . . . , y4n), we deﬁne a majorant F : R4n →R4n component-wise
as
Fi(y) := C
⎛
⎝y3
i +
1
(1 + 4na0−(y1+···+y4n)
rγ
)2
⎞
⎠+ yi,
for all 1 ≤i ≤4n, which is clearly analytic around a0(1, . . . , 1). We now consider a solution
to the following initial value problem
˙c(t) = F(c(t)),
c(0) = a0(1, . . . , 1).
(7.5)
The Theorem 2.5 implies that (7.5) has a unique solution c in C∞(] −ε, ε[, R4n) for some
ε > 0 which is analytic around 0. So c can be expressed by its Taylor series in a neighborhood
of 0:
c(t) :=
∞
	
k=0
ak(1, . . . , 1)
k!
tk
where ak(1, . . . , 1) = c(k)(0). By Theorem 2.2 we know that there exist positive constants
rc, M < ∞such that
|c(l)(t)| ≤M l!
rlc
(7.6)
for all t ∈Brc(0) and l ∈N0.
For 1 ≤i ≤4n and l ∈N0 we have by Faà di Brunos formula as stated in Remark 2.7
∂l Fi(c(t))
= C
⎛
⎝
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

c(l−k1)
i
(t)c(k1−k2)
i
(t)c(k2)
i
(t)
+p(4n)
l
⎛
⎜⎜⎝
⎧
⎪⎨
⎪⎩
(|α| + 1)!
r|α|+1
γ
1

1 +

4na0
rγ
−(c1(t)+···+c4n(t))
rγ

|α|+2
⎫
⎪⎬
⎪⎭
|α|≤l
, {c( j)
i
(t)}1≤j≤l,1≤i≤4n
⎞
⎟⎟⎠
⎞
⎟⎟⎠
+ c(l)
i (t),
so we obtain by the initial condition (7.5)
∂l Fi(c(0)) = C
⎛
⎝
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

˜al−k1 ˜ak1−k2 ˜ak2
+p(4n)
l
⎛
⎝

(|α| + 1)!
r|α|+1
γ
2
|α|≤l
, {˜a j}1≤j≤l
⎞
⎠
⎞
⎠+ ˜al.
On the analyticity of critical points of the Möbius energy
Page 27 of 28
16
Hence, for all l ∈N0
˜al+1 = C
⎛
⎝
l	
k1=0
k1
	
k2=0
 l
k1
k1
k2

˜al−k1 ˜ak1−k2 ˜ak2
+p(4n)
l
⎛
⎝

(|α| + 1)!
r|α|+1
γ
2
|α|≤l
, {˜a j}1≤j≤l
⎞
⎠
⎞
⎠+ ˜al.
(7.7)
Comparing (7.4) and (7.7) and using the fact that the coefﬁcients of the polynomial pl are
non-negative, we get by a0 = a0 and induction
al ≤al.
Hence ∥∂l+1γ ∥H1 ≤al ≤M l!
rl
C for all l ∈N0 by (7.6). Thus γ is analytic by Corollary 2.4.
⊓⊔
