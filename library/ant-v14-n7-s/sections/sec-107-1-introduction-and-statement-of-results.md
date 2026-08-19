---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-107-1-introduction-and-statement-of-results
section_title: "Introduction and statement of results"
section_number: 1
pages: 187-192
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
ϵ−L′(
E⊗χD, 1
2
)
= c2(M)L(Sym2 E, 1)g+ c3(M)+ Oε(q−g+ϵg),
where the values c2(M) and c3(M) are deﬁned in (6-2), (6-3) and (5-2). In particular , the constant
c2(M)⁄= 0 in this case and we obtain an asymptotic formula.
Theorem 1.2 above should be compared to the number ﬁeld analogous result in [Iwaniec 1990]. In
the following theorems we obtain asymptotic formulas for the second moments of L
(
E⊗χD, 1
2
)
and
L′(
E⊗χD, 1
2
)
.
Theorem 1.3. Unlessϵ2g+1ϵ(E)=− 1 and M= 1, we have
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
)2= c4(M)L(Sym2 E, 1)3g+ Oε(g1/2+ε),
where the value c4(M) is deﬁned in (7-2), (3-8) and (3-9). In particular, the constant c4(M)⁄= 0 in this
case and we obtain an asymptotic formula.
Theorem 1.4. Unlessϵ2g+1ϵ(E)= 1 and M= 1, we have
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−L′(
E⊗χD, 1
2
)2= c5(M)L(Sym2 E, 1)3g3+ Oε(g2+ϵ),
where the value c5(M) is deﬁned in (8-2), (3-8) and (3-9). In particular, the constant c5(M)⁄= 0 in this
case and we obtain an asymptotic formula.
Note that Theorem 1.3 is the function ﬁeld analogue of Theorem 1.2 in [Soundararajan and Young
2010]. Considering the smoothed second moment, Soundararajan and Young obtain an error term of
size(log X)3/4+ϵ, which would translate to g3/4+ϵ in the function ﬁeld setting. Using slightly different
techniques, Petrow [2014] states that the error term could be improved to (log X)1/2+ϵ which is of the
same quality we obtain in the result above.
Our Theorem 1.3 should also be compared to the asymptotic formula for the fourth moment of quadratic
L-functions over function ﬁelds in [Florea 2017a]. We remark that for the symplectic family of quadratic
L-functions, one can obtain lower order terms in the asymptotic formula by using an inductive argument
and then obtaining upper bounds for moments of L-functions evaluated at points far from the critical
point. The fact that one can compute a few lower order terms can be explained by the gap between
Moments of quadratic twists of elliptic curveL-functions over function ﬁelds 1857
powers of g coming from evaluating moments at the critical point versus evaluating moments far from the
critical point. When computing the fourth moment of quadratic L-functions close to the central point, one
expects to obtain a power of g10. As we move away from the central point, the family starts to behave
like a family with unitary symmetry and one expects an upper bound of the magnitude g4. The difference
in powers of g gives one room to use a repetitive argument to rigorously compute lower order terms
down to g4. In the case of the orthogonal family we consider in this paper, note that the main term in
Theorem 1.3 is of size g, and the error term has size g1/2 coming from obtaining an upper bound for
the second moment evaluated at a point far from the central point. The small difference between these
powers of g does not give us enough room to compute a lower order term in this case.
We can also study the moment of the product of the quadratic twists of two elliptic curve L-functions.
Let E1 and E2 be two elliptic curves over K . Let 1=1112, where, for i= 1, 2, 1i denotes the
discriminant of Ei. Let Mi denote the product of the ﬁnite primes where Ei has multiplicative reduction
and
ϵi=ϵdeg(D)ϵ(Ei)χD(Mi).
Deﬁne
ϵ+
i := 1+ϵi
2 and ϵ−
i := 1−ϵi
2 .
Theorem 1.5. Unlessϵ2g+1ϵ(E1)=− 1 and M1= 1, orϵ2g+1ϵ(E2)= 1 and M2= 1, orϵ(E1)=ϵ(E2)
and M1= M2, we have
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−
2 L
(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
= c6(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗ E2, 1)g+ Oε(g1/2+ε),
where the valuec6(M1, M2) is deﬁned in(9-2), (3-8) and (3-10). In particular, the constant c6(M1, M2)⁄=0
in this case and we obtain an asymptotic formula.
We are not aware of the analogous number ﬁeld result in the literature. We also prove the following.
Theorem 1.6. Unlessϵ2g+1ϵ(E1)= 1 and M1= 1, orϵ2g+1ϵ(E2)= 1 and M2= 1, orϵ(E1)=−ϵ(E2)
and M1= M2, we have
1
|H∗
2g+1|
∑
D∈H∗
2g+1
ϵ−
1ϵ−
2 L′(
E1⊗χD, 1
2
)
L′(
E2⊗χD, 1
2
)
= c7(M1, M2)L(Sym2 E1, 1)L(Sym2 E2, 1)L(E1⊗ E2, 1)g2+ Oε(g1+ε),
where the valuec7(M1,M2) is deﬁned in(10-2), (3-8) and (3-10). In particular, the constant c7(M1,M2)⁄=0
in this case and we obtain an asymptotic formula.
Note that this result is the analogue of Theorem 2.2 in [Petrow 2014]. An interesting problem would be
to compute the average of L
(
E1⊗χD, 1
2
)
L
(
E2⊗χD, 1
2
)
for distinct elliptic curves E1 and E2. This would
have applications to the question of simultaneous nonvanishing of L
(
E1⊗χD, 1
2
)
and L
(
E2⊗χD, 1
2
)
.
1858 Hung M. Bui, Alexandra Florea, Jonathan P. Keating and Edva Roditty-Gershon
However our techniques do not allow us to obtain such an asymptotic formula, as the error term (coming
from Proposition 4.7) would dominate the main term which would have constant size.
Deﬁne the analytic rank of a quadratic twist of an elliptic curve L-function L(E⊗χD, s) by
rE⊗χD:= ords=1/2 L(E⊗χD, s).
Combining the upper bounds for moments of elliptic curve L-functions (see Section 4) with Theorems 1.5
and 1.6 leads to the following corollary.
Corollary 1.7. Unlessϵ2g+1ϵ(E1)=− 1 and M1= 1, orϵ2g+1ϵ(E2)= 1 and M2= 1, orϵ(E1)=ϵ(E2)
and M1= M2, we have
#{D∈ H∗
2g+1: rE1⊗χD= 0, rE2⊗χD= 1}≫ε
q2g
g6+ε
as g→∞ . Also, unlessϵ2g+1ϵ(E1)= 1 and M1= 1, orϵ2g+1ϵ(E2)= 1 and M2= 1, orϵ(E1)=−ϵ(E2)
and M1= M2, we have
#{D∈ H∗
2g+1: rE1⊗χD= rE2⊗χD= 1}≫ε
q2g
g6+ε
as g→∞ .
As far as we are aware, Corollary 1.7 is the ﬁrst result in literature where explicit lower bounds
concerning the correlations between the ranks of two twisted elliptic curves are obtained. Following
Harper’s argument [2013], for the upper bounds for moments of L-functions one may remove the
exponentsε in Corollary 1.7. We fail to obtain positive proportions in the above results because we are
not able to use a molliﬁer. Note that the results of Heath-Brown [2004] adapted to the function ﬁeld
setting do not lead to positive proportions either.
