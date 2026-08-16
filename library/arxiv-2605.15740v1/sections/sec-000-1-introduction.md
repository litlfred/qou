---
doc_id: arxiv-2605.15740v1
doc_title: "BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
doc_brief: "BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANTS — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´ e homology"
---
In 1999, Lawrence and Zagier made a prescient observation connecting quantum invariants
and modular forms [23]. To state their result, letZ ζ(M) denote the Witten-Reshetikhin-Turaev
(WRT) invariant of a closed and oriented 3-manifoldMat the root of unityζ. Next let
p= (p 1,p 2,p 3) be a triple of pairwise coprime positive integers andP:=p 1p2p3. For any
tripleℓ= (ℓ 1,ℓ 2,ℓ 3)∈Z 3 satisfying 0<ℓ j <p j, define the odd periodic function
χℓ
p(n) =



−ϵ1ϵ2ϵ3 ifn≡P

1 +
3X
j=1
ϵjℓj
pj

 (mod 2P),
0 otherwise
whereϵ= (ϵ 1,ϵ 2,ϵ 3)∈{±1} 3. Forq=e 2πiτ ,τ∈H, consider the Eichler integral
eΦℓ
p(τ) :=
∞X
n=0
χℓ
p(n)q
n2
4P (1.1)
of the weight 3/2 modular form
Φℓ
p(τ) :=
∞X
n=0
nχℓ
p(n)q
n2
4P.
Date: May 18, 2026.
2020Mathematics Subject Classification.11F27, 33D15, 57K16.
Key words and phrases.Bailey pairs,q-multisums, Eichler integrals.
1
arXiv:2605.15740v1  [math.NT]  15 May 2026
2 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
Their main result [23, Theorem 1] reads as follows. For coprime positive integersMandN, let
ζM
N :=e
2πiM
N . Then for the Poincar´ e homology sphere Σ(2,3,5) we have
1 +ζM
N (1−ζ M
N )ZζM
N
(Σ(2,3,5)) =− 1
2 lim
τ→M
N
q− 1
120eΦ(1,1,1)
(2,3,5)(τ).(1.2)
They also established that the right-hand side of (1.2) has “a modular property modulo smooth
functions”, a notion which would later become the defining attribute of Zagier’s quantum mod-
ular forms [36]. Any Eichler integral defined by (1.1) is now known to be an example of a
quantum modular form [14, Section 4.4].
Following up on the work of Lawrence and Zagier, Hikami wrote a series of papers [16–19]
wherein he showed that limiting values of Eichler integrals give the WRT invariants for several
families of 3-manifolds, including the Brieskorn homology spheres. As an application, he used
the modularity to find asymptotic expansions forZ ζN (M) asN→∞. Hikami’s results have
recently been used in the study of limiting values of an SU(2) WRT function [2,3,9] and towards
progress on a quantum modularity conjecture for WRT invariants [30, Theorem 1].
The identity (1.2) may be recast as an identity forq-hypergeometric series at roots of unity
using Habiro’s unified WRT invariant. Habiro [15] showed that ifMis an integral homology
sphere, there is aq-hypergeometric seriesI(M;q) such that for any root of unityζone has
I(M;ζ) =Z ζ(M).
In the case of the Poincar´ e homology sphere, the unified WRT invariant is [24]
I(Σ(2,3,5);q) = 1
1−q
X
n≥0
qn(qn+1)n+1,
where
(a)n = (a;q)n :=
nY
k=1
(1−aq k−1).
Thus (1.2) says that
H(ζM
N ) =− 1
2 lim
τ→M
N
q− 1
120eΦ(1,1,1)
(2,3,5)(τ),(1.3)
where
H(q) :=
X
n≥0
qn(qn)n.
Explicit expressions forI(M;q) are uncommon as they require knowledge of the cyclotomic
expansion of the colored Jones polynomial of the knotKfrom whichMis constructed using
Dehn surgery. One case where this has been fully carried out is for the Brieskorn homology
spheres Σ(2,3,6p−1) and Σ(2,3,6p+ 1), which arise from (−1)-surgery and (+1)-surgery,
respectively, along the twist knotK p,p>0 [21, Theorem C.1]. Specifically, Hikami [21] showed
that one has
(1−q)I(Σ(2,3,6p−1);q) =H (1)
p (q) (1.4)
forp>1 and
(1−q)I(Σ(2,3,6p+ 1);q) =H (8)
p (q) (1.5)
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 3
forp≥1 where 1
H (1)
p (q) :=
X
np≥···≥n1≥0
qnp(qnp+1)np+1
p−1Y
i=1
qni(ni+1)

ni+1
ni

(1.6)
and
H (8)
p (q) :=
X
np≥···≥n1≥0
q−np(np+2)(qnp+1)np+1
p−1Y
i=1
qni(ni+1)

ni+1
ni

.(1.7)
Here 
n
k

:= (q)n
(q)n−k(q)k
(1.8)
is theq-binomial coefficient. Combining (1.4) and (1.5) with expressions for the WRT invariants
of the Brieskorn homology spheres in terms of Eichler integrals [16], Hikami deduced the identities
[21, Theorem 3.3]
H (1)
p (ζN) = (1−ζ N)I(Σ(2,3,6p−1);ζ N) =− 1
2 lim
τ→ 1
N
q− (6p+5)2
24(6p−1)eΦ(1,1,1)
(2,3,6p−1)(τ) (1.9)
forp>1 and [21, Theorem 2.4 and Proposition 3.2]
H (8)
p (ζN) = (1−ζ N)I(Σ(2,3,6p+ 1);ζ N) =− 1
2 lim
τ→ 1
N
q1− (6p−5)2
24(6p+1)eΦ(1,1,1)
(2,3,6p+1)(τ) (1.10)
forp≥1.
In [21], Hikami conjectured a number of identities forq-series at roots of unity which closely
resemble (1.3), (1.9) and (1.10) but for which no interpretation in terms of quantum invariants
is known. These conjectures are also presented in [29] and two more were made in private
communication [22]. To state them, we define the following families ofq-series. Forp≥1, let
H (2)
p (q) :=
X
np≥···≥n1≥0
qnp(qnp)np
p−1Y
i=1
qn2
i

ni+1
ni

,(1.11)
H (3)
p (q) :=
X
np≥···≥n1≥0
q2np(qnp+1)np
p−1Y
i=1
qni(ni+1)

ni+1
ni

,(1.12)
H (4)
p (q) :=
X
np≥···≥n1≥0
qnp(qnp+1)np
p−1Y
i=1
qni(ni+1)

ni+1
ni

,(1.13)
H (5)
p (q) :=
X
np≥···≥n1≥0
qnp(qnp+1)np
p−1Y
i=1
qn2
i

ni+1
ni

,(1.14)
H (6)
p (q) :=
X
np≥···≥n1≥0
q−n2
p(qnp+1)np
p−1Y
i=1
qn2
i +ni

ni+1
ni

(1.15)
1Here and throughout, we follow the notationH (i)
p (q) for theq-multisums (1.6) and (1.11)–(1.14) as given
in [29]. We have labelled (1.7), (1.15), (1.16), (1.24) and (1.25) accordingly.
4 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
and
H (7)
p (q) :=
X
np≥···≥n1≥0
q−n2
p−np(qnp+1)np
p−1Y
i=1
qn2
i +ni

ni+1
ni

.(1.16)
In [21, (3.23), (3.25b)–(3.25d), (3.35)] and [22], the following conjectures were made.
Conjecture 1.1.We have
H (2)
2 (ζN) =− 1
2 lim
τ→ 1
N
q− 1
264eΦ(1,1,2)
(2,3,11)(τ),(1.17)
H (3)
2 (ζN) =− 1
2 lim
τ→ 1
N
q−(1+ 49
264 )eΦ(1,1,3)
(2,3,11)(τ),(1.18)
H (4)
1 (ζN) =− 1
2 lim
τ→ 1
N
q− 49
120eΦ(1,1,2)
(2,3,5)(τ),(1.19)
H (4)
2 (ζN) =− 1
2 lim
τ→ 1
N
q− 169
264eΦ(1,1,4)
(2,3,11)(τ),(1.20)
H (5)
p (ζN) =− 1
2 lim
τ→ 1
N
q
1+48p
24(1−6p)eΦ(1,1,3p−1)
(2,3,6p−1)(τ) (1.21)
wherep≥1,
H (6)
1 (ζN) =− 1
2 lim
τ→ 1
N
q− 25
168eΦ(1,1,2)
(2,3,7)(τ) (1.22)
and
H (7)
1 (ζN) =− 1
2 lim
τ→ 1
N
q
47
168eΦ(1,1,3)
(2,3,7)(τ).(1.23)
The purpose of this paper is to use the Bailey pair machinery and a novel relation between
incomplete quadratic Gauss sums with periodic coefficients to construct identities between each
of the infinite families in (1.11)–(1.16) evaluated at roots of unity and limiting values of Eichler
integrals of weight 3/2 modular forms. This gives new proofs of (1.3), (1.9) and (1.10) as well
as a proof and generalization of Conjecture 1.1.
The Bailey pair method also leads to the discovery of further identities betweenq-series at
roots of unity and Eichler integrals. We will give two examples which involve the series
H (9)
p (q) :=
X
np≥···≥n1≥0
q−n2
p−np(qnp+1)np
p−1Y
i=1
qn2
i

ni+1
ni

(1.24)
and
H (10)
p (q) :=
X
np≥···≥n1≥0
q−n2
p(qnp)np
p−1Y
i=1
qn2
i

ni+1
ni

,(1.25)
defined forp≥1. We now state our main result.
BAILEY PAIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANTS 5
Theorem 1.2.LetMandNbe coprime positive integers. Forp≥2, we have
H (1)
p (ζM
N ) =− 1
2 lim
τ→M
N
q− (6p+5)2
24(6p−1)eΦ(1,1,1)
(2,3,6p−1)(τ) (1.26)
while forp= 1
H (1)
1 (ζM
N ) =−ζ−M
N − 1
2 lim
τ→M
N
q− 121
120eΦ(1,1,1)
(2,3,5)(τ).(1.27)
Forp≥1, we have
H (2)
p (ζM
N ) =− 1
2 lim
τ→M
N
q− 1
24(6p−1)eΦ(1,1,p)
(2,3,6p−1)(τ),(1.28)
H (3)
p (ζM
N ) =− 1
2 lim
τ→M
N
q−1− (6p−5)2
24(6p−1)eΦ(1,1,2p−1)
(2,3,6p−1)(τ),(1.29)
H (4)
p (ζM
N ) =− 1
2 lim
τ→M
N
q− (6p+1)2
24(6p−1)eΦ(1,1,2p)
(2,3,6p−1)(τ),(1.30)
H (5)
p (ζM
N ) =− 1
2 lim
τ→M
N
qp−1− (12p−5)2
24(6p−1)eΦ(1,1,3p−1)
(2,3,6p−1)(τ),(1.31)
H (6)
p (ζM
N ) =− 1
2 lim
τ→M
N
q− (6p−1)2
24(6p+1)eΦ(1,1,2p)
(2,3,6p+1)(τ),(1.32)
H (7)
p (ζM
N ) =− 1
2 lim
τ→M
N
q1− (6p+5)2
24(6p+1)eΦ(1,1,2p+1)
(2,3,6p+1)(τ),(1.33)
H (8)
p (ζM
N ) =− 1
2 lim
τ→M
N
q1− (6p−5)2
24(6p+1)eΦ(1,1,1)
(2,3,6p+1)(τ),(1.34)
H (9)
p (ζM
N ) =− 1
2 lim
τ→M
N
qp−1− (12p−1)2
24(6p+1)eΦ(1,1,3p)
(2,3,6p+1)(τ) (1.35)
and
H (10)
p (ζM
N ) =− 1
2 lim
τ→M
N
q− 1
24(6p+1)eΦ(1,1,p)
(2,3,6p+1)(τ).(1.36)
Remark 1.3.Observe that thep= 1 case of (1.28) recovers (1.3) while theM= 1 cases of (1.26)
and (1.34) yield (1.9) and (1.10), respectively. We have also included (1.27) for completeness
(cf. [21, (3.8), (3.10)]). Note that Theorem 1.2 embeds Hikami’s conjectures for one single value
ofp(with the exception of (1.21)) into an infinite family of identities. Finally, our main result
and [14, Section 4.4] imply that eachH (i)
p (q) is a quantum modular form.
The paper is organized as follows. In Section 2, we recall the necessary background on the
Bailey pair machinery and express all of the seriesH (i)
p (q) as finite polynomial sums at roots of
unity. See Theorems 2.7–2.16. An elucidatory principle in this section arises from the broader
perspective of quantumq-series identities [26, 27], a recent development whose applications
include new proofs for identities at roots of unity for Ramanujan’sσ-function and its companion
σ∗(q) [5, 7], a “duality” result for the Kontsevich-Zagier strange function [6, 10] and Zagier’s
strange identity and Hikami’s generalization thereof [20,35]. For further work in this direction,
6 JEREMY LOVEJOY, ROBERT OSBURN, AND MATTHIAS STORZER
see [8, 11, 12, 28]. In Section 3, we prove key properties for and relations between incomplete
quadratic Gauss sums. In Section 4, we convert the finite polynomial sums in Section 2 to
limiting values of Eichler integrals, thereby proving Theorem 1.2.
