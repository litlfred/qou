---
doc_id: traczyk1991-periodic-knots
doc_title: "Periodic knots and the skein polynomial"
section_id: sec-002-3-p-0-polynomial-for-torus-knots
section_title: "P_0 polynomial for torus knots"
section_number: "3"
pages: 4-10
source_pdf: traczyk1991-periodic-knots.pdf
source_sha256: 2e9236877cec4604
toc_source: inferred
text_source: ocr (rapidocr-onnxruntime, 300 dpi, one page per PDF page; quality: prose good, display math partly lost)
doc_brief: "Periodic knots and the skein polynomial — 6 sections: Front matter; Introduction; Reduction to torus knots"
---
3 P polynomial for torus knots
where p is a prime number, and O<k<p. We still consider the coefficients
reduced modulo p. To simplify the formulae to be considered let us denote
the Po polynomial of t(p, ps + k) by T, (p and k are fixed throughout this section).
Let us begin with the following observation.
Periodic knots and the skein polynomial 77
Proposition 3.1 T, does not contain terms of degree lower than (sp + k -- 1)(p-- 1)
or higher than (sp+ k + 1)(p- 1). If s =O then T, does not contain terms of degree
higher than (k - 1)(p - 1)+ 2k - 2.
and Williams [F-W], see also [M].
Theorem 3.2 ([F-WJ, Corollary 1.9) If b is a braid on n strands with (signed)
crossing number c, then n-C--1≥emax≥emin ≥1 -- n -c where emax is the largest
the braid, and emin is the smallest exponent.
Proof of Proposition 3.1. The torus knot t(p, sp + k) may be represented by the
braid (01 .. S,-1)sp+k, in which case n=p and c- --(p- i)(sp+k). A straightfor-
ward calculation gives the claimed bounds. For the special case of (p, k) torus
knot we may use the (01...Ok-1)p presentation with n=k and c= -(k--1)p.
Again, calculation gives the claimed upper bound. 
Corollary 3.3 The area in which Ts+1 lives is that of T, with exponents shifted
by p(p-1) (upwards), e.g. for p= 5, k =2 we have Ti living between degrees 24
and 32 and T2 lives between degrees 44 and 52, i.e. between 24+ 5(5 --1) and
32 + 5(5 1).
Let us observe that (sp+k-1)(p-1)= -k+1 (mod p) and (sp+k+1)(p
- 1)= -k - 1 (mod p). This agrees very well with our comment about the mini-
mal and the maximal degree in the Po polynomial of a periodic knot. There
is only one odd number congruent (mod p) to k or -- k between (sp+ k -- 1)(p -- 1)
  s!   I+( d)( +ds) s! n s ( -d)( ds) 
segments, one of them gathering the terms of degrees from (sp+k-- 1)(p-- 1)
to (sp+k- 1)(p- 1)+2k-2 and the second gathering terms of degrees from
(sp+k - 1)(p-- 1)+ 2k to (sp+k+1)(p-1). We denote these two segments of
the polynomial T, by Ls and Hs respectively (L and H stand for lower and
higher terms respectively). By Proposition 3.1 Ho = O, so we can write the follow-
ing formulae.
(3.4) T = Ls +Hs
To= Lo
What we want to show is that Ls and H, are regular. We begin by proving
the following formula.
Lemma 3.5 For s ≥ 1
(3.6)
Before proving the lemma let us illustrate it with 2 examples.
Example 3.7 p= 5, k = 3, s= 2. A direct computation shows that To = 218 -- 2110
+2112, Ti = - [28 + [30 - [32 - 2134 + 2136, T2= [48 -150 + 152 + [54 -[56, and there-
takes the form
T2 = [20 Ti + [60 Lo - [90 H1
78 P. Traczyk
or after substituting the computed values
 [48 + 150 - [52 - 2154 + 2156
zs1+os1-8tl+ =9sl +sl +zsl +osl 8l
- 2 154 + 2 156
which of course is easily verified to be true.
Example 3.8, p=7, k= 5, s=1. A direct _computation shows that To =3124
-3126 +3128 -- 3130 +3132, Ti = [66 - [68 +170 -- [72 +174 +3176 - 3178, and there-
fore Lo=31-32_31-30 +31-2831-26 +31-24, H1 = --31-78 +31-76. The con-
sidered equality takes the form
Ti = - [42 To- [98 Lo- [154 H,
or after substituting the computed values
- 3 [66 + 3 [68 - 3170 + 3172 - 3174
[66 - [68 +170 -172 +174 + 3176  3178  - 3166 + 3168 - 3170 + 3172 - 3174
+ 3176 3178
which is also obviously true.
Proof of the lemma. We use the formula for T, derived in Sect. 2.
z(-d)sd+(I-)a(zl )(azl+ I)+(I+ds)a(zl)= (L)
s-1
i=0 i1
The general idea of the proof may be described as follows. The formula we
want to prove expresses T, as a linear combination of T,-1, Hi and Lo. If
in formula (2.7) each term of the form T or T, is written as H;+ L; or H;+Li,
then it may be seen that the 3 terms we need on the right-hand side do appear,
as well as many terms which we do not need. Our problem is therefore to
show that all the other terms are eventually canceled. This is in fact easier
that might be expected: it turns out all the unwanted terms live outside the
area in which T, lives, while the three terms we need live inside this area. This
implies that the unwanted terms must cancel. In the following calculations we
will denote the frequently appearing product p(p -- 1)/2 with r.
Let us first consider s= 1 as a special case. In this case the right-hand side
of (2.7) reduces to
(-12)p(p+-1) Ti +(1+[2P)(-[2)p(k- 1)+r To +(1+[2P)(-[2) To,
and the right-hand side of (3.6) reduces to
H(1 -+d)a(z1)+° +(I- )a(z1)+ (l )
We can rewrite the right-hand side of (2.7) as
I (1 -+d)a(z1 )+(° ++(1 - )a(z1 )+ (z1) I
+ [2p(- [2) To +(-[2)p(k- 1)+r To).
Periodic knots and the skein polynomial 79
We can then use formula (3.4) to rewrite this again as
H (- +d)a(zl -)+(° ++(1 - )a(l -)+° (zl -) I
 I (I - +d)a(zl -)+(° ++(I - )a(z1 -)+ (zl-)azl +
A direct computation shows that the three terms in the first line of the above
formula (which are the three terms we want) live in the area from degree
(k --1)(p- 1) to degree (k-1)(p-1)+ 2k- 2, while the remaining three terms
live in the area above (k + 1) (p -- 1) which proves that they must cancel.
In the general case (s ≥2) we can rewrite the right-hand side of (2.7) (after
some regrouping) as
1(-[2) T,-1 +(-[2)p(k- 1)+sr T
+[2P(-[2) T-1 +(-12)p(k-1)+sr T
s-1
+(1 + [2P) (- [2)p(k- 1) + sr 
i=2 i=2
+(-[2)p(sp+k- 1) T
Then we can use formulae (3.4) to rewrite the above in yet another form (the
second term of the first line is just renamed, the third term is written as a
sum of two terms, one of which is moved to the last line)
(3.9)
+[2P(-[2) T,-1 +(-[2)p(k-1)+sr i
s-1
+(1 + [2P) ((- [2)p(k- 1)+ sr
i=2 i=2
The first line of (3.9) is easily identified with the right-hand side of (3.6),
and computation shows that the first term lives in the area from (s p + k -- 1)(p -- 1)
to (sp+k+1)(p-1) (same as T) the second from (sp+k- 1)(p-1) to (sp+k
 ()(s)     (  ) ()(
(sp+k +1)(p-1) (same as Hs). What remains to be done is showing that the
only terms of degrees greater than (sp+ k+ 1)(p- 1)-- the highest degree that
may possibly appear in T. This is clearly true for the three terms in the second
line, because the area in which these terms live is that in which the terms from
the first line live shifted by 2p upwards. A similar argument works for the last
As for the terms gathered under the two Z signs: if in the second sum we
increase the index i by one, then the area in which T-(it1) lives is that of
T,-i shifted by p(p- 1) downwards, but the coefficient (-j2)p(i+1)(p+1)-2)2  is
equal to (-[2jp(ip+1)-2)/2 increased' by p(p+ 1), which means that the area in
which the i+1 term of the sum lives is that of the i-th term shifted by 2p
upwards. We have demonstrated that for i=- 1 the term (1 + [2P)(-[2)p(1(p+ i)- 2)/2
(split into two terms in our formula) lives in the area beginning from the degree
(sp+ k--1)(p--1). This implies immediately that the higher terms live in the
80 P. Traczyk
area above the degree (sp+k + 1)(p -- 1). A similar argument works for the first
sum. As for the last term, (-}2ypisp+k-1) T, direct computation shows that it
lives in the area beginning with the degree -(sp+k+1)(p- 1)+2p(sp+k -1)
=(sp+k+1)(p-1)+2(sp+k+1)-4p. We are now considering s≥2 so
2(sp+k+ 1)-4p>0 which implies that the degrees appearing in (- 12jp(sp+k- 1) T,
are indeed higher than (sp+k +1)(p- 1). This completes the proof of Lem-
ma 3.5.
The formula for T, given in Lemma 3.5 may be rewritten in the following
form.
°T z/(I -d)ds+(I - a(zl )= I -" z/(I -d)a(zl )
An essential step in our proof is to analyze closely the left-hand side of this
equation. We will prove the following lemma.
Lemma 3.10 For s ≥1 the polynomial T, -(--1[2)p(p- 1)/2 T,-1 is regular.
First, we rewrite (3.6) in yet another form, by separating the higher terms and
the lower terms to obtain two equalities.
 z/(1-d)ds+(I- )a(zl) I-ST z/(-d)a(zl)
The lemma guarantees that both left sides are regular which implies immediately
that H, and Lo, and therefore also H and Lo, are regular. Now, an obvious
induction proves that H, and Ls are regular for s ≥ 1, which completes the proof.
The last remaining step in the proof of Theorem 1.1 is to prove Lemma 3.10.
To do this we will need a formula for the skein polynomial of torus knots
derived by Jones [J]. The Jones' formula involves the X polynomial, one of
many equivalent versions of the skein polynomial. This is a 2-variable polyno-
mial in variables q and  from which the P polynomial in the version used
in this paper is obtained by substituting m for i(Vq-1/Vq) and I for i/Vaq
directly, so we must first interpret Lemma 3.10 in terms of X.
We are only interested in Po polynomial, not the whole polynomial P Let
us observe that the higher powers of m are of the form ik(Vq-1/Vq)k=mk,
so they disappear when a substitution q= 1 is made. It follows that the Po
substituting I for Vai in the obtained one-variable polynomial. After such an
operation two consecutive terms of X(1, 2) become two consecutive terms of
even degrees in Po(a). The “i" factor in the substitution has such an effect that
one of the two coefficients remains unchanged while the other is multiplied
by --1. This means that Lemma 3.10 may be reformulated in terms of the X
polynomial in the following manner (of course we still consider the coefficients
reduced modulo p, and we use the same convention for denoting the polynomials
of torus knots. The reason for which T, is replaced with Xs rather than Xs
Periodic knots and the skein polynomial 81
is that there is a difference in the notation used for braids between [JJ and
describes the polynomial for the mirror image of the torus knot we consider).
Lemma 3.10' In the polynomial X,(1, 2)- p(p- 1)/2 Xs-1(1, 2) all non-zero terms
have equal coefficients.
Proof. We use the formula for the X polynomial of Tm,n) given in [J, Theo-
rem 9.7].
2(n - 1)(m - 1)/2
X(q, 2) = (- 1)βgBm+ (+ 1)/2
1q +β+1=n
,β≥0
II (qi-aq)
i[[]
where [t]! means (1 -g)(1 -q2)...(1 -q)
Let us consider the difference X,(q, 2)-ap(p-1)/2 X,-1(q, 2). The involved
polynomials are these associated with T(sp+k,p) and T(s- 1)p+k,p), so in both cases
1q
n= p and we have identical terms in both polynomials. In the formula
qp
2(p - 1) (sp +k - 1)/2
for X. the fraction appears while the analogous term in X,- 1
2(p- 1)(s - 1)p+k - 1)/2
is
1q
consider the difference X,(q, 2)- ap(p- 1)/2 X,-1(q, 2), and when X(s- 1) is multip-
lied by ap(p-1)/2 the exponents become equal: This enables us to rewrite the
considered difference as
1-q 2(p - 1)(sp +k- 1)/2
1qp 1-q y+β+1=p
,β≥0
II (qi-aq)
i=-?
[]![]!
The term (1 -- q-βp) is divisible by (1 -- qP) so the last formula may be rewritten
as
II (qi-q)
at
+β+1=p i[[]
,β≥0
82 P. Traczyk
where t is an integer and wg is a polynomial in q and q- i. Each of the EyJ! [βJ!
products is divisible by 1 --q exactly p--1 times so we can rewrite the formula
again as
Zug(q) II (qi-αq)
2t
1-aq v(q) (1 - q)p= 2
where ui...up-1, v are polynomials in q and q-1, and  is not divisible by
1 -- q. We know that the considered rational function reduces to a polynomial,
what we want to study is the value of this polynomial at q =- 1. It is an elementary
observation that this value is not affected if the exponents of q in the numerator
polynomial are modified within their (mod p) congruence classes. Thus we can
modify our formula without changing the value at q =- 1 to the form
p-1
Zwp(q) II (qi - Aq)
2t i=0
1-aq v(q) (1 -- q)p- 2
and finally we can rewrite it as
p-1 Zwe(q)
II (qi-q) i=1 v(q)(1 -q)p-2 .
It is now easy to see that the substitution q= 1 gives the value cat(1 + a+ .:
+ ap-1), which completes the proof of Lemma 3.10' and the proof of the main
theorem.
