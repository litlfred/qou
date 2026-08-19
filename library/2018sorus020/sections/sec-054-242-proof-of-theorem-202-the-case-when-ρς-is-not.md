---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-054-242-proof-of-theorem-202-the-case-when-ρς-is-not
section_title: "Proof of theorem 2.0.2, the case when ρΣ is not resi-"
section_number: 2.4.2
pages: 73-74
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
dually abelian
In this section we prove Theorem 2.0.2 in the case whereρΣ is not residually abelian.
Thiscaseisthegenericcase,neverthelesscomputationalevidencessuggestthatthere
are many examples where it is not the case, hence we will treat the residually abelian
case in the next section.
Recall from Section 1.3.6 that there the splittingM =M1∪ΣM2 provides represen-
tations ρi :π1(Mi)→ SL2(k(Y )) with ρ1 convergent, andρ2 =Unρ′
2U−1
n , where the
matrix Un is (tn 0
0 1 ).
it induces the following Mayer-Vietoris exact sequence ofk(Y )-vector spacesH :
0→H1(M, Ad◦ρ)
(i∗
1,i∗
2)
−−−→H1(M1, Ad◦ρ1)⊕H1(M2, Ad◦ρ2)
j∗
1−j∗
2
−−−→H1(Σ, Ad◦ρΣ)
δ
− →H2(M, Ad◦ρ)→ 0
In this sequence the missing term on the leftH0(Σ, Ad◦ρ) is trivial becauseρΣ is not
abelian.Moreover,wecanconsiderthecomplexes: C∗(Σ, Ad◦ρΣ)andC∗(Mi, Ad◦ρi),
i = 1, 2, with their natural geometric basescΣ,c 1,c 2, and with a choice of bases
hΣ,h 1,h 2 of their homology groups. That allows us to deﬁne their torsiontor(Σ,h Σ),
72
tor(Mi,hi)∈ k(Y ). We pick any basis ofH1(M, Ad◦ρ), and againH as a basis of
H2(M, Ad◦ρ). Then we have the following theorem of Milnor [Mil66] :
Theorem 2.4.3.
tor(M, Ad◦ρ) = tor(M1) tor(M2)
tor(Σ) tor(H)∈ Ωk(Y )/k
This equality (and the left-hand side term) does not depend on the choice of bases
we made.
Proposition 2.4.4. The terms tor(M1), tor(M2) and tor(Σ) lie inO∗
v
Proof. Those factors are torsion of based complex ofk(Y )-vector spaces with based
homology, hence they lie ink(Y )∗ by deﬁnition. Since the representationsρ1, ρ′
2
andρΣ are convergent, one can deﬁne the complexes ofOv-modulesC∗(Σ, Ad◦ρΣ)v,
C∗(M1, Ad◦ρ1)v and C∗(M2, Ad◦ρ′
2)v with their homology groups. Moreover, we
could have chosen the basescΣ,c 1,c 2,h Σ,h 1,h 2 of the paragraph above to generate
those terms asOv-modules, because C∗(Σ, Ad◦ρΣ)v,...,H ∗(Mi, Ad◦ρi)v are free
Ov-modules (see Remark 2.4.5), and those choices do not aﬀect the computation of
the torsion. To be precise, we assume that we have chosen for instance a basish2
of the freeOv-module H1(M2, Ad◦ρ′
2)v that spansH1(M2, Ad◦ρ′
2) as ak(Y )-vector
space, and that it is mapped on a basis through the isomorphism ofk(Y )-vector
spaces H1(M2, Ad◦ρ′
2) → H1(M2, Ad◦ρ2). Finally, the mapH1(M1, Ad◦ρ1)v →
H1(Σ, Ad◦ρΣ)v identiﬁes the basish1 to a sub-basis ofhΣ.
Now we prove that the torsions of this complexes lie inO∗
v : let us perform the
computation for, say, M1. The complex is C0(M1, Ad◦ρ1)v
A
− →C1(M1, Ad◦ρ1)v.
SinceH0(M1, Ad◦ρ1)v is trivial, the matrixA is the matrix of an injectiveOv-linear
morphism. Moreover,H1(M, Ad◦ρ1)v is free, hence its determinant is an invertible
detA∈O∗
v as claimed.
Since tor(M1), tor(M2) and tor(Σ) take values inO∗
v, the valuation oftor(M, Ad◦ρ)
is determined by the torsion of the exact sequenceH.
Remark 2.4.5. 1. As we wish to compute the valuation of the torsion, it would
be better to study a complex ofOv-modules, having in mind Theorem 2.3.3.
That will be the ﬁrst step of the proof.
