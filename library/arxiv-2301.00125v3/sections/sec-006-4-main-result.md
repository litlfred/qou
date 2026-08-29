---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-006-4-main-result
section_title: "Main result"
section_number: 4
pages: 12-16
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
Using equations (56) and (72), we know
α(w,x 2) =
∮
C(0;1)
w·ξ +~g(x;ξ)
x2·
(
ξ−A 1(x,w )
)(
ξ−A 2(x,w )
)(
ξ−b1(x,w )
)(
ξ−b2(x,w )
)· dξ
2πi . (73)
We will deform the contour from C(0; 1) into the open disk U(0; 1) shrinking to contours around the poles
A1(x,w ) andA2(x,w ) and also around the branch cut [ c1(x),c 2(x)] as in Figure 3.
Lemma 4.1 Forx,w∈ (0,∞) satisying 4x +w2 < 1 we have
α(w,x 2) = A1(x,w ) +A2(x,w ), (74)
for the function A1(x,w ) given by the residue theorem
A1(x,w ) = w·a1(x,w ) +~g
(
x;a1(x,w )
)
x2·
(
a1(x,w )−a2(x,w )
)(
a1(x,w )−b1(x,w )
)(
a1(x,w )−b2(x,w )
)
+ w·a2(x,w ) +~g
(
x;a2(x,w )
)
x2·
(
a2(x,w )−a1(x,w )
)(
a2(x,w )−b1(x,w )
)(
a2(x,w )−b2(x,w )
),
(75)
and for the function A2(x,w ) given by the integral
A2(x,w ) = 1
π·
∫ c2(x)
c1(x)
I2(x,w ;r)dr, (76)
where
∀r∈ [c1(x),c 2(x)], we have I2(x,w ;r) = i·~g+(x;r)−i·~g−(x;r)
2Q2(x,w ;r) , (77)
for the functions ~g+(x;·) and~g−(x;·) deﬁned such that
∀r∈ [c1(x),c 2(x)], we have ~g±(x;r) = lim
ǫ→0+
~g(x;r±iǫ). (78)
12
c1 c2
•
< <
ξ =r +iǫ
θ1 θ2
Figure 5: Consideration of the phase of the function, ~g(x;ξ) =
√
Q1(x;ξ), for ξ = r + iǫ with c1(x) ≤
r≤ c2(x). If we write ~g(x;ξ) as eiϕR for R≥ 0 and ϕ∈ R then by “phase” we mean eiϕ . For r∈ R\
{c1(x),c 2(x),d 1(x),d 2(x)}, and taking ξ =r +iδ the phase eiϕ converges to a number Ω +(r)∈{ 1,i,−1,−i} in
the δ→ 0+ limit. Similarly for the limit of the phase from the lower hal f-plane Ω − (r).
This lemma is elementary and will be proved in Appendix H. Note that sinc e w·ξ/Q2(x,ξ ) is analytic for ξ
in a neighborhood of [ c1(x),c 2(x)], its contribution to the integral along Γ 3(δ) vanishes. See Figure 3. That
is why it is not included in I2(x,w ;r).
Note thatA1(x,w ) andA2(x,w ) are roots of Q2(x,w ;ξ) which isQ1(x;ξ)−w2ξ2 as in (49) and (56). But(
~g(x;ξ)
)2
=Q1(x;ξ) by (61) and (71). Therefore, w·aj(x,w ) +~g(x;aj (x,w )) may be simpliﬁed for j = 1, 2
in the formula for A1(x,w ).
Lemma 4.2 Forx,w∈ (0,∞) satisfying 4x +w2 < 1 we have
A1(x,w ) = 2w·a1(x,w )
x2·
(
a1(x,w )−a2(x,w )
)(
a1(x,w )−b1(x,w )
)(
a1(x,w )−b2(x,w )
)
+ 2w·a2(x,w )
x2·
(
a2(x,w )−a1(x,w )
)(
a2(x,w )−b1(x,w )
)(
a2(x,w )−b2(x,w )
),
(79)
or simplifying
a1(x,w ) = 2w·
(
b1(x,w )·b2(x,w )−a1(x,w )·a2(x,w )
)
x2∏ 2
j=1
∏ 2
k=1
(
bj(x,w )−ak(x,w )
) . (80)
We will prove this lemma in Appendix H. Recall from equation (57) that b2(x,w ) = 1/a1(x,w ) and b1(x,w ) =
1/a2(x,w ). From this one may simplify a bit more.
Lemma 4.3 Forx,w∈ (0,∞) satisfying 4x +w2 < 1 we have
A1(x,w ) =
2w·a1(x,w )·a2(x,w )
(
1 +a1(x,w )·a2(x,w )
)
x2·
(
1−a1(x,w )·a2(x,w )
)(
1−
(
a1(x,w )
)2)(
1−
(
a2(x,w )
)2). (81)
This elementary lemma will also be proved in Appendix H.
Lemma 4.4 Forx,w∈ (0,∞) satisfying 4x +w2 < 1, it is the case that
∀r∈ [c1(x),c 2(x)], we have ±i·~g±(x,r ) = −
√
−Q1(x;r), (82)
where note that Q1(x;r)≤ 0 for all r∈ [c1(x),c 2(x)]. In particular
A2(x,w ) = 1
π
∫ c2(x)
c1(x)
√
−Q1(x;r)
−Q2(x,w ;r)dr, (83)
where alsoQ2(x,w ;r)< 0 for r∈ [c1(x),c 2(x)], since a1(x,r )<c 1(x)<c 2(x)<a 2(x,r ).
13
We will give the details of the proof in Appendix H. But we may indicate th e key to the calculation by referring
to Figure 5. Recall from equation (52) and (65) that ~g(x;·) is an analytic continuations of
√
Q1(x,·). More
precisely, we had a function f (x;·) deﬁned on D2(x) such that f (x;ξ) =
√
Q1(x;ξ)/ξ2. Then ~g(x;·) is deﬁned
on the region D4(x) and ~g(x;ξ) = ξ·f (x;ξ) onD2(x) (which is a subset of D4(x)). It is easy to see that
∀r∈ [c1(x),c 2(x)], we have lim
ǫ→0+
|~g(x;r +iǫ)| = lim
ǫ→0+
|~g(x;r−iǫ)| =
√
−Q1(x;r), (84)
because Q1(x;r) ≤ 0 for all r ∈ [c1(x),c 2(x)]. So all that remain is to determine the phase, meaning
~g±(x;r)/|~g±(x;r)|. Let us call that Ω ±(x;r). Then as in Figure 5, we may see that Ω ±(x;r) = ±i, mainly
because in the product of the four square roots, exactly one has an argument which is “approximately
negative,” being such that the phase of the argument of that squa re root is equal to: ei(π−δ) for ξ =r +iǫ,
and e−i(π−δ) for ξ =r−iǫ, where the quantity δ is such that δ→ 0+ when ǫ→ 0+. Taking the square-roots
we get Ω ±(x;r) =±i. We give more careful details in Appendix H.
Note that the integral equation (85) is an elliptic integral: A2(x,w ) can be put into the form
1
π·
∫ c2(x)
c1(x)
x·
√
r−c1(x)·
√
c2(x)−r·
√
d1(x)−r·
√
d2(x)−r
−Q2(x,w ;r) dr
=
∫ c2(x)
c1(x)
R(x,w ;r)√
r−c1(x)·
√
c2(x)−r·
√
d1(x)−r·
√
d2(x)−r
dr,
(85)
whereR(x,w ;·) : C→ C∪{∞} is a rational (meromorphic function), and we note that the denomin ator
on the left-hand-side is the square-root of a quartic function. Bu t for the Legendre normal form for elliptic
integrals, we prefer to use a linear fractional transformation to t ransform to a quartic of the form
(1−r2)(1−k2r2) = k2· (r− 1)(r + 1)(r−k−1)(r +k−1), (86)
for some number k∈ (0, 1). In other words, for the normal form, the roots of the quart ic should come in pairs
which are additive inverses. For Q1(x,w ;r), the roots come in pairs which are multiplicative reciprocals (53).
To reduce an elliptic integral to normal form one generally applies one or more linear fractional trans-
fomations L(r) = ( ar + b)/(cr + d), for example with ad− bc = 1 and a,b,c,d ∈ R having inverse
L−1(s) = ( ds−b)/(−cs +a), using a substitution r = L−1(s). This is a good type of transformation
for such a problem. Precomposing with L−1 has good properties for rational functions. Such a mapping also
takes the quartic function inside the square-root to another qua rtic function, modulo multiplying by an even
power of the denominator (−cs +a). It should be mentioned that dr =dL−1(s) also produces an even power
of (−cx +a).
Therefore we note, that within the family of linear fractional trans formations there is one (and its inverse)
which intertwines between pairs of numbers which are multiplicative re ciprocals and pairs of numbers which
are additive inverses. It is
L(z) = z− 1
z + 1, with L−1(ξ) = 1 +ξ
1−ξ . (87)
This satisﬁes L(1/z) =−L(z) and L(−z) = 1/L(z). After performing this transformation and rescaling, we
do replace the quartic Q1(x;r) by the normal form of (86), with
k2 =
(
K1(x)
)2
, where K1(x) =
√
1− 4x2. (88)
Then the path of integration is the interval between two of the roo ts of (86), 1 and 1 /k. We do want the path
of integration to be an invterval joining two of the roots of (86) to get a complete elliptic integral, which is a
bit simpler than the incomplete integrals. Unfortunately, for the Le gendre normal form of an elliptic integral,
it is preferred that the path of integration is between the pair of ro ots−1 and 1 (instead of between the pair
1 and 1 /k). So, we use another linear fractional transformation to permut e the roots cyclically, while also
changingk from K1(x) to another value. The linear fractional transformation is
Λ(k;z) =
(
k−1/2 + 1
)(
z−k−1/2)
(
k−1/2− 1
)(
z +k−1/2), with Λ −1(k;ξ) = k−1/2· k−1/2 + 1 +
(
k−1/2− 1
)
ξ
k−1/2 + 1−
(
k−1/2− 1
)
ξ , (89)
which has the property
Λ(k;k−1) = 1 , Λ(k; 1) = −1, Λ(k;−1) = −1/J (k) and Λ( k;−k−1) = 1 /J (k), (90)
14
for the involution J : (0, 1)→ (0, 1) given by
J (k) = (1 −k1/2)2/(1 +k1/2)2. (91)
It may be worthwhile to note that J is a decreasing function on (0 , 1) with ﬁxed point (
√
2− 1)2.
After performing the second linear fractional transformation us ing Λ( K1(x);·) and Λ −1(K1(x);·), we do
obtain another elliptic integral with the quartic of the form of (86) n ow with
k2 = (K2(x))2, where K2(x) = J (K1(x)) =
(1− (1− 4x2)1/4
1 + (1− 4x2)1/4
)2
. (92)
And the path of integration is the interval from −1 to 1, as desired.
Theorem 4.5 As usual, denote the complete elliptic integral of the ﬁrst k ind as
K(k) =
∫ 1
0
1√
(1−t2)(1−k2t2)
dt, (93)
and let the complete elliptic integral of the third kind be
Π(k;λ) =
∫ 1
0
1√
(1−t2)(1−k2t2)
· 1
1−λtdt. (94)
Then we have that A2(x,w ) can be written as a linear combination of terms of the form φi(x,w )Π(ψi(x,w ))
(with at most 4 terms) where each φi and ψi are algebraic expressions. Hence the generating function α(w,z )
is an expression involving algebraic functions and a linear combination of several Π -functions, viewed as a
vector over the ﬁeld of algebraic functions (other than the i dentically zero function).
We note that occasionally leading theoretical physicists make contr ibutions to algebra and number theory
by determining certain physical quantities in terms of algebraic or nu mber theoretic expressions. For example,
Boos, Korepin, Nishiyama and Shiroishi found that certain correlat ion functions of the XXZ ground state (for
the quantum spin chain) are expressible in terms of rational linear co mbinations of the products of ln(2) and
factors of the Riemann zeta functions ζ evaluated at the ﬁrst n odd positive integers [10]. Our main theorem
may be viewed as following their model.
The following is an important remark.
Remark 4.6 In [28], Ross Pinsky proved the combinatorial fact
A(N,j )(2N
N
)(2N
N
) =
∑
t1,...,tj ∈Z
0≤t1≤···≤tj ≤2N
P
(
Ut1 =··· =Utj = 0
⏐
⏐U2N =V2N = 0
)
, (95)
where (Ut,V t) performs the standard d = 2 dimensional SRW starting from (0, 0). See his equation 4.2 in the
ﬁrst part of his proof of his Lemma 2.
The standard d = 2 dimensional SR W is such that ( Ut+1−Ut,V t+1−Vt) are iid increments equally likely
to be any of the four elements from {(1, 0), (0, 1), (−1, 0), (0,−1)}. The transformation that Pinsky gives in
his paper is ( Xt,Y t) = (Ut +Vt,U t−Vt), so that Xt andYt independently perform d = 1 dimensional SR Ws.
Then it is seen that P(U2N =V2N = 0) = 2 −4N(2N
N
)(2N
N
)
. Therefore, Pinsky’s formula (95) can be rewritten
as
2−4NA(N,j ) =
∑
t1,...,tj ∈Z
0<t1<···<tj <2N
P
(
Ut1 =··· =Utj = 0 and U2N =V2N = 0
)
, (96)
This is also related to P´ olya’sd = 2 dimensional result. We point to McKean’s textbook, in which he disc usses
P´ olya’s result in Section 4.3, [21]. That is more accessible than P´ olya’s original [30]. The precise formula of
P´ olya is the following
∞∑
N =0
P(U2N =V2N = 0)zN = 1
πK(z), (97)
for|z| < 1, where K(z) is as in (93). Let us perform a consistency check for our main form ulas by noting
that when w = 0 we haveA1(x,w ) =A1(x, 0) = 0 due to formula (85). But in Lemma 4.4, if we send w→ 0,
we have
−Q 2(x,w ;r) = −Q2(x, 0;r) = −Q1(x;r). (98)
15
But then, by Lemma 4.1, we have
α(0,x 2) = 0 + A2(x, 0) = 1
πx
∫ c2(x)
c1(x)
1√ (
r−c1(x)
)(
c2(x)−r
)( 1
c1(x)−r
)( 1
c2(x)−r
)dr. (99)
Using the methods of Appendix I, this can be seen to give the desired specialization α(x,w = 0) = K(x)/π.
