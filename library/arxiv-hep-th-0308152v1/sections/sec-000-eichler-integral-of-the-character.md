---
doc_id: arxiv-hep-th-0308152v1
doc_title: "TORUS KNOT AND MINIMAL MODEL"
section_id: sec-000-eichler-integral-of-the-character
section_title: "Eichler Integral of the Character"
section_number: null
pages: 1-10
source_pdf: 0308152v1.pdf
source_sha256: 93bcc14b8be91257
doc_brief: "TORUS KNOT AND MINIMAL MODEL — We reveal an intimate connection between the quantum knot i nvariant for torus knot T(s, t) and the character of the minimal model M(s, t), where s and t are relatively"
---
1. I ntroduction
After Jones polynomial was introduced [1], studies of quant um invariants have been exten-
sively developed. These quantum knot invariants are physically interpreted as the Feynman path
integral of the Wilson loop with the Chern–Simons action [2] . Though, geometrical interpreta-
tion of the quantum invariant is still not complete. Some tim e ago, Kashaev deﬁned a quantum
knot invariant based on the quantum dilogarithm function [3 ], and made a conjecture [4] that a
limit of his invariant coincides with the hyperbolic volume of the knot complement [5]. This
suggests an intimate connection between the quantum invari ant and the geometry. Note that
Kashaev’s invariant was later identiﬁed with a specialization of the N-colored Jones polynomial
at q being the N-th primitive root of unity [6].
In this article, we study Kashaev’s invariant⟨K ⟩N for the torus knot K = T(s, t), where s and
t are coprime. See Fig. 1 for a projection of some torus knots. O ne may think that it is insignif-
icant from a view point of the Volume Conjecture because the torus knot is not hyperbolic [5].
Although, the Chern–Simons invariant is considered as an imaginary part of the hyperbolic vol-
ume, and in fact the torus knot is supposed to have non-trivia l Chern–Simons invariant. We
shall show that the invariant exactly coincides with a limiting value of the Eichler integral of the
character of the minimal model M(s, t) with q being the N-th root of unity.
This paper is organized as follows. In Section 2 we recall a modular property of the character
of the minimal modelM(s, t). We deﬁne the Eichler integral, and give an explicit form oflimiting
value thereof when q is the N-th primitive root of unity. In Section 3 we study the colored Jones
polynomial for the torus knot T(s, t). We give a formula relating the quantum invariant with the
Date: August 22, 2003.
1
2 KAZUHIRO HIKAMI AND ANATOL N. KIRILLOV
Figure 1. Torus knot T(s, t). From left to right, we depict trefoil T(2, 3),
Solomon’s seal knotT(2, 5), and T(3, 4), respectively.
Eichler integral. We further give some examples onq-series identities. Clariﬁed is a relationship
between the conformal weight and the Chern–Simons invarian t of the minimal model. The last
section is devoted to concluding remarks.
2. E ichler Integral of the Character
We study the character of the minimal modelM(s, t), where s and t are coprime integers. The
central charge of the minimal model M(s, t) is
c(s, t) = 1 − 6 (s − t)2
s t , (1)
and the irreducible highest weight representation of the Virasoro algebra is given for the confor-
mal weight
∆s, t
n, m = (n t − m s)2 − (s − t)2
4 s t , (2)
where integers m and n are
1 ≤ n ≤ s − 1, 1 ≤ m ≤ t − 1.
The number of distinct ﬁelds in the theory is
D(s, t) = 1
2 (s − 1) (t − 1). (3)
TORUS KNOT AND MINIMAL MODEL 3
The character chs, t
n, m(τ) for an irreducible highest weight representation of the Virasoro algebra
with above central charge and weight, is computed as [7, 8]
chs, t
n, m(τ) = Tr qL0− 1
24 c(s, t)
= q∆s, t
n, m− 1
24 c(s, t)
(q)∞
∑
k∈Z
qstk2 (
qk(nt−ms) − qk(nt+ms)+mn)
, (4)
where we set q = e2πiτ. We see that
chs, t
n, m(τ) = chs, t
s−n, t−m(τ) = cht, s
m, n(τ) = cht, s
t−m, s−n(τ).
The character is modular covariant [9, 10] as
chs, t
n, m(τ) =
∑
n′, m′
Sn′, m′
n, m chs, t
n′, m′(−1/τ), (5)
where sum runs over D(s, t) distinct ﬁelds, and a matrix is explicitly written as
Sn′, m′
n, m =
√
8
s t (−1)nm′+mn′+1 sin
(
n n′ t
s π
)
sin
(
m m′ s
t π
)
. (6)
We rewrite the character of the minimal model as
chs, t
n, m(τ) = Φ(n, m)(τ)
η(τ) . (7)
Here we have set the Dedekind η-function and Φ(n, m)(τ) as
η(τ) = q1/ 24 (q)∞,
Φ(n, m)(τ) =
∞∑
k=0
χ(n, m)
2st (k) q
1
4st k2
, (8)
where the function χ(n, m)
2st (k) is periodic with modulus 2 s t as
k mod 2 s t n t − m s n t + m s 2 s t − (n t + m s) 2 s t − (n t − m s) others
χ(n, m)
2st (k) 1 −1 −1 1 0 (9)
From the modular property of the Dedekind η-function, we see that Φ(n, m)(τ) is modular with
weight 1/ 2, and spans D(s, t) dimensional space; modular T- and S -transformations are respec-
tively written as
Φ(n, m)(τ+ 1) = e
(nt−ms)2
2st πi Φ(n, m)(τ), (10)
Φ(n, m)(τ) =
√
i
τ
∑
n′, m′
Sn′, m′
n, m Φ(n′, m′)(−1/τ). (11)
4 KAZUHIRO HIKAMI AND ANATOL N. KIRILLOV
For the modular form with weightw ∈ Z>2, the period is deﬁned by use of the classical Eichler
integral, which is w − 1 integrations of the modular form with respect to τ[11]. In a case of the
half-integral weight modular form Φ(n, m)(τ), the Eichler integral is thus naively deﬁned by the
q-series as [12]
~Φ(n, m)(τ) = −1
2
∞∑
k=0
k χ(n, m)
2st (k) q
1
4st k2
. (12)
A prefactor is for our convention. It can be seen that the former is regarded as a “half-derivative”
( 1
2 − 1 integration) of the modular form Φ(n, m)(τ) with respect to τ, as was originally studied in
Ref. 12. We consider a limiting value of the Eichler integral ~Φ(n, m)(α) at α∈ Q. Applying the
Mellin transformation, we have
~Φ(n, m)
( M
N + i y
2 π
)
≃ − 1
2
∞∑
k=0
Lω(−2 k − 1, χ(n, m)
2st )
k!
(
− y
4 s t
) k
,
where y ց 0, and M, N are coprime integers. We mean thatLω(k, χ(n, m)
2st ) is the twisted L-function
deﬁned by
Lω(k, χ(n, m)
2st ) =
∞∑
j=1
χ(n, m)
2st ( j) e
M
N
j2
2st πi j−k
= 1
(2 s t N)k
2stN∑
j=1
χ(n, m)
2st ( j) e
M
N
j2
2st πi ζ
(
k, j
2 s t N
)
,
where ζ(k, x) is the Hurwitz ζfunction. By the analytic continuation, limiting value at τ→ M/ N
is then computed as
~Φ(n, m)(M/ N) = s t N
2
2stN∑
k=1
χ(n, m)
2st (k) e
k2 M
2stN πi B2
( k
2 s t N
)
, (13)
where Bk(x) is the k-th Bernoulli polynomial, t ext
et − 1 =
∞∑
k=0
tk
k! Bk(x), and especially B2(x) =
x2 − x + 1
6.
This function fulﬁlls a nearly modular property; for N ∈ Z we have an asymptotic expansion
in N → ∞,
~Φ(n, m)(1/ N) + (−i N)3/ 2
∑
n′, m′
Sn′, m′
n, m φ(n′, m′) e− (n′t−m′s)2
2st πiN
≃
∞∑
k=0
T (n, m)(k)
k!
( π
2 s ti N
) k
. (14)
TORUS KNOT AND MINIMAL MODEL 5
Here we have set
φ(n, m) =

(s − n) m, if n t > m s,
n (t − m), if n t < m s,
(15)
and T-series is written in terms of the L-function associated with χ(n, m)
2st as
T (n, m)(k) = 1
2 (−1)k+1 L(−2 k − 1, χ(n, m)
2st )
= 1
2 (−1)k (2 s t)2k+1
2 k + 2
2st∑
j=1
χ(n, m)
2st ( j) B2k+2
( j
2 s t
)
. (16)
This can be shown as follows (see Refs. 12,13,14,15). We deﬁne a variant of the Eichler integral
ˆΦ(n, m)(z) =
√
s ti
8 π2
∫ ∞
z∗
Φ(n, m)(τ)
(τ− z)3/ 2 dτ. (17)
This function is deﬁned for z in the lower half plane, z ∈ H−, while the Eichler integral ~Φ(n, m)(z)
is for the upper half plane, z ∈ H. Using S -transformation (11), we have
ˆΦ(n, m)(z) +
( 1
i z
) 3/ 2 ∑
n′, m′
Sn′, m′
n, m ˆΦ(n′, m′)(−1/ z) = r(n, m)(z; 0), (18)
where we have deﬁned the period function
r(n, m)(z; α) =
√
s ti
8 π2
∫ ∞
α
Φ(n, m)(τ)
(τ− z)3/ 2 dτ, (19)
for z ∈ H− and α∈ Q. More generally, for γ=
(
a b
c d
)
∈ S L(2; Z), we have
ˆΦ(n, m)(z) − 1
v(n, m)(γ) (c z + d)−3/ 2
∑
n′, m′
(
Mγ
) n′, m′
n, m
ˆΦ(n′, m′)(γ(z)) = r(n, m)(z; γ−1(∞)), (20)
where a matrix Mγand v(n, m)(γ) are given from the modular transformation,
∑
n′, m′
(
Mγ
) n′, m′
n, m Φ(n′, m′)(γ(z)) = v(n, m)(γ)
√
c z + d Φ(n, m)(z).
When we substitute eq. (8) into eq. (17) and perform an integr ation term by term in a limit
z → α∈ Q, we see that
~Φ(n, m)(α) = ˆΦ(n, m)(α),
Note that the left hand side is given by eq. (13) as a limit value from H while the right hand side
is a limit from H−. We can check for N ∈ Z that an asymptotic expansion of r(n, m)(1/ N; 0) gives
6 KAZUHIRO HIKAMI AND ANATOL N. KIRILLOV
a right hand side of eq. (14), and that from eq. (13) we have
~Φ(n, m)(N + 1) = e
(nt−ms)2
2st πi ~Φ(n, m)(N),
~Φ(n, m)(0) = φ(n, m),
which shows
~Φ(n, m)(N) = φ(n, m) e
(nt−ms)2
2st πiN.
Combining these results we recover eq. (14).
3. Q uantum Knot Inv ariant forTorus Knot
We study theN-colored Jones polynomial JN(K) for the torus knotK = T(s, t). The torus knot
T(s, t) for coprime integers s, t is the knot which wraps around the solid torus in the longitudinal
direction s times and in the meridinal direction t times. See Fig. 1. It is also represented as
(σ1 σ2 · · · σs−1)t in terms of generators σj of the Artin braid group. An explicit form of the
N-colored Jones polynomial is read as [16, 17]
2 sh(N ℏ/ 2) JN(K)
JN(O) = e− ℏ
4 ( t
s + s
t )
∑
ε=±1
N−1
2∑
k=− N−1
2
εexp
(
ℏs t
(
k + s + εt
2 s t
) 2)
, (21)
where we have set a parameterq = eℏ, and O denotes unknot. As was shown in Ref. 6, Kashaev’s
invariant [3, 4] coincides with a specialization q → e2πi/ N of the colored Jones polynomial. As
the left hand side of eq. (21) vanishes in this substitution, Kashaev’s invariant for the torus knot
can be computed as a derivative of the right hand side with respect to ℏ.
Here we recall the Eichler integral~Φ(n, m)(1/ N) which was computed in eq. (13), and especially
pay attention to a case of (n, m) = (s − 1, 1). Using a property of the Gauss sum, we obtain from
eq. (13)
~Φ(s−1, 1)(1/ N) = s t
N e
st
2 Nπi+(s+t)πi
∑
ε=±1
N−1
2∑
k=− N−1
2
ε
(
k + s + εt
2 s t
) 2
e
2πi
N st(k+ s+εt
2st )
2
. (22)
As seen from eq. (21), this expression is proportional to the colored Jones polynomial at ℏ→
2 πi/ N. To conclude Kashaev’s invariant⟨K ⟩N for torus knot K = T(s, t) is identiﬁed with
e− (st−s−t)2
2stN πi · ~Φ(s−1, 1)(1/ N) = ⟨T(s, t)⟩N. (23)
We expect that the Eichler integrals~Φ(n, m)(1/ N) for other cases (n, m) are related with the quantum
invariants of 3-manifolds. As a result eq. (14) denotes an as ymptotic expansion of Kashaev’s
invariant in N → ∞. Note that an asymptotic behavior was studied in Refs. 18, 19 in a diﬀerent
manner.
TORUS KNOT AND MINIMAL MODEL 7
In general, we can construct q-series for the Eichler integrals based on the R-matrix [3]. We
give some examples below (see Fig. 1). Hereafter we use a standard notation,
(x)k = (x; q)k =
k∏
j=1
(1 − x qj−1),
[
k
j
]
= (q)k
(q) j (q)k− j
.
• Trefoil T(2, 3),
~Φ(1, 1)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 1)
12 (k) qk2/ 24
= q1/ 24
∞∑
k=0
(q)k.
This equality is Zagier’s “strange” identity [12]; though both expressions do not converge
simultaneously, the limiting values in q being roots of unity coincide. It is the Eichler
integral of the Dedekind η-function.
• Solomon’s Seal knotT(2, 5),
~Φ(1, 1)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 1)
20 (k) qk2/ 40
= q9/ 40
∞∑
k=0
(q)k
k∑
j=0
q j( j+1)
[
k
j
]
,
~Φ(1, 2)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 2)
20 (k) qk2/ 40
= q1/ 40
∞∑
k=0
(q)k
k+1∑
j=0
q j2
[
k + 1
j
]
.
The equalities in above formulae have same meaning with a cas e of trefoil [14]. These
are the Eichler integral of the Rogers–Ramanujan q-series, which is the character of the
Lee–Yang theory M(2, 5).
• Knot T(3, 4),
~Φ(1, 1)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 1)
24 (k) qk2/ 48
= q1/ 48
∞∑
k=0
(q)k

⌊k/ 2⌋∑
j=0
q2 j2
[
k
2 j
]
+
⌊(k+1)/ 2⌋∑
j=0
q2 j2
[
k + 1
2 j
]  ,
8 KAZUHIRO HIKAMI AND ANATOL N. KIRILLOV
~Φ(1, 2)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 2)
24 (k) qk2/ 48
= 2 q1/ 12
∞∑
k=0
(q2; q2)k,
~Φ(1, 3)(τ) ≡ − 1
2
∞∑
k=0
k χ(1, 3)
24 (k) qk2/ 48
= q25/ 48
∞∑
k=0
(q)k

⌊(k−1)/ 2⌋∑
j=0
q2 j( j+1)
[
k
2 j + 1
]
+
⌊k/ 2⌋∑
j=0
q2 j( j+1)
[
k + 1
2 j + 1
]  ,
These are the Eichler integral of the Slater’s q-series [20], which is the character of the
Ising model M(3, 4).
See that inﬁnite sums in all those expressions reduce to a ﬁnite sum in a case q → e2πi/ N.
Asymptotic behavior of Kashaev’s invariant,
lim
N→∞
2 π
N log⟨K ⟩N,
is conjectured [4, 6] to give the hyperbolic volume of the knot complement M = S 3 \ K . In our
case, the torus knot is not hyperbolic. We can rather expect from eqs. (14) and (23) that a value
−(nt − ms)2
st π2 = −4 π2
(
∆s, t
n, m − c(s, t) − 1
24
)
, (24)
is related to the SU(2) Chern–Simons invariant,
CS(M) = 1
4
∫
M
Tr
(
A ∧ dA + 2
3 A ∧ A ∧ A
)
.
To see this fact, we recall that the fundamental group of M = S 3 \ T(s, t) has a presentation
π1(M) = ⟨x, y|xs = yt⟩. (25)
As was shown in Ref. 21, the Chern–Simons invariant from two SU(2) representation ρ0 and ρ1
of π1(M) satisﬁes
CS(M; ρ1) − CS(M; ρ0) = −4 π2
∫ 1
0
β(z) α′(z) dz. (26)
Here α(z) and β(z) are from the representation ρz, z ∈ [0, 1], of the meridian µand the longitude
λup to conjugation,
ρz(µ) =
(
e2πiα(z)
e−2πiα(z)
)
, ρ z(λ) =
(
e2πiβ(z)
e−2πiβ(z)
)
.
TORUS KNOT AND MINIMAL MODEL 9
In a case of complement (25) of the torus knot, the longitudeλand the meridianµare respectively
given by xs and xa yb, where a, b ∈ Z satisﬁes a s + b t = 1. As the longitude λ= xs = yt is a
center of group, it is sent to ±1. From relations ( xa)s = (xs)a and (yb)t = (xs)b we see that xa and
yb is conjugate to
ρ(xa) →
(
eπin/ s
e−πin/ s
)
, ρ (yb) →
(
eπim/ t
e−πim/ t
)
,
where n, m are integers. Correspondingly we ﬁnd that a path of represen tation from a trivial
representation z = 0 is given by
α(z) = 1
2
( n
s + m
t
)
z, β (z) = s t
2
( n
s + m
t
)
.
Here β(z) is constant along this path representation since the longitude is ﬁxed to be ±1. Substi-
tuting into eq. (26), we get a quantity (24) as the Chern–Simons invariant of M modulo 2 π2.
4. C oncluding Remarks
We have revealed intriguing properties of the character of the minimal model M(s, t). We have
shown that Kashaev’s invariant,i.e., a speciﬁc value of the N-colored Jones polynomial, for the
torus knot T(s, t) is regarded as the Eichler integral of the character for (n, m) = (s − 1, 1) with q
being the N-th root of unity. It is natural to expect that general ( n, m) case is also related to the
quantum invariant of the 3-manifold.
As was shown in Ref. 15, the Eichler integral of the aﬃne ˆsu(2)m+2 character, which is modular
covariant with weight 3 / 2, gives Kashaev’s invariant for torus link T(2, 2 m) when q is the N-
th primitive root of unity. As the torus knot and link are not h yperbolic, we may regard the
hyperbolic manifold as a (massive) deformation of the conformal ﬁeld theory.
Acknowledgment
The authors would like to thank to H. Murakami for useful comm ents on early version of
manuscript. The work of KH is supported in part by the Sumitomo Foundation, and Grant-in-Aid
for Young Scientists from the Ministry of Education, Cultur e, Sports, Science and Technology
of Japan.
References
[1] V . F. R. Jones, A polynomial invariant for knots via von Neumann algebras, Bull. Amer. Math. Soc. 12, 103–
111 (1985).
[2] E. Witten, Quantum ﬁeld theory and Jones’ polynomial, Commun. Math. Phys. 121, 351–399 (1989).
10 KAZUHIRO HIKAMI AND ANATOL N. KIRILLOV
[3] R. M. Kashaev, A link invariant from quantum dilogarithm, Mod. Phys. Lett. A 10, 1409–1418 (1995).
[4] R. M. Kashaev, The hyperbolic volume of knots from quantum dilogarithm , Lett. Math. Phys. 39, 269–275
(1997).
[5] W. P. Thurston, The geometry and topology of three-manifolds, Lecture Notes in Princeton University, Prince-
ton (1980).
[6] H. Murakami and J. Murakami, The colored Jones polynomials and the simplicial volume of aknot, Acta Math.
186, 85–104 (2001).
[7] A. Rocha-Caridi, Vacuum vector representations of the Virasoro algebra, in Vertex Operators in Mathematics
and Physics, edited by J. Lepowsky, S. Mandelstam, and J. Singer, no. 3 in Math. Sci. Res. Inst. Publ., pp.
451–473. Springer, New York (1984).
[8] B. L. Feigin and D. B. Fuchs, Verma modules over the Virasoro algebra , Funct. Anal. Appl. 17, 241–242
(1983).
[9] C. Itzykson and J.-B. Zuber, Two-dimensional conformal invariant theories on a torus , Nucl. Phys. B 275,
580–616 (1986).
[10] A. Cappelli, C. Itzykson, and J.-B. Zuber, Modular invariant partition functions in two dimensions, Nucl. Phys.
B 280, 445–465 (1987).
[11] S. Lang, Introduction to Modular Forms, Grund. math. Wiss. 222, Springer, Berlin (1976).
[12] D. Zagier, Vassiliev invariants and a strange identity related to the Dedekind eta-function, Topology 40, 945–
960 (2001).
[13] R. Lawrence and D. Zagier, Modular forms and quantum invariants of 3-manifolds, Asian J. Math. 3, 93–107
(1999).
[14] K. Hikami, q-series and L-functions related to half-derivatives of the Andrews–Gordon identity, Ramanujan J.
(2003), to appear.
[15] K. Hikami, Quantum invariant for torus link and modular forms, preprint (2003).
[16] H. R. Morton, The coloured Jones function and Alexander polynomial for torus knots, Proc. Cambridge Philos.
Soc. 117, 129–135 (1995).
[17] M. Rosso and V . Jones, On the invariants of torus knots derived from quantum groups, J. Knot Theory Rami-
ﬁcations 2, 97–112 (1993).
[18] K. Hikami, Volume conjecture and asymptotic expansion of q-series, Exp. Math. (2003), to appear.
[19] R. M. Kashaev and O. Tirkkonen, Proof of the volume conjecture for torus knots , Zap. Nauch. Sem. POMI
269, 262–268 (2000).
[20] K. Hikami and A. N. Kirillov, in preparation.
[21] P. A. Kirk and E. P. Klassen,Chern–Simons invariants of 3-manifolds and representation spaces of knot groups,
Math. Ann. 287, 343–367 (1990).
Department of Physics, G raduate School of Science, U niversity of Tokyo, H ongo 7–3–1, B unkyo, T okyo
113–0033, Japan.
E-mail address: hikami@phys.s.u-tokyo.ac.jp
RIMS, Kyoto University, Kyoto 606-8502, Japan.
E-mail address: kirillov@kurims.kyoto-u.ac.jp
