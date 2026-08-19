---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-013-63-multivariable-big-q-jacobi-polynomials
section_title: "Multivariable big q-Jacobi polynomials"
section_number: 6.3
pages: 27-29
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
ments of the previous subsection to derive evaluation formulas for multivariable bigq-Jacobi
polynomials. The monic multivariable big q-Jacobi polynomial
P B
λ (z) = P B
λ (z;a,b,c,d ;q,t ) ∈ E[z]S
of degree λ ∈ Λ n is of the form
(6.22) P B
λ (z) = ~mλ(z) +
∑
µ∈Λ: µ<λ
cB
λ,µ~mµ(z)
for certain coeﬃcients cB
λ,µ = cB
λ,µ(a,b,c,d ;q,t ) ∈ E. Similarly as for the Koornwinder
polynomials and the multivariable little q-Jacobi polynomials, the multivariable big q-
Jacobi polynomials can be characterized by a second-order diﬀere nce equation they should
satisfy, or in terms of suitable orthogonality properties, see [26]. The characterization as
solution of a diﬀerence equation is DBP B
λ =EqJ
λ P B
λ with
DB =
n∑
j=1
(
φ+
B,j (z)(Tj − Id) +φ−
B,j (z)(T−1
j − Id)
)
,
φ+
B,j (z) = qtn−1(
a − c
qzj
)(
b + d
qzj
) ∏
l⁄=j
zl −tzj
zl −zj
,
φ−
B,j (z) =
(
1 − c
zj
)(
1 + d
zj
) ∏
l⁄=j
zj −tzl
zj −zl
.
We again consider the evaluation formulas for the one-variable big q-Jacobi polynomials
(n = 1) ﬁrst. The one-variable monic big q-Jacobi polynomial is independent of t and is
given explicitly as
(6.23) P B
m (z) =
(
qa, −qad/c;q
)
m
(
qm+1ab;q
)
m
(
qa/c
) m 3φ2
(
q−m,q m+1ab,qaz/c
qa, −qad/c ;q,q
)
for m ∈ Z+, see e.g. [14]. We immediately obtain from (6.23) the evaluation formula
(6.24) P B
m (c/qa) =
(
qa, −qad/c;q
)
m(
qm+1ab;q
)
m
(
c/qa
) m
form ∈ Z+. A straightforward computation using (6.23) and the q-Vandermonde formula
(6.7) yields the two evaluation formulas
P B
m (c) =
(
qa,qab, −qbc/d;q
)
m(
qab;q
)
2m
dmq
1
2 m(m−1),
P B
m (−d) =
(
−qad/c,qb,qab ;q
)
m(
qab;q
)
2m
(−1)mcmq
1
2 m(m−1)
(6.25)
28 URI ONN AND JASPER V. STOKMAN
for m ∈ Z+. Finally, by the q-Saalsch¨ utz sum
(6.26) 3φ2
(
q−m,a,b
abq1−m/c,c ;q,q
)
=
(
c/a,c/b ;q
)
m
(
c,c/ab ;q
)
m
, m ∈ Z+
(see [8, (II.12)]) we obtain the evaluation formula
(6.27) P B
m (−d/qb) =
(
qb, −qbc/d,qab ;q
)
m
(
qab;q
)
2m
(
−d/qb
) m
form ∈ Z+. In the following theorem we give the multivariable analogues of the ev aluation
formulas (6.24), (6.25) and (6.27). Recall the explicit expression ∆ λ, deﬁned by (6.10).
Theorem 6.2. Forλ ∈ Λ n we have the evaluation formulas
(6.28) P B
λ (ctρ) = ∆ λ
n∏
i=1
(
qatn−i,qabt n−i, − qbc
d tn−i;q
)
λi(
qabt2(n−i);q
)
2λi
dλiq
1
2 λi(λi−1),
(6.29) P B
λ (−dtρ) = ∆ λ
n∏
i=1
(
qbtn−i,qabt n−i, − qad
c tn−i;q
)
λi(
qabt2(n−i);q
)
2λi
(−c)λiq
1
2 λi(λi−1),
(6.30) P B
λ
(c
qat−ρ)
= ∆ λ
n∏
i=1
(
qatn−i,qabt n−i, − qad
c tn−i;q
)
λi(
qabt2(n−i);q
)
2λi
(c
qati−n) λi
,
(6.31) P B
λ
(
−d
qbt−ρ)
= ∆ λ
n∏
i=1
(
qbtn−i,qabt n−i, − qbc
d tn−i;q
)
λi(
qabt2(n−i);q
)
2λi
(
−d
qbti−n) λi
.
Proof. The proof is analogous to the proof of Theorem 6.2, so we only indicat e the main
steps. From (the proof of) [27, Theorem 7.5] (replacing the role of the limiting parameter
ǫ in [27, Theorem 7.5] by
(
cd/q
) 1
2ǫ), we obtain the two limit transitions
(6.32) lim
ǫ→0
ǫ|λ|Pλ
(
ǫ−1z;qaǫ
c , −qbǫ
d ,cǫ−1, −dǫ−1;q,t
)
=P B
λ (z;a,b,c,d ;q,t ),
(6.33) lim
ǫ→0
ǫ|λ|Pλ
(
ǫz;qaǫ
c , −qbǫ
d ,cǫ−1, −dǫ−1;q,t
)
=P B
λ (z−1;a,b,c,d ;q,t )
for λ ∈ Λ n and for a speciﬁc Zariski-dense subset of specialized parameters a,b,c,d,q and
t. If we set z =ǫ−1ctρ (respectively z = −ǫ−1dtρ) in (6.32) and use the evaluation formula
(6.2) for the Macdonald-Koornwinder polynomial Pλ, then we arrive at the evaluation
formula (6.28) (respectively (6.29)). The evaluation formulas (6.30 ) and (6.31) follow from
(6.2) and the limit transition (6.33) specialized to z = qa
c tρ andz = − qb
d tρ, respectively. □
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 29
We end this section by recalling the quadratic norm evaluations of the multivariable big
q-Jacobi polynomials from [27]. We deﬁne an E-linear functional
hB =ha,b,c,d;q,t
B : E[z]S → E
by requiring
hB
(
P B
λ
)
=
{
1, if λ = 0,
0, if λ ⁄= 0.
An analytic deﬁnition of hB can be given for speciﬁc Zariski dense choice of specialized
parameters as a multidimensional q-integral with explicit weight function, see e.g. [27].
We deﬁne a sesqui-linear form ⟨·, ·⟩B = ⟨·, ·⟩a,b,c,d;q,t
B on E[z]S by
(6.34) ⟨p1,p 2⟩B =hB
(
p1(z)p2(z)
)
, p 1,p 2 ∈ E[z]S,
with the same convention on the complex conjugation as for the mult ivariable littleq-Jacobi
polynomials. The orthogonality relations for the multivariable big q-Jacobi polynomials
are now given by
(6.35) ⟨P B
λ ,P B
µ ⟩B =NB(λ)δλ,µ, ∀λ,µ ∈ Λ n
with the quadratic norms NB(λ) = NB(λ;a,b,c,d ;q,t ) ∈ E given by
NB(λ) = (cd)|λ|t(ρ,λ)
( n∏
i=1
q(λi
2 )(
−qbc
d tn−i, −qad
c tn−i;q
)
λi
)
N +
L (λ)N−
L (λ),
with N±
L = N±
L (a,b ;q,t ) the same factors as for the multivariable little q-Jacobi polyno-
mials. We recall from [27] that
(6.36) lim
ǫ→0
ǫ2|λ|NK
(
λ;qaǫ
c , −qbǫ
d ,cǫ−1, −dǫ−1;q,t
)
=NB(λ;a,b,c,d ;q,t ), λ ∈ Λ n,
for generic specialized parameters.
