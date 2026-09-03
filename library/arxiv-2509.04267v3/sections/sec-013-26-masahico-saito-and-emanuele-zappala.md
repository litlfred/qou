---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-013-26-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 26
pages: 26-28
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Example 7.9.LetT m be a (2,m) torus knot or knot as depicted in Figure 9. Ifm−1 appears we
retain it to be positive. Note that all crossings are positive. By using Equation (17), we obtain
ΦW(T2) = [(A+A −1) +ℏ(B+A 2B)]w−
= [(A+A −1) +ℏ(B−A 2B)][−A−3 +ℏB(A−4 + 2)]
=−A −3(A+A −1) +ℏB(A−5 + 3A−1 + 2A).
By Proposition 7.4, the coefficient ofℏis considered modulo 2(A 4−1). This is satisfied with
A= √−1. In the coefficient ofℏB,
A−5 + 3A−1 + 2A=−2
√
−1.
Thus ΦW1(T2) is nontrivial.
Proposition 7.10.ForA= √−1, we haveΦ W(Tm) = (2−m) + √−1(m−1)(8−m)ℏB
ΦW(Tm) =
(
0−m√−1Bℏform≥0 even
1
2−(m−2) √−1Bℏform≥0 odd
.
Proof.From Example 7.9, we use the evaluationA= √−1. In this case the recursive formula of
Lemma 7.8 becomes
ΦW(Tm+1)A=√−1 = (
√
−1 +ℏB)w−ΦW(Tm)A=√−1 + (−
√
−1 +ℏB)w−,
wherew − :=−A −3 +ℏB(A−4 + 2) =− √−1 + 3ℏB. Hence by simplifying the notationφ m :=
ΦW(Tm)A=√−1, we obtain
φm+1 = (
√
−1 +ℏB)(
√
−1 + 3ℏB)φm + (−
√
−1 +ℏB)(
√
−1 + 3ℏB)
= (−1 + 4
√
−1Bℏ)φm + (1−2
√
−1Bℏ).
Setφ m =a m +ℏBb m. Then we obtain
am+1 +ℏBb m+1 = (−1 + 4
√
−1Bℏ)(am +ℏBb m) + (1−2
√
−1Bℏ)
= (−a m + 1) +ℏB(4
√
−1am−bm−2
√
−1),
so that (
am+1 =−a m + 1,
bm+1 = 4√−1am−bm−2√−1,
anda 1 = 1,b 1 = 0. It follows thata m = 0 formeven, anda m = 1 formodd, whileb m =−2m√−1
formeven, andb m =−2(m−2) √−1 formodd. The normalizing factor isδ=−A 2−A−2 = 2,
and dividinga m andb m by 2 we obtain the result.□
Corollary 7.11.There exist infinitely many knots and links with nontrivial, and distinct, infini-
tesimal partΦ W1 of the quantum cocycle invariantΦ W.
8.Higher order invariants
We consider now higher order deformations of YBOs, where the condition of being enhanced is
preserved for the trace approach. It is known that YBOs can be nontrivially deformed to higher
order, as seen explicitly in [21]. Our objective in this section is to characterize when higher order
deformations define EYBOs, and how to use such deformed EYBOs to define higher order quantum
cocycle invariants. Although a similar higher order deformations can be formulated, we focus on
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 27
the trace approach in the remaining sections, as our purpose of defining this procedure is to give an
interpretation of such deformations for the YBOs used for the Jones and Alexander polynomials.
We define the following in a manner similar to the infinitesimal deformation. Let
˜R(n) =
nX
i=0
ℏiϕi∈ ˜V(n) =k[[ℏ]]/(ℏ n+1)⊗V
be an orderndeformation of the EYBOϕ 0 :=R. Then, we say thatϕ n+1 is an enhanced order
(or degree)n+ 1 deformation if
˜R(n+1) := ˜R(n) +ℏn+1ϕn+1 =
n+1X
i=0
ℏiϕi∈ ˜V(n+1) =k[[ℏ]]/(ℏ n+2)⊗V
is an EYBO.
The following theorem provides conditions for (ϕn+1,µn+1) to extend deformation ˜R(n) to ˜R(n+1)
as an EYBO.
We recall the following notation from Definition 4.2.
ˆΓm
n ={(j 1,...,j m)|j 1 +···+j m =n, jℓ≥0 andj ℓ̸=n,for allℓ= 1,...,m}.
Recall also, whenmis apparent, we use ˆΓn = ˆΓm
n .
We also define, following [18], the quantity
Θn+1 :=
X
(i,j,k)∈ˆΓn+1
[(ϕi⊗1)(1⊗ϕ j)(ϕk⊗1)−(ϕ k⊗1)(ϕi⊗1)(1⊗ϕ j)]
Theorem 8.1.LetRbe a YBO, and letϕ 1,...,ϕ n,µ 1,...,µ n,α,βbe such thatS= ( ˜ϕ,α,β,˜µ)
is an EYBO, where ˜R(n) =Pn
i=0 ℏiϕi and˜µn =Pn
i=0 ℏiµi. Then the obstruction for(ϕ n+1,µn+1)
to be an enhanced ordern+ 1deformation ofRis the following system of equations
δ2
YBϕn+1 + Θn+1 = 0 (18)
and 


P
(i,j,k)∈ˆΓn+1
[(µi⊗µj)ϕk−ϕi(µj⊗µk)] = 0
P
(i,j,k)∈ˆΓn+1
Tr(ϕi(µj⊗µk)) =αβµ n+1
P
(i,j,k)∈ˆΓn+1
Tr(ˆϕi(µj⊗µk)) =αβµ n+1
(19)
where ˆϕi indicates thei th component of the inverse of ˜R(n) +ℏn+1ϕn+1 (moduloℏ n+2).
Proof.First we show that enhanced higher order deformations are equivalent to the system (18)
and (19). It is a known result, see for instance [18], that the obstruction forϕ n+1 to be an order
n+ 1 YB deformation of ˜ϕisδ 2
YBϕn+1 + Θn+1 = 0, where the left-hand side lies in the third
cohomology group ofR. Henceϕ n+1 extends ˜ϕto a YBO if and only if the first equality of (18)
holds.
Commutativity of ˜R(n+1) = ˜R(n) +ℏn+1ϕn+1 with the deformed ˜µn+1 = ˜µn +ℏn+1µn+1 means
that Equation (1) holds with ˜µ(n+1) and ˜R(n+1). Taking terms of degreen+ 1 inℏgives the first
equation in (19). Equation (2) with positive sign gives the second equation of (19) when considering
terms of degreen+ 1 inℏ. Similarly, we obtain the third equation of the system from Equation (2)
with negative sign, where the existence of the inverse of ˜R(n+1) has been shown in the first part of
the proof. This completes the first statement of the theorem.
