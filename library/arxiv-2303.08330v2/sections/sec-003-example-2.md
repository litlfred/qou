---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II John Chae"
section_id: sec-003-example-2
section_title: "Example 2"
section_number: null
pages: 5-7
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
doc_brief: "A Cable Knot and BPS-Series II John Chae — This is a companion paper to earlier work of the author, which genera lizes to an inﬁnite family of (2 , 2w + 1)-cabling of the ﬁgure eight knot ( |w| > 3)"
---
The next simplest case is K = C(11,2)(41).
Proposition 3.1. The ℏ expansion of the JK,n(q) is given by
JK,n(eℏ) = 1 +
(
11− 11n2)
ℏ2 +
(
−88 + 88n2)
ℏ3 +
(11891
12 − 1137n2 + 1753
12 n4
)
ℏ4
+
(
−12826 + 47036
3 n2− 8558
3 n4
)
ℏ5 +
(69672971
360 − 991683
4 n2 + 224545
4 n4− 630551
360 n6
)
ℏ6 +···
At each ℏ order, the degree of the polynomial in n is at most the order of ℏ, which is an equivalent
characterization of the MMR expansion of the colored Jones p olynomial of a knot.
The cabling formula for the Alexander polynomial of a knot K is [8]
∆ C(p,q )(K)(t) = ∆ K(tp)∆ T(p,q )(t), 2≤ p <|q| gcd(p, q ) = 1 ,
where ∆( t) is the symmetrized Alexander polynomial and T(p,q) is the ( p, q ) torus knot. Note that
our convention for the parameters of the torus knot are switc hed (i.e. p≡ 2, q ≡ r).
Lemma 3.2. The Alexander polynomial of C(11,2)(41) is as follows.
∆ C(11, 2)(41)(x) = ∆ 41(x2)∆ T(2, 11) (x)
=−1− 1
x7 + 1
x6 + 2
x5− 2
x4 + 1
x3− 1
x2 + 1
x + x− x2 + x3− 2x4 + 2x5 + x6− x7.
From this Alexander polynomial its symmetric expansion abo ut x = 0 (in x) and x =∞ (in 1 /x )
can be computed.
Proposition 3.3. The symmetric expansion of the inverse of the Alexander polyn omial of K in
the limit of ℏ→ 0 is given by
lim
q→ 1
2FK (x, q ) = 2 s.e.
(
x1/2− x− 1/2
∆ K(x)
)
= x13/2−
(1
x
) 13/2
+ 2x17/2− 2
(1
x
) 17/2
+ 5x21/2− 5
(1
x
) 21/2
+ 13x25/2− 13
(1
x
) 25/2
+ 34x29/2− 34
(1
x
) 29/2
+ 89x33/2− 89
(1
x
) 33/2
− x35/2 +
(1
x
) 35/2
+ 233x37/2− 233
(1
x
) 37/2
− 2x39/2 + 2
(1
x
) 39/2
+ 610x41/2− 610
(1
x
) 41/2
− 5x43/2 + 5
(1
x
) 43/2
+···∈ Z
[[
x± 1/2
]]
where s.e. denotes the symmetric expansion in x about x = 0 and 1/x about x =∞.
The coeﬃcients in the expansions are integers and the Alexan der polynomial is monic, which
is a necessary condition for fm(q)’s in (1) to be polynomials. Furthermore, the coeﬃcients of
x35/2, x 39/2, x 43/2 etc are negative, which are reﬂected as negative coeﬃcient e lements in the initial
data below (cf.Proposition 3.5).
From (5) we ﬁnd the recursion relation for fm.
5
Theorem 3.4. The recursion relation for fm(q)∈ Z[q± 1] of FK (x, q ) is given by
fv+102 (q) = −1
q
115+v
2
(
1− q
89+v
2
)
[
t2f98+v + t4f94+v + t6f90+v + t8f86+v + t10f82+v + t11f80+v
+ t12f78+v + t13f76+v + t14f74+v + t15f72+v + t16f70+v + t17f68+v + t18f66+v
+ t19f64+v + t20f62+v + t21f60+v + t22f58+v + t23f56+v + t24f54+v + t25f52+v
+ t26f50+v + t27f48+v + t28f46+v + t29f44+v + t30f42+v + t31f40+v + t32f38+v
+ t33f36+v + t34f34+v + t35f32+v + t36f30+v + t37f28+v + t38f26+v + t39f24+v
+ t40f22+v + t41f20+v + t43f16+v + t45f12+v + t47f8+v + t49f4+v + t51fv
]
(6)
where ts = ts(q, q v) are Z-Laurent polynomials in q and qv.
Proposition 3.5. The initial data for (6) consists of
{
fj(q)∈ Z[q± 1]|j = 1,··· , 101
}
. All the
nonzero elements are the following.
f +
13(q) = 2 h1(q) q6
f +
17(q) = 2 h3(q) q7
f +
21(q) = 2 h5(q) q8
...
f +
57(q) = 2
(
h23(q) q17 + h1(q) q41)
f +
61(q) = 2
(
h25(q) q18 + h3(q) q46)
f +
65(q) = 2
(
h27(q) q19 + h5(q) q51)
...
f +
101(q) = 2
(
h45(q) q28 + h23(q) q96 + h1(q) q120)
...
f −
35(q) =−2 h1(q) q18
f −
39(q) =−2 h3(q) q21
f −
43(q) =−2 h5(q) q24
...
f −
79(q) =−2
(
h23 q51 + h1 q75)
f −
83(q) =−2
(
h25 q54 + h3(q) q82)
...
f −
99(q) =−2
(
h33 q66 + h11(q) q110)
After substituting them into (6), we obtain f103(q) and f105(q) as Laurent polynomials with
integer coeﬃcients, which is non-trivial because of the den ominator (1− q(89+v)/2) in (6). Recasting
6
them in terms of hs(q), we get
f −
103(q) =−2
(
h35(q) q69 + h13(q) q117)
(7)
f +
105(q) = 2
(
h47(q) q29 + h25(q) q101 + h3(q) q129)
(8)
They agree with the predictions from Conjecture 2.4 by extra polating it beyond f101(q). As another
check, ℏ expansions of (7) and (8) match with that of FC(11, 2)(41)(x, e ℏ). They can in turn be used
to conﬁrm that subsequent fm(q)’s obtained from Conjecture 2.4 agree with that of (6).
f −
107(q) =−2
(
h37(q) q72 + h15(q) q124)
f +
109(q) = 2
(
h49(q) q30 + h27(q) q106 + h5(q) q138)
Furthermore, their ℏ expansions coincide with that of FC(13, 2)(41).
Remark When h23(q) appears in f ±
b for any b, h1(q) is added.
