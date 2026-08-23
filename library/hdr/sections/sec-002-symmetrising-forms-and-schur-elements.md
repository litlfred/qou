---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-002-symmetrising-forms-and-schur-elements
section_title: "Symmetrising forms and Schur elements"
section_number: null
pages: 16-17
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "Hecke algebras, generalisations and representation theory — 27 sections: Algebras of Finite Type; Blocks; Symmetrising forms and Schur eleme"
---
A symmetrising form on the algebra A is a linear map τ :A→R such that
(a) τ(ab) =τ(ba) for all a,b∈A, that is, τ is a trace function, and
(b) the map ˆτ :A→ HomR(A,R ), a↦→ (x↦→τ(ax)) is an isomorphism of A-bimodules.
If there exists a symmetrising form on A, we say that A is a symmetric algebra.
Example 1.2 Let G be a ﬁnite group. The linear map τ : Z[G]→ Z deﬁned by τ(1) = 1 and τ(g) = 0
for all g∈G\{ 1} is a symmetrising form on Z[G]; it is called the canonical symmetrising form on Z[G].
13
Suppose that there exists a symmetrising form τ on A. Let B = (bi)i∈I be an R-basis of A, and
letB∨ = (b∨
i )i∈I denote the dual basis of A with respect to τ, that is, τ(bib∨
j ) = δij. Let K be a ﬁeld
containing R such that the algebra KA is split. The map τ can be extended to KA by extension of
scalars. Let V ∈ Irr(KA) with character χV . We have [GePf, Lemma 7.1.7]:
ˆτ−1(χV ) =
∑
i∈I
χV (bi)b∨
i ∈Z(KA) . (1.1)
For anyz∈Z(KA), Schur’s lemma implies that z acts as a scalar on V ; we denote this scalar by ωV (z).
The K-algebra homomorphism ωV :Z(KA)→K is the central character associated with V . We deﬁne
sV :=ωV (ˆτ−1(χV ))
to be the Schur element associated with V . We have sV ∈RK, where RK denotes the integral closure
of R in K [GePf, Proposition 7.3.9]. Moreover, note that the element sV satisﬁes:
sV χV (1) =
∑
i∈I
χV (bi)χV (b∨
i ) .
Example 1.3 Let G be a ﬁnite group and let τ be the canonical symmetrising form on A := Z[G].
The set {g}g∈G forms a basis of A over Z, with {g−1}g∈G the dual basis of A with respect to τ.
If K is an algebraically closed ﬁeld of characteristic 0, then KA is a split semisimple algebra and
sV =|G|/χV (1)∈ Q for all V ∈ Irr(KA). Because of the integrality of the Schur elements, we must
have|G|/χV (1)∈ ZK∩ Q = Z for all V ∈ Irr(KA). Thus, we have also shown that χV (1) divides|G|.
Now, the algebra KA is semisimple if and only if sV ⁄= 0 for all V ∈ Irr(KA) [GePf, Theorem 7.2.6].
If this is the case, we have
τ =
∑
V∈Irr(KA)
1
sV
χV (1.2)
and
eV = 1
sV
ˆτ−1(χV ), (1.3)
whereeV is the block-idempotent of KA corresponding to V . Both results are due to Curtis and Reiner
[CuRe], but we follow the exposition in [GePf, Theorem 7.2.6] and [GePf, Proposition 7.2.7] respectively.
Combining (1.1) with (1.3), and following the characterisation of blocks of the algebraA given in Section
1.1, we obtain the following description for the blocks of a symmetric algebra:
Proposition 1.4 LetK be a ﬁeld containing R such that the algebra KA is split semisimple. The blocks
of the symmetric algebra A are the non-empty subsets B of Irr(KA) that are minimal with respect to the
property: ∑
V∈B
1
sV
χV (a)∈R ∀a∈A.
