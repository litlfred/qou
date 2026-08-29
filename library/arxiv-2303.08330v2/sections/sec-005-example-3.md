---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II John Chae"
section_id: sec-005-example-3
section_title: "Example 3"
section_number: null
pages: 8-12
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
doc_brief: "A Cable Knot and BPS-Series II John Chae — This is a companion paper to earlier work of the author, which genera lizes to an inﬁnite family of (2 , 2w + 1)-cabling of the ﬁgure eight knot ( |w| > 3)"
---
We next consider K = C(13,2)(41).
Proposition 3.6. The ℏ expansion of the JK,n(q) is given by
JK,n(eℏ) = 1 +
(
17− 17n2)
ℏ2 +
(
−156 + 156n2)
ℏ3 +
(24749
12 − 2365n2 + 3631
12 n4
)
ℏ4
+
(
−31629 + 38662n2− 7033n4)
ℏ5 +
(203413517
360 − 8687953
12 n2 + 1969367
12 n4
− 1855937
360 n6
)
ℏ6 +···
This conﬁrms that the MMR condition is satisﬁed by K.
Lemma 3.7. The Alexander polynomial of C(13,2)(41) is given by
∆ C(13, 2)(41)(x) = ∆ 41(x2)∆ T(2, 13)(x)
=−t8− 1
t8 + t7 + 1
t7 + 2t6 + 2
t6− 2t5− 2
t5 + t4 + 1
t4− t3− 1
t3 + t2 + 1
t2− t− 1
t + 1.
Proposition 3.8. The symmetric expansion of the inverse of the Alexander polyn omial of K in
the limit of ℏ→ 0 is given by
lim
q→ 1
2FK (x, q ) = 2 s.e.
(
x1/2− x− 1/2
∆ K(x)
)
= x15/2−
(1
x
) 15/2
+ 2x19/2− 2
(1
x
) 19/2
+ 5x23/2− 5
(1
x
) 23/2
+ 13x27/2− 13
(1
x
) 27/2
+ 34x31/2− 34
(1
x
) 31/2
+ 89x35/2− 89
(1
x
) 35/2
+ 233x39/2− 233
(1
x
) 39/2
− x41/2 +
(1
x
) 41/2
+ 610x43/2− 610
(1
x
) 43/2
− 2x45/2 + 2
(1
x
) 45/2
+···∈ Z
[[
x± 1/2
]]
The coeﬃcients of x41/2 and x45/2 etc being negative is consistent with the negative coeﬃcien t
elements in the initial data below (cf. Proposition 3.10).
8
Theorem 3.9. The recursion relation for fm(q)∈ Z[q± 1] of the above FK (x, q ) is given by
fv+106 (q) = −1
q
121+v
2
(
1− q
91+v
2
)
[
t2fv+102 + t4fv+98 + t6fv+94 + t8fv+90 + t10fv+86 + t12fv+82
+ t13fv+80 + t14fv+78 + t15fv+76 + t16fv+74 + t17fv+72 + t18fv+70 + t19fv+68
+ t20fv+66 + t21fv+64 + t22fv+62 + t23fv+60 + t24fv+58 + t25fv+56 + t26fv+54
+ t27fv+52 + t28fv+50 + t29fv+48 + t30fv+46 + t31fv+44 + t32fv+42 + t33fv+40
+ t34fv+38 + t35fv+36 + t36fv+34 + t37fv+32 + t38fv+30 + t39fv+28 + t40fv+26
+ t41fv+24 + t43fv+20 + t45fv+16 + t47fv+12 + t49fv+8 + t51fv+4 + t53fv
]
(9)
where ts = ts(q, q v) are Z-Laurent polynomials in q and qv.
Proposition 3.10. The initial data for (9) consists of
{
fj(q)∈ Z[q± 1]|j = 1,··· , 105
}
. All the
nonzero elements of the set are the following.
f +
15(q) = 2 h1(q) q7
f +
19(q) = 2 h3(q) q8
f +
23(q) = 2 h5(q) q9
...
f +
67(q) = 2
(
h27(q) q20 + h1(q) q48)
f +
71(q) = 2
(
h29(q) q21 + h3(q) q53)
...
f −
41(q) =−2 h1(q) q21
f −
45(q) =−2 h3(q) q24
f −
49(q) =−2 h5(q) q27
...
f −
93(q) =−2
(
h27(q) q60 + h1 q88)
f −
97(q) =−2
(
h29(q) q63 + h3(q) q95)
...
f −
105(q) =−2
(
h33(q) q69 + h7(q) q109)
After substituting them into (9), we indeed obtain f107(q) and f109(q) as Laurent polynomials with
Z-coeﬃcients. They can be recast in terms of hs(q):
f +
107(q) = 2
(
h47(q) q30 + h21(q) q98)
(10)
f −
109(q) =−2
(
h35(q) q72 + h9(q) q116)
(11)
The predictions from Conjecture 2.4 coincide with the above . Furthermore, ℏ expansions of (10)
and (11) agree with that of FC(13, 2)(41)(x, e ℏ). These can in turn be used to conﬁrm that subsequent
9
fm(q)’s obtained from (9) again agree with that of Conjecture 2.4 .
f +
111(q) = 2
(
h49(q) q31 + h23(q) q103)
f −
113(q) =−2
(
h37(q) q75 + h11(q) q123)
Their ℏ expansions of the above results match with that of FC(13, 2)(41) as well.
Remark When h27(q) appears in f ±
b for any b, h1(q) is added.
4 (3w + 1,3)-cables (w > 3)
The quantum (or noncommutative) A-polynomial of a class of c able knot C(r,3)(41) is qualita-
tively diﬀerent from that of the (2 w + 1, 2)-cabling in Section 2. It is given by [22]
ˆAK (t, M, L ) = ( L− 1)B(t, M )− 1Q(t, M, L )
(
t6sM 3rL2− t− 6rM − 3r,
)
gcd(r, 3) = 1 , |r| > 12.
(12)
The deﬁnitions of Q(t, M, L ) and B(t, M ) are written in Appendix A. Using (3) together with (12)
yields
c0(x, q )FK (x, q ) + c1(x, q )FK (xq, q ) + c2(x, q )FK (xq2, q ) + c3(x, q )FK (xq3, q )
+ c4(x, q )FK (xq4, q ) + c5(x, q )FK (xq5, q ) = 0 ,
(13)
where c0, c 1, c 2, c 3, c 4, c 5 are rational functions. We state the nonzero initial data ne eded for (13).
Conjecture 4.1. For a (3w+1, 3)-cabling of 41 (w > 3) in ZHS 3, nonzero initial data
{
fm(q)∈ Z[q± 1]
}
={
f +
i (q)| all coeﬃcients are positive
}⨆ {
f −
j (q)| all coeﬃcients are negative
}
for (13) are determined
by the coeﬃcient functions {hs(q)} of F41(x, q ) as follows.
f +
6w+5(q) = 2 h1(q) qn (h1(q) = 1)
f +
6w+11(q) = 2 h3(q) qn+2 (h3(q) = 2)
f +
6w+17(q) = 2 h5(q) qn+4
...
f +
24w+11(q) = 2
(
h6w+3(q) qn+6w+2 + h1(q) qn+6w+2+∆)
f +
24w+17(q) = 2
(
h6w+5(q) qn+6w+4 + h3(q) qn+6w+10+∆)
f +
24w+23(q) = 2
(
h6w+7(q) qn+6w+6 + h5(q) qn+6w+18+∆)
...
f +
42w+17(q) = 2
(
h12w+5(q) qn+12w+4 + h6w+3(q) qn+30w+10+∆ + h1(q) qn+30w+10+2∆)
f +
42w+23(q) = 2
(
h12w+7(q) qn+12w+6 + h6w+5(q) qn+30w+18+∆ + h3(q) qn+30w+24+2∆)
...
10
f +
60w+23(q) = 2
(
h18w+7(q) qn+18w+6 + h12w+5(q) qn+54w+18+∆ + h6w+3(q) qn+72w+24+2∆
+h1(q) qn+72w+24+3∆)
f +
60w+29(q) = 2
(
h18w+9(q) qn+12w+8 + h12w+7(q) qn+54w+26+∆ + h6w+5(q) qn+72w+38+2∆
+h3(q) qn+72w+44+3∆ )
...
f +
78w+29(q) = 2
(
h24w+9(q) qn+24w+8 + h18w+7(q) qn+78w+26+∆ + h12w+5(q) qn+114w+38+2∆
+h6w+3(q) qn+132w+44+3∆ + h1(q) qn+132w+44+4∆ )
f +
78w+35(q) = 2
(
h24w+11(q) qn+24w+10 + h18w+9(q) qn+78w+34+∆ + h12w+7(q) qn+114w+52+2∆
+h6w+5(q) qn+132w+64+3∆ + h3(q) qn+132w+70+4∆ )
...
f −
12w+7(q) =−2 h1(q) q2n
f −
12w+13(q) =−2 h3(q) q2n+4
f −
12w+19(q) =−2 h5(q) q2n+8
...
f −
30w+13(q) =−2
(
h6w+3(q) q2n+12w+4 + h1(q) q2n+12w+4+∆)
f −
30w+19(q) =−2
(
h6w+5(q) q2n+12w+8 + h3(q) q2n+12w+14+∆)
...
f −
48w+19(q) =−2
(
h12w+5(q) q2n+24w+8 + h6w+3(q) q2n+42w+14+∆ + h1(q) q2n+42w+14+2∆)
f −
48w+25(q) =−2
(
h12w+7(q) q2n+24w+12 + h6w+5(q) q2n+42w+24+∆ + h3(q) q2n+42w+30+2∆)
...
f −
66w+25(q) =−2
(
h18w+7(q) q2n+36w+12 + h12w+5(q) q2n+72w+24+∆ + h6w+3(q) q2n+90w+30+2∆
+h1(q) q2n+90w+30+3∆ )
f −
66w+31(q) =−2
(
h18w+9(q) q2n+36w+16 + h12w+7(q) q2n+72w+34+∆ + h6w+5(q) q2n+90w+46+2∆
+h3(q) q2n+90w+52+3∆ )
...
where n∈ Z and ∆ = 9 w + 6.
We state several remarks.
Remark 1 As in the previous cabling, the above sequence terminates fo r a ﬁxed w.
Remark 2 n can be found easily from the ℏ series of FC(r, 2)(41)(x, q ). We propose a formula for n
below.
Remark 3 A power of each q-monomial increases by multiples for a positive integer fro m f ±
m to
f ±
m+6
Remark 4 Coeﬃcient functions fd(q) that do not ﬁt into the above pattern vanish.
11
Remark 5 h1(q)qs is added when h6w+3 appears in f ±
b (q) for any b.
Conjecture 4.2. For the above family of knots, the power n∈ Z in Conjecture 4.1 is given by
3w + 2.
As in the (2 w + 1, 2)-cabling case, we get fm(q) for the mirror knot m(K).
Corollary 4.3. For a (3w + 1, 3)-cabling of 41 where w <−3, its nonzero initial data {fm(q)} =
{f +
m(q)}⨆ {f −
m(q)} for a recursion relation are given by q←→ q− 1 in Conjecture 4.1.
Conjecture 4.4. For the family of the cable knots Kw = C(3w+1,3)(41) in ZHS 3 for w > 3, all of
their coeﬃcient functions f ±
m(q)∈ Z[q± 1] of FKw (x, q ) can be expressed as linear combinations of
the coeﬃcient functions {hs(q)} of F41(x, q ) following the pattern of Conjecture 4.1.
