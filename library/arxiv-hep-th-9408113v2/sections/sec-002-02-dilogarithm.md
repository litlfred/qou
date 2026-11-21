---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-002-02-dilogarithm
section_title: "Dilogarithm."
section_number: 0.2
pages: 3-10
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
0.2. Dilogarithm.
The main subject of this paper is the dilogarithm identities. More exactly, we are study
the relations of the following type
N
i=1
L(xi) = cπ2
6 ,
(0.3)
where L(x) is the Rogers dilogarithm, all xi are assumed to be the algebraic and c is a
rational number. The main problems we are interested in are the following:
i) how to ﬁnd/classify the relations of type (0.3),
ii) how one can prove a dilogarithm identity.
Both problems have the deep connections with algebraic K-theory, representation the-
ory of inﬁnite dimensional algebras, combinatorics and mathematical physics.
The main purpose of the paper presented is to study the dilogarithm identities and
related topics from the diﬀerent points of view, namely, the algebraic, analytic, asymptotic,
group-theoretic and combinatorial ones.
The ﬁrst non-trivial examples of dilogarithm relations were obtained by Euler and
Landen in the second half of 18-th century. And it happened only after 150 years that
Coxeter and Watson had found the new examples of the type (0.3) dilogarithm relations
(see (1.11) and Section 2.1.2). The most complicated among the Coxeter relations is the
following one
L(ρ20) −2L(ρ10) −15L(ρ4) + 10L(ρ2) = π2
5 .
(0.4)
The methods used by Coxeter and Watson were entirely diﬀerent. Coxeter’s relations were
developed from the properties of a certain inﬁnite series, whereas Watson deduced his
relations by ”simple elimination” using Euler’s and Abel’s one-variable functional equations
(i.e. (1.3) and (1.7)). Following L. Lewin, let us give
Deﬁnition 3. A dilogarithm relation (0.3) is called to be accessible if it can be obtained
by applying the ﬁve-term relation (1.4) a number of times.
Although Watson’s dilogarithm relations are accessible from the ﬁve term relations only,
they are not obviously so. As Watson indicated, ”he had long suspected the existence of
certain results, and although his eventual proof is easy enough to follow, it is clear that
it was not all that easy to come by” (see [Le5], p.5). This comment is applicable to the
Coxeter relations as well. In fact, the last Coxeter relation had long been believed to be
inaccessible (on the basis of many failed tries). However, it has been shown by Dupont
in 1990 (see [Le5], p.52) that the relation (0.4) can be really deduced from the ﬁve-term
relation (1.4) and the so-called factorization (or multiplication) formula
L(yn) = n
n
X
l=1
L(exp
2πil
n

y).
4
Anatol N. Kirillov
There exist also the proofs of Coxeter’s relations based on Lewin’s single-variable ([Le4]
and Theorem 1) and Ray’s multivariable ([Ray] and Proposition E) functional equations.
In fact, Ray multivariable functional equation is the very powerful means for proving the
dilogarithm identities (see [Ray]). However, the known proof of Ray’s functional equation
[Ray] uses the analytical methods (e.g. the integral representation for Li2). Hence, the
Ray functional equation can not be considered ad hoc as accessible.
Now we came to one of the main problems considered in the Section 1 of our paper,
namely, to that of the dilogarithm identities accessibility. According to the strong version
of Goncharov’s conjecture (see (2.3.2)), any dilogarithm relation (0.3) with real algebraic
xi, 1 ≤i ≤N, can be obtained as a linear combination with rational coeﬃcients of the
ﬁve-term relations:
N
X
i=1
L(xi) −cL(1)
=
X
j
nj

L(aj) + L(bj) −L(ajbj) −L
aj(1 −bj)
1 −ajbj

−L
bj(1 −aj)
1 −ajbj

,
where all aj, bj lie in R ∩Q and all nj ∈Q. Here L(x) is the so-called single-valued
dilogarithm (see (1.13)). It was indicated by Lichtenbaum ([Li], see also Section 1.1.3)
that one should be careful working with the single-valued dilogarithm, because it does not
satisfy the ﬁve-term relation in general (but only modulo π2).
The main purpose of the Sections 1.1-1.3 is to prove accessibility of some well-known
dilogarithm identities such as the Coxeter, Lewin, Loxton, Browkin ones. Let us note, that
Browkin’s identities have been found in [Bro2] and [Le3] ”numerically”, i.e. without, up to-
date, any analytic proof. We give also the proofs of accessibility of the Lewin single-valued
functional equations as well as the Ray multivalued functional equation (for simplicity, we
consider in the paper presented only the case n ≤2, see Appendix).
A remarkable family of dilogarithm identities (see [Kir4], [BR], [Ku]) comes from a con-
sideration of some Mathematical Physics problems. Namely, in physics, the dilogarithm
appeared at ﬁrst from a calculation of magnetic susceptibility in the XXZ-model at small
magnetic ﬁeld [KR], [Kir4], [BR]. More recently [Z], the dilogarithm identities (through
Thermodynamic Bethe Ansatz (TBA)) appeared in the context of investigation of the
ultra violet (UV) limit or the critical behavior of the integrable 2-dimensional quantum
ﬁeld theories and lattice models [Z], [DR], ... . The meaning of dilogarithm identities in
question is to identify some theories via the central/eﬀective charges and conformal di-
mension of primary ﬁelds computation. Even more, it was shown (e.g. [NRT], [DKKMM],
[KMM], [KKMM1], [Tr], ...)
using the Richmond-Szekeres method [RS] and the Kac-
Wakimoto theorem, that the dilogarithm identities can be derived from an investigation of
the asymptotic behavior of some characters of 2-dimensional CFT. To be more precise, it
is necessary to have the Rogers-Ramanujan-left-hand-side type formulas for the characters
(and branching functions) of the Virasoro and aﬃne Lie algebras. This problem is very
interesting one and is considered in many papers [LP], [FeSt]... .
Dilogarithm identities
5
In the Section 1.3 we give a new proof of the An-type dilogarithm identity [Kir7],
mainly based on the multiple uses of the ﬁve-term relation.
In the Section 1.4 we discuss and partially prove the c
sl2-case of Kuniba-Nakanishi’s
conjecture [KN]. This conjecture predicts the integrality and divisibility by 24 for the
remainder term in some special linear combination of the principal-branch-valued Euler
dilogarithm and logarithms and has many interesting connections with CFT, TBA and
representation theory [KN], [KNS], ... . In principle, using the An-dilogarithm identity
(1.28), one can reduce a proof of Kuniba-Nakanishi’s identity for c
sln to a proving that
between the values of logarithms only. We intend to consider this interesting subject, in-
cluding a generalization of Kuniba-Nakanishi’s identity to a ”fractional level”, in a separate
publication.
Summarizing, in the Section 1 we present mainly the algebraic method for proving the
single-valued-dilogarithm identities by means of the multiple uses of the ﬁve-term relation
(1.4). Presumably, any identity of type (0.3) can be obtained by this way (strong form of
Goncharov’s conjecture). But even if it is so, to have the more direct ways to produce the
dilogarithm identities are still desirable. One of such ways, the so-called asymptotic method
(S. Ramanujan, G. Hardy, G. Meinardus, B. Richmond, S. Szekeres, W. Nahm, B. MacCoy,
M. Terhoeven, ...) and closely related with Rogers-Ramanujan type identities (L. Rogers,
S. Ramanujan, I. Schur, G. Watson, L. Slater, B. Gordon, G. Andrews, D. Bressoud,
B. Feigin, E. Melzer, ...) will be discussed in the Section 2.1. Another one, related with
the algebraic K-theory (torsion in K3(R), S. Bloch, A. Suslin, D. Zagier, E. Frenkel, A.
Szenes, ...) will be considered in Section 2.3. Finally, we discuss the so-called character-
asymptotic method due to V. Kac and M. Wakimoto (see also E. Frenkel, A. Szenes, ...).
This method is closely related with the following problems:
i) combinatorial (i.e. Rogers-Ramanujan’s and Schur’s type) formulae for the branching
and string functions in the representation theory of integrable highest weight modules over
aﬃne Kac-Moody algebras [Kac];
ii) ﬁnite-dimensional version of crystal basis (see e.g. [FrSz2]) and its connection with
Robinson-Schensted type correspondence;
iii) a natural ”ﬁnitization” (or polynomial version) of the Weyl-Kac [Kac] and Feigin-
Fuchs-Rocha-Caridi character formulae;
iv) branching functions as the Thermodynamic-Bethe-Ansatz-like limit of the Kostka-
Foulkes polynomials (or Lusztig’s q-analog of weight multiplicity).
We are going to discuss these problems in the Sections 2.2 and 2.4.
Finally, in the Section 2.5 we consider some properties of the quantum dilogarithm (cf.
[FK], [FV]) and quantum polylogarithm.
Acknowledgments. This work was written during my stay at Mathematical Depart-
ment of Tokyo University and is based on the series of lectures given at Tokyo, Nagoya,
Osaka, Kobe and Kyushu Universities and at RIMS and Yukawa Institute, Kyoto.
I would be very glad to express my gratitude to L.D. Faddeev, K. Aomoto, E. Date,
6
Anatol N. Kirillov
B. Feigin, A. Kato, A. Kuniba, B. Leclerc, N.A. Liskova, T. Miwa, W. Nahm, M. Noumi,
R. Sasaki, E. Sklyanin, M. Suzuki, V. Tarasov, J.-Y. Thibon, A.Yu. Volkov and M. Waki-
moto for fruitful discussions and valuable remarks. I also thank with much gratitude the
colleagues at Tokyo University for their invitation, their hospitality which made it possible
to ﬁnish this work.
I would like to acknowledge my special indebtedness to Dr.
N.A. Liskova for the
inestimable help in preparing the manuscript to publication.
1.1. Dilogarithm (G. Leibnitz (1696), L. Euler (1768), L. Rogers (1906)).
1.1.1. Euler’s and Rogers’ dilogarithm.
The Euler dilogarithm function Li2(x) deﬁned for 0 ≤x ≤1 by
Li2(x) :=
X
n≥1
xn
n2 = −
Z x
0
log(1 −t)
t
dt
(1.1)
is one of the lesser transcendental function. Nonetheless, it has many intriguing properties
and has appeared in various branches of mathematics and physics.
It is also convenient to introduce the Rogers dilogarithm function L(x) deﬁned for
0 < x < 1 by
L(x) :=
∞
X
n=1
xn
n2 + 1
2 log x · log(1 −x) = −1
2
Z x
0
log(1 −y)
y
+ log y
1 −y

dy.
(1.2)
The function L(x) has an analytic continuation to the complex plane cut analog the real
axis from −∞to 0 and 1 to +∞.
1.1.2. Five-term relation and characterization of Rogers’ dilogarithm.
Theorem A (W. Spence (1809), N. Abel (1830), C. Hill (1830), E. Kummer (1840)).
The function L(x) belongs to the class C∞((0, 1)) and satisﬁes the following functional
equations
1. L(x) + L(1 −x) = π2
6 ,
0 < x < 1,
(1.3)
2. L(x) + L(y) = L(xy) + L
x(1 −y)
1 −xy

+ L
y(1 −x)
1 −xy

,
(1.4)
where 0 < x,
y < 1.
Theorem B (Cf. [Ro], Section 4) Let f(x) be a function of class C3((0, 1)) which
satisﬁes the relations (1.3) and (1.4). Then we have
f(x) = L(x).
Dilogarithm identities
7
1.1.3. Single–valued dilogarithm.
We continue the function L(x) to all real axis R = R1 ∪{±∞} by the following rules
L(x) = π2
3 −L(x−1),
if x > 1,
L(x) = L

1
1 −x

−π2
6 ,
if x < 0,
(1.5)
L(0) = 0,
L(1) = π2
6 ,
L(+∞) = π2
3 ,
L(−∞) = −π2
6 .
Important remark. The continuation of Rogers’ dilogarithm function constructed
in this way satisﬁes the functional equation (1.3), but does not satisfy in general the
ﬁve-term relation (1.4). Namely, one can check LHS(1.4) −RHS(1.4) = 0, except the
case x < 0,
y < 0 and xy > 1. In the latter case LHS(1.4) −RHS(1.4) = −π2. So,
proving accessibility of a dilogarithm identity we must remember about an existence of the
exceptional cases. We leave a checking of exceptional cases to a reader.
In the last part of this section we are going to show that (1.3) is a corollary of (1.4).
Namely, let us take x =
a
1 −b and y =
b
1 −a in (1.4). It is clear that a = x(1 −y)
1 −xy ,
b = y(1 −x)
1 −xy
and the ﬁve-term relation (1.4) is reduced to the so–called Abel equation
(see e.g. [Le])
L

a
1 −b

+ L

b
1 −a

= L

a
1 −b ·
b
1 −a

+ L(a) + L(b).
(1.6)
From (1.6), with 1 −a for b, we obtain
L(a) + L(1 −a) = L(1),
as it was claimed. If in (1.4) we take x = y, we get the Abel duplication formula
L(x2) = 2L(x) −2L

x
1 + x

.
(1.7)
From (1.6), with −a for b, and using (1.7), we obtain
L(a2) + L
 −a2
1 −a2

= 0
and consequently,
L(a) + L(−a) = 1
2L(a2).
(1.8)
Finally, if in (1.6) we take a −1
a
for b, we get
L(a2) + L(a−2) = 2L(1);
L(−a2) + L
−1
a2

= −L(1).
(1.9)
8
Anatol N. Kirillov
1.1.4. Dilogarithm of complex argument. Wigner-Bloch’s function.
By using the integral representation
Li2(z) = −
Z z
0
log(1 −t)
t
dt,
Euler’s dilogarithm Li2(x) can be analytically continued as a multivalued complex function
to the complex plane cut along the real axis from 1 to +∞.
Proposition A (E. Kummer (1840)).
Assume that r, θ are the real numbers and
|r| < 1, then
Li2(reiθ) = −1
2
Z r
0
log(1 −2x cos θ + x2)
x
dx
+ i

w log(r) + 1
2Cl2(2w) + 1
2Cl2(2θ) −1
2Cl2(2θ + 2w)

,
where
w = tan−1

r sin θ
1 −r cos θ

,
and Cl2(θ) =
∞
X
n=1
sin(nθ)
n2
= −
Z θ
0
log |2 sin(t/2)|dt
is Clausen’s function.
Proposition B (F. Newman (1847)).
Li2(eiθ) = π2B2
 θ
2π

+ iCl2(θ),
where B2(x) := −1
π2
∞
X
n=1
cos 2nπx
n2
is the second modiﬁed Bernoulli polynomial.
In recent studies in K-theory the Wigner-Bloch dilogarithm function D(z) has played
an important role [Bl]. It can be related to Clausen’s function via the formula
D(z) := arg(1 −z) log |z| −Im
Z z
0
log(1 −t)
t
dt
= 1
2 {Cl2(2θ) + Cl2(2w) −Cl2(2θ + 2w)} ,
where θ = arg(z), w = arg(1 −z) and D(z) = 0 for z ∈R ∪{∞}.
The dilogarithm D: C ∪{∞} →R is a real-analytic function on C \ [0, 1], continuous
on C∪{∞}. We summarize the basic properties of Wigner-Bloch’s dilogarithm in the next
Proposition (see e.g. [Bl], [Bro2]).
Dilogarithm identities
9
Proposition C. For z ∈C ∪{∞}, we have
i) D(z) + D(1 −z) = 0, D(z) + D(1/z) = 0, D(z) = D(z),
ii) D(zn) = n
n−1
X
k=0
D

exp
2πki
n

z

,
iii) (Five-term relation) If z, w ∈C \ [0, 1], then
D(z) + D(w) = D(zw) + D
z(1 −w)
1 −zw

+ D
w(1 −z)
1 −zw

.
There is a geometric interpretation of the number D(z) and consequently of Cl2(t) =
D(eit). Namely, for a complex number z , the volume of the asymptotic simplex with
vertices 0, 1, z and ∞in 3-dimensional hyperbolic space is equal to |D(z)|. Some formulae
for the Wigner-Bloch dilogarithm can be interpreted as relations between the volumes of
corresponding simplexes. For more details, see [Mi2], [Mi3], [Za1], [Za4].
1.1.5. Multivariable functional equations (L. Rogers (1906), G. Ray (1990)).
Using the analytic methods, Rogers [Ro] had proved the following dilogarithm identity.
Proposition D (L. Rogers). Deﬁne the polynomial
r(x, t) := 1 −t −
n
Y
j=1
(1 −αjx)
of degree n in x for nonzero complex numbers α1, . . ., αn. Let {xl := xl(t)}, l = 1, . . ., n
be the algebraic functions satisfying r(xl, t) = 0. Then we have
n
X
j=1
n
X
l=1
[L(αj/αl) −L(αjxl)] = L(1 −t).
The special case n = 2 leads to the form of Hill’s equation (see Remark in Section 1.3)
with two independent variables and ﬁve dilogarithmic terms.
Example. Let us assume α1 = . . . = αn = 1 and 1 −t = yn. Then xl = ζly, where
ζl = exp
2πil
n

, and Rogers’ identity is reduced to the so-called factorization formula
L(yn) = n
n
X
l=1
L(ζly).
A remarkable generalization of Rogers’ multivariable identity for dilogarithm was dis-
covered by G. Ray [Ray]. Since the statement of the most general dilogarithm identity in
the paper [Ray] is rather involved, we present here only an important particular case of
the general Ray’s result.
10
Anatol N. Kirillov
Proposition E (G. Ray). Consider the polynomial
r(x, t) := (1 −t)A
n
Y
j=1
(1 −βjx) −
n
Y
j=1
(1 −αjx)
of degree n in x for nonzero complex numbers {αj, A} and some complex numbers {βj}.
Let {xl := xl(t)}, 1 ≤l ≤n, be the algebraic functions satisfying r(xl, t) = 0. Then we
have
n
X
j=1
n
X
l=1
[L(βjxl) −L(βj/αl) −L(αjxl) + L(αj/αl)]
= L(A(1 −t)) −L
Aβ1 . . . βn
α1 . . . αn
(1 −t)

.
In Appendix we are going to prove the accessibility of this identity for n = 1, 2. General
case will be considered elsewhere.
