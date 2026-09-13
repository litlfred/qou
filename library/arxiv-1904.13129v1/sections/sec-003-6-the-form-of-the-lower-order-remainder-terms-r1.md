---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-003-6-the-form-of-the-lower-order-remainder-terms-r1
section_title: "The form of the lower order remainder terms R1 and R2"
section_number: 6
pages: 14-23
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
---
1 and Rα
2
We show that the orthogonal projection of the truncated rema inder terms of the
decomposition of δE α found in Section 3 can be expressed as multiple integrals of
analytic functions.
Let 0 < ε≤ 1
2 , x ∈ [0, 1] and γ ∈ C∞(R/Z, Rn) be a simple closed arc-length
parametrized curve. We recall that the truncated remainder terms are given by
(Rα,ε
1 γ)(x) =
∫
|w|∈[ε, 1
2 ]
(γ(x +w) −γ(x) −w ˙γ(x))
( 1
|γ(x +w) −γ(x)|α+2 − 1
|w|α+2
)
dw,
(Rα,ε
2 γ)(x) =
∫
|w|∈[ε, 1
2 ]
¨γ(x)
( 1
|γ(x +w) −γ(x)|α − 1
|w|α
)
dw.
We begin with transforming the more elementary part P ⊥
˙γ Rα,ε
2 γ.
Theorem 6.1. The term P ⊥
˙γ Rα,ε
2 γ can be re-written as multiple integral of the
form
(P ⊥
˙γ Rε
2γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(s1 −s2)2Gα
2 (γ)(x)dφ1dφ2ds1ds2
dw
|w|α−2,
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 15
where
Gα
2 (γ)(x) = Gα
2 (γ)(x;s1,s 2,φ 1,φ 2,w )
=Gα
2
(∫ 1
0
˙γ(x +tw)dt, ˙γ(x), ¨γ(x +s2w + (s1 −s2)φ1w),
¨γ(x +s2w + (s1 −s2)φ2w), ¨γ(x)
)
for some analytic function Gα
2 : Rn \ {0, 1} × R4n → Rn.
Proof. We begin by computing the ﬁrst term in the integrand of Rα,ε
2 γ. To do so
we use the fundamental theorem of calculus and the arc-lengt h parametrization of
the curve γ (as in the proof of [ BR13, Prop. 3.2]) to get
1
|γ(x +w) −γ(x)|α − 1
|w|α
= |w|α
|γ(x +w) −γ(x)|α
1 − |γ(x+w)−γ(x)|α
|w|α
1 − |γ(x+w)−γ(x)|2
w2
1 − |γ(x+w)−γ(x)|2
w2
|w|α
=gα
2
(∫ 1
0
˙γ(x +tw)dt
) 2
(
1 − |γ(x+w)−γ(x)|2
w2
)
|w|α
=gα
2
(∫ 1
0
˙γ(x +tw)dt
) ∫∫
[0,1]2 | ˙γ(x +s1w) − ˙γ(x +s2w)|2ds1ds2
|w|α , (6.1)
where gα
2 (x) = 1
2|x|α
1−|x|α
1−|x|2 for all x ∈ Rn \ {0, 1} is analytic away from the origin.
Since we have by the fundamental theorem of calculus
| ˙γ(x +s1w) − ˙γ(x +s2w)|2
w2 =
∫ 1
0
∫ 1
0
(s1 −s2)2
× ⟨¨γ(x +s2w + (s1 −s2)φ1w), ¨γ(x +s2w + (s1 −s2)φ2w)⟩Rn dφ1dφ2, (6.2)
we can express Rα,ε
2 γ as
(Rα,ε
2 γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(s1 −s2)2
× ~Gα
2
(∫ 1
0
˙γ(x +tw)dt, ¨γ(x +s2w + (s1 −s2)φ1w),
¨γ(x +s2w + (s1 −s2)φ2w), ¨γ(x)
)
dφ1dφ2ds1ds2
dw
|w|α−2,
where ~Gα
2 : Rn \ {0, 1} × R3n → Rn deﬁned by ~Gα
2 (a,x,y,z ) := gα
2 (a) ⟨x,y ⟩Rnz is
an analytic function away from the origin in the ﬁrst variabl e as well. If we apply
the orthogonal projection P ⊥
˙γ onRα,ε
2 γ, we ﬁnally get the following representation
(P ⊥
˙γ Rα,ε
2 γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(s1 −s2)2Gα
2 (γ)(x)dφ1dφ2ds1ds2
dw
|w|α−2,
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 16
where
Gα
2 (γ)(x) = Gα
2 (γ)(x;s1,s 2,φ 1,φ 2,w )
=Gα
2
(∫ 1
0
˙γ(x +tw)dt, ˙γ(x), ¨γ(x +s2w + (s1 −s2)φ1w),
¨γ(x +s2w + (s1 −s2)φ2w), ¨γ(x)
)
and Gα
2 : Rn \ {0, 1} × R4n → Rn given by Gα
2 (a,v,x,y,z ) := P ⊥
v ~Gα
2 (a,x,y,z ) is
clearly analytic. □
We use the previous computations to rewrite the orthogonal p rojection of the
ﬁrst remaining part.
Theorem 6.2. The term P ⊥
˙γ Rα,ε
1 γ can be re-written as multiple integral of the
form
(P ⊥
˙γ Rε
1γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2Gα
1 (γ)(x)dψ1dψ2dr1dr2
dw
|w|α−2,
where
Gα
1 (γ)(x) = Gα
1 (γ)(x;r1,r 2,ψ 1,ψ 2,w )
=Gα
1
(∫ 1
0
˙γ(x +sw)ds, ˙γ(x), ¨γ(x +r2w + (r1 −r2)ψ1w),
¨γ(x +r2w + (r1 −r2)ψ2w),
∫ 1
0
¨γ(x +tw)(1 −t)dt
)
for some analytic function Gα
1 : Rn \ {0, 1} × R4n → Rn.
Proof. By the integral form of the remainder of a ﬁrst order Taylor ap proximation,
we compute the integrand of Rα,ε
1 γ as
(γ(x +w) −γ(x) −w ˙γ(x))
( 1
|γ(x +w) −γ(x)|α+2 − 1
|w|α+2
)
=w2
∫ 1
0
¨γ(x +tw)(1 −t)dt
( 1
|γ(x +w) −γ(x)|α+2 − 1
|w|α+2
)
=
∫ 1
0
¨γ(x +tw)(1 −t)dt
( w2
|γ(x +w) −γ(x)|α+2 − 1
|w|α
)
. (6.3)
Thus the last term in ( 6.3) can be expressed as
w2
|γ(x +w) −γ(x)|α+2 − 1
|w|α
= |w|α+2
|γ(x +w) −γ(x)|α+2

 1 − |γ(x+w)−γ(x)|α +2
|w|α +2
|w|α


= |w|α+2
|γ(x +w) −γ(x)|α+2
1 − |γ(x+w)−γ(x)|α +2
|w|α +2
1 − |γ(x+w)−γ(x)|2
|w|2

 1 − |γ(x+w)−γ(x)|2
|w|2
|w|α


=gα
1
(∫ 1
0
˙γ(x +sw)ds
) 
 1 − |γ(x+w)−γ(x)|2
|w|2
|w|α

, (6.4)
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 17
where gα
1 (x) = 1
2|x|α +2
1−|x|α +2
1−|x|2 for all x ∈ Rn \ {0, 1} is analytic away from the
origin. By transfering the computations in ( 6.1) and ( 6.2) to the last term in ( 6.4)
we ﬁnd that
(Rα,ε
1 γ)(x)
=
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2
×~Gα
1
(∫ 1
0
˙γ(x +sw)ds, ¨γ(x +r2w + (r1 −r2)ψ1w),
¨γ(x +r2w + (r1 −r2)ψ2w),
∫ 1
0
¨γ(x +tw)(1 −t)dt
)
dψ1dψ2dr1dr2dw,
where ~Gα
1 : Rn \ {0, 1} × R3n → Rn deﬁned by ~Gα
1 (a,x,y,z ) := gα
1 (a) ⟨x,y ⟩Rnz is
analytic away from 0 and 1 in the ﬁrst variable.
Finally, by applying the orthogonal projection to Rα,ε
1 γ, we obtain
(P ⊥
˙γ Rα,ε
1 γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2Gα
1 (γ)(x)dψ1dψ2dr1dr2dw,
where
Gα
1 (γ)(x) = Gα
1 (γ)(x;r1,r 2,ψ 1,ψ 2,w )
=Gα
1
(∫ 1
0
˙γ(x +sw)ds, ˙γ(x), ¨γ(x +r2w + (r1 −r2)ψ1w),
¨γ(x +r2w + (r1 −r2)ψ2w),
∫ 1
0
¨γ(x +tw)(1 −t)dt
)
and Gα
1 : Rn \ {0, 1} × R4n → Rn given by Gα
1 (a,v,x,y,z ) := P ⊥
v ~Gα
2 (a,x,y,z ) is
obviously analytic. □
7. Proof of the main theorem by Cauchy’s method of majorants
We now turn to the proof of Theorem 1.2. Our strategy is to ﬁrst establish a
recursive estimate for ‖∂lγ‖Hα − 1 from which we can infer, by Cauchy’s method of
majorants, the analyticity of the curve γ.
Let m := 1 > 1
2 and γ = (γ1,...,γ n) : R/Z → Rn be a simple closed arc-length
parametrized curve that is in the class C∞(R/Z, Rn). If γ is a critical point of
E α +λL, i.e. if we have
δE α(γ;h) +λ
∫
R/Z
⟨˙γ, ˙h⟩dx = 0
for all h ∈H
α +1
2 ,2(R/Z, Rn), then Theorem 3.1 and integration by parts imply that
the curve γ solves the Euler-Lagrange equation
(H αγ +λ¨γ,h )L2([0,1],Rn) = 0
for all h ∈ H
α +1
2 ,2(R/Z, Rn). Thus by the decompositions ( 3.1) and ( 3.2) of the
gradient of O’Hara’s knot energies, we conclude that
H αγ =αP ⊥
˙γ Qαγ + 2αP ⊥
˙γ Rα
1γ − 2P ⊥
˙γ Rα
3γ +λ¨γ ≡ 0
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 18
on R/Z. Moreover, by Corollary 4.2 with β := α − 2 ∈ (0, 1) and the triangle
inequality, it follows for any integer l ≥ 0 that
‖∂l+3γ‖H1+β ≤ ~C‖∂lQαγ‖H1
= ~C
‖‖∂l(
αP T
˙γ Qαγ − 2αP ⊥
˙γ Rα
1γ + 2P ⊥
˙γ Rα
2γ −λ¨γ
) ‖‖
H1
≤ 6~C(‖∂lP T
˙γ Qαγ‖H1 + ‖∂lP ⊥
˙γ Rα
1γ‖H1
+ ‖∂lP ⊥
˙γ Rα
3γ‖H1 +λ‖∂l+2γ‖H1 ). (7.1)
In order to get a recursive estimate on ‖∂lγ‖H1+β we aim to derive suitable estimates
for the ﬁrst three terms on the right-hand side of ( 7.1). To do so for the tangential
part of Qα, we use the fractional Leibniz rule from Section 5 in the following:
Lemma 7.1. Let l ∈ N0, β :=α − 2 ∈ (0, 1) for some 2< α <3 and 0< ε≤ 1
2 .
Then there exists a positive constant CQα independent of ε, γ and l such that
‖∂lP T
˙γ Qα,εγ‖H1
≤CQα
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H1+β ‖∂k1−k2+2γ‖H1+β ‖∂k2+1γ‖H1.
Proof. Using formula ( 5.2) and the Leibniz rule twice yields
∂l
(
P T
˙γ Qα,εγ(x)
)
=∂l
(
2
∫
|w|∈[ε, 1
2 ]
∫∫
[0,1]2
(1 −t)(−t) ⟨¨γ(x +tw), ¨γ(x +stw)⟩Rn
w|w|α−2 ˙γ(x)dsdtdw
)
= 2
∫
|w|∈[ε, 1
2 ]
∫∫
[0,1]2
(1 −t)(−t)∂l
(⟨¨γ(x +tw), ¨γ(x +stw)⟩Rn
w|w|β ˙γ(x)
)
dsdtdw
= 2
∫
|w|∈[ε, 1
2 ]
∫∫
[0,1]2
(1 −t)(−t)
×
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
) ⟨
∂l−k1+2γ(x +tw),∂ k1−k2+2γ(x +stw)
⟩
Rn
w|w|β ∂k2+1γ(x)dsdtdw
= 2
∫∫
[0,1]2
(1 −t)(−t)
×
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
) n∑
k=1
H ε
t,st,β(∂l−k1+2γk,∂ k1−k2+2γk)(x)∂k2+1γ(x)dsdt,
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 19
where the smoothness of the integrand allows interchanging of integrals and deriv-
ative. Then for all 1 ≤m ≤n we obtain the component-wise estimate
‖∂l(P T
˙γ Qα,εγ)m‖H1
≤ 2
∫∫
[0,1]2
|1 −t||t|
×
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
) n∑
k=1
C1‖H ε
t,st,β(∂l−k1+2γk,∂ k1−k2+2γk)‖H1 ‖∂k2+1γm‖H1 dsdt
≤ 2C1
∫∫
[0,1]2
|1 −t||t|
×
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
) ( n∑
k=1
CH ‖∂l−k1+2γk‖H1+β ‖∂k1−k2+2γk‖H1+β
)
‖∂k2+1γm‖H1dsdt
≤ 2C1CH
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H1+β ‖∂k1−k2+2γ‖H1+β ‖∂k2+1γm‖H1
(7.2)
via the Banach algebra property ( 2.1) of H 1 and the fractional Leibniz rule for each
of the components (i.e. Theorem 5.3). The desired statement follows from ( 7.2) and
the equivalence between the 1-norm and the 2-norm with a ﬁnite positive constant
CQα := 2C1CH
√n. □
Next we estimate the orthogonal projection of the truncated remaining parts
Rα,ε
1 γ andRα,ε
2 γ. The important ingredients for this are the forms of P ⊥
˙γ Rα,ε
1 γ and
P ⊥
˙γ Rα,ε
2 γ derived in Chapter 6, Faà di Bruno’s formula and the Banach algebra
property of H 1.
Lemma 7.2. Letl ∈ N0, 2<α< 3, and consider the mapping f = (f1,...,f 5n) :
R/Z → Rn \ {0, 1} × R4n given by
f (x) := ( ˙γ(x), ˙γ(x), ¨γ(x), ¨γ(x), ¨γ(x)).
Then there exist positive constants CRα
1 andr independent ofε,γ andl such that the
universal polynomials p(5n)
l from the multivariate form of Faà di Bruno’s formula.
(2.2) satisfy
‖∂lP ⊥
˙γ Rα,ε
1 γ‖H1 ≤CRα
1p(5n)
l
({(|η| + 1)!
r|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
,
whereC1 is the constant from the estimate (2.1) with m = 1.
Proof. By Theorem 6.2 we can express P ⊥
˙γ Rα,ε
1 γ as
(P ⊥
˙γ Rα,ε
1 γ)(x) =
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2Gα
1 (f1(x))dψ1dψ2dr1dr2
dw
|w|α−2
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 20
where Gα
1 : Rn \ {0, 1} × R4n → Rn is an analytic function and
f1(x) :=


∫ 1
0 ˙γ(x +sw)ds
˙γ(x)
¨γ(x +r2w + (r1 −r2)ψ1w)
¨γ(x +r2w + (r1 −r2)ψ2w))∫ 1
0 ¨γ(x +tw)dt


.
Due to the smoothness of the integrand and the generalized Fa à di Bruno’s formula
(2.2), we component-wise ﬁnd for all 1 ≤k ≤ 5n that
∂l(P ⊥
˙γ Rα,ε
1 γ)k(x)
=∂l
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2Gα
1,k(f1(x))dψ1dψ2dr1dr2
dw
|w|α−2
=
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2∂lGα
1,k(f1(x))dψ1dψ2dr1dr2
dw
|w|α−2
=
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
(r1 −r2)2
×p(5n)
l
(
{(∂ηGα
1 )k(f1(x))}|η|≤l, {f (j)
1,i (x)}1≤i≤5n
1≤j≤l
)
dψ1dψ2dr1dr2
dw
|w|α−2.
Moreover, by applying the H 1-norm on ∂l(P ⊥
˙γ Rα,ε
1 γ) component-wise for any 1 ≤
k ≤ 5n, we ﬁnd via the Banach algebra property of H 1 that
‖∂l(P ⊥
˙γ Rα,ε
1 γ)k‖H1
≤
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
|r1 −r2|2
×
‖‖‖p(5n)
l
(
{(∂ηGα
1 )k(f1)}|η|≤l, {f (j)
1,i }1≤i≤5n
1≤j≤l
) ‖‖‖
H1
dψ1dψ2dr1dr2
dw
|w|α−2
≤
∫
|w|∈[ε, 1
2 ]
∫∫∫∫
[0,1]4
|r1 −r2|2
×p(5n)
l
(
{‖(∂ηGα
1 )k(f1)‖H1 }|η|≤l, {C1‖f (j)
1,i ‖H1 }1≤i≤5n
1≤j≤l
)
dψ1dψ2dr1dr2
dw
|w|α−2,
where the constant C1 appears only in front of ‖f (j)
1,i ‖H1 because of the one-
homogeneity of p(5n)
l in its ﬁrst components.
For any 1 ≤j ≤l we also observe that ‖f (j)
1,k‖H1 ≤ ‖f (j)
k ‖H1 whenever 1 ≤k ≤n,
4n+1 ≤k ≤ 5n and that ‖f (j)
1,k‖H1 = ‖f (j)
k ‖H1 whenevern+1 ≤k ≤ 4n. Moreover,
‖f (j)
k ‖H1 does not depend on any of the parameters w,ψ i,r i,s,t for all 1 ≤k ≤ 5n
and 1 ≤ j ≤ l. In addition, since Gα
1 is an analytic function, we can deduce from
the proof of [ BV19, Theor. 7.2] that
‖(∂ηGα
1 )(f1)‖H1 ≤ ~CRα
1
(|η| + 1)!
r|η|+1
for some positive constant ~CRα
1 independent of ε,γ and l.
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 21
Now using the elementary estimate
∫
|w|∈[ε, 1
2 ]
dw
|w|α − 2 ≤ 2
3−α < ∞ since 2<α< 3
and the fact that p(5n)
l is one-homogeneous in the ﬁrst components, we ﬁnally obtain
‖∂l(P ⊥
˙γ Rε
1γ)‖H1 ≤CRα
1 p(5n)
l
({(|η| + 1)!
r|η|+1
}
|η|≤l
,
{
‖C1f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
,
where CRα
1 := ~CRα
1
2
3−α is ﬁnite and the right-hand side is independent of ε. □
The orthogonal projection of the second remainder term can b e estimated along
the lines of the previous Lemma 7.2 to get the following:
Lemma 7.3. Letl ∈ N0 and f = ( ˙γ, ˙γ, ¨γ, ¨γ, ¨γ) as in Lemma 7.2. Then there exist
positive constants CRα
2 and s that are independent of ε, γ and l such that
‖∂lP ⊥
˙γ Rα,ε
2 γ‖H1 ≤CRα
2 p(5n)
l
({(|η| + 1)!
s|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
,
wherep(5n)
l is the same universal polynomial as in Lemma 7.2.
As a direct consequence of the proof of [ BV19, Theor. 7.4] the estimates from
Lemmas 7.1, 7.2 and 7.3 also hold for the limit case ε ↓ 0.
Theorem 7.4. Let l ∈ N0 and f = ( ˙γ, ˙γ, ¨γ, ¨γ, ¨γ) as in Lemma 7.2. Then there
exist positive constants r, s, CQα , CRα
1 and CRα
2 which are independent of γ and l
such that
‖∂lP T
˙γ Qαγ‖H1 ≤CQα
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H1+β ‖∂k1−k2+2γ‖H1+β ‖∂k2+1γ‖H1
‖∂lP ⊥
˙γ Rα
1γ‖H1 ≤CRα
1 p(5n)
l
({(|η| + 1)!
r|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
‖∂lP ⊥
˙γ Rα
2γ‖H1 ≤CRα
2 p(5n)
l
({(|η| + 1)!
s|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
,
where β := α − 2 for some 2 < α <3 and p(5n)
l is the universal polynomial from
Lemma 7.2.
We are now in a position to give the proof of the main theorem.
Proof of Theorem 1.2. Letβ =α−2 for 2<α< 3. Now suppose γ = (γ1,...,γ n) :
R/Z → Rn is a closed simple arc-length parametrized curve in the clas sC∞(R/Z, Rn)
which is a stationary point of E α +λL. Using the smoothness of the curve γ, we
introduce an auxiliary function f : R/Z → R5n given by
f (x) := ( ˙γ(x), ˙γ(x), ¨γ(x), ¨γ(x), ¨γ(x))
and deﬁne
al :=C1‖∂lf ‖H1+β
for all integers l ≥ 0. If we can establish the existence of ﬁnite positive constan tsδ
and Cγ such that
al ≤Cγ
l!
δl
we immediately obtain the analyticity of the curve γ on R/Z by Corollary 2.3.
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 22
In order to obtain the desired bounds on al we ﬁrst note that there exists a
positive constant ˜C such that
‖∂l+3γ‖H1+β ≤ ~C
(
‖∂lP T
˙γ Qαγ‖H1 + ‖∂lP ⊥
˙γ Rα
1γ‖H1
+ ‖∂lP ⊥
˙γ Rα
3γ‖H1 +λ‖∂l+2γ‖H1
)
by the criticality of the curve γ, the ﬁrst variation formula of E α of Theorem 3.1,
our decomposition of the ﬁrst variation of E α +λL and Corollary 4.2. Next we
deduce from Theorem 7.4 and the Sobolev embedding of H 1+β ⊆H 1 that
al+1 =C1‖∂l+1f ‖H1+β
≤C1(3‖∂l+3γ‖H1+β + 2‖∂l+2γ‖H1+β )
≤ 3~CC1
[
‖∂lP T
˙γ Qαγ‖H1 + ‖∂lP ⊥
˙γ Rα
1γ‖H1
+ ‖∂lP ⊥
˙γ Rα
2γ‖H1 +λ‖∂l+2γ‖H1
]
+ 2C1al
≤ 3~CC1
[
CQα
l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H1+β ‖∂k1−k2+2γ‖H1+β ‖∂k2+1γ‖H1
+CRα
1p(5n)
l
({(|η| + 1)!
r|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
+CRα
2p(5n)
l
({(|η| + 1)!
s|η|+1
}
|η|≤l
,
{
C1‖f (j)
i ‖H1
}
1≤i≤5n
1≤j≤l
)
+λ‖∂l+2γ‖H1
]
+ 2C1al.
Therefore, by the embedding of H 1+β ⊆ H 1 again, there exist positive constants
C >1 and rγ independent of γ and l such that
al+1 ≤C
[ l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
al−k1ak1−k2ak2
+p(5n)
l
({(|η| + 1)!
r|η|+1
γ
}
|η|≤l
,
{
aj
}
1≤j≤l
)
+al
]
. (7.3)
To apply Cauchy’s method of majorants, we deﬁne a majorant F : R5n → R5n
component-wise by setting
Fi(y) := C
(
y3
i + 1
(1 + 5na0−(y1+···+y5n)
rγ
)2
+yi
)
for any y = (y1,...,y 5n) ∈ R5n and all 1 ≤ i ≤ 5n. It is clearly analytic around
a0(1,..., 1). Moreover, we consider the following initial value problem
˙c(t) = F (c(t)),
c(0) = a0(1,..., 1). (7.4)
and note that the ODE has a unique smooth solution c : (−ε,ε ) → R5n that is also
analytic around 0 for some ε> 0 by Theorem 2.4. Hence we can write c =c(t) as
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 23
a Taylor series in a neighbourhood of 0, i.e.
c(t) :=
∞∑
k=0
~ak(1,..., 1)
k! tk
where ~ak(1,..., 1) = c(k)(0). Then by Theorem 2.1 we can, for all t ∈ Brc(0),
bound
|c(l)(t)| ≤ M l!
rlc
(7.5)
for some ﬁnite positive constants rc and M which are independent of any integer
l ≥ 0. By applying the Leibniz rule and Faà di Bruno’s formula ( 2.2) we have that
∂lFi(c(t))
=C
[ l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
c(l−k1)
i (t)c(k1−k2)
i (t)c(k2)
i (t)
+p(5n)
l
({(|η| + 1)!
r|η|+1
γ
1
(
1 +
(
5na0
rγ
− (c1(t)+···+c5n(t))
rγ
)) |η|+2
}
|η|≤l
,
{
c(j)
i (t)
}
1≤i≤5n
1≤j≤l
)
+c(l)
i (t)
]
for any 1 ≤i ≤ 5n and l ∈ N0. Then by considering the initial condition ( 7.4) we
ﬁnd that
˜al+1 =∂lFi(c(0))
=C
[ l∑
k1=0
k1∑
k2=0
(l
k1
)( k1
k2
)
˜al−k1 ˜ak1−k2 ˜ak2
+p(5n)
l
({(|η| + 1)!
r|η|+1
γ
}
|η|≤l
,
{
˜aj
}
1≤j≤l
)
+ ˜al
]
. (7.6)
Finally an induction argument obtained from comparing ( 7.3) and ( 7.6), together
with the fact that Faà di Bruno’s polynomials pl (2.2) have non-negative coeﬃcients
and the initial condition a0 =~a0, gives
al ≤~al.
Then by ( 7.5) we conclude that ‖∂l+1γ‖H1+β ≤al ≤M l!
rl
C
for all l ∈ N0 which, by
Corollary 2.3, implies the analyticity of the curve γ. □
