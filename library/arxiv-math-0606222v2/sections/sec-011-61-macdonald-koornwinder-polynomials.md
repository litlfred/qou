---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-011-61-macdonald-koornwinder-polynomials
section_title: "Macdonald-Koornwinder polynomials"
section_number: 6.1
pages: 21-24
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
[3], [24] and [28]. The evaluation formulas for the multivariable little q-Jacobi polynomials
22 URI ONN AND JASPER V. STOKMAN
are used in the next section to obtain explicit expressions for the ge neralized dimensions
Dq (see (2.4)) and their degenerations.
6.1. Macdonald-Koornwinder polynomials. Recall our notation E = C(a,b,c,d,q,t )
for the ﬁeld of rational functions in six indeterminates a,b,c,d,q and t. Let W = Sn ⋉
{±1}n, acting on Zn by permutations and sign-changes of the coordinates, and acting on
the algebra E[z±1] = E[z±1
1 ,...,z ±1
n ] by permutations and inversions of the independent
variables zi. The cone Λ n ⊂ Zn is a fundamental domain for the W -action on Zn. The
dominance order on Λ n is the partial order ≤ deﬁned by λ ≤µ if∑ i
j=1λj ≤∑ i
j=1µj for
1 ≤i ≤n. An E-basis of the algebra E[z±1]W ofW -invariant Laurent polynomials is given
by the symmetric monomials mλ(z) :=∑
µ∈W λzµ (λ ∈ Λ n).
The monic Macdonald-Koornwinder polynomial Pλ(z) = Pλ(z;a,b,c,d ;q,t ) ∈ E[z±1]W
of degree λ ∈ Λ n is of the form
(6.1) Pλ(z) = mλ(z) +
∑
µ∈Λ n:µ<λ
cλ,µmµ(z)
for certain coeﬃcients cλ,µ =cλ,µ(a,b,c,d ;q,t ) ∈ E. It can be characterized as solution of a
particular second-order diﬀerence equation, or, for suitably spe cialized generic parameters
a,b,c,d,q,t , in terms of suitable orthogonality properties, see Koornwinder [1 5]. The
characterizing diﬀerence equation for the Macdonald-Koornwinde r polynomial Pλ(z) of
degree λ is DPλ =EλPλ where
D =
n∑
j=1
(
φj(z)(Tj − Id) +φj(z−1)(T−1
j − Id)
)
,
φj(z) = (1 −azj)(1 −bzj)(1 −czj)(1 −dzj)
(1 −z2
j )(1 −qz 2
j )
∏
l⁄=j
(1 −tzlzj)(1 −tz−1
l zj)
(1 −zlzj)(1 −z−1
l zj)
and where the eigenvalue Eλ ∈ E is given by
Eλ =
n∑
j=1
(
q−1abcdt2n−j−1(qλj − 1) +tj−1(q−λj − 1)
)
.
Note that Pλ(z;a,b,c,d ;q,t ) is symmetric in the four parameters a,b,c,d . The evaluation
formulas for Macdonald-Koornwinder polynomials are given by
Pλ(atρ) =
n∏
i=1
(
abtn−i,act n−i,adt n−i,q−1abcdtn−i;q
)
λi
(
q−1abcdt2(n−i);q
)
2λi
(
atn−i) λi
×
∏
1≤j<k≤n
(
q−1abcdt2n−j−k+1;q
)
λj+λk
(
tk−j+1;q
)
λj−λk(
q−1abcdt2n−j−k;q
)
λj+λk
(
tk−j;q
)
λj−λk
(6.2)
for λ ∈ Λ n. The evaluation formulas (6.2) have been established by van Diejen [ 3] for a
sub-family of Macdonald-Koornwinder polynomials. The general cas e follow from Sahi’s
[24] results using double aﬃne Hecke algebras, see also [28, Remark 9 .5].
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 23
In the rank one case (n = 1), the Macdonald-Koornwinder polynomials do not dependent
on t and reduce to the monic Askey-Wilson polynomials
Pm(z) =
(
ab,ac,ad ;q
)
m
am(
qm−1abcd;q
)
m
4φ3
(
q−m,q m−1abcd,az,az −1
ab,ac,ad ;q,q
)
∈ C[z +z−1], m ∈ Z+.
In particular
Pm(a) =
(
ab,ac,ad ;q
)
m
am(
qm−1abcd;q
)
m
, m ∈ Z+,
which is in accordance to (6.2).
We give here a purely algebraic formulation of the quadratic norm eva luations for the
Macdonald-Koornwinder polynomials, which has the advantage that we do not need to
specialize the parameters a,b,c,d,q and t. We deﬁne an E-linear functional
hK =ha,b,c,d;q,t
K : E[z±1]W → E
by requiring
hK
(
Pλ
)
=
{
1, if λ = 0,
0, if λ ⁄= 0.
An analytic deﬁnition of hK can be given (for speciﬁc Zariski dense choice of parameters)
as an integral over a deformed compact n-torus with explicit weight function, see e.g. [15].
We deﬁne now a sesqui-linear form ⟨·, ·⟩K = ⟨·, ·⟩a,b,c,d;q,t
K on E[z±1]W by
(6.3) ⟨p1,p 2⟩K =hK
(
p1(z)p2(z)
)
, p 1,p 2 ∈ E[z±1]W,
where complex conjugation on C is extended to an anti-linear algebra involution on E[z±1]
by requiring the six parameters a,b,c,d,q,t to be formally real, e.g. a =a, and by requiring
the variables zj to be formally purely imaginary, zj =z−1
j . The orthogonality relations for
the Macdonald-Koornwinder polynomials are now given by
(6.4) ⟨Pλ,P µ⟩K =NK(λ)δλ,µ, ∀λ,µ ∈ Λ n,
with the quadratic norms NK(λ) = NK(λ;a,b,c,d ;q,t ) given by NK(λ) = N +
K (λ)N−
K(λ),
where N±
K(λ) = N±
K (λ;a,b,c,d ;q,t ) ∈ E are
N +
K(λ) =
n∏
i=1
(
abtn−i,act n−i,adt n−i,q−1abcdtn−i;q
)
λi
(
q−1abcdt2(n−i);q
)
2λi
×
∏
1≤j<k≤n
(
q−1abcdt2n−j−k+1;q
)
λj +λk
(
tk−j+1;q
)
λj−λk
(
q−1abcdt2n−j−k;q
)
λj +λk
(
tk−j;q
)
λj−λk
,
N−
K(λ) =
n∏
i=1
(
qtn−i,bct n−i,bdt n−i,cdt n−i;q
)
λi(
abcdt2(n−i);q
)
2λi
×
∏
1≤j<k≤n
(
abcdt2n−j−k−1;q
)
λj+λk
(
qtk−j−1;q
)
λj−λk(
abcdt2n−j−k;q
)
λj+λk
(
qtk−j;q
)
λj−λk
.
24 URI ONN AND JASPER V. STOKMAN
The quadratic norm formulas have been established by van Diejen [3 ] for a sub-family of
Macdonald-Koornwinder polynomials. The general case has been de rived in [24], see also
[28].
