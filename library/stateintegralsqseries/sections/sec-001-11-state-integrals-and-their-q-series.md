---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-001-11-state-integrals-and-their-q-series
section_title: "State-integrals and their q-series"
section_number: 1.1
pages: 1-4
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
1.2. q-diﬀerence equations 4
1.3. The case of the 4 1 knot 4
1.4. The case of the 5 2 knot 5
2. Proofs 6
2.1. A residue computation 6
2.2. The Taylor series of φm(x) and ~φn(x) 8
2.3. The connection with the diﬀerential operators δl and~δl 8
2.4. Proof of Theorem 1.1 10
2.5. Some auxiliary power series 10
2.6. Proof of Proposition 2.2 12
2.7. Proof of Lemma 1.5 13
3. An application: state-integrals of the 4 1 and 52 knots 14
3.1. Proof of Corollary 1.7 14
3.2. Proof of Corollary 1.8 14
Acknowledgments 15
References 15
1. Introduction
Date: April 3, 2013.
S.G. was supported in part by grant DMS-0805078 of the US National Science Foundation. R.K. was
supported in part by the Swiss National Science Foundation.
2010 Mathematics Subject Classiﬁcation: Primary 57N10. Secondary 57M25, 33F10, 39A13.
Key words and phrases: state-integrals, q-series, quantum dilogarithm, Euler triangular numbers, Nahm
equation, gluing equations, 4 1, 52.
1
2 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
1.1. State-integrals and their q-series. Multi-dimensional state integrals of products of
Faddeev’s quantum dilogarithm appear in abundance in Quantum Topology, and were stud-
ied among others by Hikami [Hik01], Dimofte–Gukov–Lennels–Zagier [DGLZ09], Andersen–
Kashaev [AK], and Kashaev–Luo–Vartanov [KLV16]. It is well-known to the experts that
such state-integrals can be written as ﬁnite sums of products of pairs of q-series and ˜q-series.
The reason for this is a factorized structure of Faddeev’s quantum dilogarithm, the struc-
ture of the set of its poles, and the speciﬁc form of exponential factors of the integrand of
the state-integrals, while its derivation is based on an application of the residue theorem.
Instead of formulating a general theorem for multi-dimensional integrals which obscures the
principle, we will give a detailed proof for the case of a family of 1-dimensional integrals and
illustrate it with some concrete examples taken from [AK, KLV16]. Similar computations
appear in mathematical physics [BDP14].
To state our results, recall that Faddeev’s quantum dilogarithm function Φb(x) is given by
[Fad95]
(1) Φ b(x) = (e2πb(x+cb);q)∞
(e2πb−1(x−cb); ˜q)∞
,
where
q =e2πib2
, ˜q =e−2πib−2
, c b = i
2(b +b−1), ℑ(b2)> 0.
Remarkably, this function admits an extension to all values of b with b2⁄∈ R≤0. Φ b(x) is a
meromorphic function of x with
poles: cb +iN b +iN b−1, zeros: −cb−iN b−iN b−1.
The functional equation
Φb(x)Φb(−x) =eπix2
Φb(0)2, Φb(0) =q
1
24 ˜q− 1
24
allows us to move Φb(x) from the denominator to the numerator of the integrand of a state-
integral.
For natural numbersA,B withB >A> 0, we consider the absolutely convergent integral
IA,B(b) =
∫
R +iϵ
Φb(x)Be−Aπix2
dx
with small positive ϵ. The condition B >A> 0 ensures not only the convergence ofIA,B(b)
forℑ(b2)> 0, but also the convergence of the q-series and the ˜q-series (for|q|,|˜q|< 1) that
appear in Theorem 1.1 below.
To express the above state-integral in terms of series, consider the generating series
(2) FA,B(q,x ) =
∞∑
m=0
(−1)AmqAm(m+1)
2
(q)B
m
xm, ~FA,B(q,x ) =FB−A,B(q,x ).
Consider the operators δ andδk (fork a positive natural number) which act on the space of
functions of x as follows
(3) ( δF )(x) =x∂xF (x), (δkF )(x) =
∞∑
s=1
sk−1qs
1−qsF (qsx).
FROM STATE INTEGRALS TO q-SERIES 3
Likewise, there are operators ~δ and~δk which act on the space of functions of ~x and with q
replaced by ˜q. It is easy to see that any two of the operators δ, δk,~δ,~δk commute and they
freely generate over Q a commutative ringD⊗ ~D, where
D = Q [δ,δ 1,δ 2,... ], ~D = Q [~δ,~δ1,~δ2,... ].
Let
Db =D[(2πi)−1,b±1,e 2,e 4,e 6,... ], ~Db = ~D[(2πi)−1,b±1,e 2,e 4,e 6,... ],
where el =el(˜q) =~δl(1)∈ Z [[˜q]]. Consider the following operator valued polynomial:
(4) PA,B = Resw=0
(
e
1
4πiw2+Aw(b(δ+ 1
2 )+b−1(eδ+ 1
2 ))
)A
(
φ(bw,δ•)~φ(b−1w,~δ•)
b(1−eb−1w)
)B
∈D b⊗ ~Db,
where
φ(w,δ•) = exp
(
−
∞∑
l=1
δl
l!wl
)
(5a)
~φ(w,~δ•) = exp(−~δw) exp
(
2
∑
l=even>0
el(˜q)wl
l!
)
exp
(
−
∞∑
l=1
~δl
l! (−w)l
)
.(5b)
For a series F (x,~x), we deﬁne:
(6) ⟨F (x,~x)⟩ =F (1, 1).
Theorem 1.1. We have:
(7) IA,B(b) =
( ˜q
q
)B−3A
24
eπiB+2(A+1)
4
⟨
PA,B
(
FA,B(q,x )~FA,B(˜q,~x)
)⟩
.
Corollary 1.2. WritingPA,B =∑
kpkPk (a ﬁnite sum), for pk∈D b andPk∈ ~Db, it follows
that
(8) IA,B(b) =
( ˜q
q
)B−3A
24
eπiB+2(A+1)
4
∑
k
gk(q)Gk(˜q)
where
(9) gk(q) =⟨pkFA,B⟩, G k(˜q) =⟨Pk~FA,B⟩.
Remark 1.3. The left hand side of Equation (8) has analytic continuation to the cut plane
C \{b2|b2 < 0} whereas each of the series gk and Gk is only well-deﬁned in the upper-half
plane{b2|ℑ(b2)> 0}.
Remark 1.4. PA,B, as a polynomial in the variables e2,e 4,... has degree B− 1, where
the degree of el is l. PA,B as a Laurent polynomial in b has b-monomials of degrees in
{−B + 1,−B + 3,...,B − 3,B− 1}.
4 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
1.2. q-diﬀerence equations. Next we describe a linear q-diﬀerence equation of FA,B(q,x ).
Consider the operators ˆx and ˆE which act on f(x)∈ Q (q)[[x]] by:
( ˆEf )(x) =f(qx), (ˆxf)(x) =xf(x).
Observe that ˆEˆx =qˆx ˆE.
Lemma 1.5. (a) We have:
(10) FA,B(q−1,x ) = ~FA,B(q,x ).
(b) FA,B satisﬁes the linear q-diﬀerence equation
(11)
(
(1− ˆE)B− (−1)AqAx ˆEA
)
FA,B(q,x ) = 0.
Corollary 1.6. (a) If we deﬁneω(q,x ) =FA,B(q,qx )/FA,B(q,x ) andω(q,x )n =∏n
j=1ω(q,q jx),
then ω satisﬁes the nonlinear equation
B∑
j=0
(−1)j
(B
j
)
ω(q,x )j− (−1)AqAxω(q,x )A = 0.
(b) F is an admissible power series in the sense of Kontsevich-Soibelman [KS11, Sec.6], the
limit limq→1ω(q,x ) = ω(x)∈ Q [[x]] exists and satisﬁes the algebraic equation (also known
as the Nahm equation or the gluing equation)
(12) (1 −ω(x))B = (−1)Axω(x)A.
The Nahm equation has been studied by several authors including [Zag07, Sec.3], [Vla,
VZ11], [RV, Sec.4].
