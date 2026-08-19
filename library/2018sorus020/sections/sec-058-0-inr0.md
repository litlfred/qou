---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-058-0-inr0
section_title: "In−r0"
section_number: 0
pages: 76-79
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
)
is diagonal, wherer0 = dim kerA0, andIn−r0 is the(n−r0)
identity matrix. Then to computedetA, it’s enough to compute the determinant
of ther0×r0 ﬁrst block ofA1 +tA2.... More precisely detA = tr0 detA′
1 +o(tr0),
whereA′
1 is the restriction of∑tiAi+1 toH0(A0)⊗k[[t]], followed by the projection
k[[t]]n→H1(A0)⊗k[[t]].
One proceeds by induction, the argument is formalized in the following lemma :
Lemma 2.4.8. Let A :On
v →O n
v a morphism such that detA⁄= 0. Working in
the completion ˆOv if necessary, we deﬁneA≥0 = A,A≥i+1 = d
dtA≥i restricted to
75
H0(A≥i(0))⊗k[[t]] followed by the projectionk[[t]]n−∑i
k=0rk→ H1(A≥i(0))⊗k[[t]],
and ri = dim kerA≥i(0).
Then det(A) =t
∑ric, withc∈k∗.
Proof. Deﬁne the sequence(rn)n as in the lemma. AsdetA⁄= 0, there is ani0 such
that ri0 = 0. Take 0 < i≤ i0, after ﬁxing appropriated bases ofkerA≥i−1(0), one
writeA≥i(0)asadiagonalmatrix,with ri−1 zerosonthediagonal,and1’safter.Then
the classical formula for the determinant tells us thatdetA≥i =tri detA≥i+1+o(tri),
and the result follows by induction.
We will apply this lemma to the morphism∆2. Recall that forρ1,ρ′
2,ρ Σ : Γ →
SL2(Ov), we have the so-called residual representations ¯ρ1, ¯ρ2, ¯ρΣ : Γ → SL2(k)
taking values in the residual ﬁeldk. Moreover, ¯ρΣ = ¯ρ1,Σ =Unρ′
2,ΣU−1
n is reducible,
non abelian, thus we have as in Section 2.3.2 :
Lemma 2.4.9.The residual representations have the form
¯ρ1,Σ =
(
λ 0
λu1 λ−1
)
, ¯ρ2,Σ =
(
λ λ−1u2
0 λ−1
)
with λ∈H1(Σ,k∗),u 1∈H1(Σ,λ−2),u 2∈H1(Σ,kλ2) non trivial.
Proof. The expression of ¯ρ2,Σ follows from the conjugacy formulaρ1 = Unρ′
2U−1
n
when restricted onπ1(Σ), theui’s are non trivial because the residuals representa-
tions are not abelian.
The former sequence becomes residually¯H :
0→k
¯d1
− →H1(M1, Ad◦¯ρ1)⊕H1(M2, Ad◦¯ρ2)
¯D2
−→H1(Σ, Ad◦¯ρ1,Σ)
¯δ
− →k→ 0
with ¯d1(1) = (v1,v 2), and ¯D2(ζ1,ζ 2) =z2,ΣF, wherez2,Σ denotes the lower-left entry
of ζ2, restricted toπ1(Σ).
Again (see Section 2.3.2), the triangularity of the adjoint action of¯ρi,Σ provides the
following splittings :
0→K1→ Ad◦¯ρ1,Σ→kλ2→ 0
0→K2→ Ad◦¯ρ2,Σ→kλ−2→ 0
0→kλ−2→K1→k→ 0
76
and thus the exact sequences ofk-vector spaces :
0→H1(Σ,K 2)→H1(Σ, Ad◦¯ρ2,Σ)
p
− →H1(Σ,λ−2)→ 0
0→H0(Σ,k )→H1(Σ,λ−2)→H1(Σ,K 1)→H1(Σ,k )→ 0
and
0→H1(Σ,K 1)→H1(Σ, Ad◦¯ρ1,Σ)→...
We denote byj the compositionH1(Σ,λ−2)→H1(Σ,K 1)→H1(Σ, Ad◦¯ρ1,Σ).
Lemma 2.4.10.The spacekerj is one dimensional, more precisely, it is generated
by the image ofH0(Σ,k ) in H1(Σ, Ad◦¯ρ1,Σ), that is by∂1,ΣH =−2u1F.
Proof. We compute∂1,ΣH = ¯ρ1,ΣH ¯ρ−1
1,Σ−H, and obtain the claimed result.
The inclusion Σ⊂M2 induces i :H1(M2, Ad◦¯ρ2)→H1(Σ, Ad◦¯ρ2,Σ).
Lemma 2.4.11.The mapj◦p◦i :H1(M2, Ad◦¯ρ2)→H1(Σ, Ad◦¯ρ1,Σ) has a kernel
of dimension at least−χ(Σ)/2 + 1.
Proof. Notice that we knowdimH1(Σ, Ad◦¯ρΣ) =−3χ(Σ), dimH1(Σ,λ 2) =−χ(Σ)
and dimH1(Mi, Ad◦¯ρi) = −3/2χ(Σ). As p is onto, kerp has dimension equal to
dimH1(Σ, Ad◦¯ρ2,Σ)−dimH1(Σ,λ 2) =−3χ(Σ)−(−χ(Σ)) =−2χ(Σ). Ifiis injective
and if kerp and imi intersect transversally, thendim kerp∩ imi =−χ(Σ)/2. We
deﬁne the integers by the formuladim kerp∩ imi =−χ(Σ)/2 +s. Finally, by the
preceding lemma kerj has dimension 1. Moreover,p◦i(v2) = u1⁄= 0∈ kerj hence
the dimension ofker(j◦p◦i) =−χ(Σ)/2 + 1 +s. Ifs =−χ(Σ), thenp◦i = 0, but
u1⁄= 0, hence the result.
Now we can give a proof of Theorem 2.0.2 :
Proof. First we computer0, the dimension of the ﬁrst homology group of¯H, i.e.
H1( ¯H) = ker ¯D2/ im ¯d1. From the preceding lemma,dim ker ¯D2≥− χ(Σ)/2 + 1 +
(−3/2χ(Σ)) = −2χ(Σ) + 1. Hence r0 ≥ −2χ(Σ). Now the higher order maps
di
dit|t=0(D2), for i = 1,...,n − 1, remains zero when restricted to ker( ¯D2), hence
each ri,i = 1,...,n − 1 is greater than−2χ(Σ). Let r = ∑
i≥nri, we have from
Lemma 2.4.8 thatdet(D2)≥− 2nχ(Σ) +r, andv(tor(Ht))≤ 2nχ(Σ). Finally, ob-
serve that tn rk(d2) tor(Ht) = tor(H). Since rk(d2) = −3χ(Σ)− 1, the theorem is
proved.
77
