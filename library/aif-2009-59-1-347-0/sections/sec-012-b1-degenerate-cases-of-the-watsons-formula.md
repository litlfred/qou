---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-012-b1-degenerate-cases-of-the-watsons-formula
section_title: "B.1. Degenerate cases of the Watson's formula"
section_number: null
pages: 23-28
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
Let us ﬁrst consider the case b →aqm, where m denotes a non-negative
integer. For this purpose, we introduce the following notation
Ωm+1(x) =
m
X
k=0
qkx
qkx −1
and
Ω0(x) = 0,
Ω(x) := Ω∞(x) = lim
m→∞Ωm(x).
Notice that Ωm(x) may be identiﬁed to a logarithmic derivative as follows:
Ωm(x) = x d
dx(x; q)m
(x; q)m
= x d
dx log(x; q)m,
m ∈N ∪{∞}.
Since (x; q)m+n = (x; q)m(xqm; q)n for any m, n ∈N, it follows that
(B.4)
Ωm+n(x) = Ωm(x) + Ωn(qmx),
Ω(x) = Ωm(x) + Ω(qmx).
Let
Γq(x) = (q; q)∞
(qx; q)∞
(1 −q)1−x, deﬁned for any x /∈(−N),
be the Jackson’s Gamma function (cf. [8, §10.1]). It’s useful to remark that,
if Ψq(x) = d
dx log Γq(x), then
(B.5) Ψq(x) = −ln q Ω(qx)−ln(1−q),
Ψq(x+m) = Ψq(x)+ln q Ωm(qx),
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
369
for any non-negative integer m.
We recall that we have set
ℓ(x) := ℓq(x) = −xθ′(−x)
θ(−x) ,
where θ′(−x) denotes the derivative of θ w.r.t. at the variable x. From the
Jacobi’s triple formula θ(x) = (q, −x, −q/x; q)∞, one deduces the following
relation:
(B.6)
ℓ(x) = −Ω(x) + Ω
 q
x

.
Since Ω1(x) + Ω1( 1
x) = 1, putting m = 1 in (B.4) allows to obtain the
following relation:
ℓ(qx) −ℓ(x) = 1,
which means that, for any given non-zero complex number λ, the function
x 7→ℓ(λx) is a q-logarithm. From (B.5), one gets the following link between
ℓq and Ψq:
(B.7)
ℓ(qx) =
1
ln q (Ψq(x) −Ψq(1 −x)) .
Proposition B.2. — Let m be a non-negative integer and let a, c be
non-zero complex numbers. Suppose that a /∈q−N, c /∈q−N and c/a /∈q−N.
Then, the following formula holds:
(B.8)
2φ1(a, aqm; c; q, x) =
(aqm, c/a; q)∞
(c, qm; q)∞
θ(−ax)
θ(−x) Pm(a, c, x) +
(a, cq−m/a; q)∞
(c, q; q)∞(q−m; q)m
θ(−aqmx)
θ(−x)
×
(
[Cm(a, c) + ℓ(aqmx)] Φm(a, c, x) +
∞
X
n=1
Cm,n(a, c)φm,n(a, c, x)
)
,
where
Pm(a, c, x) = (q; q)m−1
(a; q)m
m−1
X
n=0
(a, aq/c; q)n
(q, q1−m; q)n
cq1−m
a2x
n
,
Cm(a, c) = Ω(q) + Ω(q1+m) −Ω(cq−m/a) −Ω(aqm) + 1,
Φm(a, c, x) = 2φ1(aqm, aq1+m/c; q1+m; q, cq1−m
a2x ) =
X
n⩾0
φm,n(a, c, x),
φm,n(a, c, x) = (aqm, aq1+m/c; q)n
(q, q1+m; q)n
cq1−m
a2x
n
and
Cm,n(a, c) = Ωn(aqm) + Ωn(aq1+m/c) −Ωn(q1+m) −Ωn(q).
TOME 59 (2009), FASCICULE 1
370
Lucia DI VIZIO & Changgui ZHANG
When m = 0, Pm(a, c, x) = 0.
Remark B.3. —
Equations (B.2) is a q-analog of [7, p. 109, (7)].
Proof. — Letting b = aqmϵ in (B) gives raise to the following formula:
(B.9)
2φ1(a, aqmϵ; c; q, x) =
(aqmϵ, c/a; q)∞
(c, qmϵ; q)∞
θ(−ax)
θ(−x) 2φ1

a, aq/c; q1−m/ϵ; q, cq1−m
a2ϵx

+(a, cq−m/(aϵ); q)∞
(c, q−m/ϵ; q)∞
θ(−aqmϵx)
θ(−x)
2φ1

aqmϵ, aq1+mϵ/c; q1+mϵ; q, cq1−m
a2ϵx

,
Suppose that m ⩾1. Since
(X; q)n+m =(X; q)m(Xqm; q)n,
(X; q)m =(−X)m(q1−m/X; q)mqm(m−1)/2
and
θ(qmX) = X−mq−m(m−1)/2θ(X),
we obtain
2φ1

a, aq/c; q1−m/ϵ; q, cq1−m
a2ϵx

=
m−1
X
n=0
(a, aq/c; q)n
(q, q1−m/ϵ; q)n
cq1−m
a2ϵx
n
+ (a, cq−m/a; q)m
(q, ϵ; q)m
 q
aϵx
m
∞
X
n=0
(aqm, aq1+m/c; q)n
(q1+m, q/ϵ; q)n
cq1−m
a2ϵx
n
and
(a, cq−m/(aϵ); q)∞
(c, q−m/ϵ; q)∞
θ(−aqmϵx)
θ(−x)
= −ϵ (a, cq−m/(aϵ); q)∞
(c, q/ϵ; q)∞(ϵ; q)m+1
 q
ax
m θ(−aϵx)
θ(−x) .
Hence, we can re-write (B.9) as follows:
(B.10)
2φ1(a, aqmϵ; c; q, x) = A(ϵ) + B1(ϵ)C1(ϵ) −B2(ϵ)C2(ϵ)
ϵ −1
,
where
A(ϵ) = (aqmϵ, c/a; q)∞
(c, qmϵ; q)∞
θ(−ax)
θ(−x)
m−1
X
n=0
(a, aq/c; q)n
(q, q1−m/ϵ; q)n
cq1−m
a2ϵx
n
,
B1(ϵ) = ϵ (a, cq−m/(aϵ); q)∞
(c, q/ϵ; q)∞(ϵq; q)m
 q
ax
m θ(−aϵx)
θ(−x) ,
C1(ϵ) = 2φ1

aqmϵ, aq1+mϵ/c; q1+mϵ; q, cq1−m
a2ϵx

,
B2(ϵ) = (a, cq−m/a; q)∞
(c, qϵ; q)∞(q; q)m
(aqmϵ; q)∞
(aqm; q)∞
 q
aϵx
m θ(−ax)
θ(−x) ,
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
371
C2(ϵ) =
∞
X
n=0
(aqm, aq1+m/c; q)n
(q1+m, q/ϵ; q)n
cq1−m
a2ϵx
n
.
Since B1(1) = B2(1) and C1(1) = C2(1), letting ϵ →1 in (B.10) allows us
to get the following relation:
2φ1(a, aqm; c; q, x) = A(1) + [B′
1(1) −B′
2(1)] C + B [C′
1(1) −C′
2(1)] ,
with C = C1(1), B = B1(1). By direct computation, it yields:
B′
1(1) =

1 −Ω(cq−m/a) + Ω(q) −Ωm(q) + ℓ(ax)

B,
B′
2(1) = [Ω(aqm) −Ω(q) −m] B,
C′
1(1) =
∞
X
n=1
(aqm, aq1+m/c; q)n
(q1+m, q; q)n

Ωn(aqm) + Ωn(aq1+m/c) −Ωn(q1+m) −n
 cq1−m
a2x
n
and
C′
2(1) =
∞
X
n=1
(aqm, aq1+m/c; q)n
(q1+m, q; q)n
[Ωn(q) −n]
cq1−m
a2x
n
.
Notice also that
B = (a, cq−m/a; q)∞
(c, q; q)∞(q; q)m
 q
ax
m θ(−ax)
θ(−x) =
(a, cq−m/a; q)∞
(c, q; q)∞(q−m; q)m
θ(−aqmx)
θ(−x)
,
which ends the proof when m ⩾1.
If m = 0, the term A(ϵ) disappears, so P0(a, c, x) = 0.
□
Consider now two cases for which the hypothesis of Proposition B.2 are
not all fulﬁlled: c/a ∈q−N or c = 0. Let k ∈N and c/a = q−kϵ, with ϵ →1.
Then the limit
lim
ϵ→1(q−kϵ; q)∞Ω(q−m−kϵ) = −(q−k; q)k(q; q)∞,
implies the following:
Corollary B.4. — Let k, m ∈N and a ∈C∗. The following equality
holds:
(B.11)
2φ1(a, aqm; aq−k; q, x) =
(q−k−m; q)k
(aq−k; q)k
θ(−ax)
θ(−x) 2φ1

aqm, q1+m+k; q1+m; q, q1−k−m
ax

.
TOME 59 (2009), FASCICULE 1
372
Lucia DI VIZIO & Changgui ZHANG
Taking now c →0 in (B.2) gives the following formula:
(B.12)
2φ1(a, aqm; 0; q, x) =
(aqm; q)∞
(qm; q)∞
θ(−ax)
θ(−x) Pm(a, x) +
(a; q)∞
(q; q)∞(q−m; q)m
θ(−aqmx)
θ(−x)
×
(
[Cm(a) + ℓ(aqmx)] Φm(a, x) +
∞
X
n=1
Cm,n(a)φm,n(a, x)
)
,
where
Pm(a, x) = (q; q)m−1
(a; q)m
m−1
X
n=0
(a; q)nqn(n−1)/2
(q, q1−m; q)n

−q2−m
ax
n
,
Cm(a) = Ω(q) + Ω(q1+m) −Ω(aqm) + 1,
Φm(a, x) = 1φ1(aqm; q1+m; q, q2
ax) =
X
n⩾0
φm,n(a, x),
φm,n(a, x) = (aqm; q)nqn(n−1)/2
(q, q1+m; q)n

−q2
ax
n
and
Cm,n(a) = Ωn(aqm) + n −Ωn(q1+m) −Ωn(q).
Once again, when m = 0 and Pm(a, x) = 0, we have:
(B.13)
2φ1(a, a; 0; q, x) =
(a; q)∞
(q; q)∞
θ(−ax)
θ(−x)
(
[C0(a) + ℓ(ax)] Φ0(a, x) +
∞
X
n=1
C0,n(a)φ0,n(a, x)
)
,
where
C0(a) = 2Ω(q) −Ω(a) + 1,
Φ0(a, x) = 1φ1(a; q; q, q2
ax) =
X
n⩾0
φ0,n(a, x),
φ0,n(a, x) = (a; q)nqn(n−1)/2
(q, q; q)n

−q2
ax
n
,
C0,n(a) = Ωn(a) + n −2Ωn(q).
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
