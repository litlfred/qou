---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-002-22-properties-of-analytic-functions
section_title: "Properties of analytic functions"
section_number: 2.2
pages: 4-14
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — W e prove the analyticity of smooth critical points for O’Har a’s knot energies E α,p , with p = 1"
---
istics of analytic functions. More information on analytic functions can be found
for instance in [ Eva10, Chap. 6.4] and [ Fol95, Chap. 1, D].
It is well-known that analytic functions can be characteriz ed by [KP02, Prop. 2.2.10]
and a standard covering argument as follows:
Theorem 2.1. A function f ∈C∞(Ω, Rn) on Ω ⊆ Rm open,n,m ≥ 1, is analytic
on Ω if and only if for every compact set K ⊆ Ω there are positive constants rK
and CK such that
‖∂αf ‖L∞ (K) ≤CK
|α|!
r|α|
K
holds for every multiindex α ∈ Nm
0 .
The previous theorem, together with the embedding of the cla ssical Sobolev
spaceW k =W k,2 intoC0 for k ∈ N with k >m
2 , yields the following:
Corollary 2.2. A function f ∈C∞(Ω, Rn) on Ω ⊆ Rm open,n,m ≥ 1, is analytic
on Ω if for every compact set K ⊂ Ω there are positive constants rK and CK such
that
‖∂αf ‖W 1(K) ≤CK
|α|!
r|α|
K
holds for every multiindex α ∈ Nm
0 .
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 5
By the equivalence of the W 1- and the H 1-norm on R/Z as well as the embedding
H s ⊆H t for any t<s we obtain:
Corollary 2.3. Let f ∈ C∞(R/Z, Rn) and s ∈ (0, 1). Then the function f is
analytic on R/Z if there are positive constants r and C such that
‖∂kf ‖H1+s ≤Ck!
rk
holds for all integers k ≥ 0.
Furthermore, we will need a ODE version of the theorem of Cauc hy-Kovalevskaya,
which is originally an existence and uniqueness theorem for analytic nonlinear par-
tial diﬀerential equations associated with Cauchy initial value problems.
Theorem 2.4 (Cauchy-Kovalevskaya - ODE case). Suppose the function g : Rn →
Rn is real analytic around 0 and the function f ∈ C∞((−ε,ε ), Rn) of the form
f (x) = (f1(x),...,f n(x)), for any ε> 0, is a solution of the initial value problem
˙f (x) = g(f (x)) for x ∈ (−ε,ε ) with
f (0) = 0.
Then the function f is real analytic around 0.
One possible method to prove the theorem of Cauchy-Kovalevs kaya is the method
of majorants (c.f. [ Fol95, Chap. 1, D] or [ Eva10, Chap. 4.6.3, Theor. 2]). This
method turns out to be useful in proving the main result of thi s article.
2.3. F aà di Bruno’s formula. The k-th derivative of the composition of two
functions f,g ∈ Ck(R, R) can be expressed by Faà di Bruno’s formula which is
given by
(d
dt
) k
g(f (t)) =
∑
m1+2m2+···kmk=k,
m1,...,mk∈N0
k!
m1!1!m1m2!2!m2...m k!k!mk
g(m1+···+mk)(f (t))
k∏
j=1
(f (j)(t))mj.
This formula can be generalized to the multivariate case by a result of [ Mis00]. In
our case the precise generalized Faà di Bruno’s formula is no t required. Nonetheless
we will make use of the the following that can be easily proven from scratch by
induction:
For any functions f ∈ Ck(R, Rn) and g ∈ Ck(Rn, R), for integers n ≥ 1 and
k ≥ 0, there exists a universial polynomial p(n)
k with non-negative coeﬃcients,
which are independent of f and g, such that
∂kg(f (x)) = p(n)
k ({∂αg}|α|≤k, {∂jfi}i=1,...,n,j=1,...,k). (2.2)
In addition, p(n)
k is one-homogeneous in the ﬁrst entries.
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 6
3. Decomposition of the ﬁrst variation of E α
Results concerning the diﬀerentiability of O’Hara’s knot e nergies go back to
the paper [ FHW94] where the Gâteaux diﬀerentiability and the L2-gradient of the
Möbius energy E 2 was derived. Subsequently, a linearized version for the gra dient
of the Möbius energy was given by He [ He00, Lem. 2.2] in the context of the heat
ﬂow. An application of He’s linearization trick to a range of O’Hara’s knot energies
E α, for 2 ≤α< 3, was given by Reiter [ Rei12, Chap. 2].
In the following we will use the linearization trick of He and Reiter to decompose
the ﬁrst variation of the energies E α, for 2<α< 3, into a highest order quasilinear
part Qα and two remaining Rα
1 , Rα
2 parts of lower order (as it was done in [ BR13]
and [ Bla18, Theor. 2.3]). A similar decomposition of the ﬁrst variatio n proved apt
for the analyticity proof of critical points of the Möbius en ergy that was given in
[BV19].
Let γ ∈ C∞(R/Z, Rn) be a simple closed arc-length parametrized curve and
x ∈ R/Z. We recall that the orthogonal projection P ⊥
˙γ(x) : Rn → Rn at the point
γ(x) onto the normal space of the curve γ is given by
(P ⊥
˙γ v)(x) = P ⊥
˙γ(x)(v) = v − ⟨v, ˙γ(x)⟩Rn ˙γ(x)
for any v ∈ Rn. Furthermore, the tangential projection P T
˙γ : Rn → Rn at the point
γ(x) onto the tangent space of the curve γ is given by
(P T
˙γ v)(x) = P T
˙γ(x)(v) = ⟨v, ˙γ(x)⟩Rn ˙γ(x)
for any v ∈ Rn. We remark also that the curvature vector of the curve γ is denoted
byκ i.e. κ = ( d
ds )2γ where d
ds is the derivative with respect to the arc-length. We
recall the following:
Theorem 3.1 (Reiter [Rei12, Theor. 2.24]) . The ﬁrst variation of E α, for 2<α<
3, at a simple regular curve γ ∈ C∞(R/Z, Rn) in direction h ∈ H 2(R/Z, Rn) can
be expressed as
δE α(γ,h ) =
∫ 1
0
⟨(H αγ)(x),h (x)⟩Rn | ˙γ(x)|dx,
where
(H αγ)(x) := lim
ǫ↓0
∫
|w|∈[ǫ, 1
2 ]
P ⊥
˙γ(x){2α γ(x +w) −γ(x)
|γ(x +w) −γ(x)|2+α
− (α − 2) κ(x)
D(γ(x +w),γ (x))α − 2 κ(x)
|γ(x +w) −γ(x)|α }| ˙γ(x +w)|dw.
Due to the the fact that P ⊥
˙γ(x)( ˙γ(x)) = 0 , ⟨˙γ(x), ¨γ(x)⟩Rn = 0 , the curve γ is
parametrized by arc-length and the orthogonal projection P ⊥
˙γ(x) is linear, one can
easily rewrite H αγ as
(H αγ)(x) = (P ⊥
˙γ ~H αγ)(x) = P ⊥
˙γ(x)((~H αγ)(x)), (3.1)
where
(~H αγ)(x) := lim
ε↓0
∫
|w|∈[ε, 1
2 ]
{2αγ(x +w) −γ(x) −w ˙γ(x)
|γ(x +w) −γ(x)|2+α
− (α − 2) ¨γ(x)
D(γ(x +w),γ (x))α − 2 ¨γ(x)
|γ(x +w) −γ(x)|α }dw.
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 7
Now we want to apply the strategy of He and Reiter indicated as in the above.
We decompose ~H αγ pointwise for all x ∈ R/Z into three functionals by
~H αγ =αQαγ + 2αRα
1γ − 2Rα
2γ, (3.2)
where
Qαγ(x) = lim
ε↓0
Qα,εγ(x)
Rα
1γ(x) = lim
ε↓0
Rα,ε
1 γ(x)
Rα
2γ(x) = lim
ε↓0
Rα,ε
2 γ(x)
are given, for any 0<ε ≤ 1
2 , by
(Qα,εγ)(x) =
∫
|w|∈[ε, 1
2 ]
(
2γ(x +w) −γ(x) −w ˙γ(x)
w2 − ¨γ(x)
) dw
|w|α,
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
dw
Blatt and Reiter [ BR13] have already used this partitioning for studying the reg-
ularity of stationary points of O’Hara’s energies E α, 2 < α <3, and furthermore,
Blatt (cf. [ Bla18, Theor. 2.3]) used it in the study of the gradient ﬂow for the s ame
range of O’Hara’s knot energies.
In the next section we will see that Qα contains the highest order part of the
ﬁrst variation of E α. Thereafter the challenge will be to attain suﬃcient estima tes
of the tangential part of Qα, whereas Rα
1 and Rα
2 are of lower order and easier to
get under control.
4. An estimate for the Qα term
Let the quantities
q(α)
k :=
{
4π
|k|α +1
∫ π
0
(kτ )2−2+2 cos(kτ )
τ 2+α dτ k ⁄= 0,
0 k = 0
and set
λ(α)
k :=
∫ kπ
0
sin(τ )
τ α−1 dτ.
We remark that the λk are well-deﬁned for all k ∈ Z andλ(α)
∞ := lim k→∞λ(α)
k < ∞
(cf. [ Rei12, Lem. 2.4]). We deduce from [ Rei12, Prop. 2.3], by switching from the
weak formulation of the Euler-Lagrange equation to the stro ng one, the following:
Theorem 4.1. For every curve γ ∈C∞(R/Z, Rn) the term Qαγ is a C∞-function
and its Fourier coeﬃcients, for all k ∈ Z, are given by
ˆQαγ(k) = −q(α)
k |k|α+1ˆγ(k). (4.1)
The constants q(α)
k are bounded and satisfy
0 ≤q(α)
k = 8πλ(α)
k
α(α + 1)(α − 1) +O( 1
k1− α )
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 8
as k → ∞.
Proof. By Taylor’s expansion up to third order we obtain
Qαγ(x) = lim
ε↓0
2
∫
|w|∈[ε, 1
2 ]
w
|w|α
∫ 1
0
(1 −t)2...γ (x +tw)dtdw
= lim
ε↓0
2
∫
|w|∈[ε, 1
2 ]
w
|w|α
∫ 1
0
(1 −t)2 (...γ (x +tw) − ...γ (x)) dtdw, (4.2)
from which directly follows that Qα mapsC3,β toL∞ for any 0<β ≤ 1. From the
linearity of Qα we get ∂lQαγ(x) = Qα∂lγ(x), so Qα maps Cl+3,β to Cl−1,1 for all
integersl ≥ 1, which demonstrates the ﬁrst part of the Theorem’s statemen t.
Now we deﬁne the bilinear functional
~Qα(γ,η ) := lim
ε↓0
∫
R/Z
∫
|w|∈[ε, 1
2 ]
(⟨γ(x +w) −γ(x),η (x +w) −η(x)⟩Rn
w2 − ⟨˙γ(x), ˙η(x)⟩Rn
) dwdx
|w|α .
for any γ,η ∈ H
α +1
2 (R/Z, Rn). Applying continuous and discrete integration by
parts, gives
~Qα(γ,η ) = lim
ε↓0
∫
R/Z
∫
|w|∈[ε, 1
2 ]
(
−2 ⟨γ(x +w) −γ(x),η (x)⟩Rn
w2 − ⟨˙γ(x), ˙η(x)⟩Rn
) dwdx
|w|α
= − lim
ε↓0
∫
R/Z
⟨Qα,εγ(x),η (x)⟩Rn dx = −
∫
R/Z
⟨Qαγ(x),η (x)⟩Rn dx (4.3)
because Qα,εγ converges to Qαγ in L∞(R/Z, Rn) as ǫ ↓ 0 by ( 4.2). Furthermore,
by [ Rei12, Prop. 2.3], we have that
~Qα(γ,η ) =
∑
k∈Z
q(α)
k |k|α+1ˆγ(k)ˆη(k)
and by Plancherel’s identity we get
∫
R/Z
⟨Qαγ,η ⟩dx =
∑
k∈Z
ˆQαγ(k)ˆη(k).
So by comparing the Fourier coeﬃcients in ( 4.3) we have ˆQαf (k) = −q(α)
k |k|α+1ˆγ(k)
for all k ∈ Z. The properties of the coeﬃcients q(α)
k directly follow from the proof
of [ Rei12, Prop. 2.3]. □
By Theorem 4.1 we obtain the following essential corollary.
Corollary 4.2. There exists a positive constant ~C such that for all curves γ ∈
C∞(R/Z, Rn) and integers l ≥ 0
‖∂l+3γ‖Hm+α − 2 ≤ ~C‖∂lQαγ‖Hm
holds for any real numbers m ≥ 0 and 2<α< 3.
Proof. By considering Theorem 4.1, in particular the form of the Fourier coeﬃcients
(4.1), the deﬁnition of the fractional Sobolev-norm, elementar y properties of Fourier
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 9
coeﬃcients and the simple estimate (1 +k2)α−2 ≤ (2|k|)2(α−2) for any k ∈ Z \ 0,
we get
‖∂lQαγ‖2
Hm =
∑
k∈Z
(1 + |k|2)m| ˆ∂lQαγ(k)|2
=
∑
k∈Z
(1 + |k|2)m(2π|k|)2l|ˆQαγ(k)|2
=
∑
k∈Z
(1 + |k|2)m(2π|k|)2l(q(α)
k )2|k|2(α+1)|ˆγ(k)|2
≥ inf
k∈Z\0
{(q(α)
k )2(2π)−622−α}
∑
k∈Z
(1 + |k|2)m+α−2(2π|k|)2(l+3)|ˆγ(k)|2
= ~C−2∑
k∈Z
(1 + |k|2)m+α−2| ˆ∂(l+3)γ(k)|2
= ~C−2‖∂(l+3)γ‖2
Hm+α − 2,
where ~C := inf k∈Z\0{(q(α)
k )2(2π)−622−α}− 1
2 is a positive constant. □
5. A fractional leibniz rule and the form of P T
˙γ Qαγ
Let γ ∈ C∞(R/Z, Rn) be a closed simple curve parametrized by arc-length.
Recall that in the decomposed ﬁrst variation of O’Hara’s ran ge of energies E α, for
2 < α <3, there appears the orthogonal projection of the main part Qαγ, which
is given by P ⊥
˙γ Qαγ = Qαγ −P T
˙γ Qαγ. Since we have worked out an estimate for
Qαγ in the previous section, it remains to study P T
˙γ Qαγ, i.e. the tangential part of
Qαγ.
In this section we will see that a type of fractional derivati ve of a product of
two functions can help to estimate the tangential part of Qαγ. We interpret the
resulting estimate as a fractional Leibniz rule .
In order to avoid problems coming from the singularities of t he integrand, we will
work with the truncated functional Qα,ε for 0<ε ≤ 1
2 . By using Taylor’s approxi-
mation up to second order with remainder term in integral fro m and ⟨˙γ(x), ¨γ(x)⟩ = 0
for all x ∈ R/Z together with the bilinearity of the scalar product and α >2, we
can write
⟨Qα,εγ(x), ˙γ(x)⟩Rn
=
∫
|w|∈[ε, 1
2 ]
⟨
2γ(x +w) −γ(x) −w ˙γ(x)
w2 − ¨γ(x), ˙γ(x)
⟩
Rn
dw
|w|α
= 2
∫
|w|∈[ε, 1
2 ]
∫ 1
0
(1 −t) ⟨¨γ(x +tw), ˙γ(x)⟩Rn dt dw
|w|α
= 2
∫
|w|∈[ε, 1
2 ]
∫ 1
0
(1 −t)
⟨
¨γ(x +tw), ˙γ(x) − ˙γ(x +tw)
w
⟩
Rn
dt dw
w|w|α−2
= 2
∫
|w|∈[ε, 1
2 ]
∫ 1
0
∫ 1
0
(1 −t)(−t) ⟨¨γ(x +tw), ¨γ(x +stw)⟩Rn
w dsdt dw
|w|α−2. (5.1)
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 10
With ε ↓ 0 we also get
(P T
˙γ Qγ)(x)
= 4 lim
ε↓0
∫
|w|∈[ε, 1
2 ]
∫∫
[0,1]2
(1 −t)(−t) ⟨¨γ(x +tw), ¨γ(x +stw)⟩Rn
w|w|α−2 ˙γ(x)dsdtdw. (5.2)
The last terms of ( 5.1) and ( 5.2) motivate us to introduce the following:
Deﬁnition 5.1. Let s1,s 2 ∈ [0, 1], 0 < ε ≤ 1
2 and β ∈ (0, 1). Then the bilinear
singular integral Hs1,s2,β :C1(R/Z, R) ×C1(R/Z, R) →L∞(R/Z, R) is given by
Hs1,s2,β(f,g )(x) := lim
ε↓0
∫
|w|∈[ε, 1
2 ]
f (x +s1w)g(x +s2w)
w|w|β dw (5.3)
for all x ∈ R/Z and, its truncated version H ε
s1,s2,β : C1(R/Z, R) ×C1(R/Z, R) →
L∞(R/Z, R) is given by
H ε
s1,s2,β(f,g )(x) :=
∫
|w|∈[ε, 1
2 ]
f (x +s1w)g(x +s2w)
w|w|β dw (5.4)
for all x ∈ R/Z.
Ifβ was allowed to vanish, the previous deﬁnition would yield th e bilinear Hilbert
transform. Since we have the factor |w|β for β ∈ (0, 1) in the denominator in the
deﬁnition of the bilinear singular integral ( 5.3), the formula is reminiscent of a
fractional derivative.
Lemma 5.2. For every s1,s 2 ∈ [0, 1], 0 < ε ≤ 1
2 and β ∈ (0, 1) the transforms
Hs1,s2,β and H ε
s1,s2,β are well-deﬁned, continuous and bilinear from C1(R/Z, R) ×
C1(R/Z, R) to L∞(R/Z, R). Furthermore, the truncated bilinear integral H ε
s1,s2,β
is also continuous from C(R/Z, R) ×C(R/Z, R) to L∞(R/Z, R).
Proof. It is easy to see by the linearity of the integral in ( 5.3) that Hs1,s2,β is
indeed linear in both components. The function Hs1,s2,β is also well-deﬁned for
everyf,g ∈C1(R/Z, R), which we can see by adding a zero to the deﬁnition of the
bilinear singular integral ( 5.3) as
Hs1,s2,β(f,g )(x) = lim
ε↓0
∫
|w|∈[ε, 1
2 ]
f (x +s1w)g(x +s2w)
w|w|β − f (x)g(x)
w|w|β dw,
by inserting a second zero and by the Lipschitz-continuity o f continuously diﬀeren-
tiable functions on a compact set such that
|Hs1,s2,β(f,g )(x)|
≤ lim
ε↓0
∫
|w|∈[ε, 1
2 ]
|f (x +s1w)g(x +s2w) −f (x)g(x +s2w) +f (x)g(x +s2w) −f (x)g(x)|
|w|1+β dw
≤ lim
ε↓0
∫
|w|∈[ε, 1
2 ]
|f (x +s1w) −f (x)||g(x +s2w)| + |f (x)||g(x +s2w) −g(x)|
|w|1+β dw
≤ lim
ε↓0
∫
|w|∈[ε, 1
2 ]
‖f ′‖∞s1|w|‖g‖∞ + ‖f ‖∞‖g′‖∞s2|w|
|w|1+β dw
≤C(s1,s 2,β )‖f ‖C 1‖g‖C 1 < ∞ (5.5)
for some positive ﬁnite constant C(s1,s 2,β ). Hence we can deduce from ( 5.5) that
Hs1,s2,β is continuous. We get the same properties for H ε
s1,s2,β for any 0<ε ≤ 1
2 by
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 11
transfering the previous arguments. Additionally, since w e cut oﬀ the singularity
in the deﬁnition of H ε
s1,s2,β, the continuity of H ε
s1,s2,β fromC(R/Z, R) ×C(R/Z, R)
to L∞(R/Z, R) follows by the following elementary estimates
⏐⏐H ε
s1,s2,β(f,g )(x)
⏐⏐ =
⏐⏐⏐⏐⏐
∫
|w|∈[ε, 1
2 ]
f (x +s1w)g(x +s2w)
w|w|β − f (x)g(x)
w|w|β dw
⏐⏐⏐⏐⏐
≤
∫
|w|∈[ε, 1
2 ]
|f (x +s1w)||g(x +s2w)| + |f (x)||g(x)|
|w|1+β dw
≤
∫
|w|∈[ε, 1
2 ]
‖f ‖∞‖g‖∞ + ‖f ‖∞‖g‖∞
|w|1+β dw
≤C(β,ε )‖f ‖L∞ ‖g‖L∞ < ∞
for all x ∈ [0, 1] and some constant 0<C (β,ε )< ∞. □
We next estimate the truncated bilinear integral ( 5.4) that leads to a new kind
of fractional Leibniz rule.
Theorem 5.3. Let m > 1
2 , 0 < ε≤ 1
2 , s1,s 2 ∈ [0, 1] and β ∈ (0, 1). Then there
exists a positive constant CH =CH (m,β )< ∞ independent of ε such that
‖H ε
s1,s2,β(f,g )‖Hm ≤CH ‖f ‖Hm+β ‖g‖Hm+β (5.6)
for all f,g ∈C∞(R/Z, Rn).
For the proof we will identify, for any p ∈ [1, ∞), the sequence space ℓp by
ℓp := {x = (xk)k∈Z ∈ CZ | ‖x‖ℓp := (∑
k∈Z |xk|p)
1
p < ∞}
and use the following lemmata.
Lemma 5.4 (Young’s inequality). Let p,q,r ≥ 1 such that 1
p + 1
q = 1
r + 1. For
sequencesx ∈ ℓp and y ∈ ℓq the convolution (x ∗y)(k) := ∑
n∈Zx(n)y(k −n) is
such that x ∗y ∈ℓr and
‖x ∗y‖ℓr ≤ ‖x‖ℓp ‖y‖ℓq.
Lemma 5.5 (Sobolev-type inequality [ BV19, Lem. 5.5]) . Let f ∈ H m(R/Z, Rn)
for m> 1
2 . Then ˆf := ( ˆf (k))k∈Z ∈ℓ1 and there exists a positive constant C0 < ∞
such that
‖ ˆf ‖ℓ1 ≤C0‖f ‖Hm.
Proof of Theorem 5.3. Let f,g ∈ C∞(R/Z, R) ⊆ H m(R/Z, R). Because of m > 1
2
and [ DNPV12, Theor. 8.2], the partial sums of the Fourier series, i.e. pn(x) :=∑ n
k=−n
ˆf (k)e−2πikx andqn(x) :=∑ n
k=−n ˆg(k)e−2πikx for any n ∈ N0 andx ∈ R/Z,
converge uniformly to the functions f and g, that means
‖f −pn‖∞ → 0 and ‖g −qn‖∞ → 0 as n → ∞. (5.7)
Note that since f,g ∈C∞(R/Z, R), also pn,q n ∈C∞(R/Z, R) holds.
Our approach is to ﬁrstly prove the estimate ( 5.6) for the approximating func-
tionspn andqn and secondly derive the actual statement of Theorem 5.3 by passing
to the limit n → ∞. We start by interchanging the integrals two times due to ε> 0
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 12
and taking account of the fact that the Fourier coeﬃcients of a product of two
functions are the convolution of their Fourier coeﬃcients, to gain
ˆH ε
s1,s2,β(pn,q n)(k)
=
∫ 1
0
∫
|w|∈[ε, 1
2 ]
pn(x +s1w)qn(x +s2w)
w|w|β e−2πikxdwdx
=
∫
|w|∈[ε, 1
2 ]
∫ 1
0
pn(x +s1w)qn(x +s2w)e−2πikx dx dw
w|w|β
=
∫
|w|∈[ε, 1
2 ]
∑
l∈Z
ˆpn(l)e2πils1wˆqn(k −l)e2πi(k−l)s2w dw
w|w|β
=
{
0 if |k|> 2n∫
|w|∈[ε, 1
2 ]
∑ n
l=−ne2πi(ls1+(k−l)s2)wˆf (l)ˆg(k −l) dw
w|w|β if |k| ≤ 2n. (5.8)
Now we focus on the non-trivial Fourier coeﬃents of H ε
s1,s2,β(pn,q n), that means
on the indices |k| ≤ 2n. By deﬁning φl,k := 2π(ls1 + (k −l)s2) ∈ R, substitution
and interchanging integral and sum, we get
∫
|w|∈[ε, 1
2 ]
n∑
l=−n
eiwφl,k ˆf (l)ˆg(k −l) dw
w|w|β
=
∫ 1
2
ε
n∑
l=−n
eiwφl,k −e−iwφl,k
w|w|β
ˆf (l)ˆg(k −l)dw
=
∫ 1
2
ε
n∑
l=−n
2i sin(wφl,k)
w1+β
ˆf (l)ˆg(k −l)dw
=
n∑
l=−n
ˆf (l)ˆg(k −l)2i
∫ 1
2
ε
sin(wφl,k)
w1+β dw
=
n∑
l=−n
ˆf (l)ˆg(k −l)2iφβ
l,k
∫ φ l,k
2
φl,k ε
sin(~w)
~w1+β d~w
=
n∑
l=−n
ˆf (l)ˆg(k −l)2iφβ
l,k(Siβ
(
φl,k
2
)
− Siβ(φl,kε)), (5.9)
where Si β(x) :=
∫ x
0
sin(t)
t1+β dt. Hence we can deduce from the previous computations
in ( 5.8) and ( 5.9)
⏐⏐⏐ ˆH ε
s1,s2,β(pn,q n)(k)
⏐⏐⏐ ≤
n∑
l=−n
|ˆf (l)||ˆg(k −l)|2|φl,k|β
(⏐⏐⏐⏐Siβ
(φl,k
2
) ⏐⏐⏐⏐+ |Siβ(φl,kε)|
)
≤ ˜M
n∑
l=−n
|ˆf (l)||ˆg(k −l)||φl,k|β, (5.10)
where ˜M := 4 supφ∈[0,∞[ Siβ(φ)< ∞ due to [ Rei12, Lem. 2.4]. By ( 5.10) and
|φk,l|β = |2π(ls1 + (k −l)s2)|β ≤ 2π|l|β|k −l|β ≤ 2π(l2 + 1)
β
2 ((k −l)2 + 1)
β
2,
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 13
we conclude
⏐⏐⏐ ˆH ε
s1,s2,β(pn,q n)(k)
⏐⏐⏐ ≤ ˜M
n∑
l=−n
|ˆf (l)||ˆg(k −l)||φl,k|β
≤M
n∑
l=−n
(l2 + 1)
β
2 |ˆf (l)|((k −l)2 + 1)
β
2 |ˆg(k −l)|
=M
n∑
l=−n
(l2 + 1)
β
2 |ˆpn(l)|((k −l)2 + 1)
β
2 |ˆqn(k −l)|, (5.11)
where M := 2π ˜M . In addition, we obtain by ( 5.11) and the elementary estimates
(k2 + 1)
m
2 ≤ 2m(
(l2 + 1)
m
2 + ((k −l)2 + 1)
m
2
)
,
which are an immediate consequence of |k| ≤ 2 max{|l|, |k −l|}, that
⏐⏐⏐(k2 + 1)
m
2 ˆH ε
s1,s2,β(pn,q n)(k)
⏐⏐⏐
≤MC (m)
∑
l∈Z
(l2 + 1)
m+β
2 |ˆpn(l)| ((k −l)2 + 1)
β
2 |ˆqn(k −l)|
+MC (m)
∑
l∈Z
(l2 + 1)
β
2 |ˆpn(l)| ((k −l)2 + 1)
m+β
2 |ˆqn(k −l)|, (5.12)
where the positive constant C(m) < ∞ only depends on the parameter m. This
leads us to the idea to set the following series component-wi se for all k ∈ Z and
anyλ> 0
pλ
n(k) := (k2 + 1)
m+λ
2 |ˆpn(k)| and
qλ
n(k) := (k2 + 1)
m+λ
2 |ˆqn(k)|
such that we can rewrite ( 5.12) as
⏐⏐⏐(k2 + 1)
m
2 ˆH ε
s1,s2,β(pn,q n)(k)
⏐⏐⏐ ≤MC (m)
(
(pβ
n ∗q0
n)(k) + (p0
n ∗qβ
n)(k)
)
.
Finally, we obtain the desired estimate ( 5.6) for pn andqn by applying Lemma 5.4,
Lemma 5.5, and Sobolev’s embedding theorem to estimate
‖H ε
s1,s2,β(pn,q n)‖Hm = ‖((k2 + 1)
m
2 ˆH εs1,s2(pn,q n)(k))k∈Z‖ℓ2
≤MC (m)
(
‖((pβ
n ∗q0
n)(k))k∈Z‖ℓ2 + ‖((p0
n ∗qβ
n)(k))k∈Z‖ℓ2
)
≤MC (m)
(
‖pβ
n‖ℓ2‖q0
n‖ℓ1 + ‖p0
n‖ℓ1‖qβ
n‖ℓ2
)
≤MC (m)C0 (‖pn‖Hm+β ‖qn‖Hm + ‖pn‖Hm‖qn‖Hm+β )
=CH ‖pn‖Hm+β ‖qn‖Hm+β, (5.13)
where CH := 2MC (m)C0 is a constant only depending on m and β.
Finally, we get the statement ( 5.6) for f and g by passing to the limit n → ∞ .
In particular, by using ( 5.13), we ﬁnd for any integer n ≥ 0 that
‖H ε
s1,s2,β(pn,q n)‖Hm ≤CH ‖pn‖Hm+β ‖qn‖Hm+β
≤CH ‖f ‖Hm+β ‖g‖Hm+β (5.14)
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 14
By uniform convergence and by Lemma 5.2 we ﬁnd that
‖H ε
s1,s2,β(f,g ) −H ε
s1,s2,β(pn,q n)‖∞
≤ ‖H ε
s1,s2,β(f,g ) −H ε
s1,s2,β(pn,g )‖∞ + ‖H ε
s1,s2,β(pn,g ) −H ε
s1,s2,β(pn,q n)‖∞
= ‖H ε
s1,s2,β(f −pn,g )‖∞ + ‖H ε
s1,s2,β(pn,g −qn)‖∞
≤C(β,ε )‖f −pn‖∞‖g‖∞ +C(β,ε )‖pn‖∞‖g −qn‖∞
→ 0
asn → ∞, since ‖f −pn‖∞ → 0 and ‖g −qn‖∞ → 0 asn → ∞ by our assumption
(5.7). Moreover, by the uniqueness of the Fourier coeﬃcients of H ε
s1,s2,β(pn,q n) ∈
H m(R/Z, R) ⊆L2(R/Z, R) we have, for all k ∈ Z, that
⏐⏐⏐ ˆH ε
s1,s2,β(f,g )(k) − ˆH ε
s1,s2,β(pn,q n)(k)
⏐⏐⏐ → 0
as n → ∞. Thus for all positive integers N ≥ 1 we ﬁnd that
⏐⏐⏐
(∑
|k|≤N
(1 + |k|2)m| ˆH ε
s1,s2,β(pn,q n)(k)|2
) 1
2
−
(∑
|k|≤N
(1 + |k|2)m| ˆH ε
s1,s2,β(f,g )(k)|2
) 1
2
⏐⏐⏐ → 0
as n → ∞. Then by ( 5.14) we conclude that
(∑
|k|≤N
(1 + |k|2)m| ˆH ε
s1,s2,β(f,g )(k)|2
) 1
2
≤CH ‖f ‖Hm+β ‖g‖Hm+β
which implies the desired estimate ( 5.6) for f and g. □
