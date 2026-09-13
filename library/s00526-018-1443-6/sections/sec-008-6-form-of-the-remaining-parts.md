---
doc_id: s00526-018-1443-6
doc_title: "Calc. Var. (2019) 58:16 Calculus of Variations On the analyticity of critical points of the Möbius energy Simon Blatt 1 · Nicole Vorderobermeier 1 © The Author(s) 2018"
section_id: sec-008-6-form-of-the-remaining-parts
section_title: "Form of the remaining parts"
section_number: 6
pages: 16-27
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
---
We aim to transform the truncated remaining parts Rε
1 and Rε
2 of the decomposition of the
Möbius energy E in Sect. 3 into multiple integrals of analytic functions of several variables.
This helps us to estimate the derivatives of the orthogonal projections of Rε
1 and Rε
2 later.
Let 1
2 ≥ ε> 0a n d x ∈[ 0, 1]. We start by recalling the deﬁnition of the ﬁrst remaining
part
(R1γ) (x) = lim
ε↓0
(Rε
1γ) (x)
where
(Rε
1γ) (x) := 4
∫
|w|∈
[
ε, 1
2
]
( 1
|γ( x + w) − γ( x)|4 − 1
w4
)
(γ (x + w) − γ( x) − w ˙γ( x))dw.
Similarly,
(R2γ) (x) = lim
ε↓0
(Rε
2γ) (x),
where
(Rε
2γ) (x) := −2
∫
|w|∈
[
ε, 1
2
]
( 1
|γ( x + w) − γ( x)|2 − 1
w2
)
¨γ( x)dw.
Because the second remaining part is the more elementary one, we start by working with
P⊥
˙γ Rε
2γ now.
123
On the analyticity of critical points of the Möbius energy Page 17 of 28 16
6.1 Form of P⊥
˙/CRR"
2 /CR
Theorem 6.1 We can express P ⊥
˙γ Rε
2γ as multiple integral
(
P⊥
˙γ Rε
2γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(s1 − s2)2G2(··· )(x)dφ1dφ2ds1ds2dw,
over the analytic function G 2 : Rn \{ 0}× R3n → Rn ,
G2(··· ) := P⊥
˙γ ~G2(··· ) = ~G2(··· ) −⟨~G2(··· ), ˙γ⟩˙γ,
where ~G2 : Rn \{ 0}× R3n → Rn deﬁned as ~G2(a, x, y, z) := − 1
|a|2 ⟨x, y⟩Rn z is analytic
and ~G2(··· ) is an abbreviation for
~G2
( ∫1
0
˙γ(·+ tw)dt, ¨γ(·+ s2w + (s1 − s2)φ1w), ¨γ(·+ s2w + (s1 − s2)φ2w), ¨γ(·)
)
.
Proof We begin to compute the left-hand side part of the integrand ofRε
2γ by the fundamental
theorem of calculus, the arc-length parametrization of γ , and linearity of the scalar product
as
1
|γ( x + w) − γ( x)|2 − 1
w2 = w2
|γ( x + w) − γ( x)|2
1 − |γ( x+w)−γ( x)|2
w2
w2
= g2
( ∫1
0
˙γ( x + tw)dt
) 2
(
1 − |γ( x+w)−γ( x)|2
w2
)
w2
= g2
( ∫1
0
˙γ( x + tw)dt
) ∫∫
[0,1]2 |˙γ( x + s1w) −˙γ( x + s2w)|2ds1ds2
w2
(6.1)
where g2(x) = 1
2|x|2 for all x ∈ Rn \{ 0} is analytic away from the origin and furthermore,
|˙γ( x + s1w) −˙γ( x + s2w)|2
w2
= (s1 − s2)2
∫1
0
∫1
0
⟨¨γ( x + s2w + (s1 − s2)φ1w), ¨γ( x + s2w + (s1 − s2)φ2w)⟩Rn dφ1dφ2.
(6.2)
Therefore, we can rewrite Rε
2γ such that
(Rε
2γ) (x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(s1 − s2)2·
~G2
( ∫1
0
˙γ( x + tw)dt, ¨γ( x + s2w + (s1 − s2)φ1w), ¨γ( x + s2w + (s1 − s2)φ2w), ¨γ( x)
)
dφ1dφ2ds1ds2dw
where ~G2 : Rn \{ 0}× R3n → Rn is deﬁned as
~G2(a, x, y, z) := −2g2(a)⟨x, y⟩Rn z
and is again an analytic function away from the origin in the ﬁrst variable, because sums,
products and compositions of analytic functions are analytic as well. Now by applying the
orthogonal projection P⊥
˙γ on Rε
2γ we obtain
123
16 Page 18 of 28 S. Blatt, N. Vorderobermeier
(
P⊥
˙γ Rε
2γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(s1 − s2)2(P⊥
˙γ ~G2(··· ))(x)dφ1dφ2ds1ds2dw
where ~G2(··· ) is an abbreviation for
~G2
( ∫1
0
˙γ(·+ tw)dt, ¨γ(·+ s2w + (s1 − s2)φ1w), ¨γ(·+ s2w + (s1 − s2)φ2w), ¨γ(·)
)
.
Finally we can express P⊥
˙γ Rε
2γ as multiple integral
(
P⊥
˙γ Rε
2γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(s1 − s2)2G2(··· )(x)dφ1dφ2ds1ds2dw,
over G2 : Rn \{ 0}× R3n → Rn ,
G2(··· ) := P⊥
˙γ ~G2(··· ) = ~G2(··· ) −⟨~G2(··· ), ˙γ⟩˙γ,
which is clearly analytic again. ⊓⊔
6.2 Form of P⊥
˙/CRR"
1 /CR
Now we may transfer the previous calculations to the orthogonal projection P⊥
˙γ Rε
1γ of the
ﬁrst remaining part.
Theorem 6.2 We can express P ⊥
˙γ Rε
1γ as multiple integral
(
P⊥
˙γ Rε
1γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2G1(··· )(x)dψ1dψ2dr1dr2dw,
over the analytic function G 1 : Rn \{ 0}× R3n → Rn ,
G1(··· ) := P⊥
˙γ ~G1(··· ) = ~G1(··· ) −⟨~G1(··· ), ˙γ⟩˙γ, (6.3)
where ~G1 : Rn \{ 0}× R3n → Rn deﬁned as ~G1(a, x, y, z) := 2( 1
|a|4 + 1
|a|2 )⟨x, y⟩Rn zi s
analytic and ~G1(··· ) is an abbreviation for
~G1
( ∫1
0
˙γ(·+ sw)ds, ¨γ(·+ r2w + (r1 − r2)ψ1w),
¨γ(·+ r2w + (r1 − r2)ψ2w),
∫1
0
¨γ(·+ tw)(1 − t)dt
)
.
(6.4)
Proof Similarly to the previous subsection we start by computing the integrand of Rε
1γ by
applying the integral form of the remainder of a Taylor polynomial
( 1
|γ( x + w) − γ( x)|4 − 1
w4
)
(γ (x + w) − γ( x) − w ˙γ( x))
=
( 1
|γ( x + w) − γ( x)|4 − 1
w4
)
w2
∫1
0
¨γ( x + tw)(1 − t)dt
=
( w2
|γ( x + w) − γ( x)|4 − 1
w2
) ∫1
0
¨γ( x + tw)(1 − t)dt.
(6.5)
123
On the analyticity of critical points of the Möbius energy Page 19 of 28 16
By considering the fundamental theorem of calculus we may transform the term within the
brackets in (6.5)a s
w2
|γ( x + w) − γ( x)|4 − 1
w2 = w4
|γ( x + w) − γ( x)|4
⎛
⎝ 1 − |γ( x+w)−γ( x)|4
w4
w2
⎞
⎠
= w4
|γ( x + w) − γ( x)|4
1
w2
(
1 + |γ( x + w) − γ( x)|2
w2
)(
1 − |γ( x + w) − γ( x)|2
w2
)
=
( w4
|γ( x + w) − γ( x)|4 + w2
|γ( x + w) − γ( x)|2
) 1
w2
(
1 − |γ( x + w) − γ( x)|2
w2
)
= g1
( ∫1
0
˙γ( x + sw)ds
) 2
w2
(
1 − |γ( x + w) − γ( x)|2
w2
)
/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
:=E
where g1(x) = 1
2|x|4 + 1
2|x|2 for all x ∈ Rn \{0} is analytic away from the origin. Furthermore,
by using (6.1)a n d( 6.2) for computing E,w ea r r i v ea t
(Rε
1γ) (x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2·
~G1
( ∫1
0
˙γ( x + sw)ds, ¨γ( x + r2w + (r1 − r2)ψ1w), ¨γ( x + r2w + (r1 − r2)ψ2w),
∫1
0
¨γ( x + tw)(1 − t)dt
)
dψ1dψ2dr1dr2dw
where ~G1 : Rn \{ 0}× R3n → Rn such that
~G1(a, x, y, z) = 4g1(a)⟨x, y⟩Rn z
and therefore analytic away from the origin in the ﬁrst variable. By applying the orthogonal
projection P⊥
˙γ on Rε
1γ we get
(
P⊥
˙γ Rε
1γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2(P⊥
˙γ ~G1(··· ))(x)dψ1dψ2dr1dr2dw
where ~G1(··· ) is an abbreviation for
~G1
( ∫1
0
˙γ(·+ sw)ds, ¨γ(·+ r2w + (r1 − r2)ψ1w),
¨γ(·+ r2w + (r1 − r2)ψ2w),
∫1
0
¨γ(·+ tw)(1 − t)dt
)
.
In the end, we can also express P⊥
˙γ Rε
1γ as multiple integral
(
P⊥
˙γ Rε
1γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2G1(··· )(x)dψ1dψ2dr1dr2dw,
over G1 : Rn \{ 0}× R3n → Rn ,
G1(··· ) := P⊥
˙γ ~G1(··· ) = ~G1(··· ) −⟨~G1(··· ), ˙γ⟩˙γ,
which is obviously analytic again. ⊓⊔
123
16 Page 20 of 28 S. Blatt, N. Vorderobermeier
7 Proof of the main theorem by Cauchy’s method of majorants
In order to prove the main result, Theorem 1.2,w ed e d u c ear e c u r s i v ee s t i m a t ef o r‖∂lγ‖H 1
by putting together the results of the previous sections. We then apply Cauchy’s method of
majorants to the recursive formula to achieve the analyticity of γ .
Let m := 1 > 1
2 and γ : R/Z → Rn , γ = (γ1,...,γ n), be a simple, closed, and by
arc-length parametrized curve with γ ∈ C∞(R/Z, Rn) and γ a critical point of the Möbius
energy E.T h e n(3.1) tells us that γ solves the Euler–Lagrange equation
(Hγ, h)L2([0,1],Rn) = 0
for all h ∈ H 2(R/Z, Rn) and therefore
Hγ = P⊥
˙γ Qγ + P⊥
˙γ R1γ + P⊥
˙γ R2γ ≡ 0 (7.1)
on R/Z by ( 3.2)a n d( 3.3). Let l ∈ N0. Then by Corollary 4.2 (7.1), the deﬁnition of the
orthogonal projection, and the triangle inequality
‖∂l+3γ‖H 1 ≤ ~C‖∂l Qγ‖H 1
= ~C
(‖‖‖∂l
(
PT
˙γ Qγ − P⊥
˙γ R1γ − P⊥
˙γ R2γ
)‖‖‖
H 1
)
≤ ~C
(
‖∂l PT
˙γ Qγ‖H 1 +‖∂l P⊥
˙γ R1γ‖H 1 +‖∂l P⊥
˙γ R2γ‖H 1
)
.
(7.2)
For the next estimates we assume 1
2 ≥ ε> 0. Then the estimates of the Sects. 2.1 and 5
imply the following estimate for the tangential part of Q.
Lemma 7.1 Let l ∈ N0. There exists a positive constant C Q < ∞ which is independent of ε
and l such that the following estimate holds:
‖∂l PT
˙γ Qεγ‖H 1 ≤ CQ
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H 1 ‖∂k1−k2+2γ‖H 1 ‖∂k2+1γ‖H 1 .
Proof Applying the Leibniz rule twice, we obtain
∂l
(
PT
˙γ Qεγ( x)
)
= ∂l
⎛
⎝4
∫
|w|∈
[
ε, 1
2
]
∫∫
[0,1]2
(1 − t)(−t)⟨¨γ( x + tw), ¨γ( x + stw)⟩Rn
w ˙γ( x)dsdtdw
⎞
⎠
= 4
∫
|w|∈
[
ε, 1
2
]
∫∫
[0,1]2
(1 − t)(−t)∂l
( ⟨¨γ( x + tw), ¨γ( x + stw)⟩Rn
w ˙γ( x)
)
dsdtdw
= 4
∫
|w|∈
[
ε, 1
2
]
∫∫
[0,1]2
(1 − t)(−t)·
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
) ⟨
∂l−k1+2γ( x + tw),∂ k1−k2+2γ( x + stw)
⟩
Rn
w ∂k2+1γ( x)dsdtdw
= 4
∫∫
[0,1]2
(1 − t)(−t)·
123
On the analyticity of critical points of the Möbius energy Page 21 of 28 16
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
) n∑
k=1
Hε
t,st (∂l−k1+2γk,∂ k1−k2+2γk)(x)∂k2+1γ( x)dsdt
where interchanging integrals and derivative are permitted due to the smoothness of the
integrand. Hence, by using the Banach algebra property of H 1 (2.1), the estimate of the
approximation of the bilinear Hilbert transform (Theorem5.3) for each of the components, the
equivalence of the Sobolev norms and the inequality of Cauchy-Schwarz we get component-
wise for all 1 ≤ m ≤ n
‖∂l(PT
˙γ Qεγ) m‖H 1
≤ 4
∫∫
[0,1]2
|1 − t||t|·
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
) n∑
k=1
C1‖Hε
t,st (∂l−k1+2γk,∂ k1−k2+2γk)‖H 1 ‖∂k2+1γm‖H 1 dsdt
≤ 4C1
∫∫
[0,1]2
|1 − t||t|·
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
) ( n∑
k=1
CH ‖∂l−k1+2γk‖H 1 ‖∂k1−k2+2γk‖H 1
)
‖∂k2+1γm‖H 1 dsdt
≤ 4C1CH
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H 1 ‖∂k1−k2+2γ‖H 1 ‖∂k2+1γm‖H 1 < ∞.
We ﬁnally get by the deﬁnition of the H 1-norm and the inequality of Cauchy-Schwarz
‖∂l PT
˙γ Qεγ‖H 1
≤ 4C1CH
√n
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H 1 ‖∂k1−k2+2γ‖H 1 ‖∂k2+1γm‖H 1 < ∞.
where CQ := 4C1CH
√n < ∞ is a positive constant which is independent of ε and l. ⊓⊔
Let us now estimate the remaining parts of the decomposition of the gradient by using
the form of P⊥
˙γ Rε
1γ (respectively, P⊥
˙γ Rε
2γ ), Faà di Bruno’s formula and the Banach algebra
property of H 1.
Lemma 7.2 Let us consider the mapping f : R/Z → Rn \{ 0}× R3n ,f = ( f1,..., f4n),
f (x) :=
⎛
⎜⎜⎝
˙γ( x)
¨γ( x)
¨γ( x)
¨γ( x)
⎞
⎟⎟⎠
and let l ∈ N0. Then we obtain positive constants C R1 , r < ∞ which are independent of ε
and l such that the universal polynomial p (4n)
l from the multivariate form of Faa di Bruno’s
formula Remark 2.7 satisfy
‖∂l P⊥
˙γ Rε
1γ‖H 1 ≤ CR1 p(4n)
l
( { (|α|+ 1)!
r|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
where C1 is the constant from the estimate (2.1) with m = 1.
123
16 Page 22 of 28 S. Blatt, N. Vorderobermeier
Proof We start by recalling the formula of P⊥
˙γ Rε
1γ computed in the previous section,
(
P⊥
˙γ Rε
1γ
)
(x) =
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2 G1( f1(x))dψ1dψ2dr1dr2dw
where G1 : Rn \{ 0}× R3n → Rn is an analytic function as deﬁned in ( 6.3)a n d( 6.4)a n d
f1(x) :=
⎛
⎜⎜⎝
∫1
0 ˙γ( x + sw)ds
¨γ( x + r2w + (r1 − r2)ψ1w)
¨γ( x + r2w + (r1 − r2)ψ2w))∫1
0 ¨γ( x + tw)dt
⎞
⎟⎟⎠ .
By interchanging derivative and integral due to the smoothness of the integrand and
by applying the generalized Faà di Bruno’s formula as stated in Remark 2.7 we obtain
component-wise for all 1 ≤ k ≤ 4n
∂l
(
P⊥
˙γ Rε
1γ
)
k
(x)
= ∂l
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2 G1,k( f1(x))dψ1dψ2dr1dr2dw
=
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2∂l G1,k( f1(x))dψ1dψ2dr1dr2dw
=
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
(r1 − r2)2·
p(4n)
l
(
{(∂α G1)k( f1(x))}|α|≤l,{ f ( j)
1,i (x)}1≤ j≤l,1≤i≤4n
)
dψ1dψ2dr1dr2dw.
Applying the H 1-norm on ∂l(P⊥
˙γ Rε
1γ) component-wise, we yield for any 1 ≤ k ≤ 4n by
the deﬁnition of the H 1-norm, triangle inequality and the Banach algebra property of H 1
‖∂l
(
P⊥
˙γ Rε
1γ
)
k
‖H 1
≤
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
|r1 − r2|2·
‖‖‖p(4n)
l
(
{(∂α G1)k( f1)}|α|≤l,{ f ( j)
1,i }1≤ j≤l,1≤i≤4n
)‖‖‖
H 1 dψ1dψ2dr1dr2dw
≤
∫
|w|∈
[
ε, 1
2
]
∫∫∫∫
[0,1]4
|r1 − r2|2·
p(4n)
l
(
{
‖‖(∂α G1)k( f1)
‖‖
H 1 }|α|≤l,{C1‖f ( j)
1,i ‖H 1 }1≤ j≤l,1≤i≤4n
)
dψ1dψ2dr1dr2dw
where p(4n)
l is the polynomial coming from Remark 2.7. The constant C1 does not appear in
front of ‖(∂α G1)k( f1)‖H 1 because p(4n)
l is one-homogeneous in the ﬁrst components.
Note that for any 1 ≤ j ≤ l
‖f ( j)
1,k ‖H 1 ≤‖ f ( j)
k ‖H 1 ∀ 1 ≤ k ≤ n, 3n + 1 ≤ k ≤ 4n,
‖f ( j)
1,k ‖H 1 =‖ f ( j)
k ‖H 1 ∀ n + 1 ≤ k ≤ 3n,
123
On the analyticity of critical points of the Möbius energy Page 23 of 28 16
and ‖f ( j)
k ‖H 1 does not depend on any of the parameters w,ψ i , ri , s, t for all 1 ≤ k ≤ 4n,
1 ≤ j ≤ l.N o w ,s i n c ef1 is a continuous function on R/Z and due to γ ∈ C∞(R/Z, Rn),
f1([0, 1]) is a compact set K of Rn \{ 0}× R3n . By the analyticity of G1, there hence are
constants CG1 < ∞, r > 0, such that
⏐⏐∂α G1(x)
⏐⏐≤ CG1
|α|!
r|α| (7.3)
for all α ∈ Nk0
0 , k0 ∈ N0,a n d x ∈ K . Without loss of generality, we assume r < 1. By
deﬁning the constant C f1 := 1 + ‖f1‖H 1 ≤ 1 + ‖f ‖H 1 < ∞, using Lemma 2.1 and (7.3)
we can estimate
‖‖(∂α G1)k( f1)
‖‖
H 1
=
‖‖(∂α G1,k|K )( f1)
‖‖
H 1
≤ Cc
‖‖∂α G1,k|K
‖‖
C1 (1 + ‖f1‖H 1 )
≤ CcC f1
‖‖∂α G1,k|K
‖‖
C1
= CcC f1 max
|β|=|α|+1
{
‖‖∂α G1,k|K
‖‖
∞ ,
‖‖∂β G1,k|K
‖‖
∞}
≤ CcC f1 CG1 max
|β|=|α|+1
{ |α|!
r|α| , |β|!
r|β|
}
≤ CcC f1 CG1
(|α|+ 1)!
r|α|+1 max
{ r|α|+1
|α|+ 1, 1
}
Hence
‖‖(∂α G1)k( f1)
‖‖
H 1 ≤~CR1
(|α|+ 1)!
r|α|+1
for all α ∈ Nk0
0 , k0 ∈ N0,a n d~CR1 := CcC f1 CG1 supα max
{
r|α|+1
|α|+1
}
< ∞ and with CR1 :=
√
4n ~CR1 we get
‖‖(∂α G1)( f1)
‖‖
H 1 ≤ CR1
(|α|+ 1)!
r|α|+1
In the end we arrive at
‖∂l
(
P⊥
˙γ Rε
1γ
)
‖H 1
≤ p(4n)
l
( {
CR1
(|α|+ 1)!
r|α|+1
}
|α|≤l
,{‖C1 f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
which is independent of ε.U s i n gt h a tp(4n)
l is one-homogeneous in the ﬁrst components, we
get the claim. ⊓⊔
The term P⊥
˙γ Rε
2γ can be estimated analogously:
Lemma 7.3 Let l ∈ N0 and f = ( ˙γ, ¨γ, ¨γ, ¨γ) as in Lemma 7.2. Then there are positive
constants C R2 , s < ∞ which are independent of ε and l and the same universal polynomial
p(4n)
l as in Lemma 7.2 such that
‖∂l P⊥
˙γ Rε
2γ‖H 1 ≤ CR2 p(4n)
l
( { (|α|+ 1)!
s|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
.
123
16 Page 24 of 28 S. Blatt, N. Vorderobermeier
Proof Completely similar to Lemma 7.2. ⊓⊔
The estimates of the Lemmata 7.1, 7.2 and 7.3 are also valid for the limit ε ↓ 0o nt h e
left-hand sides, what can be proved as below.
Theorem 7.4 Let l ∈ N0 and f = ( ˙γ, ¨γ, ¨γ, ¨γ) as in Lemma 7.2. Then there are posi-
tive constants C Q, CR1 , CR2 , r, s < ∞ which are independent of l and the same universal
polynomial p (4n)
l as in Lemma 7.2 such that
‖∂l PT
˙γ Qγ‖H 1 ≤ CQ
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H 1 ‖∂k1−k2+2γ‖H 1 ‖∂k2+1γ‖H 1 ,
‖∂l P⊥
˙γ R1γ‖H 1 ≤ CR1 p(4n)
l
( { (|α|+ 1)!
r|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
,
‖∂l P⊥
˙γ R2γ‖H 1 ≤ CR2 p(4n)
l
( { (|α|+ 1)!
s|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
.
Proof Let l ∈ N0 and { fε}ε>0 be a set of functions fε : R/Z → Rn such that there exist
positive constants Ci < ∞ with ‖∂i fε‖H 1 ≤ Ci for all ε> 0a n d0 ≤ i ≤ l. Furthermore,
let us assume that ∂i fε
ε↓0
−→ fi point-wise on [0, 1] with fi : R/Z → Rn ,0 ≤ i ≤ l.O u r
aim is to show that ∂l fε
ε↓0
−→∂l f0 ∈ H 1(R/Z, Rn) weakly in H 1 and hence especially
‖∂l f0‖H 1 ≤ lim inf
ε↓0
‖∂l fε‖H 1 ≤ Cl.
Then the statement of the theorem follows directly from applying this abstract argument
to fε = ∂l PT
˙γ Qεγ , fε = ∂l P⊥
˙γ Rε
1γ and fε = ∂l P⊥
˙γ Rε
2γ and using the previous Lem-
mata 7.1, 7.2 and 7.3.
Since H 1(R/Z, Rn) is a Hilbert space, there exists a subsequence { fεk }k∈N of { fε}ε>0
which converges weakly to a unique function f ∈ H 1(R/Z, Rn) in H 1(R/Z, Rn) and
by the compact embedding H 1(R/Z, Rn) ⊂⊂ C(R/Z, Rn) strongly to f with respect to
the uniform norm. Due to the point-wise convergence of fεk
k→∞
−→ f0 and the uniform
boundedness of{ fεk }k∈N,{ fεk }k∈N converges to f0 in C(R/Z, Rn) as well. By the uniqueness
of limits of weak convergent series we get f = f0 and since every weakly convergent
subsequence of { fε}ε>0 has the same limit, { fε}ε>0 converges weakly to f0 ∈ H 1(R/Z, Rn)
with respect to the H 1-norm and strongly to f0 with respect to the L2-norm. By the same
argument, {∂l fε}ε>0 converges weakly to fl ∈ H 1(R/Z, Rn) with respect to the H 1-norm
and strongly to fl with respect to the uniform norm.
It remains to show ∂l f0 = fl which follows by
123
On the analyticity of critical points of the Möbius energy Page 25 of 28 16
0 = lim
ε↓0
( ∫1
0
∂l fε(x)φ( x)dx − (−1)l
∫1
0
fε(x)∂lφ( x)dx
)
=
∫1
0
fl(x)φ( x)dx − (−1)l
∫1
0
f0(x)∂lφ( x)dx
for all φ ∈ C∞([0, 1], Rn) where we used Lebesgue’s theorem. ⊓⊔
Proof of Theorem 1.2 Let γ : R/Z → Rn , γ = (γ1,...,γ n), be a closed, simple, and by
arc-length parametrized curve in H
3
2 (R/Z, Rn) that is a critical point of the Möbius energy
E. We deduce by Theorem 1.1 that γ ∈ C∞(R/Z, Rn). Moreover, we set f : R/Z → R4n ,
f (x) :=
⎛
⎜⎜⎝
˙γ( x)
¨γ( x)
¨γ( x)
¨γ( x)
⎞
⎟⎟⎠
and al := C1‖∂l f ‖H 1 for all l ∈ N0. Our main goal is to determine positive constants
δ, Cγ < ∞ such that
al ≤ Cγ
l!
δl
from which we can directly conclude the analyticity of γ on R/Z by Corollary 2.4.
As explained above in the beginning of the section, ( 7.1) and therefore ( 7.2) hold for any
l ∈ N0,m o r ep r e c i s e l y
‖∂l+3γ‖H 1 ≤ ~C
(
‖∂l PT
˙γ Qγ‖H 1 +‖∂l P⊥
˙γ R1γ‖H 1 +‖∂l P⊥
˙γ R2γ‖H 1
)
.
Due to the deﬁnition of the Sobolev norm and the previous Theorem 7.4 we may conclude
that
al+1 =C1‖∂l+1 f ‖H 1 ≤ C1(3‖∂l+3γ‖H 1 +‖∂l+2γ‖H 1 )
≤ 3~CC 1
(
‖∂l PT
˙γ Qγ‖H 1 +‖∂l P⊥
˙γ R1γ‖H 1 +‖∂l P⊥
˙γ R2γ‖H 1
)
+ al
≤ 3~CC 1
⎛
⎝CQ
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
‖∂l−k1+2γ‖H 1 ‖∂k1−k2+2γ‖H 1 ‖∂k2+1γ‖H 1
+CR1 p(4n)
l
( { (|α|+ 1)!
r|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
)
+CR2 p(4n)
l
( { (|α|+ 1)!
s|α|+1
}
|α|≤l
,{C1‖f ( j)
i ‖H 1 }1≤ j≤l,1≤i≤4n
))
+ al.
Hence, there are constants C < ∞ and rγ > 0 such that
al+1 ≤ C
⎛
⎝
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
al−k1 ak1−k2 ak2
+ p(4n)
l
⎛
⎝
{
(|α|+ 1)!
r|α|+1
γ
}
|α|≤l
,{a j }1≤ j≤l
⎞
⎠
⎞
⎠
+al. (7.4)
123
16 Page 26 of 28 S. Blatt, N. Vorderobermeier
For any y ∈ R4n , y = (y1,..., y4n), we deﬁne a majorant F : R4n → R4n component-wise
as
Fi(y) := C
⎛
⎝y3
i + 1
(1 + 4na0−(y1+···+y4n)
rγ )2
⎞
⎠ + yi ,
for all 1 ≤ i ≤ 4n, which is clearly analytic around a0(1,..., 1). We now consider a solution
to the following initial value problem
˙c(t) = F(c(t)),
c(0) = a0(1,..., 1). (7.5)
The Theorem 2.5 implies that ( 7.5) has a unique solution c in C∞(]− ε, ε[, R4n) for some
ε> 0 which is analytic around 0. Soc can be expressed by its Taylor series in a neighborhood
of 0:
c(t) :=
∞∑
k=0
~ak(1,..., 1)
k! tk
where~ak(1,..., 1) = c(k)(0). By Theorem 2.2 we know that there exist positive constants
rc, M < ∞ such that
|c(l)(t)|≤ M l!
rlc
(7.6)
for all t ∈ Brc (0) and l ∈ N0.
For 1 ≤ i ≤ 4n and l ∈ N0 we have by Faà di Brunos formula as stated in Remark 2.7
∂l Fi (c(t))
= C
⎛
⎝
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
c(l−k1)
i (t)c(k1−k2)
i (t)c(k2)
i (t)
+ p(4n)
l
⎛
⎜⎜⎝
⎧
⎪⎨
⎪⎩
(|α|+ 1)!
r|α|+1
γ
1
(
1 +
(
4na0
rγ − (c1(t)+···+c4n(t))
rγ
))|α|+2
⎫
⎪⎬
⎪⎭
|α|≤l
, {c( j)
i (t)}1≤ j≤l,1≤i≤4n
⎞
⎟⎟⎠
⎞
⎟⎟⎠
+ c(l)
i (t),
so we obtain by the initial condition ( 7.5)
∂l Fi(c(0)) = C
⎛
⎝
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
˜al−k1 ˜ak1−k2 ˜ak2
+ p(4n)
l
⎛
⎝
{
(|α|+ 1)!
r|α|+1
γ
}
|α|≤l
,{˜a j }1≤ j≤l
⎞
⎠
⎞
⎠ +˜al.
123
On the analyticity of critical points of the Möbius energy Page 27 of 28 16
Hence, for all l ∈ N0
˜al+1 = C
⎛
⎝
l∑
k1=0
k1∑
k2=0
( l
k1
)( k1
k2
)
˜al−k1 ˜ak1−k2 ˜ak2
+ p(4n)
l
⎛
⎝
{
(|α|+ 1)!
r|α|+1
γ
}
|α|≤l
,{˜a j }1≤ j≤l
⎞
⎠
⎞
⎠ +˜al.
(7.7)
Comparing (7.4)a n d( 7.7) and using the fact that the coefﬁcients of the polynomial pl are
non-negative, we get by a0 =~a0 and induction
al ≤~al.
Hence ‖∂l+1γ‖H 1 ≤ al ≤ M l!
rl
C
for all l ∈ N0 by (7.6). Thus γ is analytic by Corollary 2.4.
⊓⊔
