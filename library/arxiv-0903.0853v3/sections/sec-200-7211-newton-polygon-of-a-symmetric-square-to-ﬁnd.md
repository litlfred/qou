---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-200-7211-newton-polygon-of-a-symmetric-square-to-ﬁnd
section_title: "Newton polygon of a symmetric square . — To ﬁnd the equation"
section_number: 7.2.1.1
pages: 125-127
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
satisﬁed by a product of two functions, one uses the tensor pr oduct of two
systems or modules; for a square, one uses likewise the symme tric square.
LetM = (V, Φ) be aq-diﬀerence module andT 2M :=M⊗M = (V⊗V, Φ⊗
Φ) its tensor square. The linear automorphism x⊗y↦→y⊗x commutes with
Φ⊗ Φ, so that it actually deﬁnes an involutive q-diﬀerence automorphism of
M⊗M, and a splitting:
T 2M =S2M⊕ Λ2M.
IfM has slopes µ1,...,µ k with multiplicities r1,...,r k, then T 2M has slopes
the µi +µj , 1 ≤ i,j ≤ k with multiplicities the rirj. (Of course, if many
sumsµi +µj are equal, the corresponding multiplicities rirj should be added;
the same remark will hold for the following computations.) S aid otherwise,
the slopes of T 2M are the 2µi, 1≤ i≤ k with multiplicities the r2
i ; and the
µi +µj , 1≤i<j ≤k with multiplicities the 2rirj.
The repartition of these slopes (breaking of the Newton poly gon) among
the symmetric and exterior square is as follows:
– S2M has slopes the 2 µi, 1 ≤ i≤ k with multiplicities the r2
i +ri
2 ; and
the µi +µj , 1≤i<j ≤k with multiplicities the rirj.
– Λ 2M has slopes the 2 µi, 1 ≤ i≤ k with multiplicities the r2
i−ri
2 ; and
the µi +µj , 1≤i<j ≤k with multiplicities the rirj.
If there are two slopes µ < ν, with multiplicities r,s, no confusion of sums
µi +µj can arise, and we ﬁnd:
– T 2M has slopes 2µ<µ +ν <2ν, with multiplicities r2, 2rs,s 2;
– S2M has the same slopes, with multiplicities r2 +r
2 ,rs, s2 +s
2 ;
– Λ 2M has the same slopes, with multiplicities r2−r
2 ,rs, s2−s
2 ·
120 CHAPTER 7. EXAMPLES OF THE STOKES PHENOMENON
We now take M0 =
(a 0
0 bz
)
and M =
(a u
0 bz
)
, where a,b ∈ C∗ and
u∈ C({z}). The symmetric squares admit an obvious choice of basis and
corresponding matrices:
N0 =


a2 0 0
0 abz 0
0 0 b2z2

 and N =


a2 2au u 2
0 abz ubz
0 0 b2z2

.
If F =
(1 f
0 1
)
is such that F[M0] = M, then we have G[N0] = N with G
given by:
G =S2F =


1 2 f f 2
0 1 f
0 0 1

.
Actually, if one does not cheat, when looking for G =


1 f1 f2
0 1 f3
0 0 1

 such that
G[N0] =N, one has to solve the system:
abzσqf1 =a2f1 + 2au,
b2z2σqf2 =a2f2 + 2auf3 +u2,
b2z2σqf3 =abzf3 +ubz.
Since we know from start that bzσqf = af +u, we see that f1 := 2f and
f3 := f respectively solve the ﬁrst and third equation; then, we ﬁnd that
f2 :=f 2 solve the second equation.
Using the system above, we ﬁnd a second order inhomogeneous e quation
for f2 alone as follows:
(bzσq−a) 1
2au (b2z2σq−a2)f2 = (bzσq−a)f3 + (bzσq−a) u2
2au =⇒
( bz
σq(u)σq− a
u
)
(b2z2σq−a2)f2 =bzσq(u) +au.
We leave to the reader to ﬁnd a simpler form, as well as the corr esponding
third order homogeneous equation. At any rate, in the case th at u ∈ C
(Birkhoﬀ-Guenther normal form) we have:
(bzσq−a) (b2z2σq−a2)f2 =bz +a.
