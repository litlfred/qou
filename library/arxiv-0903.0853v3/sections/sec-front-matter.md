---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-7
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
arXiv:0903.0853v3  [math.QA]  30 Jan 2012
Jean-Pierre Ramis
Jacques Sauloy
Changgui Zhang
LOCAL ANALYTIC
CLASSIFICATION OF
q-DIFFERENCE EQUATIONS
Jean-Pierre Ramis
Institut de France (Acad´emie des Sciences) and Laboratoire ´Emile Picard,
Institut de Math´ematiques, CNRS UMR 5219, U.F.R. M.I.G., Universit´e
Paul Sabatier (Toulouse 3), 31062 Toulouse CEDEX 9.
E-mail : ramis.jean-pierre@wanadoo.fr
Jacques Sauloy
Laboratoire ´Emile Picard, Institut de Math´ematiques, CNRS UMR 5219,
U.F.R. M.I.G., Universit´e Paul Sabatier (Toulouse 3), 31062 Toulouse
CEDEX 9.
E-mail : sauloy@math.univ-toulouse.fr
Url : http://www.math.univ-toulouse.fr/~sauloy/
Changgui Zhang
Laboratoire Paul Painlev´e, UMR-CNRS 8524, UFR Math´ematiques Pures et
Appliqu´ees, Universit´e des Sciences et Technologies de Lille (Lille 1), Cit´e
Scientique, 59655 Villeneuve d’Ascq Cedex.
E-mail : Changgui.Zhang@math.univ-lille1.fr
Url : http://math.univ-lille1.fr/~zhang/
2000
Mathematics
Subject
Classiﬁcation. — 39A13.
Secondary:
34M50.
Key words and phrases. — q-diﬀerence equations, analytic classiﬁcation,
Stokes phenomenon, summation of divergent series.
LOCAL ANALYTIC CLASSIFICATION OF
q-DIFFERENCE EQUATIONS
Jean-Pierre Ramis, Jacques Sauloy,
Changgui Zhang
Abstract. — We essentially achieve Birkhoﬀ’s program for q-diﬀerence equa-
tions by giving three diﬀerent descriptions of the moduli space of isoformal an-
alytic classes. This involves an extension of Birkhoﬀ-Guenther normal forms,
q-analogues of the so-called Birkhoﬀ-Malgrange-Sibuya theorems and a new
theory of summation. The results were announced in [41, 42] and in various
seminars and conferences between 2004 and 2006.
R´esum´e
(Classiﬁcation
analytique
locale
des ´equations
aux
q-
diﬀ´erences)
Nous achevons pour l’essentiel le programme de Birkhoﬀpour la classiﬁca-
tion des ´equations aux q-diﬀ´erences en donnant trois descriptions distinctes
de l’espace des modules des classes analytiques isoformelles. Cela passe par
une extension des formes normales de Birkhoﬀ-Guenther, des q-analogues des
th´eor`emes dits de Birkhoﬀ-Malgrange-Sibuya et une nouvelle th´eorie de la
sommation. Ces r´esultats ont ´et´e annonc´es dans [41, 42] ainsi que dans divers
s´eminaires et conf´erences de 2004 `a 2006.
CONTENTS
1. Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.1. The problem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2. Contents of the paper.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.3. General notations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
Acknowledgements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2. Some general nonsense. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1. The category of q-diﬀerence modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2. The Newton polygon and the slope ﬁltration. . . . . . . . . . . . . . . . . . . . . . 16
2.3. Application to the analytic isoformal classiﬁcation. . . . . . . . . . . . . . . . 21
3. The aﬃne space of isoformal analytic classes. . . . . . . . . . . . . . . . . . . 29
3.1. Isoformal analytic classes of analytic q-diﬀerence modules.. . . . . . . . 29
3.2. Index theorems and irregularity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3. Explicit description of F(P1, . . . , Pk) in the case of integral slopes
36
3.4. Interpolation by q-Gevrey classes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4. The q-analogs of Birkhoﬀ-Malgrange-Sibuya theorems. . . . . . . . 45
4.1. Asymptotics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.2. Existence of asymptotic solutions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.3. The fundamental isomorphism. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.4. The isoformal classiﬁcation by the cohomology of the Stokes sheaf 64
5. Summation and asymptotic theory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.1. Some preparatory notations and results. . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.2. Asymptotics relative to a divisor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.3. q-Gevrey theorem of Borel-Ritt and ﬂat functions. . . . . . . . . . . . . . . . 83
5.4. Relative divisors and multisummable functions. . . . . . . . . . . . . . . . . . . 89
5.5. Analytic classiﬁcation of linear q-diﬀerence equations. . . . . . . . . . . . . 93
vi
CONTENTS
6. Geometry of the space of classes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6.1. Privileged cocycles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6.2. D´evissage q-Gevrey. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
6.3. Vector bundles associated to q-diﬀerence modules. . . . . . . . . . . . . . . . . 108
7. Examples of the Stokes phenomenon. . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
7.1. The q-Euler equation and conﬂuent basic hypergeometric series. . . 112
7.2. The symmetric square of the q-Euler equation. . . . . . . . . . . . . . . . . . . . 118
7.3. From the Mock Theta functions to the q-Euler equation. . . . . . . . . . 123
7.4. From class numbers of quadratic forms to the q-Euler equation. . . 127
A. Classiﬁcation of isograded ﬁltered diﬀerence modules. . . . . . . . 131
A.1. General setting of the problem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
A.2. Diﬀerence modules over diﬀerence rings. . . . . . . . . . . . . . . . . . . . . . . . . . 135
A.3. Finitely ﬁltered diﬀerence modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
A.4. Extensions of diﬀerence modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
A.5. Extension of scalars. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
A.6. Our moduli space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
A.7. Extension classes of diﬀerence modules. . . . . . . . . . . . . . . . . . . . . . . . . . . 155
A.8. The cohomological equation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Bibliography. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Index of notations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
CHAPTER 1
INTRODUCTION
