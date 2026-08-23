---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-008-appendix-b-expansion-of-eqx-at
section_title: "Appendix B. Expansion of Eq(x) at"
section_number: null
pages: 22-28
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
The purpose of this section is the proof of Proposition 1.5. We recall the
notation
(B.1) an+1 =
n∑
k=0
1
qk+1 − 1, n /greaterorequalslant0,
A(q) =
∑
n/greaterorequalslant0
qn+1
qn+1 − 1,
and
θ(x) =
∑
n∈Z
qn(n−1)/2xn,
and the statement of the proposition:
Proposition B.1. — For any x ∈ C∗ \q−N:
(B.2)
∑
n/greaterorequalslant0
(q;q)nxn+1 = −
(
−qxθ′(−qx)
θ(−qx) + 1 +A(q)
)(q
x ;q
)
∞
+
∑
n/greaterorequalslant1
an
(q;q)n
qn(n+1)/2
(
− 1
x
)n
.
The proof of the proposition above is based on a Watson’s formula for
basic hypergeometric functions, which is the analogue of a Barnes’ formula
for Gauss hypergeometric function. Barnes ( cf. [19, §14.51] and [ 3]) proved
that if | arg(−x)|<π ,c /∈ Z⩽0 anda−b /∈ Z, then the analytic continuation
of 2F1(a,b ;c;x) for |x|> 1 is given by:
2F1(a,b ;c;x) = Γ(c)Γ(b −a)
Γ(b)Γ(c −a) (−x)−a
2F1(a,a −c + 1,a −b + 1;x−1)
+ Γ(c)Γ(a −b)
Γ(a)Γ(c −b) (−x)−b
2F1(b,b −c + 1,b −a + 1;x−1).
TOME 59 (2009), F ASCICULE 1
368 Lucia DI VIZIO & Changgui ZHANG
G.N. Watson ( cf. [8, §4.3]) proved a formula of the same kind for Heine
series, namely if:
(B.3) x /∈q−N ∪
(cq
abqN
)
, c /∈q−N, a
b /∈qZ, abcx ⁄= 0.
then
2φ1(a,b ;c;q,x ) = (b,c/a ;q)∞
(c,b/a ;q)∞
θ(−ax)
θ(−x) 2φ1
(
a,aq/c ;aq/b;q, cq
abx
)
+ (a,c/b ;q)∞
(c,a/b ;q)∞
θ(−bx)
θ(−x) 2φ1
(
b,bq/c ;bq/a;q, cq
abx
)
,
where (α1,...,α k;q)n =∏k
i=1(αi;q)n. We are going to consider a degener-
ation of Watson’s formula letting b →a and c → 0. In this way we obtain
an expression for 2φ1(a,a ; 0;q,x ) that we can apply to
Eq(x) = x2φ1
(
q,q ; 0;q, − x
1 −q
)
.
B.1. Degenerate cases of the W atson’s formula
Let us ﬁrst consider the case b →aqm, where m denotes a non-negative
integer. For this purpose, we introduce the following notation
Ωm+1(x) =
m∑
k=0
qkx
qkx − 1
and
Ω0(x) = 0, Ω(x) := Ω ∞(x) = lim
m→∞
Ωm(x).
Notice that Ωm(x) may be identiﬁed to a logarithmic derivative as follows:
Ωm(x) = x d
dx (x;q)m
(x;q)m
=xd
dx log(x;q)m, m ∈ N ∪ {∞}.
Since (x;q)m+n = (x;q)m(xqm;q)n for any m, n ∈ N, it follows that
(B.4) Ωm+n(x) = Ω m(x) + Ωn(qmx), Ω(x) = Ω m(x) + Ω(qmx).
Let
Γq(x) = (q;q)∞
(qx;q)∞
(1 −q)1−x, deﬁned for any x /∈ (−N),
be the Jackson’s Gamma function ( cf. [8, §10.1]). It’s useful to remark that,
if Ψq(x) = d
dx log Γq(x), then
(B.5) Ψq(x) = − lnq Ω(qx)−ln(1−q), Ψq(x+m) = Ψ q(x)+lnq Ωm(qx),
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 369
for any non-negative integer m.
We recall that we have set
𝓁(x) := 𝓁q(x) = −xθ′(−x)
θ(−x),
whereθ′(−x) denotes the derivative of θ w.r.t. at the variable x. From the
Jacobi’s triple formula θ(x) = (q, −x, −q/x;q)∞, one deduces the following
relation:
(B.6) 𝓁(x) = −Ω(x) + Ω
(q
x
)
.
Since Ω1(x) + Ω 1( 1
x ) = 1 , putting m = 1 in ( B.4) allows to obtain the
following relation:
𝓁(qx) −𝓁(x) = 1,
which means that, for any given non-zero complex number λ, the function
x ↦→𝓁(λx) is a q-logarithm. From (B.5), one gets the following link between
𝓁q and Ψq:
(B.7) 𝓁(qx) = 1
lnq (Ψq(x) − Ψq(1 −x)).
Proposition B.2. — Let m be a non-negative integer and let a, c be
non-zero complex numbers. Suppose that a /∈q−N,c /∈q−N andc/a /∈q−N.
Then, the following formula holds:
(B.8) 2φ1(a,aq m;c;q,x ) =
(aqm,c/a ;q)∞
(c,q m;q)∞
θ(−ax)
θ(−x) Pm(a,c,x ) + (a,cq −m/a;q)∞
(c,q ;q)∞(q−m;q)m
θ(−aqmx)
θ(−x)
×
{
[Cm(a,c ) +𝓁(aqmx)] Φm(a,c,x ) +
∞∑
n=1
Cm,n(a,c )φm,n(a,c,x )
}
,
where
Pm(a,c,x ) = (q;q)m−1
(a;q)m
m−1∑
n=0
(a,aq/c ;q)n
(q,q 1−m;q)n
(cq1−m
a2x
)n
,
Cm(a,c ) = Ω(q) + Ω(q1+m) − Ω(cq−m/a) − Ω(aqm) + 1,
Φm(a,c,x ) = 2φ1(aqm,aq 1+m/c;q1+m;q,cq1−m
a2x ) =
∑
n/greaterorequalslant0
φm,n(a,c,x ),
φm,n(a,c,x ) = (aqm,aq 1+m/c;q)n
(q,q 1+m;q)n
(cq1−m
a2x
)n
and
Cm,n(a,c ) = Ω n(aqm) + Ωn(aq1+m/c) − Ωn(q1+m) − Ωn(q).
TOME 59 (2009), F ASCICULE 1
370 Lucia DI VIZIO & Changgui ZHANG
When m = 0, Pm(a,c,x ) = 0 .
Remark B.3. — Equations ( B.2) is a q-analog of [ 7, p. 109, (7)].
Proof. — Letting b =aqmϵ in ( B) gives raise to the following formula:
(B.9) 2φ1(a,aq mϵ;c;q,x ) =
(aqmϵ,c/a ;q)∞
(c,q mϵ;q)∞
θ(−ax)
θ(−x) 2φ1
(
a,aq/c ;q1−m/ϵ;q,cq1−m
a2ϵx
)
+ (a,cq −m/(aϵ);q)∞
(c,q −m/ϵ;q)∞
θ(−aqmϵx)
θ(−x) 2φ1
(
aqmϵ,aq 1+mϵ/c;q1+mϵ;q,cq1−m
a2ϵx
)
,
Suppose that m /greaterorequalslant1. Since
(X;q)n+m = (X;q)m(Xq m;q)n, (X;q)m = (−X)m(q1−m/X;q)mqm(m−1)/2
and
θ(qmX) = X −mq−m(m−1)/2θ(X),
we obtain
2φ1
(
a,aq/c ;q1−m/ϵ;q,cq1−m
a2ϵx
)
=
m−1∑
n=0
(a,aq/c ;q)n
(q,q 1−m/ϵ;q)n
(cq1−m
a2ϵx
)n
+ (a,cq −m/a;q)m
(q,ϵ ;q)m
( q
aϵx
)m ∞∑
n=0
(aqm,aq 1+m/c;q)n
(q1+m,q/ϵ ;q)n
(cq1−m
a2ϵx
)n
and
(a,cq −m/(aϵ);q)∞
(c,q −m/ϵ;q)∞
θ(−aqmϵx)
θ(−x) = −ϵ (a,cq −m/(aϵ);q)∞
(c,q/ϵ ;q)∞(ϵ;q)m+1
( q
ax
)m θ(−aϵx)
θ(−x) .
Hence, we can re-write ( B.9) as follows:
(B.10) 2φ1(a,aq mϵ;c;q,x ) = A(ϵ) + B1(ϵ)C1(ϵ) −B2(ϵ)C2(ϵ)
ϵ − 1 ,
where
A(ϵ) = (aqmϵ,c/a ;q)∞
(c,q mϵ;q)∞
θ(−ax)
θ(−x)
m−1∑
n=0
(a,aq/c ;q)n
(q,q 1−m/ϵ;q)n
(cq1−m
a2ϵx
)n
,
B1(ϵ) = ϵ (a,cq −m/(aϵ);q)∞
(c,q/ϵ ;q)∞(ϵq;q)m
( q
ax
)m θ(−aϵx)
θ(−x) ,
C1(ϵ) = 2φ1
(
aqmϵ,aq 1+mϵ/c;q1+mϵ;q,cq1−m
a2ϵx
)
,
B2(ϵ) = (a,cq −m/a;q)∞
(c,qϵ ;q)∞(q;q)m
(aqmϵ;q)∞
(aqm;q)∞
( q
aϵx
)m θ(−ax)
θ(−x) ,
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 371
C2(ϵ) =
∞∑
n=0
(aqm,aq 1+m/c;q)n
(q1+m,q/ϵ ;q)n
(cq1−m
a2ϵx
)n
.
Since B1(1) = B2(1) and C1(1) = C2(1), letting ϵ → 1 in ( B.10) allows us
to get the following relation:
2φ1(a,aq m;c;q,x ) = A(1) + [B′
1(1) −B′
2(1)]C +B [C ′
1(1) −C ′
2(1)],
with C =C1(1), B =B1(1). By direct computation, it yields:
B′
1(1) =
[
1 − Ω(cq−m/a) + Ω(q) − Ωm(q) +𝓁(ax)
]
B,
B′
2(1) = [Ω(aqm) − Ω(q) −m]B,
C ′
1(1) =
∞∑
n=1
(aqm,aq 1+m/c;q)n
(q1+m,q ;q)n
[
Ωn(aqm) + Ωn(aq1+m/c) − Ωn(q1+m) −n
](cq1−m
a2x
)n
and
C ′
2(1) =
∞∑
n=1
(aqm,aq 1+m/c;q)n
(q1+m,q ;q)n
[Ωn(q) −n]
(cq1−m
a2x
)n
.
Notice also that
B = (a,cq −m/a;q)∞
(c,q ;q)∞(q;q)m
( q
ax
)m θ(−ax)
θ(−x) = (a,cq −m/a;q)∞
(c,q ;q)∞(q−m;q)m
θ(−aqmx)
θ(−x) ,
which ends the proof when m /greaterorequalslant1.
If m = 0, the term A(ϵ) disappears, so P0(a,c,x ) = 0 . □
Consider now two cases for which the hypothesis of Proposition B.2 are
not all fulﬁlled: c/a ∈q−N orc = 0. Let k ∈ N andc/a =q−kϵ, with ϵ → 1.
Then the limit
lim
ϵ→1
(q−kϵ;q)∞Ω(q−m−kϵ) = −(q−k;q)k(q;q)∞,
implies the following:
Corollary B.4. — Let k, m ∈ N and a ∈ C∗. The following equality
holds:
(B.11) 2φ1(a,aq m;aq−k;q,x ) =
(q−k−m;q)k
(aq−k;q)k
θ(−ax)
θ(−x) 2φ1
(
aqm,q 1+m+k;q1+m;q,q1−k−m
ax
)
.
TOME 59 (2009), F ASCICULE 1
372 Lucia DI VIZIO & Changgui ZHANG
Taking now c → 0 in ( B.2) gives the following formula:
(B.12) 2φ1(a,aq m; 0;q,x ) =
(aqm;q)∞
(qm;q)∞
θ(−ax)
θ(−x) Pm(a,x ) + (a;q)∞
(q;q)∞(q−m;q)m
θ(−aqmx)
θ(−x)
×
{
[Cm(a) +𝓁(aqmx)] Φm(a,x ) +
∞∑
n=1
Cm,n(a)φm,n(a,x )
}
,
where
Pm(a,x ) = (q;q)m−1
(a;q)m
m−1∑
n=0
(a;q)nqn(n−1)/2
(q,q 1−m;q)n
(
−q2−m
ax
)n
,
Cm(a) = Ω(q) + Ω(q1+m) − Ω(aqm) + 1,
Φm(a,x ) = 1φ1(aqm;q1+m;q, q2
ax ) =
∑
n/greaterorequalslant0
φm,n(a,x ),
φm,n(a,x ) = (aqm;q)nqn(n−1)/2
(q,q 1+m;q)n
(
−q2
ax
)n
and
Cm,n(a) = Ω n(aqm) +n − Ωn(q1+m) − Ωn(q).
Once again, when m = 0 and Pm(a,x ) = 0 , we have:
(B.13) 2φ1(a,a ; 0;q,x ) =
(a;q)∞
(q;q)∞
θ(−ax)
θ(−x)
{
[C0(a) +𝓁(ax)] Φ0(a,x ) +
∞∑
n=1
C0,n(a)φ0,n(a,x )
}
,
where
C0(a) = 2Ω(q) − Ω(a) + 1, Φ0(a,x ) = 1φ1(a;q;q, q2
ax ) =
∑
n/greaterorequalslant0
φ0,n(a,x ),
φ0,n(a,x ) = (a;q)nqn(n−1)/2
(q,q ;q)n
(
−q2
ax
)n
, C 0,n(a) = Ω n(a) +n − 2Ωn(q).
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 373
