---
doc_id: ant-v14-n7-s-p06
doc_title: "Moments of quadratic twists of elliptic curve L-functions over function ﬁelds"
section_id: sec-000-1-introduction-and-statement-of-results
section_title: "Introduction and statement of results"
section_number: 1
pages: 1-4
source_pdf: ant-v14-n7-s-p06.pdf
source_sha256: 4881141ef679dd5a
doc_brief: "Moments of quadratic twists of elliptic curve L-functions over function fields — 24 sections: Introduction and statement of resu; L′(; Some useful lemmas"
---
The values of L-functions at the central point of the critical strip have been the subject of considerable
interest in recent years. One way to study these central values is by considering moments in families
of L-functions. There are now precise conjectured asymptotic formulas for such moments motivated
by analogies with random matrix theory [Keating and Snaith 2000a; 2000b]. More precise asymptotic
formulas containing lower order terms were conjectured in [Conrey et al. 2003; 2005; Diaconu et al.
2003]. In the case of the Riemann zeta-function, the analogue of these conjectures is now relatively well
understood in terms of correlations of the divisor function [Conrey and Keating 2015a; 2015b; 2015c;
2016; 2019]. The moments of other degree-one L-functions have also been investigated intensively. It
remains a challenge to extend these calculations to L-functions of degree two and higher.
The ﬁrst moment of the family of derivatives of L-functions of quadratic twists of a ﬁxed modular
form was studied in [Bump et al. 1990b; Iwaniec 1990; Murty and Murty 1991]. Questions related to
the nonvanishing of L-functions in this family were considered in [Bump et al. 1990a; 1990b; Murty
and Murty 1991]. For example, it is shown independently in [Murty and Murty 1991] and [Bump et al.
1990a], using different techniques, that for a ﬁxed elliptic curve with root number equal to 1 there are
inﬁnitely many fundamental discriminants d< 0 such that its twist by d has analytic rank equal to 1.
The second moment of the family was considered by Soundararajan and Young [2010]. Unconditionally,
they obtained a lower bound for the second moment which matches the asymptotic formula conjectured by
Keating and Snaith [2000b] and assuming the generalized Riemann hypothesis (GRH) they established the
conjectured formula. Using similar ideas, again under GRH, Petrow [2014] obtained several asymptotic
formulas for moments of derivatives of these GL(2) L–functions when the sign of the functional equation
is−1.
MSC2010: primary 11M06; secondary 11M38.
Keywords: elliptic curve, L-function, rank, ﬁnite ﬁeld, correlation.
1853
1854 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
While no asymptotic formulas for moments larger than the second are known for this family, there
are lower and upper bounds of the right order of magnitude. Rudnick and Soundararajan [2005; 2006]
established unconditional lower bounds for all moments larger than the ﬁrst, and, assuming GRH, the work
of Soundararajan [2009] and its reﬁnement by Harper [2013] produced upper bounds of the conjectured
order of magnitude. Radziwiłł and Soundararajan [2015] proved upper bounds for moments below the
ﬁrst in this family of L-functions. Their techniques also allow them to obtain a one-sided central limit
for the distribution of the logarithm of these central L-values. Their result supports a conjecture by
Keating and Snaith [2000a] which can be viewed as the analogue of Selberg’s central limit theorem for
the distribution of log
⏐⏐ζ
( 1
2+ it
)⏐⏐.
In this paper we study several moment problems of comparable difﬁculty to the moment computation
of Soundararajan and Young in the function ﬁeld family of quadratic twists of an elliptic curve. Since we
are working over function ﬁelds, the results we obtain are unconditional due to the availability of GRH in
this setting.
Recently there has been a good deal of work on computing moments of L-functions in the function
ﬁeld setting. Andrade and Keating [2012] obtained an asymptotic formula for the ﬁrst moment in the
symplectic family of quadratic L-functions when the degree of the L-functions (which is a polynomial in
this case) goes to inﬁnity and the size of the ﬁnite ﬁeld is ﬁxed (see also [Hoffstein and Rosen 1992] for a
similar result). A lower order term of size approximately the cube root of the main term was computed in
[Florea 2017c]. The second, third and fourth moments were computed in [Florea 2017b; 2017a] (see
also [Diaconu 2019]). We note that the asymptotic formula for the fourth moment does not have a power
savings error term, but recovers several of the expected leading order terms in the conjectured formula
[Andrade and Keating 2014]. Obtaining an asymptotic formula with the leading order term for the fourth
moment in the family of quadratic L-functions is comparable in difﬁculty to establishing an asymptotic
formula for the second moment of L-functions of quadratic twists of an elliptic curve, and is one of the
problems we consider in this paper.
We note that for all of our results, we ﬁx the size q of the ﬁnite ﬁeld we work in and let the degree
of the L-functions go to inﬁnity. If instead one ﬁxes the degree and lets q→∞ , then Katz and Sarnak
[1999] showed that the L-functions become equidistributed in the orthogonal group, and hence computing
the various moments reduces to computing several random matrix integrals (see for example [Keating
and Snaith 2000a]). In the case of elliptic curve L-functions, the relevant equidistribution results were
established in [Hall et al. 2017].
To state our results we ﬁrst need some notation. Fix a prime power q with
(q, 6)= 1 and q≡ 1(mod 4).
Let K= Fq(t) be the rational function ﬁeld and OK= Fq[t]. Let E/K be an elliptic curve deﬁned by
y2= x3+ ax+ b, with a, b∈ OK and discriminant1= 4a3+ 27b2 such that degt(1) is minimal among
models of E/K of this form.
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1855
The normalized L-function associated to the elliptic curve E/K has the following Euler product and
Dirichlet series, which converge forℜ(s)> 1,
L(E, s):= L(E, u)
=
∑
f∈M
λ( f)udeg( f)
=
∏
P|1
(1−λ(P)udeg(P))−1∏
P ∤1
(1−λ(P)udeg(P)+ u2 deg(P))−1, (1-1)
where we set u:= q−s, and M denotes the set of monic polynomials over Fq[t]. For a more detailed
discussion of the coefﬁcients λ( f) and how to deﬁne the L-function, see Section 2.2 in [Baig and Hall
2012]. The L-function is a polynomial in u with integer coefﬁcients of degree
n:= deg(L(E, u))= deg(M)+ 2 deg(A)− 4, (1-2)
where for simplicity we denote by M the product of the ﬁnite primes where E has multiplicative reduction
and by A the product of the ﬁnite primes where E has additive reduction. Moreover, the L-function
satisﬁes a functional equation; namely, there exists ϵ(E)∈{± 1} such that
L(E, u)=ϵ(E)(√qu)nL
(
E, 1
qu
)
.
For a more precise formula for the sign of the functional equation, see Lemma 2.3 in [Baig and Hall
2012]. Now for D∈ OK with D square-free, monic of odd degree and (D,1)= 1, we consider the
twisted elliptic curve E⊗χD/K with the afﬁne model y2= x3+ D2ax+ D3b. Then the L-function
corresponding to the twisted elliptic curve has the following Dirichlet series and Euler product
L(E⊗χD, u)=
∑
f∈M
λ( f)χD( f)udeg( f)
=
∏
P|1
(1−λ(P)χD(P)udeg(P))−1 ∏
P ∤1D
(1−λ(P)χD(P)udeg(P)+ u2 deg(P))−1.
The new L-function is a polynomial of degree (n+ 2 deg(D)) and satisﬁes the functional equation
L(E⊗χD, u)=ϵ(√qu)n+2 deg(D)L
(
E⊗χD, 1
qu
)
, (1-3)
where
ϵ=ϵ(E⊗χD)=ϵdeg(D)ϵ(E)χD(M).
Hereϵdeg(D)∈{± 1} is an integer which only depends on the degree of D (see Proposition 4.3 in [Baig
and Hall 2012]).
Let H∗
2g+1 denote the set of monic, square free polynomials of degree (2g+ 1) coprime to1. Our ﬁrst
two theorems concern the ﬁrst moments of L
(
E⊗χD, 1
2
)
and L′(
E⊗χD, 1
2
)
.
1856 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
Theorem 1.1. Unlessϵ2g+1ϵ(E)=− 1 and M= 1, we have
1
|H∗
2g+1|
∑
D∈H∗
2g+1
L
(
E⊗χD, 1
2
)
= c1(M)+ Oε(q−g+ϵg),
where the value c1(M) is deﬁned in (5-6) and (5-2). In particular, the constant c1(M)⁄= 0 in this case
and we obtain an asymptotic formula.
Theorem 1.2. Unlessϵ2g+1ϵ(E)= 1 and M= 1, we have
1
|H∗
2g+1|
∑
D∈H∗
2g+1
