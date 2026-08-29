---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-003-8-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 8
pages: 8-8
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Proof.ApplyingRto the differential ˆd1
YB of [7], we find the relation∂ 1
YB(f) = ˆd1
YB(f)R, for any
1-cochainf. SinceRis invertible, we find a 1-1 correspondence between 1-cocycles of∂ 1
YB and 1-
cocycles of ˆd1
YB. Since∂ 0
YB and ˆd0
YB are the same, this completes the proof of the first isomorphism.
To show the second, we just use the fact that both cohomology groups are isomorphic to the group
of YB infinitesimal deformations, as shown in [6] and [18]. The groups of deformations of YBOs
are the same between the two by takingmin [6] to be (ℏ) in our notation. This completes the
proof. □
The relation betweenH n
YB(V,R) and ˆHn
YB(V,R) remains unclear forn≥3. This does not affect
the current paper.
4.Quantum cocycle invariants via traces
LetS= (R,α,β,µ) be an EYBO. Suppose that there is an infinitesimal deformation
˜R=ϕ 0 +ℏϕ 1 =R+ℏϕon ˜V=k[[ℏ]]/(ℏ 2)⊗V.
Suppose further that there is ˜µ=µ+ℏµ 1 : ˜V→ ˜Vsuch that ˜S= ( ˜R,α,β,˜µ) is an EYBO on ˜V.
Then we say that ˜Sis aninfinitesimal deformationof an EYBOS, orSis deformed to ˜S. In this
situation we also denote the deformation by the pair (ϕ,µ 1), and call it anenhancedYang-Baxter
2-cocycle, or EYB 2-cocycle for short. We also simply say thatϕis an EYB 2-cocycle whenµ 1 is
understood from context.
Definition 4.1.LetRbe a YB operator with inverseR −1, and letϕbe a YB 2-cocycle. Letb m
be anm-braid. Then, we associate an operator Ψ ϕ(bm) to the braid as follows. We consider the
operator ˜R=ϕ 0 +ℏϕ 1 withϕ 0 =Ron ˜V=k[[ℏ]]/(ℏ 2)⊗Vas above. Observe that ˜Ris invertible
with inverse ˜R−1 = ˆϕ0 +ℏ ˆϕ1, where ˆϕ0 =R−1 and ˆϕ1 =−R−1ϕ1R−1. ForRand/orR −1 we use
the notationR ±, and similarly for ˜R±.
To each standard generator (and its inverse)σ ±
i ,i= 1,...,m−1, of the braid groupB m, we
associate the operatorσ±
i 7→1⊗(i−1)⊗ ˜R±⊗1⊗(m−i−1). Then, from a presentation ofbm as a product
ofσ±
i ’s we obtain an operator obtained as composition of terms of type1 ⊗(i−1)⊗ ˜R±⊗1⊗(m−i−1),
which we denote Ψϕ(bm). We let Ψi
ϕ(bm),i= 0,1, be defined by
Ψϕ(bm) = Ψ0
ϕ(bm) +ℏΨ 1
ϕ(bm)∈Hom( ˜V⊗m, ˜V⊗m).
We use the following notation.
Definition 4.2.For given non-negative integerskandn, set
Γm
n ={(j 1,...,j m)|j 1 +···+j m =n, jℓ≥0},
ˆΓm
n ={(j 1,...,j m)|j 1 +···+j m =n, jℓ≥0 andj ℓ̸=n,for allℓ= 1,...,m}.
Whenmis apparent, we also use Γ n = Γm
n and ˆΓn = ˆΓm
n . Forn= 1 we may also omit the subscript.
Theorem 4.3.LetS= (R,α,β,µ)be an EYBO onV. LetΓ = Γ 3
