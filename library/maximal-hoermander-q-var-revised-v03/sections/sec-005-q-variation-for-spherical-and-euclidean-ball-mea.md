---
doc_id: maximal-hoermander-q-var-revised-v03
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-005-q-variation-for-spherical-and-euclidean-ball-mea
section_title: "q-variation for spherical and euclidean ball means in Rd"
section_number: null
pages: 16-21
source_pdf: Maximal-Hoermander-q-Var-revised-v03.pdf
source_sha256: 135332c04a1b3bb8
doc_brief: "HAL Id: hal-04526930 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 10 sections: Introduction"
---
In this section, we consider fort> 0, d∈N, 1<p< ∞and f∈S(Rd) a Schwartz function,
Atf(x) = 1
|Sd|

Sd
f(x−ty)dσ(y),(4.1)
Mtf(x) = 1
|Bd|

Bd
f(x−ty)dy = 1
|B(x,t )|

B(x,t)
f(y)dy,(4.2)
where Sd (resp. Bd) denotes the unit sphere (resp. the unit euclidean ball)⊆Rd,|Sd|(resp.
|Bd|) denotes the surface measure ofSd (resp. the Lebesgue measure ofBd) anddσ(y) (resp.
dy) denotes surface measure (resp. euclidean measure). The deﬁnitions (4.1) and (4.2) extend
literally to f ∈S(Rd)⊗Y when Y is a UMD lattice. They moreover extend by density to
f ∈Lp(Rd,Y ) once a priori boundedness of At and Mt on Lp(Rd,Y ) is clariﬁed. In this
section, we shall showq-variation results ofAt and Mt on Lp(Rd,Y ). We recall the following
results from the literature.
Theorem 4.1 1. (See [JSW, Theorem 1.4(i)]) Let2 < q <∞, d > 2, d
d−1 < p⩽ 2d and
f∈S(Rd). There exists a constantCp,q,d independent off such that
(4.3) ‖t↦→Atf‖Lp(Rd,Vq) ⩽Cp,q,d‖f‖Lp(Rd).
Moreover, if p > 2d and q > p
d, then (4.3) holds and conversely, if (4.3) holds, then
necessarilyq > p
d.
2. (See [BMSW, Theorem 1.3]) Let2 < q <∞, d > 1, 1 < p <∞and f∈S(Rd). There
exists a constantCp,q independent off and the dimensiond such that
(4.4) ‖t↦→Mtf‖Lp(Rd,Vq) ⩽Cp,q‖f‖Lp(Rd).
Moreover, the same result holds if the euclidean𝓁2
d ball in the deﬁnition(4.2) is replaced
by an𝓁r
d-ball with 1 ⩽r ⩽∞.
3. (See [HHL, Theorem 1.1]) Let2 < q <∞, d > 1, 1 < p <∞, Y a UMD lattice and
f∈S(Rd)⊗Y. Then there exists a constantCp,q,Y independent off and the dimension
d such that
(4.5) ‖t↦→Mtf‖Lp(Rd,Y (Vq)) ⩽Cp,q,Y‖f‖Lp(Rd,Y ).
We shall prove the following extension of (4.3) to the UMD lattice valued case. In order
(4.3) to hold, we had a minimal dimensiond > d1 = max
(
p
2, p
p−1, p
q
{
. In Theorem 4.2, we
also need some minimal dimension, but this time, it also depends on the geometry of the UMD
lattice.
15
Theorem 4.2 Let 2<q <∞, 1<p< ∞, Y be a UMD lattice and
(4.6) d>d 0 :=
2 + max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
1
2−max
(⏐⏐⏐1
p−1
2
⏐⏐⏐,
⏐⏐⏐1
pY
−1
2
⏐⏐⏐,
⏐⏐⏐1
qY
−1
2
⏐⏐⏐
{,
where pY ∈(1, 2] and qY ∈[2,∞) stand for the convexity and concavity exponents ofY (see
[LTz, Deﬁnition 1.d.3]). Letf∈S(Rd)⊗Y. Then there exists a constantCp,q,d,Y independent
of f such that
‖t↦→Atf‖Lp(Rd(Y (Vq))) ⩽Cp,q,d,Y‖f‖Lp(Rd,Y ).
Proof : The idea of the proof is the following. The operatorAt commutes with translations
in Rd, so is a Fourier multiplier associated to some symbolm : Rd→C. Since At is rotation
invariant, alsom is rotation invariant and thus,At is a spectral multiplier of the Laplacian−∆
on Rd (or its square root
√
−∆ ). For
√
−∆ , a Hörmander functional calculus onLp(Rd,Y )
space has been established in [Hy1, GiWe], see also [DKK]. So Theorem 3.3 is available. It will
then suﬃce to check the ﬁniteness of the norms of the speciﬁc spectral multiplier functionm
imposed in this Theorem 3.3.
In details, we haveAtf(x) =m(t
√
−∆)f(x) for
(4.7) m(λ) = 2π
λ
d−2
2
Jd−2
2
(2πλ),
where Jαdenotes the Bessel function of orderα[Graf, p. 577]. Indeed, withft(x) :=f(tx) for
f say, a Schwartz function,
Atf(x)
(4.1)
= 1
|Sd|

Sd
f(x−ty)dσ(y) = 1
|Sd|

Sd
ft
(1
tx−y
{
dσ(y)
= 1
|Sd|ft∗σ
(1
tx
{
= 1
|Sd|F−1[(ft)ˆˆσ]
(1
tx
{
[Graf,p. 577]
= F−1[(ft)ˆm]
(1
tx
{
=F−1[ ˆfm(t|·|)](x) =m(t
√
−∆)f(x).
We note the two following crucial formulae concerning the Bessel function:
sup
λ>0
√
λ|Jα(λ)|<∞
(
α>1
2
{
,(4.8)
d
dλ
(
λ−αJα(λ)
{
=−λ−αJα+1(λ)
(
α>1
2
{
,(4.9)
where we refer for (4.8) to [AAR, p. 238] and for (4.9) to [Graf, p. 573]. We next claim that for
c< d−1
2 , the spectral multiplier function satisﬁes the hypotheses of Theorem 3.3. First we note
that forχ0 aC∞function with support in(0, 4] and equal to1 on (0, 2],m(λ)χ0(λ) extends to
a C∞function on R [Graf, p. 577]. Thus,mχ0∈C1[0, 1] and m′χ0∈Hc−1
2 for anyc since m′
has bounded derivatives on intervals of ﬁnite length, to any order. To see this, note that the
functionλ−αJα(λ) isC∞on (0,∞) and continuous in0 being essentially the Fourier transform
of surface measure, with α= d−2
2 . Then so is also m. Now (4.9) yields d
dλ(λ−αJα(λ)) =
−λ(λ−(α+1)Jα+1(λ)). Thus, also m′is continuous in 0. Now using (4.9) withαreplaced by
16
α+ 1 shows that alsom′′is continuous in0. Repeating this argument by incrementingαstep
by step shows thatm′has bounded derivatives on intervals of ﬁnite length, to any order. In
particular, m(0) takes some ﬁnite value. We now estimate∑
n>0‖m(2n·)ϕ0‖Wc
2 (R) for (ϕn)n a
partition of unity ofR+. We have according to (4.9) and (4.8) forλ> 1
2
⏐⏐⏐⏐
d
dλm(λ)
⏐⏐⏐⏐=cλ−d−2
2
⏐⏐⏐Jd
2
(2πλ)
⏐⏐⏐≲λ−d−1
2 .
Moreover,
⏐⏐⏐⏐
d2
dλ2m(λ)
⏐⏐⏐⏐=c
⏐⏐⏐⏐
d
dλ
(
λλ−d
2Jd
2
(2πλ)
{⏐⏐⏐⏐
≲λ−d
2
⏐⏐⏐Jd
2
(2πλ)
⏐⏐⏐+λ−d−2
2
⏐⏐⏐Jd+2
2
(2πλ)
⏐⏐⏐
≲λ−d−1
2 .
In the same manner, one inductively shows, using (4.9) and (4.8) that forλ> 1
2 andk∈N, we
have
⏐⏐⏐dk
dλkm(λ)
⏐⏐⏐≲λ−d−1
2 . Therefore
( 2
1
2
⏐⏐⏐⏐
dk
dλk (m(2n·))|λ
⏐⏐⏐⏐
2
dλ
( 1
2
= 2nk
( 2
1
2
⏐⏐⏐⏐
dk
dλkm(2nλ)
⏐⏐⏐⏐
2
dλ
( 1
2
≲ 2nk
( 2
1
2
|2nλ|−2(d−1
2 )dλ
( 1
2
∼= 2nk2−nd−1
2 ,
which is summable overn > 0 provided thatk <d−1
2 . Moreover, by complex interpolation of
Wc
2 (R) spaces for non-integerc> 1
2 (see e.g. [DK, Corollary 3.11]), we obtain that forc< d−1
2 ,
we have∑
n>0‖m(2n·)ϕ0‖Wc
2 (R) <∞.
Now we want to apply Theorem 3.3. To this end, we recall that the operatorA =
√
−∆⊗IdY
has aHα
2 calculus onLp(Rd,Y ) provided that
α>d·α0(p,Y ) + 1
2,
whereα0(p,Y ) = max
(⏐⏐⏐1
p−1
2
⏐⏐⏐,
⏐⏐⏐1
pY
−1
2
⏐⏐⏐,
⏐⏐⏐1
qY
−1
2
⏐⏐⏐
{
∈[0, 1
2),pY ∈(1, 2] andqY ∈[2,∞) stand
for the non-trivial convexity and concavity exponents of the UMD latticeY. See [DKK, Remark
4.24] ﬁrst withA =−∆ , and then noting (withβ= 1
2) thatAβhas the sameHα
2 calculus as
A for anyβ >0, sincem↦→m((·)β) is an isomorphismHα
2 →Hα
2. Moreover, exp(−t
√
−∆)
is well-known to be lattice positive and contractive onLp(Rd). Combining the constraint on
c above coming from the spectral multiplier, the constraint onαabove and the constraint
c>α+ max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 1 from Theorem 3.3, we deduce from Theorem 3.3
the ﬁniteq-variation
‖t↦→Atf‖Lp(Rd,Y (Vq)) =‖t↦→m(t
√
−∆)f‖Lp(Rd,Y (Vq)) ≲‖f‖Lp(Rd,Y ),
17
provided that we have
c< d−1
2 ,
α>dα0(p,Y ) + 1
2,
c>α+ max
(1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 1.
Thecombinationofthethreeispossibleif d−1
2 >dα0(p,Y )+ 1
2+max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+
1 so ifd·
(1
2−α0(p,Y )
{
> 1
2 + 1
2 + max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
+ 1, in other words if
d>d 0 :=
2 + max
(
1
2, 1
typeLp(Y )− 1
cotypeLp(Y )
{
1
2−max
(⏐⏐⏐1
p−1
2
⏐⏐⏐,
⏐⏐⏐1
pY
−1
2
⏐⏐⏐,
⏐⏐⏐1
qY
−1
2
⏐⏐⏐
{.
Note that the denominator of d0 is strictly positive since Y has non-trivial concavity and
convexity exponents, being a UMD lattice [RdF, Corollary p. 216], [TJ, p. 218-219].
Remark 4.3 Theorem 4.2 immediately extends to the same result for the ball meansMt from
(4.2) in place of the spherical meansAt, with the same constraint on the minimal dimension
d0. That is, for d > d0 with d0 from (4.6), we have for anyf∈S(Rd)⊗Y with a constant
Cp,q,d,Y independent off that
‖t↦→Mtf‖Lp(Rd(Y (Vq))) ⩽Cp,q,d,Y‖f‖Lp(Rd,Y ).
Indeed, by Fubini we can writeMtf(x,ω) = d
td
t
0rd−1Arf(x,ω)dr. Thus, for (x,ω)∈Rd×Ω′
ﬁxed, we have
‖t↦→Mtf(x,ω)‖Vq =d
‖‖‖‖t↦→t−d
 t
0
rd−1Arf(x,ω)dr
‖‖‖‖
Vq
=d
‖‖‖‖t↦→
 t
0
(r
t
{d
Arf(x,ω)dr
r
‖‖‖‖
Vq
=d
‖‖‖‖t↦→
 1
0
rdArtf(x,ω)dr
r
‖‖‖‖
Vq
⩽d
 1
0
rd‖t↦→Artf(x,ω)‖Vq
dr
r
=d
 1
0
rd‖t↦→Atf(x,ω)‖Vq
dr
r
=d1
d‖t↦→Atf(x,ω)‖Vq.
Here we have used in the last but one step that theVq norm is dilation invariant, that is,
‖t↦→art‖Vq =‖t↦→at‖Vq for r > 0. This can be seen directly from the Deﬁnition 3.1 of
the q-variation. To conclude, it suﬃces to takeLp(Rd,Y ) norms in the above inequality and to
apply Theorem 4.2.
At the end of this section, we reprove (4.5) for large dimensions, by the alternative proof of
using ourq-variational Hörmander Functional Calculus Theorem 3.3.
18
Proposition 4.4 LetY be a UMD lattice. Let2<q <∞, 1<p< ∞and d>d 0 from (4.6).
Then there exists a constantCp,q,Y such that for anyf∈S(Rd)⊗Y, we have
‖t↦→Mtf‖Lp(Rd,Y (Vq)) ⩽Cp,q,Y‖f‖Lp(Rd,Y ).
Proof : The proof is based on the dimensiondependent estimate of theq-variation oft↦→At
from Theorem 4.2, together with the method of descent in the spirit of the Calderón-Zygmund
method of rotations that we already employed in [DeKr2]. We introduce the following further
mean operators ford′,d,k ∈N, t> 0, θ∈O(d) an orthogonal mapping andf∈S(Rd):
Ad,k,tf(x) =

|y|⩽tf(x−y)|y|kdy

|y|⩽t|y|kdy
Aθ
d′,tf(x) =

|yd′|⩽tf(x−θ(yd′, 0))|yd′|d−d′
dyd′

|yd′|⩽t|yd′|d−d′
dyd′
.
Here we writey = (yd′,yd−d′)∈Rd = Rd′
×Rd−d′
. Again, Ad,k,t and Aθ
d′,t admit obvious
extensions to f ∈S(Rd)⊗Y. Then, for such an f and (x,ω)∈Rd×Ω′ﬁxed, we obtain
similarly to Remark 4.3
‖t↦→Ad,k,tf(x,ω)‖Vq =cd
‖‖‖‖t↦→t−(d+k)
 t
0
rd−1rkArf(x,ω)dr
‖‖‖‖
Vq
= (d +k)
‖‖‖‖t↦→
 t
0
(r
t
{d+k
Arf(x,ω)dr
r
‖‖‖‖
Vq
= (d +k)
‖‖‖‖t↦→
 1
0
rd+kArtf(x,ω)dr
r
‖‖‖‖
Vq
⩽ (d +k)
 1
0
rd+k‖t↦→Artf(x,ω)‖Vq
dr
r
⩽‖t↦→Atf(x,ω)‖Vq.(4.10)
Next we show that forf∈S(Rd),
(4.11) AId
d′,tf(x) =Ad′,d−d′,t
(
f◦gxd−d′
{
(xd′),
where
gxd−d′: Rd′
→Rd, xd′↦→(xd′,xd−d′).
We have
AId
d′,tf(x) =

|yd′|⩽tf(x−(yd′, 0))|yd′|d−d′
dyd′

|yd′|⩽t|yd′|d−d′
dyd′
=

|yd′|⩽tf◦gxd−d′(xd′−yd′)|yd′|d−d′
dyd′

|yd′|⩽t|yd′|d−d′
dyd′
=Ad′,d−d′,t
(
f◦gxd−d′
{
(xd′),
which shows (4.11). We further note from [DeKr2, (7)],
(4.12) Mtf(x) =

O(d)
Aθ
d′,tf(x)dµ(θ),
19
where dµdenotes the normalized Haar measure of the compact groupO(d). Thus, we obtain
forf∈S(Rd)⊗Y, whereAt denotes this time the spherical mean from (4.1), but in dimension
d′<d ,
‖‖t↦→Mtf(x,ω)‖Vq‖Lp(Rd,Y )
(4.12)
=
‖‖‖‖‖
‖‖‖‖‖t↦→

O(d)
Aθ
d′,tf(x,ω)dµ(θ)
‖‖‖‖‖
Vq
‖‖‖‖‖
Lp(Rd,Y )
=
‖‖‖‖‖‖‖
‖‖‖‖‖‖‖
t↦→

O(d)
AId
d′,t(f◦θ)/rcehtipupleft/rcehtipdownright/rcehtipdownleft/rcehtipupright
=: ˜f
◦θ−1(x,ω)dµ(θ)
‖‖‖‖‖‖‖
Vq
‖‖‖‖‖‖‖
Lp(Rd,Y )
⩽

O(d)
‖‖‖
‖‖t↦→AId
d′,t ˜f(·,ω)
‖‖
Vq◦θ−1
‖‖‖
Lp(Rd,Y )
dµ(θ)
(4.11)
=

O(d)
‖‖‖‖
‖‖‖
‖‖‖t↦→Ad′,d−d′,t
(
˜f◦gxd−d′
{
(xd′,ω)
‖‖‖
Vq
‖‖‖
Lp(Rd′,Y )
‖‖‖‖
Lp(Rd−d′)
dµ(θ)
(4.10)
⩽

O(d)
‖‖‖‖
‖‖‖
‖‖‖t↦→At
(
˜f◦gxd−d′
{
(xd′,ω)
‖‖‖
Vq
‖‖‖
Lp(Rd′,Y )
‖‖‖‖
Lp(Rd−d′)
dµ(θ)
Theorem 4.2
⩽ Cp,q,d′,Y

O(d)
‖‖‖‖
‖‖‖
(
˜f◦gxd−d′
{
(xd′,ω)
‖‖‖
Lp(Rd′,Y )
‖‖‖‖
Lp(Rd−d′)
dµ(θ)
=Cp,q,d′,Y

O(d)
‖˜f‖Lp(Rd,Y )dµ(θ)
=Cp,q,d′,Y‖f‖Lp(Rd,Y ).
Here we have applied Theorem 4.2 with dimensiond′> d0 from (4.6). Thus the proposition
follows ford >d′>d 0.
