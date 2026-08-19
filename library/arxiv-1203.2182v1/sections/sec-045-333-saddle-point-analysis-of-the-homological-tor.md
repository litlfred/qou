---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-045-333-saddle-point-analysis-of-the-homological-tor
section_title: "Saddle point analysis of the homological torus knot invariants"
section_number: 3.3.3
pages: 42-43
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
In this section we analyze general (2 , 2p + 1) torus knots ( p ≥ 1). For this class of knots,
the quantum reﬁned curves ˆAref
T 2,2p+1(ˆx,ˆy;q,t ) are not known at present (apart from the case
of trefoil, i.e. p = 1, with the quantum curve determined in (3.129)). Therefor e, we cannot
determine reﬁned A-polynomials by taking the classical limit of ˆAref, as we did for the trefoil
knot or for the unknot. Nevertheless, we can determine reﬁne d A-polynomials from the
asymptotic behavior of the colored superpolynomials and th eir specializations (3.97). For
general values of p, we determine parametric representation of such A-polynomials, and for
several ﬁrst values of p we rewrite this parametric form as a polynomial Aref
T 2,2p+1(x,y ;t), see
Table 3.
There is one fundamental diﬀerence between the specializati on Pn(K;q,t ) of the colored
superpolynomial for torus knots found in (3.97) and that of t he unknot (3.99). Namely, the
latter is given by an inﬁnite product, whose asymptotic expansion is obtained simply from the
expansion of the quantum dilogarithm (3.154). On the other hand, the homological invariants
of torus knots are expressed as inﬁnite sums, with each term i n those sums given by inﬁnite
products. Therefore, the analysis of the asymptotic behavi or for torus knots is more delicate
and requires new methods.
In order to ﬁnd the “reﬁned volume” S0(u,t ) for torus knots, we apply the saddle point
approximation [61, 62] to (3.97) and replace the quantum dil ogarithm function by
(z;q)k ∼e
1
ℏ (Li2(z)−Li2(zq k)). (3.165)
Furthermore, via an analytic continuation we can approxima te the summation in (3.97), in
the asymptotic limit (2.5), by the following integral:
Pn(T 2,2p+1;q,t ) ∼
∫
dz e
1
ℏ (V(2,2p+1)(z,x;t)+O(ℏ)), (3.166)
with the “potential” function
V(2,2p+1)(z,x ;t) := −p log(−t) · logx + (p + 1)πi logx + log(x
1
2z−1) · logt
+(2p + 1)
(
πi logz + 1
2
(
(logx)2 − (logz)2)
+ log(x
3
2z−1) · logt
)
+Li2(z) − Li2(x) − Li2(t2z) + Li2(−t3x) + Li2(t2xz)
−Li2(−t3xz) + Li2(xz−1) − Li2(−txz−1) + Li2(−t) − Li2(1), (3.167)
– 41 –
and where the parameter z is related to ℓ in (3.97) via ℓ = 1
ℏ logz. Now, the dominant
contribution to this integral comes from the saddle point 9
∂V(2,2p+1)(z,x ;t)
∂z
⏐
⏐
⏐
⏐
⏐
z=z0
= 0, (3.168)
and the value of the “potential” V (z,x ;t) at this saddle point determines S0(u,t ):
V(2,2p+1)(z0,x ;t) = S0(u,t ). (3.169)
For the above potential VT 2,2p+1(z,x ;t), the critical point condition can simply be expressed
as 1 = exp
(
z∂V (2,2p+1)/∂z
)
|z=z0:
1 = −t−2−2p(x −z0)z−1−2p
