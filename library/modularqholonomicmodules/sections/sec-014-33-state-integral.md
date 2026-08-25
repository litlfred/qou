---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-014-33-state-integral
section_title: "State integral"
section_number: 3.3
pages: 28-29
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
I(z,α,β,τ ) =
∫
C
Φb(x)∏r−1
j=1 Φb(x +ib−1βj +ib−1−ib)∏r
j=1 Φb(x +ib−1αj +ib−1−ib) exp
(
−2πzx
b
)
dx. (137)
whereC is a contour in the complex plane asymptotic to R +iε that separates the poles of
the numerator from the zeros of the denominator of the integrand, ai = e(αi), ˜ai = e(αi/τ),
bi = e(βi) and ˜bi = e(βi/τ), and Φ b is the Faddeev quantum dilogarithm function [23, 24]
and b =√τ.
We ﬁrst discuss convergence of the above integral forτ = b2 in the upper half-plane. Using
the asymptotic behavior Φ b(x)∼ e2πix2
(resp., 1) when Re(x)≫ 0 (resp., Re(x)≪ 0) (see
for example, [3, Eqn.(46)]), it follows that when Re( x)≫ 0, the integrand of (137) is given
by a constant timese−2πxb−1(γ+z) whereγ =∑r−1
j=0βj−∑r
j=1αj, and setting x =x0 +it with
t≫ 0, it follows that the absolute value of the integrand is a constant timese−2πtIm(b−1(γ+z)),
which is exponentially decaying when Im( b−1(γ +z)) < 0. Likewise, when Re( x)≪ 0, the
integrand is exponentially decaying when Im( b−1z)> 0.
Finally, the state integral satisﬁes diﬀerence equations when we shift α,β,z by either 1
or τ. This can be used to analytically extend to a meromorphic function for τ ∈ C ′ and
α∈ C r, β∈ C r−1, and z∈ C .
From its very deﬁnition, the state integral is a well-deﬁned holomorphic function ofτ∈ C ′.
Moreover, after moving the contour of integration upwards and using the residue theorem
(see eg. [30]), the state integral in Equation (137) can be written in the factorised form
I(z,α,β,τ ) =−t1/2˜t1/2 τ
2πiI(z,α,β,τ ) (138)
where
I(z,α,β,τ ) =f (1)(t,a,b,q )f (1)(˜t, ˜a,˜b, ˜q−1)−τ
r∑
j=1
f (qb−1
j )(t,a,b,q )f (qb−1
j )(˜t, ˜a,˜b, ˜q−1). (139)
NowI(z +k +jτ,α,β,τ ) is nothing but the (j + 1,k + 1) entry of the matrix
U(t,a,b,q )


1 0 ... 0
0 −τ ... 0
: : ... :
0 0 ... −τ

U(˜t, ˜a,˜b, ˜q−1)T, (140)
MODULAR q-HOLONOMIC MODULES 29
and therefore, by Equation (119), the (j + 1,k + 1) entry of
U(t,a,b,q )


1 0 ... 0
0 τ ... 0
: : ... :
0 0 ... τ

U(˜t, ˜a,˜b, ˜q)−1Q(˜t, ˜a,˜b, ˜q)−T. (141)
Therefore, inverting Q, we see that the cocycle
Ω(z,α,β,τ ) =U(˜t, ˜a,˜b, ˜q)


1 0 ... 0
0 τ ... 0
: : ... :
0 0 ... τ


−1
U(t,a,b,q )−1 (142)
extends to a meromorphic function for τ∈ C ′. This complete the proof of Theorem 1.4.
Remark 3.4. Note that the state integral (137) is absolutely convergent and its contour of
integration can be pushed either upwards or downwards. Doing so, the integral factorises in
two diﬀerent ways, one giving theU-cocycle and another giving theV -cocycle. This explains
the equality of the two cocycles from ﬁrst principles.
