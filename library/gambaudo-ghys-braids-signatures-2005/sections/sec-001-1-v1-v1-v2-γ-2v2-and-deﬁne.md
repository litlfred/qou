---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Braids and signatures"
section_id: sec-001-1-v1-v1-v2-γ-2v2-and-deﬁne
section_title: "(v1) −v1 =v2 −γ 2(v2) and deﬁne"
section_number: 1
pages: 4-6
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Braids and signatures — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
qγ 1,γ 2(e) = Ω( v1 +v2,e )
where Ω denotes the standard symplectic form on R2g. One checks eas-
ily that qγ 1,γ 2(e) is independent of the choices of v1 and v2 and deﬁnes a
quadratic form on Eγ 1,γ 2. By deﬁnition, the evaluation of the Meyer cocycle
on the pair ( γ 1,γ 2), denoted Meyer( γ 1,γ 2), is the signature of this quadratic
form. Observe that the Meyer cocycle can be coherently deﬁne d for elements
in Sp(∞, R). In other words, if γ 1 and γ 2 are two elements in Sp(2g, R)
seen as elements γ ′
1 and γ ′
2 of Sp(2g + 2, R), the values of Meyer( γ 1,γ 2) and
Meyer(γ ′
1,γ ′
2) coincide.
We hope that this mysterious deﬁnition will become crystal c lear in Sec-
tion 3.2.
We now state the main result of this paper:
Theorem A . — Let α and β two braids in B∞ and ω ⁄= 1 a root of unity.
Then:
signω ( ˆα ·β ) − signω (ˆα ) − signω ( ˆβ ) = − Meyer
(
Bω (α ), Bω (β )
)
.
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 545
Remark 1 . — Since the Meyer cocycle evaluated on Sp(2g, R) is the signa-
ture of a quadratic form on a vector space with dimension smal ler that 2 g,
it follows easily from the deﬁnition of the Burau-Squier rep resentation that,
for any positive integer n, and any pair of braids α and β in Bn, we have
⏐
⏐signω ( ˆα ·β ) − signω (w ˆα ) − signω ( ˆβ )
⏐
⏐ ≤ 2n.
Thus, for any positive integer n, the map α ∈ Bn ↦→ signω ( ˆβ ) ∈ R is a
quasimorphism. A direct proof of this result can be found in [5] where the
authors use this property to construct non trivial quasimor phisms on the group
of area preserving diﬀeomorphisms of the 2-sphere.
Remark 2 . — The Artin braid group Bn has a standard presentation in terms
of generators σ 1, σ 2,...,σ n− 1 and relations
σ i ·σ j =σ j ·σ i, σ i ·σ i+1 ·σ i =σ i+1 ·σ i ·σ i+1;
for all i,j in {1,...,n − 1} satisfying |i −j| ≥2. See for instance [11].
The closed braids ˆσ i are trivial links. Given a braid β in Bn which reads
β =σ i1 · · ·σ i𝓁 , we have:
signω ( ˆβ ) = −
j=𝓁∑
j=2
Meyer
(
Bω (σ i1 · · ·σ i𝓁 −1 ), Bω (σ i𝓁 )
)
.
This last formula is actually very easy to use for numerical c omputations since
the matrices Bω (σ i𝓁 ) are sparse (as we shall see in Section 2).
t = 0 t = 1
1
2
i
i + 1
n
Figure 3. The braid σ i
Remark 3 . — As a trivial illustration of Theorem A, consider the case n = 2.
The image of B− 1(B2) is contained in Sp(2, R) = SL(2, R) and it is not dif-
ﬁcult to see that, up to conjugacy, B− 1(σ 1) is the matrix
( 1 0
− 1 1
)
. Evaluating
the Meyer cocycle on 2 × 2 unipotent matrices is very easy so that one can
compute sign(σ 𝓁
1) using the method explained in Remark 2. The reader will
ﬁnd immediately the value 1 −𝓁 for𝓁 ≥ 1. Of course, one can also compute this
signature using an explicit Seifert surface for this elemen tary braid (see [11]).
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
546 GAMBAUDO (J.-M.) & GHYS (E.)
Section 3 is devoted to the proof of Theorem A. This proof will be a visual
computation (following an expression borrowed from [14]). First, we int erpret
both the signature of an oriented link and the evaluation of t he Meyer cocycle
as the signatures of the intersection forms of some 4-manifo lds (subsections 3.1
and 3.2). Then, in 3.3 we construct an oriented compact conne cted 4-manifold
M 4
